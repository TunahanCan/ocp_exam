# Unit 06 · Class Design — Practice Quiz

Bu belge Java 17/OCP odağında hazırlanmış **özgün çalışma soruları** içerir;
gerçek sınav sorusu değildir. Önerilen süre 15–20 dakikadır. Önce altı sorunun
tamamını kaynaklara bakmadan çöz, ardından cevap açıklamalarına geç.

## Sorular

### Soru 1

Aşağıdaki kodun çıktısı nedir?

```java
public class InitQuiz {
    static class Parent {
        static { System.out.print("A"); }
        { System.out.print("B"); }
        Parent() { System.out.print("C"); }
    }

    static class Child extends Parent {
        static { System.out.print("D"); }
        { System.out.print("E"); }
        Child() { System.out.print("F"); }
    }

    public static void main(String[] args) {
        new Child();
    }
}
```

A. `ADBCEF`<br>
B. `ABCDEF`<br>
C. `DABCEF`<br>
D. Kod derlenmez.

<!-- page-break -->

### Soru 2

Aşağıdaki program için doğru sonuç hangisidir?

```java
import java.io.FileNotFoundException;
import java.io.IOException;

public class OverrideQuiz {
    static class Base {
        protected Number value() throws IOException {
            return 1;
        }
    }

    static class Sub extends Base {
        @Override
        public Integer value() throws FileNotFoundException {
            return 2;
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.print(new Sub().value());
    }
}
```

A. Covariant return type nedeniyle kod derlenmez.<br>
B. Checked exception değiştiği için kod derlenmez.<br>
C. Kod derlenir ve `2` yazdırır.<br>
D. Kod derlenir fakat `ClassCastException` fırlatır.

### Soru 3

Java 17 class-design kuralları hakkında doğru olan **iki seçeneği** seçin.

A. Bir subclass constructor'ında açık bir `this()` veya `super()` çağrısı
yoksa compiler ilk satıra `super()` ekler.<br>
B. Her abstract class en az bir abstract method bildirmek zorundadır.<br>
C. `final` bir instance method override edilemez fakat overload edilebilir.<br>
D. Aynı signature'a sahip static method'lar runtime object'e göre dinamik
dispatch edilir.<br>
E. Constructor'lar normal instance method'lar gibi inherited olur.

### Soru 4

`Cat`, `Animal`ı extends ediyor; `name` field'ını ve static `kind()` method'unu
hide ediyor, `sound()` instance method'unu override ediyor. Aşağıdaki reference
için hangi seçim yapılır?

```java
Animal animal = new Cat();
```

A. Field, static method ve instance method için yalnız `Animal` seçilir.<br>
B. Field ve static method için `Animal`; instance method için `Cat` seçilir.<br>
C. Field için `Cat`; static ve instance method için `Animal` seçilir.<br>
D. Üç member için de runtime object olan `Cat` seçilir.

### Soru 5

Bir class, yalnızca `String` elementleri içeren bir listeyi immutable state
olarak saklamak istiyor. Aşağıdaki yaklaşımlardan hangisi bu hedefe uygundur?

A. Constructor'da verilen mutable listeyi doğrudan field'a atamak ve aynı
listeyi accessor'dan döndürmek.<br>
B. Field'ı `final` yapmak, fakat listeyi doğrudan accessor'dan döndürmek.<br>
C. Constructor'da `List.copyOf(input)` kullanmak ve oluşan listeyi
accessor'dan döndürmek.<br>
D. Yalnız class'ı `final` ilan etmek.

### Soru 6

Şu teknik cümlenin doğal Türkçe çevirisi ve ana çıkarımı hangisidir?

> A subclass constructor must invoke another constructor, either explicitly or
> implicitly, before it can initialize its own instance fields.

A. “Bir subclass constructor'ı, kendi instance field'larını başlatmadan önce
açıkça ya da örtük biçimde başka bir constructor çağırmalıdır.” Bu, constructor
zincirinin önce parent tarafını hazırlamasını açıklar.<br>
B. “Bir subclass kendi static field'larını ancak bütün instance field'lardan
sonra başlatır.” Cümle static initialization sırasını açıklar.<br>
C. “Her subclass constructor'ı açıkça `this()` yazmalıdır.” `super()` kullanımı
yasaktır.<br>
D. “Bir subclass constructor'ı başka bir constructor'ı isterse çağırabilir.”
Çağrı tamamen optional'dır.

<!-- page-break -->

## Cevaplar ve açıklamalar

### Soru 1 — A

- **A doğru:** Önce superclass static block'u `A`, sonra subclass static
  block'u `D` çalışır. Object oluşturulurken parent instance block/constructor
  `BC`, ardından child instance block/constructor `EF` gelir.
- **B yanlış:** Parent ve child static/instance adımları sırayla
  karıştırılmıştır.
- **C yanlış:** Subclass initialize edilmeden önce superclass initialize
  edilir; `D`, `A`dan önce gelemez.
- **D yanlış:** Declaration'ların tamamı Java 17'de geçerlidir.

### Soru 2 — C

- **A yanlış:** `Integer`, `Number`ın subtype'ıdır; bu geçerli bir covariant
  return type'tır.
- **B yanlış:** Override eden method daha dar bir checked exception olan
  `FileNotFoundException` bildirebilir.
- **C doğru:** Access `protected`dan `public`e genişler, return type covariant,
  checked exception daha dardır. Runtime'da `Sub.value()` seçilir ve `2`
  yazdırılır.
- **D yanlış:** Kodda başarısız bir cast yoktur.

### Soru 3 — A ve C

- **A doğru:** Explicit constructor invocation yoksa compiler `super()` ekler;
  uygun erişilebilir no-arg parent constructor yoksa bunun sonucu compilation
  error olur.
- **B yanlış:** Abstract class hiç abstract method içermeyebilir.
- **C doğru:** `final` yalnız override'ı engeller; farklı parameter list ile
  overload mümkündür.
- **D yanlış:** Static method'lar override edilmez, hide edilir ve reference
  type'a göre seçilir.
- **E yanlış:** Constructor'lar inherited olmaz; her class kendi
  constructor'ını bildirir veya default constructor alır.

### Soru 4 — B

- **A yanlış:** Overridden instance method runtime object'e göre seçilir.
- **B doğru:** Field ve hidden static method seçimi reference type olan
  `Animal`a; overridden `sound()` seçimi object type olan `Cat`e bağlıdır.
- **C yanlış:** Field erişiminde runtime object belirleyici değildir.
- **D yanlış:** Field ve static method için polymorphic dispatch uygulanmaz.

### Soru 5 — C

- **A yanlış:** Caller aynı listeyi değiştirerek object state'ini değiştirebilir.
- **B yanlış:** `final`, field reference'ının yeniden atanmasını engeller;
  referenced list'in mutation'ını engellemez.
- **C doğru:** `List.copyOf()` input'tan bağımsız, unmodifiable bir snapshot
  oluşturur. Elementler `String` olduğu için element mutability riski de yoktur.
- **D yanlış:** `final class` subclass oluşturulmasını önler, mutable field'ları
  tek başına korumaz.

### Soru 6 — A

- **A doğru:** `either ... or ...`, “ya ... ya da ...” seçeneğini; `before`,
  constructor zincirindeki önceliği kurar. Buradaki `implicitly`, compiler'ın
  eklediği çağrıyı da kapsar.
- **B yanlış:** Kaynak cümle static field'lardan söz etmez.
- **C yanlış:** Çağrı `this()` veya `super()` olabilir ve explicit olmak
  zorunda değildir.
- **D yanlış:** Her constructor zinciri en sonunda superclass constructor'ına
  ulaşır; çağrı optional değildir.
