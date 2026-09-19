# Ünite 07 · Implementing queries in a microservice architecture

**Microservice mimarisinde sorguları uygulama** — *Microservices Patterns*, bölüm 7; kaynak PDF sayfaları **220–252**.

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

- API composition ve CQRS arasında sorgu ihtiyaçlarına göre seçim yapmak.
- Görünüm güncelleme gecikmesi ve veri tutarlılığı ilişkisini açıklamak.
- DynamoDB görünümündeki yinelenen olay denetimini ve pagination mantığını izlemek.

## Okuma rotası

1. **7.1 Querying using the API composition pattern — API composition örüntüsüyle sorgulama**
2. **7.2 Using the CQRS pattern — CQRS örüntüsünü kullanmak**
3. **7.3 Designing CQRS views — CQRS görünümlerini tasarlamak**
4. **7.4 Implementing a CQRS view with AWS DynamoDB — AWS DynamoDB ile CQRS görünümü gerçekleştirmek**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. API composition ve CQRS arasında sorgu ihtiyaçlarına göre seçim yapabilir misiniz?
2. Görünüm güncelleme gecikmesi ve veri tutarlılığı ilişkisini açıklayabilir misiniz?
3. DynamoDB görünümündeki yinelenen olay denetimini ve pagination mantığını takip edebilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
