
import folium
from folium.plugins import LocateControl
import webbrowser
import cgitb 
cgitb.enable()

# centers map on simrall
m0 = folium.Map(width="50%", location=[33.4526221, -88.7872477], zoom_start=100)
LocateControl().add_to(m0)
folium.ClickForLatLng().add_to(m0)
m0.save("map_index.html")


# modify html here



# open web browser
webbrowser.open_new_tab('map_index.html')

#x an y coord
x1 = float(input("Enter The Starting Position North:"))
x2 = float(input("Enter The Starting Position West:"))
y1 = float(input("Enter The Ending Position North:"))
y2 = float(input("Enter The Starting Position West:"))
x = (x1, x2)
y = (y1, y2)

m = folium.Map(location = [x1,x2],zoom_start=17) #creating masking layer via direct
LocateControl().add_to(m)
loc =[x,y]
folium.LatLngPopup().add_to(m)
folium.Marker([x1,x2],tooltip="<i>Starting Position</i>").add_to(m)
folium.Marker([y1,y2],tooltip="<i>Ending Position</i>").add_to(m)
folium.PolyLine(loc,color='blue', weight=10).add_to(m)

m.save("map_index.html")
webbrowser.open_new_tab('map_index.html')
