# Unit 06 Vocabulary · Class Design

## Bu belge nasıl kullanılmalı?

Bu sözlüğü [README'deki çalışma rotasının](README.md#işten-sonra-çalışma-rotası)
vocabulary adımında kullan:

1. Terimin Türkçe karşılığını kapatıp English başlıktan hatırlamaya çalış.
2. `Bağlam` ve `Example` satırlarıyla kelimenin inheritance/class-design
   anlamını doğrula.
3. Related/antonym bilgisini sesli tekrar et; son mini quiz'i notlara bakmadan
   çöz.

## A–I

### abstract · adjective
- **Türkçe:** soyut; doğrudan instantiate edilemeyen
- **Bağlam:** Implementation'ı concrete subclass'a bırakabilen class veya
  body'siz instance method.
- **Example:** An abstract method ends with a semicolon and has no body.
- **Çeviri:** Abstract method semicolon ile biter ve body'si yoktur.
- **Antonym:** concrete; **word family:** abstraction (n.)

### ancestor · noun
- **Türkçe:** ata, üst tür
- **Bağlam:** Inheritance zincirinde bir class'ın üstünde bulunan superclass.
- **Example:** Object is an ancestor of every class.
- **Çeviri:** Object her class'ın atasıdır.
- **Antonym:** descendant

### broader · adjective
- **Türkçe:** daha geniş
- **Bağlam:** Access level veya checked exception hierarchy'sinde daha geniş
  kapsamı anlatır.
- **Example:** An overriding method cannot declare a broader checked exception.
- **Çeviri:** Üst sınıftaki method’u override eden method, daha geniş kapsamlı bir checked exception bildiremez.
- **Antonym:** narrower; **word family:** broaden (v.)

### checked exception · noun phrase
- **Türkçe:** kontrol edilen exception
- **Bağlam:** Override declaration'ında parent method'dan daha broad biçimde
  eklenemeyen exception türü.
- **Example:** An overriding method may declare a narrower checked exception.
- **Çeviri:** Overriding method daha dar bir checked exception bildirebilir.
- **Related:** throws clause; **antonym:** unchecked exception

### concrete · adjective
- **Türkçe:** somut; instantiate edilebilir
- **Bağlam:** `abstract` olmayan ve inherited bütün abstract method'ları
  implement eden class.
- **Example:** The first concrete subclass must implement every inherited abstract method.
- **Çeviri:** İlk somut alt sınıf, kalıtımla aldığı bütün abstract method yükümlülüklerini yerine getirmelidir.
- **Antonym:** abstract

### constructor chaining · noun phrase
- **Türkçe:** constructor zincirleme
- **Bağlam:** Bir constructor'ın `this()` veya `super()` ile başka constructor'a
  delegation yapması.
- **Example:** Constructor chaining eventually reaches `Object`.
- **Çeviri:** Constructor chaining sonunda `Object`e ulaşır.
- **Related:** delegation, initialization order

### covariant · adjective
- **Türkçe:** alt türle uyumlu
- **Bağlam:** Overridden method return type'ının parent return type'ın subtype'ı olması.
- **Example:** Macaw is a covariant return type for Bird.
- **Çeviri:** Macaw, Bird için covariant return type'tır.
- **Related:** subtype, override

### default constructor · noun phrase
- **Türkçe:** varsayılan constructor
- **Bağlam:** Class'ta hiçbir constructor yoksa compiler'ın eklediği
  no-argument constructor.
- **Example:** Declaring any constructor prevents the default constructor.
- **Çeviri:** Herhangi bir constructor bildirmek default constructor'ın eklenmesini önler.
- **Related:** compiler-provided, no-argument constructor

### defensive copy · noun phrase
- **Türkçe:** koruyucu kopya
- **Bağlam:** Mutable internal data'nın caller tarafından değişmesini önlemek.
- **Example:** Return a defensive copy of the mutable list.
- **Çeviri:** Değiştirilebilir listenin koruyucu bir kopyasını döndür.
- **Related:** immutability, encapsulation

### descendant · noun
- **Türkçe:** alt tür
- **Bağlam:** Inheritance ağacında başka bir class'tan türeyen subclass.
- **Example:** Rhinoceros is a descendant of Mammal.
- **Çeviri:** Rhinoceros, Mammal'ın alt tür'ıdır.
- **Antonym:** ancestor

### directly · adverb
- **Türkçe:** doğrudan
- **Bağlam:** Arada type olmadan immediate superclass/interface ilişkisi.
- **Example:** A class directly extends one class.
- **Çeviri:** Bir class doğrudan bir class'ı extend eder.
- **Word family:** direct (adj.)

### established · adjective
- **Türkçe:** belirlenmiş
- **Bağlam:** Constructor call'ları izlenerek bulunan execution pathway.
- **Example:** Execute constructors using the established order.
- **Çeviri:** Constructor'ları belirlenmiş sırayla çalıştır.
- **Word family:** establish (v.)

### explicit · adjective

- **Türkçe:** açık, açıkça yazılmış
- **Bağlam:** `super(1)` gibi programcı tarafından yazılan constructor çağrısı.
- **Example (özgün çalışma cümlesi):** An explicit constructor call must come first.
- **Çeviri:** Açıkça yazılan constructor çağrısı ilk ifade olmalıdır.
- **Related:** Antonym: implicit; word family: explicitly.
- **Kaynak bağlam:** [explicit](bilingual_notes.md#understanding-compiler-enhancements).

### fulfill · verb
- **Türkçe:** karşılamak, yerine getirmek
- **Bağlam:** Concrete class'ın abstract contract'ı implement etmesi.
- **Example:** The class fulfills every abstract method contract.
- **Çeviri:** Class her abstract method contract'ını karşılar.
- **Synonym:** satisfy

### hide · verb
- **Türkçe:** gizlemek
- **Bağlam:** Subclass static member'ın parent'taki aynı adlı static member'ı saklaması.
- **Example:** Static methods are hidden, not overridden.
- **Çeviri:** Static method’lar override edilmez; aynı imzalı alt sınıf method’u üst sınıftakini gizler (hiding).
- **Word family:** hiding (n.)

### immutable · adjective
- **Türkçe:** değiştirilemez
- **Bağlam:** Oluşturulduktan sonra dışarıdan gözlenebilen durumu değişmeyen nesne tasarımı.
- **Example:** A defensive copy protects an immutable object from aliasing.
- **Çeviri:** Koruyucu kopya, değişmez nesneyi aynı mutable veriye başka referanslardan erişilmesi riskine karşı korur.
- **Antonym:** mutable; **word family:** immutability (n.)

### implicit · adjective
- **Türkçe:** örtük, açıkça yazılmadan eklenen
- **Bağlam:** Compiler'ın constructor başına `super()` eklemesi.
- **Example:** A constructor may contain an implicit call to `super()`.
- **Çeviri:** Constructor, açıkça yazılmamış bir `super()` çağrısı içerebilir.
- **Antonym:** explicit

### inherited · adjective
- **Türkçe:** kalıtımla alınmış
- **Bağlam:** Parent type'tan child type'a geçen accessible member.
- **Example:** A concrete class must implement inherited abstract methods.
- **Çeviri:** Concrete class inherited abstract method'ları implement etmelidir.
- **Word family:** inherit (v.), inheritance (n.)

### initialization order · noun phrase
- **Türkçe:** başlatma sırası
- **Bağlam:** Static ve instance component'lerin parent'tan child'a çalışma
  düzeni.
- **Example:** Trace the initialization order before computing the output.
- **Çeviri:** Çıktıyı hesaplamadan önce initialization order'ı izle.
- **Related:** initializer, constructor pathway

### invariant · noun
- **Türkçe:** değişmez koşul
- **Bağlam:** Bir object'in geçerli olduğu sürece her zaman doğru kalması gereken
  durum kuralı.
- **Example:** The list must contain an element to preserve the invariant.
- **Çeviri:** Değişmez koşulu korumak için liste en az bir öğe içermelidir.
- **Related:** validation, state

## M–S

### multiple inheritance · noun phrase
- **Türkçe:** çoklu kalıtım
- **Bağlam:** Bir class'ın birden fazla direct superclass'a sahip olması.
- **Example:** Java classes do not support multiple inheritance.
- **Çeviri:** Java class'ları multiple inheritance desteklemez.
- **Antonym:** single inheritance

### narrower · adjective
- **Türkçe:** daha dar
- **Bağlam:** Covariant return type veya azaltılmış checked exception kümesi.
- **Example:** An overriding method may return a narrower reference type.
- **Çeviri:** Overriding method daha dar bir reference type döndürebilir.
- **Antonym:** broader

### override · verb
- **Türkçe:** inherited instance method'u geçersiz kılmak
- **Bağlam:** Same signature, compatible access/exception ve covariant return
  kurallarıyla child implementation sağlamak.
- **Example:** A `final` method cannot be overridden.
- **Çeviri:** `final` method override edilemez.
- **Word family:** overriding (n.); **contrast:** overload, hide

### pathway · noun
- **Türkçe:** izlenen yol
- **Bağlam:** Constructor delegation zincirindeki call sırası.
- **Example:** Trace the constructor pathway upward first.
- **Çeviri:** Önce constructor yolunu yukarı doğru izle.
- **Synonym:** route, path

### progressively · adverb
- **Türkçe:** giderek, aşamalı biçimde
- **Bağlam:** Override return type/access'ın inheritance boyunca değişmesi.
- **Example:** Return types may become progressively narrower.
- **Çeviri:** Dönüş türleri giderek daha özel alt türlere daralabilir; aynı kalmaları da geçerlidir.
- **Word family:** progressive (adj.)

### redeclare · verb
- **Türkçe:** yeniden bildirmek
- **Bağlam:** Inherit edilmeyen `private` parent method'dan bağımsız, aynı adlı
  child method tanımlamak.
- **Example:** A subclass may redeclare a private parent method.
- **Çeviri:** Subclass private parent method'u yeniden bildirebilir.
- **Word family:** redeclaration (n.)

### restrictive · adjective

- **Türkçe:** kısıtlayıcı
- **Bağlam:** Alt sınıfın erişim düzeyini daraltması.
- **Example (özgün çalışma cümlesi):** Private access is more restrictive than protected access.
- **Çeviri:** Private erişim, protected erişimden daha kısıtlayıcıdır.
- **Related:** Word family: restrict, restriction; contrast: permissive.
- **Kaynak bağlam:** [restrictive](bilingual_notes.md#overriding-a-method).

### single inheritance · noun phrase
- **Türkçe:** tekli kalıtım
- **Bağlam:** Her Java class'ının yalnızca bir direct superclass'a sahip olması.
- **Example:** Java class design follows single inheritance.
- **Çeviri:** Java class tasarımı single inheritance modelini izler.
- **Antonym:** multiple inheritance

### slew · noun
- **Türkçe:** çok sayıda, geniş bir küme
- **Bağlam:** Inheritance ile erişilebilen çok sayıdaki member'ı anlatan informal
  fakat okuma parçalarında yararlı bir kullanım.
- **Example:** A subclass may inherit a slew of members.
- **Çeviri:** Bir subclass çok sayıda member inherit edebilir.
- **Synonym:** a large number, multitude

### subtype · noun
- **Türkçe:** alt tür
- **Bağlam:** Başka bir type'ın yerine kullanılabilen daha özel type.
- **Example:** A class is a subtype of its implemented interface.
- **Çeviri:** Class implement ettiği interface'in subtype'ıdır.
- **Antonym:** supertype

## T–Z

### wrapper method · noun phrase
- **Türkçe:** sarmalayıcı method
- **Bağlam:** Internal mutable object'i doğrudan vermeden sınırlı işlemleri
  delegate eden method.
- **Example:** A wrapper method can expose the list size safely.
- **Çeviri:** Wrapper method list boyutunu güvenli biçimde gösterebilir.
- **Related:** delegate method, encapsulation

## Karıştırılan anlamlar ve kapalı kitap hatırlama

| Karşılaştırma | Karar verirken kullan |
|---|---|
| `implicit` / `explicit` | Örtük / açıkça yazılmış; ikisi de gerçek constructor çağrısıdır. |
| `broader` / `narrower` | Daha geniş / daha dar; access genişleyebilirken checked exception kapsamı genişleyemez. |
| `immutable` / `invariant` | İlki nesnenin değişmezliğini, ikincisi korunması gereken koşulu anlatır. |

Aşağıdaki özgün cümleyi Türkçeye çevir; ardından vurgulanan anlam farkını kendi Java örneğine aktar. Cevabı açmadan önce bir tahmin yaz.

> The access becomes more restrictive.

**Kendini kontrol et:** Erişim daha kısıtlayıcı hâle gelir. `more restrictive`, daha erişilebilir demek değildir.

Dört işaretli terim için 1/3/7/14. günlerde iki yönlü hatırlama yap: English → Türkçe anlam, sonra Türkçe teknik durum → English terim. Anlamını hatırlayıp örnek kuramadığın terimi “öğrendim” diye işaretleme.

## Mini quiz

1. Override'da covariant return ne demektir?
2. Static method için `hide` neden kullanılır?
3. Defensive copy hangi riski önler?
4. Multiple inheritance'ı tanımla.
5. Default constructor hangi koşulda eklenir?
6. Invariant ile immutable arasındaki ilişki nedir?

## Cevaplar

1. Child return type, parent return type'ın subtype'ıdır.
2. Static dispatch runtime polymorphism kullanmaz.
3. Caller'ın internal mutable state'i değiştirmesini.
4. Bir class'ın multiple direct superclass'a sahip olmasıdır.
5. Class'ta hiçbir constructor bildirilmediğinde compiler tarafından eklenir.
6. Invariant object'in geçerli state kuralıdır; immutable tasarım creation
   sonrasında bu state'in dışarıdan değiştirilmesini engeller.

## 5 dakikalık active recall

1. `implicit`, `pathway` ve `initialization order` ile constructor zincirini anlat.
2. `covariant`, `narrower` ve `inherited` terimleriyle valid override tanımla.
3. `hide` ve `override` farkını selection time üzerinden açıkla.
4. `defensive copy` kullanmadan immutable class tasarlamanın riskini söyle.
