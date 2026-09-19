# Ünite 13 · İçerik ve PDF kontrol raporu

**Kontrol tarihi:** 19 Eylül 2026

## Kapsam

Kullanıcının sağladığı *Microservices Patterns* kaynak PDF’sinin 428–471. sayfaları (44 kaynak sayfası) işlendi. Ana ders bir özet değildir; çıkarılan bölüm metnini kaynak sırasıyla İngilizce–Türkçe verir.

| Öğe | Sonuç |
|---|---:|
| Kaynak kaydı | 349 |
| Paragraf kaydı | 180 |
| Liste maddesi | 88 |
| Başlık | 56 |
| Şekil | 23 |
| Kod bloğu | 2 |
| İki dilli okuma kartı | 292 |
| Vocabulary maddesi | 85 |
| Grammar konusu | 24 |
| Ana ders PDF | 76 sayfa |
| Vocabulary PDF | 31 sayfa |
| Grammar PDF | 15 sayfa |

Başlıklar iki dilli başlık olarak, kodlar tek kez özgün dilinde verildi. 347 kod dışı kaydın tamamı çevrildi. Dondurma anısını ve ardından gelen FTGO açıklamasını tek kayıtta birleştiren aktarım, kaynak bağlamına uygun iki ardışık İngilizce–Türkçe çifte ayrıldı; bu nedenle başlık dışındaki kart sayısı 292’dir. Bu bölümde tablo kaydı yoktur.

## Metin ve teknik kontroller

- 349 `source-record` kimliğinin sırası çıkarılan kaynakla bire bir karşılaştırıldı; atlanan, yinelenen veya yer değiştiren kayıt yok.
- 292 English etiketi ile 292 Türkçe etiketi eşleşiyor. 23 şekil yolu mevcut ve iki kod bloğunun metni kaynak çıkarımıyla aynı.
- İngilizce metindeki bariz yazım, eksik edat ve sözcük bölünmesi hataları düzeltildi. Anlamı etkileyen “contract/contact”, “transaction logic/log tailing”, servis adı tutarsızlıkları ve feature toggle anlatımı için ayrı editör notları eklendi.
- Saga’da yeniden denenebilir işlemin başarı güvencesi, geçici ağ hatalarının hiç oluşmayacağı şeklinde yorumlanmaması için ayrı teknik notla açıklandı.
- Grammar kaynağındaki 34 mevcut örneğin Türkçe çevirisi anlam ve doğallık bakımından düzeltildi; bu bölümde geçen beş ek yapı işlendi.
- Vocabulary’ye 25 bağlamlı terim eklendi; alfabetik sıra korundu. Courier availability, kredi kartı provizyonu ve transition period anlamları netleştirildi.
- Markdown bağlantıları, görsel yolları ve kod çitleri kontrol edildi. README, her üç kaynağın Markdown ve PDF sürümlerine bağlanıyor.

## Kod doğrulaması

Sistemdeki **OpenJDK 21.0.9 `javac --release 17`** ile iki kaynak parçası geçici dizinde derlendi. Birincisi eksik noktalı virgül nedeniyle `';' expected`, ikincisi `...` yer tutucuları nedeniyle `illegal start of type` ve `<identifier> expected` hataları verdi. Her ikisinin kaynak hâli **derlenmez**; ilgili notlar ana derste kodların yanında bulunur. Java 17 çalışma zamanı altında uygulama testi yapılmadı. Java veya Maven projesi değiştirilmediği için `mvn test` çalıştırılmadı.

## PDF kontrolü

Üç PDF güncel ortak üreticiyle Markdown kaynaklarından yeniden üretildi. Görsel kontrole alınan sürümlerin bütün sayfaları `pdftoppm` ile görüntüye çevrildi; toplam 122 sayfa contact sheet’lerde yerleşim, eşleşme, sayfa kırılmaları, boş sayfa ve taşma açısından incelendi. Ana dersin kod, ayrıntılı şekil ve editör notu içeren sayfaları ile vocabulary/grammar örnek sayfaları yakın görünümde ayrıca kontrol edildi. Türkçe karakterler, iki dilli renk ayrımı, şekil açıklamaları ve monospace kodlar okunabilir durumda. PDF metin kutularının sayfa sınırlarını aşmadığı `pdftotext -bbox` çıktısıyla da denetlendi. Ana PDF’nin son yeniden üretimine ilişkin eşdeğerlik kontrolü aşağıda ayrıca belirtilmiştir.

## Sınırlar

Şekillerin içindeki özgün İngilizce etiketler korunmuştur; her şeklin açıklaması iki dillidir. Şirket ve teknoloji örnekleri kitabın tarihsel bağlamına aittir; dış bağlantıların güncelliği bu çalışmada kontrol edilmedi. Görsel kontrol bütün sayfaların genel yerleşimini ve seçilen yakın görünümleri kapsar; kaynak kitaptaki bütün teknik iddiaların bağımsız yeniden doğrulanması veya tam uygulamanın çalıştırılması anlamına gelmez. Düzenlenebilir ana kaynaklar Markdown dosyalarıdır.

## Son dosya doğrulamaları

Son ana PDF, kod satırı devam işareti ASCII `-> ` kullanan ve kısa kod bloklarını birlikte tutan güncel ortak üreticiyle yeniden oluşturuldu. Bu ünitedeki iki kısa kod bloğu satır bölünmesi gerektirmediğinden 76 sayfanın metni ve bbox konumları önceki görsel kontrol sürümüyle aynıdır; yalnızca PDF oluşturma zamanı değişmiştir.

Vocabulary kaynağının dosya sonundaki fazladan boş satır kaldırıldıktan sonra PDF yeniden üretildi; 31 sayfanın metni ve bütün bbox konumları önceki sürümle bire bir aynı bulundu. Bu değişiklik görünür içerik veya yerleşimi etkilemedi.

| Dosya | SHA-256 |
|---|---|
| bilingual_notes.md | `5fd48086462ea66023f2d9445859d870531385f48516384e3608e7f16febc3cf` |
| bilingual_notes.pdf | `14ed945063cbe07482bd4f9dd95a3a0e07363906bf13ab70b729d0fcde38c729` |
| vocabulary.md | `0a3e6b574ccc1cc3cebd4b07a2db56c12f4c5f3b18e73f4c7fab7139a2cf5631` |
| vocabulary.pdf | `56d83a3eaf446b1e921ce2d4b1a748f55a62f2abb70ebcc6bd8fb4383d4b744e` |
| grammar_notes.md | `6a9fbe60bc95fa915679d96f901f2cbc4447be13b4101bf1fcb3126c4a73afa7` |
| grammar_notes.pdf | `73996ba26e400f5efe6f24e7c9a57016ad8804dc1a60f2e57b59c065a8f2b848` |
