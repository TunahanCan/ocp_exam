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

## İşten sonra çalışma rotası

Bu rota bütün üniteyi tek akşamda bitirme hedefi değildir. Her satır **25–30 dakikalık bir oturumun odağıdır**; okuma veya soru grubu bitmezse aynı satırı sonraki güne taşı. Bir oturumda 2–4 kaynak soruyu gerekçesiyle çözmek yeterlidir. Aşağıdaki soru numaraları kitabın **Review Questions** bölümüne aittir; `practice_quiz` ayrı özgün sorulardır.

Her oturum: **3 dk** önceki bilgiyi kapalı kitap hatırla → **10 dk** English paragrafı çevirip Türkçeyle karşılaştır → **5 dk** en fazla dört yeni kelime ve bir grammar yapısı → **8 dk** soru çöz → **2 dk** yanlışının nedenini yaz. İlk turda bütün kelimeleri ezberlemeye çalışma; bilmediklerini işaretle.

| Oturum ve kaynak başlığı | Kaynak sorular | Kelime ve grammar odağı | Oturum sonunda üret |
|---|---|---|---|
| 1. [Optional ve yokluk](bilingual_notes.md#returning-an-optional) | 20 | empty, eager, get the hang of; `whether`, `either ... or ...` | Empty/value × get/orElse/orElseGet tablosunu kur; practice quiz 4 ile pekiştir. |
| 2. [Pipeline, lazy evaluation ve durma](bilingual_notes.md#using-streams) | 1, 2, 3, 4, 6, 10, 17 | lazy evaluation, finite, short-circuit; `unless`, `since` | Her elemanın geçebileceği adımları izle; terminal var mı, gerçekten durabilir mi? |
| 3. [Dönüşüm, sıralama ve reduction](bilingual_notes.md#using-common-intermediate-operations) | 7, 11, 12, 13 | flatten, identity, reduction; `rather than`, `by + V-ing` | Her adımdan sonra stream türünü yaz; map ve flatMap katmanlarını çiz. |
| 4. [Primitive stream’ler](bilingual_notes.md#working-with-primitive-streams) | 5, 8, 9, 14, 19 | average, summarize, terminal; `without + V-ing`, `that/which` | Stream<Integer>–IntStream ve Optional–OptionalInt ayrımını yap. |
| 5. [Collector, veri kaynağı ve Spliterator](bilingual_notes.md#collecting-results) | 15, 16, 18, 21 | downstream collector, partition, traversal; `so that`, `think of ... as ...` | Collector çıktı türünü hesapla; practice quiz 1–8 ile karma kontrol yap. |

Kelime anlamlarını [ünite sözlüğünden](vocabulary.md), yapıları [grammar notundan](grammar_notes.md) kontrol et. Kaynak sorularını çözerken önce isteneni (derleme / çıktı / exception / doğru seçenek sayısı), sonra kuralı yaz; cevap harfini en son seç.

## Aralıklı tekrar ve geçiş ölçütü

- **1. gün:** Türkçeyi kapatarak dün işaretlediğin dört kelimeyi ve bir cümleyi geri çağır; yanlış yaptığın bir soruyu çöz.
- **3. gün:** Aynı kuralı ölçen başka bir kaynak soruya geç; doğru seçeneğin yanında en güçlü yanlış seçeneğin neden elendiğini söyle.
- **7. gün:** Özgün practice quiz'i yeniden çöz; çözerken kuralın adını ve sonucunu ayrı yaz. Hedef **en az 7/8** ve bütün derleme/çalışma zamanı ayrımlarını doğru gerekçelendirmek.
- **14. gün:** Önceki yanlışlarından üç soruyu karışık sırada çöz; sekiz işaretli kelimenin en az altısını ve iki cümlenin özne/fiil/yan cümle yapısını notsuz çıkar.

Yanlış kayıt biçimi: `Soru → ilk kararım → kaçırdığım Java kuralı/İngilizce yapı → düzeltilmiş gerekçe → yeniden çözüm günü`. Yalnızca cevap harfini hatırlamak geçiş ölçütü değildir. Eksik kalan konu için ilgili oturumu tekrarla.

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
- [ ] Practice quiz'de en az **7/8** doğru yapabiliyorum.

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
