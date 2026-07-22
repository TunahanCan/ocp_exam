# Unit 04 Vocabulary · Core APIs

Bu ünite sözlüğü Chapter 4'teki `String`, `StringBuilder`, array, `Math` ve
Date-Time API bağlamından seçilmiştir. Maddeler alfabetik sıralıdır.

## A–F

### account for · phrasal verb
- **Türkçe:** hesaba katmak
- **Bağlam:** DST gibi saat değişikliklerini hesaba dahil etmek.
- **Example:** `ZonedDateTime` accounts for daylight saving time.
- **Çeviri:** `ZonedDateTime` yaz saati uygulamasını hesaba katar.
- **Synonym:** consider, allow for

### apart · adjective / adverb
- **Türkçe:** aralıklı; aralarında
- **Bağlam:** İki instant arasındaki elapsed time.
- **Example:** The instants are six hours apart.
- **Çeviri:** Instant'lar arasında altı saat vardır.
- **Related:** difference, interval

### arbitrary · adjective
- **Türkçe:** keyfî, önceden sınırlandırılmamış
- **Bağlam:** Bir method'a farklı uzunluklarda `Period` verilebilmesi.
- **Example:** The method can add an arbitrary period of time.
- **Çeviri:** Method keyfî bir zaman aralığı ekleyebilir.
- **Word family:** arbitrarily (adv.)

### as opposed to · phrase
- **Türkçe:** aksine, ... yerine
- **Bağlam:** `String` ile `StringBuilder` davranışlarını karşılaştırmak.
- **Example:** The builder mutates, as opposed to creating a new object.
- **Çeviri:** Builder, yeni nesne oluşturmanın aksine mevcut nesneyi değiştirir.
- **Synonym:** rather than, in contrast to

### be able to · modal phrase
- **Türkçe:** yapabilmek
- **Bağlam:** Exam Essentials bölümündeki öğrenme hedefleri.
- **Example:** Be able to determine whether the code compiles.
- **Çeviri:** Kodun derlenip derlenmediğini belirleyebilmelisiniz.
- **Related:** capability, ability

### by contrast · discourse marker
- **Türkçe:** buna karşılık
- **Bağlam:** Immutable ve mutable API'ler arasındaki karşıtlık.
- **Example:** A `String` is immutable. By contrast, a `StringBuilder` is mutable.
- **Çeviri:** `String` immutable'dır. Buna karşılık `StringBuilder` mutable'dır.
- **Synonym:** conversely, on the other hand

### concatenation · noun
- **Türkçe:** birleştirme
- **Bağlam:** `+` ile String değerlerini art arda eklemek.
- **Example:** Concatenation is used if either operand is a `String`.
- **Çeviri:** Operand'lardan biri `String` ise birleştirme kullanılır.
- **Word family:** concatenate (v.)

### convenience method · noun phrase
- **Türkçe:** kullanımı kolaylaştıran yardımcı method
- **Bağlam:** `contains()` gibi daha uzun bir işlemi kısa yazan API.
- **Example:** `contains()` is a convenience method for an index check.
- **Çeviri:** `contains()`, indeks kontrolünü kısaltan yardımcı bir method'dur.
- **Related:** utility method

### daylight saving time · noun phrase
- **Türkçe:** yaz saati uygulaması
- **Bağlam:** Zone offset'in mevsimsel değişimi.
- **Example:** The clock jumps ahead for daylight saving time.
- **Çeviri:** Saat yaz saati uygulaması nedeniyle ileri alınır.
- **Abbreviation:** DST

### equivalent · adjective
- **Türkçe:** eşdeğer
- **Bağlam:** Aynı sonucu üreten expression veya aynı içeriğe sahip array.
- **Example:** These two expressions are equivalent.
- **Çeviri:** Bu iki ifade eşdeğerdir.
- **Word family:** equivalence (n.); **antonym:** different

### explicitly · adverb
- **Türkçe:** açıkça
- **Bağlam:** Constructor veya type bilgisini kaynak kodda doğrudan yazmak.
- **Example:** Calling the `String` constructor explicitly is optional.
- **Çeviri:** `String` constructor'ını açıkça çağırmak isteğe bağlıdır.
- **Word family:** explicit (adj.); **antonym:** implicitly

### fall back · phrasal verb
- **Türkçe:** saati geri almak
- **Bağlam:** DST sona ererken local hour'ın tekrarlanması.
- **Example:** Clocks fall back in November.
- **Çeviri:** Saatler kasım ayında geri alınır.
- **Antonym:** spring ahead

### fixed-size · adjective
- **Türkçe:** sabit boyutlu
- **Bağlam:** Array uzunluğunun oluşturulduktan sonra değişmemesi.
- **Example:** An array is a fixed-size area of memory.
- **Çeviri:** Array sabit boyutlu bir bellek alanıdır.
- **Related:** capacity, length

### fractional · adjective
- **Türkçe:** kesirli
- **Bağlam:** Floating-point değerler ve saniyenin kesirli bölümü.
- **Example:** The time contains fractional seconds.
- **Çeviri:** Saat, saniyenin kesirli bölümünü içerir.
- **Word family:** fraction (n.)

## G–M

### hard-code · verb
- **Türkçe:** değeri doğrudan koda sabitlemek
- **Bağlam:** Bir indeksi hesaplamak yerine literal olarak yazmak.
- **Example:** Avoid hard-coding the index when it can change.
- **Çeviri:** Değişebilecek indeksi doğrudan koda sabitlemekten kaçının.
- **Related:** literal, constant

### immutable · adjective
- **Türkçe:** değiştirilemez
- **Bağlam:** Method çağrısından sonra mevcut object state'inin değişmemesi.
- **Example:** `LocalDate` is immutable, so `plusDays()` returns a new value.
- **Çeviri:** `LocalDate` immutable olduğundan `plusDays()` yeni değer döndürür.
- **Antonym:** mutable

### incidental whitespace · noun phrase
- **Türkçe:** kod biçiminden kaynaklanan istenmeyen boşluk
- **Bağlam:** Text block içindeki ortak indentation.
- **Example:** `stripIndent()` removes incidental whitespace.
- **Çeviri:** `stripIndent()` istenmeyen ortak girintiyi kaldırır.
- **Related:** indentation, leading whitespace

### independently · adverb
- **Türkçe:** birbirinden bağımsız olarak
- **Bağlam:** Her API expression'ını temiz başlangıç değeriyle ayrı denemek.
- **Example:** Run each expression independently.
- **Çeviri:** Her expression'ı birbirinden bağımsız çalıştırın.
- **Word family:** independent (adj.)

### insertion point · noun phrase
- **Türkçe:** ekleme konumu
- **Bağlam:** Bulunamayan değerin sorted array'e gireceği indeks.
- **Example:** Binary search encodes the insertion point as a negative result.
- **Çeviri:** Binary search ekleme konumunu negatif sonuçla kodlar.
- **Related:** binary search, index

### instantiate · verb
- **Türkçe:** nesne örneği oluşturmak
- **Bağlam:** Constructor veya factory method ile nesne oluşturmak.
- **Example:** The array is declared but not instantiated.
- **Çeviri:** Array bildirilmiş, ancak oluşturulmamıştır.
- **Word family:** instance (n.), instantiation (n.)

### literal · noun / adjective
- **Türkçe:** kaynak kodda doğrudan yazılan sabit değer
- **Bağlam:** String pool'a yerleştirilen `"Hello"` gibi değerler.
- **Example:** String literals are stored in the string pool.
- **Çeviri:** String literal'ları string pool'da saklanır.
- **Related:** constant, compile-time

### method chaining · noun phrase
- **Türkçe:** method zincirleme
- **Bağlam:** Bir method'un sonucunda doğrudan başka method çağırmak.
- **Example:** Method chaining keeps related operations together.
- **Çeviri:** Method zincirleme ilişkili işlemleri bir arada tutar.
- **Related:** fluent API

### mismatch · noun / verb
- **Türkçe:** uyuşmazlık; ilk farklı konumu bulmak
- **Bağlam:** `Arrays.mismatch()` ile ilk differing index'i belirlemek.
- **Example:** The mismatch occurs at index one.
- **Çeviri:** İlk uyuşmazlık indeks birde oluşur.
- **Antonym:** match

### mutable · adjective
- **Türkçe:** değiştirilebilir
- **Bağlam:** Aynı `StringBuilder` nesnesinin state'inin değişmesi.
- **Example:** `StringBuilder` is mutable.
- **Çeviri:** `StringBuilder` değiştirilebilirdir.
- **Antonym:** immutable; **word family:** mutate (v.)

## N–S

### normalize · verb
- **Türkçe:** standartlaştırmak
- **Bağlam:** `indent()` method'unun line terminator düzenini `\n` yapması.
- **Example:** The method normalizes existing line breaks.
- **Çeviri:** Method mevcut satır sonlarını standartlaştırır.
- **Word family:** normalization (n.)

### operand · noun
- **Türkçe:** işlenen
- **Bağlam:** `+` operatörünün sağındaki veya solundaki değer.
- **Example:** If either operand is a `String`, Java concatenates.
- **Çeviri:** Operand'lardan biri `String` ise Java birleştirme yapar.
- **Related:** operator, expression

### out of bounds · adjective phrase
- **Türkçe:** sınırların dışında
- **Bağlam:** Geçerli array veya String indeks aralığını aşmak.
- **Example:** Index 7 is out of bounds for a seven-character String.
- **Çeviri:** Yedi karakterli bir String için indeks 7 sınır dışıdır.
- **Related:** `IndexOutOfBoundsException`

### prefix · noun
- **Türkçe:** ön ek, başlangıç bölümü
- **Bağlam:** String ordering sırasında kısa değerin diğerinin başı olması.
- **Example:** `"a"` is a prefix of `"aa"`.
- **Çeviri:** `"a"`, `"aa"` değerinin prefix'idir.
- **Antonym:** suffix

### redundant · adjective
- **Türkçe:** gereksiz, yinelenen
- **Bağlam:** `substring(3, length)` çağrısında ikinci parametrenin gereksizliği.
- **Example:** The second argument is legal but redundant.
- **Çeviri:** İkinci argüman geçerlidir, ancak gereksizdir.
- **Word family:** redundancy (n.)

### reference equality · noun phrase
- **Türkçe:** referans eşitliği
- **Bağlam:** İki değişkenin aynı nesneyi gösterip göstermediğini denetlemek.
- **Example:** The `==` operator checks reference equality for objects.
- **Çeviri:** `==`, nesnelerde referans eşitliğini denetler.
- **Contrast:** content equality

### resulting · adjective
- **Türkçe:** ortaya çıkan
- **Bağlam:** API çağrısından sonra oluşan String, tarih veya sayısal değer.
- **Example:** The resulting local hour is three.
- **Çeviri:** Ortaya çıkan local hour üçtür.
- **Word family:** result (n./v.)

### spring ahead · phrasal verb
- **Türkçe:** saati ileri almak
- **Bağlam:** DST başlangıcında local clock'un bir saati atlaması.
- **Example:** Clocks spring ahead in March.
- **Çeviri:** Saatler mart ayında ileri alınır.
- **Antonym:** fall back

### straightforward · adjective
- **Türkçe:** açık, kolay anlaşılır
- **Bağlam:** Davranışı adına uygun olan basit API method'ları.
- **Example:** The `length()` method is straightforward.
- **Çeviri:** `length()` method'unun davranışı kolay anlaşılırdır.
- **Synonym:** clear, uncomplicated

### supplied · adjective
- **Türkçe:** sağlanan, verilen
- **Bağlam:** Soruda önceden verilen array veya date-time object'i.
- **Example:** Compare the supplied arrays.
- **Çeviri:** Verilen array'leri karşılaştırın.
- **Word family:** supply (v./n.)

## T–Z

### temporal · adjective / noun
- **Türkçe:** zamansal; zaman nesnesi
- **Bağlam:** Date-Time API içinde tarih veya saat taşıyan tür.
- **Example:** A temporal type supports only compatible units.
- **Çeviri:** Temporal type yalnızca uyumlu birimleri destekler.
- **Related:** time, chronology

### trailing · adjective
- **Türkçe:** sonda bulunan
- **Bağlam:** String sonundaki whitespace veya line break.
- **Example:** `stripTrailing()` removes trailing whitespace.
- **Çeviri:** `stripTrailing()` sondaki whitespace'i kaldırır.
- **Antonym:** leading

### transform · verb
- **Türkçe:** dönüştürmek
- **Bağlam:** `StringBuilder` içeriğini mutation chain ile değiştirmek.
- **Example:** `reverse()` transforms `Java` into `avaJ`.
- **Çeviri:** `reverse()`, `Java` değerini `avaJ` değerine dönüştürür.
- **Word family:** transformation (n.)

### truncate · verb
- **Türkçe:** kesmek, alt birimleri veya kesirli kısmı atmak
- **Bağlam:** `between()` ve `truncatedTo()` işlemlerinde yuvarlamadan kesmek.
- **Example:** The calculation truncates rather than rounds.
- **Çeviri:** Hesaplama yuvarlamak yerine keser.
- **Word family:** truncation (n.)

### undefined · adjective
- **Türkçe:** tanımsız
- **Bağlam:** API contract'ın belirli input için sonuç garantisi vermemesi.
- **Example:** Binary search results are undefined for an unsorted array.
- **Çeviri:** Unsorted array'de binary search sonuçları tanımsızdır.
- **Antonym:** defined

### whitespace · noun
- **Türkçe:** boşluk karakterleri
- **Bağlam:** Space, tab ve line break gibi görünmeyen karakterler.
- **Example:** `strip()` removes leading and trailing whitespace.
- **Çeviri:** `strip()` baştaki ve sondaki whitespace'i kaldırır.
- **Related:** blank, indentation

### wrap around · phrasal verb
- **Türkçe:** sona gelince başa dönmek
- **Bağlam:** `LocalTime` değerinin gece yarısını geçince ertesi gün bilgisini tutmaması.
- **Example:** The time wraps around after midnight.
- **Çeviri:** Saat gece yarısından sonra başa döner.
- **Related:** cycle, rollover

## Mini quiz

1. `insertion point` binary search sonucunda nasıl kodlanır?
2. `spring ahead` ile `fall back` arasındaki fark nedir?
3. `reference equality` ile content equality arasındaki fark nedir?
4. `incidental whitespace` hangi method ile kaldırılır?
5. `truncate` ve `round` aynı işlem midir?

## Cevaplar

1. `-(insertion point) - 1` formülüyle.
2. İlki saati ileri, ikincisi geri alır.
3. İlki aynı nesneyi, ikincisi nesne içeriğini karşılaştırır.
4. `stripIndent()` ile.
5. Hayır. `truncate` alt kısmı atar; `round` en yakın değere yuvarlar.

## 5 dakikalık active recall

1. `immutable`, `mutable`, `resulting` ve `method chaining` terimleriyle
   `String`/`StringBuilder` farkını anlat.
2. `insertion point`, `mismatch`, `undefined` ve `out of bounds` terimlerini
   array bağlamında tanımla.
3. `temporal`, `daylight saving time`, `spring ahead` ve `fall back` ile bir
   zaman çizgisi kur.
4. `literal`, `reference equality` ve `instantiate` terimleriyle string pool'u
   açıkla.
