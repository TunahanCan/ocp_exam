# Chapter 1 - Building Blocks (Tam Kapsamlı Türkçe Çeviri + Örnekler)

> Bu doküman, Chapter 1 içeriğini sınav odaklı şekilde **başlık başlık Türkçe** anlatır ve her konuya kısa/uygulanabilir örnekler ekler.
> Amaç: konuları `com.java` altında tek yerde toplamak ve tekrar ederken hızlı referans sunmak.

---

## İçindekiler (Chapter 1 Tam Liste)

1. Learning about the Environment  
2. Major Components of Java  
3. Downloading a JDK  
4. Understanding the Class Structure  
5. Fields and Methods  
6. Classes and Source Files  
7. Writing/Creating a `main()` Method  
8. Comments  
9. Passing Parameters to a Java Program  
10. Understanding Package Declarations and Imports  
11. Packages  
12. Ordering Elements in a Class  
13. Creating Objects  
14. Wildcards  
15. Creating a JAR File  
16. Calling Constructors  
17. Following the Order of Initialization  
18. Understanding Data Types  
19. Reading and Writing Member Fields  
20. Executing Instance Initializer Blocks  
21. Using Primitive Types  
22. Defining Text Blocks  
23. Declaring Variables  
24. Using Reference Types  
25. Creating Wrapper Classes  
26. Identifying Identifiers  
27. Declaring Multiple Variables  
28. Initializing Variables  
29. Creating Local Variables  
30. Inferring the Type with `var`  
31. Managing Variable Scope  
32. Passing Constructor and Method Parameters  
33. Defining Instance and Class Variables  
34. Limiting Scope  
35. Reviewing Scope  
36. Destroying Objects  
37. Tracing Scope  
38. Applying Scope to Classes  
39. Understanding Garbage Collection  
40. Tracing Eligibility  
41. Redundant Imports  
42. Naming Conflicts  
43. Creating a New Package  
44. Compiling and Running Code with Packages  
45. Compiling to Another Directory  
46. Compiling with JAR Files  
47. Distinguishing between Primitives and Reference Types  
48. Exam Essentials  
49. Summary

---

## 1) Learning about the Environment

Java geliştirme ortamının temel parçaları:
- **JDK**: Derleyici (`javac`), çalıştırıcı (`java`), paketleme (`jar`) dahil geliştirme araçları.
- **JRE**: Kodun çalışması için runtime bileşenleri (modern dağıtımlarda JDK içinde).
- **JVM**: Bytecode’u çalıştıran sanal makine.

Hızlı kontrol:
```bash
java -version
javac -version
```

---

## 2) Major Components of Java

- **Class**: Programın şablonu.
- **Object**: Class’tan üretilen örnek.
- **Method**: Davranış.
- **Field**: Durum/veri.
- **Package**: İsimlendirme + gruplama.

```java
package com.java.chapter1;

public class Car {
    String model;          // field

    void start() {         // method
        System.out.println(model + " çalıştı");
    }
}
```

---

## 3) Downloading a JDK

Pratik adım:
1. JDK 17+ kur.
2. PATH’e `bin` klasörünü ekle.
3. `java -version`, `javac -version` ile doğrula.

Sınav tarafı: JDK/JRE/JVM rollerini karıştırmamak kritik.

---

## 4) Understanding the Class Structure

Genel yapı sırası:
1. `package`
2. `import`
3. `class/interface/enum/record`

```java
package com.java.chapter1;
import java.util.*;

public class StructureSample {
    int count;

    void print() {
        System.out.println(count);
    }
}
```

---

## 5) Fields and Methods

- Field, nesne/sınıf state’ini tutar.
- Method iş yapar, parametre alabilir, döndürebilir.

```java
class Score {
    int points;            // field

    void add(int x) {      // method
        points += x;
    }
}
```

---

## 6) Classes and Source Files

Kurallar:
- Bir `.java` dosyasında birden fazla class olabilir.
- **Public class adı dosya adıyla aynı olmalı.**

```java
// File: Zoo.java
public class Zoo {}
class ZooHelper {}
```

---

## 7) Writing/Creating a main() Method

Geçerli imza:
```java
public static void main(String[] args)
```

Varargs formu da geçerli:
```java
public static void main(String... args)
```

Örnek:
```java
public class MainApp {
    public static void main(String[] args) {
        System.out.println("Hello OCP");
    }
}
```

---

## 8) Comments

```java
// tek satır
/* çok satır */
/** JavaDoc */
```

Sınavda yorumlar kodu “metinsel” etkiler; çalıştırma mantığını değiştirmez.

---

## 9) Passing Parameters to a Java Program

```bash
java com.java.chapter1.MainApp bir iki uc
```

```java
public static void main(String[] args) {
    for (String s : args) {
        System.out.println(s);
    }
}
```

---

## 10) Understanding Package Declarations and Imports

```java
package com.java.chapter1;
import java.util.List;
import java.util.ArrayList;
```

- `package` dosyanın ilk anlamlı satırıdır.
- Import’lar package’den sonra gelir.

---

## 11) Packages

Package, class’ları mantıksal hiyerarşiyle ayırır:
- `com.java.chapter1`
- Dosya yolu: `com/java/chapter1/`

Faydaları: isim çakışması azaltma, organizasyon, erişim kontrolü.

---

## 12) Ordering Elements in a Class

Okunabilirlik için önerilen sıra:
1. Field
2. Initializer block
3. Constructor
4. Method

Java her zaman katı sıralama zorunlu tutmaz; fakat sınav senaryoları çoğunlukla bu akışla sorulur.

---

## 13) Creating Objects

```java
class Animal {}

Animal a = new Animal();
```

- `new` bellekte nesne oluşturur.
- Sol taraf referans değişkenidir.

---

## 14) Wildcards

```java
import java.util.*;
```

- `*` tüm class’ları import eder (paket içi).
- **Alt paketleri import etmez** (`java.util.function` dahil olmaz).

---

## 15) Creating a JAR File

```bash
jar --create --file app.jar -C out .
```

Çalıştırma:
```bash
java -cp app.jar com.java.chapter1.MainApp
```

---

## 16) Calling Constructors

```java
class Dog {
    String name;

    Dog(String name) {
        this.name = name;
    }
}
```

- Constructor class adıyla aynı olur.
- Dönüş tipi olmaz.

---

## 17) Following the Order of Initialization

Çalışma sırası:
1. static field + static initializer (class yüklenirken 1 kez)
2. instance field + instance initializer (her nesnede)
3. constructor

```java
class InitOrder {
    static { System.out.println("A-static"); }
    { System.out.println("B-instance"); }
    InitOrder() { System.out.println("C-ctor"); }
}
```

---

## 18) Understanding Data Types

### Primitive (8 tip)
- `boolean`, `byte`, `short`, `int`, `long`, `float`, `double`, `char`

### Reference
- Class, interface, array, `String`, wrapper vb.

---

## 19) Reading and Writing Member Fields

```java
class Book {
    String title;
}

Book b = new Book();
b.title = "Java 17";            // write
System.out.println(b.title);     // read
```

`null` referans üzerinden field erişimi `NullPointerException` üretir.

---

## 20) Executing Instance Initializer Blocks

```java
class Player {
    { System.out.println("instance init"); }

    Player() {
        System.out.println("constructor");
    }
}
```

Nesne oluşturulunca önce instance initializer çalışır.

---

## 21) Using Primitive Types

```java
int n = 10;
long l = 10L;
float f = 3.14f;
double d = 3.14;
char c = 'A';
boolean ok = true;
```

Sayı literal’lerinde suffix’leri unutmak sınavda sık hata sebebidir.

---

## 22) Defining Text Blocks

```java
String html = """
<html>
  <body>Merhaba</body>
</html>
""";
```

Çok satırlı stringlerde okunabilirliği artırır.

---

## 23) Declaring Variables

```java
int age;
String name;
```

Değişken bildirimi = tip + isim.

---

## 24) Using Reference Types

```java
String s = "abc";
int[] arr = {1,2,3};
Object o = new Object();
```

Reference değişken nesnenin kendisini değil referansını taşır.

---

## 25) Creating Wrapper Classes

```java
Integer x = Integer.valueOf(10);
Double y = Double.valueOf("3.14");
```

Autoboxing/unboxing:
```java
Integer a = 5; // boxing
int b = a;     // unboxing
```

---

## 26) Identifying Identifiers

Kurallar:
- Harf, `_`, `$` ile başlayabilir.
- Rakamla başlayamaz.
- Java keyword olamaz.

Örnek:
- Geçerli: `_count`, `$x`, `name2`
- Geçersiz: `2name`, `class`

---

## 27) Declaring Multiple Variables

```java
int x = 1, y = 2, z = 3;
```

Dikkat:
```java
int a, b = 5; // a atanmamış, b atanmış
```

---

## 28) Initializing Variables

- Class/instance field’lar default değer alır.
- Local variable default almaz.

```java
class Defaults {
    int n;        // 0
    boolean ok;   // false
}
```

---

## 29) Creating Local Variables

```java
void test() {
    int x = 10;   // local
}
```

Scope’u sadece method/blok içidir.

---

## 30) Inferring the Type with var

```java
var name = "Java"; // String
var count = 3;      // int
```

Kurallar:
- Sadece local variable.
- `var x;` geçersiz.
- `var` null ile tek başına kullanılamaz: `var v = null;` geçersiz.

---

## 31) Managing Variable Scope

```java
{
    int a = 5;
}
// a burada yok
```

Aynı scope’ta aynı isim tekrar tanımlanamaz.

---

## 32) Passing Constructor and Method Parameters

```java
class MathOps {
    MathOps(int seed) { }

    int add(int x, int y) {
        return x + y;
    }
}
```

Parametreler method/constructor yaşam süresince geçerlidir.

---

## 33) Defining Instance and Class Variables

```java
class Student {
    static String school = "OCP Academy"; // class variable
    String name;                           // instance variable
}
```

- `static` alan tüm nesnelerce paylaşılır.
- Instance alan nesne başına ayrıdır.

---

## 34) Limiting Scope

Scope’u küçük tutmak hata olasılığını düşürür.
- Değişkeni ihtiyaç duyulan en dar blokta tanımla.

---

## 35) Reviewing Scope

Tipik scope alanları:
- Class scope
- Method scope
- Block scope
- Parameter scope

Sınav soruları çoğunlukla “hangi satır derlenir/derlenmez?” şeklinde gelir.

---

## 36) Destroying Objects

Java’da manuel `free/delete` yoktur.
Nesne, referans kalmayınca GC için aday olur.

---

## 37) Tracing Scope

Kod izleme yaklaşımı:
1. Hangi değişken nerede tanımlı?
2. O satırda erişilebilir mi?
3. Aynı isimli başka değişken gölgeleme yapıyor mu?

---

## 38) Applying Scope to Classes

```java
class A {
    int x = 1;            // instance scope
    static int y = 2;     // class scope

    void m(int p) {       // parameter scope
        int z = 3;        // local scope
        System.out.println(x + y + p + z);
    }
}
```

---

## 39) Understanding Garbage Collection

- GC otomatik çalışır.
- Çalışma zamanı garanti edilmez.
- `System.gc()` sadece istektir, garanti değildir.

---

## 40) Tracing Eligibility

Bir nesne GC’ye uygun olabilir:
- Referans `null` yapılır.
- Referans başka nesneye atanır.
- Scope dışına çıkar.

```java
String s = new String("x");
s = null;
```

---

## 41) Redundant Imports

Aynı import’u tekrar etmek gereksizdir.

```java
import java.util.List;
import java.util.List; // redundant
```

---

## 42) Naming Conflicts

```java
import java.util.Date;
// import java.sql.Date; // conflict
```

Çözüm: fully qualified isim kullan.

```java
java.util.Date d = new java.util.Date();
```

---

## 43) Creating a New Package

Yeni package örneği:
- package: `com.java.chapter1.examples`
- klasör: `com/java/chapter1/examples`

---

## 44) Compiling and Running Code with Packages

```bash
javac -d out src/com/java/chapter1/MainApp.java
java -cp out com.java.chapter1.MainApp
```

---

## 45) Compiling to Another Directory

`-d` ile class çıktısını hedef klasöre yönlendirirsin.

```bash
javac -d build/classes src/com/java/chapter1/MainApp.java
```

---

## 46) Compiling with JAR Files

```bash
jar --create --file app.jar -C build/classes .
java -cp app.jar com.java.chapter1.MainApp
```

---

## 47) Distinguishing between Primitives and Reference Types

| Özellik | Primitive | Reference |
|---|---|---|
| Saklanan | Değer | Referans |
| Null olabilir mi | Hayır | Evet |
| Method çağrısı | Yok | Var |
| Boyut | Sabit tipe bağlı | Referans boyutu sabit, nesne değişken |

---

## 48) Exam Essentials (Sınav İçin Özet Kritikler)

- `main()` imzası ve `String...` varyantını bil.
- `package` + `import` sıralamasını karıştırma.
- Local variable default değer almaz.
- `var` sadece local’de ve init ile.
- Initialization sırası: static -> instance -> constructor.
- Wildcard import alt paketleri kapsamaz.
- Primitive/reference davranış farkını kod izleyerek çöz.
- Scope sorularında blok sınırlarını tek tek takip et.

---

## 49) Summary

Chapter 1’in ana kazanımı:
1. Java dosya yapısı ve derleme/çalıştırma modelini doğru kurmak.
2. Class-field-method ve object temelini netleştirmek.
3. Tip sistemi (`primitive/reference/wrapper`) ve değişken yaşam alanlarını kavramak.
4. Initialization + GC + import/package kurallarını sınav seviyesinde yorumlayabilmek.

Bu chapter net oturursa sonraki chapter’larda (operators, decisions, methods, class design) hız ciddi şekilde artar.
