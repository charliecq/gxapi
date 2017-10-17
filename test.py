import geosoft.gxapi_cy as gc
import geosoft.gxapi as ga


c = gc.WrapPGeo("a", "1.0", 0, 0)
try:
#    print("Hit Enter to continue")
#    input()
    dn = gc.Wrap3DN.create()
    try:
        print(dn)

        print(dn.get_render_controls(9,9,"","",""))
        print(dn.set_render_controls(0,0,"a","v","x"))
        print(dn.get_render_controls(9,9,"","",""))
    finally:
        del dn
finally:
    del c