# Katkıda Bulunma Rehberi (Contributing Guide)

Teşekkürler! Bu projeye katkıda bulunmayı düşünmeniz harika.

## Geliştirme Ortamı Kurulumu

```bash
# 1. Depoyu fork edin ve klonlayın
git clone https://github.com/[FORK_USER]/yazilim-github-ornek.git
cd yazilim-github-ornek

# 2. Sanal ortam oluşturun
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Bağımlılıkları kurun
pip install -r requirements-dev.txt

# 4. Pre-commit hook'larını kurun
pre-commit install
```

## Branch Akışı

```
main          ← Yayımlanmış sürümler
  └── develop ← Geliştirme dalı
       ├── feature/TASK-123-yeni-ozellik
       ├── bugfix/TASK-456-hata-duzeltme
       └── hotfix/TASK-789-acil-duzeltme
```

## Branch İsimlendirme

| Branch Türü | Format | Örnek |
|-------------|--------|-------|
| Yeni Özellik | `feature/TASK-{no}-{açıklama}` | `feature/TASK-123-yeni-login` |
| Hata Düzeltme | `bugfix/TASK-{no}-{açıklama}` | `bugfix/TASK-456-null-check` |
| Acil Düzeltme | `hotfix/TASK-{no}-{açıklama}` | `hotfix/TASK-789-guvenlik` |
| Revizyon | `revision/TASK-{no}-{açıklama}` | `revision/TASK-100-doc-guncelleme` |

## Commit Mesajı Formatı

```
<type>(<scope>): <description>

<body>

<footer>
```

### Type'lar

| Type | Açıklama | Versiyon Etkisi |
|------|----------|-----------------|
| `feat` | Yeni özellik | Minor (x.**Y**.0) |
| `fix` | Hata düzeltme | Patch (x.y.**Z**) |
| `docs` | Doküman | Yok |
| `style` | Kod stili | Yok |
| `refactor` | Yeniden yapılandırma | Yok |
| `test` | Test | Yok |
| `chore` | Bakım | Yok |
| `perf` | Performans | Patch |
| `ci` | CI/CD | Yok |

### Breaking Change

```bash
feat(api): yeni endpoint eklendi

BREAKING CHANGE: eski /api/v1/ endpoint'i kaldırıldı
```

## Pull Request Kuralları

1. PR'ı `develop` dalına açın
2. PR şablonunu eksiksiz doldurun
3. Branch isimlendirme kurallarına uyun
4. Tüm testlerin geçtiğinden emin olun
5. En az 1 kod inceleyiciden onay alın
6. Commit'lerinizin temiz olmasına dikkat edin

## Kod İnceleme (Code Review) Süreci

1. PR oluşturulduktan sonra inceleyici atanır
2. İnceleyici kodu gözden geçirir
3. Gerekli değişiklikler istenir
4. Değişiklikler yapılır ve tekrar gönderilir
5. İnceleyici onay verir
6. TL onayı ile `develop` dalına merge edilir

## Sorun Yaşarsanız

- [Genel Chat](#iletişim) üzerinden iletişime geçin
- Issue oluşturun
- Dökümanları kontrol edin

---

**Not**: Bu katkı rehberi [Contributor Covenant](https://www.contributor-covenant.org/)'a dayanmaktadır.
