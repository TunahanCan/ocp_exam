# Unit 05 Vocabulary · Methods

## Bu belge nasıl kullanılmalı?

Bu sözlüğü [README'deki oturum rotasının](README.md#çalışanlar-için-2530-dakikalık-çalışma-rotası)
dil çalışması bölümünde kısa active recall kartları gibi kullan:

1. **Recall:** Terimin Türkçe ve bağlam satırlarını kapat; anlamını ve sözcük
   türünü söyle.
2. **Context:** Cevabı açıp terimin method declaration, access veya invocation
   bağlamındaki özel anlamını kontrol et.
3. **Example:** İngilizce örneği önce kendin çevir; ardından verilen doğal
   çeviriyle karşılaştır ve terimle yeni bir Java cümlesi kur.
4. **Quiz:** Oturum sonunda [Mini quiz](#mini-quiz) ve
   [5 dakikalık active recall](#5-dakikalık-active-recall) görevlerini notlar
   kapalıyken tamamla.

> **Hızlı hedef:** Bir oturumda bütün liste yerine beş terim seç. Terimi yalnız
> tanımak değil, `argument`–`parameter` veya `reassign`–`mutation` gibi yakın
> kavramlardan ayırabilmek başarı ölçütüdür.

## A–I

### access modifier · noun phrase
- **Türkçe:** erişim belirleyici
- **Bağlam:** Bir member'a hangi class ve package'lerden erişilebileceğini belirleyen `private`, package, `protected` veya `public` düzeyi.
- **Example:** An access modifier determines where a method can be referenced.
- **Çeviri:** Access modifier, bir method'a nereden başvurulabileceğini belirler.
- **Related:** access control, visibility

### applicability · noun
- **Türkçe:** uygulanabilirlik
- **Bağlam:** Bir overload'ın verilen argument'ları kabul edip edememesi.
- **Example:** The compiler checks overload applicability first.
- **Çeviri:** Compiler önce overload uygulanabilirliğini denetler.
- **Word family:** applicable (adj.), apply (v.)

### argument · noun
- **Türkçe:** argument, çağrıda geçirilen değer
- **Bağlam:** Method invocation sırasında parameter'a aktarılan value.
- **Example:** The caller supplies an argument for each required parameter.
- **Çeviri:** Caller, gerekli her parameter için bir argument sağlar.
- **Related:** parameter; **synonym in general English:** reason

### assignable · adjective
- **Türkçe:** atanabilir
- **Bağlam:** Bir value'nun conversion kurallarına göre hedef type'ta saklanabilmesi.
- **Example:** The returned value must be assignable to the return type.
- **Çeviri:** Döndürülen value, return type'a atanabilir olmalıdır.
- **Word family:** assign (v.), assignment (n.)

### autoboxing · noun
- **Türkçe:** primitive'den wrapper'a otomatik dönüşüm
- **Bağlam:** Örneğin `int` value'nun compiler tarafından `Integer` object'ine dönüştürülmesi.
- **Example:** Autoboxing converts an int to an Integer when needed.
- **Çeviri:** Autoboxing gerektiğinde `int`i `Integer`a dönüştürür.
- **Antonym:** unboxing

### backward compatibility · noun phrase
- **Türkçe:** geriye dönük uyumluluk
- **Bağlam:** Eski Java code'unun yeni dil özellikleri eklendikten sonra da aynı overload'ı seçmesi.
- **Example:** The overload phases preserve backward compatibility.
- **Çeviri:** Overload aşamaları geriye dönük uyumluluğu korur.
- **Related:** compatible (adj.), compatibility (n.)

### broader · adjective
- **Türkçe:** daha geniş
- **Bağlam:** Access veya checked exception kapsamının genişliği.
- **Example:** Public access is broader than protected access.
- **Çeviri:** Public access, protected access'ten daha geniştir.
- **Antonym:** narrower

### caller · noun
- **Türkçe:** çağıran kod / çağrıyı yapan taraf
- **Bağlam:** Bir method'u çağırıp argument sağlayan class, method veya ifade.
- **Example:** The caller provides an int value in parentheses.
- **Çeviri:** Çağıran kod parantez içinde bir int value sağlar.
- **Word family:** call (v./n.), callable (adj.)

### clause · noun
- **Türkçe:** cümlecik; teknik bağlamda bildirim bölümü
- **Bağlam:** Kaynakta `throws` ile başlayan exception list bölümü için de kullanılır.
- **Example:** Exception types are separated by commas in this clause.
- **Çeviri:** Bu clause içinde exception type'ları virgülle ayrılır.
- **Related:** phrase, statement

### constant · noun
- **Türkçe:** sabit
- **Bağlam:** Genellikle uppercase ve underscore convention'ıyla adlandırılan `static final` variable.
- **Example:** A constant cannot be reassigned after initialization.
- **Çeviri:** Bir constant initialization'dan sonra yeniden atanamaz.
- **Word family:** constant (adj.), constantly (adv.)

### declaration · noun
- **Türkçe:** bildirim
- **Bağlam:** Method'un modifier, return type, name, parameter, exception list ve body öğelerinin tamamı.
- **Example:** The method declaration includes more than its signature.
- **Çeviri:** Method declaration, signature'dan daha fazla öğe içerir.
- **Word family:** declare (v.)

### effectively final · adjective phrase
- **Türkçe:** effectively final / fiilen `final`
- **Bağlam:** `final` yazılmamış fakat initialize edildikten sonra değişmeyen local variable.
- **Example:** The captured variable must be effectively final.
- **Çeviri:** Yakalanan variable effectively final olmalıdır.
- **Related:** final, reassignment

### exception list · noun phrase
- **Türkçe:** exception listesi
- **Bağlam:** Method declaration'da `throws` sonrasında yer alan, virgülle ayrılmış exception type'ları.
- **Example:** The exception list follows the parameter list.
- **Çeviri:** Exception list, parameter list'ten sonra gelir.
- **Related:** throw, handle

### explicitly · adverb
- **Türkçe:** açıkça, doğrudan belirtilerek
- **Bağlam:** Compiler'ın yaptığı implicit işlem yerine developer'ın cast veya `null` argument'ı açıkça yazması.
- **Example:** You can explicitly pass null to a varargs parameter.
- **Çeviri:** Varargs parameter'a açıkça `null` geçebilirsiniz.
- **Antonym:** implicitly

### fixed arity · adjective phrase
- **Türkçe:** fixed arity / sabit sayıda parameter'lı
- **Bağlam:** Varargs expansion kullanmadan belirli sayıda argument kabul eden
  method invocation/declaration.
- **Example:** A varargs method can also be invoked as a fixed-arity method.
- **Çeviri:** Varargs bildirimi olan bir method, fixed-arity method olarak da çağrılabilir.
- **Antonym:** variable arity

### immutable · adjective
- **Türkçe:** değiştirilemez
- **Bağlam:** Oluşturulduktan sonra internal state'i değişmeyen `String` gibi object type'ları.
- **Example:** Calling substring does not modify an immutable String.
- **Çeviri:** `substring()` çağırmak immutable bir `String`i değiştirmez.
- **Word family:** immutability (n.); **antonym:** mutable

### implicitly · adverb
- **Türkçe:** örtük biçimde, açıkça yazılmadan
- **Bağlam:** `int`ten `long`a widening gibi compiler'ın otomatik yaptığı conversion.
- **Example:** An int can be implicitly converted to a long.
- **Çeviri:** Bir `int`, örtük biçimde `long`a dönüştürülebilir.
- **Antonym:** explicitly

### independently · adverb
- **Türkçe:** birbirinden bağımsız olarak
- **Bağlam:** Her code snippet'in diğerlerinden ayrı değerlendirilmesi.
- **Example:** Insert each assignment independently.
- **Çeviri:** Her assignment'ı birbirinden bağımsız ekle.
- **Word family:** independent (adj.)

### instantiate · verb
- **Türkçe:** instance/object oluşturmak
- **Bağlam:** Constructor çağrısıyla bir class'tan yeni object üretmek.
- **Example:** A static helper does not require the caller to instantiate the class.
- **Çeviri:** `static` helper, caller'ın class'tan object oluşturmasını gerektirmez.
- **Word family:** instance (n.), instantiation (n.)

### invoke · verb
- **Türkçe:** çağırmak, çalıştırmak
- **Bağlam:** Bir method veya constructor call gerçekleştirmek.
- **Example:** The compiler selects a method before the JVM invokes it.
- **Çeviri:** JVM method'u çağırmadan önce compiler onu seçer.
- **Word family:** invocation (n.)

<!-- page-break -->

## J–O

### lenient · adjective

- **Türkçe:** daha az kısıtlayıcı, esnek
- **Teknik bağlam:** Erişim kurallarının ne kadar geniş izin verdiğini karşılaştırır.
- **Example:** Protected access is more lenient than package access.
- **Çeviri:** Protected erişim, paket erişiminden daha az kısıtlayıcıdır.
- **Word family / karşılaştırma:** leniency (n.); karşıt: restrictive, strict
- **Kaynak bağlam:** [İlgili ana not](bilingual_notes.md#applying-access-modifiers).

### modifier · noun
- **Türkçe:** modifier, belirleyici
- **Bağlam:** Declaration'ın access veya davranışını değiştiren `public`, `static`, `final` gibi keyword.
- **Example:** The final modifier prevents reassignment.
- **Çeviri:** `final` modifier yeniden atamayı engeller.
- **Word family:** modify (v.), modification (n.)

### mutation · noun
- **Türkçe:** object state'ini değiştirme
- **Bağlam:** Reference'ı yeniden atamadan, işaret edilen mutable object veya array'in içeriğini değiştirmek.
- **Example:** A final reference does not prevent object mutation.
- **Çeviri:** `final` reference, object mutation'ını engellemez.
- **Word family:** mutate (v.), mutable (adj.)

### omit · verb
- **Türkçe:** çıkarmak, yazmadan bırakmak
- **Bağlam:** Package access için access modifier yazılmaması veya abstract
  method'da body bulunmaması.
- **Example:** Omit the access modifier to use package access.
- **Çeviri:** Package access kullanmak için access modifier'ı yazma.
- **Word family:** omission (n.); **synonym:** leave out

### overload · verb / noun
- **Türkçe:** overload etmek; aynı adlı method'un farklı parameter listesi olan sürümünü tanımlamak
- **Bağlam:** Aynı class'ta aynı method name'i farklı parameter list'lerle bildirmek.
- **Example:** You cannot overload a method by changing only its return type.
- **Çeviri:** Yalnızca return type'ı değiştirerek bir method'u overload edemezsiniz.
- **Related:** overloading; **contrast:** override

<!-- page-break -->

## P–S

### parameter · noun
- **Türkçe:** parametre; metot bildirimindeki girdi değişkeni
- **Bağlam:** Method declaration içinde argument value'sunu alan local variable.
- **Example:** A varargs parameter must appear last.
- **Çeviri:** Varargs parameter son sırada bulunmalıdır.
- **Related:** argument, parameter list

### pass-by-value · noun phrase
- **Türkçe:** değere göre aktarım
- **Bağlam:** Java'nın argument value'sunun kopyasını parameter'a vermesi.
- **Example:** Java uses pass-by-value for object references too.
- **Çeviri:** Java object reference'ları için de pass-by-value kullanır.
- **Related:** parameter, argument

### reassign · verb
- **Türkçe:** yeniden atamak
- **Bağlam:** Bir parameter/reference variable'ı başka object'e yönlendirmek.
- **Example:** Reassigning the parameter does not change the caller.
- **Çeviri:** Parameter'ı yeniden atamak caller'ı değiştirmez.
- **Word family:** reassignment (n.)

### receiver · noun
- **Türkçe:** çağrıyı alan object/reference
- **Bağlam:** Instance member'a hangi object expression üzerinden erişildiği.
- **Example:** Protected access checks the receiver type across packages.
- **Çeviri:** Protected access package'ler arasında receiver type'ını denetler.
- **Related:** target, reference

### respectively · adverb
- **Türkçe:** sırasıyla
- **Bağlam:** İki veya daha fazla öğeyi aynı sıradaki sonuçlarla eşleştirme.
- **Example:** The calls select int and Object, respectively.
- **Çeviri:** Çağrılar sırasıyla int ve Object'i seçer.
- **Related phrase:** in the same order

### restrictive · adjective
- **Türkçe:** kısıtlayıcı
- **Bağlam:** Access düzeylerinin `private`dan `public`e doğru karşılaştırılması.
- **Example:** Private is the most restrictive access level.
- **Çeviri:** `private`, en kısıtlayıcı access düzeyidir.
- **Word family:** restrict (v.), restriction (n.); **antonym:** permissive

### signature · noun
- **Türkçe:** imza
- **Bağlam:** Method name ve parameter type listesinin birleşimi.
- **Example:** Return type is not part of the method signature.
- **Çeviri:** Return type method signature'ın parçası değildir.
- **Related:** declaration, overload

### specifier · noun
- **Türkçe:** belirteç
- **Bağlam:** Method declaration'daki `static`, `abstract`, `final` gibi optional keyword'ler.
- **Example:** Optional specifiers must appear before the return type.
- **Çeviri:** Optional specifier'lar return type'tan önce gelmelidir.
- **Word family:** specify (v.), specification (n.)

### stand-alone · adjective
- **Türkçe:** tek başına, ayrı ayrı yazılan
- **Bağlam:** Bir array yerine varargs call'a doğrudan geçirilen ayrı value'lar.
- **Example:** Only the varargs version accepts stand-alone values.
- **Çeviri:** Stand-alone value'ları yalnızca varargs sürümü kabul eder.
- **Synonym:** separate

### supplied · adjective
- **Türkçe:** sağlanan, verilen
- **Bağlam:** Method call'a geçirilen argument veya kaynak kod.
- **Example:** The supplied argument is a short value.
- **Çeviri:** Verilen argument short value'dur.
- **Word family:** supply (v./n.)

<!-- page-break -->

## U–W

### unboxing · noun
- **Türkçe:** wrapper'dan primitive'e dönüşüm
- **Bağlam:** `Integer` gibi wrapper value'nun `int` olarak kullanılması.
- **Example:** Unboxing a null reference throws a NullPointerException.
- **Çeviri:** `null` reference'ı unbox etmek `NullPointerException` fırlatır.
- **Antonym:** boxing

### varargs · noun / adjective
- **Türkçe:** değişken sayıda argument
- **Bağlam:** Son parameter'ın `Type... name` biçiminde array olarak alınması.
- **Example:** Varargs must be the last parameter.
- **Çeviri:** Varargs son parameter olmalıdır.
- **Related:** variable arity, array

### widen · verb
- **Türkçe:** daha geniş türe dönüştürmek
- **Bağlam:** Primitive veya reference value'yu compatible üst/geniş type'a taşımak.
- **Example:** A short can widen to int.
- **Çeviri:** `short`, `int`e widen edilebilir.
- **Word family:** widening (n./adj.); **antonym:** narrow

### wildcard · noun
- **Türkçe:** wildcard, joker karakter
- **Bağlam:** Import statement'ta bir package veya class'ın uygun bütün member'larını temsil eden `*`.
- **Example:** A static wildcard import can import accessible static members.
- **Çeviri:** Static wildcard import erişilebilir `static` member'ları import edebilir.
- **Related:** import, asterisk

## Önce anlam farkını geri çağır

Her oturumda en fazla beş kart seç. Türkçe anlamı kapatıp örneği sesli çevir;
sonra İngilizce terimi kapatıp Türkçeden geri çağır. **0:** hatırlamadım,
**1:** ipucuyla, **2:** örnek kurarak hatırladım biçiminde işaretle. 0/1 alan
kartları ertesi gün, 2 alanları 3/7/14 gün rotasında yeniden dene. Bu puanlar
kişisel takip içindir; hazır bir sınav puanı değildir.

`parameter` bildirimdeki değişken; `argument` çağrıda verilen değerdir. `reassign` oku başka nesneye yöneltir; `mutation` okun gösterdiği nesnenin içeriğini değiştirir.

**Kontrol:** Bu ayrımlardan birini İngilizce iki cümleyle açıkla; yalnız Türkçe karşılığı söylemekle yetinme.

## Mini quiz

| Soru |
|---|
| 1. Method signature hangi iki öğeden oluşur? |
| 2. Reassignment ile mutation arasındaki farkı açıkla. |
| 3. `broader` kelimesini access modifier cümlesinde kullan. |
| 4. Varargs için konum kuralını yaz. |

## Cevaplar

| Cevap |
|---|
| 1. Method name ve parameter type listesi. |
| 2. Reassignment reference variable'ı değiştirir; mutation object state'ini. |
| 3. *Public access is broader than protected access.* |
| 4. Varargs parameter listesinde son sırada olmalıdır. |

## 5 dakikalık active recall

| Hatırlama görevi |
|---|
| 1. `applicability`, `invoke` ve `signature` kelimeleriyle overload seçimini anlat. |
| 2. `receiver` terimini cross-package `protected` access bağlamında tanımla. |
| 3. `pass-by-value` ile `reassign` arasındaki ilişkiyi object reference üzerinden açıkla. |
| 4. `unboxing`, `null` ve runtime exception kelimeleriyle bir uyarı cümlesi yaz. |
