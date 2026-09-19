# Ünite 08 · External API patterns

**Dış API örüntüleri** — *Microservices Patterns*, bölüm 8; kaynak PDF sayfaları **253–291**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 11 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |



- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Bütün üniteler](../../README.md)
- [Teslim ve doğrulama raporu](../../review_report.md)

## Öğrenme hedefleri

- İstemci türlerinin dış API tasarımını nasıl etkilediğini açıklamak.
- API gateway ve Backend for Frontend sorumluluklarını ayırmak.
- API composition sırasında hata ve performans sınırlarını değerlendirmek.

## Okuma rotası

1. **8.1 External API design issues — Dış API tasarımında ele alınacak konular**
2. **8.2 The API gateway pattern — API gateway örüntüsü**
3. **8.3 Implementing an API gateway — API gateway gerçekleştirmek**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. İstemci türlerinin dış API tasarımını nasıl etkilediğini açıklayabilir misiniz?
2. API gateway ve Backend for Frontend sorumluluklarını ayırt edebilir misiniz?
3. API composition sırasında hata ve performans sınırlarını değerlendirebilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
