# H1D024102-PraktikumKB-Pertemuan4

Pengumpulan tugas praktikum Kecerdasan Buatan pertemuan 4.

## Sistem Pakar Diagnosa Kerusakan Komputer/Laptop

Program ini merupakan implementasi sistem pakar (Expert System) berbasis Python menggunakan metode **Forward Chaining** untuk mendiagnosa kerusakan pada komputer/laptop berdasarkan gejala yang dimasukkan oleh pengguna.

---

### 1. Knowledge Base (Basis Pengetahuan)

Knowledge base didefinisikan menggunakan struktur data **Dictionary** pada **baris ke-5 sampai 55**. Setiap kerusakan memiliki daftar gejala dan solusi penanganannya.

Program ini memiliki **7 jenis kerusakan** yang dapat dideteksi:

| No | Kerusakan | Jumlah Gejala | Baris |
|---|---|---|---|
| 1 | RAM Rusak | 3 gejala | 7–9 |
| 2 | Power Supply (PSU) Lemah | 3 gejala | 11–13 |
| 3 | Overheat (Prosesor) | 4 gejala | 15–18 |
| 4 | VGA Bermasalah | 4 gejala | 20–23 |
| 5 | Hardisk Corrupt | 4 gejala | 25–28 |
| 6 | Motherboard Rusak | 4 gejala | 30–33 |
| 7 | Kerusakan Keyboard Laptop | 3 gejala | 35–37 |

Struktur penyimpanan menggunakan Dictionary nested:
```python
database_kerusakan = {
    "Nama Kerusakan": {
        "gejala": ["gejala_1", "gejala_2", ...],
        "solusi": "Deskripsi solusi penanganan"
    }
}
```

---

### 2. Daftar Gejala (Pertanyaan)

Seluruh gejala yang diajukan kepada pengguna didefinisikan pada **baris ke-59 sampai 80** dalam bentuk list of tuple. Terdapat **20 gejala** yang akan ditanyakan secara berurutan.

Setiap elemen tuple berisi:
- **Kode gejala** — digunakan sebagai key untuk pencocokan dengan knowledge base.
- **Teks pertanyaan** — pertanyaan yang ditampilkan ke pengguna dalam bahasa Indonesia.

---

### 3. Working Memory

Working memory dideklarasikan pada **baris ke-83** berupa list kosong `gejala_pasien = []`. List ini berfungsi untuk menyimpan kode gejala yang dijawab "Ya" oleh pengguna selama sesi diagnosa berlangsung.

---

### 4. Fungsi Tanya Gejala

Fungsi `tanya_gejala()` pada **baris ke-86 sampai 93** bertugas menampilkan pertanyaan kepada pengguna dan memasukkan kode gejala ke dalam working memory jika pengguna menjawab `'y'`. Fungsi ini juga menangani validasi input agar hanya menerima jawaban `'y'` atau `'t'`.

---

### 5. Mesin Inferensi (Forward Chaining)

Mesin inferensi diimplementasikan pada fungsi `jalankan_diagnosa()` di **baris ke-96 sampai 113**. Proses inferensi bekerja sebagai berikut:

1. Program mengiterasi seluruh kerusakan di knowledge base.
2. Untuk setiap kerusakan, program menghitung jumlah gejala yang cocok dengan gejala di working memory.
3. Jika **semua gejala** terpenuhi → kerusakan **terdeteksi** (100%).
4. Jika **sebagian gejala** terpenuhi (≥ 50%) → kerusakan berstatus **kemungkinan** dengan persentase kesesuaian.
5. Jika tidak ada gejala yang cocok → kerusakan **tidak terdeteksi**.

Program mampu menangani kondisi dimana gejala yang dimasukkan tidak cocok dengan kerusakan apa pun.

---

### 6. Output Hasil Diagnosa

Fungsi `tampilkan_hasil()` pada **baris ke-116 sampai 137** menampilkan hasil diagnosa yang meliputi:
- **Status deteksi** — `TERDETEKSI` atau `KEMUNGKINAN`.
- **Nama kerusakan** — jenis kerusakan yang teridentifikasi.
- **Tingkat kesesuaian** — persentase kesesuaian gejala.
- **Gejala yang cocok** — daftar gejala yang terpenuhi.
- **Solusi singkat** — rekomendasi penanganan kerusakan.

Hasil diagnosa diurutkan berdasarkan persentase kesesuaian tertinggi. Jika tidak ada kerusakan yang cocok, program menampilkan pesan bahwa tidak ditemukan kerusakan dan menyarankan pengguna untuk membawa perangkat ke teknisi.

---

### 7. Percobaan Dari Modul Praktikum

Selain tugas utama `main.py`, terdapat file percobaan dari modul praktikum:

**a. `percobaan1.py` — Fakta & Aturan Keluarga**
Program yang mengimplementasikan konsep fakta dan aturan sederhana berupa relasi keluarga (parent, sibling, grandparent) menggunakan list of tuple dan fungsi pencarian.

**b. `percobaan3.py` — Sistem Pakar Diagnosa Malaria (Console)**
Program sistem pakar berbasis console yang mendiagnosa jenis penyakit malaria berdasarkan gejala menggunakan pendekatan IF-THEN sederhana.

**c. `percobaan4.py` — Sistem Pakar Diagnosa Malaria (GUI)**
Program sistem pakar berbasis GUI menggunakan library `tkinter` yang mendiagnosa penyakit malaria dengan dictionary sebagai knowledge base.

---

### 8. Cara Menjalankan Program

```bash
# Jalankan Sistem Pakar Diagnosa Kerusakan Komputer/Laptop
python main.py

# Jalankan Percobaan 1 — Fakta & Aturan Keluarga
python percobaan1.py

# Jalankan Percobaan 3 — Diagnosa Malaria (Console)
python percobaan3.py

# Jalankan Percobaan 4 — Diagnosa Malaria (GUI)
python percobaan4.py
```
