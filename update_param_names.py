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
    name = recamel1.sub(r'\1_\2', name)
    name = recamel2.sub(r'\1_\2', name).lower()
    name = name.replace("3_d", "_3d")
    if name.startswith("_3d"):
        return "o{}".format(name[1:])
    else:
        return name

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
                .replace('const void*','')
                .replace('const char *','')
                .replace('const long *','')
                .replace('const void *','')
                .replace('HWND','')
                .replace('HDC','')
                .replace('long*','')
                .replace('double*','')
                .replace('char*','')
                .replace('void*','')
                .replace('long *','')
                .replace('double *','')
                .replace('char *','')
                .replace('void *','')
                .replace('long ','')
                .replace('void ','')
                .replace('H_GXX* hGXX','')
                .replace('H_GXX *hGXX','')
                .replace('H_GXX *','')
                .replace('H_GXX*','')
                .replace('GS_EXPDLL ','')
                .replace('(',' ')
                .replace(')','')
                .replace(',','')
                .replace('*','')
                .split()
                for match in rew.finditer(gxx_source)]

    for f in funcs:
        params = [p[2:] if len(p) > 2 and (p.startswith("pl") or p.startswith("pd") or p.startswith("pc") or p.startswith("sz")) else p for p in f[1:]]
        if len(params) > 0:
            params = [convert_camel_case(p) for p in params]
            params = ['val' if (p == 'pl' or p == 'pd') and 'val' not in params else p for p in params]
            params = ['str_val' if (p == 'pc' or p == 'sz' or p == 'str' or p == 'string') and 'str_val' not in params else p for p in params]
            params = ['v{}'.format(p) if p[0] >= '0' and p[0] <= '9' else p for p in params]
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
    if cl in sources.keys():
        for match in re.finditer(r"Method\(\'{}\'([^\n]*\n)+?.*Parameter\(\'[^\]]*?\]\),".format(func, 1), sources[cl][1], re.MULTILINE):
            func_def = match[0]
            repl_def = func_def
            should_replace = False
            for i in range(0, len(params)):
                param_name = "Parameter('p{}'".format(i + 1)
                if repl_def.find(param_name) > 0:
                    should_replace = True
                    repl_def = repl_def.replace(param_name, "Parameter('{}'".format(params[i]))
            if should_replace:
                sources[cl][1] = sources[cl][1].replace(func_def, repl_def)
            break

for cl, pair in sources.items():
    with open(pair[0], 'w') as f:
        f.write(pair[1])
