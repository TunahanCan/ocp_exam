# Unit 05 · Methods — Practice Quiz

Bu belge sekiz adet **OCP tarzı özgün çalışma sorusu** içerir. Sorular gerçek
sınavdan alınmamıştır. Method sorularında üç aşamayı ayır: declaration'ın
geçerliliği, overload seçimi ve seçilen method'un runtime davranışı.

## Sorular

### Soru 1

**Odak:** Overload resolution

Aşağıdaki programın çıktısı nedir?

```java
public class Picker {
    static void pick(long value) {
        System.out.print("L");
    }

    static void pick(Integer value) {
        System.out.print("I");
    }

    public static void main(String[] args) {
        pick(5);
    }
}
```

A. `L`<br>
B. `I`<br>
C. Kod ambiguous olduğu için derlenmez.<br>
D. Runtime'da `NullPointerException` oluşur.

### Soru 2

**Odak:** Varargs declaration

Aşağıdaki declaration için hangisi doğrudur?

```java
static void label(int... numbers, String name) {
}
```

A. Geçerlidir; varargs herhangi bir konumda olabilir.<br>
B. Kod derlenmez; varargs parameter son sırada olmalıdır.<br>
C. Kod derlenir fakat method yalnız boş array ile çağrılabilir.<br>
D. Kod ancak method `public` yapılırsa derlenir.

<!-- page-break -->

### Soru 3

**Odak:** Pass-by-value

Aşağıdaki programın çıktısı nedir?

```java
public class References {
    static void update(StringBuilder value) {
        value.append("x");
        value = new StringBuilder("y");
    }

    public static void main(String[] args) {
        var text = new StringBuilder("a");
        update(text);
        System.out.println(text);
    }
}
```

A. `a`<br>
B. `ax`<br>
C. `y`<br>
D. Kod derlenmez.

### Soru 4

**Odak:** Geçerli overload'lar

Aynı class içinde bildirildikleri varsayıldığında aşağıdaki method çiftlerinden
**hangi ikisi** geçerli birer overload oluşturur?

A. `void run(int value)` ve `int run(int value)`<br>
B. `void run(int value)` ve `void run(long value)`<br>
C. `void run(int... values)` ve `void run(int[] values)`<br>
D. `void run(String value)` ve `void run(Object value)`<br>
E. `void run(int first)` ve `void run(int second)`

<!-- page-break -->

### Soru 5

**Odak:** Cross-package `protected`

Farklı bir package'deki subclass, parent class'tan miras aldığı `protected`
instance member'a hangi durumda erişebilir?

A. Herhangi bir parent object reference'ı üzerinden her zaman<br>
B. Yalnız member aynı zamanda `static` ise<br>
C. Inheritance yoluyla, `this`/`super` veya erişimi yapan subclass type'ıyla
   uyumlu bir receiver üzerinden<br>
D. `protected`, package dışından hiçbir koşulda erişilemez.

### Soru 6

**Odak:** English → Turkish / YDS

Cümleyi doğal Türkçeye çevir ve `when` clause'unun overload kuralına eklediği
koşulu belirt:

> The compiler prefers primitive widening to boxing when both conversions
> could make an overload applicable.

> **Çalışma alanı:** PDF üzerinde çözüyorsan kalan boşluğu kendi çevirin,
> `when` koşulu ve overload tercih sırasını yazmak için kullan.

<!-- page-break -->

### Soru 7

**Odak:** Varargs için açık null

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class NullVarargs {
    static int count(int... values) {
        return values.length;
    }
    public static void main(String[] args) {
        System.out.println(count(null));
    }
}
```

A. `0`<br>
B. `1`<br>
C. Kod derlenmez.<br>
D. Kod derlenir; `NullPointerException` oluşur.

<!-- page-break -->

### Soru 8

**Odak:** Varargs metodunun array olarak uygulanması

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class NullOverload {
    static void pick(Object value) { System.out.print("O"); }
    static void pick(int... values) { System.out.print("A"); }
    public static void main(String[] args) {
        pick(null);
    }
}
```

A. `O`<br>
B. `A`<br>
C. Belirsiz çağrı nedeniyle derlenmez.<br>
D. Null array yüzünden exception oluşur.

<!-- page-break -->

## Cevaplar ve açıklamalar

### 1. A — `L`

Argument bir `int` literal'dır. Overload resolution, primitive widening'i
boxing'den önceki phase'de dener; bu nedenle `int → long` seçilir. B boxing
seçeneğini gereksiz yere öne alır. C yanlıştır; phase sırası ambiguity'yi
önler. D için `null` değer veya unboxing yoktur.

### 2. B — Does not compile / derlenmez

Bir method en fazla bir varargs parameter alabilir ve bu parameter listede son
sırada olmalıdır. A doğrudan bu kuralı ihlal eder. Declaration geçersiz olduğu
için C'deki runtime/çağrı varsayımına ulaşılamaz. Access modifier değiştirmek
parameter sırasını düzeltmez; D yanlıştır.

### 3. B — `ax`

Java reference'ı da pass-by-value geçirir: parameter, caller'daki reference
value'nun kopyasını alır. `append("x")` ortak object'i mutate eder. Parameter'a
yeni object atamak yalnız yerel kopyayı değiştirir; caller'daki `text` hâlâ
`ax` object'ini gösterir. A mutation'ı, C reassignment'ın yerel olduğunu yok
sayar. D yanlıştır; kod derlenir.

### 4. B ve D

- **A yanlış:** Return type method signature'ın parçası değildir.
- **B doğru:** Parameter type'ları `int` ve `long` olarak farklıdır.
- **C yanlış:** Varargs declaration compile time signature açısından array
  parameter ile aynıdır; ikisi birlikte bildirilemez.
- **D doğru:** `String` ve `Object` farklı parameter type'larıdır.
- **E yanlış:** Parameter name signature'a dahil değildir.

### 5. C

Cross-package subclass erişimi inheritance üzerinden yapılır ve receiver,
erişimi yapan subclass'ın type'ı veya onun subtype'ıyla uyumlu olmalıdır. A,
rastgele bir parent instance üzerinden erişime yanlışlıkla izin verir. B,
instance member sorusuna ilgisiz bir şart ekler. D, `protected` erişimin
subclass yönünü yok sayar.

### 6. Örnek çeviri

“Her iki dönüşüm de bir overload'ı uygulanabilir hâle getirebildiğinde compiler,
boxing yerine primitive widening'i tercih eder.”

`when`, iki conversion'ın da aday üretebildiği koşulu kurar. Cümlenin ana
kuralı, bu koşul altında widening phase'inin boxing phase'inden önce
değerlendirilmesidir.

### 7. D

`null`, int[] reference olarak kabul edilir; sıfır elemanlı array oluşturmaz. Gövdede `values.length` null üzerinde çalıştığı için NPE oluşur; A boş çağrının, B tek elemanlı çağrının davranışıdır.

### 8. B

Varargs bildirimi ilk aşamada int[] parametreli metot olarak da değerlendirilir. `null` her iki reference type'a da uyarken `int[]`, `Object`ten daha özeldir; varargs bildirimi seçilir ve `A` yazdırılır (doğru seçenek B). Gövde array nesnesini okumadığı için D yoktur; C, unrelated reference overload durumundaki ambiguity ile karıştırır.

## Sonraki çalışma adımı

Yanlış yaptığın sorunun kuralını [teknik notta](technical_memory_notes.md) bul;
cevabı kapatıp aynı kodda tek bir değeri değiştirerek sonucu yeniden tahmin et.
Dil sorusunda hem doğal çeviriyi hem bağlacın kurduğu ilişkiyi açıklayabildiysen
başarılı say. [README oturum rotası](README.md) kaynak sorularına dönüşü gösterir.
