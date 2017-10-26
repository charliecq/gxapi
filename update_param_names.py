import re
import os
import glob
import itertools
from collections import defaultdict
import codecs

spec_files = glob.glob('spec/core/*.py')
spec_files.extend(glob.glob('spec/desk/*.py'))


rew = re.compile('GS_EXPDLL[^\(]+\([^)]+\)', re.MULTILINE)
rec = re.compile('//.*')

recamel1 = re.compile('(.)([A-Z][a-z]+)')
recamel2 = re.compile('([a-z0-9])([A-Z])')

def convert_camel_case(name):
	s1 = recamel1.sub(r'\1_\2', name)
	s2 = recamel2.sub(r'\1_\2', s1).lower()
	return s2.replace("3_d", "_3d")

funclookup = defaultdict(list)

gxx_files = glob.glob('e:/ggit/t/core/**/gxx_*.c', recursive=True)
gxx_files.extend(glob.glob('e:/ggit/t/core/**/gxx_*.cpp', recursive=True))
gxx_files.extend(glob.glob('e:/ggit/t/desk/**/gxx_*.c', recursive=True))
gxx_files.extend(glob.glob('e:/ggit/t/desk/**/gxx_*.cpp', recursive=True))

for gxx_file in gxx_files:
    with open(gxx_file, 'r') as f:
         gxx_source = f.read()

    funcs = [' '.join(rec.sub('', match[0]).split())
                .replace('const double*','')
                .replace('const char*','')
                .replace('const long*','')
                .replace('const double *','')
                .replace('const char *','')
                .replace('const long *','')
                .replace('long*','')
                .replace('double*','')
                .replace('char*','')
                .replace('long *','')
                .replace('double *','')
                .replace('char *','')
                .replace('H_GXX* hGXX','')
                .replace('H_GXX *hGXX','')
                .replace('H_GXX *','')
                .replace('H_GXX*','')
                .replace('GS_EXPDLL ','')
                .replace('(',' ')
                .replace(')','')
                .replace(',','')
                .split()
                for match in rew.finditer(gxx_source)]

    for f in funcs:
        params = [p[2:] if len(p) > 2 and (p.startswith("pl") or p.startswith("pd") or p.startswith("pc") or p.startswith("sz")) else p for p in f[1:]]
        params = [convert_camel_case(p) for p in params]
        params = ['val' if (p == 'pl' or p == 'pd') and 'val' not in params else p for p in params]
        params = ['str_val' if (p == 'pc' or p == 'sz' or p == 'str' or p == 'string') and 'str_val' not in params else p for p in params]
        params = ['_{}'.format(p) if p[0] >= '0' and p[0] <= '9' else p for p in params]
        params = ['lda' if p == 'lambda' and 'lda' not in params else p for p in params]
        
        funclookup[f[0]] = params


sources = defaultdict(list)

for file in spec_files:
    parts = file.replace('/', '.').replace('\\', '.').split('.')
    parts.pop()
    gx_cl = parts.pop()

    with open(file, 'r') as f:
         sources[gx_cl] = [file, f.read()]

for func, params in funclookup.items():
    cl = func[func.rfind('_')+1:]
    if len(params) > 0 and cl in sources.keys():
        method_re = "(\(\'{}\'[^\[]*?\[.*\s)(.*Parameter\(\')(p{})((?:.*\n)*?(?:.*\),?\n))".format(func, 1)
        replace_str = r'\1\2{}\4'.format(params[0])
        group_pos = 5
        for i in range(1, len(params)):
            method_re += "(.*Parameter\(\')(p{})((?:.*\n)*?(?:.*\),?\n))".format(i + 1)
            replace_str += r'\{}{}\{}'.format(group_pos, params[i], group_pos + 2)
            group_pos = group_pos + 3

        reg_func = re.compile(method_re, re.MULTILINE)
        sources[cl][1] = reg_func.sub(replace_str, sources[cl][1])

for cl, pair in sources.items():
    with open(pair[0], 'w') as f:
        f.write(pair[1])
