import streamlit as st
st.title("🚗 Sistem Rekomendasi Mobil")
st.write("Sistem Cerdas berbasis Rule (IF-ELSE)")

pilihan_budget = st.selectbox(
    "Pilih Range Budget Anda:",
    ["< 500 Juta", "500 Juta - 1 Milyar", "1 - 10 Milyar", "> 10 Milyar"]
)

pilihan_kebutuhan = st.selectbox(
    "Pilih Kebutuhan Utama:",
    ["Harian / Irit (LCGC)", "Keluarga / Kapasitas Banyak (Suv)", "Offroad / Tangguh (4x4)","Gaya / Performa (Sport)", "Mewah / Eksklusif (Luxury)", "Atap Terbuka (Convertible)"]
)

if st.button("Cari Mobil!", type="primary"):
    
    tipe_pesan = "success" 
    
    if pilihan_budget == "< 500 Juta":
        if pilihan_kebutuhan == "Harian / Irit (LCGC)":
            hasil = "Honda Brio Satya, Toyota Agya, atau Daihatsu Ayla. Pilihan aman, irit, dan sisa budget bisa ditabung."
        elif pilihan_kebutuhan == "Keluarga / Kapasitas Banyak (Suv)":
            hasil = "Toyota Rush, Honda BR-V, atau Mitsubishi Xpander Cross. Cukup tangguh untuk jalanan Indonesia."
        elif pilihan_kebutuhan == "Offroad / Tangguh (4x4)":
            hasil = "Suzuki Jimny (kalau sabar inden) atau Ford Everest / Toyota Hilux Bekas."
        elif pilihan_kebutuhan == "Gaya / Performa (Sport)":
            tipe_pesan = "warning"
            hasil = "Budget ngepas untuk 'Sport' murni. Ambil Honda Civic Hatchback RS (Bekas) atau Toyota 86 Bekas, tapi siapkan sisa dana untuk modif dan perawatannya."
        elif pilihan_kebutuhan == "Mewah / Eksklusif (Luxury)":
            tipe_pesan = "warning"
            hasil = "Budget segini untuk 'Mewah' agak nanggung. Mending ambil sedan bekas ex-pejabat seperti Toyota Camry 2015-2018 dan nikmati sisa kemewahannya."
        elif pilihan_kebutuhan == "Atap Terbuka (Convertible)":
            tipe_pesan = "error"
            hasil = "Budget Anda sangat kurang untuk convertible. Naikkan budget ke 1 Milyar-an untuk ambil BMW Z4 / Mercedes SLK Bekas (dan siapkan dana ekstra untuk perawatan). Kalau maksa, potong atap mobil yang ada di bengkel las."

    elif pilihan_budget == "500 Juta - 1 Milyar":
        if pilihan_kebutuhan == "Harian / Irit (LCGC)":
            tipe_pesan = "info"
            hasil = "Budget Anda kebesaran untuk LCGC! Daripada LCGC, sekalian beli Honda HR-V RS atau Toyota Yaris Cross Hybrid. Tetap irit, tapi jauh lebih nyaman dan aman."
        elif pilihan_kebutuhan == "Keluarga / Kapasitas Banyak (Suv)":
            hasil = "Honda CR-V Turbo, Hyundai Santa Fe, atau duet Fortuner/Pajero Sport."
        elif pilihan_kebutuhan == "Offroad / Tangguh (4x4)":
            hasil = "Toyota Hilux GR Sport, Mitsubishi Triton, atau Isuzu D-Max. Siap kerja keras dan masuk tambang."
        elif pilihan_kebutuhan == "Gaya / Performa (Sport)":
            hasil = "Subaru BRZ (Baru) atau VW Golf GTI Bekas. Fun to drive dapet banget."
        elif pilihan_kebutuhan == "Mewah / Eksklusif (Luxury)":
            hasil = "Toyota Camry Hybrid Baru, BMW Seri 3, atau Mercedes-Benz C-Class."
        elif pilihan_kebutuhan == "Atap Terbuka (Convertible)":
            hasil = "Mazda MX-5 Miata RF atau Mini Cooper Cabriolet. Pas buat gaya di akhir pekan."


    elif pilihan_budget == "1 - 10 Milyar":
        if pilihan_kebutuhan == "Harian / Irit (LCGC)":
            tipe_pesan = "warning"
            hasil = "Anda punya miliaran tapi nyari LCGC? Anda bisa borong puluhan unit Brio se-dealer-dealernya! Tapi kalau mau mobil kecil nan mewah untuk harian, beli saja Lexus UX atau Mini Cooper EV."
        elif pilihan_kebutuhan == "Keluarga / Kapasitas Banyak (Suv)":
            hasil = "Toyota Land Cruiser 300, Lexus LX 600, atau BMW X7. Kasta tertinggi mobil keluarga."
        elif pilihan_kebutuhan == "Offroad / Tangguh (4x4)":
            hasil = "Jeep Wrangler Rubicon, Mercedes-Benz G-Class (G-Wagon), atau Land Rover Defender."
        elif pilihan_kebutuhan == "Gaya / Performa (Sport)":
            hasil = "Porsche 911 Carrera, Nissan GT-R, atau BMW M4 Competition."
        elif pilihan_kebutuhan == "Mewah / Eksklusif (Luxury)":
            hasil = "Mercedes-Benz S-Class, BMW Seri 7, atau Porsche Panamera."
        elif pilihan_kebutuhan == "Atap Terbuka (Convertible)":
            hasil = "Porsche 718 Boxster, BMW Seri 4 Convertible, atau Ferrari Portofino (Bekas)."

    elif pilihan_budget == "> 10 Milyar":
        if pilihan_kebutuhan == "Harian / Irit (LCGC)":
            tipe_pesan = "error"
            hasil = "Budget Anda level Sultan, sangat tidak masuk akal mencari LCGC! Kalau memang peduli lingkungan dan mau 'irit' bensin, beli saja Porsche Taycan (Full Electric) atau bikin armada taksi Brio sekalian."
        elif pilihan_kebutuhan == "Keluarga / Kapasitas Banyak (Suv)":
            hasil = "Rolls-Royce Cullinan atau Bentley Bentayga. Mobil keluarga dengan karpet bulu domba asli."
        elif pilihan_kebutuhan == "Offroad / Tangguh (4x4)":
            hasil = "Mercedes-AMG G63, Brabus 800 Adventure XLP, atau beli Tank militer beneran sekalian."
        elif pilihan_kebutuhan == "Gaya / Performa (Sport)":
            hasil = "Ferrari SF90 Stradale, Lamborghini Revuelto, atau McLaren 765LT."
        elif pilihan_kebutuhan == "Mewah / Eksklusif (Luxury)":
            hasil = "Rolls-Royce Phantom atau Bentley Flying Spur Mulliner."
        elif pilihan_kebutuhan == "Atap Terbuka (Convertible)":
            hasil = "Ferrari F8 Spider, Rolls-Royce Dawn, atau Lamborghini Huracan Evo Spyder."

    else:
        hasil = "Kombinasi belum terdaftar di sistem."

    st.markdown("---")
    
    if tipe_pesan == "success":
        st.success(f"**Rekomendasi Terbaik:** {hasil}")
    elif tipe_pesan == "info":
        st.info(f"**Saran untuk Anda:** {hasil}")
    elif tipe_pesan == "warning":
        st.warning(f"{hasil}")
    elif tipe_pesan == "error":
        st.error(f"{hasil}")