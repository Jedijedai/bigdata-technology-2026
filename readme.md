📊 Big Data Project – Simple PySpark Job
👤 Identitas

Nama: Husni Majedi
NIM: 230104040123
Mata Kuliah: Teknologi Big Data
Semester: 6

📌 Deskripsi Project

Project ini merupakan implementasi sederhana penggunaan PySpark untuk melakukan proses agregasi data menggunakan metode groupBy dan sum.

Framework yang digunakan adalah:

Apache Spark

PySpark

Python 3.10

JDK 17

Program akan:

Membuat DataFrame

Melakukan grouping berdasarkan kategori

Menjumlahkan nilai pada setiap kategori

Menampilkan hasil agregasi

🗂 Struktur Project
bigdata-project/
│
├── scripts/
│   └── simple_job.py
│
└── README.md
⚙️ Requirement

Pastikan sudah menginstall:

Python 3.10

JDK 17

Apache Spark

VS Code (opsional)

Cek versi dengan:

python --version
java -version
🔧 Konfigurasi Penting (Windows Fix)

Jika muncul error:

Cannot run program "python3"

Tambahkan konfigurasi berikut di dalam simple_job.py:

import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"

Ini bertujuan agar Spark menggunakan Python yang benar.

🧠 Source Code
import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)
df.groupBy("category").sum("value").show()

spark.stop()
▶️ Cara Menjalankan

Masuk ke folder project:

cd bigdata-project

Jalankan:

python scripts/simple_job.py
📈 Output yang Diharapkan
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
🎯 Tujuan Pembelajaran

Melalui project ini mahasiswa mampu:

Memahami konsep dasar Big Data

Menggunakan PySpark untuk pemrosesan data

Melakukan transformasi dan agregasi DataFrame

Mengatasi error konfigurasi Java dan Python di Windows

📝 Catatan

Warning seperti:

Did not find winutils.exe

Tidak mempengaruhi eksekusi program pada job sederhana.