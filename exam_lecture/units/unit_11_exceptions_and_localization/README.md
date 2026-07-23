# Unit 11 · Exceptions and Localization

Bu ünite Java 17 exception handling, try-with-resources, number/date formatting
ve localization konularını çift dilli ana ders; teknik hafıza, vocabulary ve
grammar materyalleriyle birlikte ele alır.

## Çalışma kaynakları

1. **Ana çift dilli ders**
   - [Markdown kaynağı](bilingual_notes.md)
   - [PDF çalışma sürümü](bilingual_notes.pdf)
2. **Teknik hafıza ve karar notları**
   - [Technical memory notes](technical_memory_notes.md)
   - [PDF çalışma sürümü](technical_memory_notes.pdf)
3. **Ünite vocabulary çalışması**
   - [Markdown kaynağı](vocabulary.md)
   - [PDF çalışma sürümü](vocabulary.pdf)
4. **Ünite grammar çalışması**
   - [Markdown kaynağı](grammar_notes.md)
   - [PDF çalışma sürümü](grammar_notes.pdf)

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 11 physical PDF pages: **591–660**
- Chapter 11 Appendix official answers: **945–948**
- Chapter gövdesi: **70/70 source marker**
- Görsel kaynaklar: **Table 11.1–11.12** ve **Figure 11.1–11.6**
- Bölüm sonu: Summary, Exam Essentials ve Review Questions 1–26
- Appendix: Official Answers 1–26 ve bütün gerekçeleri

Physical page 660 boş chapter separator sayfasıdır. Chapter 12 page 661'de
başlar. Appendix page 945'in üst bölümü Chapter 10'a, Chapter 11 heading'inden
sonraki alt bölümü bu üniteye aittir.

## Konu haritası

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
