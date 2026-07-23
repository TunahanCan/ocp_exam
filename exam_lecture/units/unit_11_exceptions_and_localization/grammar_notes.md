# Unit 11 · Exceptions and Localization — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) exception ve
localization metninden seçilen İngilizce yapıları teknik okuma/YDS açısından
açıklar.

## 1. `adapt to + noun`

### Yapı

```text
adapt to + noun / pronoun / V-ing
adapt something to + noun
```

`to` burada preposition'dır; “...e uyum sağlamak/uyarlamak” anlamı verir.

> **English:** “This chapter is about creating applications that adapt to
> change.”
>
> **Türkçe:** “Bu chapter, değişime uyum sağlayan application'lar oluşturmak
> hakkındadır.”

```text
adapt to change   ✓
adapt to changing requirements ✓
adapt to change requirements   ✗
```

## 2. `what happens if ...?`

### Yapı

```text
What happens if + present simple?
What would happen if + past simple?
```

İlki gerçek/genel olasılığı, ikincisi hypothetical durumu sorar.

> **English:** “What happens if a user enters invalid data on a web page?”
>
> **Türkçe:** “Bir kullanıcı web sayfasına invalid data girerse ne olur?”

YDS'de `if` clause ile result clause arasındaki tense uyumuna dikkat et.

## 3. `in the middle of + noun/gerund`

### Yapı

```text
in the middle of + noun / V-ing
```

Bir süreç devam ederken araya giren olayı anlatır.

> **English:** “What if our connection to a database goes down in the middle
> of a sale?”
>
> **Türkçe:** “Database connection bir satışın ortasında kesilirse ne olur?”

`of` preposition'ından sonra verb gelirse gerund kullanılır:
`in the middle of processing a request`.

## 4. `make sure (that) + clause`

### Yapı

```text
make sure (that) + subject + verb
```

Bir durumun gerçekleşmesini güvence altına almak anlamındadır.

> **English:** “One way to make sure your applications respond to change is
> to build in support early on.”
>
> **Türkçe:** “Application'ların değişime karşılık vermesini sağlamanın bir
> yolu desteği baştan tasarlamaktır.”

`make sure to + V1` aynı subject'in yapacağı eylem için de kullanılabilir:
`Make sure to close the resource.`

## 5. `does not mean ...; it means ...`

### Yapı

```text
A does not mean B. It means C.
```

Yanlış yorumu reddedip doğru anlamı verir.

> **English:** “Supporting localization doesn’t mean you actually need to
> support specific languages right away. It just means your application can be
> more easily adapted in the future.”
>
> **Türkçe:** “Localization desteği, belirli dilleri hemen desteklemeniz
> gerektiği anlamına gelmez. Yalnız application'ın gelecekte daha kolay
> uyarlanabileceği anlamına gelir.”

`just` burada “yalnızca” anlamıyla scope'u daraltır.

## 6. `by the end of + time period`

### Yapı

```text
by the end of + noun, result
```

Belirli bir dönemin sonuna kadar ulaşılacak durumu anlatır.

> **English:** “By the end of this chapter, we hope we’ve provided structure.”
>
> **Türkçe:** “Bu chapter'ın sonuna kadar bir yapı sunmuş olmayı umuyoruz.”

`by`, deadline; `until`, o ana kadar süren durum bildirir:

```text
finish by Friday   → en geç Friday
work until Friday  → Friday'e kadar çalış
```

## 7. `just about any`

### Yapı

```text
just about + any/every + noun
```

“Neredeyse her” anlamında informal fakat yaygın bir emphasis kalıbıdır.

> **English:** “A program can fail for just about any reason.”
>
> **Türkçe:** “Program neredeyse her nedenle fail olabilir.”

`just about` burada “tam hakkında” değil, `almost/nearly` anlamındadır.

## 8. `as you can see`

### Yapı

```text
as + subject + can + see/observe, main clause
```

Okuyucunun önceki örnekten çıkarabileceği sonucu işaretler.

> **English:** “As you can see, some of these are coding mistakes.”
>
> **Türkçe:** “Görülebileceği gibi bunların bazıları coding mistake'tir.”

Buradaki `as` “...dığı gibi” anlamındadır; cause anlamındaki `as` ile
karıştırma.

## 9. `beyond someone’s control`

### Yapı

```text
be + beyond + possessive + control
```

Bir kişinin müdahale edemediği durumu anlatır.

> **English:** “Others are completely beyond your control.”
>
> **Türkçe:** “Diğerleri tamamen kontrolünüz dışındadır.”

**Related phrase:** `within your control` → kontrolünüz dahilinde.

## 10. `deal with + noun`

### Yapı

```text
deal with + problem/situation/exception
```

Bir sorunu ele almak, yönetmek anlamındadır.

> **English:** “What the program can do is deal with the situation.”
>
> **Türkçe:** “Programın yapabileceği şey durumu ele almaktır.”

`deal` sonrasında doğrudan object değil `with` gerekir:
`deal the exception` ✗, `deal with the exception` ✓.

## 11. `either ... or ...`

### Yapı

```text
either + verb phrase A + or + verb phrase B
```

İki alternative'i parallel biçimde sunar.

> **English:** “You can either deal with the exception or make it the calling
> code’s problem.”
>
> **Türkçe:** “Exception'ı ya handle edebilir ya da caller code'un problemi
> haline getirebilirsiniz.”

İki tarafta verb biçimini eşleştir: `either deal ... or make ...`.

## 12. Passive obligation: `must be + V3`

### Yapı

```text
subject + must be + past participle
```

Zorunluluğu passive biçimde verir.

> **English:** “A checked exception must be declared or handled.”
>
> **Türkçe:** “Checked exception declare veya handle edilmelidir.”

Agent önemli değilse passive teknik metinde sık kullanılır.

## 13. `be required to + verb`

### Yapı

```text
subject + be required to + V1
```

Kural veya zorunluluk bildirir.

> **English:** “A method is not required to throw an exception that it
> declares.”
>
> **Türkçe:** “Method declare ettiği exception'ı throw etmek zorunda değildir.”

`must` ile yakın anlamlıdır; `not required to` “yapması yasaktır” değil,
“yapmak zorunda değildir” demektir.

## 14. `be capable of + gerund`

### Yapı

```text
subject + be capable of + V-ing
```

Bir eylemi yapabilme kapasitesini bildirir.

> **English:** “The try block is not capable of throwing an `IOException`.”
>
> **Türkçe:** “Try block `IOException` throw edebilecek durumda değildir.”

`of` sonrasında infinitive değil gerund gelir:
`capable of throwing` ✓.

## 15. `due to + noun`

### Yapı

```text
result/state + due to + noun phrase
```

Neden bildirir: “... nedeniyle”.

> **English:** “The subclass catch is unreachable due to the earlier
> superclass catch.”
>
> **Türkçe:** “Subclass catch, önceki superclass catch nedeniyle
> unreachable'dır.”

`because` full clause, `due to` noun phrase alır:

```text
because the catch is earlier ✓
due to the earlier catch     ✓
due to the catch is earlier  ✗
```

## 16. `regardless of + noun/clause word`

### Yapı

```text
regardless of + noun / wh-clause
```

Bir koşulun sonucu değiştirmediğini anlatır: “... bakılmaksızın”.

> **English:** “The first line produces a runtime exception regardless of what
> is inserted into the blank.”
>
> **Türkçe:** “Boşluğa ne yazılırsa yazılsın ilk satır runtime exception
> üretir.”

`regardless` sonrasında çoğunlukla `of` gerekir.

## 17. `in the order in which`

### Yapı

```text
in the order in which + subject + verb
```

Sequence'in hangi sıraya göre olduğunu açıklar.

> **English:** “Catch blocks are checked in the order in which they appear.”
>
> **Türkçe:** “Catch block'lar göründükleri sırayla kontrol edilir.”

Kısa eşdeğer: `in the order they appear`; relative phrase düşürülebilir.

## 18. `once + past participle`

### Yapı

```text
once + subject + be + V3
→ once + V3
```

Reduced passive time/condition clause'dur.

> **English:** “Once selected, only resources in that hierarchy are allowed.”
>
> **Türkçe:** “Bir kez seçildikten sonra yalnız o hierarchy'deki resource'lara
> izin verilir.”

Tam biçim: `Once the hierarchy is selected, ...`.

## 19. `instead of + gerund`

### Yapı

```text
instead of + noun / V-ing
```

Bir seçenek yerine başka seçeneği kullanmayı anlatır.

> **English:** “The method returns `-1` instead of throwing an exception.”
>
> **Türkçe:** “Method exception throw etmek yerine `-1` döndürür.”

`instead of throw` değil, `instead of throwing` kullanılır.

## 20. `without + gerund`

### Yapı

```text
main clause + without + V-ing
```

Bir eylemin gerçekleşmediğini belirtir.

> **English:** “The code compiles without handling the unchecked exception.”
>
> **Türkçe:** “Kod unchecked exception'ı handle etmeden derlenir.”

`without` preposition olduğu için sonrasında gerund gelir.

## 21. `starting with` ve `followed by`

### Yapı

```text
starting with + noun
X, followed by Y
```

Sequence açıklamalarında başlangıç ve sonraki adımı gösterir.

> **English:** “Java looks for the most specific bundle first, followed by its
> parent.”
>
> **Türkçe:** “Java önce en specific bundle'ı, ardından parent'ını arar.”

`followed by` reduced passive yapıdır: `which is followed by`.

## 22. `if and only if`

### Yapı

```text
A if and only if B
```

Necessary and sufficient condition (gerekli ve yeterli koşul) bildirir;
matematikte `iff`.

> **English:** “The variable is effectively final if and only if it is not
> reassigned after initialization.”
>
> **Türkçe:** “Variable yalnız ve ancak initialization sonrasında reassign
> edilmiyorsa effectively finaldır.”

Sıradan `if` yalnız bir yönlü yeter koşul verebilir; `if and only if` iki yönü
de kapsar.

## 23. `the more specific ..., the earlier ...`

### Yapı

```text
the + comparative + clause, the + comparative + clause
```

İki değişimin birlikte ilerlediğini belirtir.

> **English:** “The more specific the locale, the earlier its bundle is
> considered.”
>
> **Türkçe:** “Locale ne kadar specific ise bundle'ı o kadar erken
> değerlendirilir.”

Türkçede “ne kadar ... o kadar ...” biçimi doğaldır.

## 24. `even if` ile varsayımsal ödünleme

### Yapı

```text
even if + condition, unchanged result
```

Koşul gerçekleşse bile sonucun değişmediğini bildirir.

> **English:** “The method compiles even if it never throws the declared
> exception.”
>
> **Türkçe:** “Method declare edilen exception'ı hiç throw etmese bile
> derlenir.”

`even though` gerçek bir duruma, `even if` olası/varsayımsal duruma daha
yatkındır.

## Mini quiz · Özgün YDS/teknik İngilizce çalışması

1. `Applications must adapt ___ changing requirements.` preposition nedir?
2. `The code compiles ___ handling the unchecked exception.` “...meden”
   yapısını tamamlayın.
3. `The resource is capable of ___ (throw) an exception during close.`
4. `The child catch is unreachable ___ to the parent catch.` boşluğu doldurun.
5. `The bundles are checked in the order ___ which they appear.`
6. `___ selected, the hierarchy does not switch to another locale.` reduced
   clause bağlacını yazın.
7. `The method returns null instead of ___ (throw).`
8. `The ___ specific the locale, the earlier Java checks it.`
9. “... ne yazılırsa yazılsın” anlamı için `regardless ___ what ...`.
10. `not required to throw` “throw etmesi yasaktır” mı, “zorunda değildir” mi?

<!-- page-break -->

## Cevaplar ve kısa açıklamalar

1. `to` — `adapt to`.
2. `without` — `without + gerund`; devamı `handling`.
3. `throwing` — `capable of + gerund`.
4. `due` — bütün phrase `due to`.
5. `in`.
6. `Once`.
7. `throwing` — `instead of + gerund`.
8. `more` — correlative comparative.
9. `of`.
10. “Throw etmek zorunda değildir.” Prohibition anlamı vermez.

## Hızlı YDS özeti

```text
adapt to + noun/V-ing
what happens if + present?
in the middle of + noun/V-ing
make sure (that) + clause
by the end of → deadline
just about any → almost any
deal with + problem
must be + V3
be required to + V1
be capable of + V-ing
due to + noun
regardless of + noun/wh-clause
in the order in which
once + V3 → reduced passive
instead of / without + V-ing
the more ..., the more ...
even if + hypothetical condition
```
