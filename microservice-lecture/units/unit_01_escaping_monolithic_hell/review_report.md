# Ünite 01 · Kalite kontrol raporu

## Teslim kapsamı

Kaynak PDF'nin **1–32. sayfalarındaki birinci bölüm bütünüyle** işlendi. Diğer 12 bölümün başlangıç ve bitişleri [ünite haritasında](../../README.md) kayıtlıdır; bu teslimde çevrilmemiştir.

| Belge | Sayfa | İçerik |
|---|---|---|
| [bilingual_notes.pdf](bilingual_notes.pdf) | 62 | 266 İngilizce–Türkçe paragraf/madde/şekil açıklaması çifti; 16 özgün şekil; iki dilli SOA tablosu; özgün tekrar eki |
| [vocabulary.pdf](vocabulary.pdf) | 18 | 68 alfabetik madde; bağlam, sözcük türü, örnek, çeviri ve ilişkili kelimeler; 10 soruluk alıştırma |
| [grammar_notes.pdf](grammar_notes.pdf) | 14 | 18 dil yapısı; kaynakla eşleştirilmiş 38 örnek/parça; formüller, YDS ipuçları ve 12 soruluk alıştırma |

PDF'ler aynı adlı Markdown kaynaklarından üretildi. PDF içeriği ayrıca elle düzenlenmedi.

## Metin ve kaynak denetimi

- Bölüm ve alt bölüm sırası, bütün düz metin paragrafları, liste maddeleri, kutu metinleri ve şekil açıklamaları kaynakla karşılaştırıldı. Eksik kaynak paragrafı veya şekil açıklaması saptanmadı.
- Sayfa sonlarında bölünen paragraflar birleştirildi; OCR/kopyalama kaynaklı sözcük ve URL bölünmeleri giderildi. Görsel içindeki İngilizce etiketler ayrıca paragraf sayılmadı.
- Ana kaynakta 266 English ve 266 Türkçe bloğu var. PDF'de ek iki dilli tablo başlığıyla birlikte 267/267 etiket bulunuyor; sıra EN→TR ve sayfa bazındaki sayılar eşit.
- Grammar belgesinin 38 İngilizce örneği veya açıkça belirtilmiş parçası, kaynak PDF'de verilen sayfalarla eşleşiyor. Son PDF'de 38/38 dil bloğu var.
- Sözlük 68 benzersiz ve alfabetik maddeden oluşuyor; her maddede tür, Türkçe anlam, kaynak bağlamı, EN/TR örnek ve ilişkili kelime bilgisi var.
- Kaynak dışı teknik açıklamalar ve özgün çalışma soruları açıkça işaretlendi. Kitabın dönemsel teknoloji iddiaları güncel öneri gibi sunulmadı.

## Görseller

- Şekil **1.1–1.16** kaynak PDF'den 240 dpi olarak çıkarıldı. Çizim, renk, ok ve İngilizce etiketlere müdahale edilmedi; kaynak açıklaması ayrı çevrilmek üzere kırpım dışında bırakıldı.
- 14 kaynak şekil sayfası ve 16 kırpım görsel olarak kontrol edildi. [Görsel manifesti](assets/manifest.json) sayfaları, koordinatları ve SHA-256 değerlerini içeriyor.
- PDF içindeki 16 görsel tekrar çıkarılıp PNG dosyalarıyla RGB piksel düzeyinde karşılaştırıldı: **16/16 görselde boyutlar ve bütün pikseller aynı**.
- Kaynak PDF ve bütün PNG dosyalarının SHA-256 değerleri manifestle karşılaştırıldı; eşleşiyor.

## PDF görünümü ve sayfa kırılmaları

- Ana PDF'nin 62, vocabulary PDF'nin 18 ve grammar PDF'nin 14 sayfasının tamamı render edilerek incelendi. Geçici render dosyaları ders klasörüne eklenmedi.
- İngilizce–Türkçe çiftleri, şekil/açıklama birlikteliği, sayfa sonları, Türkçe karakterler, font boyutları, kontrast, tablolar, başlıklar ve sayfa numaraları kontrol edildi.
- Vocabulary alıştırmalarının ikinci kısmındaki numaralandırma 7–10 olarak düzeltildi. Grammar kaynak örnekleri ve çevirileri aynı kart çiftinde toplandı; formüllerin sayfalar arasında bölünmesi giderildi.
- Son PDF'lerin sözcük koordinatları `pdftotext -bbox-layout` ile kontrol edildi: **sayfa dışına taşan sözcük 0**, **bozuk karakter göstergesi U+FFFD 0**, **boş sayfa 0**.
- Ana PDF'de bütün paragraf çiftleri aynı sayfada; 16 şekil de kendi EN/TR açıklamasıyla aynı sayfada. Büyük şekillerin birlikte tutulması bazı sayfalarda daha geniş alt boşluk bırakıyor.

## Dosya düzeni

- README bağlantıları, yerel görsel yolları, başlıklar, iç bağlantılar ve Markdown kod çitleri kontrol edildi.
- Bu ünitede derlenebilir tam Java kod örneği bulunmadığı için Java/Maven testi gerekmiyor.
- Mevcut OCP ders dosyaları ve kaynak PDF değiştirilmedi. Yeni bağımlılık, Git commit veya uzak depoya gönderim yapılmadı.

## Yeniden üretme

[PDF üretim yönergesindeki](../../tools/README.md) komutlar kullanılabilir. Metin değişiklikleri önce Markdown kaynağına yapılmalı, ilgili PDF yeniden üretilmeli ve etkilenen sayfalar kontrol edilmelidir.
