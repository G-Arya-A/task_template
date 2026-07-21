# Yaşam Döngüsü Rehberi (Lifecycle Guide)

## Issue Durum Akışı

### 1. ANALİZ
- Yeni bir task talebi (TR) veya hata raporu (BR) oluşturulur
- Talep formu eksiksiz doldurulur
- Takım lideri tarafından incelenir

### 2. ONAYLI
- Takım lideri talebi onaylar
- Öncelik ve hedef sürüm belirlenir
- `request_approved` olayı tetiklenir

### 3. ATANMIŞ
- Görev ilgili kişiye/gruba atanır
- Atanan kişi bilgilendirilir
- `assigned` olayı tetiklenir

### 4. BAŞLAMADI
- Atanmış ama henüz başlanmamış
- Kişi başlayacağı zaman durumu günceller

### 5. BAŞLADI (WIP)
- Çalışma devam ediyor
- Branch oluşturulur: `feature/TASK-{no}-{açıklama}`
- Düzenli commit'ler yapılır

### 6. KOD GÖZDEN GEÇİRME
- PR oluşturulur (`develop` dalına)
- Kod inceleyici atanır
- İnceleme yapılır
- Gerekli değişiklikler istenir

### 7. TEST PLANI
- Test senaryoları hazırlanır
- QA tarafından review edilir

### 8. TEST
- Testler çalıştırılır
- `test_passed` veya `test_failed` olayı tetiklenir

### 9. REVİZYON (gerekirse)
- Testler başarısız olursa veya değişiklik gerekirse
- Yeni issue açılmadan mevcut issue revize edilir
- Revizyon formu doldurulur
- İlgili kişiye atanır

### 10. YAYIMLANMIŞ
- Tüm kontroller başarılı
- `version_released` olayı tetiklenir
- Sürüm yayınlanır

---

## Olaylar (Events)

| Event | Tanım | Kaynak |
|-------|-------|--------|
| `request_approved` | Talep onaylandı | TL onayı |
| `test_passed` | Testler başarılı | CI/CD |
| `test_failed` | Testler başarısız | CI/CD |
| `version_released` | Sürüm yayımlandı | Semantic Release |
| `revision_requested` | Revizyon istendi | CR / Test |
| `assigned` | Kişilere atandı | TL |

---

## Etiket Kullanımı

Her durum bir etiket ile temsil edilir:

```
state:analiz
state:onaylı
state:atanmış
state:başlamadı
state:başladı
state:kod-gözden-geçirme
state:test-plani
state:test
state:revizyon
state:yayınlanmış
```

**Kural**: Her issue'da sadece **bir** `state:*` etiketi bulunmalıdır.

---

## Revizyon Akışı

```
Mevcut Issue → REVİZYON durumuna geç
    ↓
Revizyon Formu Doldur
    ↓
Revizyon Sorumlusuna Ata
    ↓
Değişiklikleri Yap
    ↓
KOD GÖZDEN GEÇİRME → TEST → YAYIMLANMIŞ
```

**Önemli**: Revizyon için yeni issue açmayın! Mevcut issue'yu revize edin.
