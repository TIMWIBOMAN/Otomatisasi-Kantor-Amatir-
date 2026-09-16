import time
import webbrowser

print("==========================================")
print("   SISTEM OTOMATISASI KERJA KANTOR V1.0   ")
print("==========================================")
print("Menyiapkan ruang kerja digital Anda...\n")

# Daftar situs kerja harian Anda
situs_kerja = [
    "https://web.whatsapp.com/"  # WA Saya
    "https://grok.com/c/59d5c7f2-fd81-42cf-ac10-574bc524d3ad?rid=db34f08a-5843-4558-8362-629873234f7c",  # Grok Auto
    "https://mail.google.com/mail/u/3/#inbox",  # Email Saya
    "https://drive.google.com/drive/u/3/home",  # Drive Saya
    "https://www.google.com/webhp?authuser=3",  # Tab kosong 
]

# Proses membuka semua tab sekaligus
for url in situs_kerja:
    print(f"-> Membuka: {url}")
    webbrowser.open(url)
    time.sleep(0.5)  

print("\n[SUKSES] Semua ruang kerja berhasil dibuka. Selamat bekerja, tetap produktif!")
