import folium

mapa = folium.Map(location=[52.2297, 21.8122], zoom_start=13)

folium.Marker(location=[52.2297, 21.8122], popup='Warszawa').add_to(mapa)

mapa.save('mapa.html')
