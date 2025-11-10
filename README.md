# 🏗️ Analisis *Pyramid Quick Tutorial - Hello World*

### Tujuan Tutoirial 

Tujuan dari tutorial "Hello World" ini adalah untuk mendemonstrasikan konsep inti dan komponen minimal yang diperlukan untuk membuat aplikasi web yang berfungsi menggunakan framework Pyramid. Ini menunjukkan bagaimana Pyramid dapat memulai dari satu file Python sederhana tanpa memaksakan struktur direktori yang kompleks.

---

## 1. Komponen Utama Kode

Kode *Hello World* ini memperkenalkan **3 pilar utama Pyramid**:

---

### 🧩 A. View Callable (`hello_world`)

```python
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')
```
