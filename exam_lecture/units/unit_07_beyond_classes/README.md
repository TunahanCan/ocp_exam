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

## İşten sonra çalışma rotası

Bu rota bütün üniteyi tek akşamda bitirme hedefi değildir. Her satır **25–30 dakikalık bir oturumun odağıdır**; okuma veya soru grubu bitmezse aynı satırı sonraki güne taşı. Bir oturumda 2–4 kaynak soruyu gerekçesiyle çözmek yeterlidir. Aşağıdaki soru numaraları kitabın **Review Questions** bölümüne aittir; `practice_quiz` ayrı özgün sorulardır.

Her oturum: **3 dk** önceki bilgiyi kapalı kitap hatırla → **10 dk** English paragrafı çevirip Türkçeyle karşılaştır → **5 dk** en fazla dört yeni kelime ve bir grammar yapısı → **8 dk** soru çöz → **2 dk** yanlışının nedenini yaz. İlk turda bütün kelimeleri ezberlemeye çalışma; bilmediklerini işaretle.

| Oturum ve kaynak başlığı | Kaynak sorular | Kelime ve grammar odağı | Oturum sonunda üret |
|---|---|---|---|
| 1. [Interface üyeleri](bilingual_notes.md#implementing-interfaces) | 5, 6, 7, 10, 17, 23, 24, 28 | implicit, conflict, compatible; `allow ... to`, `since` | Üyeyi field/abstract/default/static/private olarak sınıflandır; yoğun soru grubunu gerekirse böl. |
| 2. [Enum ve sealed türler](bilingual_notes.md#working-with-enums) | 3, 4, 13, 14, 19, 26, 30 | permitted, restrict, constant-specific class body; `unless`, `while` | Enum sözdizimi ile sealed doğrudan alt tür denetimini ayrı yap. |
| 3. [Record ve encapsulation](bilingual_notes.md#encapsulating-data-with-records) | 1, 8, 12, 21, 27 | canonical, accessor, shallow immutability; `assuming`, `each of which` | Compact body sonunda hangi parametrenin hangi field’a gittiğini yaz. |
| 4. [Nested class ve kapsam](bilingual_notes.md#creating-nested-classes) | 11, 15, 16, 18, 22, 25 | enclosing instance, independently, latter; `when + V3`, `provided` | Outer nesne gerekli mi; erişilen üye static mi, instance mı? |
| 5. [Polymorphism ve karma tekrar](bilingual_notes.md#understanding-polymorphism) | 2, 9, 20, 29 | override, retrieve, revoke; `regardless of whether`, `not ... until` | Reference türü ile nesne türünü ayrı yaz; ardından practice quiz 1–8. |

Kelime anlamlarını [ünite sözlüğünden](vocabulary.md), yapıları [grammar notundan](grammar_notes.md) kontrol et. Kaynak sorularını çözerken önce isteneni (derleme / çıktı / exception / doğru seçenek sayısı), sonra kuralı yaz; cevap harfini en son seç.

## Aralıklı tekrar ve geçiş ölçütü

- **1. gün:** Türkçeyi kapatarak dün işaretlediğin dört kelimeyi ve bir cümleyi geri çağır; yanlış yaptığın bir soruyu çöz.
- **3. gün:** Aynı kuralı ölçen başka bir kaynak soruya geç; doğru seçeneğin yanında en güçlü yanlış seçeneğin neden elendiğini söyle.
- **7. gün:** Özgün practice quiz'i yeniden çöz; çözerken kuralın adını ve sonucunu ayrı yaz. Hedef **en az 7/8** ve bütün derleme/çalışma zamanı ayrımlarını doğru gerekçelendirmek.
- **14. gün:** Önceki yanlışlarından üç soruyu karışık sırada çöz; sekiz işaretli kelimenin en az altısını ve iki cümlenin özne/fiil/yan cümle yapısını notsuz çıkar.

Yanlış kayıt biçimi: `Soru → ilk kararım → kaçırdığım Java kuralı/İngilizce yapı → düzeltilmiş gerekçe → yeniden çözüm günü`. Yalnızca cevap harfini hatırlamak geçiş ölçütü değildir. Eksik kalan konu için ilgili oturumu tekrarla.

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
- [ ] Practice quiz'de en az **7/8** doğru yapabiliyorum.

## Kaynak sorularının cevapları

[Kitabın cevapları ve Türkçe çözüm özetleri](bilingual_notes.md#appendix--kaynak-cevaplarıyla-kontrol), her kaynak soru için cevap ve kritik gerekçeyi verir. Bunlar kitabın bölüm sonu cevaplarıdır; gerçek OCP sınavının cevapları değildir. Önce soruyu çöz, sonra kontrol et.

## Kaynak ve kapsam

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  eksiksiz Chapter 7 · Beyond Classes, PDF sayfaları 345–418.
- Ana çift dilli not; chapter girişini, bütün konu anlatımını, code ve
  table/figure metinlerini, Summary, Exam Essentials ve Review Questions
  1–30'u kaynak sırasıyla kapsar. Running header/footer ve basılı sayfa
  numaraları kapsam dışıdır.
- Önceden hazırlanmış Review Questions 15–29 teknik analizleri, ana kaynak
  aktarımından sonra appendix olarak korunmuştur.
