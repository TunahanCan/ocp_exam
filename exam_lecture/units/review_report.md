# Çalışma Dokümanları · İnceleme ve İyileştirme Kaydı

## 14–15 Eylül 2026 · Teknik dil ve ders kullanılabilirliği incelemesi

Bu inceleme 15 ünitedeki 90 Markdown kaynağını ve ortak çalışma belgelerini
kapsar. Yerel kitap PDF'si, özgün metin, kaynak soru ve OCR düzeltmelerinde
karşılaştırma kaynağıdır. İngilizce teknik terimler korunurken doğal Türkçe
anlatım, anlamı değiştiren modal/koşul yapıları ve Java 17 kuralları birlikte
kontrol edilmiştir. Mevcut konu sırası, ünite yapısı ve önceki çalışmalar korunur.

### Çeviri ve okuma düzeni

- `overload`, `override`, `interface`, `stream`, `thread`, `exception`,
  `wrapper` ve `garbage collection` gibi yerleşik terimler bağlamına uygun
  biçimde korunur. Dosya/satır/çıktı gibi normal Türkçe sözcükler gereksiz
  yere İngilizceleştirilmez. [Çalışma Merkezi](README.md#çevirilerde-teknik-dil)
  ve [çalışma planı](study_plan.md#teknik-terimi-koruyarak-çevir) bu yaklaşımı
  örnekler.
- Kod veya terminal çıktısı olduğu hâlde çeviri paragrafına dönüşmüş içerik,
  kaynakla karşılaştırılarak doğru blok türüne taşınmıştır. Bu nedenle bazı
  ünitelerde paragraf çifti sayısı azalırken okunabilir kod/çıktı blokları artar.
- İngilizce ve Türkçe PDF blokları aynı kartta, sırasıyla mavi ve yeşil alanlarda
  gösterilir. Editör açıklamaları turuncu kutularda kalır. Kaynak sayfa
  numaraları konu başlıklarından daha küçük gösterilir.
- Belge denetimine yalnız blok sayısını değil, English → Türkçe sırasını ve
  seçenek harflerinin eşleşmesini de kontrol eden bir kural eklenmiştir.

### Somut teknik düzeltmeler

- **Unit 01–05:** `var` bağlamları, initialization sırası, operator precedence
  ve operand evaluation farkı, constant narrowing sınırı, UTF-16 `length()`
  anlamı, blank final field ve overload seçim aşamaları netleştirilmiştir.
  Label içeren bölünmüş kodlar kaynakla birleştirilmiştir.
- **Unit 06–10:** Parameterized `instanceof` için Java 17'de geçerli olan
  istisnalar açıklanmış; Streams metnindeki `Optional`, boxing/unboxing ve
  terminal operation çevirileri düzeltilmiştir. Streams içindeki sekiz OCR
  tablosu yeniden kurulmuş ve sayfa sınırında bölünen Spliterator örneği
  kaynak PDF sayfası 569 ile karşılaştırılarak birleştirilmiştir.
- **Unit 11–15:** Unchecked exception için ters çevrilmiş izin cümlesi,
  `NumberFormat` türü, suppressed exception koşulu ve çevrilmiş stack trace
  satırları düzeltilmiştir. Teknik terimlerin vocabulary/grammar içindeki
  kullanımları da bağlamıyla kontrol edilmiştir. Exceptions içindeki 12 tablo
  düzenlenmiş; `s`/`S` tarih biçimlendirme ayrımı ve ResourceBundle seçim
  önceliği doğrulanmıştır. I/O içindeki 27 şekil/tablo caption çifti art arda
  alınmış, sekiz çift tablo satır bazında iki dilli tek tabloda birleştirilmiştir.
  JDBC şekline `CallableStatement → PreparedStatement → Statement` doğrudan
  inheritance zinciri, kaynak açıklamasından ayrılan bir editör notuyla eklenmiştir.

### Doğrulama ve sınırlar

- **356 kaynak cevabının harfleri** yerel PDF'nin Appendix bölümünden yeniden
  çıkarılan anahtarla karşılaştırılmış, tamamı eşleşmiştir. Bu, kitaptaki her
  açıklamanın teknik olarak hatasız olduğu anlamına gelmez; bulunan kaynak
  hataları ayrı editör açıklamasıyla işaretlenmiştir.
- Markdown başlıkları, yerel dosya/başlık bağlantıları, kaynak soru sınırları,
  kod çitleri ve çift dilli eşlemeler denetlenmiştir. **93 Markdown dosyası**
  denetimi geçmiştir. Kaynak bölümlerin 908 sayfa işareti ve Appendix sayfa
  işaretleri korunmuştur. Sayfa işaretleri, metnin kelime kelime eksiksiz
  olduğunun kanıtı olarak kullanılmaz.
- **76 PDF / 2.081 sayfa** güncel Markdown kaynaklarından üretilmiştir.
  Bütün sayfalar görüntüye dönüştürülmüş; 173 toplu sayfa görünümü ve gereken
  tekil sayfa büyütmeleriyle görsel olarak incelenmiştir. İngilizce–Türkçe
  eşleşmeleri, caption/şekil/tablo birlikteliği, Türkçe karakterler, kod
  blokları ve sayfa kırılmaları kontrol edilmiştir. Son otomatik yerleşim
  taramasında metin taşması, boş içerik sayfası veya ayrılmış paragraf çifti
  bulgusu kalmamıştır.
- Tablo başlıklarındaki inline code ve link renkleri beyaza alınmıştır.
  Son kontrast düzeltmesinin uygulandığı 10 PDF'de 464 sayfanın metni ve
  koordinatları aynı kalmış; rengi değişen 17 sayfa ayrıca görsel olarak
  kontrol edilmiştir. Unit 15 ana PDF'si son şekil düzeltmesi ve yeni
  renklerle ayrıca baştan sona incelenmiştir.
- Bütün PDF ve kaynak Markdown dosyalarının SHA256 özetleri render sırasında
  kaydedilen son sürümle eşleşmiştir. Kaynak kitap PDF'si değiştirilmemiştir.
- Java kontrollerinde gerçek **Amazon Corretto JDK 17.0.20.1** kullanılmıştır;
  yalnızca daha yeni JDK üzerinde `--release 17` ile yetinilmemiştir.
  [Dağıtımın resmî indirme kaynağı](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/downloads-list.html).
- **57 özgün quiz programı ve 18 odaklı örnek** Java 17 ile doğrulanmıştır.
  Beklenen derleme hataları ve runtime exception'lar başarıyla çalışan
  örneklerden ayrı değerlendirilmiştir. Ünite 01–05'te 26, 06–10'da 29,
  11–15'te 19 kontrol beklenen sonucu vermiştir. JDBC için haricî driver veya
  veritabanı kurulmamış; uygun soruda standart `CachedRowSet` kullanılmıştır.
  Ek son kontrolde JDBC interface'lerinin doğrudan üst türleri reflection ile
  doğrulanmıştır; toplam **75 Java 17 kontrolü** beklenen sonucu vermiştir.
- Bu inceleme bütün kitabın yeniden çevirisi veya bütün örneklerinin çalıştırma
  testi değildir. Geniş yapısal tarama ile tespit edilen anlam/teknik sorunların
  kaynak karşılaştırması ve odaklı kod doğrulaması birlikte yapılmıştır.

Aşağıdaki 9 Eylül kaydı önceki çalışmanın tarihçesidir; içindeki üretim sayıları
ve doğrulama ifadeleri o tarihteki sürüme aittir.

---

**Önceki inceleme tarihi:** 9 Eylül 2026.

İnceleme 15 ünitenin girişlerini, vocabulary, grammar, teknik hafıza ve özgün
quiz materyallerini kapsar. Ana çift dilli notlarda soru/cevap bütünlüğü,
kaynak sayfa sırası, bağlantılar ve tespit edilen somut teknik/çeviri sorunları
ele alınmıştır. Uzun ana metinlerin bütün cümleleri yeniden çevrilmiş değildir.

## Öğrenmeyi zorlaştıran başlıca sorunlar

| Önceki durum | Yapılan iyileştirme |
|---|---|
| İlk 7 ünitede kitap soruları vardı, kaynak cevapları yoktu | 172 soruya kaynak cevabı ve özgün Türkçe çözüm gerekçesi eklendi |
| Genel çalışma süreleri gerçek konu ve sorularla yeterince eşleşmiyordu | Her üniteye konu başlığı ve kaynak soru numarası içeren kısa oturum rotası kondu |
| Bazı Türkçe örnekler İngilizce sözcük dizisini koruyordu | Özellikle vocabulary örnek çevirileri doğallaştırıldı; teknik anlam ayrımları eklendi |
| Grammar'de formülü görmek, uzun cümleyi çözmek için tek başına yetmiyordu | Özne, çekimli fiil ve yan cümle ayrımıyla çözümleme örnekleri eklendi |
| Bazı kural ve çeviriler gereğinden fazla genellenmişti | Java 17 bağlamı ve istisnaları açıklanarak düzeltildi |
| Ek quiz sayısı ünite başına altıydı | Her üniteye iki özgün soru eklendi; toplam 120 soruya ulaşıldı |
| PDF içindekiler bağlantıları yalnız görsel biçim taşıyordu | Belge içi bağlantılar ve konu yer imleri eklendi |
| Birden fazla kaynak satırına yayılan vurgu PDF'de bozulabiliyordu | Paragrafın Markdown biçimi birlikte işlenerek düzeltildi |
| Kısa cevap gerekçeleri, soru seçenekleri veya tek sözcükler sonraki sayfaya düşebiliyordu | Kısa soru/cevap blokları birlikte tutuldu; paragraf sonlarının tek satıra ayrılması önlendi |

## Önemli içerik düzeltmelerinden örnekler

- **Unit 01:** Bir referansın kapsamı ile nesnenin erişilebilirliği ayrıldı.
  `eligible` ve `guaranteed` anlamları karşılaştırıldı. Kaynak sorudaki
  `float` varsayılanı için `0` / `0.0f` anlatımındaki belirsizlik belirtildi.
- **Unit 02:** `&` ve `^` operatörlerinin aynı öncelikte olduğu biçimindeki
  kaynak gerekçesi düzeltildi.
- **Unit 03:** `switch statement` ile `switch expression`, ayrıca colon ile
  arrow yazımı ayrı eksenlerde açıklandı. `do/while` için “bir kez” yerine
  “en az bir kez” sınırı korundu; pattern değişkeninin flow scope'u düzeltildi.
- **Unit 04:** `Which of the following ...?` yapısının doğrudan soru olduğu
  açıklandı. `indent()` metodunun son satır sonuna etkisi kaynak cevabının
  gerekçesinde belirtildi.
- **Unit 05:** Pass-by-value ile nesnenin içeriğinin değiştirilmesi ayrıldı;
  gövdesiz metotlar için `native` istisnası ve non-void metotlarda normal
  tamamlanmama olasılığı ele alındı.
- **Unit 06–07:** Inheritance / hiding / override sınırları ve sealed
  hiyerarşide record/enum türlerinin örtük modifier'ları açıklandı.
- **Unit 08–10:** Lambda, variance ve stream bağlamlarında cümle çözümlemesi
  geliştirildi; `findFirst()` predicate alıyormuş izlenimi veren açıklama ve
  Stream tablosundaki OCR kaynaklı düzen bozukluğu düzeltildi.
- **Unit 11–15:** Resource, module, concurrency, dosya ve JDBC örneklerinin
  Türkçe karşılıkları geliştirildi; try-with-resources içinde uygun `final`
  field kullanımı, paralel çıktı sırası ve koşul cümlelerinin varsayımları
  netleştirildi.

15 ünitenin **Summary** ve **Exam Essentials** bölümleri ayrıca tarandı.
Tespit edilen OCR birleşmeleri, kip/anlam hataları ve doğal olmayan Türkçe
cümleler düzeltildi. Sınav öncesi tekrar metinlerinde kaynak yargısı ile Java 17
istisnasının birbirine karışmamasına dikkat edildi.

Kaynak kitaptaki cevap ile Java 17 açıklaması arasında sorun görüldüğünde,
kaynağın söylediği ile editör açıklaması ayrı gösterildi. `Official Answer`
başlığı kitabın Appendix cevaplarını izler; gerçek sertifika sınavı sorusu
veya cevap anahtarı iddiası taşımaz.

## Kullanılacak belgeler

- [Günlük çalışma planı](study_plan.md) · [PDF](study_plan.pdf): 25–30 dakikalık
  oturum, çözümlü cümle analizi, kişisel kelime seçimi ve yanlış günlüğü.
- [Çalışma Merkezi](README.md): 15 ünitenin girişleri ve materyal bağlantıları.
- Her ünitenin `README.md` dosyası: konulara ve sorulara bağlı çalışma rotası.
- Her ünitenin `bilingual_notes.md/pdf` dosyası: kaynak okuması, Review
  Questions ve kaynak cevapları.
- Her ünitenin `vocabulary.md/pdf`, `grammar_notes.md/pdf` ve
  `practice_quiz.md/pdf` dosyaları: bağlama bağlı dil çalışması ve ölçme.

## Doğrulama kapsamı

- 356 kaynak sorusunun cevap harfleri, kaynak PDF'nin Appendix bölümünden
  bağımsız çıkarılan anahtarla karşılaştırıldı; tamamı eşleşti. Bu kontrol,
  kitabın bütün gerekçelerinin hatasız olduğu anlamına gelmez.
- Ana metindeki fiziksel kaynak sayfası işaretlerinin 1–908 sırasını koruduğu
  kontrol edildi. English/Türkçe blok sayıları, kod çitleri ve yerel dosya/başlık
  bağlantıları denetlendi. Sayfa işaretleri tek başına tüm kaynak metnin
  kelime kelime eksiksiz olduğunu kanıtlamaz.
- Yeni quiz kodları gerçek JDK 17 ile denendi; beklenen derleme hataları,
  çalışma zamanı istisnaları ve normal çıktılar ayrı kontrol edildi.
- PDF'ler düzenlenebilir Markdown kaynaklarından üretildi. Bütün sayfalar
  görüntüye dönüştürüldü; metin sınırları ve belge içi bağlantılar tarandı.
  Genel sayfa düzeni küçük sayfa görselleriyle, yoğun/yeni içerikler ayrıca
  büyütülmüş sayfalarla incelendi.
  Son üretimde **76 PDF / 1.955 sayfa** bulunur. Markdown, PDF ve render
  dosyalarının aynı son sürüme ait olduğu dosya özetleriyle kontrol edildi.
- Görsel kontrolde bulunan satır numarasının liste numarasına dönüşmesi,
  bölünen alıntı kutuları, ham vurgu işaretleri ve gereksiz zorunlu sayfa
  kırılmaları düzeltildi; etkilenen sayfalar yeniden kontrol edildi.
- Kaynak kitapta bulunan bütün Java kodları çalıştırılmış değildir. JDBC için
  gerçek bir veritabanı sürücüsü eklenmedi; dil/API derleme kontrolü ile gerçek
  veritabanı davranışını doğrulama ayrı tutuldu.

1/3/7/14 gün tekrar aralıkları ve geçiş ölçütleri uygulanabilir bir başlangıç
önerisidir. Kullanıcının kelime bilgisi veya tamamladığı çalışmalar adına
otomatik başarı işareti konmadı.
