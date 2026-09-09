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
| Bilgiyi kaynaklar kapalıyken sekiz soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## Çalışan biri için çalışma rotası · 25–30 dakikalık oturumlar

Bu tablo bir **ilk tur rotasıdır**; bütün üniteyi tek oturumda bitirme hedefi değildir.
Yoğun başlığı veya uzun soru grubunu aynı rota satırında ikinci güne böl.
Her oturumda **3 dk kapalı kitap hatırlama → 9 dk okuma → 10 dk soru →
5 dk dil çalışması → 3 dk hata kaydı** uygula. Okuma bölümünde önce İngilizce
paragrafı sesli veya yazılı özetle, sonra Türkçe çeviriyle karşılaştır.

| Oturum | Okuma ve teknik hedef | Kaynak Review Questions | Kelime odağı | Grammar odağı |
|---|---|---|---|---|
| 1 · Exception türü ve bildirim | [Understanding Exceptions](bilingual_notes.md#understanding-exceptions) | [1](bilingual_notes.md#question-1--soru-1), [2](bilingual_notes.md#question-2--soru-2), [10](bilingual_notes.md#question-10--soru-10), [11](bilingual_notes.md#question-11--soru-11), [21](bilingual_notes.md#question-21--soru-21) | declare / throw / handle | 12 ve 13: zorunluluk ile zorunda olmama |
| 2 · Yakalama ve kontrol akışı | [Handling Exceptions](bilingual_notes.md#handling-exceptions) | [4](bilingual_notes.md#question-4--soru-4), [13](bilingual_notes.md#question-13--soru-13), [14](bilingual_notes.md#question-14--soru-14), [20](bilingual_notes.md#question-20--soru-20), [26](bilingual_notes.md#question-26--soru-26) | propagate / recover | 11: either … or; 15: due to |
| 3 · Kaynakları kapatma | [Automating Resource Management](bilingual_notes.md#automating-resource-management) | [7](bilingual_notes.md#question-7--soru-7), [12](bilingual_notes.md#question-12--soru-12), [18](bilingual_notes.md#question-18--soru-18), [23](bilingual_notes.md#question-23--soru-23), [24](bilingual_notes.md#question-24--soru-24) | primary / suppress / resource | 18: once; 24: even if |
| 4 · Sayı ve tarih biçimlendirme | [Formatting Values](bilingual_notes.md#formatting-values) | [5](bilingual_notes.md#question-5--soru-5), [6](bilingual_notes.md#question-6--soru-6), [9](bilingual_notes.md#question-9--soru-9), [16](bilingual_notes.md#question-16--soru-16), [22](bilingual_notes.md#question-22--soru-22) | parse / format / explicit | 16: regardless of |
| 5 · Locale ve kaynak demeti | [Supporting Internationalization and Localization](bilingual_notes.md#supporting-internationalization-and-localization) | [3](bilingual_notes.md#question-3--soru-3), [8](bilingual_notes.md#question-8--soru-8), [15](bilingual_notes.md#question-15--soru-15), [17](bilingual_notes.md#question-17--soru-17), [19](bilingual_notes.md#question-19--soru-19), [25](bilingual_notes.md#question-25--soru-25) | locale / fallback / user-facing | 17: in the order in which; 23: karşılaştırma |
| 6 · Karışık kontrol | [Teknik hafıza notu](technical_memory_notes.md): önce karar kuralını bellekten yaz | Önceki oturumların en zor 3 sorusu + [özgün quiz 7–8](practice_quiz.md#soru-7) | Yanlış yaptığın 5 kelime | Bir uzun cümlede özne, yüklem ve bağlacı işaretle |

Kaynak soruların seçenek sayısı ve “Choose all that apply” yönergesi korunmuştur.
Cevaplara geçmeden seçtiğin her şık için bir gerekçe yaz. Kaynak cevapla Java 17
notu ayrışıyorsa ilgili editör notunu da oku; yalnız harf ezberleme.

### 1 / 3 / 7 / 14 gün tekrar döngüsü

Her oturumun tekrarını kendi çalışma tarihinden itibaren planla:

- **1. gün · 5 dk:** O günün 3–5 kelimesini Türkçeden İngilizceye üret; kuralı bir örnekle anlat.
- **3. gün · 8 dk:** Yanlış veya tahminle doğru yaptığın iki soruyu seçenekleri kapatarak yeniden çöz.
- **7. gün · 10 dk:** Farklı konulardan üç soru ve bir cümle çözümlemesi yap.
- **14. gün · 10 dk:** Hâlâ karıştırdığın kuralları ve kelimeleri tekrar yokla; doğru cevapla birlikte nedenini söyle.

Hata kaydına tek satır yeter: **soru → benim gerekçem → doğru kural →
yeni örnek → tekrar tarihi**. Hatanın türünü `Java kuralı`, `kod izleme`,
`kelime` veya `cümle yapısı` olarak belirt; böylece bir sonraki kısa oturumun
hedefi belli olur.

**Geçiş ölçütü:** İki ayrı günde özgün quiz'de en az **7/8**; kaynaklarda
yanlış yapılan soruların doğru gerekçesi; seçilen 5 kelimeden en az 4'ünü
cümlenin içinde kullanma; bir İngilizce cümlede ana yüklemi ve koşul/karşıtlık
ilişkisini açıklama. Sağlanmayan beceri için yalnız ilgili oturumu yinele.

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
- [ ] Practice quiz'de en az **7/8** doğru yapıp yanlış seçenekleri
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
