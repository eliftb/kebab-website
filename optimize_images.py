import os
from PIL import Image

# Desteklenen formatlar
formats = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')

def optimize_images():
    print("Resim optimizasyonu başlıyor...")
    
    # Klasördeki tüm dosyaları gez
    for filename in os.listdir('.'):
        if filename.endswith(formats):
            filepath = os.path.join('.', filename)
            
            try:
                # Resmi aç
                with Image.open(filepath) as img:
                    # Dosya boyutunu kontrol et (MB cinsinden)
                    file_size = os.path.getsize(filepath) / (1024 * 1024)
                    
                    # Eğer dosya zaten küçükse (örn: 1MB altı) atla
                    if file_size < 1:
                        print(f"Skipped (Zaten küçük): {filename}")
                        continue
                    
                    print(f"Optimizing: {filename} ({file_size:.2f} MB)...")
                    
                    # Resmi RGB moduna çevir (PNG'ler için gerekebilir)
                    if img.mode in ("RGBA", "P"): 
                        img = img.convert("RGB")
                    
                    # Boyutlandırma (Genişlik maksimum 1920px olsun, web standardı)
                    if img.width > 1920:
                        ratio = 1920 / float(img.width)
                        new_height = int((float(img.height) * float(ratio)))
                        img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
                    
                    # Aynı ismin üzerine kaydet (Kaliteyi %85'e düşür - Gözle fark edilmez ama boyut çok düşer)
                    img.save(filepath, "JPEG", optimize=True, quality=85)
                    
                    new_size = os.path.getsize(filepath) / (1024 * 1024)
                    print(f" --> Yeni Boyut: {new_size:.2f} MB ✅")
                    
            except Exception as e:
                print(f"Hata oluştu ({filename}): {e}")

if __name__ == "__main__":
    optimize_images()