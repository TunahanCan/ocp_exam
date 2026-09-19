# Ünite 03 · Interprocess communication in a microservice architecture

**Microservice mimarisinde süreçler arası iletişim** — *Microservices Patterns*, bölüm 3; kaynak PDF sayfaları **65–109**.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders ve 18 özgün şekil | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Ünite sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |



- [Şekillerin kaynak bilgileri](assets/manifest.json)
- [Bütün üniteler](../../README.md)
- [Teslim ve doğrulama raporu](../../review_report.md)

- [Ünite kalite kontrolü](review_report.md)

## Öğrenme hedefleri

- Senkron çağrı ile asenkron mesajlaşmanın gecikme ve arıza davranışlarını karşılaştırmak.
- Service discovery, timeout ve circuit breaker rollerini ayırmak.
- Yinelenen mesaj, sıra ve transactional messaging sorunlarını açıklamak.

## Okuma rotası

1. **3.1 Overview of interprocess communication in a microservice architecture — Mikroservis mimarisinde süreçler arası iletişime genel bakış**
2. **3.2 Communicating using the synchronous Remote procedure invocation pattern — Senkron Remote procedure invocation örüntüsüyle iletişim**
3. **3.3 Communicating using the Asynchronous messaging pattern — Asynchronous messaging örüntüsüyle iletişim**
4. **3.4 Using asynchronous messaging to improve availability — Asenkron mesajlaşmayla kullanılabilirliği artırmak**

Her oturumda bir alt başlık okuyun. Önce İngilizce paragrafın öznesini ve ana fiilini bulun; hemen altındaki Türkçe çeviriyle karşılaştırın. İlgili şekli açıklamasıyla birlikte inceleyin. Sözlükten 3–5 terim, grammar notlarından bir yapı seçin; mini quiz cevaplarını önce kendiniz üretin.

## Kısa kontrol

1. Senkron çağrı ile asenkron mesajlaşmanın gecikme ve arıza davranışlarını karşılaştırabilir misiniz?
2. Service discovery, timeout ve circuit breaker rollerini ayırt edebilir misiniz?
3. Yinelenen mesaj, sıra ve transactional messaging sorunlarını açıklayabilir misiniz?

**Kaynak bağlamı:** Teknoloji sürümleri ve ürün karşılaştırmaları kitabın dönemine aittir. Kodlar kaynak uygulamanın parçalarıdır; bağımsız Java 17 programları veya çalıştırılmış entegrasyon testleri olarak sunulmaz.
