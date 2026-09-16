# Ünite 03 · Ana ders kaynağı ve PDF kontrol raporu

## Kapsam ve sonuç

[Çift dilli Markdown](bilingual_notes.md) ve ondan üretilen [ana ders PDF'si](bilingual_notes.pdf) kontrol edildi. Kaynak, *Microservices Patterns* kitabının **Interprocess communication in a microservice architecture** başlıklı 3. bölümüdür: kaynak PDF'nin **65–109. sayfaları**, toplam **45 sayfa**.

- Kaynağın 22 numaralı bölüm/alt bölüm başlığı ve konu sırası korundu.
- **349 İngilizce–Türkçe paragraf/madde çifti** ve **18 çift dilli şekil açıklaması** bulunur: toplam **367 English / 367 Türkçe** bloğu.
- **2 tablo** ve **10 kod/komut bloğu** bulunur. Kodlar bir kez gösterilir; kaynak örneklerdeki API, sınıf ve metot adları korunur.
- **18 özgün şekil**, 3.1–3.18 sırasıyla kullanılır. Dosyalar, kaynak sayfaları ve kırpma koordinatları [görsel manifestinde](assets/manifest.json) kayıtlıdır.
- Üretilen ana PDF **81 sayfadır**.

## Kaynak kapsamının doğrulanması

Kaynak PDF'nin metin konumları çıkarıldı; grafik içindeki yazılar ve ayrı işlenen şekil açıklamaları ana metin akışından ayrıldı. Ardışık kaynak aralıkları başlık, paragraf, madde, tablo veya kod olarak eşleştirildi. Sayfa sonunda bölünen paragraflar birleştirildi; satır sonu tireleri ve belirgin aktarım hataları giderildi. Kapsam denetiminde **93.752 / 93.752 karakterlik normalleştirilmiş kaynak akışı işlendi; atlanan kaynak aralığı bulunmadı**. Şekil açıklamaları ayrıca manifestle karşılaştırıldı. Bu denetim, aktarım kapsamını ölçer; çevirinin otomatik anlamsal doğruluk puanı değildir.

Kaynak SHA-256: `0ed35ffec713a7a929df1efcd2aaf8f153c70aa3b918c1bbc6ccdd50d549d382`.

## PDF ve görsel kontrolü

PDF'nin **81 sayfasının tamamı** 90 dpi PNG'ye dönüştürüldü ve 21 temas sayfasında tek tek gözden geçirildi. Yoğun tablo içeren 6. sayfa, Protocol Buffers örneği içeren 24. sayfa ve Java örnekleri içeren 69. sayfa ayrıca 1600 piksel boyutunda incelendi.

- İngilizce blok ile hemen altındaki Türkçe karşılığı tutarlı biçimde ayrılıyor; eşleşme ve sıra korunuyor.
- Şekillerin etiketleri, okları ve sınırları kesilmiyor; şekil numarası ile açıklaması uyumlu.
- Türkçe karakterler, başlıklar, sayfa numaraları, tablolar ve kodlar okunabiliyor.
- Kesilmiş metin, sayfa dışına taşan metin, boş sayfa veya bozuk karakter gözlenmedi.
- Metin konumu denetimi de sayfa sınırını aşan sözcük bulmadı. PDF'den çıkarılan metinde 367 İngilizce ve 367 Türkçe etiket doğrulandı.
- Tablo 3.2 sonraki sayfaya başlık satırı tekrarlanarak devam ediyor. Bazı sayfalardaki boşluklar, şekil ve ilgili açıklamanın birlikte tutulmasından kaynaklanıyor.

İnceleme görselleri geçici olarak `/tmp/ms_pdf_review/unit03/bilingual/` altında tutuldu. PDF, `microservice-lecture/tools/generate_study_pdf.py` ile Markdown'dan üretildi.

## Editör notları ve sınırlar

Kaynakta tamamlanmamış API parçaları ve `...` yer tutucuları vardır; bunlar çalışır bağımsız program olarak sunulmadı ve derleme testi yapılmadı. Kaynaktaki `ORDERED BY` yazımı ve ilk Java örneğindeki değişken/noktalı virgül tutarsızlığı ayrı editör notuyla açıklandı. Kullanılabilirlik hesabındaki bağımsızlık varsayımı kısa teknik notla belirtildi. Tarihsel teknoloji değerlendirmeleri kaynak bağlamında çevrildi.

Bu rapor ana ders Markdown/PDF'sini kapsar. Ünitenin vocabulary ve grammar materyalleri ayrı dosyalardır.
