def hesapla_taksi_ücreti(mesafe, beklenen_sure):
    # Ücretler
    ucret_katsayisi = 3.50  # Her km başına düşer.
    sabit_ucret = 4.50  # Başlangıç ücret
    bekleme_ucreti = 0.90  # Dakika başına düşen bekleme ücreti
    
    mesafe_ucreti = ucret_katsayisi * mesafe
    bekleme_ucreti = bekleme_ucreti * beklenen_sure
    
    # Toplam taksi ücreti
    toplam_ucret = bekleme_ucreti + mesafe_ucreti + sabit_ucret
    return toplam_ucret

# Kullanıcıdan input alma
mesafe = float(input("Gidilecek toplam mesafe (km):"))
beklenen_sure = float(input("Beklenen süreyi girin (Dakika): "))

# Toplam ücret hesabı
ucret = hesapla_taksi_ücreti(mesafe, beklenen_sure)

print(f"Taksi ücreti: ${ucret:.2f}")