# GitHub'a Yükleme Rehberi

## ADIM 1: GitHub'da Yeni Repo Oluştur

1. https://github.com/new adresine git
2. **Repository name**: `projeSablonu` (veya istediğiniz isim)
3. **Description**: "Şirket içi standart yazılım yaşam döngüsü şablonu"
4. **Public** seç (herkes görebilsin)
5. **README, .gitignore, License** SEÇME (bizde zaten var)
6. **Create repository** tıkla

## ADIM 2: Git Yapısını Kur

Terminalde sırasıyla şu komutları çalıştır:

```powershell
cd C:\Users\PC_1938_YD26\Desktop\projeSablonu

# Git kullanıcı bilgilerini ayarla (kendi bilgilerinle değiştir)
git config --global user.name "SeninAdin"
git config --global user.email "senin@email.com"

# Git'i başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit'i yap
git commit -m "feat: kurumsal proje şablonu oluşturuldu"

# Ana dalı main olarak ayarla
git branch -M main

# GitHub uzak depo adresini ekle (kendi repo URL'ini kullan)
git remote add origin https://github.com/KULLANICI_ADI/REPO_ADI.git

# Push et
git push -u origin main
```

## ADIM 3: Etiketleri Yükle

1. https://github.com/KULLANICI_ADI/REPO_ADI/labels adresine git
2. Her etiketi tek tek oluştur veya script kullan

---

**NOT**: Repo adını ve kullanıcı adını söyledikten sonra otomatik yükleyebilirim.
