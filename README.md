# Analisis Pyramid Quick Tutorial - Python Packages for Pyramid Applications

## Tujuan Tutorial

Tujuan dari tutorial ini adalah untuk mengubah aplikasi web "Hello World" yang sebelumnya berbentuk satu file (.py) menjadi sebuah paket Python (Python package) yang terstruktur dan dapat diinstal.
Ini adalah langkah fundamental untuk membangun aplikasi yang lebih besar dan lebih terorganisir. Tutorial ini memperkenalkan konsep-konsep kunci untuk skalabilitas:
1. Struktur Proyek: Mengubah satu file menjadi struktur direktori paket (tutorial/__init__.py).
2. Manajemen Dependensi: Menggunakan setup.py untuk mendefinisikan apa saja yang dibutuhkan oleh aplikasi (misalnya, pyramid, waitress).
3. Konfigurasi Eksternal: Menggunakan file .ini (development.ini) untuk mengelola pengaturan server dan aplikasi, alih-alih melakukan hardcoding di dalam file Python.
4. Server Produksi (Entry-level): Mengganti server bawaan Python (wsgiref) dengan server WSGI yang lebih mumpuni, yaitu waitress.
5. Entry Points: Memperkenalkan konsep entry points agar aplikasi dapat dijalankan oleh runner standar seperti pserve.

---

## Komponen Utama Kode

Tutorial ini merombak struktur file tunggal menjadi paket yang dapat diinstal. Komponen utamanya adalah tiga file baru yang bekerja bersama:

---

### A. setup.py (Manajer Paket & Dependensi)

File ini memberi tahu Python cara menginstal paket Anda dan apa saja dependensinya.

```python
from setuptools import setup

# List dependensi yang dibutuhkan
requires = [
    'pyramid',
    'waitress', # Server WSGI
]

setup(
    name='tutorial',
    install_requires=requires,
    # 'Entry points' adalah "iklan" paket Anda ke dunia luar
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main', # Menghubungkan nama 'main' ke fungsi 'main' di 'tutorial'
        ],
    },
)
```
