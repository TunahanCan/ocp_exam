# Unit 02 · Operators

Bu ünite Java 17 operator'larını, numeric promotion ve casting kurallarını,
operator precedence'ı ve expression evaluation ayrıntılarını OCP odaklı işler.
Kaynak metin ile Türkçe çeviri ana notta art arda verilmiştir.

## Learning objectives

- Unary, binary ve ternary operator'ları ayırt etmek
- Numeric promotion ve explicit casting gereksinimini belirlemek
- Prefix/postfix increment–decrement sonuçlarını izlemek
- Assignment ve compound assignment farkını uygulamak
- Equality, relational, logical ve short-circuit operator'ları çözümlemek
- Operator precedence'ı parentheses ile bilinçli olarak değiştirmek

## Hangi belgeyi ne zaman kullanmalıyım?

| Belge | Ne zaman kullanmalıyım? | Bu oturumdaki hedef |
|---|---|---|
| [Çift dilli ana ders notu](bilingual_notes.md) · [PDF](bilingual_notes.pdf) | Operator'ları ilk kez öğrenirken veya kaynak soruları bağlamıyla okurken | English → Türkçe akışında kural, örnek ve Review Questions bağlantısını görmek |
| [Teknik hafıza notu](technical_memory_notes.md) · [PDF](technical_memory_notes.pdf) | İşlem sırası veya promotion kuralları karıştığında | Expression'ı type, precedence ve side effect adımlarına ayırmak |
| [Unit 02 vocabulary](vocabulary.md) · [PDF](vocabulary.pdf) | `operand`, `precedence`, `narrowing` gibi terimleri tekrar ederken | Teknik kelimeyi gerçek operator bağlamında kullanmak |
| [Unit 02 grammar notes](grammar_notes.md) · [PDF](grammar_notes.pdf) | Koşul, karşıtlık ve sonuç bağlaçlarını çalışırken | Teknik İngilizce ve YDS sentence structure'larını tanımak |
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu tekrarından sonra, süre tutarak | Sekiz soruyla compile/runtime/output ve English anlama düzeyini ölçmek |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana notu baştan sona tek oturumda bitirmek yerine konu
> haritasından bir operator ailesi seçip örneklerini çöz.

## Çalışanlar için 25–30 dakikalık çalışma rotası

Her satır bir **konu durağıdır**; ünitenin tamamını tek oturumda bitirme hedefi
koymaz. Özellikle soru sayısı fazla olan durağı aynı düzenle birkaç güne böl.
Bir oturumda 2–3 kaynak sorusu ve en fazla 5 yeni kelime yeterlidir. Soru
numaraları bu ünitenin kitabındaki Review Questions numaralarıdır.

| Durak | Ana notta okunacak bölüm | Kaynak soruları | Kelime ve grammar odağı |
|---|---|---|---|
| 1. Gruplama ve unary işlemler | [Precedence, parentheses, prefix/postfix](bilingual_notes.md#operator-precedence) | 5, 11, 12, 18, 20, 21 | precedence / associativity / complement; `the order in which` |
| 2. Sayısal dönüşüm | [Promotion, cast, overflow](bilingual_notes.md#numeric-promotion) | 2, 3, 6, 10, 16, 19 | promotion / narrowing / overflow; `when applied independently` |
| 3. Atama ve yan etki | [Normal/compound assignment, dönüş değeri](bilingual_notes.md#compound-assignment-operators) | 8, 14, 17 | assign / resulting / side effect; `allow + object + to + V1` |
| 4. Mantıksal işlemler | [Boolean, kısa devre, ternary](bilingual_notes.md#conditional-operators) | 1, 4, 7, 9, 13, 15 | operand / short-circuit / vice versa; `except that`, `may be + V3` |

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

- **Önkoşul:** [Unit 01](../unit_01_building_blocks/README.md) içindeki primitive
  type, literals, variable declaration ve assignment temelleri.
- **Konu akışı:** Operand type'ları → precedence ve evaluation order → unary
  side effect'ler → numeric promotion ve casting → assignment/compound
  assignment → equality, relational ve short-circuit → ternary expression
- **Sonraki bağlantı:** Boolean expression'ları program akışında kullanmak için
  [Unit 03 · Making Decisions](../unit_03_making_decisions/README.md).

## Hazır mıyım?

- [ ] Prefix ve postfix side effect'lerini soldan sağa doğru izleyebiliyorum.
- [ ] Binary numeric promotion sonrası expression type'ını söyleyebiliyorum.
- [ ] Simple assignment ile compound assignment'ın casting farkını açıklayabiliyorum.
- [ ] `&&`/`||` short-circuit davranışının output ve exception'a etkisini bulabiliyorum.
- [ ] Ternary expression'da seçilmeyen branch'in çalışmadığını biliyorum.
- [ ] [Practice quiz](practice_quiz.md) cevaplarında compile/runtime/output ayrımını gerekçelendirebiliyorum.

## Teknik pekiştirme odağı

Teknik hafıza notunda promotion merdiveni, compound assignment'ın implicit
cast'i, short-circuit side effect'leri, zero division ve reference equality
compatibility tek karar akışında toplanmıştır.

## Kaynak ve kapsam notu

- Ana kaynak: [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 2, PDF sayfaları 65–100.
- [Çift dilli ana ders notu](bilingual_notes.md), Chapter 2'nin girişinden
  Review Questions 1–21'in son seçeneğine kadar her kaynak sayfayı izler;
  tablolar ve şekil açıklamaları da kapsam içindedir.
- OCR kaynaklı ayrılmış operator'lar (`- -`, `- =`, `- >`) doğru Java syntax'ına
  (`--`, `-=`, `->`) getirilmiştir.
- Review soruları kaynak kitabın çalışma sorularıdır; gerçek OCP sınavından
  çıkmış sorular olarak sunulmamaktadır.
