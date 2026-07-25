# Unit 11 · Exceptions and Localization

Bu ünite Java 17 exception handling, try-with-resources, number/date formatting
ve localization konularını çift dilli ana ders; teknik hafıza, vocabulary ve
grammar materyalleriyle birlikte ele alır.

## Amaç ve öğrenme hedefleri

Bu ünitenin sonunda exception hierarchy'yi kullanarak handle-or-declare
kararı verebilmen; try-with-resources kapanış ve suppressed exception akışını
izleyebilmen; formatter, locale ve resource bundle sorularında compile-time ile
runtime sonucunu ayırabilmen hedeflenir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Chapter'ı English → Türkçe eşleşmesiyle kaynak sırasından öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Exception ve localization kararlarını hızlı tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Teknik terimleri bağlam, örnek ve word family ile çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Teknik İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi kaynaklar kapalıyken altı soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Aşağıdaki konu haritasından exception veya localization
   kümelerinden birini seç.
2. **5–25 dk:** Ana çift dilli notta seçtiğin başlığın English paragrafını önce
   kendin çevir; ardından Türkçe blok ve OCP kutusuyla karşılaştır.
3. **25–35 dk:** Teknik hafıza notunda hierarchy, TWR flow veya locale fallback
   karar kartını kaynak kapalıyken yeniden kur.
4. **35–43 dk:** Vocabulary'den 6–8 terim seç ve her biriyle kısa teknik cümle
   kur.
5. **43–50 dk:** Grammar notes içinden bir bağlaç ve bir passive yapıyı
   örnekleriyle çözümle.
6. **50–60 dk:** [Practice quiz](practice_quiz.md)'i cevaplara bakmadan çöz;
   yanlışını compile-time, runtime, output veya English etiketiyle kaydet.

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 11 physical PDF pages: **591–660**
- Chapter 11 Appendix official answers: **945–948**
- Chapter gövdesi: **70/70 kaynak sayfa**
- Görsel kaynaklar: **Table 11.1–11.12** ve **Figure 11.1–11.6**
- Bölüm sonu: Summary, Exam Essentials ve Review Questions 1–26
- Appendix: Official Answers 1–26 ve bütün gerekçeleri

Physical page 660 boş chapter separator sayfasıdır. Chapter 12 page 661'de
başlar. Appendix page 945'in üst bölümü Chapter 10'a, Chapter 11 heading'inden
sonraki alt bölümü bu üniteye aittir.

## Önkoşul ve konu haritası

**Önkoşul:** Class hierarchy, method override, interface ve temel
`java.time` bilgisini; Unit 10'dan resource-backed stream'lerin kapatılması
fikrini hatırlamak yararlıdır.

- `Throwable`, checked/unchecked exception ve handle-or-declare rule
- Runtime, checked ve `Error` class'ları
- `throw` / `throws`, method call ve override kuralları
- Traditional `try`, catch order, multi-catch ve `finally` flow
- Custom exception ve stack trace
- `AutoCloseable`, try-with-resources ve effectively final resource
- Reverse close order, primary ve suppressed exception
- `NumberFormat`, `DecimalFormat`, compact number, parse/format
- `DateTimeFormatter`, standard/custom pattern ve temporal-field uyumu
- `Locale`, DISPLAY/FORMAT category ve default locale
- `.properties`, `ResourceBundle` hierarchy ve key fallback
- `Properties` ve `MessageFormat`

## Hazır mıyım?

- [ ] Checked, unchecked ve `Error` ayrımını hierarchy üzerinde gösterebiliyorum.
- [ ] `throw`, `throws`, catch order ve override exception kurallarını birlikte
  uygulayabiliyorum.
- [ ] TWR kapanış sırasını, primary ve suppressed exception'ı izleyebiliyorum.
- [ ] Formatter pattern'i ile temporal object uyumsuzluğunu runtime sonucu
  olarak sınıflandırabiliyorum.
- [ ] Locale candidate ve `ResourceBundle` parent fallback sırasını
  yazabiliyorum.
- [ ] Number/date pattern'lerinde `M`–`m` ve `0`–`#` ayrımını biliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapıp yanlış seçenekleri
  gerekçelendirebiliyorum.

## Java 17 teknik doğruluk notları

- Checked exception: `Exception` kolunda olup `RuntimeException` kolunda
  olmayan exception'dır; handle veya declare edilmelidir.
- Override method daha geniş checked exception declare edemez; daha dar type
  veya hiç checked exception kullanabilir.
- Multi-catch alternatifleri parent/child ilişkili olamaz ve catch variable
  implicitly finaldır.
- TWR resource'ları declaration'ın ters sırasıyla kapanır.
- Try body exception'ı varken `close()` exception'ı suppressed olur; primary
  exception değişmez.
- Existing resource syntax için variable final veya effectively final olmalıdır.
- `M` month, `m` minute; `0` required digit, `#` optional digit anlamındadır.
- Formatter'ın istediği field temporal object'ta yoksa kod derlenebilir fakat
  runtime `DateTimeException` oluşur.
- Explicit locale verilen formatter default locale category'lerinden bağımsızdır.
- Bir resource bundle hierarchy seçildikten sonra eksik key yalnız o
  hierarchy'nin parent chain'inde aranır.

## Önerilen çalışma sırası

1. Ana çift dilli notu chapter sırasıyla oku.
2. Exception sorularında hierarchy çizip checked/unchecked ayrımını yap.
3. TWR sorularında body → reverse close → catch → finally sırasını uygula.
4. Localization sorularında explicit/default locale ve candidate bundle
   sırasını ayrı yaz.
5. `technical_memory_notes.md` karar algoritmaları ve mini quiz'i çöz.
6. Review Questions 1–26'yı Appendix'e bakmadan tamamla; sonra bütün seçenek
   gerekçelerini karşılaştır.

Vocabulary ve grammar quiz'leri ile teknik hafıza soruları kitaptan alınmış
gerçek sınav soruları değil, açıkça belirtilmiş özgün çalışma sorularıdır.
