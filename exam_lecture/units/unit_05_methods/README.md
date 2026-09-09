# Unit 05 · Methods

Bu ünite method declaration, access control, `static`, `final`, varargs,
pass-by-value ve overloading kurallarını Java 17/OCP odağında işler.

## Learning objectives

- Cross-package access modifier sonuçlarını belirlemek
- `static` member, initializer ve import kurallarını uygulamak
- `final`/effectively final variable'ları tanımak
- Java pass-by-value davranışını primitive ve object reference ile izlemek
- Overload seçiminde promotion, boxing ve varargs önceliğini çözmek

## Hangi belgeyi ne zaman kullanmalıyım?

| Belge | Ne zaman kullanmalıyım? | Bu oturumdaki hedef |
|---|---|---|
| [Eksiksiz çift dilli ana ders notu](bilingual_notes.md) · [PDF](bilingual_notes.pdf) | Method kurallarını ilk kez öğrenirken veya kaynak Review Questions'a dönerken | English → Türkçe akışında declaration, access ve invocation bağlamını görmek |
| [Teknik hafıza notu](technical_memory_notes.md) · [PDF](technical_memory_notes.pdf) | Access, pass-by-value veya overload seçimi karıştığında | Declaration → overload → runtime algoritmasını hızla uygulamak |
| [Unit 05 vocabulary](vocabulary.md) · [PDF](vocabulary.pdf) | Method terminolojisini tekrar ederken | `argument`, `parameter`, `signature`, `applicability` ayrımını yerleştirmek |
| [Unit 05 grammar notes](grammar_notes.md) · [PDF](grammar_notes.pdf) | Kural cümlelerindeki koşul ve karşıtlığı çözerken | Teknik İngilizce/YDS yapılarını method bağlamında tanımak |
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu tekrarından sonra, cevaplar kapalıyken | Sekiz soruyla declaration, overload, pass-by-value, access ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 56 kaynak sayfasını korur. Bir oturumda
> declaration/access veya invocation/overload eksenlerinden yalnız birini seç.

## Çalışanlar için 25–30 dakikalık çalışma rotası

Her satır bir **konu durağıdır**; ünitenin tamamını tek oturumda bitirme hedefi
koymaz. Özellikle soru sayısı fazla olan durağı aynı düzenle birkaç güne böl.
Bir oturumda 2–3 kaynak sorusu ve en fazla 5 yeni kelime yeterlidir. Soru
numaraları bu ünitenin kitabındaki Review Questions numaralarıdır.

| Durak | Ana notta okunacak bölüm | Kaynak soruları | Kelime ve grammar odağı |
|---|---|---|---|
| 1. Metot anatomisi | [Modifier, signature, return, final](bilingual_notes.md#designing-methods) | 1, 2, 3, 5, 12, 21 | declaration / signature / modifier; `which lines`, `unless + passive` |
| 2. Varargs ve çağrı | [Son parametre, boş dizi, array argümanı](bilingual_notes.md#working-with-varargs) | 6, 7 | parameter / argument / at most; `as if`, `at most` |
| 3. Erişim ve static | [Paket/protected, static üyeler ve initializer](bilingual_notes.md#applying-access-modifiers) | 8, 9, 10, 11, 13, 14, 15, 19 | restrictive / lenient / receiver; `even though`, `rather than` |
| 4. Değer aktarımı | [Reference kopyası, mutation/reassignment](bilingual_notes.md#passing-data-among-methods) | 17, 18 | pass-by-value / reassign / mutation; `since`, `whether` |
| 5. Overload aşamaları | [Widening, boxing ve varargs](bilingual_notes.md#overloading-methods) | 4, 16, 20 | applicability / autoboxing / unboxing; `not until`, `while` |

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

- **Önkoşul:** [Unit 01](../unit_01_building_blocks/README.md) declaration,
  initialization ve type temeli; [Unit 02](../unit_02_operators/README.md)
  promotion/casting; [Unit 04](../unit_04_core_apis/README.md) yaygın reference
  type'ları.
- **Konu akışı:** Method declaration ve signature → local/field modifiers →
  access control → `static` context/imports → varargs → pass-by-value →
  autoboxing/unboxing → overload applicability phase'leri → return kontrolü
- **Sonraki bağlantı:** Constructor, inheritance ve override bağlantıları için
  [Unit 06 · Class Design](../unit_06_class_design/README.md).

## Hazır mıyım?

- [ ] Method declaration parçalarının geçerli sırasını ve signature'ı söyleyebiliyorum.
- [ ] Access matrix'i, özellikle cross-package `protected` receiver kuralını uygulayabiliyorum.
- [ ] Static ve instance context erişimlerini birbirinden ayırabiliyorum.
- [ ] Pass-by-value içinde reassignment ile object mutation farkını izleyebiliyorum.
- [ ] Overload seçiminde widening, boxing ve varargs phase sırasını kullanabiliyorum.
- [ ] [Practice quiz](practice_quiz.md) cevaplarını declaration/selection/runtime ayrımıyla savunabiliyorum.

## Teknik pekiştirme odağı

Teknik hafıza notu method declaration iskeletini, cross-package `protected`
receiver kuralını, pass-by-value modelini, varargs'ı ve overload resolution'ın
fazlarını akılda kalıcı karar kartlarıyla birleştirir.

## Kaynak

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 5 — Methods, PDF sayfaları 219–274.
- Ana not; bölüm açılışı, bütün konu anlatımı, tablolar/şekiller, Summary,
  Exam Essentials ve Review Questions 1–21 dahil tam bölüm kapsamını izler.
- Sorular kaynak kitabın review çalışmalarıdır; gerçek sınav sorusu değildir.
