# Nesne Oluşturma ve Initialization Sırası

Bu not, kaynak metindeki **constructor**, **member field**,
**instance initializer block** ve basit nesne başlatma sırası konularını Java 17 ve OCP sınavı
açısından düzenler.

## Learning objectives

Bu çalışmanın sonunda:

- class, object ve reference arasındaki farkı açıklayabilecek,
- constructor ile aynı adlı normal bir method'u ayırt edebilecek,
- member field'ları okuyup yazabilecek,
- code block ile instance initializer block'u ayırt edebilecek,
- field, instance initializer ve constructor çalışma sırasını izleyebileceksin.

## 1. Object, class ve reference

Bir **object (nesne)**, bir class'ın çalışma zamanındaki **instance (örnek)**
değeridir.

```java
Park p = new Park();
```

İfadeyi üç parçaya ayır:

| Parça | Anlamı |
|---|---|
| `Park` | Referans değişkeninin türü |
| `p` | Nesneye ulaşmak için kullanılan referans değişkeni |
| `new Park()` | Yeni nesne oluşturan constructor çağrısı |

`p`, nesnenin kendisini doğrudan içermez; nesneye ulaşmayı sağlayan bir
reference taşır.

## 2. Constructor çağırma

Constructor, yeni bir object oluşturulurken çalışan özel bir bildirimdir.

```java
public class Chick {
    public Chick() {
        System.out.println("in constructor");
    }
}
```

Bir constructor için iki ayırt edici kural:

1. Adı class adıyla aynı olmalıdır.
2. `void` dahil hiçbir return type yazılmaz.

### Constructor gibi görünen method tuzağı

```java
public class Chick {
    public void Chick() { }
}
```

Bu kod **başarıyla derlenir**, ancak `Chick()` bir constructor değildir. `void`
return type bulunduğu için büyük harfle başlayan sıradan bir instance method'dur.
`new Chick()` yazıldığında bu method otomatik çağrılmaz.

> **OCP exam trap:** Class adıyla aynı ada sahip olmak tek başına yeterli
> değildir. Return type görüyorsan bildirim constructor değil, method'dur.

## 3. Default constructor

Bir class içinde hiçbir constructor bildirilmezse compiler parametresiz bir
**default constructor** sağlar.

```java
public class Swan {
    // Compiler, Swan() constructor'ını sağlar.
}
```

Ancak herhangi bir constructor açıkça bildirilirse compiler artık default
constructor eklemez.

```java
public class Swan {
    public Swan(int eggCount) { }
}

// new Swan();  // DOES NOT COMPILE
```

> **Common mistake:** Yazılı parametresiz constructor ile compiler'ın sağladığı
> default constructor aynı şey değildir. “Default constructor” terimi yalnızca
> compiler tarafından eklenen constructor için kullanılır.

## 4. Field'ları başlatma

Field'lar bildirildikleri satırda veya constructor içinde başlatılabilir.

```java
public class Chicken {
    int numEggs = 12;  // Bildirim sırasında initialization
    String name;

    public Chicken() {
        name = "Duke"; // Constructor içinde initialization
    }
}
```

Constructor'ın temel amacı yeni nesnenin başlangıç durumunu hazırlamaktır;
constructor gövdesinde başka geçerli ifadeler de bulunabilir.

## 5. Member field okuma ve yazma

Bir instance variable'a nesne referansı üzerinden erişilebilir:

```java
public class Swan {
    int numberEggs;

    public static void main(String[] args) {
        Swan mother = new Swan();
        mother.numberEggs = 1;                 // write
        System.out.println(mother.numberEggs); // read
    }
}
```

Bu program başarıyla derlenir ve şu çıktıyı üretir:

```text
1
```

Örnekte erişim aynı class içinden yapıldığı için `numberEggs` alanına doğrudan
ulaşılabilir. Encapsulation uygulandığında field genellikle `private` tutulur ve
kontrollü erişim method'larla sağlanır.

### Önceki field değerlerini kullanma

```java
public class Name {
    String first = "Theodore";
    String last = "Moose";
    String full = first + last;
}
```

`full` başlatılırken daha önce bildirilmiş `first` ve `last` okunur. Sonuç
`"TheodoreMoose"` olur; kaynak kodda ayrıca boşluk eklenmediğine dikkat et.

## 6. Code block ve instance initializer

Eşleşen `{` ve `}` arasındaki bölüm bir **code block**'tur. Bir class gövdesinde,
method/constructor dışında bulunan ve `static` olmayan block ise
**instance initializer** olarak adlandırılır.

```java
public class Bird {                            // 1: class block
    public static void main(String[] args) {   // 2: method block
        { System.out.println("Feathers"); }    // 3: inner block
    }

    { System.out.println("Snowy"); }           // 4: instance initializer
}
```

Bu örnekte:

- toplam **4 code block**,
- yalnızca **1 instance initializer** vardır.

`main()` içindeki inner block, method çalıştığında yürütülür; instance
initializer değildir. Class gövdesindeki `Snowy` block'u ise her yeni nesne
oluşturulduğunda çalışır.

> **OCP exam trap:** Her süslü parantez çifti instance initializer değildir.
> Önce block'un bir method/constructor içinde olup olmadığına bak.

## 7. Basit initialization sırası

Bu ünitenin kapsamındaki sadeleştirilmiş sıra şöyledir:

1. Instance field initializer'lar ve instance initializer block'ları, kaynak
   dosyada göründükleri sırayla çalışır.
2. Bunların tamamı bittikten sonra constructor gövdesi çalışır.

Superclass ve `static` initialization ayrıntıları Class Design ünitesinde bu
sıraya eklenecektir.

```java
public class Chick {
    private String name = "Fluffy";

    { System.out.println("setting field"); }

    public Chick() {
        name = "Tiny";
        System.out.println("setting constructor");
    }

    public static void main(String[] args) {
        Chick chick = new Chick();
        System.out.println(chick.name);
    }
}
```

Çıktı:

```text
setting field
setting constructor
Tiny
```

Akış:

1. `main()` içinde `new Chick()` çağrılır.
2. `name`, `"Fluffy"` değerini alır.
3. Instance initializer `setting field` yazdırır.
4. Constructor `name` değerini `"Tiny"` olarak değiştirir.
5. Constructor `setting constructor` yazdırır.
6. `main()` son `name` değerini yazdırır: `Tiny`.

## 8. Illegal forward reference

Bir instance initializer, daha sonra bildirilmiş bir field'ı simple name ile
okumaya çalışırsa **illegal forward reference** oluşur:

```java
public class Chick {
    { System.out.println(name); } // DOES NOT COMPILE
    private String name = "Fluffy";
}
```

> **İnce ayrıntı:** OCP sorularında bildirimin fiziksel sırası önemlidir. Bu
> aşamada güvenli yaklaşım, bir field'ı okumadan önce bildirilmiş olmasını
> sağlamaktır.

## 9. Initialization sırasını izleme

```java
public class Egg {
    public Egg() {
        number = 5;
    }

    public static void main(String[] args) {
        Egg egg = new Egg();
        System.out.println(egg.number);
    }

    private int number = 3;
    { number = 4; }
}
```

Bu kod başarıyla derlenir ve şu çıktıyı üretir:

```text
5
```

Değer akışı:

```text
field initializer       instance initializer       constructor
number = 3        →      number = 4          →      number = 5
```

Son atama constructor içinde gerçekleştiği için ekrana `5` yazılır.

> **Memory tip:** **FIC** → **F**ields/blocks in file order, sonra
> **I**nstance hazırlığı tamamlanır, en sonda **C**onstructor gövdesi. Asıl kuralı
> “field ve block'lar dosya sırasıyla; constructor en son” diye hatırla.

## English → Turkish translation practice

### Sentence 1

**EN:** An object is an instance of a class.

**TR:** Bir nesne, bir sınıfın örneğidir.

- `instance of`: bir yapının somut örneği
- `be`: tanım cümlesinde eşitlik/kimlik bağlantısı kurar

### Sentence 2

**EN:** All you have to do is write `new` before the class name.

**TR:** Tek yapman gereken, class adından önce `new` yazmaktır.

- `all you have to do is ...`: “tek yapman gereken ...” kalıbı
- `before`: önce anlamı veren preposition

### Sentence 3

**EN:** The constructor runs after all fields and instance initializer blocks
have run.

**TR:** Constructor, tüm field'lar ve instance initializer block'ları
çalıştıktan sonra çalışır.

- `after + present perfect`: bir eylemin tamamlanmasından sonraki aşamayı vurgular
- `have run`: present perfect

Ayrıntılı dil çalışması için [ünite sözlüğüne](vocabulary.md) ve
[grammar notlarına](grammar_notes.md) bak.

## OCP tarzı mini quiz

Bu sorular özgün çalışma sorularıdır; gerçek sınav sorusu değildir.

### 1. Aşağıdakilerden hangisi constructor'dır?

```java
public class Fox {
    // Hangi satır constructor'dır?
    public Fox() { }          // A
    public void Fox() { }     // B
    void fox() { }            // C
    public static Fox() { }   // D
}
```

### 2. Compiler ne zaman default constructor sağlar?

A. Her class için\
B. Yalnızca hiçbir constructor açıkça bildirilmediğinde\
C. Yalnızca field bulunmadığında\
D. Yalnızca class `public` olduğunda

### 3. Aşağıdaki kod kaç instance initializer içerir?

```java
class Owl {
    { int x = 1; }
    void fly() { { int y = 2; } }
    { int z = 3; }
}
```

A. 1\
B. 2\
C. 3\
D. 5

### 4. Aşağıdaki kod ne yazdırır?

```java
class Score {
    int value = 1;
    { value = 2; }
    Score() { value = 3; }

    public static void main(String[] args) {
        System.out.println(new Score().value);
    }
}
```

A. `1`\
B. `2`\
C. `3`\
D. Kod derlenmez

### 5. `public void Chick() {}` için hangisi doğrudur?

A. Parametresiz constructor'dır.\
B. Return type nedeniyle sıradan bir method'dur.\
C. Class adıyla aynı olduğu için derlenmez.\
D. Yalnızca `static` olursa derlenir.

## Cevaplar ve açıklamalar

1. **A.** Class adıyla aynıdır ve return type yoktur. B'de `void` vardır; C'nin
   adı farklıdır; constructor `static` olamayacağı için D derlenmez.
2. **B.** Tek bir açık constructor bile compiler'ın default constructor
   sağlamasını engeller.
3. **B.** Method dışındaki iki block instance initializer'dır. Method içindeki
   iç block değildir.
4. **C.** Field `1`, block `2`, constructor `3` atar; son değer `3` olur.
5. **B.** `void` bir return type'tır; dolayısıyla bu bildirim method'dur.

## Kısa tekrar özeti

- Object, class'ın instance'ıdır; değişken nesneye ait reference'ı taşır.
- Constructor class adıyla aynıdır ve return type içermez.
- Compiler yalnızca hiç constructor yazılmadığında default constructor sağlar.
- Instance initializer, class içinde fakat method/constructor dışında bulunur.
- Field initializer ve instance initializer'lar dosya sırasıyla çalışır.
- Constructor gövdesi instance field/block initialization tamamlandıktan sonra
  çalışır.
