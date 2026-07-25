# Unit 06 · Class Design

Bu ünite inheritance, constructor chaining, initialization order,
overriding/hiding, abstract/concrete class ve immutable class kurallarını Java
17/OCP odağında öğretir. Hedef yalnızca kuralı hatırlamak değil; bir kodun
**derlenip derlenmediğini**, derleniyorsa **hangi sırayla çalıştığını** hızlıca
ayırt edebilmektir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Konuyu kaynak sırasıyla, English → Türkçe eşleşmesiyle öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Sınavdan önce kuralları ve karar tablolarını hızla tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Class design terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Kaynaktaki İngilizce cümle yapılarını ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi cevap anahtarına bakmadan geri çağırmak | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> `practice_quiz` içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Aşağıdaki konu haritasını oku; zayıf olduğun iki başlığı seç.
2. **5–25 dk:** Ana çift dilli notta bu başlıkların English → Türkçe
   paragraflarını ve kod örneklerini çalış.
3. **25–35 dk:** Teknik hafıza notunda constructor, initialization order ve
   override karar tablolarını kapatıp kendin yeniden kur.
4. **35–43 dk:** Vocabulary'den bilmediğin 6–8 terimi örnekleriyle tekrar et.
5. **43–50 dk:** Grammar notes içinden iki yapıyı İngilizce örnekleri üzerinden
   çözümle.
6. **50–60 dk:** Practice quiz'i kaynaklara bakmadan çöz; yalnız sonra cevap
   açıklamalarına dön.

## Önkoşullar ve konu haritası

**Önkoşul:** Class/member declaration, access modifier, method overload ve
temel exception bilgisini hatırlıyor olmalısın.

```text
inheritance ve access
        ↓
constructor chaining → class/instance initialization order
        ↓
override kuralları ↔ static method/field hiding
        ↓
abstract–concrete ilişkisi → immutability ve defensive copy
```

Teknik hafıza notundaki rulebook; inheritance member'larını, constructor
zincirini, complete initialization order'ı, S-R-A-E override kartını,
abstract/final uyumluluğunu ve immutability checklist'ini tek tekrar akışında
ele alır.

## Hazır mıyım?

- [ ] `this()` ve `super()` çağrılarının neden constructor'ın ilk ifadesi
  olması gerektiğini açıklayabiliyorum.
- [ ] Class initialization ile instance initialization sırasını ayrı ayrı
  kurabiliyorum.
- [ ] Bir method declaration için override, overload ve **Does not compile**
  ayrımını yapabiliyorum.
- [ ] Covariant return type, access genişletme ve checked exception daraltma
  kurallarını birlikte uygulayabiliyorum.
- [ ] Static method/field hiding ile instance method dispatch farkını
  açıklayabiliyorum.
- [ ] Mutable bir alanı constructor ve accessor sınırlarında defensive copy ile
  koruyabiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapabiliyorum.

## Kaynak ve kapsam

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 6 — Class Design, PDF sayfaları 275–344.
- Ana not; bölüm açılışı, bütün konu anlatımı, tablolar/şekiller, Summary,
  Exam Essentials ve Review Questions 1–26 dahil tam bölüm kapsamını izler.
