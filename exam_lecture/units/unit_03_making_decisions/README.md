# Unit 03 · Making Decisions

Bu ünite Java 17 `if`/`else`, `switch`, pattern matching, loop ve branching
kurallarını OCP odaklı işler. Chapter 3'ün konu anlatımı, şekil ve tabloları,
Summary, Exam Essentials ve bütün Review Questions içeriği sayfa bazında
izlenebilen English–Türkçe eşleşmeleriyle tek ana notta tutulur.

## Learning objectives

- `if`/`else` akışını ve assignment–comparison tuzaklarını çözmek
- Statement ile expression biçimindeki `switch` yapılarını ayırt etmek
- `instanceof` pattern matching ve flow scoping uygulamak
- `while`, `do/while`, traditional `for` ve enhanced `for` döngülerini izlemek
- Label, `break`, `continue`, scope ve infinite loop sorularını analiz etmek

## Hangi belgeyi ne zaman kullanmalıyım?

| Belge | Ne zaman kullanmalıyım? | Bu oturumdaki hedef |
|---|---|---|
| [Çift dilli ana ders notu](bilingual_notes.md) · [PDF](bilingual_notes.pdf) | Bir control-flow yapısını ilk kez çalışırken veya kaynak Review Questions'a dönerken | Kaynak sırasındaki English → Türkçe anlatımı, şekilleri ve örnekleri izlemek |
| [Teknik hafıza notu](technical_memory_notes.md) · [PDF](technical_memory_notes.pdf) | Switch, loop veya pattern scope kararını hızlandırmak istediğinde | Akış kurallarını karşılaştırmalı kartlarla hatırlamak |
| [Unit 03 vocabulary](vocabulary.md) · [PDF](vocabulary.pdf) | `exhaustive`, `flow scoping`, `fall-through` gibi terimleri pekiştirirken | Teknik kelimeyi control-flow bağlamında kullanmak |
| [Unit 03 grammar notes](grammar_notes.md) · [PDF](grammar_notes.pdf) | Koşul ve sonuç yapılarının çevirisini çalışırken | YDS anlam ilişkilerini kısa örneklerle ayırt etmek |
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu sonunda, notlar kapalıyken | Sekiz soruyla scope, compile, branch, output ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 54 kaynak sayfasını korur. Bir oturumda yalnız
> bir karar ailesine (`if`, `switch`, loops veya branching) odaklan.

## Çalışanlar için 25–30 dakikalık çalışma rotası

Her satır bir **konu durağıdır**; ünitenin tamamını tek oturumda bitirme hedefi
koymaz. Özellikle soru sayısı fazla olan durağı aynı düzenle birkaç güne böl.
Bir oturumda 2–3 kaynak sorusu ve en fazla 5 yeni kelime yeterlidir. Soru
numaraları bu ünitenin kitabındaki Review Questions numaralarıdır.

| Durak | Ana notta okunacak bölüm | Kaynak soruları | Kelime ve grammar odağı |
|---|---|---|---|
| 1. Karar ve akış kapsamı | [if/else, pattern matching ve scope](bilingual_notes.md#creating-decision-making-statements) | 2, 8, 18, 23, 28 | discern / accessible / flow scoping; `if` ile `whether` farkı |
| 2. Switch kuralları | [Selector, constant case, statement/expression](bilingual_notes.md#applying-switch-statements) | 1, 4, 10, 11, 15, 21, 22, 25, 27 | selector / exhaustive / fall-through; `unless`, `does not have to` |
| 3. Döngü ve sınır | [while, do/while, for ve güncelleme sırası](bilingual_notes.md#writing-while-loops) | 6, 12, 13, 17, 19, 29 | at least / iteration / terminate; `since`, `as long as` |
| 4. Array dolaşımı | [Enhanced for, var, ters indeksleme](bilingual_notes.md#the-for-each-loop) | 3, 5, 7, 14, 16, 24 | reverse order / scope / skip; `provided that`, reduced passive |
| 5. Etiketli akış | [Nested loop, break/continue, sonlanma](bilingual_notes.md#controlling-flow-with-branching) | 9, 20, 26 | branching / infinite loop / unreachable; `would have + V3` |

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

- **Önkoşul:** [Unit 02](../unit_02_operators/README.md) içindeki boolean
  expression, comparison, assignment ve short-circuit kuralları.
- **Konu akışı:** `if/else` → pattern matching ve flow scoping → switch
  statement → switch expression ve exhaustiveness → `while`/`do-while`/`for`
  → labels, `break`, `continue`, `return` → reachability
- **Sonraki bağlantı:** Loop'larda işlenecek String, array ve Date/Time
  değerleri için [Unit 04 · Core APIs](../unit_04_core_apis/README.md).

## Hazır mıyım?

- [ ] Dangling `else` ve braces etkisini kod üzerinde açıklayabiliyorum.
- [ ] Pattern variable'ın yalnız kanıtlanmış true-path scope'unda kullanıldığını biliyorum.
- [ ] Switch statement ile expression ve `break` ile `yield` farkını ayırabiliyorum.
- [ ] Bir switch expression'ın exhaustive olup olmadığını kontrol edebiliyorum.
- [ ] Loop'ta initialization, condition, body ve update sırasını izleyebiliyorum.
- [ ] [Practice quiz](practice_quiz.md) cevaplarını scope ve akış gerekçesiyle savunabiliyorum.

## Teknik pekiştirme odağı

Teknik hafıza notunda Java 17 switch selector/label kuralları,
statement–expression farkı, loop garantileri, labeled branching ve pattern
variable'ın true-path scope'u karşılaştırmalı olarak verilmiştir.

## Kaynak ve kapsam notu

- Ana kaynak: [OCP Java SE 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 3, PDF sayfaları 101–154.
- Ana notta **54/54 kaynak sayfa** kayıtlıdır; kapsam bilgisi belgenin başında,
  kapsam doğrulaması belgenin sonundadır.
- OCR kaynaklı `- -`, `- =`, `- >` biçimleri `--`, `-=`, `->` olarak
  düzeltilmiştir.
- Bunlar kaynak kitabın review sorularıdır; gerçek OCP sınav sorusu olarak
  sunulmamaktadır.
