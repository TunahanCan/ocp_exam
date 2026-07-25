# Unit 07 · Beyond Classes

Bu ünite interface, enum, sealed class, record, nested class ve polymorphism
konularını Java 17 kurallarıyla bir araya getirir. Amaç, type declaration
kurallarını ezberlemekten öte reference type ile runtime object'in hangi kararı
etkilediğini güvenle çözebilmektir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Konuyu kaynak sırasıyla, English → Türkçe eşleşmesiyle öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Interface, record, sealed ve nested type kurallarını hızlı tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Ünitenin teknik İngilizce terimlerini bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Kaynaktaki cümle yapılarını ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi yeni kod ve kavram sorularında sınamak | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions--gözden-geçirme-soruları) | [Ana PDF](bilingual_notes.pdf) |

> Bu ünitedeki mini quiz'ler ve `practice_quiz`, OCP tarzı **özgün çalışma
> sorularıdır**; gerçek sınav sorusu olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasında en çok karıştırdığın iki type ailesini seç.
2. **5–25 dk:** Ana çift dilli notta seçtiğin başlıkları ve hemen altındaki kod
   örneklerini English → Türkçe sırasıyla oku.
3. **25–35 dk:** Teknik hafıza notundan interface member, sealed hierarchy,
   record constructor ve nested class tablolarını tekrar et.
4. **35–43 dk:** Vocabulary'den 6–8 terimi kendi örnek cümlenle geri çağır.
5. **43–50 dk:** Grammar notes içinden iki yapıda clause sınırlarını işaretle.
6. **50–60 dk:** Practice quiz'i kapalı kaynakla çöz ve her yanlışını ilgili
   teknik hafıza başlığına bağla.

## Önkoşullar ve konu haritası

**Önkoşul:** Unit 06'daki inheritance, access, override/hiding ve constructor
kurallarına hâkim olmalısın.

```text
interface member'ları ─┐
enum ve record ────────┼→ type declaration kuralları
sealed hierarchy ──────┘
        ↓
nested class + enclosing scope
        ↓
reference type → cast/instanceof → runtime polymorphism
```

Teknik hafıza notunun master map bölümü interface member modifier'larını, enum
API'sini, sealed hierarchy kurallarını, record constructor/immutability
ayrımını, nested type'ları ve casting kararını tek tekrar akışında toplar.

## Hazır mıyım?

- [ ] Interface field ve method'larının implicit modifier'larını
  söyleyebiliyorum.
- [ ] Çakışan iki `default` method'u nasıl çözeceğimi biliyorum.
- [ ] `sealed`, `final` ve `non-sealed` subtype rollerini ayırabiliyorum.
- [ ] Record'un generated member'larını ve canonical/compact constructor
  kurallarını açıklayabiliyorum.
- [ ] Inner, static nested, local ve anonymous class erişimlerini
  karşılaştırabiliyorum.
- [ ] Cast'in compile-time uygunluğu ile runtime `ClassCastException` riskini
  ayrı kontrol edebiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapabiliyorum.

## Kaynak ve kapsam

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  eksiksiz Chapter 7 · Beyond Classes, PDF sayfaları 345–418.
- Ana çift dilli not; chapter girişini, bütün konu anlatımını, code ve
  table/figure metinlerini, Summary, Exam Essentials ve Review Questions
  1–30'u kaynak sırasıyla kapsar. Running header/footer ve basılı sayfa
  numaraları kapsam dışıdır.
- Önceden hazırlanmış Review Questions 15–29 teknik analizleri, ana kaynak
  aktarımından sonra appendix olarak korunmuştur.
