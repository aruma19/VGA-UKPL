import re
import sys

def validasi_password(password, username):
    blacklist = ['password', '12345678', 'admin']
    score = 0

    print("\nHasil Analisis Password:")

    # V(G) 1: Mengecek panjang password minimal 8 karakter
    if len(password) >= 8:
        score += 1
        print("✅ Panjang password mencukupi (≥ 8 karakter)")
    else:
        print("❌ Password terlalu pendek (< 8 karakter)")

    # V(G) 2: Mengecek apakah password mengandung huruf kapital
    if re.search(r'[A-Z]', password):
        score += 1
        print("✅ Mengandung huruf kapital")
    else:
        print("❌ Tidak mengandung huruf kapital")

    # V(G) 3: Mengecek apakah password mengandung huruf kecil
    if re.search(r'[a-z]', password):
        score += 1
        print("✅ Mengandung huruf kecil")
    else:
        print("❌ Tidak mengandung huruf kecil")

    # V(G) 4: Mengecek apakah password mengandung angka
    if re.search(r'\d', password):
        score += 1
        print("✅ Mengandung angka")
    else:
        print("❌ Tidak mengandung angka")

    # V(G) 5: Mengecek apakah password mengandung simbol atau karakter khusus
    if re.search(r'[\W_]', password):
        score += 1
        print("✅ Mengandung simbol/karakter khusus")
    else:
        print("❌ Tidak mengandung simbol")

    # V(G) 6: Mengecek apakah password tidak mengandung spasi
    if ' ' not in password:
        score += 1
        print("✅ Tidak mengandung spasi")
    else:
        print("❌ Password mengandung spasi")

    # V(G) 7: Mengecek apakah password tidak termasuk daftar blacklist
    if password not in blacklist:
        score += 1
        print("✅ Password bukan kata sandi umum (blacklist)")
    else:
        print("❌ Password termasuk dalam blacklist umum")

    # V(G) 8: Mengecek apakah password tidak sama dengan username
    if password != username:
        score += 1
        print("✅ Password tidak identik dengan username")
    else:
        print("❌ Password sama dengan username")

    # V(G) 9: Mengecek apakah password tidak mengandung karakter berulang lebih dari 2 kali
    if not re.search(r'(.)\1{2,}', password):
        score += 1
        print("✅ Tidak mengandung karakter yang berulang lebih dari 2 kali")
    else:
        print("❌ Terdapat karakter berulang (seperti 'aaa', '111')")

    print("\nKekuatan Password:")
    # V(G) 10: Password lemah jika skor ≤ 4
    if score <= 4:
        print("🔴 Password Lemah (Skor: {}/9)".format(score))
    # V(G) 11: Password sedang jika skor antara 5–7
    elif score <= 7:
        print("🟠 Password Sedang (Skor: {}/9)".format(score))
    # V(G) 12: Password kuat jika skor ≥ 8 (else)
    else:
        print("🟢 Password Kuat (Skor: {}/9)".format(score))


# ===============================
# Program Utama
# ===============================

print("=" * 50)
print("🛡️  Program Validasi dan Klasifikasi Password".center(50))
print("=" * 50)

try:
    username = input("👤 Masukkan Username: ").strip()
    if not username:
        raise ValueError("Username tidak boleh kosong.")

    password = input("🔑 Masukkan Password: ").strip()
    if not password:
        raise ValueError("Password tidak boleh kosong.")

    validasi_password(password, username)

except ValueError as ve:
    print(f"\n⚠️  Kesalahan: {ve}")
    sys.exit(1)

except Exception as e:
    print(f"\n❌ Terjadi kesalahan tak terduga: {e}")
    sys.exit(1)
