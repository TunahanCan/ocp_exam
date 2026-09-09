# Unit 05 · Technical Memory Notes · Methods

Bu dosya eksiksiz [çift dilli ana nottaki](bilingual_notes.md) kuralları bir method
tasarım ve çağrı algoritmasıyla tamamlar. Bir method sorusunda üç ayrı zamanı
karıştırma: **declaration kontrolü → overload seçimi → runtime execution**.
Dil çalışması: [vocabulary](vocabulary.md).

## Kapsam denetimi

Ana çift dilli kaynak access, static context, effectively final, varargs,
pass-by-value ve overload kurallarını tam kapsar. Bu hafıza notu şu bağları
birlikte tekrar ettirir:

- method declaration parçaları ve signature tanımı,
- `protected` erişimin cross-package receiver kısıtı,
- overload applicability phase'leri,
- varargs'ın compile time'da array'e dönüşmesi,
- autoboxing/unboxing ile `null` runtime riski.

## 1. Method declaration anatomisi

```java
public static final int count(String name, int... values)
        throws IllegalArgumentException {
    return values.length;
}
```

Declaration iskeleti: access modifier → optional specifiers → return type →
method name → parameter list → optional `throws` list → body veya semicolon.

**Method signature yalnız method name + parameter type/order bilgisidir.** Return
type, access modifier, parameter names ve `throws` list signature'a dahil değildir.

Bu yüzden yalnız return type'ı değiştirerek overload yapılamaz.

## 2. Local ve field modifiers

- Local variable access modifier veya `static` alamaz.
- Local variable `final` olabilir; `final var x = 3;` geçerlidir.
- Instance/static fields access modifier, `final`, `volatile`, `transient` gibi
  uygun modifier'lar alabilir.
- Blank `final` field constructor'da; blank `static final` field static
  initializer'da exactly once atanabilir.

`effectively final`, explicit `final` yazılmasa da initialization sonrasında
reassign edilmeyen local/parameter demektir. Lambda/local class capture için
gerekir.

## 3. Access matrix

| Member access | Same class | Same package | Different package subclass | Other package non-subclass |
|---|---:|---:|---:|---:|
| `private` | Evet | Hayır | Hayır | Hayır |
| package | Evet | Evet | Hayır | Hayır |
| `protected` | Evet | Evet | Evet* | Hayır |
| `public` | Evet | Evet | Evet | Evet |

`protected` yıldızı önemlidir: different package subclass, inherited member'a
subclass context'i üzerinden erişir. Arbitrary parent reference üzerinden erişim
verilmez.

```java
package child;
class Cub extends parent.Lion {
    void test(Cub cub, parent.Lion lion) {
        cub.age = 2;   // age protected ise geçerli
        // lion.age = 3; // different package'ta geçersiz
    }
}
```

**Hafıza cümlesi:** Protected dış package'ta “subclass ol” demekle kalmaz;
“subclass gözüyle bak” da der.

## 4. Static versus instance membership

- Instance method hem instance hem static member'a direct erişebilir.
- Static method direct olarak yalnız static member'a erişir.
- Static member class'a aittir; tüm instances tarafından paylaşılır.
- Static method'u instance expression üzerinden çağırmak derlenebilir, fakat
  method runtime object'e göre dispatch edilmez.

```java
class Counter {
    static int total;
    int own;

    static void reset() {
        total = 0;
        // own = 0; // Does not compile: receiver yok
    }
}
```

Static initializer class initialization sırasında source order ile bir kez
çalışır ve `this` kullanamaz.

## 5. Varargs: çağrıda esnek, içeride array

```java
static int sum(String label, int... values) {
    return values.length;
}
```

- Bir method en fazla bir varargs parameter taşır.
- Varargs parameter son sırada olmalıdır.
- Method body içinde normal array gibi davranır.
- Caller sıfır, bir veya çok argument ya da doğrudan array verebilir.

```java
sum("a");
sum("b", 1, 2);
sum("c", new int[] {1, 2});
```

Explicit `null` varargs array olarak geçirilebilir; body `values.length`
çağırırsa `NullPointerException` oluşabilir.

## 6. Pass-by-value: kopyalanan şey variable value'sudur

Primitive için value'nun, reference için object address/reference value'nun
kopyası gider.

```java
static void change(StringBuilder b) {
    b.append("!");                  // ortak object mutate edilir
    b = new StringBuilder("new");   // yalnız local parameter reassign edilir
}

var x = new StringBuilder("old");
change(x);
System.out.println(x); // old!
```

**Hafıza cümlesi:** Java object'i değil, oku kopyalar; iki ok aynı object'i
gösterebilir.

## 7. Overload resolution

Overload'lar same name, different parameter list taşır. Compiler call için
applicable candidates'ı phase'ler hâlinde arar; daha erken phase'de uygun method
bulursa sonraki phase'e geçmez.

Pratik sınav sırası:

1. exact/more specific match,
2. primitive widening veya reference widening,
3. boxing/unboxing içeren loose invocation,
4. varargs.

```java
static void call(long x)    { System.out.print("long"); }
static void call(Integer x) { System.out.print("Integer"); }
static void call(int... x)  { System.out.print("varargs"); }

call(3); // long: primitive widening, boxing'den önce
```

Önemli dönüşüm sınırları:

- Primitive widening sonra boxing yapılmaz: `int` doğrudan `Long` olamaz.
- Boxing sonra reference widening olabilir: `int` → `Integer` → `Object`.
- Birden fazla equally specific candidate kalırsa call ambiguous olur.
- Runtime object type yeni overload'ı görünür yapmaz; overload compile-time
  reference types ile seçilir.

## 8. Autoboxing, unboxing ve `null`

```java
Integer boxed = 3; // boxing
int value = boxed; // unboxing
```

Wrapper `null` ise unboxing compile olur fakat runtime'da
`NullPointerException` üretir.

```java
Integer boxed = null;
// int value = boxed; // runtime NullPointerException
```

## 9. Return kontrolü

- `void` metot değer döndüremez. Non-void metot gövdesi sona düşerek normal
  tamamlanamaz; `return` varsa uygun türde değer ister. `throw` veya kesin
  sonsuz döngü nedeniyle normal tamamlanmayan bir gövde de derlenebilir.
- Return assignment conversion uygular; arbitrary narrowing otomatik yapılmaz.
- Returned reference yine pass-by-value'dur; object kopyalanmaz.

## OCP için 20 saniyelik analiz sırası

1. Declaration, access ve static receiver birlikte geçerli mi?
2. Overload phase sırası doğru mu; varargs/ambiguity var mı?
3. Execution parameter reassign mı, object mutation mı yapıyor?
4. Boxing `null` riski ve bütün return path'leri kontrol edildi mi?

## Aktif hatırlama · Özgün çalışma soruları

1. Return type method signature'ın parçası mıdır?
2. `int` argument için `long` ve `Integer` overload'ları varsa hangisi seçilir?
3. Reference parameter'a yeni object atamak caller variable'ını değiştirir mi?
4. Varargs parameter neden son sırada olmalıdır?

## Cevaplar

1. Hayır; signature name ve parameter type/order'dır.
2. `long`; primitive widening boxing'den önce uygulanır.
3. Hayır; reference value'nun kopyası reassign edilir.
4. Önce gelseydi hangi argument'ların varargs'a, hangilerinin sonraki parameter'a
   ait olduğu belirlenemezdi.
