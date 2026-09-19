# Ünite 09 · Testing microservices: Part 1

**Microservice testleri: Bölüm 1** — *Microservices Patterns*, bölüm 9; kaynak PDF sayfaları **292–317**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 11 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |

- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Ünite doğrulama raporu](review_report.md)
- [Bütün üniteler](../../README.md)

## Okuma rotası

1. 9.1 Test stratejileri, test piramidi, consumer-driven contract testing ve deployment pipeline
2. 9.2 Entity, value object, saga, domain service, controller ve message handler için unit testler

Her oturumda bir alt başlığı okuyun. İngilizce paragrafın öznesini ve ana fiilini bulup hemen altındaki Türkçe çeviriyle karşılaştırın. Şekilleri açıklamalarıyla birlikte inceleyin. [Sözlükten](vocabulary.md) 3–5 terim ve [grammar notlarından](grammar_notes.md) bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. Unit, integration, component ve end-to-end testlerin kapsamını ayırt edebilir misiniz?
2. Stub ile mock arasındaki farkı ve solitary/sociable unit test seçimini açıklayabilir misiniz?
3. Tüketici ve sağlayıcı sözleşme testlerinin neden aynı sözleşmeleri kullandığını anlatabilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış integration testler olarak sunulmaz. Kaynakta görülen somut kod/adlandırma sorunları ilgili listelerin yanında işaretlenmiştir.
