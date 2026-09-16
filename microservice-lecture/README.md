# Microservices Patterns · Çift dilli çalışma

Kaynak PDF, ünite ünite İngilizce–Türkçe karşılaştırmalı ders materyaline dönüştürülür. Her ünite için tek `bilingual_notes.md` ana kaynak ve ondan üretilen tek `bilingual_notes.pdf` tutulur. Vocabulary ve grammar kaynakları/PDF’leri üniteye özeldir.

## Hazır materyaller

- [Ünite 01 — Monolitik çıkmazdan kurtulmak](units/unit_01_escaping_monolithic_hell/README.md)
- [Ünite 01 ana PDF](units/unit_01_escaping_monolithic_hell/bilingual_notes.pdf)
- [Kaynak PDF](Microservices_Patterns_1_Bolumden_Itibaren.pdf)

## Ünite haritası

Kaynak PDF 492 sayfadır. Numaralı 13 bölüm PDF 1–471 arasındadır; sonraki sayfalar boş sayfa, dizin ve tanıtım materyalidir. Sayfa aralıkları dosyada 1’den başlayan PDF sayfa numaralarıdır.

| Ünite | Kaynak başlık | PDF sayfaları | Durum |
|---|---|---|---|
| 01 | Escaping monolithic hell | 1–32 | [Tamamlandı](units/unit_01_escaping_monolithic_hell/README.md) |
| 02 | Decomposition strategies | 33–64 | Sırada |
| 03 | Interprocess communication in a microservice architecture | 65–109 | Sırada |
| 04 | Managing transactions with sagas | 110–145 | Sırada |
| 05 | Designing business logic in a microservice architecture | 146–182 | Sırada |
| 06 | Developing business logic with event sourcing | 183–219 | Sırada |
| 07 | Implementing queries in a microservice architecture | 220–252 | Sırada |
| 08 | External API patterns | 253–291 | Sırada |
| 09 | Testing microservices: Part 1 | 292–317 | Sırada |
| 10 | Testing microservices: Part 2 | 318–347 | Sırada |
| 11 | Developing production-ready services | 348–382 | Sırada |
| 12 | Deploying microservices | 383–427 | Sırada |
| 13 | Refactoring to microservices | 428–471 | Sırada |

## Çalışma düzeni

1. Bir alt başlıkta İngilizce paragrafı oku; hemen altındaki Türkçe çeviriyle karşılaştır.
2. Şemayı incele; özgün etiketleri çift dilli şekil açıklamasıyla ilişkilendir.
3. Ünite sözlüğünden birkaç yeni kelime ve grammar notlarından bir yapı çalış.
4. Ünite sonundaki özgün tekrar sorularını notlara bakmadan yanıtla.

Görseller kaynak PDF’nin vektör çizimleri ve yazıları birlikte render edilerek çıkarılır; şema içeriği yeniden çizilmez. Ünite `assets/manifest.json` dosyası her şeklin kaynak sayfasını, kırpım sınırlarını ve çözünürlüğünü kaydeder.

## Üretim ve doğrulama

- [PDF üretim aracı ve kullanım](tools/README.md)
- [Kaynak bölüm/şekil haritası](source_map.json)
- [Ünite 01 kalite kontrolü](units/unit_01_escaping_monolithic_hell/review_report.md)

Diğer üniteler bu teslimde çevrilmemiştir; sıra ve kaynak aralıkları sonraki çalışmalar için kaydedilmiştir.
