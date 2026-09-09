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

## İşten sonra çalışma rotası

Bu rota bütün üniteyi tek akşamda bitirme hedefi değildir. Her satır **25–30 dakikalık bir oturumun odağıdır**; okuma veya soru grubu bitmezse aynı satırı sonraki güne taşı. Bir oturumda 2–4 kaynak soruyu gerekçesiyle çözmek yeterlidir. Aşağıdaki soru numaraları kitabın **Review Questions** bölümüne aittir; `practice_quiz` ayrı özgün sorulardır.

Her oturum: **3 dk** önceki bilgiyi kapalı kitap hatırla → **10 dk** English paragrafı çevirip Türkçeyle karşılaştır → **5 dk** en fazla dört yeni kelime ve bir grammar yapısı → **8 dk** soru çöz → **2 dk** yanlışının nedenini yaz. İlk turda bütün kelimeleri ezberlemeye çalışma; bilmediklerini işaretle.

| Oturum ve kaynak başlığı | Kaynak sorular | Kelime ve grammar odağı | Oturum sonunda üret |
|---|---|---|---|
| 1. [Collection, List ve Set](bilingual_notes.md#using-common-collection-apis) | 1, 2, 4, 10, 17 | backed by, fixed-size, duplicate; `unlike`, `whether` | Mutable/fixed-size/unmodifiable tablosunu kapalı kitap kur. |
| 2. [Queue, Deque ve Map](bilingual_notes.md#using-the-queue-and-deque-interfaces) | 3, 15, 16, 19 | absent, entry, retrieve; `unless`, `rather than` | Deque uçlarını çiz; Map için yok/null/değer üç durumunu ayır. |
| 3. [Sıralama ve arama](bilingual_notes.md#sorting-data) | 6, 8, 12, 13 | consistent, natural order, insertion point; `as long as`, `while` | Önce comparator’ı uygula; binary search aynı sıralamayı mı bekliyor? |
| 4. [Generic bildirim ve erasure](bilingual_notes.md#working-with-generics) | 5, 7, 9, 18 | raw type, type erasure, parameterized type; `so that`, `when + V-ing` | Class ve method type parameter’larını ayır; Soru 7’deki kaynak anahtarı düzeltmesini oku. |
| 5. [Wildcard ve güvenli işlem](bilingual_notes.md#bounding-generic-types) | 11, 14, 20 | upper bound, lower bound, invariant; `which/that`, `only` anlam sınırı | `? extends`/`? super` için okuma ve ekleme türlerini yaz; practice quiz 1–8. |

Kelime anlamlarını [ünite sözlüğünden](vocabulary.md), yapıları [grammar notundan](grammar_notes.md) kontrol et. Kaynak sorularını çözerken önce isteneni (derleme / çıktı / exception / doğru seçenek sayısı), sonra kuralı yaz; cevap harfini en son seç.

## Aralıklı tekrar ve geçiş ölçütü

- **1. gün:** Türkçeyi kapatarak dün işaretlediğin dört kelimeyi ve bir cümleyi geri çağır; yanlış yaptığın bir soruyu çöz.
- **3. gün:** Aynı kuralı ölçen başka bir kaynak soruya geç; doğru seçeneğin yanında en güçlü yanlış seçeneğin neden elendiğini söyle.
- **7. gün:** Özgün practice quiz'i yeniden çöz; çözerken kuralın adını ve sonucunu ayrı yaz. Hedef **en az 7/8** ve bütün derleme/çalışma zamanı ayrımlarını doğru gerekçelendirmek.
- **14. gün:** Önceki yanlışlarından üç soruyu karışık sırada çöz; sekiz işaretli kelimenin en az altısını ve iki cümlenin özne/fiil/yan cümle yapısını notsuz çıkar.

Yanlış kayıt biçimi: `Soru → ilk kararım → kaçırdığım Java kuralı/İngilizce yapı → düzeltilmiş gerekçe → yeniden çözüm günü`. Yalnızca cevap harfini hatırlamak geçiş ölçütü değildir. Eksik kalan konu için ilgili oturumu tekrarla.

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
- [ ] Practice quiz'de en az **7/8** doğru yapabiliyorum.

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
