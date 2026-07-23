# Unit 09 · Collections and Generics

Bu ünite Java 17 Collections Framework, sorting ve generics konularını kaynak
sırasını koruyan çift dilli ders akışıyla; ayrıca hızlı tekrar, vocabulary ve
grammar materyalleriyle birlikte ele alır.

## Çalışma kaynakları

1. **Ana çift dilli ders**
   - [Markdown kaynağı](bilingual_notes.md)
   - [PDF çalışma sürümü](bilingual_notes.pdf)
2. **Teknik hafıza ve karar notları**
   - [Technical memory notes](technical_memory_notes.md)
   - [PDF çalışma sürümü](technical_memory_notes.pdf)
3. **Ünite vocabulary çalışması**
   - [Markdown kaynağı](vocabulary.md)
   - [PDF çalışma sürümü](vocabulary.pdf)
4. **Ünite grammar çalışması**
   - [Markdown kaynağı](grammar_notes.md)
   - [PDF çalışma sürümü](grammar_notes.pdf)

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 9 physical PDF pages: **463–530**
- Chapter 9 Appendix official answers: **939–942**
- Chapter gövdesi: **68/68 source marker**
- Görsel kaynaklar: **Table 9.1–9.14** ve **Figure 9.1–9.8**
- Bölüm sonu: Summary, dört Exam Essentials maddesi ve Review Questions 1–20
- Appendix: Official Answers 1–20 ve bütün gerekçeleri

Physical page 530 boş chapter separator sayfasıdır. Appendix kapsamına önceki
ve sonraki chapter cevapları alınmamıştır.

## Konu haritası

- Common `Collection` APIs, equality, iteration ve mutation
- `List`, factory/constructor farkları, overload'lar ve array dönüşümleri
- `Set`, hash-based ve tree-based implementation farkları
- `Queue`, `Deque`, FIFO/LIFO ve exception/return-value method çiftleri
- `Map`, safe lookup, `putIfAbsent()`, `replace*()` ve `merge()` state'leri
- Collection type seçimi ve legacy collection'lar
- `Comparable`, `Comparator`, comparator chain, sorting ve binary search
- Generic class/interface/method/record, type inference ve type erasure
- Unbounded, upper-bounded ve lower-bounded wildcard'lar
- Generic supertype ve argument aktarımı

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

## Önerilen çalışma sırası

1. `bilingual_notes.md` içinde ilgili başlığı English → Türkçe çiftleriyle oku.
2. Kodun **Does not compile**, runtime exception veya output sonucunu önce
   kendin tahmin et.
3. `technical_memory_notes.md` içindeki karar tablolarıyla kuralı sıkıştır.
4. `vocabulary.md` ve `grammar_notes.md` mini quiz'lerini çöz.
5. Review Questions 1–20'yi cevap anahtarına bakmadan tamamla; sonra Appendix
   gerekçeleriyle bütün yanlış seçenekleri kontrol et.

Vocabulary ve grammar mini quiz'leri ile teknik hafıza notundaki ek sorular,
kitaptan alınmış gerçek sınav soruları değil; açıkça belirtilmiş özgün çalışma
sorularıdır.
