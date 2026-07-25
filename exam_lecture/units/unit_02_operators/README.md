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
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu tekrarından sonra, süre tutarak | Altı soruyla compile/runtime/output ve English anlama düzeyini ölçmek |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana notu baştan sona tek oturumda bitirmek yerine konu
> haritasından bir operator ailesi seçip örneklerini çöz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk · Hedef koy:** Promotion, assignment, comparison veya
   short-circuit başlıklarından birini seç.
2. **5–25 dk · Ana okuma:** İlgili ana not bölümünü oku; expression'larda
   operator precedence ve operand type'larını işaretle. Üç Exam Essentials
   paragrafını tara ve bir Review Question'ı cevaplamadan önce sonucu tahmin et.
3. **25–35 dk · Teknik sıkıştırma:** Teknik hafıza notundaki karar kartını
   notlar kapalıyken yeniden kur.
4. **35–45 dk · Dil tekrarı:** Vocabulary'den beş kelime, grammar notundan bir
   bağlaç seç ve mini quizleri çöz.
5. **45–55 dk · Ölçme:** Practice quiz'i çöz; her cevap için `Does not
   compile`, runtime exception veya output etiketini açıkça yaz.
6. **55–60 dk · Hata kaydı:** Yanlış yaptığın expression'da ilk hatalı
   varsayımını bir cümleyle kaydet.

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
