# Çalışma Dokümanları · İnceleme ve İyileştirme Kaydı

**İnceleme tarihi:** 9 Eylül 2026.

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
