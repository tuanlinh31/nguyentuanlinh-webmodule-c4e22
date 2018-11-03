from river import River

import mlab


mlab.connect()

rivers_list = River.objects()
for p in rivers_list:
    if p.continent == "Africa":
        print(p.name)
        print("**************************")