# Unit 02 · Operators — Practice Quiz

Bu belge sekiz adet **OCP tarzı özgün çalışma sorusu** içerir. Sorular gerçek
sınavdan alınmamıştır. Her kod sorusunda önce operator precedence ve operand
type'larını işaretle; ardından side effect'leri soldan sağa uygula.

## Çalışma yönergesi
Yanlış yaptığın sorunun kuralını [teknik notta](technical_memory_notes.md) bul;
cevabı kapatıp aynı kodda tek bir değeri değiştirerek sonucu yeniden tahmin et.
Dil sorusunda hem doğal çeviriyi hem bağlacın kurduğu ilişkiyi açıklayabildiysen
başarılı say. [README oturum rotası](README.md) kaynak sorularına dönüşü gösterir.

## Sorular

### Soru 1

**Odak:** Evaluation order

Aşağıdaki programın çıktısı nedir?

```java
public class Counter {
    public static void main(String[] args) {
        int x = 2;
        int y = x++ * 3 + ++x;
        System.out.println(x + ":" + y);
    }
}
```

A. `3:9`<br>
B. `4:10`<br>
C. `4:12`<br>
D. Kod derlenmez.

### Soru 2

**Odak:** Numeric promotion

Aşağıdaki kod için hangisi doğrudur?

```java
public class Narrowing {
    public static void main(String[] args) {
        byte value = 10;
        value = value + 1;
        System.out.println(value);
    }
}
```

A. `11` yazdırır.<br>
B. Kod derlenmez.<br>
C. `ClassCastException` oluşur.<br>
D. Overflow nedeniyle `-128` yazdırır.

### Soru 3

**Odak:** Short-circuit davranışı

`&&` ile `&` operator'larının `boolean` operand'larla kullanımı hakkında
hangisi doğrudur?

A. İkisi de sağ operand'ı her zaman değerlendirir.<br>
B. `&` short-circuit yapar, `&&` yapmaz.<br>
C. `&&` sonucu soldan belirlenebiliyorsa sağ operand'ı değerlendirmez; `&`
   iki operand'ı da değerlendirir.<br>
D. `&` yalnız numeric operand'larla kullanılabilir.

### Soru 4

**Odak:** Boolean sonuçlar

Aşağıdaki declaration'lardan **hangi ikisi**, bir method body içinde bağımsız
olarak değerlendirildiğinde başarıyla tamamlanır ve `true` değerini üretir?

A. `boolean a = true | false;`<br>
B. `boolean b = true || (1 / 0 > 0);`<br>
C. `boolean c = null instanceof String;`<br>
D. `boolean d = (5 % 0) == 0;`<br>
E. `boolean e = (3 > 2) == (1 > 4);`

### Soru 5

**Odak:** Compound assignment

Aşağıdaki kod neden derlenir ve `7` yazdırır?

```java
short score = 3;
score += 4.6;
System.out.println(score);
```

A. `4.6` önce otomatik olarak `int`e yuvarlanır.<br>
B. Compound assignment, işlemin sonucuna hedef type'a implicit cast uygular.<br>
C. `short` bütün `double` değerlerini kayıpsız saklayabilir.<br>
D. `+=` operator'ı sağ operand'ı yok sayar.

### Soru 6

**Odak:** English → Turkish / YDS

Cümleyi doğal Türkçeye çevir; `because` ve passive voice yapısının görevini
belirt:

> Because the left operand is false, the right operand of `&&` is not evaluated.

<!-- page-break -->

### Soru 7

**Odak:** Gruplama ile operand değerlendirme sırası

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class OrderCheck {
    public static void main(String[] args) {
        int x = 1;
        int result = x++ + (x = 4) * 2;
        System.out.println(x + ":" + result);
    }
}
```

A. `4:9`<br>
B. `5:12`<br>
C. `4:12`<br>
D. Kod derlenmez.

<!-- page-break -->

### Soru 8

**Odak:** Negative division ve remainder

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class RemainderCheck {
    public static void main(String[] args) {
        System.out.println((-7 / 3) + ":" + (-7 % 3));
    }
}
```

A. `-3:2`<br>
B. `-2:1`<br>
C. `-2:-1`<br>
D. `ArithmeticException` oluşur.

<!-- page-break -->

## Cevaplar ve açıklamalar

### 1. B — `4:10`

`x++` ifadeye `2` verir, sonra `x` değeri `3` olur. `2 * 3` sonucu `6`dır.
`++x`, `x`i önce `4` yapıp ifadeye `4` verir; toplam `10` olur. A ve C side
effect sırasını yanlış izler. D yanlıştır; expression type'ı `int`tir.

### 2. B — Does not compile / derlenmez

Binary numeric promotion nedeniyle `value + 1` ifadesinin type'ı `int` olur;
bu sonuç explicit cast olmadan `byte` variable'a atanamaz. A ancak
`value++`, `value += 1` veya uygun cast ile mümkün olur. C bir reference cast
hatasıdır ve burada ilgisizdir. D için önce kodun derlenmesi ve gerçekten
overflow üreten bir değer gerekir.

### 3. C

`false && right` ve `true || right` durumlarında sağ taraf değerlendirilmez.
Boolean `&` ise iki tarafı da değerlendirir. A ve B davranışları yanlış
tanımlar. D yanlıştır; `&` hem integral bitwise hem de boolean logical operator
olarak kullanılabilir.

### 4. A ve B

- **A doğru:** Boolean `|` iki tarafı değerlendirir; sonuç `true`dur.
- **B doğru:** Sol taraf `true` olduğundan `||` sağ tarafı atlar; dolayısıyla
  sıfıra bölme çalıştırılmaz.
- **C yanlış:** `null instanceof String` geçerlidir fakat sonucu `false`tur.
- **D yanlış:** Kod derlenir, ancak expression değerlendirilirken
  `ArithmeticException` oluşur.
- **E yanlış:** `true == false` sonucu `false`tur.

### 5. B

`score += 4.6`, assignment aşamasında yaklaşık olarak
`score = (short) (score + 4.6)` davranışı gösterir. Fractional bölüm explicit
görünmeyen narrowing sırasında kaybolur ve sonuç `7` olur. A, C ve D Java'nın
uyguladığı kural değildir.

### 6. Örnek çeviri

“Sol operand `false` olduğu için `&&` operator'ının sağ operand'ı
değerlendirilmez.”

`because` neden bildirir. `is not evaluated`, `be + V3` biçiminde passive
voice'tur; odağı değerlendirmeyi yapan mekanizmadan sağ operand'a taşır.

### 7. A

Sol operand `x++` önce eski 1 değerini üretir. Sağdaki atama x değerini 4 yapar; çarpım 8, toplam 9 olur. B/C, çarpmanın gruplama önceliğini sol operandı atlama izni sanır; D yanlıştır, bütün türler uygundur.

### 8. C

Tamsayı bölümü sıfıra doğru kesilir: -2. `a = (a / b) * b + a % b` bağıntısıyla kalan -1 olur. A floor division sanır; B kalan işaretini değiştirir; bölen 3 olduğu için D yanlıştır.
