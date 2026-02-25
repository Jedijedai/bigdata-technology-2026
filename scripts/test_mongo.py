from pymongo import MongoClient

uri = "PASTE_CONNECTION_STRING_DI_SINI"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)