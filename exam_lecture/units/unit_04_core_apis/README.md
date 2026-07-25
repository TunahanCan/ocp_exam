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
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Bir veya birkaç API ailesini tamamladıktan sonra | Altı soruyla mutability, equality, index, runtime ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 64 kaynak sayfasını içerir. Tüm API'leri tek
> oturumda çalışmak yerine aşağıdaki haritadan bir dal seç.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk · Hedef koy:** String/StringBuilder, arrays, Math veya Date/Time
   dallarından birini seç.
2. **5–25 dk · Ana okuma:** İlgili English → Türkçe bölümünü oku. Her method
   için receiver değişiyor mu, return type nedir ve hangi sınır geçerlidir
   sorularını cevapla.
3. **25–35 dk · Teknik sıkıştırma:** Teknik hafıza notunda aynı API'nin karar
   kartını kapatıp I-R-A veya uygun type/önkoşul kuralını yeniden kur.
4. **35–45 dk · Dil tekrarı:** Vocabulary'den beş terim, grammar notundan bir
   boundary/condition yapısı seç ve mini quizleri çöz.
5. **45–55 dk · Ölçme:** Practice quiz'i notlar kapalıyken tamamla; ana nottaki
   bir Review Question'ı da yeniden çöz.
6. **55–60 dk · Hata kaydı:** Yanlışını `immutability / identity / index /
   return type / date-time / English` etiketiyle yaz.

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
