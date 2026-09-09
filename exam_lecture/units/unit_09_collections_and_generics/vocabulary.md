# Unit 09 · Collections and Generics — Vocabulary

Bu ünite sözlüğü, [ana çift dilli notta](bilingual_notes.md) geçen Java ve YDS
açısından değerli kelime/kalıpları bağlam içinde toplar. Maddeler alfabetiktir.

## A–C

### absent · adjective

- **Türkçe:** mevcut olmayan, bulunmayan
- **Bağlam:** Map’te key’in bulunmaması. Bazı API işlemleri null ile eşlenmiş key’i de ayrı kural gereği absent gibi ele alır.
- **Example (özgün çalışma cümlesi):** The key is absent from the map.
- **Çeviri:** Anahtar map’te bulunmuyor.
- **Related:** Antonym: present; word family: absence.
- **Kaynak bağlam:** [absent](bilingual_notes.md#putting-if-absent).

### arbitrary · adjective

- **Türkçe:** keyfî, belirli bir kurala bağlı olmayan
- **Java bağlamı:** Bir collection'ın iteration order'ının garanti edilmediğini
  anlatabilir.
- **Example:** “A `HashSet` may display its elements in an arbitrary order.”
- **Çeviri:** “Bir `HashSet`, element'larını keyfî bir sırada gösterebilir.”
- **Related:** arbitrarily (adverb); synonym: unspecified

### backed by · phrasal adjective

- **Türkçe:** tarafından desteklenen, altında onu kullanan
- **Java bağlamı:** `Arrays.asList()` sonucunun özgün array ile aynı storage'ı
  paylaşmasını anlatır.
- **Example:** “The fixed-size list is backed by the original array.”
- **Çeviri:** “Fixed-size list, özgün array tarafından desteklenir.”
- **Related:** backing (noun/adjective); synonym: supported by

### bound · noun

- **Türkçe:** sınır, type kısıtı
- **Java bağlamı:** Generic type parameter'ın kabul edebileceği type'ları
  sınırlar.
- **Example:** “The bound restricts `T` to `Number` and its subclasses.”
- **Çeviri:** “Bound, `T`yi `Number` ve onun subclass'larıyla sınırlar.”
- **Related:** bound (adjective); bounded, unbounded

### bounded wildcard · noun phrase

- **Türkçe:** sınırlandırılmış wildcard
- **Java bağlamı:** `? extends T` veya `? super T` biçimindeki unknown type.
- **Example:** “A bounded wildcard makes the method more flexible without
  discarding type safety.”
- **Çeviri:** “Bounded wildcard, type safety'yi kaybetmeden method'u daha
  esnek yapar.”
- **Related:** upper-bounded wildcard, lower-bounded wildcard

### collection · noun

- **Türkçe:** koleksiyon, object grubu
- **Java bağlamı:** Küçük harfle genel object grubunu; `Collection` biçiminde
  ise `java.util.Collection` interface'ini anlatabilir.
- **Example:** “A collection stores a group of objects in one object.”
- **Çeviri:** “Collection, bir object grubunu tek object içinde saklar.”
- **Related:** collect (verb), collective (adjective)

### collision · noun

- **Türkçe:** çakışma
- **Java bağlamı:** Farklı object'lerin aynı hash bucket/value ile
  karşılaşması.
- **Example:** “A good hash distribution reduces collisions.”
- **Çeviri:** “İyi bir hash dağılımı collision'ları azaltır.”
- **Related:** collide (verb); synonym: clash

### comparable · adjective / interface name

- **Türkçe:** karşılaştırılabilir
- **Java bağlamı:** `Comparable<T>`, object'in natural order'ını
  `compareTo()` ile tanımlar.
- **Example:** “The elements must be comparable before natural-order sorting.”
- **Çeviri:** “Natural-order sorting öncesinde element'lar karşılaştırılabilir
  olmalıdır.”
- **Related:** compare (verb), comparison (noun)

### comparator · noun / interface name

- **Türkçe:** karşılaştırıcı
- **Java bağlamı:** `Comparator<T>`, iki object için alternative order
  tanımlar.
- **Example:** “Pass a comparator when the class has no natural order.”
- **Çeviri:** “Class'ın natural order'ı yoksa bir comparator geçirin.”
- **Related:** compare, comparative; contrast: `Comparable`

### consistent · adjective

- **Türkçe:** tutarlı, birbiriyle uyumlu
- **Bağlam:** `compareTo()` sonucu 0 olması ile `equals()` sonucunun true olması arasındaki uyum.
- **Example (özgün çalışma cümlesi):** Keep the ordering consistent with equals.
- **Çeviri:** Sıralama ilişkisini equals ile tutarlı tutun.
- **Related:** Antonym: inconsistent; word family: consistency, consistently.
- **Kaynak bağlam:** [consistent](bilingual_notes.md#keeping-compareto-and-equals-consistent).

### constant time · noun phrase

- **Türkçe:** sabit zaman
- **Java bağlamı:** Input büyüklüğünden bağımsız ortalama işlem süresi;
  çoğunlukla `O(1)` ile gösterilir.
- **Example:** “Hash lookup is expected to take constant time.”
- **Çeviri:** “Hash lookup'ın sabit zaman alması beklenir.”
- **Related:** linear time, logarithmic time

### convenience method · noun phrase

- **Türkçe:** kullanım kolaylığı sağlayan yardımcı method
- **Java bağlamı:** Başka method'larla da yapılabilecek bir işlemi daha açık ve
  kısa sunar.
- **Example:** “`removeIf()` is a convenient way to remove matching elements.”
- **Çeviri:** “`removeIf()`, eşleşen element'ları kaldırmanın kullanışlı bir
  yoludur.”
- **Related:** convenient (adjective), conveniently (adverb)

### covariant · adjective

- **Türkçe:** kovaryant, daha dar subtype'a izin veren
- **Java bağlamı:** Override edilen method'un return type'ı özgün return
  type'ın subtype'ı olabilir.
- **Example:** “Java permits a covariant return type in an override.”
- **Çeviri:** “Java, override'da covariant return type'a izin verir.”
- **Related:** covariance (noun); contrast: invariant

## D–I

### deduce · verb

- **Türkçe:** çıkarsamak, sonuç çıkarmak
- **Java bağlamı:** Compiler'ın context'ten generic veya `var` type'ını
  belirlemesi.
- **Example:** “The compiler deduces `String` from the assignment context.”
- **Çeviri:** “Compiler, assignment context'inden `String` type'ını çıkarır.”
- **Related:** deduction (noun); synonym: infer

### descending order · noun phrase

- **Türkçe:** azalan/ters sıra
- **Java bağlamı:** Büyükten küçüğe veya natural order'ın tersine sorting.
- **Example:** “The reversed comparator sorts the IDs in descending order.”
- **Çeviri:** “Ters comparator, ID'leri descending order'da sıralar.”
- **Related:** descend (verb); antonym: ascending order

### duplicate · noun / adjective

- **Türkçe:** yinelenen, kopya
- **Java bağlamı:** `List` duplicate kabul eder; `Set` etmez.
- **Example:** “`Set.of()` rejects duplicate elements.”
- **Çeviri:** “`Set.of()`, duplicate element'ları reddeder.”
- **Related:** duplicate (verb), duplication (noun)

### element · noun

- **Türkçe:** öğe, element
- **Java bağlamı:** Collection içinde saklanan tek object.
- **Example:** “The first element is removed from the deque.”
- **Çeviri:** “İlk element deque'dan kaldırılır.”
- **Related:** elemental (adjective); near-synonym: item

### entry · noun

- **Türkçe:** kayıt, girdi
- **Java bağlamı:** `Map.Entry<K,V>`, tek bir key/value pair'ini temsil eder.
- **Example:** “`entrySet()` returns a set of map entries.”
- **Çeviri:** “`entrySet()`, map entry'lerinden oluşan bir set döndürür.”
- **Related:** enter (verb); phrase: entry set

### equivalent · adjective

- **Türkçe:** eşdeğer
- **Java bağlamı:** Farklı syntax veya method dizilerinin aynı sonucu vermesi.
- **Example:** “The explicit generic type and the diamond form are
  equivalent.”
- **Çeviri:** “Açık generic type ile diamond biçimi eşdeğerdir.”
- **Related:** equivalence (noun); synonym: equal in effect

### erasure · noun

- **Türkçe:** silme, type bilgisinin silinmesi
- **Java bağlamı:** Generic bilgisinin compile sonrasında büyük ölçüde
  kaldırılması.
- **Example:** “After erasure, both overloads have the same signature.”
- **Çeviri:** “Erasure sonrasında iki overload aynı signature'a sahip olur.”
- **Related:** erase (verb); phrase: type erasure

### factory method · noun phrase

- **Türkçe:** object üreten factory method
- **Java bağlamı:** `List.of()`, `Set.of()` ve `Map.of()` gibi constructor
  yerine object döndüren static method.
- **Example:** “The factory method returns an immutable list.”
- **Çeviri:** “Factory method immutable bir list döndürür.”
- **Related:** factory (noun); creator method

### fixed-size · adjective

- **Türkçe:** sabit boyutlu
- **Java bağlamı:** Element'ları replace edilebilen fakat size'ı değiştirilemeyen
  `Arrays.asList()` view'su.
- **Example:** “Adding to a fixed-size list throws an exception.”
- **Çeviri:** “Fixed-size list'e ekleme yapmak exception fırlatır.”
- **Related:** fixed (adjective); contrast: resizable

### generic · adjective / noun

- **Türkçe:** genel tür parametreli, generic
- **Java bağlamı:** Class, interface veya method'u farklı type'larla type-safe
  biçimde yeniden kullanmayı sağlar.
- **Example:** “A generic class declares its type parameter in angle brackets.”
- **Çeviri:** “Generic class, type parameter'ını angle bracket'lar içinde
  bildirir.”
- **Related:** generalize (verb), generalization (noun)

### hash table · noun phrase

- **Türkçe:** hash tablosu
- **Java bağlamı:** `HashMap` ve `HashSet`in hızlı lookup için kullandığı yapı.
- **Example:** “A `HashSet` stores its elements in a hash table.”
- **Çeviri:** “`HashSet`, element'larını hash table içinde saklar.”
- **Related:** hash code, bucket, collision

### immutable · adjective

- **Türkçe:** değiştirilemez
- **Java bağlamı:** Oluşturulduktan sonra state'i değiştirilemeyen object.
- **Example:** “`List.of()` creates an immutable list.”
- **Çeviri:** “`List.of()`, immutable bir list oluşturur.”
- **Related:** immutability (noun); antonym: mutable

### infer · verb

- **Türkçe:** çıkarmak, dolaylı olarak belirlemek
- **Java bağlamı:** Compiler'ın diamond operator veya `var` için type
  belirlemesi.
- **Example:** “Java can infer the generic type from the left side.”
- **Çeviri:** “Java generic type'ı sol taraftan çıkarabilir.”
- **Related:** inference (noun); synonym: deduce

### insertion point · noun phrase

- **Türkçe:** ekleme noktası
- **Java bağlamı:** `binarySearch()` hedefi bulamazsa, sorted order'ı koruyarak
  ekleneceği index.
- **Example:** “Decode the negative result to find the insertion point.”
- **Çeviri:** “Insertion point'i bulmak için negative sonucu çözümleyin.”
- **Related:** insert (verb), position (noun)

### invariant · adjective

- **Türkçe:** değişmez varyanslı
- **Java bağlamı:** `Integer` subtype olsa da `List<Integer>`ın
  `List<Number>` subtype'ı olmaması.
- **Example:** “Java generic classes are invariant by default.”
- **Çeviri:** “Java generic class'ları varsayılan olarak invariant'tır.”
- **Related:** invariance (noun); contrast: covariant

### iterate · verb

- **Türkçe:** sırayla dolaşmak
- **Java bağlamı:** Collection element'larını loop, iterator veya `forEach()`
  ile ziyaret etmek.
- **Example:** “Use `entrySet()` to iterate over keys and values together.”
- **Çeviri:** “Key ve value'ları birlikte dolaşmak için `entrySet()` kullanın.”
- **Related:** iteration, iterator, iterable

## K–P

### key/value pair · noun phrase

- **Türkçe:** anahtar/değer çifti
- **Java bağlamı:** Map'teki her entry'nin iki parçası.
- **Example:** “A map stores each value as part of a key/value pair.”
- **Çeviri:** “Map her value'yu bir key/value pair'in parçası olarak saklar.”
- **Related:** mapping, entry

### legacy · adjective

- **Türkçe:** eski sistemden kalma
- **Java bağlamı:** `Vector`, `Hashtable` ve `Stack` gibi modern code'da
  genellikle tercih edilmeyen eski API'ler.
- **Example:** “The legacy class remains for backward compatibility.”
- **Çeviri:** “Eski sınıf, geriye dönük uyumluluğu korumak için varlığını sürdürür.”
- **Related:** heritage (noun); phrase: legacy code

### lower bound · noun phrase

- **Türkçe:** alt sınır
- **Java bağlamı:** `? super T`, `T` veya onun supertype'ını kabul eder.
- **Example:** “A lower bound lets the method add a `String` safely.”
- **Çeviri:** “Lower bound, method'un güvenle `String` eklemesini sağlar.”
- **Related:** lower-bounded wildcard; contrast: upper bound

### mapping function · noun phrase

- **Türkçe:** eşleme fonksiyonu
- **Java bağlamı:** `Map.merge()` içinde eski ve yeni value'dan sonuç üreten
  `BiFunction`.
- **Example:** “The mapping function is skipped when the old value is null.”
- **Çeviri:** “Eski value null olduğunda mapping function çağrılmaz.”
- **Related:** map (verb), remapping function

### natural order · noun phrase

- **Türkçe:** doğal sıralama
- **Java bağlamı:** Class'ın `Comparable.compareTo()` ile tanımladığı default
  order.
- **Example:** “Strings use lexicographic natural order.”
- **Çeviri:** “String değerlerinin doğal sıralaması sözlükbilimseldir (lexicographic).”
- **Related:** natural ordering; contrast: custom order

### parameterized type · noun phrase

- **Türkçe:** type argument verilmiş tür
- **Java bağlamı:** `List<String>` gibi generic declaration'ın belirli type ile
  kullanımı.
- **Example:** “`Map<String,Integer>` is a parameterized type.”
- **Çeviri:** “`Map<String,Integer>` parameterized type'tır.”
- **Related:** type parameter, type argument

### precondition · noun

- **Türkçe:** ön koşul
- **Java bağlamı:** `binarySearch()` öncesinde list'in aynı order ile sorted
  olması gibi çağrı şartı.
- **Example:** “Sorting the list satisfies the search precondition.”
- **Çeviri:** “Listeyi sıralamak, aramanın ön koşulunu karşılar.”
- **Related:** prerequisite; antonym: postcondition

<!-- page-break -->

## R–Z

### raw type · noun phrase

- **Türkçe:** type argument'ı yazılmamış ham generic type
- **Java bağlamı:** `List` yazıp `List<String>` yazmamak; warning ve type
  safety kaybı doğurur.
- **Example:** “Using a raw type may postpone an error until runtime.”
- **Çeviri:** “Ham tür kullanmak, bir hatanın ancak çalışma zamanında ortaya çıkmasına yol açabilir.”
- **Related:** unchecked warning, parameterized type

### retrieve · verb

- **Türkçe:** getirmek, erişip almak
- **Java bağlamı:** Collection veya map'ten value okumak.
- **Example:** “Use the key to retrieve the mapped value.”
- **Çeviri:** “Eşlenen value'yu getirmek için key'i kullanın.”
- **Related:** retrieval (noun); synonym: fetch

### reverse order · noun phrase

- **Türkçe:** ters sıra
- **Java bağlamı:** Natural order'ın `Comparator.reverseOrder()` veya
  `reversed()` ile çevrilmiş hâli.
- **Example:** “The comparator arranges the values in reverse order.”
- **Çeviri:** “Comparator değerleri ters sıraya koyar.”
- **Related:** reverse (verb/adjective); antonym: natural order

### shorthand notation · noun phrase

- **Türkçe:** kısa gösterim
- **Java bağlamı:** Diamond operator'ın sağ taraftaki tekrar eden generic type'ı
  gizlemesi.
- **Example:** “The diamond operator is shorthand notation for the inferred
  type.”
- **Çeviri:** “Diamond operator, inferred type için shorthand notation'dır.”
- **Related:** abbreviation; antonym: explicit notation

### sorted · adjective

- **Türkçe:** sıralanmış
- **Java bağlamı:** Belirli comparator veya natural order'a göre düzenlenmiş
  collection.
- **Example:** “Binary search requires a sorted list.”
- **Çeviri:** “İkili arama, aynı karşılaştırma düzenine göre sıralanmış bir liste gerektirir.”
- **Related:** sort (verb), sorting (noun); antonym: unsorted

### subtype · noun

- **Türkçe:** alt tür
- **Java bağlamı:** Başka bir type'ın üyelerini inherit eden ve onun yerine
  kullanılabilen type.
- **Example:** “`Integer` is a subtype of `Number`.”
- **Çeviri:** “`Integer`, `Number`ın subtype'ıdır.”
- **Related:** supertype, subclass

### trade-off · noun

- **Türkçe:** ödünleşim, bir kazanç karşılığındaki bedel
- **Java bağlamı:** `TreeSet`in sorted olması karşılığında hash lookup'tan daha
  yavaş olabilmesi.
- **Example:** “The trade-off for ordering is additional processing cost.”
- **Çeviri:** “Sıralı tutmanın karşılığında ek işlem maliyeti ödenir.”
- **Related:** compromise; phrase: cost-benefit trade-off

### type erasure · noun phrase

- **Türkçe:** tür silme
- **Java bağlamı:** Generic type bilgisinin compilation sırasında büyük ölçüde
  kaldırılması.
- **Example:** “Type erasure prevents overloading solely by generic argument.”
- **Çeviri:** “Type erasure yalnız generic argument'a göre overload yapılmasını
  engeller.”
- **Related:** erasure, erased type

### unbounded wildcard · noun phrase

- **Türkçe:** sınır belirtilmemiş wildcard
- **Java bağlamı:** `?`, herhangi bir generic type'ı temsil eder; read type'ı
  güvenli olarak `Object`tir.
- **Example:** “`List<?>` accepts a list of any element type.”
- **Çeviri:** “`List<?>`, herhangi bir element type'ındaki list'i kabul eder.”
- **Related:** wildcard; contrast: bounded wildcard

### underlying · adjective

- **Türkçe:** altta yatan, temel oluşturan
- **Java bağlamı:** Bir view'nun bağlı olduğu özgün array veya data structure.
- **Example:** “Changing the list also changes the underlying array.”
- **Çeviri:** “Listeyi değiştirmek, listenin dayandığı diziyi de değiştirir.”
- **Related:** underlie (verb); synonym: foundational

### upper bound · noun phrase

- **Türkçe:** üst sınır
- **Java bağlamı:** `? extends T`, unknown type'ın `T` veya subtype'ı olmasını
  ister.
- **Example:** “The upper bound allows values to be read as `Number`.”
- **Çeviri:** “Upper bound, value'ların `Number` olarak okunmasına izin verir.”
- **Related:** upper-bounded wildcard; contrast: lower bound

### wildcard · noun

- **Türkçe:** joker/bilinmeyen type göstergesi
- **Java bağlamı:** Generic declaration'da `?` ile gösterilir.
- **Example:** “Use a wildcard when the exact generic type is not important.”
- **Çeviri:** “Exact generic type önemli olmadığında wildcard kullanın.”
- **Related:** unbounded wildcard, bounded wildcard

## Karıştırılan anlamlar ve kapalı kitap hatırlama

| Karşılaştırma | Karar verirken kullan |
|---|---|
| `absent` / null-mapped | Key yok / key var ama değeri null. `containsKey()` bunları ayırabilir. |
| `fixed-size` / unmodifiable | Boyut sabit ama set mümkün / değişiklik işlemleri desteklenmez. |
| `sorted` / arbitrary order | Belirli karşılaştırma düzeni / sırası garanti edilmeyen dolaşım. |

Aşağıdaki özgün cümleyi Türkçeye çevir; ardından vurgulanan anlam farkını kendi Java örneğine aktar. Cevabı açmadan önce bir tahmin yaz.

> The collection is backed by an array.

**Kendini kontrol et:** Collection, depolama için bir diziye dayanır; kopya oluşturulduğu sonucu çıkarılamaz.

Dört işaretli terim için 1/3/7/14. günlerde iki yönlü hatırlama yap: English → Türkçe anlam, sonra Türkçe teknik durum → English terim. Anlamını hatırlayıp örnek kuramadığın terimi “öğrendim” diye işaretleme.

## Mini vocabulary quiz

1. “The list shares storage with the array” anlamına en yakın phrase hangisi?
2. `binarySearch()` sonucundan hedefin ekleneceği index'i anlatan terim nedir?
3. Bir kazanç karşılığında başka bir özellikten vazgeçmeyi anlatan kelime
   hangisidir?
4. `List` yazıp type argument'ı atlamanın adı nedir?
5. `? super String` hangi bound türüdür?

## Cevap anahtarı

1. **backed by**
2. **insertion point**
3. **trade-off**
4. **raw type**
5. **lower bound**
