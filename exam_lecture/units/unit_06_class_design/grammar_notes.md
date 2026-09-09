# Unit 06 Grammar Notes · Class Design

## Bu belge nasıl kullanılmalı?

Bu kaynağı [README'deki çalışma rotasının](README.md#işten-sonra-çalışma-rotası)
grammar adımında kullan:

1. Önce koyu formülü oku ve örnekteki yapıyı kendin bul.
2. English cümleyi Türkçe satırı açmadan çevir.
3. YDS ipucu/common mistake ayrımını kontrol et; mini quiz'i en son çöz.

## 1. `provided + clause`

**EN:** Mutable data may be exposed, provided the caller cannot modify it.
**TR:** Caller değiştiremediği sürece mutable data gösterilebilir.

**Formül:** `sonuç cümlesi + provided (that) + özne + fiil`.

**Çözümleme:** `Mutable data` özne; `may be exposed` edilgen yüklem; `provided ...` koşul yan cümlesidir. Bu yan cümlede `the caller` özne, `cannot modify` yüklem, `it` ise mutable data’ya dönen nesnedir.

**Doğal çeviri:** Çağıran taraf değiştiremediği koşuluyla, değiştirilebilir veriye erişim sağlanabilir.

**Kaynak bağlam:** [Creating Immutable Objects](bilingual_notes.md#creating-immutable-objects). Yukarıdaki kısa cümle bu bağlamdan hazırlanmış çalışma örneğidir.

## 2. `regardless of`

**EN:** The overridden method runs regardless of the reference type.
**TR:** Reference type ne olursa olsun overridden method çalışır.

**Formül:** `regardless of + isim/isim grubu`; “-den bağımsız olarak / ne olursa olsun”. `regardless of whether + cümle` de mümkündür.

**Çözümleme:** `The overridden method` özne, `runs` yüklem, `regardless of the reference type` sonuç üzerinde etkisiz olan koşuldur. “Regardless” sözcüğünü görüp referans türünün derleme aşamasında önemsiz olduğunu çıkarma; cümle çalışma zamanındaki geçerli instance override seçimini anlatır.

**Kaynak bağlam:** [Inheriting Members](bilingual_notes.md#inheriting-members).

## 3. `since` ile neden

**EN:** The code fails since the parent has no no-argument constructor.
**TR:** Üst sınıfın parametresiz constructor’ı olmadığı için kod derlenmez.

**Formül:** `sonuç + since + neden cümlesi`. `The code` özne, `fails` yüklem; `the parent` yan cümle öznesi, `has` yan cümle fiilidir. Örnekte alt constructor’ın örtük `super()` çağırdığı varsayılır; `super(1)` gibi geçerli açık çağrı varsa sonuç değişir.

**Kaynak bağlam:** [Understanding Compiler Enhancements](bilingual_notes.md#understanding-compiler-enhancements).

## 4. `by definition`

**EN:** A concrete class is, by definition, not abstract.
**TR:** Somut sınıf, tanımı gereği abstract değildir.

**Formül:** `özne + is, by definition, + tamamlayıcı`. Virgüller arasındaki ifade ana yüklemi değiştirmeyen açıklama zarfıdır.

## 5. `not only ... but also`

**EN:** The subclass not only inherits members but also adds behavior.
**TR:** Alt sınıf yalnızca üyeleri kalıtımla almakla kalmaz, yeni davranış da ekler.

**Formül:** `özne + not only + fiil grubu A + but also + fiil grubu B`. `inherits` ve `adds` aynı özneye bağlı paralel yüklemlerdir.

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
**TR:** Constructor normal biçimde tamamlanıncaya kadar her `final` instance alanına tam olarak bir kez değer atanmış olmalıdır.

Bu Java açıklaması **normal tamamlanma** içindir: constructor exception ile sonlanıyorsa nesne oluşturma başarıyla tamamlanmaz. Static final alanların ataması constructor’a ait değildir.

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
6. *By the time a constructor completes normally, every final instance field must have been assigned.*
