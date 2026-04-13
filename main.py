# Sistem Pakar Diagnosa Kerusakan Komputer/Laptop

# 1. Knowledge Base — Database Kerusakan & Gejala
# Struktur: "Nama Kerusakan": {"gejala": [...], "solusi": "..."}
database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["komputer_sering_restart", "blue_screen", "bunyi_beep_berulang"],
        "solusi": "Cabut RAM, bersihkan pin RAM dengan penghapus, lalu pasang kembali. Jika masih bermasalah, coba pindahkan ke slot lain atau ganti RAM."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["komputer_mati_sendiri", "komputer_tidak_menyala", "restart_saat_beban_berat"],
        "solusi": "Periksa kabel daya dan konektor PSU. Coba gunakan PSU lain untuk pengujian. Jika PSU lemah, segera ganti dengan PSU baru yang sesuai watt-nya."
    },
    "Overheat (Prosesor)": {
        "gejala": ["komputer_mati_sendiri", "performa_lambat", "suhu_tinggi", "kipas_berisik"],
        "solusi": "Bersihkan kipas dan heatsink dari debu. Ganti thermal paste pada prosesor. Pastikan sirkulasi udara di dalam casing baik."
    },
    "VGA Bermasalah": {
        "gejala": ["layar_bergaris", "blue_screen", "layar_gelap_saat_gaming", "artefak_visual"],
        "solusi": "Cabut dan pasang ulang kartu VGA. Perbarui driver VGA ke versi terbaru. Jika masalah berlanjut, coba tes dengan VGA lain atau bawa ke service center."
    },
    "Hardisk Corrupt": {
        "gejala": ["booting_lama", "file_hilang_rusak", "bunyi_klik_hardisk", "blue_screen"],
        "solusi": "Segera backup data penting. Jalankan perintah 'chkdsk /f' di Command Prompt. Pertimbangkan untuk mengganti hardisk dengan SSD baru."
    },
    "Motherboard Rusak": {
        "gejala": ["komputer_tidak_menyala", "bunyi_beep_berulang", "usb_tidak_berfungsi", "bios_tidak_tampil"],
        "solusi": "Periksa kapasitor pada motherboard apakah ada yang menggembung. Lakukan reset BIOS dengan melepas baterai CMOS. Jika rusak parah, ganti motherboard."
    },
    "Kerusakan Keyboard Laptop": {
        "gejala": ["tombol_tidak_merespon", "huruf_berulang", "keyboard_mengetik_sendiri"],
        "solusi": "Bersihkan keyboard dari debu dan kotoran. Periksa kabel fleksibel keyboard. Jika rusak, gunakan keyboard eksternal atau ganti keyboard internal."
    }
}

# 2. Daftar Semua Gejala Untuk Pertanyaan
# Struktur: (kode_gejala, teks_pertanyaan)
semua_gejala = [
    ("komputer_sering_restart",   "Apakah komputer/laptop Anda sering restart sendiri?"),
    ("blue_screen",               "Apakah muncul layar blue screen (BSOD)?"),
    ("bunyi_beep_berulang",       "Apakah terdengar bunyi beep berulang saat dinyalakan?"),
    ("komputer_mati_sendiri",     "Apakah komputer/laptop tiba-tiba mati sendiri?"),
    ("komputer_tidak_menyala",    "Apakah komputer/laptop sama sekali tidak menyala?"),
    ("restart_saat_beban_berat",  "Apakah komputer restart saat menjalankan program berat?"),
    ("performa_lambat",           "Apakah performa komputer/laptop terasa sangat lambat?"),
    ("suhu_tinggi",               "Apakah suhu komputer/laptop terasa sangat panas?"),
    ("kipas_berisik",             "Apakah kipas berbunyi sangat berisik?"),
    ("layar_bergaris",            "Apakah layar menampilkan garis-garis (artefak)?"),
    ("layar_gelap_saat_gaming",   "Apakah layar menjadi gelap/mati saat bermain game?"),
    ("artefak_visual",            "Apakah muncul kotak-kotak atau warna aneh di layar?"),
    ("booting_lama",              "Apakah proses booting sangat lama?"),
    ("file_hilang_rusak",         "Apakah ada file yang hilang atau rusak (corrupt)?"),
    ("bunyi_klik_hardisk",        "Apakah terdengar bunyi klik-klik dari hardisk?"),
    ("usb_tidak_berfungsi",       "Apakah port USB tidak berfungsi?"),
    ("bios_tidak_tampil",         "Apakah BIOS tidak tampil saat booting?"),
    ("tombol_tidak_merespon",     "Apakah ada tombol keyboard yang tidak merespon?"),
    ("huruf_berulang",            "Apakah huruf muncul berulang saat mengetik?"),
    ("keyboard_mengetik_sendiri", "Apakah keyboard mengetik sendiri tanpa ditekan?"),
]

# 3. Working Memory — Menyimpan Gejala yang Dialami Pengguna
gejala_pasien = []

# 4. Fungsi Tanya Gejala
def tanya_gejala(kode_gejala, teks_pertanyaan):
    """Menampilkan pertanyaan dan menyimpan jawaban ke working memory."""
    while True:
        jawaban = input(f"  {teks_pertanyaan} (y/t): ").lower().strip()
        if jawaban in ('y', 't'):
            break
        print("Masukkan 'y' untuk Ya atau 't' untuk Tidak.")
    if jawaban == 'y':
        gejala_pasien.append(kode_gejala)

# 5. Mesin Inferensi — Forward Chaining
def jalankan_diagnosa():
    """Mencocokkan gejala pasien dengan knowledge base untuk menentukan kerusakan."""
    hasil_diagnosa = []

    for kerusakan, data in database_kerusakan.items():
        gejala_kerusakan = data["gejala"]
        # Hitung berapa gejala yang cocok
        gejala_cocok = [g for g in gejala_kerusakan if g in gejala_pasien]
        jumlah_cocok = len(gejala_cocok)
        jumlah_total = len(gejala_kerusakan)

        # Kerusakan terdeteksi jika semua gejala kunci terpenuhi
        if jumlah_cocok == jumlah_total:
            persentase = 100.0
            hasil_diagnosa.append((kerusakan, data["solusi"], persentase, gejala_cocok))
        # Kerusakan kemungkinan jika sebagian besar gejala terpenuhi (>= 50%)
        elif jumlah_cocok > 0 and (jumlah_cocok / jumlah_total) >= 0.5:
            persentase = round((jumlah_cocok / jumlah_total) * 100, 1)
            hasil_diagnosa.append((kerusakan, data["solusi"], persentase, gejala_cocok))

    return hasil_diagnosa

# 6. Fungsi Menampilkan Hasil Diagnosa
def tampilkan_hasil(hasil_diagnosa):
    """Menampilkan hasil diagnosa kerusakan beserta solusinya."""
    print("\n" + "=" * 60)
    print("            HASIL DIAGNOSA KERUSAKAN")
    print("=" * 60)

    if not hasil_diagnosa:
        print("\n  Tidak ditemukan kerusakan yang cocok berdasarkan")
        print("     gejala yang Anda masukkan.")
        print("\n  Saran: Coba periksa ulang gejala atau bawa")
        print("     perangkat ke teknisi profesional.\n")
    else:
        # Urutkan berdasarkan persentase tertinggi
        hasil_diagnosa.sort(key=lambda x: x[2], reverse=True)
        for i, (kerusakan, solusi, persentase, gejala_cocok) in enumerate(hasil_diagnosa, 1):
            status = "TERDETEKSI" if persentase == 100.0 else "KEMUNGKINAN"
            print(f"\n  [{i}] {status}: {kerusakan}")
            print(f"      Tingkat Kesesuaian : {persentase}%")
            print(f"      Gejala Cocok       : {', '.join(gejala_cocok)}")
            print(f"      Solusi             : {solusi}")

    print("\n" + "=" * 60)

# 7. Fungsi Utama — Main Program
def main():
    print("=" * 60)
    print("   SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER/LAPTOP")
    print("=" * 60)
    print("\n  Jawablah pertanyaan berikut dengan:")
    print("  'y' untuk Ya  |  't' untuk Tidak\n")
    print("-" * 60)

    # Tanyakan semua gejala kepada pengguna
    for kode, teks in semua_gejala:
        tanya_gejala(kode, teks)

    print("-" * 60)
    print("\nMenganalisis gejala...\n")

    # Jalankan mesin inferensi
    hasil = jalankan_diagnosa()

    # Tampilkan hasil diagnosa
    tampilkan_hasil(hasil)

    # Tampilkan ringkasan gejala yang dipilih
    if gejala_pasien:
        print("Gejala yang Anda alami:")
        for g in gejala_pasien:
            # Ubah kode gejala menjadi format yang lebih mudah dibaca
            nama_gejala = g.replace("_", " ").capitalize()
            print(f"     - {nama_gejala}")
        print()

# Menjalankan program
if __name__ == "__main__":
    main()
