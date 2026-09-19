# Ünite 09 · Doğrulama raporu

**Tarih:** 19 Eylül 2026. **Kaynak:** Kullanıcının sağladığı *Microservices Patterns*, bölüm 9, PDF sayfaları 292–317.

## Tamamlanan içerik

- Kaynak çıkarımındaki **227 kayıt** ana notta aynı kimlik ve sırayla bulunuyor; kayıp veya yinelenen kayıt yok.
- **187 English–Türkçe blok çifti**, çevrilmiş başlıklar, **7 dil etiketli kod bloğu** ve **11 kaynak şekli** korundu.
- Sözlükte **54 alfabetik kelime kartı**, grammar kaynağında **30 gözden geçirilmiş İngilizce–Türkçe örnek** bulunuyor.
- `bilingual_notes.md`, `vocabulary.md` ve `grammar_notes.md` düzenlenebilir kaynaklardır; PDF’ler bu dosyalardan üretildi. README bütün sürümlere bağlantı verir.

Özellikle **lead time**, **subject it to testing**, **used interchangeably**, **to and from JSON**, **solitary/sociable test** ve **compile-time test** ifadeleri düzeltildi veya açıklandı. Kaynak Kod Listeleri 9.5–9.7’de görülen eksik parantez, yardımcı metot adı ve fluent zincir sorunları ilgili listelerde editör notuyla işaretlendi.

## PDF ve görsel kontrol

| PDF | Sayfa |
|---|---:|
| Ana çift dilli ders | 49 |
| Vocabulary | 21 |
| Grammar | 12 |
| **Toplam** | **82** |

Üç PDF’nin **bütün sayfaları** Poppler ile PNG olarak render edildi ve bütün contact sheet’ler görsel olarak incelendi. Paragraf çiftleri, kaynak sırası, şekil açıklamaları, kodlar, Türkçe karakterler ve sayfa kırılmaları kontrol edildi. Yoğun kod, şekil/tablo ve grammar sayfaları ayrıca büyük görünümde incelendi. Görünür metin taşması, kesilme, eksik görsel, bozuk Türkçe karakter veya istemsiz boş sayfa bulunmadı. Uzun kodlar gerektiğinde sonraki sayfada sürer; PDF görünümünde sarılan satırlar ASCII `-> ` işaretiyle belirtilir, Markdown kodunda bu görsel işaret yer almaz.

Ek olarak `pdftotext -bbox` çıktıları üzerinde sayfa dışına taşan sözcük ve boş sayfa kontrolü yapıldı: **0 taşma, 0 boş sayfa**. Markdown’daki yerel bağlantılar, kod çitlerinin eşleşmesi, English/Türkçe sayılarının eşitliği ve kaynak kayıt sırası programatik olarak doğrulandı. Sözlük kartları ve sayfaya sığan grammar konu bölümleri birlikte tutulur. En fazla 10 görsel satır içeren kısa kod blokları da bölünmeden aynı sayfada tutulur. Son üretimde ana PDF yeniden render edildi; bütün sayfalar önceki incelenmiş görüntülerle piksel düzeyinde eşit çıktı.

## Doğrulamanın sınırları

Java/Spring, Groovy sözleşme ve Gherkin parçaları kaynak kitaptaki uygulama bağlamına aittir. Eksik import, fixture ve harici framework bağımlılıkları olan bu parçalar bağımsız Java 17 programı olarak derlenmedi; integration/component testler çalıştırılmadı. Kaynakta bulunan somut sözdizimi sorunları yukarıda belirtilen editör notlarıyla ayrıştırıldı. Maven/Java uygulama dosyası veya bağımlılık değiştirilmedi. Teknoloji sürümleri ve tarihsel ürün iddiaları güncel ürün bilgisi olarak sunulmadı; dış bağlantıların çevrimiçi erişilebilirliği bu çalışmada denetlenmedi.

Render ve otomatik denetim ara dosyaları ders klasörlerine eklenmedi; yerel inceleme klasörü `/tmp/ms_final_review_u09/` altında tutuldu.

Son ana PDF: **49 sayfa**; SHA-256: `a80cd68ca55c8e8cda2264ee24665b84f954aeb461d952a1c15eb8e0669410c4`. Son karşılaştırma ve render kayıtları `/tmp/ms_shortcode_final/unit_09_testing_microservices_part_1/bilingual_notes/` altında; yukarıdaki yerel inceleme klasörünün manifesti de son PDF ile güncellendi.
