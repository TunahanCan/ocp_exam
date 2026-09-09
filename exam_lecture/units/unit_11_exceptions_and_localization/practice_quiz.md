# Unit 11 · Exceptions and Localization — Practice Quiz

Bu belge sekiz adet **OCP tarzı özgün çalışma sorusu** içerir; sorular gerçek
sınavdan alınmamıştır. Önerilen süre 25–30 dakikadır; istersen 1–4 ve 5–8 olarak iki oturuma böl. Cevaplara geçmeden önce
her kodu **derleme durumu → çalışma zamanı → çıktı** sırasıyla değerlendir.

## Sorular

### Soru 1

**Odak:** Try-with-resources kapanma sırası

Aşağıdaki programın çıktısı nedir?

```java
public class CloseOrder {
    static class Resource implements AutoCloseable {
        private final String name;

        Resource(String name) {
            this.name = name;
        }

        @Override
        public void close() {
            System.out.print(name);
        }
    }

    public static void main(String[] args) {
        try (var first = new Resource("A");
             var second = new Resource("B")) {
            System.out.print("T");
        } finally {
            System.out.print("F");
        }
    }
}
```

A. `TABF`

B. `TBAF`

C. `ABTF`

D. Kod derlenmez.

<!-- page-break -->

### Soru 2

**Odak:** Formatter ile temporal type uyumu

Aşağıdaki program için doğru sonuç hangisidir?

```java
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class FormatTime {
    public static void main(String[] args) {
        var formatter = DateTimeFormatter.ofPattern("MM");
        System.out.print(formatter.format(LocalTime.of(9, 5)));
    }
}
```

A. `09` yazdırır.

B. `05` yazdırır.

C. Kod derlenmez.

D. Kod derlenir; runtime'da `DateTimeException` ailesinden bir exception oluşur.

### Soru 3

**Odak:** Override ve checked exception

`Parent.read()` method'u `throws java.io.IOException` bildiriyor. Aşağıdaki
`Child.read()` declaration'larından hangisi geçerli bir override'dır?

A. `public void read() throws Exception`

B. `protected void read() throws Throwable`

C. `public void read() throws java.io.FileNotFoundException`

D. `private void read()`

`Parent.read()` method'unun access düzeyinin `protected` ve return type'ının
`void` olduğunu varsay.

### Soru 4

**Odak:** Exception ve try-with-resources tuzakları

Aşağıdaki ifadelerden **hangi ikisi doğrudur?**

A. Bir try-with-resources statement'ında daha önce oluşturulmuş bir variable
resource olarak kullanılıyorsa bu variable `final` veya effectively final
olmalıdır.

B. Resource'lar declaration sırasıyla kapatılır.

C. `catch (java.io.IOException | Exception e)` geçerli bir multi-catch'tir.

D. Try body bir exception fırlatırken `close()` da exception fırlatırsa,
`close()` exception'ı genellikle primary exception'a suppressed olarak eklenir.

E. `catch` bloğunda `return` çalışırsa `finally` bloğu atlanır.

### Soru 5

**Odak:** `ResourceBundle` fallback

`Messages.properties`, `Messages_tr.properties` ve
`Messages_tr_TR.properties` dosyaları vardır. `title` key'i
`Messages_tr_TR.properties` içinde yok, fakat `Messages_tr.properties`
içinde vardır. İstenen locale `tr_TR` olduğunda ne olur?

A. En özel bundle bulunduğu için eksik key hemen `MissingResourceException`
üretir.

B. Seçilen hierarchy'nin parent'ı olan `Messages_tr.properties` içindeki değer
kullanılır.

C. Önce JVM'in default locale hierarchy'si aranır.

D. Dil bundle'ından önce her zaman root bundle aranır.

### Soru 6

**Odak:** English → Turkish / YDS

Aşağıdaki cümleyi doğal Türkçeye çevir; `once` ve `even if` yapılarının anlam
ilişkisini belirt:

> A resource is closed automatically once execution leaves the
> try-with-resources statement, even if an exception is thrown.

### Soru 7

**Odak:** Önceden oluşturulmuş `final` field ve kaynak türü

Aşağıdaki tam program için **tek doğru** sonuç hangisidir?

```java
public class FieldResource {
    static class Resource implements AutoCloseable {
        public void close() { System.out.print("C"); }
    }
    private final Resource resource = new Resource();

    void run() {
        try (this.resource) { System.out.print("B"); }
    }
    public static void main(String[] args) {
        new FieldResource().run();
    }
}
```

A. Derlenmez; önceden oluşturulmuş kaynak yalnız yerel değişken olabilir.

B. Derlenmez; `AutoCloseable` kullanan her metot `throws Exception` yazmalıdır.

C. Başarıyla derlenir ve `BC` yazdırır.

D. Başarıyla derlenir ve `CB` yazdırır.

### Soru 8

**Odak:** Gövde başarılı, kapanışlar başarısız

Aşağıdaki programın **tek doğru** çıktısını seç.

```java
public class ClosingFailures {
    record Resource(String name) implements AutoCloseable {
        public void close() { throw new IllegalStateException(name); }
    }
    public static void main(String[] args) {
        try (var a = new Resource("A"); var b = new Resource("B")) {
            System.out.print("T:");
        } catch (IllegalStateException e) {
            System.out.print(e.getMessage() + ":"
                    + e.getSuppressed()[0].getMessage());
        }
    }
}
```

A. `T:A:B`

B. `T:B:A`

C. `T:B:` yazdırdıktan sonra `ArrayIndexOutOfBoundsException` fırlatır.

D. Derlenmez; record bir kaynağı temsil edemez.

**Dil aktarımı:** Seçimini bir İngilizce cümlede `primary`, `suppressed` ve
`because` kullanarak gerekçelendir.

<!-- page-break -->

## Cevaplar ve açıklamalar

### Soru 1 — B

- **A yanlış:** Resource'lar oluşturuldukları sıranın tersinde kapatılır; `A`,
  `B`den önce kapanmaz.
- **B doğru:** Try body `T`, ardından `second` için `B`, `first` için `A` ve en
  son `finally` için `F` yazdırılır: `TBAF`.
- **C yanlış:** Kapanma, try body tamamlandıktan sonra başlar.
- **D yanlış:** Her iki resource `AutoCloseable`dır ve `close()` imzaları
  geçerlidir; kod Java 17'de derlenir.

### Soru 2 — D

- **A yanlış:** `MM`, minute değil month-of-year alanıdır; ayrıca `LocalTime`
  month alanı taşımaz.
- **B yanlış:** Minute pattern'i küçük `mm` olurdu.
- **C yanlış:** Pattern ile temporal object arasındaki field uyumu compile
  time'da denetlenmez.
- **D doğru:** Kod derlenir. Formatting sırasında `LocalTime` üzerinde
  month-of-year alanı bulunamadığı için runtime'da
  `UnsupportedTemporalTypeException` oluşur; bu type `DateTimeException`
  ailesindedir.

### Soru 3 — C

- **A yanlış:** `Exception`, `IOException`dan daha geniş bir checked exception
  type'ıdır.
- **B yanlış:** Hem access `protected` olarak kalsa bile `Throwable` daha geniş
  bir checked type'dır.
- **C doğru:** Access `protected`dan `public`e genişler ve
  `FileNotFoundException`, `IOException`ın subtype'ıdır.
- **D yanlış:** Override eden method inherited `protected` erişimi `private`
  yaparak daraltamaz.

### Soru 4 — A ve D

- **A doğru:** Önceden oluşturulmuş uygun türde bir `final` veya effectively final
  değişken kullanılabilir; `final` alan erişimi de geçerlidir (Soru 7).
- **B yanlış:** Kapanma sırası declaration sırasının tersidir.
- **C yanlış:** Aynı multi-catch içindeki alternatifler parent/child ilişkili
  olamaz; `Exception`, `IOException`ı zaten kapsar.
- **D doğru:** Try body exception'ı primary kalır; kapanış exception'ı
  `getSuppressed()` ile erişilebilen suppressed exception olur.
- **E yanlış:** JVM normal kontrol akışında method'dan çıkmadan önce `finally`
  bloğunu çalıştırır.

### Soru 5 — B

- **A yanlış:** Bundle seçilmesi, yalnız en özel dosyanın key'lerinin
  kullanılacağı anlamına gelmez.
- **B doğru:** `tr_TR` bundle'ında eksik olan key aynı seçilmiş hierarchy
  içindeki `tr` parent bundle'ında aranır.
- **C yanlış:** Uygun requested-locale hierarchy bulunduğunda eksik key için
  rastgele default-locale hierarchy'sine geçilmez.
- **D yanlış:** Candidate order en özel locale'den daha genel parent'a ve
  sonunda root'a doğru ilerler.

### Soru 6 — Örnek çeviri

“Çalışma try-with-resources statement'ından ayrıldığı anda, bir exception
fırlatılsa bile resource otomatik olarak kapatılır.”

`once`, burada “-dığı anda/-dığında” anlamıyla zaman sınırını kurar.
`even if`, exception olasılığının sonucu değiştirmediğini belirten
concession (ödünleme) yapısıdır. `is closed` ve `is thrown` passive voice
yapılarıdır.

### Soru 7 — C

- **C doğru:** Kaynak olarak uygun türde bir `final` alan da kullanılabilir. Gövde `B`, kapanış `C` yazdırır: başarıyla derlenir ve `BC` üretir.
- **A yanlış:** Sözdizimi yalnız yerel değişkenlerle sınırlı değildir; `this.resource` geçerli bir field access'tir.
- **B yanlış:** Buradaki bildirilen tür `Resource` ve `close()` checked exception bildirmiyor. Türü `AutoCloseable` olsaydı `close()` imzasındaki `Exception` hesaba katılırdı.
- **D yanlış:** Kaynak, gövde bittikten sonra kapanır.

Kural: [JLS 17 §14.20.3](https://docs.oracle.com/javase/specs/jls/se17/html/jls-14.html#jls-14.20.3).

### Soru 8 — B

- **B doğru:** Gövde `T:` yazar; önce `b` kapanır ve `B` birincil olur. Ardından `a` kapanır; `A`, `B` üzerinde suppressed olarak saklanır. Sonuç `T:B:A` olur.
- **A yanlış:** Kapanışlar bildirim sırasının tersindedir.
- **C yanlış:** `A` gerçekten suppressed listesine eklenmiştir; `[0]` geçerlidir.
- **D yanlış:** Record, `AutoCloseable` arayüzünü uygulayabilir.

Örnek dil yanıtı: “B is primary because it is the first closing failure; A is suppressed.” → “İlk kapanış hatası B olduğundan B birincildir; A ikincil olarak saklanır.”
