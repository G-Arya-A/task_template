# Yazılım Projesi - Kurumsal Şablon

> **Şirket İçi Standart Yazılım Yaşam Döngüsü Şablonu**

Bu şablon, şirket içerisindeki tüm yazılım projeleri için ortak bir yaşam döngüsü, issue yönetimi ve kalite kontrol süreci sunar.

---

## Proje Yapısı

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/       # Issue şablonları
│   │   ├── task_request.yml   # Görev talebi
│   │   ├── revision_request.yml # Revizyon talebi
│   │   ├── bug_report.yml     # Hata raporu
│   │   └── config.yml         # Şablon yapılandırması
│   ├── workflows/             # CI/CD otomasyonları
│   │   ├── ci.yml             # Sürekli entegrasyon
│   │   └── release.yml        # Sürüm yayımlama
│   ├── CODEOWNERS             # Kod sahipliği tanımları
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── labels.yml             # Yaşam döngüsü etiketleri
├── src/                       # Kaynak kodlar
├── tests/                     # Test dosyaları
├── docs/                      # Dokümantasyon
│   ├── GLOSSARY.md            # Kısaltmalar ve terimler
│   ├── LIFECYCLE.md           # Yaşam döngüsü akışı
│   └── templates/             # Şirket içi şablonlar
├── pyproject.toml
├── requirements-dev.txt
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Kısaltmalar ve Anlamları (Glossary)

| Kısaltma | Açıklama |
|----------|----------|
| **TR** | Task Request - Görev Talebi |
| **RR** | Revision Request - Revizyon Talebi |
| **BR** | Bug Report - Hata Raporu |
| **AC** | Acceptance Criteria - Kabul Kriterleri |
| **CL** | Control List - Kontrol Listesi |
| **SME** | Subject Matter Expert - Konu Uzmanı |
| **TL** | Team Lead - Takım Lideri |
| **QA** | Quality Assurance - Kalite Güvence |
| **CR** | Code Review - Kod Gözden Geçirme |
| **CI** | Continuous Integration - Sürekli Entegrasyon |
| **CD** | Continuous Deployment - Sürekli Dağıtım |
| **PR** | Pull Request - Çekme İsteği |
| **UR** | Unit Test - Birim Testi |
| **IT** | Integration Test - Entegrasyon Testi |
| **ST** | System Test - Sistem Testi |
| **UAT** | User Acceptance Test - Kullanıcı Kabul Testi |
| **REQ** | Requirement - Gereksinim |
| **P1** | Öncelik Seviyesi 1 - Kritik |
| **P2** | Öncelik Seviyesi 2 - Yüksek |
| **P3** | Öncelik Seviyesi 3 - Orta |
| **P4** | Öncelik Seviyesi 4 - Düşük |
| **RSL** | Released - Yayımlanmış |
| **REV** | Revision - Revizyon |
| **WIP** | Work In Progress - Çalışma Devam Ediyor |

---

## Yazılım Yaşam Döngüsü (Issue Lifecycle)

### Durumlar (States)

```
┌─────────────┐
│  ANALİZ     │ ← Yeni task talebi oluşturulur
└──────┬──────┘
       ▼
┌─────────────┐
│  ONAYLI     │ ← Takım lideri tarafından onaylanır
└──────┬──────┘
       ▼
┌─────────────┐
│  ATANMIŞ    │ ← İlgili kişiye/grupta assign edilir
└──────┬──────┘
       ▼
┌─────────────┐
│ BAŞLAMADI   │ ← Atanmış ama henüz başlanmamış
└──────┬──────┘
       ▼
┌─────────────┐
│  BAŞLADI    │ ← Çalışma devam ediyor (WIP)
└──────┬──────┘
       ▼
┌─────────────┐
│    KOD      │ ← Kod gözden geçirme aşamasında
│ GÖZDEN      │
│ GEÇİRME    │
└──────┬──────┘
       ▼
┌─────────────┐
│ TEST PLANI  │ ← Test senaryoları hazırlanıyor
└──────┬──────┘
       ▼
┌─────────────┐
│    TEST     │ ← Testler çalışıyor
└──────┬──────┘
       ▼
┌─────────────┐
│  REVİZYON   │ ← Değişiklik gerektiriyor (yeni issue açmadan)
└──────┬──────┘
       ▼
┌─────────────┐
│ YAYIMLANMIŞ │ ← Sürüm yayımlandı (RSL)
└─────────────┘
```

### Olaylar (Events)

| Event | Açıklama | Tetikleyici |
|-------|----------|-------------|
| `request_approved` | Talep onaylandı | TL onayı |
| `test_passed` | Testler başarılı | CI/CD pipeline |
| `test_failed` | Testler başarısız | CI/CD pipeline |
| `version_released` | Sürüm yayımlandı | Semantic Release |
| `revision_requested` | Revizyon istendi | CR / Test sonucu |
| `assigned` | Kişilere atandı | TL tarafından |

### Revizyon Akışı

Revizyon durumunda **yeni issue açılmadan** mevcut issue revize edilir:

1. Issue `REVİZYON` durumuna geçer
2. Revizyon formu doldurulur:
   - **Talep Sahibi**: Revizyonu kim istedi
   - **Sebep**: Revizyon nedeni
   - **Revize Kategorisi**: Doküman / Debug / Enhancement / Refactoring
   - **Açıklama**: Detaylı değişiklik açıklaması
3. İlgili kişiye assign edilir
4. Değişiklikler yapılır
5. Tekrar `KOD GÖZDEN GEÇİRME` aşamasına dönülür

---

## Kabul Kriterleri (Acceptance Criteria)

Başarılı sayılıması için gereken koşullar:

### Zorunlu Koşullar
- [ ] Tüm acceptance criteria karşılanmış olmalı
- [ ] Kod gözden geçirme (CR) onayı alınmış olmalı
- [ ] Birim testleri (UR) %80+ coverage ile geçmeli
- [ ] Entegrasyon testleri (IT) başarılı olmalı
- [ ] CI pipeline'ı yeşil olmalı
- [ ] Documenter updated olmalı (gerekliyse)

### Sorumluluk Alanları

| Rol | Sorumluluk |
|-----|-----------|
| **Talep Sahibi** | Gereksinimleri tanımlamak, acceptance criteria belirlemek |
| **Takım Lideri (TL)** | Task'ı onaylamak, kişilere atamak, öncelik belirlemek |
| **Geliştirici** | Kodu yazmak, testleri oluşturmak, dokümantasyonu güncellemek |
| **Kod Gözden Geçirici** | Kodu incelemek, geri bildirim vermek |
| **QA** | Test senaryolarını oluşturmak, testleri çalıştırmak |
| **Konu Uzmanı (SME)** | Alan bilgisi sağlamak, kabul testlerine katılmak |

---

## İletişim Kanalları

| Kanal | Amaç | Link |
|-------|------|------|
| **Genel Chat** | Günlük iletişim | `[TEAM_CHAT_LINK]` |
| **Tech Chat** | Teknik tartışmalar | `[TECH_CHAT_LINK]` |
| **Proje Kanalı** | Proje özelinde iletişim | `[PROJECT_CHANNEL_LINK]` |
| **Acil Durum** | Kritik sorunlar | `[EMERGENCY_CHANNEL_LINK]` |

---

## Doküman Kategorileri

| Kategori | Açıklama |
|----------|----------|
| **Gelen** | Dışarıdan gelen dokümanlar, spekülatif dokümanlar |
| **Girdi Yapılan** | Proje içerisine bilgi girdisi sağlayan dokümanlar |
| **Gönderilen** | Dışarıya gönderilen dokümanlar |
| **Revize** | Güncellenmiş/revizyonu yapılmış dokümanlar |

---

## Versiyonlama

Otomatik versiyonlama **Semantic Release** ile yapılır:

| Commit Mesajı | Versiyon Etkisi | Örnek |
|---------------|-----------------|-------|
| `fix: ...` | Patch (1.0.0 → 1.0.1) | Hata düzeltmesi |
| `feat: ...` | Minor (1.0.0 → 1.1.0) | Yeni özellik |
| `feat!: ...` / `BREAKING CHANGE:` | Major (1.0.0 → 2.0.0) | Kırıcı değişiklik |
| `docs: ...` | Versiyon etkilemez | Doküman güncellemesi |
| `chore: ...` | Versiyon etkilemez | Bakım çalışmaları |

---

## Hızlı Başlangıç

```bash
# 1. Depoyu klonlayın
git clone https://github.com/[ORG]/yazılım_github_örnek.git
cd yazılım_github_örnek

# 2. Ortamı kurun
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements-dev.txt

# 3. Pre-commit hook'larını kurun
pre-commit install

# 4. Geliştirmeye başlayın
```

---

## License

Bu proje [MIT License](LICENSE) altında lisanslanmıştır.
