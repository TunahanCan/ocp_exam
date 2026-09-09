# Unit 01 · Building Blocks

Bu ünite Java 17 programlarının en küçük yapı taşlarını, kaynak koddan çalışan
programa giden yolu ve değişkenlerin yaşam döngüsünü OCP odaklı biçimde öğretir.
İngilizce ve Türkçe paragraflar ana notta art arda verilmiştir; ayrıntılı dil
çalışmaları ünitenin kendi vocabulary ve grammar kaynaklarındadır.

## Learning objectives

- JDK, JVM, `javac`, `java` ve `jar` rollerini ayırt etmek
- Class yapısını, `main()` imzasını, package/import kurallarını çözümlemek
- Object oluşturma ve initialization sırasını izlemek
- Primitive/reference type, wrapper, text block ve `var` kurallarını uygulamak
- Variable scope ile garbage collection eligibility sorularını çözmek

## Hangi belgeyi ne zaman kullanmalıyım?

| Belge | Ne zaman kullanmalıyım? | Bu oturumdaki hedef |
|---|---|---|
| [Çift dilli ana ders notu](bilingual_notes.md) · [PDF](bilingual_notes.pdf) | Konuyu ilk kez öğrenirken veya kaynak metni English → Türkçe karşılaştırırken | Kaynak sırasını izlemek, kuralı bağlamında görmek |
| [Teknik hafıza notu](technical_memory_notes.md) · [PDF](technical_memory_notes.pdf) | Ana okumadan sonra veya sınav öncesi hızlı tekrarda | Compile → runtime → result karar akışını kurmak |
| [Unit 01 vocabulary](vocabulary.md) · [PDF](vocabulary.pdf) | Teknik kelimeleri tanımakta zorlandığında | Terimi anlamı, örneği ve word family'siyle hatırlamak |
| [Unit 01 grammar notes](grammar_notes.md) · [PDF](grammar_notes.pdf) | İngilizce cümlenin anlam ilişkisi belirsiz kaldığında | Teknik metindeki grammar yapısını ve YDS ipucunu çözmek |
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konuyu çalıştıktan sonra, notlar kapalıyken | Sekiz soruyla derleme, çıktı, OCP trap ve teknik İngilizce kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not ayrıntılı bir kaynak arşividir; tek oturumda
> bitirmeye çalışma. Önce aşağıdaki konu haritasından bir bölüm seç.

## Çalışanlar için 25–30 dakikalık çalışma rotası

Her satır bir **konu durağıdır**; ünitenin tamamını tek oturumda bitirme hedefi
koymaz. Özellikle soru sayısı fazla olan durağı aynı düzenle birkaç güne böl.
Bir oturumda 2–3 kaynak sorusu ve en fazla 5 yeni kelime yeterlidir. Soru
numaraları bu ünitenin kitabındaki Review Questions numaralarıdır.

| Durak | Ana notta okunacak bölüm | Kaynak soruları | Kelime ve grammar odağı |
|---|---|---|---|
| 1. Araçlar ve giriş noktası | [JDK/JVM, `javac`/`java` ve `main()`](bilingual_notes.md#learning-about-the-environment) | 1, 2, 11, 13 | compile / run / precede; Amaç `to + V1` |
| 2. Nesne ve başlatma | [Constructor, field ve initializer sırası](bilingual_notes.md#creating-objects) | 3, 17, 20, 21 | declaration / initialize / instance; `before` / `after` |
| 3. Türler ve literal | [Primitive/reference, wrapper, text block](bilingual_notes.md#understanding-data-types) | 4, 7, 9, 14, 16, 19 | essential / incidental whitespace; `which/that` ile niteleme |
| 4. Yerel değişkenler | [Definite assignment, `var`, çoklu bildirim](bilingual_notes.md#initializing-variables) | 8, 10, 12, 18, 22, 23 | explicitly / restricted identifier; Modal passive `must be + V3` |
| 5. Kapsam ve yaşam süresi | [Scope, reachability ve garbage collection](bilingual_notes.md#managing-variable-scope) | 5, 6, 15 | reachable / eligibility / reclaim; `unless` ve koşul |

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

- **Önkoşul:** Java bilgisi gerektirmez; terminalde command çalıştırma ve
  dosya/dizin kavramlarına aşinalık yararlıdır.
- **Konu akışı:** JDK/JVM ve araçlar → source/class yapısı → `package`,
  `import`, classpath → object ve initialization → primitive/reference,
  literals ve `var` → scope, lifetime ve garbage collection
- **Sonraki bağlantı:** Type ve expression temeli oturduktan sonra
  [Unit 02 · Operators](../unit_02_operators/README.md) ile devam et.

## Hazır mıyım?

- [ ] `javac`, `java`, JVM ve JDK rollerini birbirine karıştırmadan açıklayabiliyorum.
- [ ] Package/import sırasını ve wildcard'ın subpackage'leri kapsamadığını biliyorum.
- [ ] Field ile local variable initialization farkını kod üzerinde bulabiliyorum.
- [ ] Primitive/reference, literal ve `var` sorularında compile durumunu belirleyebiliyorum.
- [ ] Bir object'in reachable olup olmadığını reference zincirini çizerek gösterebiliyorum.
- [ ] [Practice quiz](practice_quiz.md) sorularında yanlışlarımı gerekçelendirebiliyorum.

## Teknik pekiştirme odağı

Teknik hafıza notu compile → runtime → result çözüm sırasını; field/local
initialization, `var`, literals, classpath ve reachability ayrımlarını tek memory
map üzerinde birleştirir.

## Kaynak ve kapsam notu

- Ana kaynak: [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 1, PDF sayfaları 1–64.
- [Çift dilli ana ders notu](bilingual_notes.md), her kaynak PDF sayfasını
  izler; **64/64 kaynak sayfa** doğrulanmıştır. Başlıkları, tabloları, şekil
  açıklamalarını, Summary, Exam Essentials ve Review Questions bölümlerini
  kaynak sırasıyla içerir.
- İngilizce metinde yalnızca running header/footer, basılı sayfa numarası ve OCR
  kaynaklı tireleme temizlenmiştir. Review Questions kaynak kitabın çalışma
  sorularıdır; gerçek OCP sınavından çıkmış sorular olarak sunulmaz.
