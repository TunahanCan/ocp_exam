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
| [Özgün practice quiz](practice_quiz.md) · [PDF](practice_quiz.pdf) | Konuyu çalıştıktan sonra, notlar kapalıyken | Altı soruyla derleme, çıktı, OCP trap ve teknik İngilizce kontrolü yapmak |
| [Kaynak Review Questions](bilingual_notes.md#review-questions) · [Ana PDF](bilingual_notes.pdf) | Ana konuyu bitirdikten sonra kaynak bölüm-sonu sorularını çözerken | Özgün soru metnini, Java kodunu ve seçenekleri eksiksiz takip etmek |

> **İlk ziyaret için:** Ana not ayrıntılı bir kaynak arşividir; tek oturumda
> bitirmeye çalışma. Önce aşağıdaki konu haritasından bir bölüm seç.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk · Hedef koy:** Learning objectives ve konu haritasından bir alt konu
   seç.
2. **5–25 dk · Ana okuma:** Seçtiğin bölümde önce English paragrafı oku, Türkçe
   anlamı tahmin et, sonra çeviriyle karşılaştır. OCP kutularında kodun
   derlenip derlenmeyeceğini önceden söyle.
3. **25–35 dk · Teknik sıkıştırma:** Teknik hafıza notundaki ilgili karar kartını
   kapatıp kuralı kendi cümlenle anlat.
4. **35–45 dk · Dil tekrarı:** Vocabulary'den beş terim ve grammar notundan bir
   yapı seç; mini quizleri cevapla.
5. **45–55 dk · Ölçme:** Practice quiz'i cevap anahtarına bakmadan çöz. Ana
   nottaki Review Questions'dan zorlandığın bir soruyu da yeniden dene.
6. **55–60 dk · Hata kaydı:** Yanlışını “compile-time / runtime / output /
   English” etiketlerinden biriyle not et.

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
