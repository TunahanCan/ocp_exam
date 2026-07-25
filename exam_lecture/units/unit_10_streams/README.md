# Unit 10 · Streams

Bu ünite Java 17 `Optional`, object/primitive stream ve advanced collector
konularını kaynak sırasını koruyan çift dilli ders akışıyla ele alır. Hedef,
pipeline'ı source → intermediate → terminal olarak okuyup sonucu **output**,
**Does not compile**, runtime exception veya “sona ermez” biçiminde
sınıflandırabilmektir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Konuyu kaynak sırasıyla, English → Türkçe eşleşmesiyle öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Pipeline, mapping ve collector tablolarını hızlı tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Stream/Optional terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Kaynaktaki İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi yeni compile/output ve kavram sorularında sınamak | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Vocabulary ve grammar quiz'leri, teknik hafıza soruları ve `practice_quiz`,
> OCP tarzı **özgün çalışma sorularıdır**; gerçek sınavdan alınmış sorular
> olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasını incele; bir pipeline'da source, intermediate ve
   terminal operation'ı nasıl bulacağını anlat.
2. **5–25 dk:** Ana çift dilli notta zayıf olduğun iki başlığı, kod sonucunu
   önceden tahmin ederek çalış.
3. **25–35 dk:** Teknik hafıza notundaki terminal operation, mapping ve
   collector tablolarını kapatıp yeniden kur.
4. **35–43 dk:** Vocabulary'den 6–8 terimi pipeline bağlamında tekrar et.
5. **43–50 dk:** Grammar notes içinden iki yapıyı doğal Türkçe karşılığıyla
   çözümle.
6. **50–60 dk:** Practice quiz'i kapalı kaynakla çöz; her cevabı compile-time,
   runtime, output veya termination açısından gerekçelendir.

## Önkoşullar ve konu haritası

**Önkoşul:** Lambda ve built-in functional interface'ler (Unit 08), collection
API'leri ve generics (Unit 09) bilinmelidir.

```text
Optional: value / empty + eager / lazy fallback
        ↓
stream source → intermediate operations → terminal operation
        ↓
object stream ↔ primitive stream + primitive Optional
        ↓
mutable reduction → Collectors → grouping/partitioning/teeing
        ↓
single use + underlying data + Spliterator
```

Ana konu başlıkları:

- `Optional` factory'leri, empty/value state'i ve eager/lazy fallback
- Finite/infinite stream, lazy pipeline ve short-circuiting
- Terminal operations ve three `reduce()` overload'ı
- Intermediate operations, stateful/stateless ayrımı
- Primitive streams, mapping matrix ve summary statistics
- `toMap()`, `groupingBy()`, `partitioningBy()` ve downstream collector
- Underlying data bağlantısı, single-use stream ve `Spliterator`

## Hazır mıyım?

- [ ] `orElse()` ile `orElseGet()` evaluation farkını açıklayabiliyorum.
- [ ] Bir pipeline'da operation sırasının output ve termination'ı nasıl
  değiştirdiğini görebiliyorum.
- [ ] Empty stream'de match ve reduction sonuçlarını belirleyebiliyorum.
- [ ] Object/primitive stream mapping method'larını doğru seçebiliyorum.
- [ ] Tüketilmiş stream'in yeniden kullanımının runtime sonucu olduğunu
  biliyorum.
- [ ] `toMap()`, `groupingBy()` ve `partitioningBy()` sonuçlarını
  karşılaştırabiliyorum.
- [ ] Infinite pipeline için terminal operation'ın gerçekten sona erip
  ermeyeceğini analiz edebiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapabiliyorum.

## Java 17 teknik doğruluk notları

- Intermediate operation'lar terminal operation çağrılana kadar lazy'dir.
- `orElse()` fallback'i eager, `orElseGet()` supplier'ı lazy değerlendirilir.
- Empty stream'de `allMatch()` ve `noneMatch()` `true`, `anyMatch()` `false`
  döndürür.
- Tüketilmiş stream'in tekrar kullanılması compile-time değil runtime
  `IllegalStateException` üretir.
- `Stream<Integer>` üzerinde `boxed()` yoktur; `boxed()` primitive stream
  method'udur.
- İki-argument `Collectors.toMap()` duplicate key'de runtime
  `IllegalStateException` üretir; merge function bu conflict'i çözer.
- `partitioningBy()` iki Boolean key'i de üretir; `groupingBy()` yalnız oluşan
  key'leri üretir.
- Kaynakta “`DoubleSummaryStream` / `IntSummaryStream` /
  `LongSummaryStream`” biçiminde görünen adların Java 17 API karşılıkları
  `DoubleSummaryStatistics`, `IntSummaryStatistics` ve
  `LongSummaryStatistics`tır.

## Kaynak ve kapsam

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 10 physical PDF pages: **531–590**
- Chapter 10 Appendix official answers: **942–945**
- Chapter gövdesi: **60/60 kaynak sayfa**
- Görsel kaynaklar: **Table 10.1–10.10** ve **Figure 10.1–10.5**
- Bölüm sonu: Summary, Exam Essentials ve Review Questions 1–21
- Appendix: Official Answers 1–21 ve bütün gerekçeleri

Physical page 590 chapter'ın son review question sayfasıdır; Chapter 11 physical
page 591'de başlar. Appendix page 945'in üst bölümü Chapter 10 Answers 19–21'i,
alt bölümü Chapter 11 cevaplarını içerir; yalnız ilgili bölüm alınmıştır.
