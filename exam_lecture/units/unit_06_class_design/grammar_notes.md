# Unit 06 Grammar Notes · Class Design

## Bu belge nasıl kullanılmalı?

Bu kaynağı [README'deki çalışma rotasının](README.md#4560-dakikalık-önerilen-çalışma-rotası)
grammar adımında kullan:

1. Önce koyu formülü oku ve örnekteki yapıyı kendin bul.
2. English cümleyi Türkçe satırı açmadan çevir.
3. YDS ipucu/common mistake ayrımını kontrol et; mini quiz'i en son çöz.

## 1. `provided + clause`

**EN:** Mutable data may be exposed, provided the caller cannot modify it.
**TR:** Caller değiştiremediği sürece mutable data gösterilebilir.

`provided (that)` güçlü bir condition bildirir.

## 2. `regardless of`

**EN:** The overridden method runs regardless of the reference type.
**TR:** Reference type ne olursa olsun overridden method çalışır.

Ardından noun/noun phrase gelir; “-den bağımsız olarak” anlamı taşır.

## 3. `since` ile neden

**EN:** The code fails since the parent has no no-argument constructor.
**TR:** Parent no-argument constructor'a sahip olmadığı için kod derlenmez.

## 4. `by definition`

**EN:** A concrete class is, by definition, not abstract.
**TR:** Concrete class tanımı gereği abstract değildir.

## 5. `not only ... but also`

**EN:** The subclass not only inherits members but also adds behavior.
**TR:** Subclass yalnız member'ları inherit etmekle kalmaz, davranış da ekler.

## 6. `followed by`

**EN:** Parent initialization is followed by child initialization.
**TR:** Parent initialization'ı child initialization izler.

Passive sequence kalıbıdır: `A + be + followed by + B`.

## 7. `by + V-ing`

**EN:** By extending an existing class, you increase code reuse.
**TR:** Mevcut bir class'ı extend ederek code reuse'u artırırsın.

`by + gerund`, bir sonucun hangi yöntemle elde edildiğini bildirir. YDS'de
“nasıl?” sorusuna cevap verir; agent bildiren passive `by + noun` ile karıştırma.

## 8. `which in turn + verb`

**EN:** AfricanElephant extends Elephant, which in turn extends Mammal.
**TR:** AfricanElephant, Elephant'ı extend eder; Elephant da sırasıyla Mammal'ı
extend eder.

`which in turn`, zincirleme sonucu veya bir sonraki ilişki halkasını gösterir.

## 9. `as long as + clause`

**Formül:** `main clause + as long as + condition`
**EN:** A class can have multiple constructors, as long as each constructor has
a unique signature.
**TR:** Her constructor benzersiz bir signature'a sahip olduğu sürece class
birden fazla constructor içerebilir.

`as long as`, gerekli condition'ı “-dığı sürece / koşuluyla” anlamıyla verir.
YDS'de süre anlamındaki *while* ile karıştırmayın; burada logical condition
bildirir.

## 10. `whether ... or not`

**Formül:** `whether + clause + or not`
**EN:** Every class has a constructor, whether you code one or not.
**TR:** Siz yazsanız da yazmasanız da her class'ın bir constructor'ı vardır.

İki olasılığın da ana sonucu değiştirmediğini gösterir. Türkçede çoğunlukla
“-sa da -masa da” kalıbıyla doğal çevrilir.

## 11. `by the time + clause`

**Formül:** `result + by the time + event`
**EN:** By the time the constructor completes, every final instance variable
must be assigned exactly once.
**TR:** Constructor tamamlanıncaya kadar her `final` instance variable'a exactly
once değer atanmış olmalıdır.

`by the time`, belirtilen son ana kadar sonucun tamamlanmış olmasını bekler.
YDS'de tense uyumuna ve deadline (son sınır) anlamına dikkat edin.

## 12. `even though + clause`

**Formül:** `even though + unexpected fact, main clause`
**EN:** Even though only one object is created, both hidden variables exist.
**TR:** Yalnızca bir object oluşturulsa da iki hidden variable da vardır.

Güçlü contrast/concession (karşıtlık/ödünleme) bildirir. `despite` ve
`in spite of` sonrasında noun veya gerund gelirken `even though` tam clause alır.

## Mini quiz

1. `regardless of` ile polymorphism cümlesi yaz.
2. `provided` ile immutability condition'ı kur.
3. `followed by` ile initialization sırasını anlat.
4. `by definition` kullanarak concrete class'ı tanımla.
5. `whether ... or not` ile default constructor kuralını anlat.
6. `by the time` ile `final` field kuralını yaz.

## Cevaplar

1. *Runtime dispatch applies regardless of the reference type.*
2. *Data may be exposed, provided the caller cannot mutate it.*
3. *Static initialization is followed by instance initialization.*
4. *A concrete class is, by definition, not abstract.*
5. *Every class has a constructor, whether you declare one or not.*
6. *By the time the constructor completes, every final field must be assigned.*
