# Unit 09 · Collections and Generics — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) gerçek Java metni
bağlamından seçilen İngilizce yapıları açıklar. Amaç kelime kelime çeviri değil,
teknik anlamı hızlı çözebilmektir.

`English` etiketiyle alıntılanan bütün örnekler ana nottaki kaynak
paragraflardan aynen seçilmiştir. Formül, doğru/yanlış karşılaştırması ve mini
quiz satırları ise öğretim amacıyla hazırlanmış özgün çalışma örnekleridir.

## 1. `allow + object + to + verb`

### Yapı

```text
subject + allow(s) + object + to + base verb
```

Bir kişi veya şeyin başka bir eylemi yapmasına “izin vermek / olanak sağlamak”
anlamı verir.

> **English:** “This allows us to make the Assistant disappear.”
>
> **Türkçe:** “Böylece Assistant'ı ortadan kaldırabiliriz.”

`allow` sonrasında doğrudan infinitive kullanma:

```text
allows to access       [YANLIŞ]
allows users to access [DOĞRU]
allows access          [DOĞRU]
```

**YDS ipucu:** Passive biçim sık görülür:
`object + be allowed to + verb` → “object'in ... yapmasına izin verilir.”

## 2. `as + adjective/adverb + as`

### Yapı

```text
as + adjective/adverb + as + comparison target
not as/so + adjective/adverb + as
```

Eşitlik karşılaştırması yapar; negative biçim “... kadar değil” anlamındadır.

> **English:** “The trade-off is that it isn’t as efficient as a “pure”
> queue.”
>
> **Türkçe:** “Karşılığında ‘pure’ queue kadar efficient değildir.”

**Sık hata:** Adjective'i ilk `as`tan önce koyma:
`as efficient as` doğrudur; `efficient as` eksiktir.

## 3. `be said/considered/expected to`

### Yapı

```text
subject + be + past participle + to-infinitive
```

Reporting passive (aktarım edilgeni) ile “... olduğu söylenir/kabul
edilir/beklenir” anlamı verir.

> **English:** “It is considered part of the Java Collections Framework even
> though it isn’t technically a `Collection`.”
>
> **Türkçe:** “Teknik olarak bir `Collection` olmamasına rağmen Java
> Collections Framework'ün parçası kabul edilir.”

> **English:** “A natural ordering that uses `compareTo()` is said to be
> consistent with `equals` if, and only if, `x.equals(y)` is `true` whenever
> `x.compareTo(y)` equals 0.”
>
> **Türkçe:** “`compareTo()` kullanan natural ordering; yalnız ve ancak
> `x.compareTo(y)` 0 olduğunda `x.equals(y)` de `true` ise `equals` ile
> consistent kabul edilir.”

**YDS ipucu:** Active eşdeğeri çoğunlukla belirsiz bir özne içerir:
`People consider Map ...` → `Map is considered ...`.

## 4. `by + gerund`

### Yapı

```text
main clause + by + verb-ing
```

Ana eylemin **hangi yöntemle** yapıldığını gösterir; “... yaparak” diye
çevrilir.

> **English:** “You can fix this by passing a `Comparator` to `sort()`.”
>
> **Türkçe:** “`sort()`a bir `Comparator` geçirerek bunu düzeltebilirsiniz.”

**YDS ipucu:** `by` burada agent bildiren passive `by` değildir; yöntem
bildirir. Sonrasında base verb değil `-ing` gelir.

## 5. Causal `since` ile temporal `since`

### Yapı

```text
since + clause, result clause       (çünkü)
present perfect + since + past time (…den beri)
```

Bu ünitede çoğunlukla neden bildirir.

> **English:** “Since there isn’t a type specified for the generic, Java has
> to assume the ultimate superclass.”
>
> **Türkçe:** “Generic için bir type belirtilmediğinden Java ultimate
> superclass'ı varsaymak zorundadır.”

Zaman anlamındaki `since` ise bir başlangıç noktası verir ve çoğunlukla perfect
tense ile kullanılır. Bu ayrım kaynak örneğindeki açık neden-sonuç ilişkisinden
anlaşılır.

**YDS ipucu:** `since` clause'undan sonra neden-sonuç mantığı kuruluyorsa
“çünkü/…dığı için”; başlangıç zamanı varsa “...den beri” anlamını dene.

## 6. Concessive `even though`

### Yapı

```text
even though + full clause, contrasting clause
```

Beklenen sonucun tersine bir durum bildirir: “... olmasına rağmen”.

> **English:** “It is considered part of the Java Collections Framework even
> though it isn’t technically a `Collection`.”
>
> **Türkçe:** “Teknik olarak bir `Collection` olmamasına rağmen Java
> Collections Framework'ün parçası kabul edilir.”

**Sık hata:** `despite` ile aynı syntax'ı sanmak:

```text
even though + subject + verb [DOĞRU]
despite + noun / verb-ing    [DOĞRU]
despite + full clause        [YANLIŞ]
```

## 7. `given + noun` ve `given that + clause`

### Yapı

```text
given + noun phrase
given that + subject + verb
```

“... verildiğinde / ... göz önüne alındığında” anlamı taşır.

> **English:** “Finally, the exam expects you to be able to choose the right
> collection type given a description of a problem.”
>
> **Türkçe:** “Son olarak sınav, bir problem description'ı verildiğinde doğru
> collection type'ını seçebilmenizi bekler.”

> **English:** “Given that `Map` doesn’t extend `Collection`, more methods are
> specified on the `Map` interface.”
>
> **Türkçe:** “`Map`, `Collection`ı extend etmediği için `Map` interface'inde
> daha fazla method tanımlanmıştır.”

**YDS ipucu:** `given` burada “verilmiş” adjective'i değil, condition/assumption
bağlayıcısı gibi çalışabilir.

## 8. `if` clause ve gerçek koşul

### Yapı

```text
if + present simple, present simple / modal / imperative
```

Teknik dokümanda genel kural veya olası sonucu anlatır.

> **English:** “If the `List` fits in that array, it will be returned.”
>
> **Türkçe:** “`List` bu array'e sığarsa o array döndürülür.”

> **English:** “Please go back and review Table 8.4 if the functional
> interfaces are unfamiliar.”
>
> **Türkçe:** “Functional interface'ler size yabancı geliyorsa Table 8.4'ü
> yeniden inceleyin.”

**Sık hata:** Genel kuralda `if` clause'una gereksiz `will` koyma. Sonuç
clause'unda `will` olabilir; koşul clause'unda çoğunlukla simple present gelir.

## 9. `if it were ..., would ...` — unreal condition

### Yapı

```text
if + subject + past / were, subject + would + base verb
```

Gerçekte olmayan veya varsayımsal durumu anlatır.

> **English:** “If it were, we’d have a `NullPointerException`.”
>
> **Türkçe:** “Çağrılsaydı `NullPointerException` oluşurdu.”

**YDS ipucu:** Past biçim geçmiş zaman değil, gerçeğe uzaklık gösterebilir.
`were`, tekil subject ile de resmî ve yaygın biçimdir.

## 10. Indirect question: `what/whether/how + clause`

### Yapı

```text
main clause + question word + subject + verb
```

Indirect question'da normal statement order kullanılır; yardımcı fiil subject
önüne geçmez.

> **English:** “This time, the `boolean` return value tells us whether a match
> was removed.”
>
> **Türkçe:** “Bu kez `boolean` return value, bir eşleşmenin kaldırılıp
> kaldırılmadığını söyler.”

> **English:** “Figure 9.2 shows how you can envision a `List`.”
>
> **Türkçe:** “Figure 9.2, bir `List`i nasıl gözünüzde
> canlandırabileceğinizi gösterir.”

```text
We know how the method works. [DOĞRU]
We know how does the method work. [YANLIŞ]
```

**YDS ipucu:** `whether` iki olasılık arasındaki “olup olmadığı” anlamında,
özellikle `whether ... or not` kalıbında sık görülür.

## 11. `make sure (that) + clause`

### Yapı

```text
make sure (that) + subject + verb
```

“... olduğundan emin olmak / ... yapmayı garanti altına almak” anlamındadır.
`that` çoğunlukla atılabilir.

> **English:** “Make sure that you can fill in Table 9.8 to compare the four
> collection types from memory.”
>
> **Türkçe:** “Dört collection type'ını hafızadan karşılaştırmak için Table
> 9.8'i doldurabildiğinizden emin olun.”

**Sık hata:** `make sure to + verb` de mümkündür, fakat anlam odağı eylemi
unutmamak üzerindedir:
`Make sure to sort the list first.` → “List'i önce sıralamayı unutmayın.”

## 12. Modal necessity: `need to`, `have to`, `must`

### Yapı

```text
subject + need(s) to / have-has to / must + base verb
```

Teknik gereklilik bildirir. `must` daha doğrudan; `need to` ve `have to`
bağlamsal gereklilik için yaygındır.

> **English:** “You don’t need to know the names of the specific interfaces
> that the different maps implement, but you do need to know that `TreeMap` is
> sorted.”
>
> **Türkçe:** “Farklı map'lerin implement ettiği belirli interface'lerin
> adlarını bilmeniz gerekmez; ancak `TreeMap`in sorted olduğunu bilmeniz
> gerekir.”

> **English:** “When using `binarySearch()`, the `List` must be sorted in the
> same order that the `Comparator` uses.”
>
> **Türkçe:** “`binarySearch()` kullanılırken `List`, `Comparator`ın kullandığı
> order ile aynı biçimde sorted olmalıdır.”

**YDS ipucu:** Negative anlamlar farklı olabilir:

- `must not`: yasaktır.
- `do not have to` / `do not need to`: gerekmez.

## 13. `rather than`

### Yapı

```text
noun + rather than + noun
verb-ing + rather than + verb-ing
base verb + rather than + base verb
```

İki seçenek arasında tercih/karşıtlık kurar: “... yerine”.

> **English:** “For example, when you use the contact list in your phone, you
> look up “George” rather than looking through each phone number in turn.”
>
> **Türkçe:** “Örneğin telefonunuzdaki kişi listesini kullanırken her telefon
> numarasına sırayla bakmak yerine ‘George’ adını ararsınız.”

**Sık hata:** İki tarafın grammatical form'unu paralel tutmamak. YDS'de
parallelism (paralel yapı) kontrolü answer elemede kullanılır.

## 14. Reduced clause: `when/while + verb-ing`

### Yapı

```text
when/while + verb-ing, main clause
```

Yan clause ile main clause'un subject'i aynıysa
`when subject is/does ...` bölümü kısaltılabilir.

> **English:** “When writing your own compare methods, you should check the
> data before comparing it if it is not validated ahead of time.”
>
> **Türkçe:** “Kendi compare method'larınızı yazarken data önceden validate
> edilmediyse karşılaştırmadan önce kontrol etmelisiniz.”

Tam biçim:

```text
When you write your own compare methods, ...
```

**YDS ipucu:** Reduced clause'un gizli subject'i main clause subject'iyle
mantıksal olarak uyumlu olmalıdır. Aksi durumda dangling modifier oluşur.

## 15. Reduced relative clause

### Yapı

```text
noun + past participle ...  = noun + that/which is/was + past participle
noun + verb-ing ...         = noun + that/which + active verb
```

> **English:** “A collection is a group of objects contained in a single
> object.”
>
> **Türkçe:** “Collection, tek bir object içinde bulunan object grubudur.”

Tam biçim:

```text
A group of objects that is contained in a single object
```

> **English:** “The first says to create an empty `LinkedList` containing all
> the defaults.”
>
> **Türkçe:** “İlki bütün default'ları taşıyan boş bir `LinkedList` oluşturmayı
> söyler.”

**YDS ipucu:** Past participle çoğunlukla passive; `-ing` çoğunlukla active
anlam taşır.

## 16. `so that + clause`

### Yapı

```text
action + so that + subject + can/could/will/would + verb
```

Amaç veya hedeflenen sonucu bildirir: “...mesi için”.

> **English:** “Finally, we discuss how to create your own classes and methods
> that use generics so that the same class can be used with many types.”
>
> **Türkçe:** “Son olarak aynı class'ın birçok type ile kullanılabilmesi için
> generics kullanan kendi class ve method'larınızı nasıl oluşturacağınızı
> tartışıyoruz.”

**Sık hata:** `so that` ile sonuç bildiren `so + adjective + that` yapısını
karıştırma:

- `so that we can reuse it` → amaç
- `so flexible that we can reuse it` → derece-sonuç

## 17. `suppose/supposing (that)`

### Yapı

```text
suppose/supposing (that) + clause
```

Örnek scenario kurar: “... olduğunu varsayalım”.

> **English:** “Supposing we are using this as a FIFO queue.”
>
> **Türkçe:** “Bunu FIFO queue olarak kullandığımızı varsayalım.”

> **English:** “Suppose you want to sort the rabbits in descending order.”
>
> **Türkçe:** “Tavşanları descending order'da sıralamak istediğinizi
> varsayalım.”

**YDS ipucu:** Buradaki `supposing`, continuous tense değildir; condition
bağlayıcısı gibi çalışır ve `if`e yakın anlam taşır.

## 18. `the same ... as`

### Yapı

```text
the same + noun + as + noun/clause
```

“... ile aynı ...” anlamındadır.

> **English:** “This works the same way as classes.”
>
> **Türkçe:** “Bu, class'larla aynı şekilde çalışır.”

**Sık hata:** Standart kullanımda `the same ... than` değil, `the same ... as`
gelir.

## 19. `unless`

### Yapı

```text
unless + affirmative clause
= if + negative clause
```

“...medikçe / ... olmadığı sürece” anlamındadır.

> **English:** “Unless you are writing a library for others to reuse, generics
> hardly show up in the class definitions you write.”
>
> **Türkçe:** “Başkalarının reuse edeceği library yazmıyorsanız generics,
> yazdığınız class definition'larında neredeyse hiç görünmez.”

**Sık hata:** `unless` zaten negative anlam taşıdığı için standart kullanımda
yanına bir de `not` ekleme:
`unless it compiles` → “derlenmedikçe”.

## 20. `unlike + noun`

### Yapı

```text
unlike + noun phrase, clause
```

İki varlık arasındaki farkı vurgular: “...den farklı olarak”.

> **English:** “Unlike an array, though, many `List` implementations can
> change in size after they are declared.”
>
> **Türkçe:** “Ancak array'den farklı olarak birçok `List` implementation'ı
> bildirildikten sonra size değiştirebilir.”

`unlike` burada preposition'dır; ardından tam clause değil noun phrase gelir.

```text
Unlike a List, a Set ... [DOĞRU]
Unlike a List allows duplicates ... [YANLIŞ]
```

## 21. Contrast veya time bildiren `while`

### Yapı

```text
while + clause, contrasting clause  (oysa/iken)
while + clause, simultaneous event  (... sırasında)
while + verb-ing                    (... yaparken; reduced clause)
```

> **English:** “The `compareTo()` method returns 0 if two objects are equal,
> while your `equals()` method returns `true` if two objects are equal.”
>
> **Türkçe:** “İki object eşitse `compareTo()` method'u 0 döndürürken
> `equals()` method'unuz `true` döndürür.”

> **English:** “Line 8 checks for the next entry in the queue while leaving it
> in place.”
>
> **Türkçe:** “Line 8, sıradaki entry'yi yerinde bırakarak kontrol eder.”

**YDS ipucu:** İki clause'daki bilgi birbirine karşıtsa “oysa/iken”; zaman
ilişkisi varsa “... sırasında” çevirisi daha doğaldır.

## 22. `which/that` relative clause

### Yapı

```text
noun + which/that + verb ...
noun + which/that + subject + verb ...
```

Önceki noun hakkında bilgi verir.

> **English:** “A `Deque` is a subinterface of `Queue` that allows access at
> both ends.”
>
> **Türkçe:** “`Deque`, iki uçtan da erişime izin veren bir `Queue`
> subinterface'idir.”

> **English:** “It is possible to put these concepts together to write some
> really confusing code, which the exam likes to do.”
>
> **Türkçe:** “Bu kavramları birleştirerek sınavın yapmayı sevdiği gerçekten
> kafa karıştırıcı code yazmak mümkündür.”

**YDS ipucu:** Relative pronoun clause'un subject'iyse atılamaz:
`a queue that allows ...`. Object ise restrictive clause'da atılabilir:
`the value (that) we received`.

## Mini grammar quiz

Boşluklara uygun seçeneği yerleştirin.

1. The list must be sorted ______ binary search can work correctly.
   (`so that` / `despite`)
2. ______ a `List`, a `Set` rejects duplicates. (`Unlike` / `Unless`)
3. You can avoid boxing ______ using `comparingInt()`. (`by` / `since`)
4. The method tells us ______ the key exists. (`whether` / `despite`)
5. ______ using a wildcard, check which operations remain type-safe.
   (`When` / `Rather than`)
6. The code cannot compile ______ the type parameter is declared.
   (`unless` / `even though`)

## Cevaplar

1. **so that** — amaç
2. **Unlike** — farklılık
3. **by** — yöntem
4. **whether** — indirect yes/no question
5. **When** — reduced time/condition clause
6. **unless** — gerekli koşulun yokluğu
