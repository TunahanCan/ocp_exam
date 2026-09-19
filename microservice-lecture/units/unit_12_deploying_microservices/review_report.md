# Ünite 12 · Kaynak aktarımı ve çalışma materyali kontrolü

**Tarih:** 19 Eylül 2026.

## Kapsam

Kaynak: kullanıcının sağladığı *Microservices Patterns*, **Deploying microservices**, kaynak PDF sayfaları **383–427**; toplam 45 sayfa.

Kaynak PDF SHA-256: `0ed35ffec713a7a929df1efcd2aaf8f153c70aa3b918c1bbc6ccdd50d549d382`.

| Materyal | Son içerik | PDF |
|---|---|---:|
| [Ana çift dilli ders](bilingual_notes.md) | 337 English/Türkçe çifti, 79 kaynak başlığı, 26 kod/komut bloğu, 15 şekil | [87 sayfa](bilingual_notes.pdf) |
| [Vocabulary](vocabulary.md) | 63 alfabetik kart, terim karşılaştırmaları ve özgün mini quiz | [25 sayfa](vocabulary.pdf) |
| [Grammar](grammar_notes.md) | 19 konu başlığı, 36 iki dilli kaynak örneği ve özgün mini quiz | [13 sayfa](grammar_notes.pdf) |

## Metin ve dil kontrolü

- Yapılandırılmış kaynak çıkarımındaki **440 kaydın tamamı** Markdown içinde aynı sırada bulunur. Bunlar 186 prose, 79 heading, 79 item, 55 annotation, 26 code ve 15 figure kaydıdır. Kod dışındaki 414 kayıt tek tek okunup çevrildi. Başlangıçta birleşmiş bir paragraf ve liste/sonraki açıklama ayrılarak 337 ardışık paragraf/madde/açıklama çifti oluşturuldu.
- English/Türkçe etiket sırası ve sayıları, 26 kod bloğunun kapanışı, kaynak kayıt kimlikleri ve 15 yerel şekil bağlantısı doğrulandı. Şekillerin sırası 12.1–12.15’tir. Kaynak şekil varlıkları değiştirilmedi.
- Çeviri yerel makine çevirisiyle üretilmedi. Deployment/release, readiness/liveness, registry türleri, process/container/VM ve Lambda handler terimlerinin anlam ayrımları korundu.
- Mevcut grammar dosyasındaki **33 örneğin Türkçe çevirisi** yeniden düzenlendi. Özellikle olumsuzluğun tersine dönmesi, whether belirsizliğinin silinmesi, özne/nesne kayması ve teknik terimlerin yanlış çevrilmesi düzeltildi. Mevcut embedded questions başlığına whether ayrıntısı eklendi; iki yeni yapı ayrı başlıkta ele alındı.
- Vocabulary içindeki orchestration, registry, rollback, retrieve, in isolation ve view maddeleri bu ünitenin dağıtım bağlamına uyarlandı. 22 yeni bağlamsal kart eklendi; alfabetik düzen korundu.

440 kayıt kontrolü, çıkarımdan Markdown’a aktarımın eksiksizliğini gösterir; kaynak PDF’nin bütün metninin bağımsız ikinci bir çıkarımla kelime kelime eşleştiği iddiası değildir. Kaynakta sorun görülen kod ve paragraf bölümleri ayrıca PDF metniyle karşılaştırıldı.

## Kaynak hataları ve teknik açıklamalar

Kaynağın tarihsel örnekleri korunurken ayrı editör kutuları eklendi:

- Docker `--interval` seçeneği, komutlardaki yollar ve bölünen Java identifier’ı birleştirildi. YAML girintileri düzeltildi; kaynakta yinelenen `image: image:` ifadesi açık notla tek anahtara indirildi.
- Kaynağın readiness için verdiği 30 saniye ile YAML’daki 60 saniye ayrıldı. `--start-period` başlangıç toleransı ile ilk kontrol gecikmesi arasındaki fark, [Docker belgesi](https://docs.docker.com/reference/dockerfile/#healthcheck) ile doğrulandı.
- NodePort örneğindeki Consumer Service/API Gateway, 8082/8080 ve 3000/30000 uyuşmazlıkları, gösterilen YAML’a dayanılarak işaretlendi.
- Secret ile ConfigMap’in ayrı nesne türleri olması [Kubernetes belgesi](https://kubernetes.io/docs/concepts/configuration/secret/) üzerinden kontrol edildi.
- `Long.parseLong(null)` davranışı [Java 17 API belgesi](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) ile; servlet `service(...)` metodunun parametreleri ve `void` dönüşü [Servlet 4 API belgesi](https://jakarta.ee/specifications/servlet/4.0/apidocs/javax/servlet/http/httpservlet) ile karşılaştırıldı.
- Static context ile instance kilidinin genel eşzamanlılık garantisi vermediği, gösterilen koddan çıkarılan bir sınır olarak belirtildi.

**10 YAML bloğu**, mevcut PyYAML ile sözdizimi açısından ayrıştırıldı. Bu kontrol, eksik örneklerin tam Kubernetes manifest’i olduğunu veya hedef platform API’lerine uyduğunu kanıtlamaz. Docker/Kubernetes/Istio/AWS dağıtımı yapılmadı. Kaynak Java parçaları haricî kütüphanelere ve eksik gövdelere bağlı olduğundan bağımsız Java 17 programı olarak derlenmedi. Ortamda bulunan JDK 21, Java 17 testi yapılmış gibi sunulmadı.

## PDF ve görsel kontrol

- Üç PDF, düzenlenebilir Markdown dosyalarından ortak üreticiyle oluşturuldu: **125 sayfa**.
- Bütün sayfalar 75 dpi PNG’ye render edildi; **15 temas sayfasındaki bütün küçük sayfa görselleri** incelendi. İngilizce/Türkçe birlikteliği, şekil/caption sırası, Türkçe karakterler, kodlar, kartlar, grammar formülleri ve sayfa kırılmaları kontrol edildi.
- Ana dersin 40, 77 ve 83. sayfaları ile grammar’ın 12. sayfası ayrıca 1600 piksel görüntülerde incelendi.
- Bu kontrolde kod satırı devamındaki Unicode okun kare olarak göründüğü saptandı. Ortak üreticide ASCII `->` devam işareti kullanılarak düzeltildi. Ana PDF yeniden üretildi; 87 sayfasının tamamı yeniden render edildi. Önceki render ile piksel karşılaştırmasında yalnız 25, 42, 57 ve 83. sayfalar değişti; bu dört son sayfa ayrıca gözden geçirildi. Devam işareti PDF görünümüne aittir, Markdown kodunun parçası değildir.
- Kısa kod bloklarını aynı sayfada tutan son üretici güncellemesinden sonra ana PDF bir kez daha üretildi ve 87 sayfanın tümü yeniden render edildi. Son render, daha önce incelenen düzeltilmiş render ile sayfa sayfa piksel karşılaştırmasında aynıdır; bu güncelleme Ünite 12 yerleşimini değiştirmedi.
- `pdftotext -bbox-layout` denetiminde sayfa dışına taşan sözcük ve boş içerik sayfası bulunmadı. Metin çıkarımında U+FFFD bozuk karakteri bulunmadı. Ana PDF’de 337 English etiketi doğrulandı.
- Uzun kodlar bir sonraki sayfaya devam edebilir. Bazı sayfalardaki boşluklar, şekil/caption veya çift dilli kartların birlikte tutulmasından kaynaklanır. Son dosyalarda kesilmiş görsel, taşan metin veya ayrılmış kelime kartı görülmedi.

Geçici doğrulama çıktıları `/tmp/ms_u12_work/` altında tutuldu. Kalıcı ders kaynakları ve PDF’ler bu ünite klasöründedir; giriş bağlantıları [README](README.md) içindedir.
