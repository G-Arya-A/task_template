# Kurumsal Yazılım Görev Yönetimi ve Yaşam Döngüsü Standardı (Task Template)

## 1. Doküman Amacı

Bu doküman; kurum içi yazılım geliştirme faaliyetlerinin **tek tip, izlenebilir ve otomatize**
bir süreç üzerinden yürütülmesini sağlayan standart şablonun tanımını, mimarisini ve kullanım
kurallarını resmi olarak açıklar.

Dokümanın hedef kitlesi; yazılım ekiplerinde görev alan tüm personel (talep sahipleri, takım
liderleri, geliştiriciler, kalite güvence mühendisleri, süreç yöneticileri) ile sürece dışarıdan
dahil olan paydaşlardır.

Bu standart, GitHub platformunun Issue, Label ve GitHub Actions altyapısı üzerinde çalışır ve
aşağıdaki kurumsal hedefleri garanti altına alır:

- Tüm iş taleplerinin **standart formlarla** ve **eksiksiz** kayıt altına alınması,
- Her işin yaşam döngüsü boyunca **tek bir görünür durum üzerinden** takip edilmesi,
- Sorumluluk, öncelik ve ekip atamalarının **otomatik ve tutarlı** biçimde yapılması,
- Yayınlanan her sürümün **izlenebilir bir geçmişe** sahip olması.

---

## 2. Kapsam ve Geçerlilik

Bu standart; kurum bünyesindeki tüm yazılım projelerinde ortak bir taban oluşturmak üzere
tasarlanmıştır. Standart; görev talebi (TR), hata raporu (BR), revizyon talebi (RR) ve kalite
doğrulama (QV) olmak üzere **dört resmi iş kaydı türü**, **54 standart etiket** ve **üç
otomasyon süreci** tanımlar.

Aşağıda sunulan tüm kurallar; aksi ayrıca ve yazılı olarak belirlenmedikçe bu standart
kapsamındaki her proje için bağlayıcıdır.

---

## 3. Temel Tanımlar ve Kısaltmalar

| Terim | Açılım | Açıklama |
|-------|--------|----------|
| **TR** | Task Request (Görev Talebi) | Yürütülmesi istenen işin resmi kaydı |
| **BR** | Bug Report (Hata Raporu) | Tespit edilen hatanın resmi kaydı |
| **RR** | Revision Request (Revizyon Talebi) | Mevcut bir iş kaydının revize edilmesi talebi |
| **QV** | QA Validation (Kalite Doğrulama) | İşin kabul kriterlerini sağladığının resmi doğrulaması |
| **AC** | Acceptance Criteria (Kabul Kriterleri) | İşin başarılı sayılması için sağlanması gereken koşullar |
| **PR** | Pull Request | Kod değişikliğinin incelemeye sunulduğu birleştirme isteği |
| **TL** | Team Lead (Takım Lideri) | Onay ve atama yetkisine sahip süreç sorumlusu |
| **QA** | Quality Assurance (Kalite Güvence) | Test ve doğrulama faaliyetlerinin yürütücüsü |
| **CI** | Continuous Integration | Sürekli entegrasyon; kod bütünlüğünü otomatik doğrular |
| **WIP** | Work In Progress | Üzerinde çalışılan, devam eden iş |
| **P1–P4** | Priority Level (Öncelik Düzeyi) | Aciliyet derecelendirmesi |

---

## 4. Süreç Mimarisi

### 4.1. Genel Bakış

Süreç; bir iş kaydının oluşturulması ile başlar, sıralı ve onaylı aşamalardan geçer ve
sürümün yayımlanması ile sonlanır. Tüm aşamalar GitHub üzerinde **etiketlerle** temsil edilir;
durum değişiklikleri etiket değişikliği ile gerçekleştirilir.

```
Oluşturma → Analiz → Onay → Atama → Başlama → Geliştirme
    → Kod İnceleme → Test Planı → Test → Yayımlama
```

Herhangi bir aşamada tespit edilen eksiklik, **revizyon** mekanizması ile mevcut kayıt
üzerinden çözülür. Bu amaçla yeni bir iş kaydı oluşturulmaz.

### 4.2. Yaşam Döngüsü Durumları

| # | Durum | Etiket | Tanım |
|---|-------|--------|-------|
| 1 | Analiz | `state:analiz` | Kayıt oluşturuldu; değerlendirme bekliyor |
| 2 | Onaylı | `state:onaylı` | Takım lideri tarafından onaylandı |
| 3 | Atanmış | `state:atanmış` | Sorumlu kişiye/gruplara atandı |
| 4 | Başlamadı | `state:başlamadı` | Atandı, henüz çalışmaya başlanmadı |
| 5 | Başladı | `state:başladı` | Çalışma devam ediyor (WIP) |
| 6 | Kod Gözden Geçirme | `state:kod-gözden-geçirme` | Kod incelemesi yapılıyor |
| 7 | Test Planı | `state:test-plani` | Test senaryoları hazırlanıyor |
| 8 | Test | `state:test` | Testler uygulanıyor |
| 9 | Revizyon | `state:revizyon` | Eksiklik tespit edildi; düzeltme gerekiyor |
| 10 | Yayımlanmış | `state:yayınlanmış` | İş tamamlandı ve sürüme dahil edildi |

**Kural:** Herhangi bir iş kaydında aynı anda yalnızca **bir** durum etiketi (`state:*`)
bulunabilir.

### 4.3. Rol ve Sorumluluklar

| Rol | Yetki ve Sorumluluklar |
|-----|------------------------|
| **Talep Sahibi** | İş gereksinimini tanımlar; kabul kriterlerini belirler; formu eksiksiz doldurur |
| **Takım Lideri (TL)** | Kaydı analiz eder; onaylar; önceliği ve sorumlu ekibi netleştirir; atamayı yapar |
| **Geliştirici** | İşi uygular; kodu ve testleri yazar; dokümantasyonu günceller; revizyonları tamamlar |
| **Kod İnceleyici** | Değişikliği gözden geçirir; geri bildirim sağlar; onay verir |
| **QA Mühendisi** | Test planını uygular; sonucu QV kaydı ile resmi olarak doğrular |
| **Süreç Yöneticisi** | Standartta değişiklik yapar; etiketleri ve otomasyonları yönetir |

---

## 5. İş Kaydı Türleri (Issue Formları)

Platformda **New Issue** aracılığıyla dört standart form sunulur. Boş (formatsız) issue
oluşturma **kapalıdır**; tüm kayıtlar bu formlar üzerinden üretilmelidir.

### 5.1. TR — Görev Talebi `[TR]`

Süreçteki temel iş kaydıdır. İş türü ayrımı; aşağıda listelenen talep türü seçeneği ile
yapılır. Varsayılan etiketler: `state:analiz`, `type:görev`, `priority:P3`.

**Talep Türü Seçenekleri:**

| Talep Türü | Kullanım Amacı |
|------------|----------------|
| Yeni Özellik | Mevcut sisteme yeni bir yetenek eklenmesi |
| Hata Düzeltme | Tespit edilen bir hatanın giderilmesi |
| Kod/Yapı Yeniden Düzenleme | Davranış değiştirmeden kod yapısının iyileştirilmesi |
| Araştırma/Keşif (zaman kutusu) | Belirsizliği gidermek için sınırlı süreli inceleme |
| Risk Azaltma | Tespit edilen bir riskin etkisinin azaltılması |
| İş Gereksinimi | Bir iş ihtiyacının iş değeri ile birlikte kayıt altına alınması |
| Soru / Açıklama | Bir konunun netleştirilmesi |
| Diğer | Yukarıdaki kategorilere uymayan işler |

**Form Bölümleri:**

| Bölüm | İçerik | Zorunluluk |
|-------|--------|------------|
| 1. Temel Bilgiler | Talep Sahibi, Talep Türü, Öncelik | Zorunlu |
| 2. İş Gereksinimi | İş problemi, iş değeri/gerekçe | Zorunlu |
| 3. Teknik Kapsam | Teknik açıklama, kapsam, araştırma ve açık sorular | Kısmi |
| 4. Risk ve Geri Dönüş | Riskler ve azaltma önlemleri, orijinal sürüm yedeği, geri dönüş planı | Zorunlu |
| 5. Kabul Kriterleri | Test edilebilir kabul koşulları | Zorunlu |
| 6. Test Planı | Uygulanacak test senaryoları | Zorunlu |
| 7. Organizasyon | Sorumlu Ekip, atanacak kişi, son tarih, bağımlılıklar, dokümanlar | Kısmi |
| 8. Notlar | Ek notlar, kısıtlar, varsayımlar ve kontrol listesi | İsteğe bağlı |

**Sorumlu Ekip Seçenekleri (Organizasyon Yapısı):**

`PY` · `AYG` · `FYYG` · `GSYG` · `IMYG` · `K2` · `OYG` · `PSYG` · `SSYG` · `SYG` · `YMG` ·
`YSYG` · `YTO` · `ST` · `SSG-STAGY`

> **Otomasyon Notu:** TR formunda bir ekip seçildiğinde, seçime karşılık gelen `team:<ekip>`
> etiketi kayda **otomatik olarak** eklenir.

**Tarih Formatı:** Tüm tarih alanlarında zorunlu biçim `GG/AA/YYYY`'dir.

### 5.2. BR — Hata Raporu `[BR]`

Mevcut bir davranışın hatası olarak raporlanması için kullanılır.
Varsayılan etiketler: `state:analiz`, `type:hata`, `priority:P2`.

**Form Bölümleri:** İlgili Görev (TR) · Raporlayan · Hata Önemi · Hata Açıklaması · Tekrar
Oluşturma Adımları · Beklenen Davranış · Gerçekleşen Davranış · Ortam Bilgisi · Ekran
Görüntüleri/Loglar · İletişim Kanalı · Hata Kontrol Listesi.

**Hata Önemi Derecelendirmesi:** Kritik (sistem durdurucu) · Yüksek (temel özellik çalışmıyor) ·
Orta (kısmi çalışma sorunu) · Düşük (kozmetik/küçük sorun).

> **Otomasyon Notu:** BR formundaki "İlgili Görev (TR)" alanı `#<numara>` biçiminde
> girildiğinde otomasyon; ilgili iş kaydına `type:hata` etiketi ekler, kaydı `state:revizyon`
> durumuna alır ve bilgilendirme yorumu yazar.

### 5.3. RR — Revizyon Talebi `[RR]`

Tamamlanmış veya devam eden bir iş kaydının düzeltilmesi gerektiğinde kullanılır.
**Bu form yeni bir iş kaydı oluşturmaz; ilgili mevcut kaydı revize eder.**

Varsayılan etiketler: `state:revizyon`, `type:revizyon`.

**Form Bölümleri:** İlgili Issue Numarası · Revizyon Talep Eden · Revize Kategorisi · Revizyon
Önemi · Revizyon Sebebi · Mevcut Durum (As-is) · İstenen Durum (To-be) · Revize Kabul Kriterleri
· Revizyon Sorumlusu.

**Revize Kategorileri:** Doküman · Hata Düzeltme · İyileştirme · Yeniden Yapılanma ·
Gereksinim Değişikliği · Performans · Güvenlik · Uyumluluk.

> **Otomasyon Notu:** RR formundaki "İlgili Issue Numarası" alanı `#<numara>` biçiminde girilir.
> Otomasyon; RR açıldığında ilgili kaydı `state:revizyon` durumuna, RR kapandığında ise
> `state:başladı` durumuna getirir ve her iki işlemi yorum olarak kaydeder.

### 5.4. QV — QA Doğrulama `[QV]`

Tamamlanmış bir işin kabul kriterlerini sağladığının kalite güvence tarafından resmi olarak
belgelendiği kayıttır. **Test planı ilgili TR kaydı içinde tutulur; QV yalnızca sonucu doğrular.**

Varsayılan etiketler: `state:test-plani`, `type:doğrulama`.

**Form Bölümleri:** İlgili Görev (TR) · İlgili PR · QA Mühendisi · Yapı Sürümü · Test Ortamı ·
Test Tarihi · Genel Sonuç · Başarısız Senaryolar · Regresyon Değerlendirmesi · Öneri · QA Onayı
· Onay Tarihi · Test Notları.

**Genel Sonuç Seçenekleri:** GEÇTİ (tüm kriterler sağlandı) · GEÇTİ (kritik kriterler sağlandı,
kritik olmayan sorunlar belgelendi) · KALDI (bir veya daha fazla kriter sağlanmadı) · ENGELLİ
(doğrulama gerçekleştirilemiyor).

> **Otomasyon Notu:** QV formundaki "Genel Sonuç" seçimine göre otomasyon; **GEÇTİ**'de QV'ye
> `event:test-geçti` etiketi atar ve ilgili TR'yi `state:yayınlanmış` durumuna getirir,
> **KALDI**'da QV'ye `event:test-kaldı` etiketi atar ve ilgili TR'yi düzeltme için `state:başladı`
> durumuna döndürür (resmi revizyon talebi `state:revizyon` olarak ayrı kalır). **ENGELLİ**'de
> ek etiket atanmaz; yalnızca kayıt tutulur.

---

## 6. Etiket Sistemi (Label Standardı)

Tüm etiketler, tek yetkili kaynak olan `.github/labels.yml` dosyasında tanımlanır. Etiketler;
durum, tip, öncelik, revizyon kategorisi, olay, ekip ve doküman yönü olmak üzere **yedi
kategorik grupta** toplanır. Repo üzerindeki 54 etiket, bu dosya ile birebir senkronizedir.

| Kategori | Önek | Kapsam | Örnekler |
|----------|------|--------|----------|
| Durum | `state:` | Yaşam döngüsü pozisyonu | `state:analiz`, `state:onaylı`, `state:başladı`, `state:yayınlanmış` |
| Tip | `type:` | İş kaydı türü | `type:görev`, `type:hata`, `type:revizyon`, `type:doğrulama` |
| Öncelik | `priority:` | Aciliyet | `priority:P1` … `priority:P4` |
| Revizyon | `rev:` | Revizyon kategorisi | `rev:doküman`, `rev:hata-düzeltme`, `rev:güvenlik` |
| Olay | `event:` | Otomasyon tetikleyicileri | `event:test-geçti`, `event:test-kaldı`, `event:sürüm-yayınlandı` |
| Ekip | `team:` | Sorumlu birim | `team:PY`, `team:AYG`, `team:SSG-STAGY` |
| Doküman | `doc:` | Doküman yönü | `doc:gelen`, `doc:gönderilen`, `doc:revize` |

**Öncelik Derecelendirmesi:**

| Seviye | Anlam | Kullanım |
|--------|-------|----------|
| **P1** | Kritik | Acil; sistem durdurucu |
| **P2** | Yüksek | Mühim; kısa sürede yapılmalı |
| **P3** | Orta | Normal plan dahilinde |
| **P4** | Düşük | Fırsat olduğunda |

**Etiket Yönetimi:** Etiketlerde değişiklik yapılması gerektiğinde `.github/labels.yml`
güncellenir ve `python scripts/setup_labels.py <owner/repo>` komutu ile GitHub'a senkronize
edilir. Etiket adları üzerinde yetkisiz değişiklik yapılamaz; otomasyon etiket adlarına
bağımlıdır.

---

## 7. Otomasyon Altyapısı (GitHub Actions)

Süreç; aşağıda açıklanan üç iş akışı (workflow) ile otomatikleştirilmiştir. Bu iş akışları
repo üzerinde yayınlandığı anda GitHub tarafından aktif edilir.

### 7.1. Issue Yaşam Döngüsü Yöneticisi
`/.github/workflows/issue-lifecycle.yml`

| İş Akışı | Tetikleyici Olay | Gerçekleştirilen İşlem |
|----------|------------------|------------------------|
| `auto-label` | Issue oluşturulduğu an | Formdaki Sorumlu Ekip seçiminden `team:<ekip>` etiketi otomatik atanır. `[RR]` açıldıysa ilgili kayıt `state:revizyon` durumuna alınır. `[BR]` açıldıysa ilgili kayda `type:hata` eklenir ve `state:revizyon` yapılır. `[QV]` açıldıysa sonuca göre QV'ye `event:test-geçti` / `event:test-kaldı` etiketi atanır ve ilgili TR `state:yayınlanmış` / `state:başladı` durumuna getirilir. |
| `on-rr-closed` | Issue kapatıldığı an | `[RR]` kaydı kapatıldıysa ilgili iş kaydı `state:başladı` durumuna döndürülür ve bilgilendirme yorumu yazılır. |
| `on-approve` | `state:onaylı` etiketi eklendiği an | "Talep onaylandı" bildirim yorumu oluşturulur. |
| `on-test-result` | `event:test-geçti` / `event:test-kaldı` etiketi eklendiği an | Test sonucu bildirim yorumu oluşturulur. |

### 7.2. Sürekli Entegrasyon (CI)
`/.github/workflows/ci.yml`

`main` ve `develop` dallarına gönderilen her değişiklik ile her PR üzerinde çalışır:

| Adım | Araç | Kapsam |
|------|------|--------|
| Statik analiz ve biçimlendirme | Ruff, Black | `src/`, `tests/` |
| Test | Pytest | Python 3.10 / 3.11 / 3.12, kod kapsama raporu |
| Paketleme | `python -m build` | Derleme çıktısının arşivlenmesi |

CI'nın başarısız olması durumunda değişiklik yayımlanamaz; ilgili kayıt revizyon sürecine
alınır.

### 7.3. Otomatik Sürüm Yönetimi (Release)
`/.github/workflows/release.yml`

`main` dalına gönderilen her değişiklikte **Semantic Release** çalıştırılır:

| Commit Türü | Sürüm Etkisi | Örnek |
|-------------|--------------|-------|
| `fix:` | Patch (1.0.0 → 1.0.1) | `fix: tarih formatı güncellendi` |
| `feat:` | Minor (1.0.0 → 1.1.0) | `feat: ekip etiketi otomasyonu` |
| `feat!:`, `BREAKING CHANGE:` | Major (1.0.0 → 2.0.0) | `feat!: API yeniden tasarlandı` |
| `docs:`, `chore:` | Sürüm etkisiz | `docs: doküman güncellendi` |

Sürüm oluşturulduğunda; `CHANGELOG.md` güncellenir, ilgili commit otomatik yazılır ve GitHub
Release kaydı oluşturulur.

---

## 8. Sürüm Yönetimi ve Değişiklik Kuralları

Sürümler, **Semantic Versioning (SemVer)** ilkesine göre otomatik olarak üretilir ve yalnızca
`main` dalı üzerinden yayımlanır. Sürüm numaraları; commit mesajlarının türüne göre belirlenir
(Bölüm 7.3).

**Commit Mesaj Standardı:** Tüm commit'ler aşağıdaki biçime uymalıdır:

```
<tür>: <açıklama>
```

Örnekler: `feat: ...`, `fix: ...`, `docs: ...`, `refactor: ...`, `test: ...`, `chore: ...`.

**Dal (Branch) Adlandırma Standardı:**

| Dal Öneki | Kullanım |
|-----------|----------|
| `feature/` | Yeni özellik geliştirmesi |
| `bugfix/` | Hata düzeltmesi |
| `hotfix/` | Acil üretim düzeltmesi |
| `revision/` | Revizyon kapsamındaki değişiklik |

---

## 9. Kod İnceleme (Pull Request) Süreci

Her değişiklik, `.github/PULL_REQUEST_TEMPLATE.md` şablonu üzerinden PR olarak sunulur.
Şablon; aşağıdaki bölümleri zorunlu kılar:

1. **PR Özeti** — değişikliğin amacı,
2. **İlgili Issue'lar** — `Closes #__` / `Related to #__` bağlantıları,
3. **Değişiklik Türü** — feat / fix / refactor / docs / test / chore,
4. **Kod Gözden Geçirme Kontrol Listesi** — genel, fonksiyonellik, güvenlik, dokümantasyon,
5. **Testing** — birim, entegrasyon, manuel test onayları,
6. **Deploy Notları** — migration, ortam değişkeni, yapılandırma değişiklikleri,
7. **Review İsteği** — kod inceleyici, QA ve TL onay alanları.

Bir PR; CI süreçlerinden geçmeden, kod inceleme onayı alınmadan ve QA doğrulaması
tamamlanmadan birleştirilemez.

---

## 10. Kalite Güvence Standardı

İşin yayımlanabilir sayılması için aşağıdaki koşulların tamamının sağlanması gerekir:

- Tüm kabul kriterlerinin test planı üzerinden uygulanmış ve doğrulanmış olması,
- Test planının kabul kriterlerini eksiksiz kapsaması,
- Kod incelemesinin tamamlanmış ve onaylanmış olması,
- CI sürecinin (lint, test, build) başarılı olması,
- Orijinal sürüm yedeğinin ve geri dönüş planının tanımlı olması,
- Değişiklikle ilgili risk değerlendirmesinin yapılmış olması.

**Kalite Kapıları (Quality Gates):**

| Katman | Araç/Süreç | Görev |
|--------|-----------|-------|
| Yerel | Pre-commit hooks | Biçim, sözdizimi, merge çakışması, hata ayıklama kalıntısı kontrolü |
| Sürekli | CI pipeline | Statik analiz, test matrisi, paketleme |
| İnceleme | PR onayı | Kod gözden geçirme kontrol listesi |
| Doğrulama | QV kaydı | Kabul kriterlerinin resmi doğrulaması |

---

## 11. Kurulum ve Yapılandırma

### 11.1. Ortam Kurulumu

```bash
# 1. Kaynak kod deposunu klonlayın
git clone https://github.com/G-Arya-A/task_template.git
cd task_template

# 2. Sanal ortam oluşturun ve bağımlılıkları kurun
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements-dev.txt

# 3. Pre-commit hook'larını aktif edin
pre-commit install
```

### 11.2. Etiket Senkronizasyonu

Etiketler, tek yetkili kaynak olan `.github/labels.yml` üzerinden yönetilir. Etiketlerde
değişiklik yapıldığında senkronizasyon aşağıdaki komutla gerçekleştirilir:

```bash
python scripts/setup_labels.py <owner/repo>
```

Senkronizasyon; yeni etiketleri oluşturur, değişenleri günceller ve eksik olanları atlar.
Yetkisiz etiket oluşturulması veya silinmesi; otomasyonun çalışma bütünlüğünü bozabileceği
için yasaktır.

---

## 12. Günlük Kullanım Prosedürü

Aşağıdaki akış, sürece dahil olan tüm personel için geçerli resmi kullanım prosedürüdür:

| Adım | İşlem | Yöntem |
|------|-------|--------|
| 1 | Yeni iş talebi | `New Issue` → **TR** formu (ekip seçimi etiketi otomatik atar) |
| 2 | Hata bildirimi | `New Issue` → **BR** formu |
| 3 | Revizyon gereksinimi | `New Issue` → **RR** formu (ilgili kayıt numarası ile) |
| 4 | Test doğrulaması | `New Issue` → **QV** formu |
| 5 | Durum güncelleme | `state:*` etiketi değiştirilerek |
| 6 | Kod değişikliği | Standart dal adı + conventional commit + PR |
| 7 | Yayımlama | `main` dalına birleştirme sonrası otomatik sürüm |

**Yasaklar ve Bağlayıcı Kurallar:**

- Formlar dışında (boş issue) kayıt oluşturulamaz.
- Bir kayıtta birden fazla `state:*` etiketi bulunamaz.
- Revizyon için yeni kayıt oluşturulamaz; mevcut kayıt revize edilir.
- Tarih alanları `GG/AA/YYYY` biçiminde doldurulur.
- Otomasyonun bağlı olduğu etiket adları değiştirilemez veya silinemez.

---

## 13. Proje Dosya Yapısı

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/          # TR, BR, RR, QV formları + config.yml
│   ├── workflows/               # ci.yml · issue-lifecycle.yml · release.yml
│   ├── PULL_REQUEST_TEMPLATE.md # PR inceleme şablonu
│   ├── CODEOWNERS               # Kod sahipliği tanımları
│   └── labels.yml               # 54 etiketin tek yetkili kaynağı
├── scripts/
│   └── setup_labels.py          # Etiket senkronizasyon aracı
├── docs/
│   ├── ARCHITECTURE.md          # Süreç mimarisi ve otomasyon kataloğu
│   ├── LIFECYCLE.md             # Yaşam döngüsü rehberi
│   ├── GLOSSARY.md              # Terimler sözlüğü
│   ├── GITHUB_YUKLEME_REHBERI.md # Repo kurulum rehberi
│   └── templates/               # CHECKLIST.md · USAGE.md
├── src/                         # Uygulama kaynak kodu
├── tests/                       # Birim testleri
├── CHANGELOG.md                 # Otomatik sürüm geçmişi
├── pyproject.toml               # Paket ve araç yapılandırması
├── requirements*.txt            # Bağımlılık tanımları
├── .pre-commit-config.yaml      # Yerel kalite kapıları
├── .releaserc.json              # Sürüm otomasyonu yapılandırması
├── Dockerfile / docker-compose.yml
└── README.md                    # Bu doküman
```

---

## 14. Referans Dokümanlar

| Doküman | Konusu |
|---------|--------|
| `docs/ARCHITECTURE.md` | Süreç mimarisi, rol tanımları, otomasyon kataloğu |
| `docs/LIFECYCLE.md` | Adım adım yaşam döngüsü ve etiket kuralları |
| `docs/templates/USAGE.md` | Form kullanım rehberi |
| `docs/templates/CHECKLIST.md` | Kontrol listeleri |
| `docs/GLOSSARY.md` | Kısaltma ve terimler sözlüğü |
| `CHANGELOG.md` | Sürüm geçmişi |

---

## 15. Yürürlük ve Değişiklik Yönetimi

Bu standart; süreç yöneticisi ve ilgili takım liderleri tarafından yönetilir. Standartta
yapılacak her türlü değişiklik; `docs/ARCHITECTURE.md` ve ilgili yapılandırma dosyalarının
güncellenmesini ve bu dokümanın değişiklik kaydına işlenmesini gerektirir. Etiket ve otomasyon
değişiklikleri, mevcut iş kayıtlarını etkileyebileceği için kontrollü biçimde uygulanır.

---

## 16. Lisans

Bu standart ve şablon kodu [MIT License](LICENSE) koşulları altında dağıtılmaktadır.
