# Unit 02 Grammar Notes · Operators

Bu notlar Unit 02 kaynak metnindeki soru kalıpları ve teknik açıklama yapılarını
YDS bakışıyla ele alır.

## 1. `whenever + clause`

### Kısa açıklama

`whenever`, “her ne zaman / her ...-dığında” anlamıyla tekrar eden veya genel
bir condition bildirir.

### Formül

```text
Whenever + subject + verb, subject + verb
```

**EN:** Whenever you mix operands, the compiler determines the result type.
**TR:** Operand'ları her karıştırdığında compiler result type'ı belirler.

> **YDS tip:** `when` tek bir olayı da anlatabilir; `whenever` “her seferinde”
> anlamını daha açık taşır.

## 2. Indirect question: `the order in which`

### Kısa açıklama

`in which`, bir noun'u izleyen formal relative clause kurar. `the order in
which` kalıbı “...-diği sıra” diye çevrilir.

### Formül

```text
noun + preposition + which + subject + verb
```

**EN:** Understand the order in which Java evaluates each operator.
**TR:** Java'nın her operator'ı değerlendirdiği sırayı anla.

> **Common mistake:** `in which` kısmını ayrı bir yer ifadesi gibi çevirmek
> yerine `order` noun'una bağla.

## 3. `be able to + V1`

### Kısa açıklama

Bir işi yapabilme becerisini bildirir. Exam objective'lerde adaydan beklenen
uygulama yeteneğini anlatır.

### Formül

```text
subject + be + able to + V1
```

**EN:** Be able to write code that uses parentheses.
**TR:** Parentheses kullanan kod yazabil.

> **YDS tip:** `able` sonrasında doğrudan fiil değil `to + V1` gelir.

## 4. Reduced passive clause: `when + V3`

### Kısa açıklama

`when applied independently` gibi yapılarda subject ve `be` düşürülür. Anlam
passive kalır.

### Formül

```text
when + subject + be + V3 → when + V3
```

**EN:** What change, when applied independently, would allow the code to compile?
**TR:** Birbirinden bağımsız uygulandığında hangi değişiklik kodun derlenmesini
sağlar?

## 5. `allow + object + to-infinitive`

### Kısa açıklama

Bir kişi veya şeyin bir eylemi yapmasını mümkün kılmayı anlatır.

### Formül

```text
allow + object + to + V1
```

**EN:** Which data types allow the snippet to compile?
**TR:** Hangi data type'lar kod parçasının derlenmesini sağlar?

> **Common mistake:** Active yapıda `allow the code compile` değil, `allow the
> code to compile` kullanılır.

## 6. `while` ile karşıtlık

### Kısa açıklama

`while`, eş zaman anlamının yanında iki farklı davranışı karşılaştırarak “iken”
anlamı verir.

### Formül

```text
clause, while + contrasting clause
```

**EN:** Post-increment returns the original value, while pre-decrement returns
the new value.
**TR:** Post-increment özgün değeri döndürürken pre-decrement yeni değeri döndürür.

## 7. `after + passive clause`

### Kısa açıklama

Bir state'in başka bir operation tamamlandıktan sonraki durumunu sorar.

**EN:** What are the values after the snippet is executed?
**TR:** Kod parçası çalıştırıldıktan sonra değerler nedir?

`is executed`, `be + V3` biçiminde passive voice'tur; kod eylemi yapan değil,
çalıştırılan öğedir.

## 8. `as long as` ile yeter koşul

`as long as`, bir sonucun gerçekleşmesi için yeterli koşulu “-dığı sürece”
anlamıyla verir.

```text
main clause + as long as + condition clause
```

**EN:** You do not need complicated bit arithmetic as long as you remember this
rule.
**TR:** Bu kuralı hatırladığınız sürece karmaşık bit aritmetiğine ihtiyacınız
yoktur.

> **Common mistake:** Bu bağlamda `as long as` süre uzunluğunu değil, koşulu
bildirir.

## 9. Beklenmeyen karşıtlık: `even though`

### Kısa açıklama

`even though + clause`, beklenen sonucun tersini vurgulayarak “-mesine rağmen”
anlamı verir. `although` ile benzerdir; vurgu genellikle daha güçlüdür.

### Formül

```text
Even though + subject + verb, main clause
```

**EN:** Even though the table includes casting, we postpone discussing it.
**TR:** Tablo casting'i içermesine rağmen onu ele almayı erteliyoruz.

> **YDS tip:** `despite/in spite of` sonrasında noun veya `V-ing`; `even though`
sonrasında subject + verb bulunan tam clause beklenir.

## 10. İstisna bildiren `unless`

### Kısa açıklama

`unless`, “if ... not” anlamıyla genel kurala istisna veya negatif condition
ekler.

### Formül

```text
main clause + unless + affirmative clause
```

**EN:** Numbers are positive unless accompanied by a negative unary operator.
**TR:** Negatif unary operator eşlik etmedikçe sayılar pozitiftir.

> **Common mistake:** `unless` zaten negatif condition taşır; ardından gereksiz
bir `not` kullanma.

## 11. Farkı sınırlayan `except that`

### Kısa açıklama

`except that + clause`, iki şeyin büyük ölçüde aynı olduğunu, yalnız belirtilen
noktada ayrıldığını söyler.

### Formül

```text
clause + except that + subject + verb
```

**EN:** Conditional operators are identical to logical operators, except that
the right side may not be evaluated.
**TR:** Conditional operator'lar logical operator'larla aynıdır; yalnız sağ
tarafın değerlendirilmeyebilmesi bakımından ayrılır.

## 12. Sonuç bağlayıcısı: `therefore`

### Kısa açıklama

`therefore`, önceki bilgiden mantıksal sonuç çıkarır ve “bu nedenle/dolayısıyla”
anlamına gelir.

### Formül

```text
sentence; therefore, result sentence
```

**EN:** The value cannot be assigned to an `int`; therefore, the code does not
compile.
**TR:** Value bir `int`e atanamaz; dolayısıyla kod derlenmez.

> **YDS tip:** `therefore` bir conjunctive adverb'dür; iki independent clause'u
tek başına virgülle bağlamaz.

## 13. Alternatif durum: `otherwise`

### Kısa açıklama

`otherwise`, “aksi takdirde/bunun dışında” anlamıyla önceki condition'ın
sağlanmadığı durumu gösterir.

**EN:** Print “O'clock” for whole numbers; otherwise, print the value.
**TR:** Tam sayılarda “O'clock” yazdır; aksi takdirde value'yu yazdır.

## 14. Modal passive: `may + be + V3`

### Kısa açıklama

`may + be + V3`, bir işlemin gerçekleşmesinin mümkün olduğunu fakat kesin
olmadığını passive biçimde anlatır.

### Formül

```text
subject + may + be + V3
```

**EN:** The right side of the expression may never be evaluated.
**TR:** Expression'ın sağ tarafı hiçbir zaman değerlendirilmeyebilir.

> **Common mistake:** Modal'dan sonra `be` yalın kalır: `may be evaluated`; `may
is evaluated` kullanılmaz.

## 15. Paralel karşılaştırma: `the + comparative, the + comparative`

### Kısa açıklama

İki değişimin birlikte arttığını veya azaldığını “ne kadar ..., o kadar ...”
anlamıyla gösterir.

### Formül

```text
The + comparative + clause, the + comparative + clause
```

**EN:** The better you understand this chapter, the more prepared you will be.
**TR:** Bu bölümü ne kadar iyi anlarsanız o kadar hazırlıklı olursunuz.

> **YDS tip:** İlk `the` article değil, comparative correlation yapısının
parçasıdır.

## Mini quiz

1. `Whenever two bytes are added, they are promoted to int.` cümlesini çevir.
2. `the order in which` kalıbını kullanarak bir precedence cümlesi yaz.
3. Boşluğu tamamla: `This cast allows the expression ___ compile.`
4. `while` kullanarak prefix ve postfix davranışlarını karşılaştır.

## Cevaplar

1. İki byte her toplandığında `int`e promote edilir.
2. Örnek: *Parentheses change the order in which operators are evaluated.*
3. `to`
4. Örnek: *Prefix increment returns the new value, while postfix increment
   returns the original value.*

## Kısa tekrar özeti

- Genel/tekrarlanan koşul: `whenever + clause`
- Formal relative yapı: `the order in which`
- Beceri: `be able to + V1`
- Reduced passive: `when + V3`
- Olanak sağlama: `allow + object + to + V1`
- Karşıtlık: `while + clause`
- Beklenmeyen karşıtlık: `even though + clause`
- İstisna: `unless + clause`
- Modal passive: `may + be + V3`
- Paralel değişim: `the + comparative, the + comparative`
