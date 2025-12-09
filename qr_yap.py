import qrcode

site_url = "https://sanliurfakebap.com/menu" 

# QR Kod Ayarları (Baskı Kalitesi)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Yüksek hata düzeltme (Leke gelse de okunur)
    box_size=30, # Yüksek çözünürlük (Pikselleşmez)
    border=2,    # Beyaz kenarlık
)

# Veriyi ekle ve oluştur
qr.add_data(site_url)
qr.make(fit=True)

# Rengi ayarla (Siyah-Beyaz en garantisidir)
img = qr.make_image(fill_color="black", back_color="white")

# Dosyayı kaydet
dosya_adi = "masa_menu_qr.png"
img.save(dosya_adi)

print(f"✅ Karekod başarıyla oluşturuldu: {dosya_adi}")
print(f"🔗 Yönlenen Adres: {site_url}")
print("Bu dosyayı telefonunla test et, sonra matbaaya gönder!")