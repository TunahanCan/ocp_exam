# Unit 10 · Streams — Vocabulary

Bu ünite sözlüğü, [ana çift dilli notta](bilingual_notes.md) geçen Java ve YDS
açısından değerli kelime/kalıpları gerçek stream bağlamında toplar. Maddeler
alfabetiktir.

## A–C

### aggregate · verb / noun

- **Türkçe:** bir araya getirmek; toplu sonuç
- **Java bağlamı:** Stream element'larından tek bir sonuç veya collection
  üretmek.
- **Example:** “A terminal operation may aggregate all elements.”
- **Çeviri:** “Bir terminal operation bütün element'ları bir araya getirebilir.”
- **Related:** aggregation (noun); synonym: combine

### average · noun / verb

- **Türkçe:** ortalama; ortalamasını almak
- **Java bağlamı:** Primitive stream'lerde `average()` empty olasılığı nedeniyle
  `OptionalDouble` döndürür.
- **Example:** “The average is absent when the stream is empty.”
- **Çeviri:** “Stream boş olduğunda ortalama değeri bulunmaz.”
- **Related:** mean (noun); word family: averaging

### chain · verb / noun

- **Türkçe:** zincirlemek; zincir
- **Java bağlamı:** Stream veya `Optional` operation'larını art arda bağlamak.
- **Example:** “Chain the mapping and filtering operations.”
- **Çeviri:** “Mapping ve filtering operation'larını zincirleyin.”
- **Related:** chaining (noun); synonym: link

### collect · verb

- **Türkçe:** toplamak, bir sonuç container'ında biriktirmek
- **Java bağlamı:** `collect()` mutable reduction veya `Collector` çalıştırır.
- **Example:** “Collect the names into a sorted set.”
- **Çeviri:** “Adları sorted set içinde toplayın.”
- **Related:** collection, collector, collective

### concatenate · verb

- **Türkçe:** uç uca eklemek, birleştirmek
- **Java bağlamı:** String'leri veya iki stream'i sırayla birleştirmek.
- **Example:** “The reduction concatenates four letters.”
- **Çeviri:** “Reduction dört harfi uç uca ekler.”
- **Related:** concatenation (noun); synonym: join

### consume · verb

- **Türkçe:** tüketmek
- **Java bağlamı:** Terminal operation stream'i kullanır; aynı stream tekrar
  kullanılamaz.
- **Example:** “A terminal operation consumes the stream.”
- **Çeviri:** “Terminal operation stream'i tüketir.”
- **Related:** consumer, consumption; synonym: use up

## D–I

### decomposition · noun

- **Türkçe:** parçalara ayırma
- **Java bağlamı:** `Spliterator.trySplit()` source'u parallel işleme uygun
  parçalara bölebilir.
- **Example:** “A spliterator supports traversal and decomposition.”
- **Çeviri:** “Spliterator, öğeleri dolaşmayı ve kaynağı parçalara ayırmayı destekler.”
- **Related:** decompose (verb); antonym: composition

### downstream collector · noun phrase

- **Türkçe:** alt aşamada çalışan collector
- **Java bağlamı:** `groupingBy()` veya `partitioningBy()` sonrasında group
  value'larının nasıl toplanacağını belirler.
- **Example:** “Use a downstream collector to produce sets.”
- **Çeviri:** “Set üretmek için downstream collector kullanın.”
- **Related:** upstream; collector

### eager · adjective

- **Türkçe:** istekli; programlama bağlamında hemen değerlendirilen
- **Java bağlamı:** `orElse()` argument'ı value gerekmeden de çalışır.
- **Example:** “The fallback passed to `orElse()` is evaluated eagerly.”
- **Çeviri:** “`orElse()`e verilen yedek değeri hesaplayan ifade, o değere ihtiyaç olup olmadığına bakılmadan değerlendirilir.”
- **Related:** eagerly (adverb); antonym: lazy

### empty · adjective

- **Türkçe:** boş
- **Java bağlamı:** Value içermeyen `Optional` veya element içermeyen stream.
- **Example:** “An empty stream has a count of zero.”
- **Çeviri:** “Empty stream'in count değeri sıfırdır.”
- **Related:** emptiness; antonym: populated

### finite · adjective

- **Türkçe:** sonlu
- **Java bağlamı:** Terminal operation'ın bütün element'ları tüketerek sona
  erebileceği sınırlı stream.
- **Example:** “Applying `limit()` can make the result finite.”
- **Çeviri:** “`limit()` uygulamak sonucu finite hale getirebilir.”
- **Related:** finiteness; antonym: infinite

### flatten · verb

- **Türkçe:** düzleştirmek, iç içe yapıyı tek katmana indirmek
- **Java bağlamı:** `flatMap()` nested stream veya `Optional` katmanını kaldırır.
- **Example:** “Flatten the nested streams before collecting.”
- **Çeviri:** “Sonucu toplamadan önce iç içe stream’leri tek katmana indirin.”
- **Related:** flat, flat mapping

### generate · verb

- **Türkçe:** üretmek
- **Java bağlamı:** `Stream.generate(Supplier)` varsayılan olarak infinite
  source oluşturur.
- **Example:** “Generate values only when the pipeline requests them.”
- **Çeviri:** “Value'ları yalnız pipeline istediğinde üretin.”
- **Related:** generator, generation

### get the hang of · idiom

- **Türkçe:** mantığını kavramak; nasıl yapıldığını öğrenmek
- **Bağlam:** Stream pipeline’ını adım adım takip edebilir hâle gelmek.
- **Example (özgün çalışma cümlesi):** You will get the hang of streams with practice.
- **Çeviri:** Alıştırma yaptıkça stream’lerin mantığını kavrayacaksınız.
- **Related:** Near synonym: learn how to use; hang burada asmak anlamında çevrilmez.
- **Kaynak bağlam:** [get the hang of](bilingual_notes.md#chapter-10--streams).

### identity · noun

- **Türkçe:** özdeş eleman, başlangıç değeri
- **Java bağlamı:** Reduction operation'ında sonucu değiştirmeyen başlangıç
  value'su.
- **Example:** “Zero is the identity for addition.”
- **Çeviri:** “Sıfır, toplama işleminin sonucunu değiştirmeyen özdeş elemandır.”
- **Related:** identical; phrase: identity value

### infinite · adjective

- **Türkçe:** sonsuz
- **Java bağlamı:** `generate()` ve iki-argument `iterate()` gibi bitişi olmayan
  stream source'ları.
- **Example:** “Counting an infinite stream does not terminate.”
- **Çeviri:** “Infinite stream'i saymak sona ermez.”
- **Related:** infinity; antonym: finite

## L–P

### lazy evaluation · noun phrase

- **Türkçe:** tembel/gecikmeli değerlendirme
- **Java bağlamı:** Intermediate operation'ın terminal operation gelene kadar
  çalışmaması.
- **Example:** “Lazy evaluation avoids processing unused elements.”
- **Çeviri:** “Lazy evaluation kullanılmayan element'ların işlenmesini önler.”
- **Related:** deferred execution; antonym: eager evaluation

### link · verb

- **Türkçe:** bağlamak
- **Java bağlamı:** Stream'in terminal operation başlayana kadar underlying
  data source ile ilişkili kalması.
- **Example:** “The stream remains linked to its source.”
- **Çeviri:** “Stream source'una bağlı kalır.”
- **Related:** linkage, underlying data

### map · verb

- **Türkçe:** dönüştürmek, eşlemek
- **Java bağlamı:** Her input element'ını bir output element'ına dönüştürmek.
- **Example:** “Map each name to its length.”
- **Çeviri:** “Her adı length değerine dönüştürün.”
- **Related:** mapping; contrast: flat map

### partition · verb / noun

- **Türkçe:** iki bölüme ayırmak; bölüm
- **Java bağlamı:** `partitioningBy()` element'ları predicate'e göre `true` ve
  `false` group'larına ayırır.
- **Example:** “Partition the values by whether they are even.”
- **Çeviri:** “Değerleri çift olup olmamalarına göre iki gruba ayırın.”
- **Related:** partitioning, division

### pipeline · noun

- **Türkçe:** işlem hattı
- **Java bağlamı:** Source, intermediate operation'lar ve terminal
  operation'dan oluşan stream akışı.
- **Example:** “The terminal operation triggers the pipeline.”
- **Çeviri:** “Terminal operation pipeline'ı tetikler.”
- **Related:** flow, stage

## R–S

### reduction · noun

- **Türkçe:** indirgeme
- **Java bağlamı:** Birçok element'tan tek bir value veya sonuç container'ı
  üretme işlemi.
- **Example:** “Summing the values is a reduction.”
- **Çeviri:** “Value'ları toplamak bir reduction'dır.”
- **Related:** reduce, accumulator

### short-circuit · verb / adjective

- **Türkçe:** sonucu erken belirleyip işlemi sonlandırmak
- **Java bağlamı:** `findFirst()` veya `anyMatch()` bütün source'u tüketmeden
  bitebilir.
- **Example:** “The match operation short-circuits after the first success.”
- **Çeviri:** “Match operation ilk başarıdan sonra erken sona erer.”
- **Related:** early termination

### source · noun

- **Türkçe:** kaynak
- **Java bağlamı:** Pipeline'a element sağlayan collection, array, generator
  veya başka stream source'u.
- **Example:** “A collection can serve as the stream source.”
- **Çeviri:** “Bir collection stream source'u olarak kullanılabilir.”
- **Related:** originate, origin

### stateful · adjective

- **Türkçe:** durum tutan
- **Java bağlamı:** `sorted()` veya `distinct()` önceki element'lara ilişkin
  bilgi tutar.
- **Example:** “Sorting is a stateful intermediate operation.”
- **Çeviri:** “Sorting, stateful intermediate operation'dır.”
- **Related:** state; antonym: stateless

### steep learning curve · noun phrase

- **Türkçe:** başlangıçta öğrenmesi zor süreç
- **Bağlam:** Kaynakta fonksiyonel programlamaya alışmanın başlangıçta zor gelebilmesi.
- **Example (özgün çalışma cümlesi):** Streams can have a steep learning curve.
- **Çeviri:** Stream’leri öğrenmek başlangıçta zor gelebilir.
- **Related:** Contrast: easy to learn; steep bu bağlamda dik diye çevrilmek zorunda değildir.
- **Kaynak bağlam:** [steep learning curve](bilingual_notes.md#chapter-10--streams).

### stream · noun

- **Türkçe:** akış; Java'da stream
- **Java bağlamı:** Element sequence'i üzerinde declarative operation'lar
  tanımlayan, data saklamayan API abstraction'ı.
- **Example:** “A stream is not a reusable collection.”
- **Çeviri:** “Stream yeniden kullanılabilen bir collection değildir.”
- **Related:** streaming, pipeline

### summarize · verb

- **Türkçe:** özetlemek
- **Java bağlamı:** Count, min, max, sum ve average değerlerini statistics
  object'inde toplamak.
- **Example:** “The statistics object summarizes the numeric stream.”
- **Çeviri:** “Statistics object numeric stream'i özetler.”
- **Related:** summary, summarizing

## T–Z

### terminal · adjective

- **Türkçe:** son, sonlandırıcı
- **Java bağlamı:** Pipeline execution'ını başlatan ve stream dışı sonuç üreten
  operation.
- **Example:** “Exactly one terminal operation completes a pipeline.”
- **Çeviri:** “İşlem hattını tamamlayan tam olarak bir terminal operation vardır.”
- **Related:** terminate, termination; antonym: intermediate

### traversal · noun

- **Türkçe:** sırayla dolaşma
- **Java bağlamı:** `Spliterator`ın source element'larını ziyaret etmesi.
- **Example:** “`tryAdvance()` performs one step of traversal.”
- **Çeviri:** “`tryAdvance()` traversal'ın bir adımını gerçekleştirir.”
- **Related:** traverse (verb)

### underlying · adjective

- **Türkçe:** altta yatan, temel oluşturan
- **Java bağlamı:** Stream'in element aldığı gerçek collection veya data
  source'u.
- **Example:** “Do not modify the underlying source during traversal.”
- **Çeviri:** “Öğeleri dolaşırken stream’in dayandığı veri kaynağını değiştirmeyin.”
- **Related:** basis, backing

### vacuous truth · noun phrase

- **Türkçe:** boş kümede doğruluk
- **Java bağlamı:** Empty stream'de `allMatch()` ve `noneMatch()` sonucunun
  `true` olmasını açıklar.
- **Example:** “The empty result follows the rule of vacuous truth.”
- **Çeviri:** “Empty sonuç vacuous truth kuralını izler.”
- **Related:** logic, universal condition

## Karıştırılan anlamlar ve kapalı kitap hatırlama

| Karşılaştırma | Karar verirken kullan |
|---|---|
| `eager` / `lazy` | Hemen değerlendirme / gerektiğinde değerlendirme; kişilik özelliği anlamı kullanılmaz. |
| `finite` / terminating | Sonlu sayıda öğe / gerçekten sona eren hesaplama; lazy pipeline’ın konumu da önemlidir. |
| `map` / `flatten` | Öğeyi dönüştürmek / iç içe katmanı kaldırmak; map burada harita değildir. |

Aşağıdaki özgün cümleyi Türkçeye çevir; ardından vurgulanan anlam farkını kendi Java örneğine aktar. Cevabı açmadan önce bir tahmin yaz.

> A short-circuiting operation may terminate the pipeline.

**Kendini kontrol et:** Erken sonlandırabilen bir işlem, işlem hattını sona erdirebilir. “may”, her zaman sona erer garantisi değildir.

Dört işaretli terim için 1/3/7/14. günlerde iki yönlü hatırlama yap: English → Türkçe anlam, sonra Türkçe teknik durum → English terim. Anlamını hatırlayıp örnek kuramadığın terimi “öğrendim” diye işaretleme.

## Mini quiz · Vocabulary recall

Bu bölüm özgün çalışma alıştırmasıdır.

1. Terminal operation gelene kadar çalışmama özelliği hangi phrase'dir?
2. Nested stream'leri tek katmana indiren fiil hangisidir?
3. Sonucu değiştirmeyen reduction başlangıç value'suna ne denir?
4. Bütün element'ları tüketmeden sonuç veren operation özelliği nedir?
5. Stream'in üzerinde çalıştığı gerçek collection için hangi adjective
   kullanılır?
6. `allMatch()`in empty stream'de `true` olmasını açıklayan mantık terimi nedir?

## Cevaplar

1. lazy evaluation
2. flatten
3. identity
4. short-circuit
5. underlying
6. vacuous truth
