# Microservices Patterns · Devam çalışması ve kalite raporu

**Tarih:** 19 Eylül 2026.

## Kapsam ve sonuç

Önceki çalışmada 01–08. ünitelerin ana dersleri ile 13 ünitenin vocabulary/grammar kaynakları bulunuyordu. Eksik **09–13. ünitelerin çift dilli ana dersleri** tamamlandı; 02–13. ünitelerin giriş sayfaları oluşturuldu. Artık 13 ünitenin her birinde ana ders, vocabulary ve grammar için düzenlenebilir Markdown ile ondan üretilen PDF bulunur. Bütün bağlantılar [çalışma merkezinde](README.md) toplanmıştır.

Kaynak, kullanıcının sağladığı `Microservices_Patterns_1_Bolumden_Itibaren.pdf` dosyasıdır. Numaralı 13 bölüm fiziksel PDF sayfaları 1–471 arasındadır. Bölüm sonrasındaki dizin ve tanıtım sayfaları ders kapsamına alınmamıştır. Kaynak PDF ve **188 özgün şekil varlığı** değiştirilmemiştir.

## Materyal envanteri

Her satır, aynı ünitenin üç çalışma PDF’sinin sayfa sayısını gösterir.

| Ünite | Ana ders | Vocabulary | Grammar |
|---|---:|---:|---:|
| 01 | 62 | 18 | 17 |
| 02 | 56 | 22 | 13 |
| 03 | 81 | 22 | 13 |
| 04 | 64 | 20 | 13 |
| 05 | 62 | 19 | 12 |
| 06 | 67 | 18 | 13 |
| 07 | 60 | 18 | 12 |
| 08 | 69 | 17 | 13 |
| 09 | 49 | 21 | 12 |
| 10 | 51 | 18 | 12 |
| 11 | 63 | 22 | 13 |
| 12 | 87 | 25 | 13 |
| 13 | 76 | 31 | 15 |

**Toplam: 39 PDF, 1.289 sayfa.** Markdown ve PDF hash’leriyle makinece okunabilir son envanter [verification_manifest.json](verification_manifest.json) dosyasındadır.

## İçerik çalışması

- Yeni tamamlanan 09–13. üniteler, kaynak PDF’nin 292–471. sayfalarını kapsar. Yapılandırılmış çıkarımdaki **1.581 kayıt**, **61 kod/çıktı bloğu** ve **74 özgün şekil**, kaynak sırası korunarak ana derslere aktarıldı. English/Türkçe paragraflar ardışık yerleştirildi; OCR düzeltmeleri ve teknik açıklamalar kaynak çevirisinden ayrıldı.
- 02–13. ünitelerin grammar kaynaklarındaki mevcut örnek çevirileri gözden geçirilip düzeltildi. Olumsuzluk, zamir göndergesi, cümle öğeleri ve teknik sözcüklerin anlamını bozan çeviriler giderildi. Yeni ünitelerin sözlükleri kendi bağlamlarına uygun terimlerle geliştirildi.
- 02–08. ünitelerin mevcut ana dersleri korundu. İncelemede bulunan `Pattern` başlıkları, tablo hücreleri, kredi kartı provizyonu bağlamı ve GraphQL cümlesindeki anlam sırası gibi belirli sorunlar düzeltildi. Bu işlem, önceki bütün ana derslerin baştan çevrildiği anlamına gelmez.
- Her ünitenin kendi vocabulary ve grammar kaynakları, mini quiz’leri ve cevapları vardır. Ünite README’leri öğrenme hedeflerini, okuma rotasını ve çalışma dosyalarını birbirine bağlar.

Yeni ünitelerin ayrıntılı kontrolleri: [09](units/unit_09_testing_microservices_part_1/review_report.md), [10](units/unit_10_testing_microservices_part_2/review_report.md), [11](units/unit_11_developing_production_ready_services/review_report.md), [12](units/unit_12_deploying_microservices/review_report.md), [13](units/unit_13_refactoring_to_microservices/review_report.md).

Kaynak kayıt sayımı, yapılandırılmış çıkarımdan Markdown’a aktarımın kapsamını gösterir. Kaynak PDF ile bağımsız ikinci bir kelime-kelime karşılaştırma veya bütün tarihsel teknik iddiaların güncellik doğrulaması değildir. Güncel bir teknik ayrım gerektiğinde ilgili notta birincil kaynak gösterilmiştir.

## PDF düzeni ve görsel kontrol

PDF’lerin bütün sayfaları geçici PNG görsellerine render edildi; tüm sayfaların küçük görselleri temas sayfalarında incelendi. Yoğun kodlar, tablolar, şekiller ve şüpheli sayfa kırılmaları ayrıca büyütülerek kontrol edildi. Son düzen değişikliklerinden sonra etkilenen PDF’ler yeniden üretildi; değişen sayfalar tekrar incelendi. Görünümü değişmeyen yeniden üretimlerde önceki kontrol sürümüyle piksel veya metin/bbox eşitliği kullanıldı.

Kontrolde düzeltilen başlıca düzen sorunları:

- Vocabulary kartları ile sayfaya sığan grammar konularının ayrı sayfalara bölünmesi.
- Kısa SQL ifadelerinin, koşulların ve kod açıklaması etiketlerinin tek satırının sonraki sayfaya taşınması.
- Fontta bulunmayan kod devam okunun kare olarak görünmesi; PDF görünümünde ASCII `->` kullanıldı.
- 02 ve 06 vocabulary quiz’lerinin gereksiz bölünmesi; 02’de bir tablo satırının İngilizce/Türkçe içeriğinin ayrılması.

Son görsel incelemede kesilmiş şekil, sayfa dışına taşan metin veya bozuk Türkçe karakter görülmedi. İngilizce/Türkçe paragraf eşleşmeleri ve şekil açıklamaları birlikte kontrol edildi. Uzun kodlar gerektiğinde sonraki sayfaya devam eder; kartların birlikte tutulduğu bazı sayfalarda bilinçli boşluk kalır.

## Yapısal doğrulama ve sınırlar

[Denetim aracı](tools/audit_study_materials.py) ile 13 ünitenin gerekli dosyaları, yerel dosya bağlantıları, tek ana başlık kullanımı, kod bloklarının kapanışı, English/Türkçe etiket sırası, kaynak kayıtlarının sırası ve şekil envanteri kontrol edildi. `pdftotext -bbox-layout` ile sayfa sınırları ve boş içerik sayfaları tarandı. Ana PDF’lerde sayfa başına English/Türkçe etiket sayıları arasında fark bulunmadı. Bu sayım tek başına anlam doğruluğu kanıtı değildir.

Kaynak PDF’nin SHA-256 değeri özgün kaynak haritasıyla eşleşir. `git diff --check` ve değişen Python araçlarının sözdizimi kontrolü yapıldı. Yeni bağımlılık eklenmedi. Java/Maven uygulama kaynakları değişmediği için Maven testi çalıştırılmadı.

Kitaptaki Java, Docker, Kubernetes, Spring, AWS ve test örnekleri tarihsel kaynak bağlamıyla sunulur. Eksik kod parçaları bağımsız Java 17 programları olarak tanıtılmadı; servisler kurulup entegrasyon testleri çalıştırılmadı. Ünite 12’deki YAML sözdizimi ve ünite 13’teki seçili derleme kontrollerinin kapsamı, kendi raporlarında açıklanır.

PDF güncelleme ve denetim komutları [araç rehberindedir](tools/README.md). Eski ünite raporları önceki kontrol tarihlerini anlatır; bu rapor ve bağlantılı doğrulama kaydı mevcut teslimi esas alır.
