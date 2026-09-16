# Microservices çalışma PDF'lerini üretme

`generate_study_pdf.py`, düzenlenebilir Markdown kaynaklarını aynı adlı PDF'lere
dönüştürür. Mevcut `exam_lecture/tools/generate_study_pdf.py` dosyasının tipografisini
salt okunur biçimde kullanır; görsel desteği ve Microservices sayfa düzeni bu
klasörde tanımlanır.

## Kullanım

Projenin kök klasöründen tek belgeyi güncellemek için:

```bash
python3 microservice-lecture/tools/generate_study_pdf.py \
  microservice-lecture/units/unit_01_escaping_monolithic_hell/bilingual_notes.md
```

Aynı ünitenin üç çalışma belgesini birlikte güncellemek için:

```bash
python3 microservice-lecture/tools/generate_study_pdf.py \
  microservice-lecture/units/unit_01_escaping_monolithic_hell/bilingual_notes.md \
  microservice-lecture/units/unit_01_escaping_monolithic_hell/vocabulary.md \
  microservice-lecture/units/unit_01_escaping_monolithic_hell/grammar_notes.md
```

Her girdi kendi klasöründe aynı adla `.pdf` üretir. Tek girdi kullanırken
`--output /tmp/onizleme.pdf` ile farklı bir çıktı konumu seçilebilir. Araç yeni
bağımlılık kurmaz; mevcut Python ortamındaki ReportLab'i veya mevcut uv paket
önbelleğindeki ReportLab'i kullanır. Unicode fontları ortak üreticinin desteklediği
Arial veya DejaVu font ailelerinden yükler.

## Kaynak biçimi

Belgeyi `# Ünite 01 · Konu adı` biçiminde bir başlıkla başlat. `##` düzeyindeki
başlıklar için, kaynakta içindekiler bölümü bulunmuyorsa PDF'ye bağlantılı bir
içindekiler bölümü eklenir. Başlıklar PDF yer imlerine de dönüşür.

Her paragraf çifti şu biçimde yazılabilir:

```markdown
> **English:** Each service exposes an API.
>
> **Türkçe:** Her servis bir API sunar.
```

`>` işareti olmadan, ayrı paragraflardaki aynı dil etiketleri de desteklenir.
İngilizce açık mavi, Türkçe açık yeşil kartta gösterilir. Çift bir sayfaya
sığıyorsa birlikte tutulur. Tek sayfaya sığmayan uzun çiftlerde yinelenen dil
başlığı ve paragraf numarası, iki dil arasındaki ilişkiyi gösterir.

Şekli ayrı satıra yerleştir; hemen arkasına İngilizce ve Türkçe açıklamasını ekle:

```markdown
![Şekil 1.1](assets/figure_01_01.png)

> **English:** Figure 1.1 The structure of the application.
>
> **Türkçe:** Şekil 1.1 Uygulamanın yapısı.
```

Görsel yolu Markdown dosyasının bulunduğu klasöre göre çözülür. Görsel içeriği
değiştirilmez; en-boy oranı korunarak sayfaya sığdırılır. Şekil ile hemen
arkasındaki açıklama çifti birlikte tutulur. Açıklama verilmezse görselin köşeli
parantez içindeki alternatif metni kullanılır. Şekil açıklamasından sonra yeni
bir içerik paragrafına başlamadan önce boş satır bırak.

## Üretim sonrası görsel kontrol

PDF'nin bütün sayfalarını geçici bir klasöre render etmek için:

```bash
mkdir -p /tmp/microservices_pdf_review
pdftoppm -png -scale-to 1600 \
  microservice-lecture/units/unit_01_escaping_monolithic_hell/bilingual_notes.pdf \
  /tmp/microservices_pdf_review/page
```

Üretilen bütün sayfalarda paragraf sırasını ve dil eşleşmelerini, şekillerin
tamlığını, açıklamaları, Türkçe karakterleri, kodları ve sayfa kırılmalarını kontrol
et. Düzeltmeyi Markdown kaynağında yapıp PDF'yi yeniden üret.
