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
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu sonunda, notlar kapalıyken | Altı soruyla scope, compile, branch, output ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 54 kaynak sayfasını korur. Bir oturumda yalnız
> bir karar ailesine (`if`, `switch`, loops veya branching) odaklan.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk · Hedef koy:** Konu haritasından bir control-flow ailesi seç.
2. **5–25 dk · Ana okuma:** Ana nottaki ilgili English → Türkçe bölümünü ve bir
   şekli incele. Review Questions'da önce compile-time scope, sonra runtime
   branch, en son output kontrolü yap.
3. **25–35 dk · Teknik sıkıştırma:** Teknik hafıza notundaki ilgili switch,
   loop, label veya flow-scope kartını notsuz yeniden anlat.
4. **35–45 dk · Dil tekrarı:** Vocabulary'den beş terim ve grammar notundan bir
   koşul yapısı seç; mini quizleri tamamla.
5. **45–55 dk · Ölçme:** Practice quiz'i süre tutarak çöz ve her yanlışta akış
   şeması çiz.
6. **55–60 dk · Hata kaydı:** Hatanı `scope / exhaustiveness / iteration /
   branching / English` etiketiyle kaydet.

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
