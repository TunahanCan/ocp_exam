# Unit 04 · Core APIs — Practice Quiz

Bu belge sekiz adet **OCP tarzı özgün çalışma sorusu** içerir. Sorular gerçek
sınavdan alınmamıştır. API sorularında receiver'ın değişip değişmediğini,
return type'ı ve index sınırlarını ayrı ayrı kontrol et.

## Sorular

### Soru 1

**Odak:** String immutability

Aşağıdaki programın çıktısı nedir?

```java
public class TextValue {
    public static void main(String[] args) {
        String text = " java ";
        text.strip();
        text = text.toUpperCase();
        System.out.println("[" + text + "]");
    }
}
```

A. `[JAVA]`<br>
B. `[ JAVA ]`<br>
C. `[java]`<br>
D. Kod derlenmez.

### Soru 2

**Odak:** Index sınırı

Aşağıdaki kod için hangisi doğrudur?

```java
public class BuilderRange {
    public static void main(String[] args) {
        var builder = new StringBuilder("abc");
        System.out.println(builder.substring(1, 4));
    }
}
```

A. `bc` yazdırır.<br>
B. `bc` ve ardından boşluk yazdırır.<br>
C. Kod derlenmez.<br>
D. Kod derlenir fakat runtime'da `StringIndexOutOfBoundsException` oluşur.

### Soru 3

**Odak:** `==` ve `equals()`

Reference type'larda `==` ile `equals()` hakkında hangisi doğrudur?

A. `==` her zaman object içeriklerini karşılaştırır.<br>
B. `equals()` bütün class'larda otomatik olarak alan alan karşılaştırma yapar.<br>
C. `==` reference identity'yi karşılaştırır; `equals()` sonucu class'ın
   implementation'ına bağlıdır.<br>
D. `String` için `==` ve `equals()` her zaman aynı sonucu verir.

<!-- page-break -->

### Soru 4

**Odak:** String equality

Aşağıdaki ifadelerden **hangi ikisi** `true` üretir?

A. `"java" == "ja" + "va"`<br>
B. `new String("java") == "java"`<br>
C. `new StringBuilder("x").equals(new StringBuilder("x"))`<br>
D. `"java".equals(new String("java"))`<br>
E. `new String("x") == new String("x")`

### Soru 5

**Odak:** Date/Time immutability

```java
var date = java.time.LocalDate.of(2026, 7, 25);
date.plusDays(1);
System.out.println(date);
```

Bu kod neden `2026-07-25` yazdırır?

A. `plusDays()` yalnız leap year içinde çalışır.<br>
B. `LocalDate` immutable'dır; dönen yeni değer `date` variable'ına atanmamıştır.<br>
C. `plusDays()` günü değiştirmek yerine saati değiştirir.<br>
D. `LocalDate` bütün mutation işlemlerini program kapanana kadar erteler.

### Soru 6

**Odak:** English → Turkish / YDS

Cümleyi doğal Türkçeye çevir ve `only when` yapısının koyduğu koşulu belirt:

> `Arrays.binarySearch()` produces a predictable result only when the array is
> sorted according to the ordering used by that overload: natural order or its
> supplied `Comparator`.

<!-- page-break -->

### Soru 7

**Odak:** Binary search sonucu ve ilk farklı indeks

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
import java.util.Arrays;

public class ArrayResults {
    public static void main(String[] args) {
        int[] first = {2, 4, 7};
        int[] second = {2, 6, 7};
        System.out.println(Arrays.binarySearch(first, 5) + ":"
                + Arrays.mismatch(first, second));
    }
}
```

A. `-2:1`<br>
B. `-3:1`<br>
C. `-3:2`<br>
D. Aranan değer bulunmadığı için exception oluşur.

<!-- page-break -->

### Soru 8

**Odak:** Doğru metot, desteklenmeyen zaman birimi

Aşağıdaki program için hangisi doğrudur? **Bir seçenek seç.**

```java
import java.time.Duration;
import java.time.LocalDate;

public class DateAmount {
    public static void main(String[] args) {
        var date = LocalDate.of(2024, 3, 1);
        System.out.println(date.plus(Duration.ofHours(24)));
    }
}
```

A. `2024-03-02`<br>
B. `2024-03-01`<br>
C. Kod derlenmez.<br>
D. Kod derlenir; `UnsupportedTemporalTypeException` oluşur.

<!-- page-break -->

## Cevaplar ve açıklamalar

### 1. B — `[ JAVA ]`

`String` immutable'dır. `strip()` yeni bir String döndürür; return value
atanmadığı için `text` hâlâ iki yanındaki boşlukları taşır. `toUpperCase()`
sonucu atandığından yalnız harfler büyür. A, atanmayan `strip()` sonucunu
kullanmış gibi davranır. C case dönüşümünü yok sayar. D yanlıştır; kod
başarıyla derlenir.

### 2. D — Runtime exception

`substring(begin, end)` için `end` en fazla length olabilir. Length `3`
olduğundan `end = 4` geçersizdir. Method invocation compile time'da geçerlidir,
bu nedenle C yanlıştır; A ve B ise runtime sınır kontrolünü yok sayar.

### 3. C

`==`, iki reference'ın aynı object'i gösterip göstermediğini sınar.
`equals()` override edilmediyse `Object.equals()` yine identity davranışı
gösterir; override edilmişse içerik karşılaştırabilir. Bu nedenle A ve B
genelleme hatasıdır. D, string pool nedeniyle bazı örneklerde tesadüfen doğru
görünebilir ama genel bir kural değildir.

### 4. A ve D

- **A doğru:** Yalnız constant expression'lardan oluşan concatenation compile
  time'da `"java"` literal'ına dönüşür ve pooled reference kullanılır.
- **B yanlış:** `new` ayrı bir object oluşturur; identity aynı değildir.
- **C yanlış:** `StringBuilder`, content-based `equals()` override etmez.
- **D doğru:** `String.equals()` karakter içeriğini karşılaştırır.
- **E yanlış:** İki ayrı `new` işlemi iki ayrı object üretir.

### 5. B

`LocalDate` immutable'dır; `plusDays(1)` receiver'ı değiştirmez, yeni bir
`LocalDate` döndürür. Değişiklik için `date = date.plusDays(1);` gerekir. A, C
ve D API davranışını tanımlamaz.

### 6. Örnek çeviri

“`Arrays.binarySearch()`, yalnızca array ilgili overload'un kullandığı düzene
—natural order veya verilen `Comparator`— göre sıralanmışsa öngörülebilir bir
sonuç üretir.”

`only when`, **gerekli koşulu** sınırlar: arama ile sıralama aynı ordering
kuralını kullanmalıdır. Burada kullanılan overload'a göre bu kural natural
order ya da supplied `Comparator` olabilir. Array sıralı değilse method çağrısı
yine derlenebilir; ancak sonucun anlamlı veya öngörülebilir olduğu
varsayılamaz.

### 7. B

5 için ekleme indeksi 2, binarySearch sonucu -2-1 = -3 olur. İlk farklı eleman indeksi 1’dir; A negatif sonuç formülünü, C sıfırdan başlayan indekslemeyi kaçırır. Bulunamama exception değildir.

### 8. D

`plus(TemporalAmount)` çağrısı tür bakımından geçerlidir, ancak Duration saniye tabanlıdır ve LocalDate saniye birimini desteklemez. A bunu `Period.ofDays(1)` sanır; B, runtime hatasını yalnız atanmayan dönüş değeriyle açıklamaya çalışır; C derleme ile çalışma zamanı kontrolünü karıştırır.

## Sonraki çalışma adımı

Yanlış yaptığın sorunun kuralını [teknik notta](technical_memory_notes.md) bul;
cevabı kapatıp aynı kodda tek bir değeri değiştirerek sonucu yeniden tahmin et.
Dil sorusunda hem doğal çeviriyi hem bağlacın kurduğu ilişkiyi açıklayabildiysen
başarılı say. [README oturum rotası](README.md) kaynak sorularına dönüşü gösterir.
