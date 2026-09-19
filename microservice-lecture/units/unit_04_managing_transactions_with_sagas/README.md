# Ünite 04 · Managing transactions with sagas

**Transaction işlemlerini saga ile yönetme** — *Microservices Patterns*, bölüm 4; kaynak PDF sayfaları **110–145**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 15 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |



- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Bütün üniteler](../../README.md)
- [Teslim ve doğrulama raporu](../../review_report.md)

## Öğrenme hedefleri

- Yerel transaction ile servisler arası saga sınırını ayırmak.
- Koreografi ve orkestrasyonun koordinasyon maliyetlerini karşılaştırmak.
- Compensation işlemlerini ve isolation eksikliğine karşı önlemleri açıklamak.

## Okuma rotası

1. **4.1 Transaction management in a microservice architecture — Mikroservis mimarisinde transaction (işlem) yönetimi**
2. **4.2 Coordinating sagas — Saga'ları koordine etmek**
3. **4.3 Handling the lack of isolation — Isolation (yalıtım) eksikliğini ele almak**
4. **4.4 The design of the Order Service and the Create Order Saga — Order Service ve Create Order Saga'nın tasarımı**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. Yerel transaction ile servisler arası saga sınırını ayırt edebilir misiniz?
2. Koreografi ve orkestrasyonun koordinasyon maliyetlerini karşılaştırabilir misiniz?
3. Compensation işlemlerini ve isolation eksikliğine karşı önlemleri açıklayabilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
