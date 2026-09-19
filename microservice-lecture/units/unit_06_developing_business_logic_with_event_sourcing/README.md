# Ünite 06 · Developing business logic with event sourcing

**Event sourcing ile iş mantığı geliştirme** — *Microservices Patterns*, bölüm 6; kaynak PDF sayfaları **183–219**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 13 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |



- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Bütün üniteler](../../README.md)
- [Teslim ve doğrulama raporu](../../review_report.md)

## Öğrenme hedefleri

- Event sourcing ile güncel durum saklama arasındaki farkı açıklamak.
- Event store, replay ve snapshot rollerini ayırmak.
- Saga ile event sourcing birlikte kullanıldığında idempotency gereksinimini değerlendirmek.

## Okuma rotası

1. **6.1 Developing business logic using event sourcing — Event sourcing kullanarak iş mantığı geliştirmek**
2. **6.2 Implementing an event store — Event store gerçekleştirmek**
3. **6.3 Using sagas and event sourcing together — Saga'ları ve event sourcing'i birlikte kullanmak**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. Event sourcing ile güncel durum saklama arasındaki farkı açıklayabilir misiniz?
2. Event store, replay ve snapshot rollerini ayırt edebilir misiniz?
3. Saga ile event sourcing birlikte kullanıldığında idempotency gereksinimini değerlendirebilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
