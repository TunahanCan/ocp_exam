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

## İşten sonra çalışma rotası

Bu rota bütün üniteyi tek akşamda bitirme hedefi değildir. Her satır **25–30 dakikalık bir oturumun odağıdır**; okuma veya soru grubu bitmezse aynı satırı sonraki güne taşı. Bir oturumda 2–4 kaynak soruyu gerekçesiyle çözmek yeterlidir. Aşağıdaki soru numaraları kitabın **Review Questions** bölümüne aittir; `practice_quiz` ayrı özgün sorulardır.

Her oturum: **3 dk** önceki bilgiyi kapalı kitap hatırla → **10 dk** English paragrafı çevirip Türkçeyle karşılaştır → **5 dk** en fazla dört yeni kelime ve bir grammar yapısı → **8 dk** soru çöz → **2 dk** yanlışının nedenini yaz. İlk turda bütün kelimeleri ezberlemeye çalışma; bilmediklerini işaretle.

| Oturum ve kaynak başlığı | Kaynak sorular | Kelime ve grammar odağı | Oturum sonunda üret |
|---|---|---|---|
| 1. [Inheritance ve erişim](bilingual_notes.md#understanding-inheritance) | 14, 17 | ancestor, descendant, implicit; `by + V-ing`, `whether ... or not` | Bir üst sınıf, bir alt sınıf ve iki ayrı field çiz. |
| 2. [Constructor zinciri](bilingual_notes.md#declaring-constructors) | 1, 4, 10, 13, 19 | default constructor, explicit, pathway; `since`, `as long as` | Her constructor için çağırdığı constructor’ı okla göster. |
| 3. [Başlatma sırası](bilingual_notes.md#initializing-objects) | 11, 16, 23, 24 | established, initialization order; `followed by`, `by the time` | Static ve instance adımlarını iki ayrı sütunda izle. |
| 4. [Override, overload ve hiding](bilingual_notes.md#inheriting-members) | 2, 3, 5, 7, 8, 9, 12, 18, 20, 22, 26 | covariant, broader, restrictive; `regardless of`, `even though` | Önce imza/erişim/return/exception; sonra çıktı. Bu yoğun oturumu gerekirse ikiye böl. |
| 5. [Abstract ve immutable tasarım](bilingual_notes.md#creating-abstract-classes) | 6, 15, 21, 25 | concrete, defensive copy, invariant; `provided`, `by definition` | Mutable listeyi alan ve döndüren sınırları işaretle; ardından practice quiz 1–8. |

Kelime anlamlarını [ünite sözlüğünden](vocabulary.md), yapıları [grammar notundan](grammar_notes.md) kontrol et. Kaynak sorularını çözerken önce isteneni (derleme / çıktı / exception / doğru seçenek sayısı), sonra kuralı yaz; cevap harfini en son seç.

## Aralıklı tekrar ve geçiş ölçütü

- **1. gün:** Türkçeyi kapatarak dün işaretlediğin dört kelimeyi ve bir cümleyi geri çağır; yanlış yaptığın bir soruyu çöz.
- **3. gün:** Aynı kuralı ölçen başka bir kaynak soruya geç; doğru seçeneğin yanında en güçlü yanlış seçeneğin neden elendiğini söyle.
- **7. gün:** Özgün practice quiz'i yeniden çöz; çözerken kuralın adını ve sonucunu ayrı yaz. Hedef **en az 7/8** ve bütün derleme/çalışma zamanı ayrımlarını doğru gerekçelendirmek.
- **14. gün:** Önceki yanlışlarından üç soruyu karışık sırada çöz; sekiz işaretli kelimenin en az altısını ve iki cümlenin özne/fiil/yan cümle yapısını notsuz çıkar.

Yanlış kayıt biçimi: `Soru → ilk kararım → kaçırdığım Java kuralı/İngilizce yapı → düzeltilmiş gerekçe → yeniden çözüm günü`. Yalnızca cevap harfini hatırlamak geçiş ölçütü değildir. Eksik kalan konu için ilgili oturumu tekrarla.

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
- [ ] Practice quiz'de en az **7/8** doğru yapabiliyorum.

## Kaynak sorularının cevapları

[Kitabın cevapları ve Türkçe çözüm özetleri](bilingual_notes.md#appendix--kaynak-cevaplarıyla-kontrol), her kaynak soru için cevap ve kritik gerekçeyi verir. Bunlar kitabın bölüm sonu cevaplarıdır; gerçek OCP sınavının cevapları değildir. Önce soruyu çöz, sonra kontrol et.

## Kaynak ve kapsam

- [OCP Java 17 çalışma kaynağı](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf),
  Chapter 6 — Class Design, PDF sayfaları 275–344.
- Ana not; bölüm açılışı, bütün konu anlatımı, tablolar/şekiller, Summary,
  Exam Essentials ve Review Questions 1–26 dahil tam bölüm kapsamını izler.
