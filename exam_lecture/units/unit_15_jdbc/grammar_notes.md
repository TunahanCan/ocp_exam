# Unit 15 · JDBC — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) relational database ve
JDBC anlatımından seçilen gerçek İngilizce yapılarını teknik okuma ve YDS
bakış açısıyla açıklar.


Örnekler kaynak bağlamını öğretmek için seçilmiş veya sadeleştirilmiştir;
“kaynak alıntısı” diye belirtilmeyen cümleler birebir kitap alıntısı değildir.
Her oturumda bir yapıyı çalış: **ana yüklem → özne → bağlaç → yan cümle →
doğal Türkçe** sırasını izle. Yapıyı ertesi gün örneğe bakmadan yeniden kur.

## 1. `stand for`

### Yapı

```text
abbreviation + stand(s) for + full expression
```

Bir abbreviation'ın açılımını verir.

> **English:** “JDBC stands for Java Database Connectivity.”
>
> **Türkçe:** “JDBC, Java Database Connectivity ifadesinin kısaltmasıdır.”

YDS ipucu: Buradaki `stand` “ayakta durmak” değildir. `represent` veya `mean`
ile yakın anlamlıdır.

## 2. `consist of`

### Yapı

```text
whole + consist(s) of + parts
```

Bir bütünün hangi parçalardan oluştuğunu belirtir.

> **English:** “Tables consist of rows and columns.”
>
> **Türkçe:** “Tablolar, satır ve sütunlardan oluşur.”

`consist of` passive kullanılmaz: `is consisted of` standart kullanım değildir.
Yakın yapı: `be composed of`.

## 3. `refer to A as B`

### Yapı

```text
refer to + object + as + name/category
object + be referred to as + name/category
```

Bir kavramı belirli bir adla anmayı gösterir.

> **English:** “The operations are referred to as CRUD.”
>
> **Türkçe:** “İşlemler CRUD olarak adlandırılır.”

Passive yapıda `to` ve `as` birlikte korunur. `refer` tek başına “başvurmak”,
bu kalıpta “olarak adlandırmak” anlamındadır.

## 4. `unlike + noun`

### Yapı

```text
unlike + noun/pronoun, complete clause
```

İki şey arasında contrast kurar.

> **English:** “Unlike Java, SQL keywords are case insensitive.”
>
> **Türkçe:** “Java’dan farklı olarak SQL anahtar kelimeleri büyük/küçük harfe duyarlı değildir.”

`unlike` preposition'dır; ardından doğrudan finite clause gelmez. Clause için
`although` veya `whereas` gerekir.

## 5. `while` ile concessive contrast

### Yapı

```text
while + clause, contrasting main clause
```

Bu kullanım zaman değil “...olsa da / buna karşın” anlamı taşır.

> **English:** “While the exam is database agnostic, the examples use a
> particular database.”
>
> **Türkçe:** “Sınav belirli bir veritabanından bağımsız olsa da örnekler belirli bir veritabanı kullanır.”

YDS'de context'e göre temporal `while` (“...iken”) ile concessive `while`
ayrılmalıdır.

## 6. `along with`

### Yapı

```text
main noun + along with + additional noun
```

“...ile birlikte / ...yanı sıra” anlamında ek bilgi verir.

> **English:** “The driver contains the key implementations along with other
> interfaces.”
>
> **Türkçe:** “Sürücü, diğer arayüzlerin yanı sıra temel gerçekleştirimleri içerir.”

Subject–verb agreement çoğunlukla `along with` öncesindeki main subject'e göre
yapılır: `The driver, along with its classes, is ...`

## 7. `whether ... or ...`

### Yapı

```text
whether + alternative A + or + alternative B
```

İki ihtimali tek noun clause içinde toplar.

> **English:** “The boolean indicates whether the first result is a result
> set or an update count.”
>
> **Türkçe:** “Boolean değer, ilk sonucun bir sonuç kümesi mi yoksa güncelleme sayısı mı olduğunu gösterir.”

Türkçeye çoğunlukla “...olup olmadığı” veya “...mi ...mi” ile çevrilir.

## 8. `rather than`

### Yapı

```text
A rather than B
verb A rather than verb B
```

B yerine A'nın seçildiğini belirtir.

> **English:** “Use an `if` statement rather than a `while` loop for one row.”
>
> **Türkçe:** “Tek satır için `while` döngüsü yerine `if` deyimi kullanın.”

İki taraf paralel grammar formunda olmalıdır. `rather than`ı otomatik olarak
“...den daha çok” diye çevirmek teknik cümlede anlamı bozabilir.

## 9. `instead of + V-ing/noun`

### Yapı

```text
instead of + noun/gerund
```

Bir yöntem yerine başka yöntemin kullanıldığını gösterir.

> **English:** “Use bind variables instead of concatenating user input.”
>
> **Türkçe:** “Kullanıcı girdisini birleştirmek yerine bağlama değişkenleri kullanın.”

`of` preposition olduğu için ardından `concatenate` değil `concatenating`
gelir.

## 10. `allow + object + to + V1`

### Yapı

```text
allow + noun/pronoun + to + base verb
```

Bir bileşene eylem olanağı verdiğini bildirir.

> **English:** “A `PreparedStatement` allows you to set parameters.”
>
> **Türkçe:** “`PreparedStatement`, parametrelere değer atamanıza olanak verir.”

Passive:

```text
object + be allowed to + V1
```

Sık hata: Active kullanımda object'i veya `to`yu atlamak.

## 11. `by + V-ing`

### Yapı

```text
main clause + by + gerund
```

Sonucun hangi yöntemle elde edildiğini açıklar.

> **English:** “You create a statement by calling `prepareStatement()`.”
>
> **Türkçe:** “`prepareStatement()` çağırarak bir deyim oluşturursunuz.”

`by` sonrasında base verb değil gerund kullanılır.

## 12. `before/after + V-ing`

### Yapı

```text
before/after + gerund
before/after + subject + finite verb
```

Technical operation sırasını bildirir.

> **English:** “Set every bind variable before executing the query.”
>
> **Türkçe:** “Sorguyu çalıştırmadan önce her bağlama değişkenine değer atayın.”

Gerund clause'un gizli subject'i main clause subject'iyle mantıksal olarak
uyumlu olmalıdır.


**Gizli özneyi bul:** “Set every bind variable before executing the query.” bir emir cümlesidir; gizli özne `[you]`, ana yüklem `[set]`, nesne `[every bind variable]` olur. `before executing` → `before you execute`; aynı kişi iki işi de yapar.

**Sıra tuzağı:** `before` yerine `after` koymak yalnız dilbilgisini değil JDBC işlem sırasını değiştirir. Önceden atanmış parametre değerleri korunabilir; her yeniden çalıştırmada bütün setter'ları yinelemek zorunlu değildir.

**Kaynak bağlamı:** [Working with Parameters](bilingual_notes.md#working-with-parameters).

## 13. `when + passive clause`

### Yapı

```text
when + subject + be + past participle, main clause
when + past participle, main clause
```

Bir state veya event gerçekleştiğinde ortaya çıkan sonucu anlatır.

> **English:** “When autocommit is enabled, each statement is committed
> automatically.”
>
> **Türkçe:** “Otomatik kalıcılaştırma etkinleştirildiğinde her deyim otomatik olarak kalıcılaştırılır.”

`when enabled` reduced clause'tur; omitted subject main clause ile doğru
eşleşmelidir.

## 14. `once + clause`

### Yapı

```text
once + subject + verb, main clause
```

Bir action tamamlanır tamamlanmaz sonraki sonucu bildirir.

> **English:** “Once `next()` returns false, the cursor is no longer on a valid row.”
>
> **Türkçe:** “`next()` false döndürdükten sonra imleç artık geçerli bir satırın üzerinde değildir.”

Context'e göre “...ınca”, “...dıktan sonra” veya “artık” ile çevrilebilir.

## 15. Real conditional: `if + present`

### Yapı

```text
if + present simple, present simple / can / will + V1
```

Gerçek olasılık veya genel API kuralını anlatır.

> **English:** “If the query returns no rows, `next()` returns false.”
>
> **Türkçe:** “Sorgu hiç satır döndürmezse `next()` false döndürür.”

Future anlamında bile condition clause içinde çoğunlukla `will return` yerine
present simple kullanılır.

## 16. `unless`

### Yapı

```text
unless + clause = if ... not
```

Olumsuz koşul bildirir.

> **English:** “Unless the question says otherwise, assume the SQL is valid.”
>
> **Türkçe:** “Soru aksini söylemedikçe SQL'in geçerli olduğunu varsayın.”

`unless` zaten negative anlam taşır; `unless ... not` çoğunlukla istenmeyen
çifte olumsuzluk üretir.

## 17. `so that`

### Yapı

```text
main clause + so that + subject + can/will + V1
```

Amaç veya hedef sonucu belirtir.

> **English:** “Register the output parameter so that JDBC can retrieve its
> value.”
>
> **Türkçe:** “JDBC, değerini alabilsin diye çıktı parametresini kaydedin.”

`so + adjective + that` derece-sonuç yapısıyla karıştırma.

## 18. `since` — neden veya başlangıç zamanı

### Yapı

```text
since + clause
since + point in time
```

> **English:** “Use `executeQuery()` since the procedure returns rows.”
>
> **Türkçe:** “Saklı yordam satır döndürdüğü için `executeQuery()` kullanın.”

Bu örnekte `since` neden bildirir. Present perfect ile “...den beri” anlamında
da kullanılabilir; doğru anlam context'ten çıkarılır.

## 19. `as + clause`

### Yapı

```text
as + subject + verb, main clause
```

Context'e göre zaman (“...iken”), neden (“...dığı için”) veya biçim
(“...dığı gibi”) gösterebilir.

> **English:** “As the cursor advances, each iteration represents one row.”
>
> **Türkçe:** “İmleç ilerledikçe her yineleme bir satırı temsil eder.”

YDS sorularında `as` için tek bir Türkçe karşılığı ezberlemek yerine iki clause
arasındaki semantic ilişkiyi belirle.

## 20. `as long as`

### Yapı

```text
as long as + condition clause
```

“...dığı sürece / koşuluyla” anlamı verir.

> **English:** “The index is valid as long as it refers to an existing
> column.”
>
> **Türkçe:** “İndeks, var olan bir sütunu gösterdiği sürece geçerlidir.”

Süre anlamındaki `as long as` ile koşul anlamını context ayırır.

## 21. `not ... until`

### Yapı

```text
subject + do/does not + verb + until + event
```

Bir eylemin belirli ana kadar gerçekleşmediğini vurgular.

> **English:** “The error does not appear until the statement is executed.”
>
> **Türkçe:** “Hata, deyim çalıştırılana kadar ortaya çıkmaz.”

Türkçede olumlu görünen “ancak ... olduğunda” çevirisi de aynı anlamı
verebilir.


**Cümleyi parçala:** `[The error]` özne, `[does not appear]` olumsuz yüklem; `[until the statement is executed]` zaman sınırıdır. İkinci yüklem `[is executed]` edilgendir: deyim çalıştırılır.

**Doğal alternatif:** “Hata ancak deyim çalıştırıldığında ortaya çıkar.” Türkçe cümle olumlu görünür; `not … until` anlamı korunur. Bu, belirli örnekteki hatayı anlatır; bütün JDBC hatalarının aynı aşamada oluştuğu genellemesini yapma.

**Kaynak bağlamı:** [Executing a PreparedStatement](bilingual_notes.md#executing-a-preparedstatement).

## 22. `there is/are`

### Yapı

```text
there is + singular/uncountable noun
there are + plural noun
```

Bir şeyin varlığını tanıtır.

> **English:** “There are overloaded methods for selecting a result-set
> type.”
>
> **Türkçe:** “Sonuç kümesi türünü seçmek için aşırı yüklenmiş metotlar vardır.”

Buradaki `there` yer zarfı değildir; existential subject yapısının parçasıdır.

## 23. Relative clause: `that/which`

### Yapı

```text
noun + that/which + verb ...
```

Önceki noun'u tanımlar veya onun hakkında ek bilgi verir.

> **English:** “A bind variable is a placeholder that receives its value at
> runtime.”
>
> **Türkçe:** “Bağlama değişkeni, değerini çalışma zamanında alan bir yer tutucudur.”

Defining clause içinde `that` veya `which` kullanılabilir. Virgülle ayrılan non-defining clause için `that` kullanılmaz; bu örneklerde `which` gerekir.

## 24. `the order in which`

### Yapı

```text
the order in which + subject + verb
```

Operation sırasını tanımlayan formal relative clause'tur.

> **English:** “Resources close in the reverse order from that in which they
> were opened.”
>
> **Türkçe:** “Kaynaklar, açıldıkları sıranın tersinde kapanır.”

Daha sade eşdeğer: `the order that they were opened in`. YDS metinlerinde
preposition + relative pronoun biçimi sık görülür.

## 25. `no matter + wh-clause`

### Yapı

```text
no matter + what/which/how/where + clause
```

Sonucu değiştirmeyen olasılığı ifade eder.

> **English:** “The cursor is invalid no matter which getter is called.”
>
> **Türkçe:** “Hangi okuyucu metot çağrılırsa çağrılsın imleç geçersizdir.”

Yakın yapı: `regardless of which ...`

## 26. Modal passive

### Yapı

```text
modal + be + past participle
```

Possibility, obligation veya ability'yi passive biçimde anlatır.

> **English:** “The parameter can be referenced by name or by index.”
>
> **Türkçe:** “Parametre, adıyla veya indeksiyle belirtilebilir.”

Modal'dan sonra `be` yalın halde, ardından past participle gelir:
`can be referenced`; `can is referenced` yanlıştır.

## 27. `be supposed to`

### Yapı

```text
subject + be supposed to + V1
```

Beklenti, kural veya amaçlanan davranışı belirtir.

> **English:** “You are supposed to use braces for JDBC escape syntax.”
>
> **Türkçe:** “JDBC kaçış sözdizimi için süslü parantez kullanmanız beklenir.”

Mutlak teknik zorunlulukta `must`; sınav beklentisi veya convention için
`be supposed to` görülebilir.

## 28. `may/might/can + V1`

### Yapı

```text
subject + may/might/can + base verb
```

`may/might` possibility; `can` ability veya genel possibility bildirir.

> **English:** “The exact exception message may vary by driver.”
>
> **Türkçe:** “İstisna mesajının tam metni sürücüye göre değişebilir.”

Modal'dan sonra `to` gelmez, verb `-s` almaz.

## 29. Özgün mini quiz

### Soru 1

“The acronym JDBC ___ Java Database Connectivity.”

A. consists of<br>
B. stands for<br>
C. refers<br>
D. depends on

### Soru 2

“Set each parameter ___ executing the query.”

A. before<br>
B. unless<br>
C. whereas<br>
D. no matter

### Soru 3

Hangi cümle “Driver'a göre değişebilir” anlamına gelir?

A. It must vary by driver.<br>
B. It may vary by driver.<br>
C. It is varied until driver.<br>
D. It stands for driver.

### Soru 4

“Resources are closed in the reverse order ___ they were opened.”

A. which<br>
B. what<br>
C. in which<br>
D. whereas

<!-- page-break -->

### Soru 5

“Use a setter ___ JDBC can receive the input value.”

A. no matter<br>
B. so that<br>
C. unlike<br>
D. rather than

## 30. Cevaplar

1. **B.** `stand for`, abbreviation'ın açılımını verir.
2. **A.** `before + V-ing`, operation order belirtir.
3. **B.** `may`, possibility bildirir.
4. **C.** Formal relative clause `in which` gerekir.
5. **B.** `so that` amaç bildirir.

## Kısa tekrar

- Tanım: `stand for`, `consist of`, `refer to ... as`
- Contrast: `unlike`, `while`, `rather than`, `instead of`
- Amaç/yöntem: `so that`, `by + V-ing`
- Koşul: `if`, `unless`, `as long as`
- Sıra: `before/after + V-ing`, `once`, `the order in which`
- Possibility: `may/might/can + V1`, modal passive
