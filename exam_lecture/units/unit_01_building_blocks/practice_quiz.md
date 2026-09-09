# Unit 01 · Building Blocks — Practice Quiz

Bu belge sekiz adet **OCP tarzı özgün çalışma sorusu** içerir. Sorular gerçek
sınavdan alınmamıştır. Önce cevaplara bakmadan bütün soruları çöz; kod
sorularında sırayla **derleme durumu → çalışma zamanı → çıktı** kontrolü yap.

## Çalışma yönergesi
Yanlış yaptığın sorunun kuralını [teknik notta](technical_memory_notes.md) bul;
cevabı kapatıp aynı kodda tek bir değeri değiştirerek sonucu yeniden tahmin et.
Dil sorusunda hem doğal çeviriyi hem bağlacın kurduğu ilişkiyi açıklayabildiysen
başarılı say. [README oturum rotası](README.md) kaynak sorularına dönüşü gösterir.

## Sorular

### Soru 1

**Odak:** Initialization sırası

Aşağıdaki programın çıktısı nedir?

```java
public class Start {
    static { System.out.print("S"); }
    { System.out.print("I"); }
    Start() { System.out.print("C"); }

    public static void main(String[] args) {
        new Start();
    }
}
```

A. `SIC`<br>
B. `ISC`<br>
C. `ICS`<br>
D. Kod derlenmez.

### Soru 2

**Odak:** `var` ve derleme

Aşağıdaki kod için hangisi doğrudur?

```java
public class LocalType {
    public static void main(String[] args) {
        var count;
        count = 3;
        System.out.println(count);
    }
}
```

A. `3` yazdırır.<br>
B. `0` yazdırır.<br>
C. Kod derlenmez.<br>
D. Kod derlenir fakat runtime'da `NullPointerException` oluşur.

### Soru 3

**Odak:** Wildcard import

`import java.util.*;` bildirimi hakkında hangisi doğrudur?

A. `java.util` ve bütün alt package'lerdeki type'ları import eder.<br>
B. Yalnız `java.util` package'indeki erişilebilir type'ları kapsar.<br>
C. `java.util` içindeki type'ların bütün member'larını import eder.<br>
D. Aynı dosyada başka bir import kullanılmasını engeller.

### Soru 4

**Odak:** Literals ve primitive types

Aşağıdaki declaration'lardan **hangi ikisi** bağımsız olarak derlenir?

A. `int octal = 08;`<br>
B. `long large = 2_147_483_648L;`<br>
C. `double amount = 1_000_.0;`<br>
D. `char letter = 65;`<br>
E. `float rate = 2.0;`

### Soru 5

**Odak:** Garbage collection eligibility

Aşağıdaki satırlar aynı method body içindedir ve `second` variable'ı bu
satırlardan sonra yeniden okunacaktır:

```java
var first = new StringBuilder("cat");
var second = first;
first = null;
```

Yukarıdaki son assignment'tan hemen sonra oluşturulan `StringBuilder` için
hangisi doğrudur?

A. Kesin olarak garbage collection yapılmıştır.<br>
B. `first` `null` olduğu için object artık reachable değildir.<br>
C. Object, `second` üzerinden reachable olduğu için henüz GC'ye uygun değildir.<br>
D. `StringBuilder` object'leri garbage collection'a hiçbir zaman uygun olmaz.

### Soru 6

**Odak:** English → Turkish / YDS

Aşağıdaki cümleyi doğal Türkçeye çevir ve `whereas` bağlacının kurduğu anlam
ilişkisini belirt:

> A local variable must be initialized before it is read, whereas an instance
> variable receives a default value.

<!-- page-break -->

### Soru 7

**Odak:** Definite assignment · kesin atanmışlık

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class LocalRead {
    static int field;
    public static void main(String[] args) {
        int local;
        if (args.length > 0) local = 4;
        System.out.println(field + ":" + local);
    }
}
```

A. `0:0` yazdırır.<br>
B. `0:4` yazdırır.<br>
C. Kod derlenmez.<br>
D. `NullPointerException` oluşur.

<!-- page-break -->

### Soru 8

**Odak:** Final reference ve nesne durumu

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
public class FinalReference {
    public static void main(String[] args) {
        final StringBuilder first = new StringBuilder("a");
        var second = first;
        second.append("b");
        System.out.println(first);
    }
}
```

A. `a` yazdırır.<br>
B. `ab` yazdırır.<br>
C. `final` nesne değiştirildiği için derlenmez.<br>
D. İkinci referans oluşturulurken exception oluşur.

<!-- page-break -->

## Cevaplar ve açıklamalar

### 1. A — `SIC`

Class ilk kullanıldığında static initializer bir kez çalışır (`S`). `new`
işleminde instance initializer (`I`), ardından constructor body (`C`) çalışır.
B ve C bu sırayı bozar. D yanlıştır; program Java 17 ile başarıyla derlenir.

### 2. C — Does not compile / derlenmez

`var` kullanan local variable aynı declaration içinde initializer'a sahip
olmalıdır; compiler type'ı sonraki assignment'tan çıkarmaz. Bu nedenle A ve B
bir output varsayamaz. D de yanlıştır; hata runtime'a ulaşmadan compile time'da
oluşur.

### 3. B

Package wildcard yalnız belirtilen package'deki erişilebilir type'ları kapsar.
A yanlıştır; `java.util.concurrent` gibi subpackage'ler ayrıca import edilir.
C, type import ile `static import` kavramlarını karıştırır. D için böyle bir
kısıtlama yoktur.

### 4. B ve D

- **A yanlış:** Baştaki `0` octal literal başlatır; octal sistemde `8` rakamı
  geçersizdir.
- **B doğru:** Değer `int` aralığını aşar, fakat `L` suffix'i literal'ı `long`
  yapar; underscore konumları geçerlidir.
- **C yanlış:** Underscore decimal point'in hemen yanında olamaz.
- **D doğru:** Sabit `65`, `char` aralığındadır ve `A` karakter koduna karşılık
  gelir.
- **E yanlış:** `2.0` bir `double` literal'dır; `float` için `2.0F` veya explicit
  cast gerekir.

### 5. C

`first` ve `second` aynı object'i gösterir. Yalnız `first` reference'ını
`null` yapmak object'e giden bütün yolları kaldırmaz. A, GC'nin zamanını da
yanlış biçimde garanti eder. B kalan reference'ı yok sayar. D yanlıştır; bütün
normal object'ler unreachable olduklarında GC'ye uygun olabilir.

### 6. Örnek çeviri

“Bir local variable okunmadan önce initialize edilmelidir; buna karşılık bir
instance variable varsayılan bir değer alır.”

`whereas`, iki variable türünün initialization davranışını
**karşılaştırıp karşıtlaştırır**. “Oysa” çevirisi mümkün olsa da bu teknik bağlamda “buna
karşılık” daha doğaldır. `must be initialized` ise zorunluluk bildiren passive
voice yapısıdır.

### 7. C

`local`, args boşken değer almamış olabilir; derleyici bütün geçerli yollar için atamayı kanıtlayamaz. `field` varsayılan 0 alır, fakat bu kural yerel değişkene taşınmaz; A/B çıktı varsayımı yapar, D runtime bekler.

### 8. B

`final` değişkenin başka nesneye atanmasını engeller; builder içeriğini dondurmaz. İki referans aynı nesneyi gösterdiği için `ab` yazdırılır; A mutation etkisini atlar, C/D referans ve nesneyi karıştırır.
