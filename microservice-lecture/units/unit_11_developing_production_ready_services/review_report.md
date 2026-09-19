# Ünite 11 · Kaynak aktarımı ve kalite kontrolü

**Tarih:** 19 Eylül 2026. Kaynak: kullanıcının sağladığı *Microservices Patterns*, bölüm 11, PDF’nin 348–382. sayfaları.

## Tamamlanan materyaller

| Materyal | İçerik | PDF |
|---|---|---:|
| [Çift dilli ana ders](bilingual_notes.md) | 267 English/Türkçe çifti, 316 kaynak kaydı, 17 özgün şekil, 4 kod/çıktı bloğu | [63 sayfa](bilingual_notes.pdf) |
| [Vocabulary](vocabulary.md) | 58 alfabetik kart, bağlamsal örnekler ve özgün mini quiz | [22 sayfa](vocabulary.pdf) |
| [Grammar](grammar_notes.md) | 18 dil yapısı, 33 kaynak örneği, cümle çözümleme ve özgün mini quiz | [13 sayfa](grammar_notes.pdf) |

## Metin ve teknik inceleme

- Kaynak çıkarımındaki 316 kayıt, kimlikleri ve sıraları korunarak aktarıldı. Başlıklar, şekil açıklamaları, maddeler ve paragraflar çevrildi; kodlar bir kez gösterildi. Birleşmiş üç kaynak kaydındaki ayrı paragraflar okuma sırası değiştirilmeden ayrıldı.
- İngilizce ve Türkçe etiketlerinin dönüşümlü sırası, 267 çift, kapalı kod blokları ve 11.1–11.17 şekil sırası kontrol edildi. Kaynak görsellerin dosyaları değiştirilmedi.
- Bölünmüş identifier’lar ve belirgin OCR yazım hataları düzeltildi. Vocabulary’ye 10 bağlamsal terim eklendi; `registry`, `feature` ve `view` maddeleri bu ünitedeki kullanıma göre geliştirildi.
- Mevcut grammar kaynağının 33 Türkçe örneği yeniden incelendi ve düzeltildi. `decrypt`, `principal`, `server is up` gibi anlamı bozan çeviriler giderildi; özne, zamir göndergesi ve olumsuzluk ilişkileri açıklandı.
- JWT imzası ile şifreleme, stateless doğrulamada iptal sınırı, OAuth authorization ile OpenID Connect authentication ayrımı ayrı teknik kutularda açıklandı. Tarihsel Password Grant örneğinin güncel kullanım kuralı kaynak metinden ayrı belirtildi. Dayanaklar ilgili kutularda RFC 7519, RFC 7009, RFC 9700 ve OpenID Connect Core bağlantılarıyla verildi.
- Kaynağın Exception tracking tanımındaki Audit logging bağlantısı için editör notu eklendi. Health check yanıt kodları ile service mesh ürünlerinin tarihsel karşılaştırması bağlam içinde açıklandı.

Kayıt sayımı, çıkarımdan Markdown’a aktarımın kapsamını doğrular; kaynak PDF ile bağımsız ikinci bir kelime-kelime karşılaştırma değildir. Dört kod/çıktı bloğu eksik kaynak uygulama parçalarıdır; bağımsız Java 17 programları olarak derlenmiş veya çalışan servisler üzerinde test edilmiş gibi sunulmaz.

## PDF ve görsel inceleme

Üç PDF, Markdown kaynaklarından üretildi. **98 sayfanın tamamı** PNG’ye render edilip temas sayfalarında görsel olarak incelendi; yoğun metin ve kod içeren sayfalar ayrıca büyütülerek kontrol edildi. Son üretimde ana dersin 63 sayfası yeniden render edilip tekrar incelendi.

English/Türkçe bloklarının birlikteliği, şekillerin açıklamaları, sayfa numaraları, Türkçe karakterler, kod satırları, vocabulary kartları ve grammar konu bütünlüğü kontrol edildi. Ortak üreticide kısa kodlar, kelime kartları ve sayfaya sığan grammar konuları birlikte tutuldu. Uzun kodlar gerektiğinde sayfa değiştirebilir; `->` yalnızca PDF’deki görsel satır devamını gösterir.

Son dosyaların hash’leri, sayfa sayıları, bağlantı ve PDF sınır kontrolleri [ortak doğrulama kaydındadır](../../verification_manifest.json). Kontrolün kapsamı ve diğer üniteler [genel raporda](../../review_report.md) açıklanır.
