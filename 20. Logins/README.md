# Analisis Logins with authentication

## Tujuan Tutorial
Tutorial ini mendemonstrasikan implementasi sistem **Authentication** (Autentikasi) sederhana. Tujuannya adalah memahami bagaimana aplikasi Pyramid memverifikasi identitas pengguna, menyimpan status login menggunakan **Auth Ticket**, dan mengelola siklus Login/Logout melalui manipulasi Header HTTP.

---

## Komponen Utama Kode

### A. Security Policy (`app.py`)
Pyramid memisahkan logika keamanan dari logika aplikasi. Kita menggunakan kebijakan berbasis tiket (Ticket-Based).

1.  **`AuthTktAuthenticationPolicy`:**
    Kebijakan ini mengelola identitas pengguna dengan menyimpan "tiket" terenkripsi di dalam Cookie browser.
2.  **Secret Key (`'sosecret'`):**
    Digunakan untuk menandatangani tiket. Ini mencegah pengguna memalsukan identitas dengan cara mengedit cookie secara manual.

### B. Security Helpers (`views.py`)
Pyramid menyediakan fungsi bantuan untuk menghasilkan Header HTTP yang diperlukan browser.

1.  **`remember(request, userid)`:**
    Dipanggil saat login sukses. Fungsi ini menghasilkan header `Set-Cookie` berisi tiket autentikasi yang valid.
2.  **`forget(request)`:**
    Dipanggil saat logout. Fungsi ini menghasilkan header yang memerintahkan browser untuk menghapus cookie autentikasi.
3.  **`request.authenticated_userid`:**
    Properti otomatis yang berisi ID pengguna (misal: 'editor') jika cookie valid ditemukan. Jika tidak ada cookie atau cookie palsu, nilainya `None`.

---

## Alur Kerja (Request Lifecycle)

1.  **Login Attempt:** Pengguna mengirim kredensial (username/password) via POST.
2.  **Verification:** Kode memverifikasi data dengan database (dictionary `USERS`).
3.  **Cookie Generation:** Jika valid, `remember()` membuat token terenkripsi. Server mengirim response dengan header `Set-Cookie`.
4.  **Authenticated Request:** Pada request selanjutnya, browser otomatis mengirim cookie tersebut.
5.  **Decoding:** `AuthTktAuthenticationPolicy` membaca cookie, memvalidasi tanda tangan, dan mengisi variabel `request.authenticated_userid`. Aplikasi mengenali bahwa user sudah login.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 17 48 50_480ccea9](https://github.com/user-attachments/assets/692a3ca4-c833-433b-8410-3b993001039a)

![Gambar WhatsApp 2025-11-13 pukul 17 48 50_c01c05ba](https://github.com/user-attachments/assets/5d50dc13-f11a-438c-9483-16ad480fd3e7)

![Gambar WhatsApp 2025-11-13 pukul 17 48 50_d15618f7](https://github.com/user-attachments/assets/df4b8321-c8c3-49cc-9889-2c9cb001e29e)
