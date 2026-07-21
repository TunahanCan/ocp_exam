# Classpath, JAR ve Sınıf Bildirim Sırası

Bu not, kaynak metindeki **classpath**, **JAR oluşturma** ve bir Java kaynak
dosyasındaki öğelerin doğru sırası konularını Java 17 ve OCP sınavı açısından
düzenler.

## Learning objectives

Bu çalışmanın sonunda:

- `classpath` kavramının derleme ve çalıştırmadaki görevini açıklayabilecek,
- `javac`, `java` ve `jar` komutlarının sınavda önemli seçeneklerini ayırt
  edebilecek,
- Windows ile macOS/Linux classpath ayırıcılarını karşılaştırabilecek,
- `package`, `import` ve top-level type sırasını denetleyebilecek,
- tipik OCP derleme tuzaklarını fark edebileceksin.

## 1. Classpath nedir?

**Classpath**, Java araçlarına ihtiyaç duyulan derlenmiş sınıfların ve JAR
dosyalarının nerede aranacağını söyler.

- `javac` için: Programı **derlemek** amacıyla gereken sınıfların konumu.
- `java` için: Programı **çalıştırmak** amacıyla gereken sınıfların konumu.

Örneğin derlenmiş dosyanın yolu `classes/packageb/ClassB.class` ise:

```bash
java -cp classes packageb.ClassB
```

Burada:

- `classes`, classpath root'tur.
- `packageb.ClassB`, çalıştırılacak sınıfın **fully qualified class name**
  (tam nitelikli sınıf adı) değeridir.
- Komuta `.class` uzantısı veya `classes/packageb/ClassB.class` dosya yolu
  yazılmaz.

> **OCP exam trap:** Classpath paket klasörünün kendisini değil, paket ağacının
> başladığı kök dizini göstermelidir. Bu örnekte `classes/packageb` değil,
> `classes` yazılır.

## 2. Classpath seçeneklerinin üç yazımı

Aşağıdaki seçenekler aynı amacı taşır:

| Kısa seçenek | Uzun seçenek | İki tireli uzun seçenek |
|---|---|---|
| `-cp` | `-classpath` | `--class-path` |

```bash
java -cp classes packageb.ClassB
java -classpath classes packageb.ClassB
java --class-path classes packageb.ClassB
```

Kaynak metindeki `- cp`, `- classpath` ve `- - class- path` görünümleri sayfa
düzeni/OCR kaynaklıdır. Komut satırında boşluklar kaldırılmalı ve yukarıdaki
gerçek yazımlar kullanılmalıdır.

> **Memory tip:** Tek tireli kısa aile: `-cp`, `-classpath`. İki tireli,
> kelimeleri tireyle ayıran modern uzun biçim: `--class-path`.

## 3. Sınav için önemli `javac` ve `java` seçenekleri

### `javac` seçenekleri

| Seçenek | Görevi |
|---|---|
| `-cp <classpath>` | Derleme için gereken sınıfların/JAR'ların konumu |
| `-classpath <classpath>` | `-cp` ile aynı |
| `--class-path <classpath>` | `-cp` ile aynı |
| `-d <directory>` | Üretilen `.class` dosyalarının yerleştirileceği dizin |

Örnek:

```bash
javac -cp libs/helper.jar -d classes src/packageb/ClassB.java
```

Bu komutta `libs/helper.jar` derleme bağımlılığıdır; oluşan `.class` dosyaları
`classes` altına yazılır.

### `java` seçenekleri

| Seçenek | Görevi |
|---|---|
| `-cp <classpath>` | Çalışma sırasında aranacak sınıfların/JAR'ların konumu |
| `-classpath <classpath>` | `-cp` ile aynı |
| `--class-path <classpath>` | `-cp` ile aynı |

> **Common mistake:** `javac -d` çıktı dizinini belirler. `java` komutundaki
> `-cp` ise JVM'in sınıfları nerede arayacağını belirler. Aynı görev değildir.

## 4. Birden fazla classpath girdisi

Bir classpath içinde mevcut dizin, başka bir sınıf dizini ve bir JAR birlikte
bulunabilir.

### Windows

```bash
java -cp ".;C:\temp\someOtherLocation;C:\temp\myJar.jar" myPackage.MyClass
```

### macOS/Linux

```bash
java -cp ".:/tmp/someOtherLocation:/tmp/myJar.jar" myPackage.MyClass
```

| İşletim sistemi | Classpath ayırıcısı |
|---|---|
| Windows | noktalı virgül `;` |
| macOS/Linux | iki nokta `:` |

Nokta (`.`), **current directory** (mevcut dizin) anlamına gelir.

> **OCP exam trap:** Windows'ta `;`, macOS/Linux'ta `:` kullanılır. Komutun
> çalışacağı işletim sistemi soruda belirtilmişse ayırıcıyı ona göre seç.

## 5. Classpath wildcard kullanımı

Bir dizindeki tüm JAR dosyalarını classpath'e eklemek için `*` kullanılabilir.

```bash
# Windows
java -cp "C:\temp\directoryWithJars\*" myPackage.MyClass

# macOS/Linux
java -cp "/tmp/directoryWithJars/*" myPackage.MyClass
```

Wildcard:

- belirtilen dizindeki JAR dosyalarını eşleştirir,
- alt dizinlere **recursive** (özyinelemeli) biçimde inmez,
- alt klasörlerdeki JAR'ları kendiliğinden eklemez.

## 6. JAR dosyası oluşturma

**JAR (Java Archive)**, çoğunlukla derlenmiş Java sınıflarını ve ilgili
kaynakları bir arada taşıyan ZIP tabanlı arşiv biçimidir.

### Mevcut dizinin içeriğini paketlemek

```bash
jar -cvf myNewFile.jar .
jar --create --verbose --file myNewFile.jar .
```

### Başka bir dizinin içeriğini paketlemek

```bash
jar -cvf myNewFile.jar -C dir .
```

| Kısa | Uzun | Anlamı |
|---|---|---|
| `-c` | `--create` | Yeni JAR oluşturur |
| `-v` | `--verbose` | İşlem ayrıntılarını yazdırır |
| `-f <file>` | `--file <file>` | JAR dosyasının adını belirtir |
| `-C <directory>` | — | Sonraki dosyalar için dizini değiştirir |

`-C dir .`, önce `dir` dizinine geçilmesini, ardından bu dizinin içeriğinin
arşive eklenmesini ifade eder. `-C` seçeneğinin uzun biçimi yoktur.

> **Memory tip:** `cvf` → **c**reate, **v**erbose, **f**ile.

## 7. Java kaynak dosyasında öğelerin sırası

Sınav için temel hatırlatıcı **PIC**'tir:

1. **P**ackage declaration
2. **I**mport statements
3. **C**lass veya başka bir top-level type declaration

```java
package structure;      // İlk anlamlı bildirim

import java.util.List;  // package'dan sonra

public class Meerkat {  // import'lardan sonra
    double weight;      // Field'lar class içinde

    public double getWeight() {
        return weight;
    }

    double height;      // Field ve method'ların birlikte olması gerekmez
}
```

Kurallar:

- `package` bildirimi isteğe bağlıdır; varsa ilk anlamlı bildirim olmalıdır.
- `import` bildirimleri isteğe bağlıdır; varsa `package` sonrasında ve type
  bildirimlerinden önce gelmelidir.
- Field ve method bildirimleri bir class, record, enum veya interface gibi type
  gövdesinin içinde bulunmalıdır.
- Yorumlar ve boş satırlar bu sıralamayı bozmaz; kod içinde uygun yerlerde
  bulunabilir.

```java
/* Dosya başlığı */

package structure;

// Meerkat sınıfı
public class Meerkat { }
```

Bu örnek başarıyla derlenir. `import` bulunması zorunlu değildir.

### Derlenmeyen örnek

```java
import java.util.*;
package structure;       // DOES NOT COMPILE
String name;             // DOES NOT COMPILE
public class Meerkat { }
```

İki bağımsız problem vardır:

1. `package`, `import` bildiriminden sonra yazılmıştır.
2. `name` field'ı herhangi bir type gövdesinin dışında bildirilmiştir.

Bu nedenle dosya bütünüyle derlenmez. Son satırın biçimi tek başına geçerli
görünse de aynı compilation unit içindeki önceki hatalar derlemeyi başarısız
kılar.

> **OCP exam trap:** Bir kod parçasında iki `public` top-level class görürsen,
> soru aynı `.java` dosyasında olduklarını açıkça söylemediği sürece bunların
> ayrı dosyalarda olduğunu varsayabilirsin. Aynı dosyadaysalar en fazla bir
> top-level type `public` olabilir ve dosya adı onun adıyla eşleşmelidir.

## English → Turkish translation practice

### Sentence 1

**EN:** To run the program, you specify the classpath so Java knows where to
find the classes.

**TR:** Programı çalıştırmak için classpath'i belirtirsin; böylece Java,
sınıfları nerede bulacağını bilir.

- `to run the program`: amaç bildiren infinitive yapı
- `so`: burada amaç/sonuç bağlantısı kurar
- `where to find`: “nerede bulacağını” anlamında question word + infinitive

### Sentence 2

**EN:** You can use a wildcard to match all the JARs in a directory.

**TR:** Bir dizindeki tüm JAR dosyalarını eşleştirmek için wildcard
kullanabilirsin.

- `to match`: amaç bildirir
- `in a directory`: konum belirten prepositional phrase

### Sentence 3

**EN:** Comments can go anywhere in the code.

**TR:** Yorumlar kodun herhangi bir yerinde bulunabilir.

- `can`: yeterlilik/olasılık bildiren modal verb
- `anywhere`: herhangi bir yerde

Ayrıntılı dil çalışması için [ünite sözlüğüne](vocabulary.md) ve
[grammar notlarına](grammar_notes.md) bak.

## OCP tarzı mini quiz

Bu sorular özgün çalışma sorularıdır; gerçek sınav sorusu değildir.

### 1. Hangi komut Java 17'de geçerli bir classpath kullanımıdır?

A. `java - cp classes packageb.ClassB`\
B. `java --class-path classes packageb.ClassB`\
C. `java --classpath=classes packageb.ClassB`\
D. `java classes/packageb/ClassB.class`

### 2. macOS'ta iki dizini classpath içinde hangi karakter ayırır?

A. `;`\
B. `,`\
C. `:`\
D. `.`

### 3. `lib/*` classpath girdisi neyi ekler?

A. `lib` ve tüm alt dizinlerdeki her dosyayı\
B. Yalnızca `lib` içindeki JAR dosyalarını\
C. Yalnızca `lib` içindeki `.class` dosyalarını\
D. `lib` altındaki JAR'ları recursive biçimde

### 4. Doğru bildirim sırası hangisidir?

A. import → package → class\
B. class → package → import\
C. package → class → import\
D. package → import → class

### 5. `javac -d classes Bird.java` komutunda `-d` neyi belirler?

A. Bağımlılıkların aranacağı dizini\
B. Kaynak dosyanın package adını\
C. Üretilen class dosyalarının hedef dizinini\
D. Çalıştırılacak main class'ı

## Cevaplar ve açıklamalar

1. **B.** Geçerli iki tireli yazım `--class-path` biçimidir. A'daki boşluk ve
   C'deki seçenek adı yanlıştır; D classpath ile class adı kullanımını karıştırır.
2. **C.** macOS/Linux `:`, Windows `;` kullanır.
3. **B.** Classpath wildcard doğrudan o dizindeki JAR'ları eşleştirir; alt
   dizinlere inmez.
4. **D.** Hatırlatıcı **PIC**: package, import, class.
5. **C.** `-d`, `javac` çıktısının yerleştirileceği dizini belirler.

## Kısa tekrar özeti

- `-cp`, `-classpath` ve `--class-path` eşdeğerdir.
- Windows classpath ayırıcısı `;`, macOS/Linux ayırıcısı `:` karakteridir.
- `.` mevcut dizini, `*` belirtilen dizindeki JAR dosyalarını temsil eder.
- `jar -cvf` için `c=create`, `v=verbose`, `f=file` eşlemesini hatırla.
- Kaynak dosyasında temel sıra **PIC**: package → import → class.
- Field ve method'lar bir type gövdesinin içinde bulunmalıdır.
