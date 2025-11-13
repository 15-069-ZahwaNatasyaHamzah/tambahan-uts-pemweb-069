# Analisis Dispatching URLs To Views With Routing

## Tujuan Tutorial
Tutorial ini mendemonstrasikan konsep **Dynamic Routing** (Rute Dinamis). Tujuannya adalah memahami cara menangkap variabel dari struktur URL (Pattern Matching) dan memanfaatkannya di dalam logika aplikasi menggunakan `matchdict`.

---

## Komponen Utama Kode

### A. Configurator (`app.py`)
Bagian ini mendefinisikan pola URL yang fleksibel menggunakan tanda kurung kurawal `{}` sebagai *placeholder*.

1.  **Pattern Matching:**
    Kode `config.add_route('hello', '/howdy/{first}/{last}')` membuat rute yang tidak kaku.
2.  **Dynamic Segments:**
    Bagian `{first}` dan `{last}` akan menangkap teks apa pun yang dimasukkan pengguna di posisi tersebut, memungkinkan satu rute menangani banyak variasi URL.

### B. View Class (`views.py`)
Di sisi logika, kita mengakses data yang ditangkap URL tersebut melalui objek request.

1.  **`self.request.matchdict`:**
    Adalah dictionary khusus yang menyimpan nilai dari segmen dinamis URL.
2.  **Ekstraksi Data:**
    Jika URL adalah `/howdy/Zahwa/Hamzah`, maka `matchdict['first']` otomatis berisi "Zahwa" dan `matchdict['last']` berisi "Hamzah".

---

## Alur Kerja (Request Lifecycle)

1.  **User Request:** Pengguna mengakses `http://localhost:6543/howdy/Zahwa/Hamzah`.
2.  **URL Dispatch:** Pyramid memindai rute dan menemukan kecocokan pola dengan `/howdy/{first}/{last}`.
3.  **Populasi Matchdict:** Pyramid mengekstrak nilai "Zahwa" dan "Hamzah" ke dalam dictionary `matchdict`.
4.  **View Execution:** Method `hello` dipanggil, mengambil nilai dari `matchdict`, dan mengembalikannya sebagai data JSON.
5.  **Response:** Browser menerima data JSON yang dinamis sesuai input URL.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 13 51 38_61064f4e](https://github.com/user-attachments/assets/78464996-32d3-4eb1-b658-bc12a33a27ce)
