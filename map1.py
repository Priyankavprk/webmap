import folium
import pandas

data = pandas.read_csv("webmap/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def getIconColor(elev):
    if elev < 1000:
        return "green"
    elif elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m", fill_color=getIconColor(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("webmap/world.json", "r", encoding='UTF-8-sig').read(), 
style_function=lambda x: {'fillColor': "green" if x['properties']['POP2005'] < 10000000 
else "orangle" if 10000000 <= x['properties']['POP2005'] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("webmap/Map1.html")