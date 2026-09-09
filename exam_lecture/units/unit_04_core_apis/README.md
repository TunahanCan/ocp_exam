# Unit 04 · Core APIs

Bu ünite Java 17 `String`, `StringBuilder`, array, `Math` ve Date/Time API
kurallarını OCP odaklı işler.

## Learning objectives

- String immutability, pool, equality ve method sonuçlarını izlemek
- StringBuilder mutation ve chaining işlemlerini uygulamak
- Array sorting, searching, comparison ve mismatch sonuçlarını çözmek
- `Math` method return type'larını ayırt etmek
- `LocalDate`, `ZonedDateTime`, `Instant` ve daylight saving time davranışlarını
  değerlendirmek

## Hangi belgeyi ne zaman kullanmalıyım?

| Belge | Ne zaman kullanmalıyım? | Bu oturumdaki hedef |
|---|---|---|
| [Çift dilli ana ders notu](bilingual_notes.md) · [PDF](bilingual_notes.pdf) | Bir API ailesini ilk kez öğrenirken veya kaynak örneğe dönmek istediğinde | English → Türkçe anlatımı, method davranışlarını ve Review Questions'ı bağlamında izlemek |
| [Teknik hafıza notu](technical_memory_notes.md) · [PDF](technical_memory_notes.pdf) | Method return type'ı, mutability veya önkoşul karıştığında | String, array, Math ve Date/Time karar kartlarını hızlı uygulamak |
| [Unit 04 vocabulary](vocabulary.md) · [PDF](vocabulary.pdf) | API metnindeki teknik kelimeleri tekrar ederken | Terimleri gerçek Core API bağlamında kullanmak |
| [Unit 04 grammar notes](grammar_notes.md) · [PDF](grammar_notes.pdf) | Boundary, koşul ve karşılaştırma cümlelerini çözerken | Teknik İngilizce ile YDS yapılarını birlikte çalışmak |
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Bir veya birkaç API ailesini tamamladıktan sonra | Sekiz soruyla mutability, equality, index, runtime ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 64 kaynak sayfasını içerir. Tüm API'leri tek
> oturumda çalışmak yerine aşağıdaki haritadan bir dal seç.

## Çalışanlar için 25–30 dakikalık çalışma rotası

Her satır bir **konu durağıdır**; ünitenin tamamını tek oturumda bitirme hedefi
koymaz. Özellikle soru sayısı fazla olan durağı aynı düzenle birkaç güne böl.
Bir oturumda 2–3 kaynak sorusu ve en fazla 5 yeni kelime yeterlidir. Soru
numaraları bu ünitenin kitabındaki Review Questions numaralarıdır.

| Durak | Ana notta okunacak bölüm | Kaynak soruları | Kelime ve grammar odağı |
|---|---|---|---|
| 1. String ve sınırlar | [Concatenation, substring, indent/escape](bilingual_notes.md#creating-and-manipulating-strings) | 1, 8, 12, 16, 17 | concatenation / one past / trailing; `up to, but not including` |
| 2. Mutability ve kimlik | [Builder zinciri, pool, ==/equals](bilingual_notes.md#using-the-stringbuilder-class) | 4, 5, 13, 18, 21 | immutable / mutable / reference equality; `whereas`, `by + V-ing` |
| 3. Array ve arama | [Boyut, sort, compare/mismatch, binarySearch](bilingual_notes.md#understanding-arrays) | 2, 9, 15, 19 | insertion point / mismatch / undefined; `whether`, `given + noun phrase` |
| 4. Math dönüş türleri | [round/min/floor/random ve atama](bilingual_notes.md#calculating-with-math-apis) | 6, 10 | fractional / truncate / resulting; `which of the following` |
| 5. Tarih ve zaman | [Local tipler, Instant, DST, Period/Duration](bilingual_notes.md#working-with-dates-and-times) | 3, 7, 11, 14, 20, 22 | daylight saving time / temporal; `without + V-ing`, `because of` |

**Tek oturumun akışı:** 3 dk önceki kuralı notsuz hatırla → 10 dk bir alt
başlıkta English/Türkçe okuma → 8 dk iki kaynak sorusu → 5 dk kelime ve bir
cümle çözümleme → 2 dk hata kaydı. Metni yetiştirmek için tahmin yapma; kalan
alt başlığa sonraki oturumda devam et.

Soruyu çözerken önce **derlenir mi → çalışırsa exception/sonlanma sorunu var mı
→ çıktı ne** sırasını izle. Ardından [kaynak cevaplarıyla kontrol](bilingual_notes.md#appendix--kaynak-cevaplarıyla-kontrol)
bölümünü aç. Bu bölüm kitabın cevap harflerini özgün Türkçe gerekçeyle açıklar;
[practice quiz](practice_quiz.md) ise ayrı özgün sorulardır.

### 1 / 3 / 7 / 14 gün tekrar

- **1 gün sonra · 5 dk:** Dünkü beş kelimenin Türkçesini kapat, iki yanlış
  sorunun kuralını söyle, bir English cümlede özne ve çekimli fiili işaretle.
- **3 gün sonra · 8 dk:** İki eski soruyu seçenekleri kapatarak yeniden çöz;
  aynı grammar kalıbıyla bir Java cümlesi kur.
- **7 gün sonra · 10 dk:** [Practice quiz](practice_quiz.md) içinden dört
  soruyu karışık çöz; yanlışının nedenini [teknik notta](technical_memory_notes.md) bul.
- **14 gün sonra · 10 dk:** Önce yanlış yaptığın iki kaynak sorusu, beş kelime
  ve bir çeviriyi yeniden dene. Hâlâ açıklayamadığın maddeyi bir sonraki tekrar
  gününe taşı. Bunlar önerilen çalışma aralıklarıdır; kişisel tempona uyarla.

**İlerleme ölçütü:** Son beş kaynak sorusunun en az dördünü bütün seçenekleriyle
doğru gerekçelendirebil; seçtiğin beş kelimeden dördünü yeni cümlede kullan;
bir cümlenin ana yargısını ve koşul/karşıtlık ilişkisini çeviriyi açmadan söyle.
Yapamıyorsan bütün üniteyi yeniden okumak yerine ilgili alt başlığa dön.

**Kısa hata kaydı:** `Tarih | Soru/kelime | Benim cevabım | Doğru kural ve neden |
Bir sonraki tekrar`. Yalnız harf kaydetmek, aynı tuzağı yeniden fark etmeyi sağlamaz.

## Önkoşul ve konu haritası

- **Önkoşul:** [Unit 01](../unit_01_building_blocks/README.md) type/reference
  temeli, [Unit 02](../unit_02_operators/README.md) expression ve index
  işlemleri, [Unit 03](../unit_03_making_decisions/README.md) loop okuma becerisi.
- **Konu akışı:** Immutable `String` → mutable `StringBuilder` → identity ve
  equality → one/multidimensional arrays → sort/search/compare → `Math` return
  type'ları → Local/Zoned Date-Time → `Period`, `Duration`, DST
- **Sonraki bağlantı:** API type'larını method parameter ve overload'larında
  kullanmak için [Unit 05 · Methods](../unit_05_methods/README.md).

## Hazır mıyım?

- [ ] String method sonucunun atanıp atanmadığını her örnekte kontrol ediyorum.
- [ ] `StringBuilder` mutation ile `String` immutability farkını açıklayabiliyorum.
- [ ] `==`, `equals()`, `compare()` ve `mismatch()` görevlerini ayırabiliyorum.
- [ ] Array index/boundary ve binary search önkoşullarını uygulayabiliyorum.
- [ ] Uygun Date/Time type'ını seçip immutable dönüş değerini izleyebiliyorum.
- [ ] [Practice quiz](practice_quiz.md) cevaplarında compile/runtime/result ayrımını gösterebiliyorum.

## Teknik pekiştirme odağı

Teknik hafıza notundaki karar kartları immutable API'ler için I-R-A kuralını,
String index aralıklarını, array search/compare önkoşullarını, Math return
type'larını ve Date/Time type uyumluluğunu birlikte tekrar ettirir.

## Kaynak ve kapsam notu

- Ana kaynak: [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 4, PDF sayfaları 155–218.
- Ana çift dilli not, bölüm metnini ve Review Questions 1–22'yi kaynak
  sırasıyla içerir.
- Bunlar kaynak kitabın review sorularıdır; gerçek sınav sorusu değildir.
