# Unit 10 · Streams — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) stream metninde görülen
İngilizce yapıları teknik okuma ve YDS açısından açıklar. Örnekler kaynak
bağlamından seçilmiş veya aynı teknik kuralla özgün çalışma cümlesi olarak
işaretlenmiştir.

## 1. `by now` + perfect/modal anlam

### Yapı

```text
by now, subject + should/may + have/be ...
```

`by now`, “şimdiye kadar / bu aşamada artık” anlamı verir ve önceki
öğrenmelerden beklenen mevcut durumu anlatır.

> **English:** “By now, you should be comfortable with the lambda and method
> reference syntax.”
>
> **Türkçe:** “Bu aşamada artık lambda ve method reference syntax'ına aşina
> olmalısınız.”

**YDS ipucu:** `by + time point` çoğunlukla o noktaya kadar tamamlanma veya
ulaşılmış durum anlamı kurar.

## 2. `be comfortable with + noun/gerund`

### Yapı

```text
subject + be + comfortable with + noun / V-ing
```

Bir konuya alışkın ve o konuda rahat olmak anlamındadır. `with` preposition
olduğu için sonrasında verb gelirse `-ing` alır.

> **English:** “You should be comfortable with the lambda syntax.”
>
> **Türkçe:** “Lambda syntax'ı konusunda rahat olmalısınız.”

```text
comfortable with use streams   ✗
comfortable with using streams ✓
```

## 3. `both ... and ...`

### Yapı

```text
both + item A + and + item B
```

İki öğeyi birlikte vurgular ve parallel structure (koşut yapı) ister.

> **English:** “Both are used when implementing functional interfaces.”
>
> **Türkçe:** “Her ikisi de functional interface implement ederken kullanılır.”

Subject `both` çoğul olduğu için verb de çoğuldur: `both are`, `both have`.

## 4. Contrast marker: `by contrast`

### Yapı

```text
Statement A. By contrast, statement B.
```

İki kavram arasındaki belirgin farkı gösterir: “buna karşılık”.

> **English:** “The Streams API in this chapter is used for functional
> programming. By contrast, there are also `java.io` streams.”
>
> **Türkçe:** “Bu chapter'daki Streams API functional programming için
> kullanılır. Buna karşılık `java.io` stream'leri de vardır.”

**YDS ipucu:** `by contrast`, `in contrast` ve `on the other hand` contrast
bildirir; cause-result anlamı vermez.

## 5. `despite + noun/gerund`

### Yapı

```text
despite + noun phrase / V-ing
despite the fact that + full clause
```

Beklenen sonucun tersini bildirir: “... rağmen”.

> **English:** “Despite both using the word stream, they are nothing alike.”
>
> **Türkçe:** “İkisinde de stream sözcüğü kullanılmasına rağmen birbirlerine
> hiç benzemezler.”

```text
despite they use the same word             ✗
despite using the same word                ✓
despite the fact that they use the same word ✓
```

## 6. `tend to + base verb`

### Yapı

```text
subject + tend(s) to + V1
```

Genel eğilim bildirir: “genellikle ... eğiliminde olmak”.

> **English:** “Functional programming tends to have a steep learning curve.”
>
> **Türkçe:** “Functional programming'in learning curve'ü genellikle diktir.”

`tend` kesinlik bildirmez; `always` kadar güçlü değildir.

## 7. `once + clause`

### Yapı

```text
once + present simple, future/general result
```

“... olduğunda / ... olduktan sonra” anlamı verir.

> **English:** “It can be very exciting once you get the hang of it.”
>
> **Türkçe:** “Mantığını kavradığınızda çok heyecan verici olabilir.”

Future anlamı olsa bile time clause içinde genellikle `will` yerine present
simple kullanılır.

## 8. `suppose that` ile varsayım

### Yapı

```text
suppose (that) + clause
```

Okuyucudan bir scenario'yu varsaymasını ister: “varsayalım ki”.

> **English:** “Suppose that you are taking an introductory Java class.”
>
> **Türkçe:** “Başlangıç düzeyinde bir Java dersi aldığınızı varsayalım.”

Teknik açıklamalarda `assume that`, `imagine that` ile yakın işlev görür.

## 9. `either ... or ...`

### Yapı

```text
either + alternative A + or + alternative B
```

İki seçenek sunar.

> **English:** “You can either request an empty `Optional` or pass a value for
> the `Optional` to wrap.”
>
> **Türkçe:** “Ya empty `Optional` isteyebilir ya da sarılacak bir value
> geçebilirsiniz.”

**Sık hata:** İki tarafın grammar biçimi parallel olmalıdır:

```text
either request ... or pass ...       ✓
either requesting ... or to pass ... ✗
```

## 10. `whether ... or ...`

### Yapı

```text
whether + alternative/state A + or + alternative/state B
```

“... olup olmadığı” veya iki olasılık anlamı verir.

> **English:** “First we check whether the `Optional` contains a value.”
>
> **Türkçe:** “Önce `Optional`ın value içerip içermediğini kontrol ederiz.”

`if` bazı indirect question'larda kullanılabilse de preposition sonrasında ve
`whether ... or not` kalıbında `whether` daha güvenlidir.

## 11. Purpose: `so that`

### Yapı

```text
main clause + so that + subject + can/will + verb
```

Amaç bildirir: “...abilmek için”.

> **English:** “Use `limit()` so that the infinite stream can terminate.”
>
> **Türkçe:** “Infinite stream'in sona erebilmesi için `limit()` kullanın.”

`so` tek başına result, `so that` çoğunlukla purpose veya intended result
bildirir.

## 12. `rather than + parallel form`

### Yapı

```text
noun rather than noun
V-ing rather than V-ing
base verb rather than base verb
```

Tercih veya contrast bildirir: “... yerine”.

> **English:** “The `spliterator()` method returns a `Spliterator` rather than
> a `Stream`.”
>
> **Türkçe:** “`spliterator()` method'u `Stream` yerine `Spliterator`
> döndürür.”

İki tarafta aynı grammar biçimini kullanmak readability'yi artırır.

## 13. `unless` = `if ... not`

### Yapı

```text
result + unless + positive-form clause
```

Gerekli olumsuz koşulu kısa verir: “... olmadıkça”.

> **English:** “An infinite pipeline will not finish unless an operation
> short-circuits it.”
>
> **Türkçe:** “Bir operation erken sonlandırmadıkça infinite pipeline bitmez.”

```text
unless it does not stop ✗  (double negative)
unless it stops         ✓
```

## 14. `by + gerund` ile yöntem

### Yapı

```text
main action + by + V-ing
```

Bir sonucun nasıl elde edildiğini anlatır: “... yaparak”.

> **English:** “We calculate the average by adding the scores and dividing by
> the number of scores.”
>
> **Türkçe:** “Average değerini score'ları toplayıp score sayısına bölerek
> hesaplarız.”

`by` sonrasında base verb değil gerund gelir.

## 15. `without + gerund`

### Yapı

```text
main clause + without + V-ing
```

Bir eylemin gerçekleşmediğini veya gerekli olmadığını belirtir.

> **English:** “The pipeline can stop without examining every element.”
>
> **Türkçe:** “Pipeline her element'ı incelemeden durabilir.”

`without to examine` değil, `without examining` kullanılır.

## 16. `when + V-ing`: reduced time clause

### Yapı

```text
when + subject + be + V-ing
→ when + V-ing
```

Main clause ve time clause subject'i aynı olduğunda subject ile `be`
düşürülebilir.

> **English:** “Be careful when working with infinite streams.”
>
> **Türkçe:** “Infinite stream'lerle çalışırken dikkatli olun.”

Tam biçim: `when you are working with infinite streams`.

## 17. Relative clause: `that/which + verb`

### Yapı

```text
noun + that/which + verb ...
```

Önündeki noun'u tanımlar.

> **English:** “A terminal operation is an operation that produces a result.”
>
> **Türkçe:** “Terminal operation, sonuç üreten bir operation'dır.”

Defining relative clause'da `that` sık kullanılır. Relative pronoun clause'un
subject'i ise düşürülemez:

```text
an operation produces a result  (ayrı cümle)
an operation that produces a result ✓
```

## 18. `the first/only + noun + to-infinitive`

### Yapı

```text
the first/last/only + noun + to + V1
```

İlgili eylemi yapan ilk/son/tek öğeyi kısa biçimde tanımlar.

> **English:** “`findFirst()` returns the first element to match.”
>
> **Türkçe:** “`findFirst()`, eşleşen ilk element'ı döndürür.”

Relative clause eşdeğeri: `the first element that matches`.

## 19. Cause: `since`

### Yapı

```text
since + clause, result
```

Bu ünite bağlamında çoğunlukla neden bildirir: “...dığı için”.

> **English:** “Since the stream is infinite, `count()` does not terminate.”
>
> **Türkçe:** “Stream infinite olduğu için `count()` sona ermez.”

Perfect tense ve başlangıç zamanı varsa “...den beri” anlamı da olabilir.
Mantıksal cause-result ilişkisini kontrol et.

## 20. `as if` / “think of ... as ...”

### Yapı

```text
think of A as B
```

Bir kavramı analogy ile açıklamayı sağlar: “A'yı B gibi düşünmek”.

> **English:** “Think of an `Optional` as a box that might be empty.”
>
> **Türkçe:** “`Optional`ı empty olabilecek bir kutu gibi düşünün.”

`as`, burada “olarak/gibi” anlamındadır; time veya cause bağlacı değildir.

## Mini quiz · Özgün YDS/teknik İngilizce çalışması

1. `___ now, you should recognize terminal operations.` boşluğunu doldurun.
2. `The stream does not run ___ a terminal operation is called.` “...madıkça”
   anlamındaki bağlacı yazın.
3. `We avoid nested streams by ___ (use) flatMap.` doğru formu yazın.
4. `You can ___ collect into a list ___ reduce to one value.` iki parçalı
   bağlacı yazın.
5. `___ the source is infinite, count() never returns.` neden bildiren bağlaç
   yazın.
6. `A collector is an object ___ performs mutable reduction.` relative pronoun
   yazın.
7. `Be careful when ___ (reuse) a stream.` doğru reduced-clause formu yazın.
8. `Think ___ Optional ___ a box.` iki preposition'ı yazın.

<!-- page-break -->

## Cevaplar ve kısa açıklamalar

1. `By` — `by now`.
2. `unless` — positive clause ile negative condition.
3. `using` — `by + gerund`.
4. `either ... or ...`.
5. `Since` — burada cause bildirir.
6. `that` veya `which`.
7. `reusing` — `when + V-ing`.
8. `of ... as ...` — `think of A as B`.

## Hızlı YDS özeti

```text
by now → bu aşamaya kadar
be comfortable with + noun/V-ing
both A and B
by contrast → karşıtlık
despite + noun/V-ing
tend to + V1
once + clause
suppose that + clause
either A or B
whether ... or ...
so that + clause → amaç
rather than + parallel form
unless = if not
by / without + V-ing
when + V-ing → reduced time clause
think of A as B
```
