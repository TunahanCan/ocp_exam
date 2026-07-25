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

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasını incele; target type → SAM → lambda akışını
   sesli olarak anlat.
2. **5–25 dk:** Ana çift dilli notta lambda syntax, method reference ve
   built-in interface bölümlerini örneklerle çalış.
3. **25–35 dk:** Teknik hafıza notundaki ana matrisleri kapatıp `Supplier`,
   `Consumer`, `Predicate` ve `Function` imzalarını yaz.
4. **35–43 dk:** Vocabulary'den 6–8 terimi teknik örnekleriyle tekrar et.
5. **43–50 dk:** Grammar notes içinden iki yapıyı clause/phrase sınırlarıyla
   çözümle.
6. **50–60 dk:** Practice quiz'i IDE kullanmadan çöz; sonra compile-time,
   runtime ve output sınıflandırmanı cevaplarla karşılaştır.

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
- [ ] Practice quiz'de en az **5/6** doğru yapabiliyorum.

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
