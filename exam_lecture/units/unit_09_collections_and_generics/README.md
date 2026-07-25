# Unit 09 · Collections and Generics

Bu ünite Java 17 Collections Framework, sorting ve generics konularını kaynak
sırasını koruyan çift dilli ders akışıyla ele alır. Hedef; önce veri yapısının
contract'ını seçmek, ardından equality/ordering, mutability ve generic bound
kurallarını doğru sırayla uygulamaktır.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Konuyu kaynak sırasıyla, English → Türkçe eşleşmesiyle öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Collection seçimi, sorting ve wildcard kararlarını hızlı tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Collections/generics terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Kaynaktaki İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi yeni compile/output ve kavram sorularında sınamak | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions--gözden-geçirme-soruları) | [Ana PDF](bilingual_notes.pdf) |

> Vocabulary ve grammar mini quiz'leri, teknik hafıza soruları ve
> `practice_quiz`, OCP tarzı **özgün çalışma sorularıdır**; gerçek sınavdan
> alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasını incele; collection seçimi ve PECS kararını
   ezberden anlat.
2. **5–25 dk:** Ana çift dilli notta zayıf olduğun iki başlığın English →
   Türkçe çiftlerini ve kodlarını çalış.
3. **25–35 dk:** Teknik hafıza notundaki implementation, `Map.merge()`,
   sorting ve wildcard tablolarını kapatıp yeniden kur.
4. **35–43 dk:** Vocabulary'den 6–8 terimi kısa teknik örneklerle tekrar et.
5. **43–50 dk:** Grammar notes içinden iki yapının clause/phrase sınırlarını
   işaretle.
6. **50–60 dk:** Practice quiz'i kaynaklara bakmadan çöz; yanlışlarını
   collection, ordering veya generic başlığına göre sınıflandır.

## Önkoşullar ve konu haritası

**Önkoşul:** Interface/implementation ayrımı, `equals()`, lambda/method
reference ve temel generic syntax bilgisini hatırlıyor olmalısın.

```text
gereksinim → List / Set / Queue-Deque / Map
        ↓
mutability + equality + ordering
        ↓
Comparable / Comparator → sort / binarySearch
        ↓
generic declaration → invariance → wildcard (PECS) → type erasure
```

Ana konu başlıkları:

- Common `Collection` APIs, equality, iteration ve mutation
- `List`, factory/constructor farkları, overload'lar ve array dönüşümleri
- `Set`, hash-based ve tree-based implementation farkları
- `Queue`, `Deque`, FIFO/LIFO ve exception/return-value method çiftleri
- `Map`, safe lookup, `putIfAbsent()`, `replace*()` ve `merge()` state'leri
- `Comparable`, `Comparator`, comparator chain, sorting ve binary search
- Generic class/interface/method/record, type inference ve type erasure
- Unbounded, upper-bounded ve lower-bounded wildcard'lar

## Hazır mıyım?

- [ ] Gereksinime göre doğru collection interface ve implementation'ı
  seçebiliyorum.
- [ ] Mutable, fixed-size ve unmodifiable collection farklarını
  açıklayabiliyorum.
- [ ] `remove(int)` ile `remove(Object)` overload'unu ayırabiliyorum.
- [ ] Equality ile ordering'in aynı şey olmadığını `TreeSet` örneğiyle
  gösterebiliyorum.
- [ ] `Comparable`, `Comparator`, `sort()` ve `binarySearch()` ilişkisini
  kurabiliyorum.
- [ ] `? extends` / `? super` için güvenli okuma-yazma tiplerini
  belirleyebiliyorum.
- [ ] Compile-time generic hatası ile raw type kaynaklı runtime riskini
  ayırabiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapabiliyorum.

## Java 17 teknik doğruluk notları

Ana not, kaynak metni eksiksiz korurken teknik açıdan yanıltıcı olabilecek
yerleri ayrı **Editor note / Editör notu** kutularında açıklar. Öne çıkanlar:

- `Set.of()` duplicate element aldığında `IllegalArgumentException` fırlatır.
- `containsKey()` ile `get() != null`, explicit null mapping durumunda eşdeğer
  değildir.
- `TreeMap` null value saklayabilir. Natural order kullanan `TreeMap` null key,
  `TreeSet` ise null element kabul etmez; null-aware custom comparator bu
  davranışı değiştirebilir.
- `java.util.Stack`, `Queue` implement etmez; `Vector`ı extends eder.
- `Comparator` class değil interface'tir.
- Subtraction comparator extreme `int` değerlerinde overflow yapabilir;
  `Integer.compare()` daha güvenlidir.
- Review Question 7'nin resmî B,F anahtarı “override” sözcüğüyle Java 17
  açısından çelişir: B overload, yalnız F gerçek override'dır. Kaynak anahtarı
  Appendix bölümünde aynen korunmuş ve çelişki yanında gösterilmiştir.

## Kaynak ve kapsam

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 9 physical PDF pages: **463–530**
- Chapter 9 Appendix official answers: **939–942**
- Chapter gövdesi: **68/68 kaynak sayfa**
- Görsel kaynaklar: **Table 9.1–9.14** ve **Figure 9.1–9.8**
- Bölüm sonu: Summary, dört Exam Essentials maddesi ve Review Questions 1–20
- Appendix: Official Answers 1–20 ve bütün gerekçeleri

Physical page 530 boş chapter separator sayfasıdır. Appendix kapsamına önceki
ve sonraki chapter cevapları alınmamıştır.
