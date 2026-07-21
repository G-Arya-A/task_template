# Şablon Kullanım Rehberi

## Issue Oluşturma

### Yeni Görev Talebi (Task Request)
1. `Issues` sekmesine gidin
2. `New Issue` butonuna tıklayın
3. `TR - Task Request (Görev Talebi)` şablonunu seçin
4. Formu eksiksiz doldurun
5. Submit edin

### Revizyon Talebi (Revision Request)
1. İlgili issue'yu açın
2. `New Issue` ile `RR - Revision Request` şablonunu seçin
3. İlgili issue numarasını girin
4. Revizyon formunu doldurun
5. Submit edin

### Hata Raporu (Bug Report)
1. `Issues` sekmesine gidin
2. `New Issue` butonuna tıklayın
3. `BR - Bug Report (Hata Raporu)` şablonunu seçin
4. Hatayı detaylı açıklayın
5. Submit edin

---

## Durum Güncelleme

Issue'ların durumunu güncellemek için etiketleri kullanın:

```
state:analiz         → Analiz aşamasında
state:onaylı         → Onaylandı
state:atanmış        → Atandı
state:başlamadı      → Başlanmadı
state:başladı        → Başladı
state:kod-gözden-geçirme → Kod incelemede
state:test-plani     → Test planı hazırlanıyor
state:test           → Test aşamasında
state:revizyon       → Revizyon gerekli
state:yayınlanmış    → Yayımlandı
```

**Kural**: Her issue'da sadece **bir** `state:*` etiketi olmalıdır.

---

## Branch Oluşturma

```
feature/TASK-123-yeni-ozellik
bugfix/TASK-456-hata-duzeltme
hotfix/TASK-789-acil-duzeltme
revision/TASK-100-doc-guncelleme
```

---

## PR Oluşturma

1. Branch'inizi `develop` dalına açın
2. PR şablonunu eksiksiz doldurun
3. İlgili issue'ları linkleyin
4. İnceleyici atayın

---

## Versiyonlama

Otomatik versiyonlama Semantic Release ile yapılır:

| Commit | Versiyon |
|--------|----------|
| `fix: hata düzeltme` | Patch (1.0.0 → 1.0.1) |
| `feat: yeni özellik` | Minor (1.0.0 → 1.1.0) |
| `feat!: breaking change` | Major (1.0.0 → 2.0.0) |
