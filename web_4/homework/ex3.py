from river import River
import mlab

mlab.connect()

rivers_list = River.objects(length__lt=1000)

for p in rivers_list:
    if p.continent == "S.America":
        print(p.name)
        print("********************************")