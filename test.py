import geosoft.gxapi_cy as gc
import geosoft.gxapi as ga

c = gc.WrapPGeo("a", "1.0", 0, 0)

print("Hit Enter to continue")
input()
dn = gc.Wrap3DN.create()

print(dn)

print(dn.get_point_of_view(1,2,3))