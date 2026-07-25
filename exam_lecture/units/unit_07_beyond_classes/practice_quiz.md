# Unit 07 · Beyond Classes — Practice Quiz

Bu belge Java 17/OCP odağında hazırlanmış **özgün çalışma soruları** içerir;
gerçek sınav sorusu değildir. Önerilen süre 15–20 dakikadır. Önce altı soruyu
cevap anahtarına bakmadan çöz.

## Sorular

### Soru 1

Aşağıdaki kodun çıktısı nedir?

```java
public class DefaultQuiz {
    interface A {
        default String id() { return "A"; }
    }

    interface B {
        default String id() { return "B"; }
    }

    static class C implements A, B {
        @Override
        public String id() {
            return A.super.id() + B.super.id();
        }
    }

    public static void main(String[] args) {
        System.out.print(new C().id());
    }
}
```

A. `A`<br>
B. `B`<br>
C. `AB`<br>
D. Kod, duplicate default method nedeniyle derlenmez.

### Soru 2

Aşağıdaki Java 17 programı için doğru sonuç hangisidir?

```java
sealed interface Shape permits Circle, Polygon {}
final class Circle implements Shape {}
non-sealed class Polygon implements Shape {}
class Triangle extends Polygon {}

public class SealedQuiz {
    public static void main(String[] args) {
        System.out.print(new Triangle() instanceof Shape);
    }
}
```

A. Kod derlenir ve `true` yazdırır.<br>
B. `Triangle`, `Shape` permits listesinde olmadığı için kod derlenmez.<br>
C. `Polygon`, `final` olmadığı için kod derlenmez.<br>
D. Kod derlenir ve `false` yazdırır.

<!-- page-break -->

### Soru 3

Java 17 record'ları hakkında doğru olan **iki seçeneği** seçin.

A. Bir record declaration örtük olarak `final`dır.<br>
B. Her record component için `private final` field vardır; component adıyla
eşleşen `public` accessor açıkça bildirilmemişse compiler bunu üretir.<br>
C. Compact constructor'ın ilk ifadesi açıkça `this(...)` olmalıdır.<br>
D. Component `name` ise generated accessor'ın adı `getName()` olur.<br>
E. Record, generated `java.lang.Record` yerine başka bir class'ı extends
edebilir.

### Soru 4

Enum API ve declaration kuralları için doğru ifade hangisidir?

A. `valueOf()` constant adını büyük/küçük harf duyarsız arar.<br>
B. `values()` constant'ları declaration sırasıyla içeren bir array döndürür.<br>
C. Enum constructor'ı `public` ilan edilebilir.<br>
D. Bir enum, seçilen herhangi bir concrete class'ı extends edebilir.

### Soru 5

`Inner`, non-static member inner class olduğuna göre static bir method içinden
geçerli oluşturma ifadesi hangisidir?

```java
class Outer {
    class Inner {}
}
```

A. `Outer.Inner x = new Outer.Inner();`<br>
B. `Outer.Inner x = new Outer().new Inner();`<br>
C. `Inner x = new Inner();`<br>
D. `Outer.Inner x = Outer.new Inner();`

### Soru 6

Şu cümlenin en doğal teknik çevirisi ve doğru çıkarımı hangisidir?

> A sealed type restricts its direct subtypes to a known set, although a
> non-sealed subtype can reopen its own branch of the hierarchy.

A. “Sealed bir type doğrudan subtype'larını bilinen bir kümeyle sınırlar;
ancak non-sealed bir subtype hiyerarşinin kendi dalını yeniden açabilir.”
Kısıtlama yalnız doğrudan subtype listesiyle bitmeyebilir.<br>
B. “Sealed bir type bütün alt nesnelerin oluşturulmasını yasaklar.”
`non-sealed` yalnız constructor erişimini değiştirir.<br>
C. “Non-sealed bir subtype, parent'ın permits listesinde bulunamaz.” Bu yüzden
dal hiçbir zaman açılamaz.<br>
D. “Sealed type yalnız interface olabilir.” Cümle class'ları kapsam dışı
bırakır.

<!-- page-break -->

## Cevaplar ve açıklamalar

### Soru 1 — C

- **A yanlış:** `C.id()` iki parent default implementation'ını da açıkça
  çağırır.
- **B yanlış:** `B.super.id()` tek başına dönülmez.
- **C doğru:** `C`, default-method conflict'i override ederek çözer ve sırasıyla
  `A`, `B` döndürür.
- **D yanlış:** Conflict çözülmeseydi kod derlenmezdi; explicit override bunu
  geçerli hâle getirir.

### Soru 2 — A

- **A doğru:** `Polygon`, permitted direct subtype'tır ve `non-sealed` olduğu
  için kendi alt dalını tekrar açar. `Triangle` dolaylı olarak `Shape`tir.
- **B yanlış:** `permits`, yalnız direct subtype'ları listeler; `Triangle`
  doğrudan `Polygon`ı extends eder.
- **C yanlış:** Permitted subtype `final`, `sealed` veya `non-sealed` olmalıdır;
  burada `non-sealed` geçerlidir.
- **D yanlış:** `instanceof Shape`, dolaylı subtype olan `Triangle` object'i
  için `true`dur.

### Soru 3 — A ve B

- **A doğru:** Record subclass edilemez; declaration örtük olarak `final`dır.
- **B doğru:** Her component `private final` field'a sahiptir. Aynı adlı
  `public` accessor explicit yazılabilir; yazılmazsa compiler üretir.
  JavaBean tarzı `get...` adı kullanılmaz.
- **C yanlış:** Compact constructor explicit constructor invocation yazmaz;
  component field atamaları compiler tarafından tamamlanır.
- **D yanlış:** Accessor `name()` olur.
- **E yanlış:** Her record örtük olarak `java.lang.Record`u extends eder ve
  başka class extends edemez.

### Soru 4 — B

- **A yanlış:** `valueOf()` exact, case-sensitive constant adı bekler; eşleşme
  yoksa `IllegalArgumentException` fırlatır.
- **B doğru:** `values()` declaration sırasını koruyan yeni bir array döndürür.
- **C yanlış:** Enum constructor'ı `private` erişim mantığıyla sınırlıdır;
  `public` veya `protected` olamaz.
- **D yanlış:** Enum zaten `java.lang.Enum` hiyerarşisine bağlıdır ve başka
  class extends edemez.

### Soru 5 — B

- **A yanlış:** Non-static inner class oluşturmak için enclosing `Outer`
  instance gerekir.
- **B doğru:** `new Outer()` enclosing instance'ı, `.new Inner()` inner
  instance'ı oluşturur.
- **C yanlış:** Static context'te örtük bir `Outer.this` yoktur.
- **D yanlış:** `Outer` bir class adıdır; inner object creation için object
  instance kullanılmalıdır.

### Soru 6 — A

- **A doğru:** `although` karşıtlık kurar; “buna rağmen/ancak” anlamıyla
  `non-sealed` dalın yeniden açılabildiğini gösterir.
- **B yanlış:** Sealing object creation'ı değil, direct subtype kümesini
  denetler.
- **C yanlış:** `non-sealed` class/interface önce permitted direct subtype
  olmalı, ardından kendi dalını açabilir.
- **D yanlış:** Hem class hem interface `sealed` olabilir.
