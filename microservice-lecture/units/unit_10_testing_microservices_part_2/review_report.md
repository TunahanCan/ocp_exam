# Ünite 10 · Doğrulama raporu

**Tarih:** 19 Eylül 2026. **Kaynak:** Kullanıcının sağladığı *Microservices Patterns*, bölüm 10, PDF sayfaları 318–347.

## Tamamlanan içerik

- Kaynak çıkarımındaki **249 kayıt** ana notta aynı kimlik ve sırayla bulunuyor; kayıp veya yinelenen kayıt yok.
- **178 English–Türkçe blok çifti**, çevrilmiş başlıklar, **22 dil etiketli kod bloğu** ve **8 kaynak şekli** korundu. Tablo 10.1’in bütün başlık ve hücrelerinde EN/TR karşılıkları yer alıyor.
- Sözlükte **44 alfabetik kelime kartı**, grammar kaynağında **26 gözden geçirilmiş İngilizce–Türkçe örnek** bulunuyor.
- `bilingual_notes.md`, `vocabulary.md` ve `grammar_notes.md` düzenlenebilir kaynaklardır; PDF’ler bu dosyalardan üretildi. README bütün sürümlere bağlantı verir.

Özellikle **making the tests unreliable** ifadesindeki ters anlam, sipariş oluşturma/değiştirme/iptal etme eylemleri, **out-of-process**, **annotated with** ve **hook method** çevirileri düzeltildi. Kaynaktaki BaseHttp/HttpBase, OrderRepository/OrderController, OrderResponse, sözleşmeye 10.3 başvurusu, Reply/reply kanal adı ve expired/invalid kart tutarsızlıkları editör notlarıyla işaretlendi. Kod Listesi 10.15’in sonundaki yanlış `]`, açık editör notuyla `}` yapıldı.

## PDF ve görsel kontrol

| PDF | Sayfa |
|---|---:|
| Ana çift dilli ders | 51 |
| Vocabulary | 18 |
| Grammar | 12 |
| **Toplam** | **81** |

Üç PDF’nin **bütün sayfaları** Poppler ile PNG olarak render edildi ve bütün contact sheet’ler görsel olarak incelendi. Paragraf çiftleri, kaynak sırası, şekil açıklamaları, kodlar, Türkçe karakterler ve sayfa kırılmaları kontrol edildi. Yoğun kod, şekil/tablo ve grammar sayfaları ayrıca büyük görünümde incelendi. Görünür metin taşması, kesilme, eksik görsel, bozuk Türkçe karakter veya istemsiz boş sayfa bulunmadı. Uzun kodlar gerektiğinde sonraki sayfada sürer; PDF görünümünde sarılan satırlar ASCII `-> ` işaretiyle belirtilir, Markdown kodunda bu görsel işaret yer almaz.

Ek olarak `pdftotext -bbox` çıktıları üzerinde sayfa dışına taşan sözcük ve boş sayfa kontrolü yapıldı: **0 taşma, 0 boş sayfa**. Markdown’daki yerel bağlantılar, kod çitlerinin eşleşmesi, English/Türkçe sayılarının eşitliği ve kaynak kayıt sırası programatik olarak doğrulandı. Sözlük kartları ve sayfaya sığan grammar konu bölümleri birlikte tutulur. En fazla 10 görsel satır içeren kısa kod blokları da bölünmeden aynı sayfada tutulur. Son üretimde ana PDF yeniden render edildi; bütün sayfalar önceki incelenmiş görüntülerle piksel düzeyinde eşit çıktı.

## Doğrulamanın sınırları

Java/Spring, Groovy sözleşme ve Gherkin parçaları kaynak kitaptaki uygulama bağlamına aittir. Eksik import, fixture ve harici framework bağımlılıkları olan bu parçalar bağımsız Java 17 programı olarak derlenmedi; integration/component testler çalıştırılmadı. Kaynakta bulunan somut sözdizimi sorunları yukarıda belirtilen editör notlarıyla ayrıştırıldı. Maven/Java uygulama dosyası veya bağımlılık değiştirilmedi. Teknoloji sürümleri ve tarihsel ürün iddiaları güncel ürün bilgisi olarak sunulmadı; dış bağlantıların çevrimiçi erişilebilirliği bu çalışmada denetlenmedi.

Render ve otomatik denetim ara dosyaları ders klasörlerine eklenmedi; yerel inceleme klasörü `/tmp/ms_final_review_u10/` altında tutuldu.

Son ana PDF: **51 sayfa**; SHA-256: `ff322d5ea277b1d828ee33d18c9c461f350fa82116bc506d50f62e5dae20d506`. Son karşılaştırma ve render kayıtları `/tmp/ms_shortcode_final/unit_10_testing_microservices_part_2/bilingual_notes/` altında; yukarıdaki yerel inceleme klasörünün manifesti de son PDF ile güncellendi.
