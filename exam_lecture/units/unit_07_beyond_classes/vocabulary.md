# Unit 07 Vocabulary · Beyond Classes

## Bu belge nasıl kullanılmalı?

Bu sözlüğü [README'deki çalışma rotasının](README.md#işten-sonra-çalışma-rotası)
vocabulary adımında kullan:

1. English terimden Türkçe anlamı active recall ile üret.
2. `Bağlam` ve `Example` satırlarında record, enum, sealed type veya nested
   class kullanımını ayırt et.
3. Related/word-family bilgisini tekrar et; son mini quiz'i kapalı notla çöz.

## A–C

### accessor · noun
- **Türkçe:** erişim method'u, okuyucu method
- **Bağlam:** Record component değerini aynı adlı method ile döndürür.
- **Example:** The compiler generates an accessor for each record component.
- **Çeviri:** Derleyici, açıkça bildirilmemişse her record bileşeni için bir erişim method’u üretir.
- **Related:** access (v./n.), accessible (adj.), mutator (n.)

### analogous · adjective
- **Türkçe:** benzer, karşılaştırılabilir
- **Bağlam:** Bir interface kuralının class'lardaki eşdeğer kuralla aynı mantığı
  izlemesi.
- **Example:** The rule for sealed interfaces is analogous to the class rule.
- **Çeviri:** Sealed interface kuralı, sealed sınıf kuralına benzer.
- **Related:** analogy (n.), similarly (adv.)

### anonymous class · noun phrase
- **Türkçe:** anonim sınıf
- **Bağlam:** Tek expression içinde adı olmadan bildirilen ve oluşturulan class.
- **Example:** An anonymous class cannot extend a final class.
- **Çeviri:** Anonymous class, final class'ı extend edemez.
- **Related:** unnamed, subclass

### arbitrary · adjective
- **Türkçe:** herhangi bir, keyfî seçilmiş
- **Bağlam:** Önceden belirli runtime type'ı bilinmeyen bir instance.
- **Example:** An arbitrary reference may point to several subtype objects.
- **Çeviri:** Bir referans, farklı alt türlerden nesnelere işaret edebilir; aynı anda yalnız bir nesneyi gösterir.
- **Synonym:** unspecified

### boilerplate code · noun phrase
- **Türkçe:** kalıp kod, tekrarlanan standart kod
- **Bağlam:** Record declaration'ında compiler'ın otomatik ürettiği constructor,
  accessor ve temel `Object` method'ları gibi kodlar.
- **Example:** Records remove much of the boilerplate code.
- **Çeviri:** Record'lar kalıp kodun büyük bölümünü ortadan kaldırır.
- **Related:** repetitive code, code generation

### canonical · adjective
- **Türkçe:** standart, bileşenlerle bire bir eşleşen
- **Bağlam:** Record components'ı aynı order/type ile alan constructor.
- **Example:** The canonical constructor initializes every record component.
- **Çeviri:** Canonical constructor, record’un bütün bileşenlerini başlatır.
- **Related:** compact constructor

### compatible · adjective
- **Türkçe:** uyumlu
- **Bağlam:** Tek bir implementation ile birlikte override edilebilen inherited
  method declaration'ları.
- **Example:** The two inherited return types must be compatible.
- **Çeviri:** İki inherited return type uyumlu olmalıdır.
- **Antonym:** incompatible; **Word family:** compatibility (n.)

### component · noun
- **Türkçe:** bileşen
- **Bağlam:** Record header'da bildirilen state öğesi.
- **Example:** Each record component has a corresponding private final field.
- **Çeviri:** Her record component'inin karşılık gelen private final field'ı vardır.
- **Related:** compose (v.), composition (n.)

### compound · verb
- **Türkçe:** ağırlaştırmak, daha karmaşık hâle getirmek
- **Bağlam:** Hidden member'ların parent ve child tarafında değiştirilmesinin
  anlaşılabilirlik sorununu büyütmesi.
- **Example:** Updating both hidden fields compounds the confusion.
- **Çeviri:** Üst ve alt sınıftaki aynı adlı iki alanı da güncellemek kafa karışıklığını artırır.
- **Word family:** compounded (adj./V3), compounding (n./adj.)

### conflict · noun / verb
- **Türkçe:** çakışma / çakışmak
- **Bağlam:** İki interface'in aynı signature ile incompatible default method
  sağlaması.
- **Example:** The class must resolve the inherited default-method conflict.
- **Çeviri:** Class, inherited default-method çakışmasını çözmelidir.
- **Related:** conflicting (adj.), resolve (v.)

### constant-specific class body · noun phrase
- **Türkçe:** sabite özgü class gövdesi
- **Bağlam:** Belirli bir enum constant'ın davranışı override ettiği `{ ... }`.
- **Example:** FISH has a constant-specific class body.
- **Çeviri:** FISH, sabite özgü bir class gövdesine sahiptir.

### cornerstone · noun
- **Türkçe:** temel taşı
- **Bağlam:** Method overriding'in polymorphism için merkezi rolü.
- **Example:** Overriding is a cornerstone of polymorphism.
- **Çeviri:** Overriding, polymorphism'in temel taşıdır.
- **Synonym:** foundation

### covariant · adjective
- **Türkçe:** alt türe doğru uyumlu
- **Bağlam:** Overriding method'un parent return type'ın subtype'ını döndürmesi.
- **Example:** `Float` is a covariant return type for `Number`.
- **Çeviri:** `Float`, `Number` için covariant bir return type'tır.
- **Related:** covariance (n.)

## D–I

### delegate · verb
- **Türkçe:** yönlendirmek, devretmek
- **Bağlam:** Constructor'ın initialization işini `this(...)` ile başka
  constructor'a aktarması.
- **Example:** The overloaded constructor must delegate to another constructor.
- **Çeviri:** Overloaded constructor başka bir constructor'a yönlendirilmelidir.
- **Word family:** delegation (n.)

### discourage · verb
- **Türkçe:** önermemek, caydırmak
- **Bağlam:** Static member'a instance reference üzerinden erişmenin geçerli ama
  kötü bir practice olması.
- **Example:** Java permits this syntax, but good style discourages it.
- **Çeviri:** Java bu syntax'a izin verir; ancak iyi coding style bunu önermez.
- **Antonym:** encourage

### enclosing instance · noun phrase
- **Türkçe:** çevreleyen nesne
- **Bağlam:** Non-static inner class object'ine bağlı outer object.
- **Example:** An inner class requires an enclosing instance.
- **Çeviri:** Inner class, çevreleyen bir instance gerektirir.
- **Related:** outer instance

### explicitly · adverb
- **Türkçe:** açıkça, doğrudan yazarak
- **Bağlam:** Compiler'ın implicit eklemesi yerine modifier veya cast'in kodda
  yazılması.
- **Example:** The concrete class must explicitly declare the method `public`.
- **Çeviri:** Concrete class method'u açıkça `public` bildirmelidir.
- **Antonym:** implicitly; **Word family:** explicit (adj.)

### finite · adjective
- **Türkçe:** sonlu, sınırlı sayıda
- **Bağlam:** Enum'un önceden bilinen sabit bir value kümesi sunması.
- **Example:** An enum represents a finite set of values.
- **Çeviri:** Enum, sonlu bir değer kümesini temsil eder.
- **Antonym:** infinite

### grant · verb
- **Türkçe:** sağlamak, vermek
- **Bağlam:** Reference type değişikliğinin belirli member'lara erişim sağlaması.
- **Example:** A cast may grant access to subtype members.
- **Çeviri:** Bir cast, subtype member'larına erişim sağlayabilir.
- **Synonym:** provide; **Antonym:** deny

### implicit · adjective
- **Türkçe:** örtük, compiler tarafından kendiliğinden uygulanan
- **Bağlam:** Interface member modifier'larının veya record field assignment'ının
  source code'da yazılmadan eklenmesi.
- **Example:** Interface fields have implicit `public static final` modifiers.
- **Çeviri:** Interface field'ları implicit `public static final` modifier'lara
  sahiptir.
- **Antonym:** explicit; **Word family:** implicitly (adv.)

### independently · adverb
- **Türkçe:** birbirinden bağımsız olarak
- **Bağlam:** Multiple-choice seçeneklerinin aynı anda değil ayrı ayrı denenmesi.
- **Example:** Insert each option independently.
- **Çeviri:** Her seçeneği birbirinden bağımsız olarak ekle.
- **Word family:** independent (adj.), independence (n.)

### instantiate · verb
- **Türkçe:** nesne oluşturmak
- **Bağlam:** Bir concrete class constructor'ını çağırarak object oluşturmak.
- **Example:** An interface cannot be instantiated directly.
- **Çeviri:** Interface için doğrudan instance oluşturulamaz.
- **Word family:** instance (n.), instantiation (n.)

## L–N

### latter · adjective / pronoun

- **Türkçe:** sonuncusu; son sözü edilen
- **Bağlam:** “the latter two” önce sayılan türlerin son ikisi olan local ve anonymous class’ı gösterir.
- **Example (özgün çalışma cümlesi):** The latter two types depend on the context.
- **Çeviri:** Son sözü edilen iki tür bağlama bağlıdır.
- **Related:** Antonym: former; latter iki öğeden ikincisi, the latter two listenin son iki öğesidir.
- **Kaynak bağlam:** [latter](bilingual_notes.md#summary--özet).

### maintain · verb
- **Türkçe:** bakımını yapmak, sürdürülebilir tutmak
- **Bağlam:** Hidden member'ların kodun başkaları tarafından bakımını
  zorlaştırması.
- **Example:** Ambiguous member access makes the code hard to maintain.
- **Çeviri:** Belirsiz member erişimi kodun bakımını zorlaştırır.
- **Word family:** maintenance (n.), maintainable (adj.)

## O–R

### override · verb
- **Türkçe:** üst türdeki instance method’u alt türde yeniden gerçekleştirmek
- **Bağlam:** Inherited instance method'a compatible yeni implementation vermek.
- **Example:** Penguin must override the conflicting default method.
- **Çeviri:** Penguin çakışan default method'u override etmelidir.
- **Related:** overriding (n.), dynamic dispatch

### permitted · adjective
- **Türkçe:** izin verilmiş
- **Bağlam:** Sealed type'ın doğrudan subtype olmasına izin verdiği type.
- **Example:** Every permitted subclass chooses a hierarchy modifier.
- **Çeviri:** Her permitted subclass bir hierarchy modifier seçer.
- **Word family:** permit (v./n.), permission (n.)

### reclaim · verb
- **Türkçe:** yeniden kazanmak
- **Bağlam:** Cast ile subtype member erişimini yeniden elde etmek.
- **Example:** A safe downcast can reclaim access to `age`.
- **Çeviri:** Güvenli bir downcast, `age` erişimini yeniden kazandırabilir.
- **Synonym:** regain

### redeclare · verb
- **Türkçe:** yeniden bildirmek
- **Bağlam:** Compiler-generated record member'ını explicit olarak yeniden yazmak.
- **Example:** A record may redeclare its accessor.
- **Çeviri:** Record kendi accessor'ını yeniden bildirebilir.
- **Word family:** declaration (n.)

### resemble · verb
- **Türkçe:** benzemek
- **Bağlam:** Çok sayıda member içeren enum'un tam bir class'a benzemesi.
- **Example:** A complex enum may resemble a full-featured class.
- **Çeviri:** Complex enum, tam özellikli bir class'a benzeyebilir.
- **Related:** resemblance (n.), similar (adj.)

### restrict · verb
- **Türkçe:** kısıtlamak
- **Bağlam:** Sealed type'ın permitted direct subtype kümesini sınırlaması.
- **Example:** A sealed interface restricts its direct implementations.
- **Çeviri:** Sealed interface doğrudan implementation'larını kısıtlar.
- **Synonym:** limit

### retrieve · verb
- **Türkçe:** almak, erişip getirmek
- **Bağlam:** Encapsulated state'in değerini bir method aracılığıyla okumak.
- **Example:** An accessor retrieves the value of a private field.
- **Çeviri:** Accessor, private field'ın değerini alır.
- **Synonym:** obtain; **Related:** retrieval (n.)

### revoke · verb
- **Türkçe:** geri almak, iptal etmek
- **Bağlam:** Kaynaktaki Pluto örneğinde planetary status'un geri alınması.
- **Example:** Pluto had its planetary status revoked.
- **Çeviri:** Plüton'un gezegen statüsü geri alındı.
- **Word family:** revocation (n.)

### rudimentary · adjective
- **Türkçe:** temel, başlangıç düzeyinde
- **Bağlam:** Interface'in önce basit tanımla sunulup yeni member türleriyle
  genişletilmesi.
- **Example:** The chapter starts with a rudimentary interface definition.
- **Çeviri:** Bölüm temel bir interface tanımıyla başlar.
- **Synonym:** basic; **Antonym:** advanced

## S–T

### shallow immutability · noun phrase
- **Türkçe:** yüzeysel değişmezlik
- **Bağlam:** Record component reference'ının final olup target object'in mutable kalması.
- **Example:** Records provide shallow immutability for component references.
- **Çeviri:** Record'lar component reference'ları için shallow immutability sağlar.
- **Related:** defensive copy

### succinctly · adverb
- **Türkçe:** kısa ve öz biçimde
- **Bağlam:** Compact constructor'ın validation ve transformation kodunu az
  syntax ile ifade etmesi.
- **Example:** A compact constructor validates input succinctly.
- **Çeviri:** Compact constructor input'u kısa ve öz biçimde validate eder.
- **Word family:** succinct (adj.), succinctness (n.)

### supply · verb
- **Türkçe:** sağlamak
- **Bağlam:** Enum constant'ın abstract method implementation'ı vermesi.
- **Example:** Every constant must supply the missing implementation.
- **Çeviri:** Her constant eksik implementation'ı sağlamalıdır.
- **Synonym:** provide

### terminator · noun
- **Türkçe:** sonlandırıcı
- **Bağlam:** Member içeren enum'da constant list'i bitiren semicolon.
- **Example:** The enum constant list requires a semicolon terminator.
- **Çeviri:** Enum constant listesi semicolon sonlandırıcısı gerektirir.
- **Word family:** terminate (v.), termination (n.)

### top-level type · noun phrase
- **Türkçe:** üst düzey type
- **Bağlam:** Başka bir type'ın gövdesi içinde nested olarak bildirilmeyen
  class, interface, enum veya record.
- **Example:** The sealed classes are declared as top-level types.
- **Çeviri:** Sealed class'lar top-level type olarak bildirilir.
- **Related:** nested type

## U–Z

### underlying · adjective
- **Türkçe:** altta bulunan, gerçekte kullanılan
- **Bağlam:** Reference type'tan bağımsız olarak memory'de bulunan gerçek runtime
  object.
- **Example:** The underlying object is still a `Lemur`.
- **Çeviri:** Altta bulunan gerçek object hâlâ bir `Lemur`'dur.
- **Related:** runtime object, actual implementation

## Karıştırılan anlamlar ve kapalı kitap hatırlama

| Karşılaştırma | Karar verirken kullan |
|---|---|
| `former` / `latter` | İki öğenin ilki / ikincisi; “the latter two” listenin son iki öğesidir. |
| `implicit` / `explicitly` | İlki sıfat, ikincisi zarf: an implicit modifier / explicitly declare a modifier. |
| `shallow immutability` / deep immutability | Referansın değişmemesi / erişilen nesnelerin durumunun da değişmemesi. |

Aşağıdaki özgün cümleyi Türkçeye çevir; ardından vurgulanan anlam farkını kendi Java örneğine aktar. Cevabı açmadan önce bir tahmin yaz.

> The latter two classes require an instance in this context.

**Kendini kontrol et:** Bu bağlamda son sözü edilen iki sınıf için bir nesne gerekir. Hangi iki sınıf olduğunu önceki cümlede bulmadan çeviriyi tamamlamış sayma.

Dört işaretli terim için 1/3/7/14. günlerde iki yönlü hatırlama yap: English → Türkçe anlam, sonra Türkçe teknik durum → English terim. Anlamını hatırlayıp örnek kuramadığın terimi “öğrendim” diye işaretleme.

## Mini quiz

1. `enclosing instance` hangi nested class türü için gereklidir?
2. `delegate` record constructor bağlamında ne anlama gelir?
3. `independently` bir multiple-choice yönergesini nasıl değiştirir?
4. `redeclare` ile `override` arasındaki temel fark nedir?

## Cevaplar

1. Non-static inner class için.
2. `this(...)` ile başka bir constructor'a yönlendirmek.
3. Seçeneklerin birlikte değil, tek tek değerlendirilmesini ister.
4. Redeclare member'ı explicit yeniden bildirir; override inherited instance
   method'a polymorphic implementation verir.

## 5 dakikalık active recall

1. `permitted`, `restrict` ve `subtype` ile sealed hierarchy'yi sözlü açıkla.
2. `canonical`, `component` ve `delegate` ile record constructor kuralını anlat.
3. `enclosing instance` ile anonymous/inner class farkını karşılaştır.
4. `shallow immutability` ve defensive copy arasındaki bağlantıyı açıkla.
