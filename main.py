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
folium.Marker([-7.025329, 110.434279], popup='<i>Water Blaster Golf Residance</i>').add_to(m)
folium.Marker([-7.025281, 110.438463], popup='<i>Graha Candi Golf Club</i>').add_to(m)
folium.Marker([-7.028361, 110.434418], popup='<i>Sekolah Menengah Pertama Negeri 17 Semarang</i>').add_to(m)
folium.Marker([-7.030011, 110.432669], popup='<i>Area Hijau Jangli</i>').add_to(m)
folium.Marker([-7.028009, 110.428512], popup='<i>Pasar Jangli</i>').add_to(m)
folium.Marker([-7.026490, 110.428356], popup='<i>Bank Rakyat Indonesia</i>').add_to(m)
folium.Marker([-7.026748, 110.427895], popup='<i>Kantor Kecamatan Candisari</i>').add_to(m)
folium.Marker([-7.026913, 110.426980], popup='<i>Masjid Al - Falah</i>').add_to(m)
folium.Marker([-7.026512, 110.425025], popup='<i>Satya Wirawicaksana</i>').add_to(m)
folium.Marker([-7.024912, 110.424427], popup='<i>Inara Tour Travel</i>').add_to(m)

m
