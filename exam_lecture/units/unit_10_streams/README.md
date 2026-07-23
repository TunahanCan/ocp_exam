# Unit 10 · Streams

Bu ünite Java 17 `Optional`, object/primitive stream ve advanced collector
konularını kaynak sırasını koruyan çift dilli ders akışıyla; ayrıca hızlı
tekrar, vocabulary ve grammar materyalleriyle birlikte ele alır.

## Çalışma kaynakları

1. **Ana çift dilli ders**
   - [Markdown kaynağı](bilingual_notes.md)
   - [PDF çalışma sürümü](bilingual_notes.pdf)
2. **Teknik hafıza ve karar notları**
   - [Technical memory notes](technical_memory_notes.md)
   - [PDF çalışma sürümü](technical_memory_notes.pdf)
3. **Ünite vocabulary çalışması**
   - [Markdown kaynağı](vocabulary.md)
   - [PDF çalışma sürümü](vocabulary.pdf)
4. **Ünite grammar çalışması**
   - [Markdown kaynağı](grammar_notes.md)
   - [PDF çalışma sürümü](grammar_notes.pdf)

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 10 physical PDF pages: **531–590**
- Chapter 10 Appendix official answers: **942–945**
- Chapter gövdesi: **60/60 source marker**
- Görsel kaynaklar: **Table 10.1–10.10** ve **Figure 10.1–10.5**
- Bölüm sonu: Summary, Exam Essentials ve Review Questions 1–21
- Appendix: Official Answers 1–21 ve bütün gerekçeleri

Physical page 590 chapter'ın son review question sayfasıdır; Chapter 11 physical
page 591'de başlar. Appendix page 945'in üst bölümü Chapter 10 Answers 19–21'i,
alt bölümü Chapter 11 cevaplarını içerir; yalnız ilgili bölüm alınmıştır.

## Konu haritası

- `Optional` factory'leri, empty/value state'i ve eager/lazy fallback
- Stream source'ları, finite/infinite stream ve lazy pipeline flow
- Common terminal operations, short-circuiting ve three `reduce()` overload'ı
- Common intermediate operations, stateful/stateless ayrımı
- `IntStream`, `LongStream`, `DoubleStream` ve primitive optional type'lar
- Mapping matrix, boxing ve summary statistics
- Mutable reduction ve `Collectors`
- `toMap()`, `groupingBy()`, `partitioningBy()` ve downstream collector
- Underlying data bağlantısı, single-use stream ve `Optional` chaining
- `Spliterator` traversal/decomposition method'ları

## Java 17 teknik doğruluk notları

- Intermediate operation'lar terminal operation çağrılana kadar lazy'dir.
- `orElse()` fallback'i eager, `orElseGet()` supplier'ı lazy değerlendirir.
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

## Önerilen çalışma sırası

1. `bilingual_notes.md` içindeki English → Türkçe paragraf çiftlerini oku.
2. Her pipeline için source, intermediate ve terminal operation'ı işaretle.
3. Sonucu **Does not compile**, runtime exception, output veya “sona ermez”
   olarak sınıflandır.
4. `technical_memory_notes.md` karar tabloları ve mapping matrix'iyle tekrar et.
5. Vocabulary/grammar mini quiz'lerini ve Review Questions 1–21'i çöz.
6. Son olarak Appendix gerekçeleriyle yanlış seçenekleri tek tek kontrol et.

Vocabulary ve grammar quiz'leri ile teknik hafıza soruları kitaptan alınmış
gerçek sınav soruları değil, açıkça belirtilmiş özgün çalışma sorularıdır.
