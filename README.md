# Analisis HTML Generation With Templating

## Tujuan Tutorial

Tujuan tutorial ini adalah untuk berhenti mengembalikan teks mentah (plain text) dari view kita. Sebaliknya, kita akan menggunakan sistem template (pyramid_chameleon) untuk merender file HTML yang dinamis.

View kita tidak lagi bertanggung jawab membuat HTML. Sebaliknya, view hanya akan menyiapkan data (sebagai dictionary Python), dan meneruskannya ke renderer template untuk dibuatkan HTML-nya.

