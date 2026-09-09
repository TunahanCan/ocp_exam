# Unit 08 · Lambdas and Functional Interfaces

Bu ünite lambda expression, functional interface, method reference, built-in
functional interface ve lambda variable scope kurallarını Java 17 davranışıyla
ele alır. Hedef, önce target type'ı bulup syntax, parameter/return uyumu ve
variable capture kararını sistemli biçimde verebilmektir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Konuyu kaynak sırasıyla, English → Türkçe eşleşmesiyle öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Lambda/SAM/method reference karar tablolarıyla hızlı tekrar yapmak | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Lambda terminolojisini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Kaynaktaki İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi yeni compile/output sorularında sınamak | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions--gözden-geçirme-soruları) | [Ana PDF](bilingual_notes.pdf) |

> Bu ünitedeki mini quiz'ler ve `practice_quiz`, OCP tarzı **özgün çalışma
> sorularıdır**; gerçek sınav sorusu olarak sunulmaz.

## İşten sonra çalışma rotası

Bu rota bütün üniteyi tek akşamda bitirme hedefi değildir. Her satır **25–30 dakikalık bir oturumun odağıdır**; okuma veya soru grubu bitmezse aynı satırı sonraki güne taşı. Bir oturumda 2–4 kaynak soruyu gerekçesiyle çözmek yeterlidir. Aşağıdaki soru numaraları kitabın **Review Questions** bölümüne aittir; `practice_quiz` ayrı özgün sorulardır.

Her oturum: **3 dk** önceki bilgiyi kapalı kitap hatırla → **10 dk** English paragrafı çevirip Türkçeyle karşılaştır → **5 dk** en fazla dört yeni kelime ve bir grammar yapısı → **8 dk** soru çöz → **2 dk** yanlışının nedenini yaz. İlk turda bütün kelimeleri ezberlemeye çalışma; bilmediklerini işaretle.

| Oturum ve kaynak başlığı | Kaynak sorular | Kelime ve grammar odağı | Oturum sonunda üret |
|---|---|---|---|
| 1. [Lambda sözdizimi ve hedef tür](bilingual_notes.md#writing-simple-lambdas) | 1, 2, 4, 6, 7, 14, 17 | target type, omit, explicitly; `allow ... to`, `only if` | Her lambda’nın parametre ve dönüş türünü yaz; yoğun grubu gerekirse ikiye böl. |
| 2. [Functional interface ve SAM](bilingual_notes.md#coding-functional-interfaces) | 3, 21 | single abstract method, insufficient, annotation; `even though`, `just because ...` | Object’ın public imzalarını ve concrete method’ları SAM sayımından ayır. |
| 3. [Method reference ve hazır arayüzler](bilingual_notes.md#using-method-references) | 5, 8, 9, 18, 19, 20 | receiver, equivalent, primitive specialization; `while`, `without + V-ing` | Method reference’ı lambda’ya aç; Supplier/Function/Consumer türlerini karşılaştır. |
| 4. [Bileşim ve local değişkenler](bilingual_notes.md#working-with-variables-in-lambdas) | 10, 11, 12, 13, 15, 16 | capture, effectively final, scope; `as long as`, `when + V3` | Yeniden atama ile nesnenin içeriğini değiştirmeyi ayır; practice quiz 1–8. |

Kelime anlamlarını [ünite sözlüğünden](vocabulary.md), yapıları [grammar notundan](grammar_notes.md) kontrol et. Kaynak sorularını çözerken önce isteneni (derleme / çıktı / exception / doğru seçenek sayısı), sonra kuralı yaz; cevap harfini en son seç.

## Aralıklı tekrar ve geçiş ölçütü

- **1. gün:** Türkçeyi kapatarak dün işaretlediğin dört kelimeyi ve bir cümleyi geri çağır; yanlış yaptığın bir soruyu çöz.
- **3. gün:** Aynı kuralı ölçen başka bir kaynak soruya geç; doğru seçeneğin yanında en güçlü yanlış seçeneğin neden elendiğini söyle.
- **7. gün:** Özgün practice quiz'i yeniden çöz; çözerken kuralın adını ve sonucunu ayrı yaz. Hedef **en az 7/8** ve bütün derleme/çalışma zamanı ayrımlarını doğru gerekçelendirmek.
- **14. gün:** Önceki yanlışlarından üç soruyu karışık sırada çöz; sekiz işaretli kelimenin en az altısını ve iki cümlenin özne/fiil/yan cümle yapısını notsuz çıkar.

Yanlış kayıt biçimi: `Soru → ilk kararım → kaçırdığım Java kuralı/İngilizce yapı → düzeltilmiş gerekçe → yeniden çözüm günü`. Yalnızca cevap harfini hatırlamak geçiş ölçütü değildir. Eksik kalan konu için ilgili oturumu tekrarla.

## Önkoşullar ve konu haritası

**Önkoşul:** Method signature, interface inheritance, generic type parameter ve
local-variable scope konularını temel düzeyde bilmelisin.

```text
target type → single abstract method (SAM)
        ↓
lambda syntax ↔ dört method reference biçimi
        ↓
built-in functional interface + primitive specialization
        ↓
effectively final capture + scope + evaluation order
```

Teknik hafıza notu; lambda syntax seçeneklerini, SAM hesabını, dört method
reference biçimini, temel built-in functional interface matrisini, primitive
specialization'ları, convenience method'ları ve effectively final variable
kurallarını tek karar akışında toplar.

## Hazır mıyım?

- [ ] Bir lambda için önce target type ve SAM signature'ını çıkarabiliyorum.
- [ ] Expression body ile block body'nin return kurallarını ayırabiliyorum.
- [ ] Dört method reference biçimini eşdeğer lambda'ya çevirebiliyorum.
- [ ] Temel built-in functional interface'lerin parameter ve return tiplerini
  söyleyebiliyorum.
- [ ] Primitive specialization adlarını soldan sağa okuyabiliyorum.
- [ ] `final` ile effectively final farkını ve capture sonucunu
  açıklayabiliyorum.
- [ ] Practice quiz'de en az **7/8** doğru yapabiliyorum.

## Kaynak ve kapsam

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  eksiksiz Chapter 8 · Lambdas and Functional Interfaces, PDF sayfaları
  419–462.
- Aynı kaynağın resmî **Answers to the Review Questions** appendix'i, PDF
  sayfaları 936–939; Question 1–21'in bütün doğru cevap ve seçenek gerekçeleri.
- Ana çift dilli not; chapter girişini, bütün konu anlatımını, code,
  table/figure metinlerini, Summary, Exam Essentials ve Review Questions
  1–21'i kaynak sırasıyla; ardından resmî cevap ekini kapsar. Running
  header/footer ve basılı sayfa numaraları kapsam dışıdır.
