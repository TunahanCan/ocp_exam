# Unit 08 Vocabulary · Lambdas and Functional Interfaces

Bu sözlük, [çift dilli ana notta](bilingual_notes.md) geçen lambda ve functional
interface bağlamındaki teknik/YDS değeri yüksek sözcükleri alfabetik sırayla
toplar.

## A–C

### ambiguous · adjective
- **Türkçe:** belirsiz, birden fazla yoruma açık
- **Bağlam:** Target type'ın overloaded method'lardan tek birini seçememesi.
- **Example:** Multiple matching overloads can make the method reference ambiguous.
- **Çeviri:** Birden fazla eşleşen overload, method reference'ı belirsiz hâle
  getirebilir.
- **Related:** ambiguity (n.), unambiguous (adj.); **Antonym:** clear

### annotation · noun
- **Türkçe:** ek açıklama, annotation
- **Bağlam:** `@FunctionalInterface`, compiler'a interface'in SAM kuralına
  uymasının amaçlandığını bildirir.
- **Example:** The annotation is optional, but it enables a compiler check.
- **Çeviri:** Annotation optional'dır; fakat compiler kontrolünü etkinleştirir.
- **Related:** annotate (v.), annotated (adj.)

### arrow operator · noun phrase
- **Türkçe:** ok operator'ü
- **Bağlam:** Lambda parameter listesi ile body'yi ayıran `->`.
- **Example:** The arrow operator separates the parameters from the body.
- **Çeviri:** Arrow operator parameter'ları body'den ayırır.
- **Related:** lambda syntax

### capture · verb / noun
- **Türkçe:** yakalamak / yakalama
- **Bağlam:** Lambda'nın çevreleyen scope'taki local variable'a reference vermesi.
- **Example:** A lambda may capture an effectively final local variable.
- **Çeviri:** Lambda, effectively final bir local variable'ı capture edebilir.
- **Related:** captured (adj.), variable capture

### closure · noun
- **Türkçe:** closure, çevresindeki variable'ları taşıyan function yapısı
- **Bağlam:** Başka dillerde lambda benzeri yapılara verilen ad.
- **Example:** Java lambdas may be familiar to developers who have used closures.
- **Çeviri:** Java lambda'ları closure kullanmış geliştiricilere tanıdık gelebilir.
- **Related:** lambda expression

### compact · adjective
- **Türkçe:** kısa ve yoğun, kompakt
- **Bağlam:** Method reference'ın eşdeğer lambda'ya göre daha kısa syntax sunması.
- **Example:** A method reference is a compact form of a lambda.
- **Çeviri:** Method reference, lambda'nın compact bir biçimidir.
- **Antonym:** verbose; **Word family:** compactness (n.)

### convenience method · noun phrase
- **Türkçe:** kolaylık sağlayan yardımcı method
- **Bağlam:** `andThen()`, `compose()`, `and()`, `or()` ve `negate()` gibi
  default method'lar.
- **Example:** Convenience methods combine existing predicates.
- **Çeviri:** Convenience method'lar mevcut predicate'leri birleştirir.
- **Related:** convenient (adj.), facilitate (v.)

### criteria · plural noun
- **Türkçe:** ölçütler, kriterler
- **Bağlam:** Listedeki hayvanların hangi koşulla seçileceğini belirleyen kurallar.
- **Example:** The program prints animals according to specific criteria.
- **Çeviri:** Program hayvanları belirli ölçütlere göre yazdırır.
- **Singular:** criterion

## D–F

### declaratively · adverb
- **Türkçe:** bildirime dayalı biçimde, ne istendiğini söyleyerek
- **Bağlam:** State ve loop adımlarından çok istenen sonucu ifade eden functional
  programming yaklaşımı.
- **Example:** Functional code often describes the task declaratively.
- **Çeviri:** Functional kod çoğu zaman görevi declarative biçimde açıklar.
- **Related:** declarative (adj.), declaration (n.); **Contrast:** imperatively

### deferred execution · noun phrase
- **Türkçe:** ertelenmiş yürütme
- **Bağlam:** Lambda kodunun şimdi tanımlanıp invocation method çağrıldığında
  daha sonra çalışması.
- **Example:** Lambdas support deferred execution of a block of code.
- **Çeviri:** Lambda'lar bir kod bloğunun deferred execution'ını destekler.
- **Related:** defer (v.), immediate execution

### determine · verb
- **Türkçe:** belirlemek, saptamak
- **Bağlam:** Context'in lambda parameter type'ını veya overload'u seçmesi.
- **Example:** The target type determines the lambda parameter types.
- **Çeviri:** Target type, lambda parameter type'larını belirler.
- **Related:** determination (n.), determine whether

### distinct · adjective
- **Türkçe:** farklı, ayrı
- **Bağlam:** `Function<T,R>` içinde input type'tan farklı bir return type
  gerekebilmesi.
- **Example:** Use `R` when a distinct return type is needed.
- **Çeviri:** Farklı bir return type gerektiğinde `R` kullanın.
- **Synonym:** separate; **Antonym:** identical

### effectively final · adjective phrase
- **Türkçe:** fiilen final, ilk assignment sonrasında değiştirilmeyen
- **Bağlam:** Lambda'nın capture edebildiği local variable/method parameter.
- **Example:** The captured variable must remain effectively final.
- **Çeviri:** Capture edilen variable effectively final kalmalıdır.
- **Related:** final, reassignment

### equivalent · adjective
- **Türkçe:** eşdeğer
- **Bağlam:** Method reference ile long-form lambda'nın aynı runtime davranışını
  vermesi.
- **Example:** `String::isEmpty` is equivalent to `s -> s.isEmpty()`.
- **Çeviri:** `String::isEmpty`, `s -> s.isEmpty()` ile eşdeğerdir.
- **Related:** equivalence (n.); **Antonym:** different

### explicitly · adverb
- **Türkçe:** açıkça
- **Bağlam:** Lambda parameter type'ının source code'da yazılması.
- **Example:** Parentheses are required when the type is stated explicitly.
- **Çeviri:** Type açıkça belirtildiğinde parentheses gereklidir.
- **Related:** explicit (adj.); **Antonym:** implicitly

### facilitate · verb
- **Türkçe:** kolaylaştırmak
- **Bağlam:** Convenience method'ların functional interface'leri birleştirmeyi
  kolaylaştırması.
- **Example:** These methods facilitate predicate composition.
- **Çeviri:** Bu method'lar predicate composition'ı kolaylaştırır.
- **Related:** facilitation (n.), facilitator (n.)

### factory method · noun phrase
- **Türkçe:** factory method, object üreten static method
- **Bağlam:** Constructor doğrudan kullanılmadan `LocalDate.now()` ile object
  oluşturulması.
- **Example:** The supplier calls a factory method to create the date.
- **Çeviri:** Supplier tarihi oluşturmak için factory method çağırır.
- **Related:** constructor, instantiate

### filtering · noun / gerund
- **Türkçe:** filtreleme, koşula göre seçme
- **Bağlam:** `Predicate` ile collection öğelerinin seçilmesi.
- **Example:** Predicates are commonly used for filtering.
- **Çeviri:** Predicate'ler filtering için yaygın biçimde kullanılır.
- **Related:** filter (v./n.), matching (n.)

### full-fledged · adjective
- **Türkçe:** tam teşekküllü, tüm özelliklere sahip
- **Bağlam:** Lambda'nın parameter/body açısından normal method'a benzemesi,
  ancak adı olmaması.
- **Example:** A lambda is shorter than a full-fledged method.
- **Çeviri:** Lambda, tam teşekküllü bir method'dan daha kısadır.
- **Synonym:** fully developed

### functional interface · noun phrase
- **Türkçe:** işlevsel interface, tek abstract method contract'ı olan interface
- **Bağlam:** Lambda veya method reference için target type.
- **Example:** Every lambda expression needs a target functional interface.
- **Çeviri:** Her lambda expression bir target functional interface'e ihtiyaç
  duyar.
- **Related:** SAM, `@FunctionalInterface`

## G–M

### general-purpose · adjective
- **Türkçe:** genel amaçlı
- **Bağlam:** `java.util.function` package'ındaki reusable interface'ler.
- **Example:** Java provides general-purpose functional interfaces.
- **Çeviri:** Java genel amaçlı functional interface'ler sağlar.
- **Antonym:** specialized

### imply · verb
- **Türkçe:** ima etmek, açıkça yazılmadan anlaşılmasını sağlamak
- **Bağlam:** Functional interface type'ının method argument context'inden
  anlaşılması.
- **Example:** The method signature may imply the target interface.
- **Çeviri:** Method signature target interface'i ima edebilir.
- **Related:** implication (n.), implicit (adj.)

### infer · verb
- **Türkçe:** mevcut bilgiden çıkarsamak
- **Bağlam:** Compiler'ın lambda parameter type'ını surrounding context'ten
  bulması.
- **Example:** Java infers the parameter type from the predicate.
- **Çeviri:** Java parameter type'ını predicate'ten infer eder.
- **Related:** inference (n.), inferred (adj.)

### instantiate · verb
- **Türkçe:** instance oluşturmak
- **Bağlam:** Constructor reference'ın `new` ile object üretmesi.
- **Example:** A constructor reference can instantiate a new object.
- **Çeviri:** Constructor reference yeni bir object instantiate edebilir.
- **Related:** instance (n.), instantiation (n.)

### interchangeable · adjective
- **Türkçe:** birbirinin yerine kullanılabilir
- **Bağlam:** Inferred, explicit ve `var` parameter yazımlarının target type
  sabitken aynı davranışı vermesi.
- **Example:** The three single-parameter forms are interchangeable here.
- **Çeviri:** Üç tek-parameter biçimi burada birbirinin yerine kullanılabilir.
- **Related:** interchange (v./n.)

### invocation method · noun phrase
- **Türkçe:** çağırma method'u
- **Bağlam:** Functional interface'in SAM method adı; örneğin `test()` veya
  `apply()`.
- **Example:** Calling the invocation method executes the lambda body.
- **Çeviri:** Invocation method'u çağırmak lambda body'sini çalıştırır.
- **Related:** invoke (v.), invocation (n.)

### lambda body · noun phrase
- **Türkçe:** lambda gövdesi
- **Bağlam:** Arrow operator'ün sağındaki expression veya block.
- **Example:** A block lambda body may contain local declarations.
- **Çeviri:** Block biçimindeki lambda body local declaration'lar içerebilir.
- **Related:** expression body, block body

### lambda expression · noun phrase
- **Türkçe:** lambda ifadesi
- **Bağlam:** Adı olmadan behavior taşıyan ve functional interface'e bağlanan
  kod.
- **Example:** The lambda expression is evaluated in a target context.
- **Çeviri:** Lambda expression target context içinde değerlendirilir.
- **Synonym:** lambda

### method reference · noun phrase
- **Türkçe:** method referansı
- **Bağlam:** `::` kullanarak lambda'nın compact biçimde yazılması.
- **Example:** A method reference defers the method invocation, although a bound
  receiver expression is evaluated immediately.
- **Çeviri:** Method reference method invocation'ı erteler; ancak bound receiver
  expression hemen değerlendirilir.
- **Related:** constructor reference, deferred execution

## O–R

### omit · verb
- **Türkçe:** atlamak, yazmadan bırakmak
- **Bağlam:** Kural izin verdiğinde parameter type, parentheses, braces veya
  `return` keyword'ünü yazmamak.
- **Example:** You may omit the braces for a single expression.
- **Çeviri:** Tek expression için braces'i atlayabilirsiniz.
- **Related:** omission (n.); **Antonym:** include

### particular · adjective
- **Türkçe:** belirli, özel olarak seçilmiş
- **Bağlam:** `str::startsWith` içindeki önceden bilinen receiver object.
- **Example:** This method reference uses a particular object.
- **Çeviri:** Bu method reference belirli bir object kullanır.
- **Synonym:** specific

### predicate · noun
- **Türkçe:** koşul sınayıcı ifade/interface
- **Bağlam:** `T` input'unu `boolean` sonuca dönüştüren functional interface.
- **Example:** The predicate tests whether the string is empty.
- **Çeviri:** Predicate, string'in empty olup olmadığını test eder.
- **Related:** predict (v., farklı anlam), condition

### primitive specialization · noun phrase
- **Türkçe:** primitive'e özelleştirilmiş sürüm
- **Bağlam:** `IntPredicate`, `DoubleFunction` gibi boxing'i azaltan interface'ler.
- **Example:** A primitive specialization avoids unnecessary boxing.
- **Çeviri:** Primitive specialization gereksiz boxing'i önler.
- **Related:** specialize (v.), specialized (adj.)

### provide · verb
- **Türkçe:** sağlamak, sunmak
- **Bağlam:** Java'nın built-in functional interface'leri hazır sunması.
- **Example:** The package provides several reusable interfaces.
- **Çeviri:** Package birçok reusable interface sağlar.
- **Related:** provider (n.), provision (n.)

### receiver · noun
- **Türkçe:** method çağrısını alan object
- **Bağlam:** `String::startsWith` unbound reference'ında ilk SAM parameter'ı.
- **Example:** The first parameter becomes the receiver of the instance method.
- **Çeviri:** İlk parameter instance method'un receiver'ı olur.
- **Related:** target object

### redundancy · noun
- **Türkçe:** gereksiz tekrar
- **Bağlam:** Lambda parameter'ının hiçbir işlem yapılmadan başka method'a
  geçirilmesi.
- **Example:** A method reference removes parameter-passing redundancy.
- **Çeviri:** Method reference, parameter geçirme tekrarını kaldırır.
- **Related:** redundant (adj.); **Antonym:** necessity

### refactor · verb
- **Türkçe:** davranışı koruyarak kod yapısını iyileştirmek
- **Bağlam:** Uzun lambda body'sini ayrı method'a ve sonra method reference'a
  dönüştürmek.
- **Example:** Refactor a long lambda into a named method.
- **Çeviri:** Uzun lambda'yı named method'a refactor edin.
- **Related:** refactoring (n.)

## S–Z

### scope · noun
- **Türkçe:** kapsam, bir adın erişilebilir olduğu bölge
- **Bağlam:** Lambda parameter/local adlarının çevreleyen variable adlarıyla
  çakışmaması.
- **Example:** The name is already declared in the surrounding scope.
- **Çeviri:** Ad, çevreleyen scope'ta zaten bildirilmiştir.
- **Related:** scoped (adj.), variable scope

### single abstract method (SAM) · noun phrase
- **Türkçe:** tek abstract method
- **Bağlam:** Functional interface olmayı belirleyen contract kuralı.
- **Example:** A functional interface follows the single abstract method rule.
- **Çeviri:** Functional interface single abstract method kuralını izler.
- **Related:** functional interface

### succinct · adjective
- **Türkçe:** kısa ve öz
- **Bağlam:** `BinaryOperator<T>`ın üç generic type'lı `BiFunction`dan daha
  açıklayıcı/kısa olabilmesi.
- **Example:** The operator form is more succinct.
- **Çeviri:** Operator biçimi daha kısa ve özdür.
- **Synonym:** concise; **Antonym:** verbose

### supply · verb
- **Türkçe:** sağlamak, üretip vermek
- **Bağlam:** `Supplier`ın input almadan value üretmesi.
- **Example:** The supplier supplies a new list on each call.
- **Çeviri:** Supplier her çağrıda yeni bir liste sağlar.
- **Related:** supplier (n.), provision (n.)

### target type · noun phrase
- **Türkçe:** hedef type
- **Bağlam:** Lambda/method reference'ın hangi SAM signature'ına uyması
  gerektiğini belirleyen functional interface.
- **Example:** The target type resolves the overloaded method reference.
- **Çeviri:** Target type overloaded method reference'ı çözer.
- **Related:** target typing, context

### trait · noun
- **Türkçe:** özellik, nitelik
- **Bağlam:** Bir hayvanın zıplayabilme veya yüzebilme özelliği.
- **Example:** The checker can test any animal trait.
- **Çeviri:** Checker herhangi bir hayvan özelliğini test edebilir.
- **Synonym:** characteristic, attribute

### unary · adjective
- **Türkçe:** tek operandlı
- **Bağlam:** `UnaryOperator<T>`ın bir `T` alıp `T` döndürmesi.
- **Example:** Incrementing a value is a unary operation.
- **Çeviri:** Bir değeri artırmak unary operation'dır.
- **Related:** binary (adj.)

### vice versa · adverbial phrase
- **Türkçe:** tersi de geçerli olmak üzere
- **Bağlam:** Lambda ile method reference arasında iki yönlü dönüşüm yapma.
- **Example:** Convert the method reference to a lambda and vice versa.
- **Çeviri:** Method reference'ı lambda'ya, tersini de method reference'a
  dönüştürün.
- **Related:** conversely

## Mini quiz · Vocabulary recall

Bu bölüm özgün çalışma alıştırmasıdır.

1. “Kodun şimdi belirtilip daha sonra çalışması” hangi phrase'dir?
2. Bir lambda'nın local variable'a erişmesine hangi teknik fiil kullanılır?
3. `String::isEmpty` içindeki runtime object'ine ne denir?
4. “Kısa ve öz” anlamında source context'te hangi adjective kullanılmıştır?
5. “Tersi de geçerli olmak üzere” hangi phrase'dir?

## Cevaplar

1. deferred execution
2. capture
3. receiver
4. succinct
5. vice versa
