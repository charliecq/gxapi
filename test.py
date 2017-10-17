import geosoft.gxapi_cy as gc


c = gc.WrapPGeo("a", "1.0", 0, 0)
try:
#    print("Hit Enter to continue")
#    input()
    dn = gc.Wrap3DN.create()
    try:
        print(dn)

        print(dn.get_render_controls(9,9,"".encode(),"".encode(),"".encode()))
        print(dn.set_render_controls(0,0,"a".encode(),"v".encode(),"x".encode()))
        print(dn.get_render_controls(9,9,"".encode(),"".encode(),"".encode()))
    finally:
        del dn
finally:
    del c