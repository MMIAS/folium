#!/bin/python


import folium

m = folium.Map(
    location=[-6.966667, 110.416667],
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'

folium.Marker([-6.971730, 110.424165], popup='<i>Pasar Johar</i>').add_to(m)
folium.Marker([-6.993648, 110.407317], popup='<i>RSUP Dr. KARIADI</i>').add_to(m)
folium.Marker([-6.955928, 110.460815], popup='<i>Sultan Agung Islamic hospital</i>').add_to(m)
folium.Marker([-6.983722, 110.445570], popup='<i>Masjid Agung Jawa Tengah</i>').add_to(m)
folium.Marker([-6.990504, 110.422951], popup='<i>Kawasan Simpang Lima</i>').add_to(m)
folium.Marker([-6.978714, 110.378570], popup='<i>Bandar Udara Internasional Ahmad Yani</i>').add_to(m)
folium.Marker([-6.990593, 110.423723], popup='<i>ATM Bank BJB Citraland Semarang</i>').add_to(m)
folium.Marker([-6.975235, 110.426991], popup='<i>Bank Sinarmas</i>').add_to(m)
folium.Marker([-6.968443, 110.425948], popup='<i>Kota Lama Semarang</i>').add_to(m)
folium.Marker([-6.948832, 110.389341], popup='<i>Pantai Marina</i>').add_to(m)

m
