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
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konu tekrarından sonra, cevaplar kapalıyken | Altı soruyla declaration, overload, pass-by-value, access ve English anlama kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not 56 kaynak sayfasını korur. Bir oturumda
> declaration/access veya invocation/overload eksenlerinden yalnız birini seç.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk · Hedef koy:** Konu haritasından bir method kararını seç.
2. **5–25 dk · Ana okuma:** İlgili English → Türkçe bölümü oku; her örnekte
   önce declaration geçerli mi, sonra hangi method seçilir, en son runtime'da
   ne olur sorularını yanıtla.
3. **25–35 dk · Teknik sıkıştırma:** Teknik hafıza notundaki access matrix,
   pass-by-value veya overload phase kartını notsuz yeniden çiz.
4. **35–45 dk · Dil tekrarı:** Vocabulary'den beş terim ve grammar notundan bir
   koşul yapısı seç; mini quizleri tamamla.
5. **45–55 dk · Ölçme:** Practice quiz'i çöz ve ana nottaki bir Review
   Question'ı yeniden dene.
6. **55–60 dk · Hata kaydı:** Yanlışını `declaration / access / static /
   pass-by-value / overload / English` etiketiyle kaydet.

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
