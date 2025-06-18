import re

def validasi_password(password, username):
    blacklist = ['password', '12345678', 'admin']
    score = 0

    if len(password) >= 8:                       # 1
        score += 1
    if re.search(r'[A-Z]', password):            # 2
        score += 1
    if re.search(r'[a-z]', password):            # 3
        score += 1
    if re.search(r'\d', password):               # 4
        score += 1
    if re.search(r'[\W_]', password):            # 5
        score += 1
    if ' ' not in password:                      # 6
        score += 1
    if password not in blacklist:                # 7
        score += 1
    if password != username:                     # 8
        score += 1
    if not re.search(r'(.)\1{2,}', password):     # 9 (tidak ada 3 karakter sama berurutan)
        score += 1

    # 10 - klasifikasi
    if score <= 4:
        print("Password Lemah")
    elif score <= 7:
        print("Password Sedang")
    else:
        print("Password Kuat")

# Contoh
password = "Admin@2024"
username = "admin"
validasi_password(password, username)
