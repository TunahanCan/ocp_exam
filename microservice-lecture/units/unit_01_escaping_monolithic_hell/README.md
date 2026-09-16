# Ünite 01 · Escaping monolithic hell

**Monolitik çıkmazdan kurtulmak** — *Microservices Patterns*, bölüm 1, kaynak PDF sayfaları 1–32.

## İçindekiler

| Belge | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Çift dilli ana ders: bütün bölüm, 16 özgün şekil ve SOA karşılaştırması | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| Üniteye özel teknik İngilizce ve YDS sözlüğü | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| Kaynak cümlelerle grammar ve YDS notları | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |

- [Görsellerin kaynak ve kırpım bilgileri](assets/manifest.json)
- [Kalite kontrol raporu](review_report.md)
- [Bütün üniteler ve ilerleme](../../README.md)

## Öğrenme hedefleri

- Monolitik mimarinin başlangıçtaki yararları ile büyüme sırasında ortaya çıkan sorunları ayırt etmek.
- X, Y ve Z eksenlerinde ölçeklemeyi şekiller üzerinden açıklamak.
- Servis sınırı, gevşek bağlılık ve veri sahipliği arasındaki ilişkiyi kurmak.
- Mikroservislerin yararlarını dağıtık sistemlerin maliyetleriyle birlikte değerlendirmek.
- Pattern language, saga, sorgu, dağıtım, gözlemlenebilirlik ve test örüntülerinin neden birlikte gerektiğini görmek.
- DevOps, ekip yapısı ve mimari arasındaki ilişkiyi anlamak.

## Okuma rotası

1. **1.1–1.3:** FTGO örneği ve monolitik uygulamanın büyümesi.
2. **1.4:** Ölçekleme küpü, servis sınırları ve SOA karşılaştırması.
3. **1.5:** Mikroservislerin yararları ve maliyetleri.
4. **1.6:** Birbirini tamamlayan mimari örüntüler.
5. **1.7 ve Summary:** Süreç, organizasyon, insan faktörü ve tekrar.

Her oturumda bir alt başlık ve ilgili şekiller yeterlidir. İngilizce şekil etiketleri özgün hâliyle korunmuştur; açıklamaları iki dilde verilmiştir. Teknik terminoloji ile cümle yapılarını uzun ara açıklamalar olmadan izlemek için sözlük ve grammar dosyalarını yanında açık tut.

**Kaynak bağlamı:** Metindeki tarihsel örnek ve öneriler kitabın anlatımıdır. Bu ünite Java 17/OCP kapsamını anlatan bir belge değildir; mikroservis mimarisi ve teknik İngilizce çalışmasıdır.
