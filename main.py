#!/bin/python


import folium
def inisiasi(long,lat):
	m = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')
	return m
	
def hitam(long,lat):
	c = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Toner')	
	return c

def masukkin(apa,ini):
	d = folium.Map(
	location=[apa,ini],
	zoom_start=12,
    tiles='Stamen Terrain')	
	return d
	
def simpan(anu,gede):
	anu.save(gede)

d = masukkin(-6.966667, 110.416667)
c = hitam(-6.966667, 110.416667)
m = inisiasi(-6.966667, 110.416667)
tooltip = 'Click me!'



folium.Marker([-7.021435, 110.460825], popup='<i>Universitas Muhammadiyah Semarang</i>').add_to(m)
folium.Marker([-7.024314, 110.461330], popup='<i>UMMAH Aceh & Melayu Culinary</i>').add_to(m)
folium.Marker([-7.024615, 110.467166], popup='<i>GREAT COFFEE 1987 SEMARANG</i>').add_to(m)
folium.Marker([-7.027426, 110.470685], popup='<i>RUMAH INGGRIS GAK 15</i>').add_to(m)
folium.Marker([-7.033836, 110.466683], popup='<i>RSUD K.R.M.T. Wongsonegoro Semarang</i>').add_to(m)
folium.Marker([-7.021221, 110.463669], popup='<i>Waterpark Semawis</i>').add_to(m)
folium.Marker([-7.020224, 110.465478], popup='<i>Garce Gultar Galerry</i>').add_to(m)
folium.Marker([-7.032059, 110.456388], popup='<i>PLN Undiklat Semarang</i>').add_to(m)
folium.Marker([-7.036866, 110.456578], popup='<i>Citra Grand Semarang</i>').add_to(m)
folium.Marker([-7.030471, 110.455194], popup='<i>Pusdiklat PAlang Merah Indonesia Jawa Tengah</i>').add_to(m)
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
folium.Marker([-7.024245, 110.418597], popup='<i>Karangrejo</i>').add_to(m)
folium.Marker([-7.038990, 110.410235], popup='<i>Gombel Golf Semarang</i>').add_to(m)
folium.Marker([-7.051899, 110.400286], popup='<i>Lapangan Atletik UNNES</i>').add_to(m)
folium.Marker([-7.047619, 110.394267], popup='<i>Masjid Ulul Albab</i>').add_to(m)
folium.Marker([-7.049780, 110.392475], popup='<i>Universitar Library UNNES</i>').add_to(m)
folium.Marker([-7.046894, 110.394556], popup='<i>Lapangan Banaran</i>').add_to(m)
folium.Marker([-7.045276, 110.392518], popup='<i>Citra Garden</i>').add_to(m)
folium.Marker([-7.044658, 110.391273], popup='<i>Planet ban Hemat</i>').add_to(m)
folium.Marker([-7.044839, 110.391906], popup='<i>The T-co</i>').add_to(m)
folium.Marker([-7.042646, 110.388612], popup='<i>Ayodya</i>').add_to(m)
folium.Marker([-6.994899, 110.461150], popup='<i>Harian Semarang</i>').add_to(m)
folium.Marker([-6.995750, 110.455224], popup='<i>Sekolah Dasar Negeri Kalicari 02</i>').add_to(m)
folium.Marker([-6.992854, 110.455271], popup='<i>Omah Gading Guest House</i>').add_to(m)
folium.Marker([-6.996453, 110.461376], popup='<i>Sekolah Tinggi Maritim dan Transpor AMNI</i>').add_to(m)
folium.Marker([-6.997071, 110.463017], popup='<i>BPJS Ketenagakerjaan Kantor Cab Smg II</i>').add_to(m)
folium.Marker([-6.998328, 110.463961], popup='<i>Coca-Cola Amatil Indonesia</i>').add_to(m)
folium.Marker([-7.000149, 110.458908], popup='<i>SD ISLAM PRIMADANA</i>').add_to(m)
folium.Marker([-7.002340, 110.461924], popup='<i>SMP ISLAM TERPADU PAPB</i>').add_to(m)
folium.Marker([-7.003860, 110.459362], popup='<i>Rumah Bersalin Citra Insani</i>').add_to(m)
folium.Marker([-7.002099, 110.454033], popup='<i>Masjid Baitun Nur</i>').add_to(m)
folium.Marker([-6.972907, 110.436526], popup='<i>Panti Sosial Tresna Werdha Bethany Bala Keselamatan</i>').add_to(m)
folium.Marker([-6.972552, 110.435656], popup='<i>PT. Mutual Medica</i>').add_to(m)
folium.Marker([-6.972278, 110.435331], popup='<i>Lapis Legit Niki Sae</i>').add_to(m)
folium.Marker([-6.972374, 110.436377], popup='<i>Vanni Bengkel</i>').add_to(m)
folium.Marker([-6.971751, 110.436136], popup='<i>Kumon Indonesia-Senjoyo Indah</i>').add_to(m)
folium.Marker([-6.971985, 110.435425], popup='<i>Lina Catering</i>').add_to(m)
folium.Marker([-6.971884, 110.434910], popup='<i>Petruk Mie Jowo</i>').add_to(m)
folium.Marker([-6.972172, 110.434577], popup='<i>Ayam Goreng Rasa Sama</i>').add_to(m)
folium.Marker([-6.972957, 110.436849], popup='<i>Toko Tiara</i>').add_to(m)
folium.Marker([-6.972864, 110.436577], popup='<i>Omah Sae</i>').add_to(m)
folium.Marker([-7.020742, 110.374764], popup='<i>Universitas Wahid Hasyim Fak. Kedokteran</i>').add_to(m)
folium.Marker([-7.025518, 110.374587], popup='<i>Green Farm</i>').add_to(m)
folium.Marker([-7.025326, 110.372017], popup='<i>RS B. Permata Sari</i>').add_to(m)
folium.Marker([-7.038576, 110.351016], popup='<i>Obyek Wisata Goa Kreo</i>').add_to(m)
folium.Marker([-7.061661, 110.365337], popup='<i>Dinas Kesehatan Kota Semarang</i>').add_to(m)
folium.Marker([-7.051362, 110.438237], popup='<i>Teknik Arsitektur Undip</i>').add_to(m)
folium.Marker([-7.051192, 110.436000], popup='<i>Fakultas Hukum Universitas Diponegoro</i>').add_to(m)
folium.Marker([-7.052321, 110.435528], popup='<i>Politeknik Negeri Semarang (POLINES)</i>').add_to(m)
folium.Marker([-7.054382, 110.432555], popup='<i>SPBU Undip</i>').add_to(m)
folium.Marker([-7.054964, 110.428407], popup='<i>Poltekkes Kemenkes Semarang</i>').add_to(m)
folium.Marker([-7.054607, 110.429340], popup='<i>Jurusan Keperawatan Gigi</i>').add_to(m)
folium.Marker([-7.058942, 110.488909], popup='<i>Brown Canyon</i>').add_to(m)
folium.Marker([-6.966962, 110.427719], popup='<i>Badan Pusat Statistik Kabupaten Semarang</i>').add_to(m)
folium.Marker([-6.967340, 110.426914], popup='<i>Taman Garuda</i>').add_to(m)
folium.Marker([-6.983949, 110.410367], popup='<i>Lawang Sewu</i>').add_to(m)
folium.Marker([-6.984479, 110.410831], popup='<i>Dp Mall Maxx Coffe</i>').add_to(m)
folium.Marker([-6.989198, 110.406663], popup='<i>Gereja Sub Tutela Matris</i>').add_to(m)
folium.Marker([-7.130024, 110.389404], popup='<i>Watu Gunung</i>').add_to(m)
folium.Marker([-7.129313, 110.384602], popup='<i>Kolam Renang Bukit Lereng Indah</i>').add_to(m)
folium.Marker([-7.151226, 110.398894], popup='<i>Glory Face Monkey</i>').add_to(m)
folium.Marker([-7.174177, 110.399010], popup='<i>Makam Syekh Penanggalan</i>').add_to(m)
folium.Marker([-6.945110, 110.398248], popup='<i>Pantai Baruna</i>').add_to(m)
folium.Marker([-6.948695, 110.410332], popup='<i>Pantai Cipta</i>').add_to(m)
folium.Marker([-6.961821, 110.390419], popup='<i>prpp Gedung Merbabu</i>').add_to(m)
folium.Marker([-6.960973, 110.386271], popup='<i>Grand Marakaca</i>').add_to(m)
folium.Marker([-6.960171, 110.389507], popup='<i>Gedung Merapi</i>').add_to(m)
folium.Marker([-6.957529, 110.392074], popup='<i>Marina Beach Karaoke & Lounge</i>').add_to(m)
folium.Marker([-6.954527, 110.358967], popup='<i>Pantai Tirang</i>').add_to(m)
folium.Marker([-6.958307, 110.360467], popup='<i>Mangrove Edu Park</i>').add_to(m)
folium.Marker([-6.964427, 110.427933], popup='<i>Semarang Tawang</i>').add_to(m)
folium.Marker([-6.961189, 110.435932], popup='<i>SPBU Pertamina</i>').add_to(m)
folium.Marker([-6.962435, 110.456930], popup='<i>HNR Optima</i>').add_to(m)
folium.Marker([-6.961839, 110.456244], popup='<i>Talenta Electroplating</i>').add_to(m)
folium.Marker([-6.961785, 110.456544], popup='<i>Indo Karya Glassco PD</i>').add_to(m)
folium.Marker([-6.963042, 110.455890], popup='<i>Toko Pojok</i>').add_to(m)
folium.Marker([-6.963053, 110.456255], popup='<i>PT.Anugrah Pradipta</i>').add_to(m)
folium.Marker([-6.963053, 110.456480], popup='<i>Bina Aluminium</i>').add_to(m)
folium.Marker([-6.962872, 100.456072], popup='<i>Adhi Putra</i>').add_to(m)
folium.Marker([-6.963031, 110.456845], popup='<i>PT.Lola Mina</i>').add_to(m)
folium.Marker([-6.963042, 110.457048], popup='<i>CV.Varia</i>').add_to(m)
folium.Marker([-6.963010, 110.457295], popup='<i>Artha Niaga Transport</i>').add_to(m)
folium.Marker([-6.971136, 110.436155], popup='<i>CV.Sari Nastiti</i>').add_to(m)
folium.Marker([-7.105307, 110.408505], popup='<i>Toko Ratu</i>').add_to(m)
folium.Marker([-7.103132, 110.406899], popup='<i>Wawik Ice n Coffee</i>').add_to(m)
folium.Marker([-7.102299, 110.407639], popup='<i>PAUD Bakti</i>').add_to(m)
folium.Marker([-7.102759, 110.407477], popup='<i>KB Bhakti</i>').add_to(m)
folium.Marker([-6.971038, 110.434834], popup='<i>Anantha Salon</i>').add_to(m)
folium.Marker([-6.970752, 110.435919], popup='<i>RM.Cik Gwat</i>').add_to(m)
folium.Marker([-6.971347, 110.436010], popup='<i>Miracle Cell</i>').add_to(m)
folium.Marker([-6.970526, 110.436071], popup='<i>SMPN 2 Penawangan</i>').add_to(m)
folium.Marker([-6.971143, 110.436822], popup='<i>CV.Aneka Teknik Baru</i>').add_to(m)
folium.Marker([-7.000297, 110.403791], popup='<i>Bank Mandiri Sampangan</i>').add_to(m)
folium.Marker([-6.997416, 110.401865], popup='<i>ATM Mandiri</i>').add_to(m)
folium.Marker([-6.997480, 110.399655], popup='<i>Sekolah Dasar Islam Terpadu Al Qolam</i>').add_to(m)
folium.Marker([-6.996527, 110.402171], popup='<i>Gudeg Rahayu</i>').add_to(m)
folium.Marker([-6.966454, 110.402456], popup='<i>SMK Negeri 10 Semarang</i>').add_to(m)
folium.Marker([-6.975793, 110.439845], popup='<i>Garuda</i>').add_to(m)
folium.Marker([-6.975072, 110.439384], popup='<i>Kedai Maria Qua</i>').add_to(m)
folium.Marker([-6.975602, 110.440352], popup='<i>Bakso Paka Alex</i>').add_to(m)
folium.Marker([-6.975117, 110.439934], popup='<i>Lestari Private</i>').add_to(m)
folium.Marker([-6.974640, 110.438896], popup='<i>Arvia Jaya Fashion</i>').add_to(m)
folium.Marker([-6.974874, 110.438373], popup='<i>Klinik Bersalin Hertinawati</i>').add_to(m)
folium.Marker([-6.975092, 110.438089], popup='<i>Fortuna Apotik</i>').add_to(m)
folium.Marker([-6.975092, 110.439081], popup='<i>Qstin catering</i>').add_to(m)
folium.Marker([-6.974996, 110.437845], popup='<i>Warteg Aero</i>').add_to(m)
folium.Marker([-6.973435, 110.441660], popup='<i>Ikura Toko</i>').add_to(m)
folium.Marker([-6.966403, 110.403448], popup='<i>TK. Bu Surati</i>').add_to(m)
folium.Marker([-6.966253, 110.401638], popup='<i>Bengkel Tambal Ban Pak Mali</i>').add_to(m)
folium.Marker([-6.967539, 110.402411], popup='<i> Gloria Toko</i>').add_to(m)
folium.Marker([-6.967265, 110.403170], popup='<i>Toko bu Surati</i>').add_to(m)
folium.Marker([-6.967573, 110.403298], popup='<i>Warung Makan</i>').add_to(m)
folium.Marker([-6.966604, 110.403958], popup='<i>Mulya Manunggal Meubel</i>').add_to(m)
folium.Marker([-6.966785, 110.403956], popup='<i>Balai Latihan Kerja Luar Negeri (BLKLN)</i>').add_to(m)
folium.Marker([-6.966743, 110.404589], popup='<i>PT, Mercusuar Abadi Jaya</i>').add_to(m)
folium.Marker([-6.966724, 110.404323], popup='<i>Koperasi Karya Manunggal</i>').add_to(m)
folium.Marker([-6.967243, 110.404374], popup='<i>Andalan Tehnik CV</i>').add_to(m)
folium.Marker([-6.966863, 110.405120], popup='<i>Musholla Al Huda</i>').add_to(m)
folium.Marker([-6.966051, 110.403953], popup='<i>Sido Sehat</i>').add_to(m)
folium.Marker([-6.965241, 110.403526], popup='<i>Pulau Harapan</i>').add_to(m)
folium.Marker([-6.963745, 110.401860], popup='<i>Anugerah Mandiri Trans. PT</i>').add_to(m)
folium.Marker([-6.963875, 110.401710], popup='<i>Gereja Katolik Hati Kudus Yesus Semarang Tanah Mas</i>').add_to(m)
folium.Marker([-6.962908, 110.401943], popup='<i>Super-Vit</i>').add_to(m)
folium.Marker([-6.963358, 110.402394], popup='<i>Blessed Wholesale</i>').add_to(m)
folium.Marker([-6.963042, 110.402667], popup='<i>Masjid Annur</i>').add_to(m)
folium.Marker([-6.963159, 110.403281], popup='<i>Masjid An-Nur</i>').add_to(m)
folium.Marker([-6.963164, 110.403665], popup='<i>Digini Studio</i>').add_to(m)
folium.Marker([-6.963982, 110.403670], popup='<i>Rani Creation</i>').add_to(m)
folium.Marker([-6.968187, 110.427871], popup='<i>Taman Srigunting</i>').add_to(m)
folium.Marker([-6.968310, 110.427413], popup='<i>PT.Fabamus Famili Utama</i>').add_to(m)
folium.Marker([-6.968739, 110.426419], popup='<i>Semarang Kreatif Galeri</i>').add_to(m)
folium.Marker([-6.969289, 110.426426], popup='<i>Tanah Air NV Co</i>').add_to(m)
folium.Marker([-6.969319, 110.426085], popup='<i>Dewi Batik</i>').add_to(m)
folium.Marker([-6.968800, 110.425865], popup='<i>Wartel Matel</i>').add_to(m)
folium.Marker([-6.968822, 110.425516], popup='<i>Kantor Phapros Kota Lama</i>').add_to(m)
folium.Marker([-6.969154, 110.425903], popup='<i>PT.Lautan Mutiara Sewu</i>').add_to(m)
folium.Marker([-6.968980, 110.426760], popup='<i>Gorontalo Express</i>').add_to(m)
folium.Marker([-6.969184, 110.427155], popup='<i>PT.Masaji Prakasa Cargo</i>').add_to(m)
folium.Marker([-7.338247, 110.184986], popup='<i>Pikatan Water Park</i>').add_to(m)
folium.Marker([-7.340311, 110.185158], popup='<i>Tirtamas Megah. PT</i>').add_to(m)
folium.Marker([-7.361299, 110.191155], popup='<i>Beyond Water Dewi</i>').add_to(m)
folium.Marker([-7.356628, 110.189353], popup='<i>KANTOR KECAMATAN TEMBARAK</i>').add_to(m)
folium.Marker([-7.352665, 110.191692], popup='<i>Curug Titang</i>').add_to(m)
folium.Marker([-7.372926, 110.182589], popup='<i>Ganjuran Indah Farm Divisi Kidul Cepit</i>').add_to(m)
folium.Marker([-7.372213, 110.181709], popup='<i>Kud Sumbing</i>').add_to(m)
folium.Marker([-7.379246, 110.173072], popup='<i>Kantor Kecamatan Selopampang</i>').add_to(m)
folium.Marker([-7.378022, 110.168751], popup='<i>Pasar Selopampang</i>').add_to(m)
folium.Marker([-7.378925, 110.185946], popup='<i>Kantor Desa Gambasan</i>').add_to(m)
folium.Marker([-6.984886, 110.410179]).add_to(m)
folium.Marker([-6.985120, 110.408709]).add_to(m)
folium.Marker([-6.982894, 110.404535]).add_to(m)
folium.Marker([-6.978538, 110.409609]).add_to(m)
folium.Marker([-6.975322, 110.409952]).add_to(m)
folium.Marker([-6.971925, 110.409866]).add_to(m)
folium.Marker([-6.970626, 110.411035]).add_to(m)
folium.Marker([-6.970296, 110.412859]).add_to(m)
folium.Marker([-6.971968, 110.408417]).add_to(m)
folium.Marker([-6.971105, 110.409790]).add_to(m)
folium.Marker([-6.961003, 110.386307]).add_to(m)
folium.Marker([-6.961264, 110.386570]).add_to(m)
folium.Marker([-6.960534, 110.386093]).add_to(m)
folium.Marker([-6.961402, 110.385422]).add_to(m)
folium.Marker([-6.960859, 110.385272]).add_to(m)
folium.Marker([-6.960263, 110.386747]).add_to(m)
folium.Marker([-6.960694, 110.386892]).add_to(m)
folium.Marker([-6.960444, 110.387466]).add_to(m)
folium.Marker([-6.957899, 110.385910]).add_to(m)
folium.Marker([-6.958921, 110.386672]).add_to(m)

folium.RegularPolygonMarker(
    [-7.012746, 110.417792],
    popup='Indomaret Candi',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.012211, 110.416814],
    popup='PT. Jasa Raharja Persero Jawa Tengah',
    fill_color='#45647d',
    number_of_sides=4,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.007835, 110.416380],
    popup='Taman Diponegoro',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.006216, 110.416874],
    popup='Jonas Photo Studio Semarang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.026276, 110.409497],
    popup='Gor Jatidiri',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.019195, 110.409572],
    popup='Stadion taruna Bhayangkara Akpol',
    fill_color='#45647d',
    number_of_sides=4,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.016587, 110.409771],
    popup='Rumah sakit Bhayangkara Akpol',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.014521, 110.404857],
    popup='Oak Tree Emerald Semarang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.012221, 110.406810],
    popup='Kangen Water',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.007888, 110.408859],
    popup='PT PLN Persero Pusat Manajemen Konstruksi',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.987817, 110.397154],
    popup='Gereja Katholik Santa Teresia',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.988027, 110.396282],
    popup='PT Lubrindo Suwardhana',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.989238, 110.395794],
    popup='DERMA CLINIC',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.988507, 110.393613],
    popup='Virgin Cake & Bakery',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.988379, 110.392371],
    popup='Gedung Dekopin',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.988265, 110.392140],
    popup='Jamkrindo Kanca Semarang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.990645, 110.393572],
    popup='Flochi Hostel',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.992900, 110.396289],
    popup='Griya Paseban',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.995733, 110.398974],
    popup='Kimia Farma. PT Persero',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-7.206718, 110.424440],
    popup='Cimory On The Valley',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.957899, 110.385910],
    popup='Istana Teknik PD',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.957899, 110.385910],
    popup='Gosyen Badminton Courts',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.957899, 110.385910],
    popup='Hotel Fovere Bandara Semarang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
folium.RegularPolygonMarker(
    [-6.967195, 110.390409],
    popup='CV. Indoreka Buana Mandiri',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(m)
m

	
folium.Circle(
    radius=100,
    location=[-7.002457, 110.387132],
    popup='Bukit Wahid',
    color='crimson',
    fill=False,
).add_to(c)
c


folium.Marker(
    location=[-7.010464, 110.441225],
    popup='Pasar Mrican',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.009991, 110.441950],
    popup='Bakso Beranak Mekar Sari',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.010449, 110.441955],
    popup='Pondok Bakmi Ayu Bu Tarno',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.011109, 110.442733],
    popup='Gudang Gypsum',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.011285, 110.442390],
    popup='Asrama TNI-AD Mrican',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.011258, 110.443624],
    popup='Fingerspot',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.011559, 110.444750],
    popup='Polsek Banyumanik',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.010753, 110.446082],
    popup='Baby Shop J N C',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.006419, 110.446457],
    popup='Kantor Urusan Agama',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.006254, 110.445886],
    popup='Polsek Semarang Selatan',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.022648, 110.700036],
    popup='Api Abadi Mrapen',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.020880, 110.701205],
    popup='Polsek Kebonagung',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.023851, 110.709048],
    popup='SMP N 1 Kebonagung',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.025885, 110.713425],
    popup='Balai Desa Mijen',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.037728, 110.727680],
    popup='PT. HARY BAROKAH',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.337385, 110.187593],
    popup='Total Air Minum Temanggung Tirtamas',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.336695, 110.182046],
    popup='Taman Makam Pahlawan Prayudha',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.338291, 110.184846],
    popup='Temanggung',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.318208, 110.024637],
    popup='Taman Wisata Alam Posong',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-7.044734, 110.726768],
    popup='Balai Desa Karanggeneng',
    icon=folium.Icon(icon='cloud')
).add_to(d)
d


simpan(m,'4.html')
simpan(c,'5.html')
simpan(d,'6.html')
