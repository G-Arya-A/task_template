# Task Template — Kurumsal Görev Yönetim Şablonu

> **Şirket içi standart yazılım yaşam döngüsü (SDLC) şablonu.**
> Issue oluşturma → analiz → onay → geliştirme → test → yayımlama sürecini otomatikleştiren,
> tamamen Türkçe çalışan bir GitHub yapılandırmasıdır.

Bu repo; tüm projelerde ortak bir görev akışı, otomatik etiketleme ve sürüm yönetimi sağlar.
Amacı: **herkesin aynı şekilde issue açması, aynı süreçten geçmesi ve sonucun otomatik izlenmesi.**

---

## 📌 Şu An Ne Durumdayız?

| Başlık | Durum |
|--------|-------|
| Güncel sürüm | **v1.8.1** (2026-08-01) |
| Issue template sayısı | **4** (TR, BR, RR, QV) |
| Etiket (label) sayısı | **54** — GitHub'da birebir senkronize |
| Workflow sayısı | **3** (CI, Issue Lifecycle, Release) |
| Otomatik etiketleme | ✅ Çalışıyor (ekip seçiminden `team:X`) |
| RR → parent issue otomasyonu | ✅ Çalışıyor |
| Semantic Release | ✅ Çalışıyor |
| Dil | ✅ Tamamen Türkçe |

---

## 🧩 Issue Template'leri

GitHub'da **New Issue** tıklanınca şu 4 form görünür:

### 1. TR — Görev Talebi (Ticket) `[TR]`
**Varsayılan etiketler:** `state:analiz`, `type:görev`, `priority:P3`

Tek görev formu — tüm iş türlerini kapsar. Form bölümleri:

| # | Bölüm | Zorunlu |
|---|-------|---------|
| 1 | **Temel Bilgiler** — Talep Sahibi, Talep Türü, Öncelik | ✅ |
| 2 | **İş Gereksinimi** — İş problemi, iş değeri/gerekçe | ✅ |
| 3 | **Teknik Kapsam** — Teknik açıklama, kapsam, araştırma soruları, açık sorular | kısmi |
| 4 | **Risk ve Geri Dönüş** — Riskler+azaltma, orijinal sürüm yedeği, geri dönüş planı | ✅ |
| 5 | **Kabul Kriterleri** — test edilebilir AC listesi | ✅ |
| 6 | **Test Planı** — uygulanacak test senaryoları (T-1, T-2...) | ✅ |
| 7 | **Organizasyon** — Sorumlu Ekip, atanacak kişi, son tarih, bağımlılıklar | kısmi |
| 8 | **Notlar** — ek notlar + kontrol listesi | ❌ |

**Talep Türü seçenekleri:** Yeni Özellik · Hata Düzeltme · Kod/Yapı Yeniden Düzenleme · Araştırma/Keşif (zaman kutusu) · Risk Azaltma · İş Gereksinimi · Soru / Açıklama · Diğer

**Sorumlu Ekip seçenekleri:** PY · AYG · FYYG · GSYG · IMYG · K2 · OYG · PSYG · SSYG · SYG · YMG · YSYG · YTO · ST · SSG-STAGY

### 2. BR — Hata Raporu `[BR]`
**Varsayılan etiketler:** `state:analiz`, `type:hata`, `priority:P2`

Alanlar: Raporlayan · Hata Önemi (Kritik/Yüksek/Orta/Düşük) · Hata Açıklaması · Tekrar Oluşturma Adımları · Beklenen Davranış · Gerçekleşen Davranış · Ortam Bilgisi · Ekran Görüntüleri/Loglar · İletişim Kanalı · Kontrol Listesi

### 3. RR — Revizyon Talebi `[RR]`
**Varsayılan etiketler:** `state:revizyon`, `type:revizyon`

> ⚠️ Bu form **yeni bir issue oluşturmaz** — mevcut issue'yu revize eder.
> `İlgili Issue Numarası` alanındaki `#123` sayesinde otomasyon parent issue'yu günceller.

Alanlar: İlgili Issue Numarası · Revizyon Talep Eden · Revize Kategorisi (Doküman/Hata Düzeltme/İyileştirme/Yeniden Yapılanma/Gereksinim/Performans/Güvenlik/Uyumluluk) · Revizyon Önemi · Revizyon Sebebi · Mevcut Durum (As-is) · İstenen Durum (To-be) · Revize Kabul Kriterleri · Revizyon Sorumlusu

### 4. QV — QA Doğrulama `[QV]`
**Varsayılan etiketler:** `state:test-plani`, `type:doğrulama`

> Test planı TR içinde tutulur; QV **yalnızca sonucu doğrular**.

Alanlar: İlgili Görev (TR) · İlgili PR · QA Mühendisi · Yapı Sürümü · Ortam (Geliştirme/Önizleme/Üretim/Sürekli Entegrasyon/Yerel) · Test Tarihi · Genel Sonuç (GEÇTİ/KALDI/ENGELLİ) · Başarısız Senaryolar · Regresyon Değerlendirmesi · Öneri · QA Onayı · Onay Tarihi · Test Notları

> `config.yml` — boş issue açmayı kapatır; iletişim kanallarını bağlar.

---

## 🏷️ Etiket Sistemi (54 Etiket)

Tüm etiketler `.github/labels.yml` içinde tanımlı ve GitHub'da **birebir senkronize**. Kategoriler:

| Kategori | Örnekler | Amaç |
|----------|----------|------|
| **Durum** `state:*` | `state:analiz`, `state:onaylı`, `state:atanmış`, `state:başlamadı`, `state:başladı`, `state:kod-gözden-geçirme`, `state:test-plani`, `state:test`, `state:revizyon`, `state:yayınlanmış` | Yaşam döngüsü pozisyonu |
| **Tip** `type:*` | `type:görev`, `type:hata`, `type:revizyon`, `type:özellik`, `type:iyileştirme`, `type:doküman`, `type:teknik-borç`, `type:güvenlik`, `type:doğrulama` | İşin türü |
| **Öncelik** `priority:*` | `priority:P1` … `priority:P4` | Aciliyet |
| **Revizyon** `rev:*` | `rev:doküman`, `rev:hata-düzeltme`, `rev:iyileştirme`, `rev:yeniden-yapılanma`, `rev:gereksinim`, `rev:performans`, `rev:güvenlik` | Revizyon kategorisi |
| **Olay** `event:*` | `event:talep-onaylandı`, `event:test-geçti`, `event:test-kaldı`, `event:sürüm-yayınlandı`, `event:revizyon-istendi` | Otomasyon tetikleyicileri |
| **Ekip** `team:*` | `team:PY`, `team:AYG`, `team:FYYG`, `team:GSYG`, `team:IMYG`, `team:K2`, `team:OYG`, `team:PSYG`, `team:SSYG`, `team:SYG`, `team:YMG`, `team:YSYG`, `team:YTO`, `team:ST`, `team:SSG-STAGY` | Sorumlu ekip |
| **Doküman** `doc:*` | `doc:gelen`, `doc:girdi`, `doc:gönderilen`, `doc:revize` | Doküman yönü |

**Kural:** Bir issue'da **yalnızca bir** `state:*` etiketi bulunmalıdır.

Etiketler tek kaynaktan yönetilir. İki senkronizasyon yolu:
1. `python scripts/setup_labels.py G-Arya-A/task_template` (PyGithub ile)
2. GitHub API ile (bu repo kurulurken yapıldı)

---

## 🤖 Otomasyonlar (Workflow'lar)

### 1. Issue Lifecycle Manager — `.github/workflows/issue-lifecycle.yml`

| Job | Tetikleyici | Ne yapar? |
|-----|-------------|-----------|
| `auto-label` | Issue **açıldığında** | 🔹 Formdaki **Sorumlu Ekip** seçimini okuyup `team:X` etiketini otomatik atar 🔹 `[RR]` açıldıysa body'deki `#123` parent issue'sunu bulup `state:revizyon` yapar + yorum atar |
| `on-rr-closed` | Issue **kapatıldığında** | `[RR]` kapandıysa parent issue'yu `state:başladı`'ya döndürür + yorum atar |
| `on-approve` | `state:onaylı` **etiketi eklenince** | "Talep onaylandı" yorumu atar |
| `on-test-result` | `event:test-geçti` / `event:test-kaldı` **etiketi eklenince** | Test sonucu yorumu atar |

### 2. CI — `.github/workflows/ci.yml`
`main`/`develop`'a push ve PR'da çalışır:
- **Lint:** `ruff check` + `black --check` (src/, tests/)
- **Test:** `pytest` — Python 3.10 / 3.11 / 3.12 matrisi, coverage
- **Build:** `python -m build` + artifact yükleme

### 3. Release — `.github/workflows/release.yml`
`main`'e her push'ta **Semantic Release** çalıştırır:
- Conventional commit'lere göre sürüm (patch/minor/major)
- `CHANGELOG.md` günceller ve otomatik commit yapar
- GitHub Release oluşturur

---

## 🔄 Issue Yaşam Döngüsü

```
ANALİZ → ONAYLI → ATANMIŞ → BAŞLAMADI → BAŞLADI
                                              ↓
                               KOD GÖZDEN GEÇİRME → TEST PLANI → TEST
                                              ↓ (başarısız)
                                             REVİZYON ───────────┐
                                              ↓                   │
                                     YAYIMLANMIŞ ←────────────────┘
```

**Durum nasıl ilerler?** `state:*` etiketi değiştirilerek. Otomasyon belirli geçişleri yapar:
- RR açılması → parent issue `state:revizyon`
- RR kapanması → parent issue `state:başladı`
- `state:onaylı` eklenmesi → onay bildirimi
- Test etiketi eklenmesi → sonuç bildirimi

**Revizyon kuralı:** Yeni issue açmayın — mevcut issue'yu revize edin (RR formu ile).

---

## 📐 Commit & Branch Stratejisi

**Commit mesajı — Conventional Commits:**

| Commit | Sürüm etkisi | Örnek |
|--------|--------------|-------|
| `fix:` | Patch (1.0.0 → 1.0.1) | `fix: tarih formatı güncellendi` |
| `feat:` | Minor (1.0.0 → 1.1.0) | `feat: ekip etiketi otomasyonu` |
| `feat!:` / `BREAKING CHANGE:` | Major (1.0.0 → 2.0.0) | `feat!: API yeniden tasarlandı` |
| `docs:` / `chore:` | Etkisiz | `docs: README güncellendi` |

**Branch adları:**
```
feature/TASK-123-yeni-ozellik
bugfix/TASK-456-hata-duzeltme
hotfix/TASK-789-acil-duzeltme
revision/TASK-100-doc-guncelleme
```

---

## ✅ PR Kontrol Listesi

`.github/PULL_REQUEST_TEMPLATE.md` her PR'da açılır:
- PR özeti + ilgili issue linkleri (`Closes #__`)
- Değişiklik türü seçimi
- Kod gözden geçirme kontrol listesi (genel/fonksiyonellik/güvenlik/dokümantasyon)
- Ekran görüntüleri
- Testing onayları
- Deploy notları (migration/env değişikliği vb.)
- Review isteği (kod inceleyici / QA / TL)

---

## 🛡️ Kalite Kapıları

- **Pre-commit hooks** (`.pre-commit-config.yaml`): trailing whitespace, EOF, YAML/JSON doğrulama, merge conflict, debug statement, black, ruff, mypy
- **CI:** lint + test (3 Python sürümü) + build
- **Kabul kriterleri** her issue'da test edilebilir şekilde zorunlu
- **Test planı** her TR içinde zorunlu

---

## 📂 Proje Yapısı

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/        # 4 issue formu + config.yml
│   │   ├── task_request.yml    # TR — Görev Talebi
│   │   ├── bug_report.yml      # BR — Hata Raporu
│   │   ├── revision_request.yml # RR — Revizyon Talebi
│   │   ├── qa_validation.yml   # QV — QA Doğrulama
│   │   └── config.yml          # blank issue kapalı + iletişim linkleri
│   ├── workflows/             # ci.yml · issue-lifecycle.yml · release.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   └── labels.yml             # 54 etiketin tek kaynağı
├── scripts/
│   └── setup_labels.py        # Etiket senkronizasyon script'i
├── docs/
│   ├── ARCHITECTURE.md        # SDLC mimari dokümanı
│   ├── LIFECYCLE.md           # Yaşam döngüsü rehberi
│   ├── GLOSSARY.md            # Kısaltmalar
│   ├── GITHUB_YUKLEME_REHBERI.md
│   └── templates/             # CHECKLIST.md · USAGE.md
├── src/                       # Kaynak kod (Python paketi)
├── tests/                     # Birim testleri
├── CHANGELOG.md               # Otomatik sürüm geçmişi
├── pyproject.toml
├── requirements*.txt
├── .pre-commit-config.yaml
├── .releaserc.json            # Semantic Release yapılandırması
├── Dockerfile / docker-compose.yml
└── README.md
```

---

## 🚀 Kurulum

```bash
# 1. Klonla
git clone https://github.com/G-Arya-A/task_template.git
cd task_template

# 2. Ortamı kur
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements-dev.txt

# 3. Pre-commit hook'larını kur
pre-commit install

# 4. (İlk seferde) etiketleri senkronize et
python scripts/setup_labels.py G-Arya-A/task_template
```

---

## 🧭 Hızlı Kullanım

1. **Yeni iş mi var?** → New Issue → **TR** formunu doldur (ekibi seç → etiket otomatik atanır)
2. **Hata mı bulundu?** → New Issue → **BR**
3. **Onaylı iş revize mi olacak?** → New Issue → **RR** (ilgili issue numarasını ver)
4. **İş test edilecek mi?** → New Issue → **QV**
5. Durumu `state:*` etiketiyle ilerlet, geliştirme bitince PR aç, CI geçsin, sürüm otomatik olsun.

---

## 📚 Dokümanlar

| Doküman | İçerik |
|---------|--------|
| `docs/ARCHITECTURE.md` | SDLC mimarisi, rol tanımları, otomasyon kataloğu |
| `docs/LIFECYCLE.md` | Adım adım yaşam döngüsü ve etiket kuralları |
| `docs/GLOSSARY.md` | Kısaltmalar sözlüğü |
| `docs/templates/USAGE.md` | Şablon kullanım rehberi |
| `docs/templates/CHECKLIST.md` | Kontrol listeleri |
| `docs/GITHUB_YUKLEME_REHBERI.md` | Repo kurulum rehberi |

---

## 📄 Lisans

Bu proje [MIT License](LICENSE) altında lisanslanmıştır.
