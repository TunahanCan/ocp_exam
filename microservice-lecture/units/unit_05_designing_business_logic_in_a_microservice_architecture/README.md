# Ünite 05 · Designing business logic in a microservice architecture

**Microservice mimarisinde iş mantığını tasarlama** — *Microservices Patterns*, bölüm 5; kaynak PDF sayfaları **146–182**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 14 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |



- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Bütün üniteler](../../README.md)
- [Teslim ve doğrulama raporu](../../review_report.md)

## Öğrenme hedefleri

- Transaction Script ve Domain Model yaklaşımlarını karşılaştırmak.
- Aggregate sınırını ve invariant kavramını örnekle açıklamak.
- Domain event yayımlamanın transaction ile ilişkisini izlemek.

## Okuma rotası

1. **5.1 Business logic organization patterns — İş mantığını düzenleme örüntüleri**
2. **5.2 Designing a domain model using the DDD aggregate pattern — DDD aggregate örüntüsüyle bir alan modeli tasarlamak**
3. **5.3 Publishing domain events — Domain event (alan olayı) yayımlamak**
4. **5.4 Kitchen Service business logic — Kitchen Service iş mantığı**
5. **5.5 Order Service business logic — Order Service iş mantığı**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. Transaction Script ve Domain Model yaklaşımlarını karşılaştırabilir misiniz?
2. Aggregate sınırını ve invariant kavramını örnekle açıklayabilir misiniz?
3. Domain event yayımlamanın transaction ile ilişkisini takip edebilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
