# Unit 01 Grammar Notes · Building Blocks

Bu notlar, Unit 01 için verilen teknik İngilizce metinde karşılaşılan yapılardan
seçilmiştir. Amaç hem teknik metni doğru çevirmek hem de YDS'de yapı ve anlam
ilişkisini hızlı görmektir.

> **Çalışma yöntemi:** Her yapıda önce formülü incele, ardından İngilizce örneği
> Türkçesini kapatarak çöz. Son olarak aynı kalıpla kendi Java cümleni kur.

## 1. Amaç bildiren infinitive: `to + verb`

### Kısa açıklama

Cümlenin başında veya ana eylemden sonra gelen `to + verb`, çoğunlukla “-mek
için” anlamıyla amaç bildirir.

### Formül

```text
To + V1, subject + verb ...
subject + verb ... + to + V1
```

### Kaynak bağlamlı örnek

**EN:** To run the program, you specify the classpath.\
**TR:** Programı çalıştırmak için classpath'i belirtirsin.

**EN:** Use a wildcard to match all the JARs.\
**TR:** Tüm JAR'ları eşleştirmek için wildcard kullan.

> **YDS tip:** Buradaki virgülle ayrılmış `To run the program` amaç bildirir.
> Ancak cümle başındaki her infinitive amaç değildir: `To learn Java takes time.`
> cümlesinde `To learn Java` özne, `takes` çekimli fiildir.

## 2. Amaç/sonuç bağlantısı kuran `so`

### Kısa açıklama

`so + clause`, bağlama göre “böylece”, “bu nedenle” veya konuşma dilinde “...mesi
için” anlamı verebilir. Ardından özne ve çekimli fiil gelir.

### Formül

```text
main clause + so + subject + verb
```

### Kaynak bağlamlı örnek

**EN:** You specify the classpath so Java knows where to find the classes.\
**TR:** Java'nın sınıfları nerede bulacağını bilmesi için classpath'i belirtirsin.

Alternatif doğal çeviri: “Classpath'i belirtirsin; böylece Java sınıfları nerede
bulacağını bilir.”

> **Common mistake:** `so` sonrasında bir clause bulunur. `so that` açık amaç
> bildirirken `so` tek başına sonuç anlamına da gelebilir; kesin anlamı bağlam
> belirler.

## 3. `question word + to-infinitive`

### Kısa açıklama

`where/how/what/when + to + verb`, dolaylı bir soruyu kısa biçimde aktarır.
Türkçede genellikle “nerede/nasıl/ne...-eceğini” şeklinde çevrilir.

### Formül

```text
where / how / what / when + to + V1
```

### Kaynak bağlamlı örnek

**EN:** Java knows where to find the classes.\
**TR:** Java, sınıfları nerede bulacağını bilir.

**EN:** The developer decides how to organize the packages.\
**TR:** Geliştirici package'ları nasıl düzenleyeceğine karar verir.

> **YDS tip:** Bu yapı tam bir soru değildir; daha büyük cümlede object görevinde
> bulunan reduced noun clause olarak düşünülebilir.

## 4. Seçenek/olasılık bildiren `might`

### Kısa açıklama

`might + V1`, kesin olmayan olasılık bildirir; tek başına belirli bir olasılık
yüzdesi veya her bağlamda `may`den daha düşük olasılık göstermez. `You might wonder ...` akademik ve teknik
metinlerde okuyucunun olası sorusuna geçiş yapmak için sık kullanılır.

### Formül

```text
subject + might + V1
```

### Kaynak bağlamlı örnek

**EN:** You might wonder why there are three classpath options.\
**TR:** Neden üç classpath seçeneği olduğunu merak ediyor olabilirsin.

> **Common mistake:** Modal verb'den sonra fiilin yalın hali gelir: `might
> wonder`; `might wonders` veya `might to wonder` kullanılmaz.

## 5. Neden bildiren `because` ve `since`

### Kısa açıklama

`because + clause` açık ve güçlü bir neden verir. `since + clause` teknik
metinlerde “-dığı için” anlamıyla daha arka planda kabul edilen nedeni sunabilir.
`since` ayrıca “-den beri” zaman anlamına da gelir.

### Formül

```text
result + because/since + subject + verb
```

### Kaynak bağlamlı örnek

**EN:** Developers choose `-cp` because it requires less typing.\
**TR:** Geliştiriciler daha az yazma gerektirdiği için `-cp` seçeneğini seçer.

**EN:** It is not a constructor since it has a return type.\
**TR:** Return type'a sahip olduğu için constructor değildir.

> **YDS tip:** `since` sonrasında başlangıç zamanı geliyorsa zaman; özne + fiil
> içeren neden cümlesi geliyorsa bağlama göre “çünkü/-dığı için” anlamını ara.

## 6. Koşul yapıları: `if` ve `unless`

### Kısa açıklama

`if`, bir koşul gerçekleştiğinde oluşacak sonucu verir. `unless`, “if ... not”
anlamına gelir ve Türkçede “-medikçe/-mazsa” diye çevrilir.

### Formül

```text
If + present simple, subject + will/can/V1 ...
Unless + affirmative clause, result ...
```

### Kaynak bağlamlı örnek

**EN:** If you use the wrong number of dashes, the program will not run.\
**TR:** Yanlış sayıda tire kullanırsan program çalışmaz.

**EN:** Assume the classes are in different files unless the question says
otherwise.\
**TR:** Soru aksini söylemedikçe sınıfların farklı dosyalarda olduğunu varsay.

> **Common mistake:** `unless` zaten olumsuz anlam taşır. Standart kullanımda
> ardından ayrıca `not` getirip çift olumsuzluk oluşturma.

## 7. `when + clause` ile zaman/koşul ilişkisi

### Kısa açıklama

`when`, bir işlemin gerçekleştiği zamanı belirtir. Genel kuralları anlatan
teknik metinlerde Türkçeye “-dığında” diye çevrilir ve koşula yakın bir işlev
görebilir.

### Formül

```text
When + subject + present simple, subject + present simple
```

### Kaynak bağlamlı örnek

**EN:** The inner block runs when the `main()` method is executed.\
**TR:** Inner block, `main()` method'u çalıştırıldığında yürütülür.

**EN:** The compiler supplies a default constructor when none is declared.\
**TR:** Hiç constructor bildirilmediğinde compiler default constructor sağlar.

> **YDS tip:** Genel gerçeklerde hem `when` clause hem ana cümle simple present
> olabilir. Gelecek anlamı olsa bile time clause içinde çoğunlukla `will`
> kullanılmaz.

## 8. Passive voice: `be + V3`

### Kısa açıklama

Passive voice, işi yapan kişiden çok işlemden etkilenen öğeyi öne çıkarır.
Teknik metinlerde süreç ve kuralları tarafsız anlatmak için çok yaygındır.

### Formül

```text
subject + am/is/are/was/were + V3
modal + be + V3
```

### Kaynak bağlamlı örnek

**EN:** Blank lines are ignored.\
**TR:** Boş satırlar göz ardı edilir.

**EN:** Fields must be declared inside a class.\
**TR:** Field'lar bir class içinde bildirilmelidir.

> **YDS tip:** `be + V3` gördüğünde öznenin eylemi yapan mı, eylemden etkilenen
> mi olduğunu kontrol et. `must be declared` = modal + passive.

## 9. Relative clause: `which/that/who`

### Kısa açıklama

Relative clause, kendinden önceki noun hakkında ek bilgi verir. Nesneler ve
kavramlar için `which/that`, kişiler için çoğunlukla `who` kullanılır.

### Formül

```text
noun + which/that + verb ...
person + who + verb ...
```

### Kaynak bağlamlı örnek

**EN:** A constructor is a special declaration that creates a new object.\
**TR:** Constructor, yeni bir nesne oluşturan özel bir bildirimdir.

**EN:** The directory contains JAR files that are required at runtime.\
**TR:** Dizin, çalışma zamanında gerekli olan JAR dosyalarını içerir.

> **YDS tip:** `that creates ...` bölümü doğrudan önceki `declaration` adını
> niteler. Çeviriye ana cümleden başlayıp relative clause'u ada bağlamak yapıyı
> çözmeyi kolaylaştırır.

## 10. `all + relative clause + be ...` odak kalıbı

### Kısa açıklama

`All you have to do is ...`, yapılması gereken işlemi tek bir adıma indirger.
Doğal Türkçesi “Tek yapman gereken ...” biçimindedir.

### Formül

```text
All + subject + have to do + is + (to) V1
```

### Kaynak bağlamlı örnek

**EN:** All you have to do is write `new` before the class name.\
**TR:** Tek yapman gereken class adından önce `new` yazmaktır.

> **Common mistake:** `is` sonrasında yalın fiil veya `to + verb` görülebilir.
> Yapıyı kelime kelime “bütün yapmak zorunda olduğun...” diye çevirmek yerine
> Türkçede doğal olan “tek yapman gereken” kalıbını kullan.

## 11. Sıralama bildiren `before`, `after`, `once`

### Kısa açıklama

Bu bağlaçlar iki eylemin zaman sırasını kurar. `once`, teknik süreçlerde “-ınca,
tamamlandığında” anlamı verir.

### Formül

```text
before/after/once + subject + verb, main clause
main clause + before/after/once + subject + verb
```

### Kaynak bağlamlı örnek

**EN:** The constructor runs after all fields and initializer blocks have run.\
**TR:** Constructor, tüm field ve initializer block'ları çalıştıktan sonra
çalışır.

**EN:** Once initialization is complete, execution returns to `main()`.\
**TR:** Initialization tamamlandığında yürütme `main()` method'una döner.

> **YDS tip:** Önce olayları zaman çizgisine yerleştir. `after X, Y` yapısında X
> önce, Y sonra gerçekleşir; Türkçe sözcük sırası bunu bazen gizleyebilir.

## 12. Reduced passive time clause: `when + V3`

### Kısa açıklama

`when` sonrasında özne ve `be` düşürülerek passive bir time/condition clause
kısaltılabilir. Gizli özne, ana cümlenin öznesi veya bağlamdaki isimdir.

### Formül

```text
when + subject + be + V3  →  when + V3
```

### Kaynak bağlamlı örnek

**EN:** Which expressions, when inserted into the blank, allow the code to
compile?\
**TR:** Hangi ifadeler boşluğa yerleştirildiğinde kodun derlenmesini sağlar?

Tam biçim: `when the expressions are inserted into the blank`.

> **YDS tip:** `when inserted` ifadesini active biçimde “yerleştirdiğinde” diye
> değil, passive anlamı koruyarak “yerleştirildiğinde” diye çöz. `inserted`
> burada past tense değil, past participle'dır.

## 13. `rather than` ile tercih ve karşıtlık

`rather than`, bir seçeneğin diğerinin yerine kullanıldığını anlatır.

```text
X rather than Y
```

**EN:** Use `Integer` rather than `int` when `null` is required.

**TR:** `null` gerektiğinde `int` yerine `Integer` kullan.

> **YDS ipucu:** `rather than` sonrasındaki yapı, karşılaştırılan ilk yapıyla
> parallel olmalıdır.

## Cümleyi parçalayarak okuma

[İlgili kaynak bölümü](bilingual_notes.md#initializing-variables). Aşağıdaki çalışma cümlesi
kaynak bağlamına dayanır; gerektiğinde öğretim amacıyla sadeleştirilmiştir.

**English:** Which expressions, when inserted into the blank, allow the code to compile?

**Çözümleme:** `Which expressions` = özne; `allow` = ana fiil; `the code` = nesne; `to compile` = nesnenin yaptığı iş. Araya giren `when inserted into the blank`, `when the expressions are inserted ...` edilgen yan cümlesinin kısaltmasıdır.

**Doğal Türkçe:** Hangi ifadeler boşluğa yerleştirildiğinde kodun derlenmesini sağlar?

**Kapalı kitap kontrolü:** `when inserted`ı kaldır: ana soru hâlâ tamam mı? `allow`dan sonra neden `to` var?

## Mini quiz

### 1. Boşluğu uygun seçenekle tamamla

`_____ run the class, specify its fully qualified name.`

A. Because\
B. To\
C. Unless\
D. Since

### 2. En doğal çeviri hangisidir?

`Java knows where to find the class.`

A. Java, sınıfı bulmak için nerede bilir.\
B. Java, sınıfın nerede bulduğunu bilir.\
C. Java, sınıfı nerede bulacağını bilir.\
D. Java, nerede sınıf bulmak bilir.

### 3. Boşluğu uygun seçenekle tamamla

`The program will not compile _____ the package declaration comes first.`

A. unless\
B. throughout\
C. after\
D. so

### 4. Passive voice içeren cümle hangisidir?

A. Java locates the class.\
B. The developer creates a JAR.\
C. Blank lines are ignored.\
D. Constructors initialize fields.

### 5. Olay sırası hangisidir?

`The constructor runs after the initializer block has run.`

A. Önce constructor, sonra initializer\
B. İkisi aynı anda\
C. Önce initializer, sonra constructor\
D. Sıra belirtilmiyor

## Cevaplar ve açıklamalar

1. **B.** Cümle başındaki `To run` amaç bildirir.
2. **C.** `where to find` doğal olarak “nerede bulacağını” diye çevrilir.
3. **A.** `unless`, “package bildirimi önce gelmezse” koşulunu kurar.
4. **C.** `are + ignored (V3)` passive voice yapısıdır.
5. **C.** `after` clause içindeki initializer önce tamamlanır; constructor sonra
   çalışır.

## Kısa tekrar özeti

- Amaç: `to + V1`
- Amaç/sonuç: `so + clause`
- Dolaylı kısa soru: `where/how/what + to + V1`
- Olasılık: `might + V1`
- Neden: `because/since + clause`
- Koşul: `if`; olumsuz koşul: `unless`
- Edilgen yapı: `be + V3`
- Niteleme: `noun + which/that + clause`
- Zaman sırası: `before`, `after`, `once`

## 5 dakikalık aktif tekrar

1. `Java uses the classpath.` cümlesini passive voice ile yeniden yaz.
2. `If the package does not come first, the file will not compile.` cümlesini
   `unless` kullanarak yeniden kur.
3. Bir constructor'ı `that` relative clause ile İngilizce olarak tanımla.
4. `after` kullanarak field initializer ile constructor arasındaki sırayı anlat.
5. `might` kullanarak bir OCP sorusunda ortaya çıkabilecek olasılığı ifade et.

> **Self-check:** Yapıyı tanımak kadar anlam ilişkisini söylemek de önemlidir:
> amaç mı, neden mi, koşul mu, zaman sırası mı? YDS'de önce bu ilişkiyi bul.
