# Unit 13 · Concurrency

Bu ünite Java 17 thread lifecycle, `ExecutorService`, thread safety, concurrent
collection, liveness problem'ları ve parallel stream konularını çift dilli ana
ders akışı; teknik hafıza, vocabulary ve grammar materyalleriyle birlikte ele
alır.

## Amaç ve öğrenme hedefleri

Bu ünitenin sonunda task execution ve lifecycle akışını izleyebilmen; shared
state için visibility, atomicity ve mutual exclusion gereksinimlerini
ayırabilmen; concurrent collection, liveness ve parallel reduction sorularında
garanti edilen sonuçla possible sonucu ayırt edebilmen hedeflenir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| Concurrency konularını English → Türkçe eşleşmesiyle kaynak sırasından öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Thread, executor, lock ve parallel stream kararlarını hızla tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Concurrency terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Teknik İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi kaynaklar kapalıyken sekiz soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## Çalışan biri için çalışma rotası · 25–30 dakikalık oturumlar

Bu tablo bir **ilk tur rotasıdır**; bütün üniteyi tek oturumda bitirme hedefi değildir.
Yoğun başlığı veya uzun soru grubunu aynı rota satırında ikinci güne böl.
Her oturumda **3 dk kapalı kitap hatırlama → 9 dk okuma → 10 dk soru →
5 dk dil çalışması → 3 dk hata kaydı** uygula. Okuma bölümünde önce İngilizce
paragrafı sesli veya yazılı özetle, sonra Türkçe çeviriyle karşılaştır.

| Oturum | Okuma ve teknik hedef | Kaynak Review Questions | Kelime odağı | Grammar odağı |
|---|---|---|---|---|
| 1 · Thread ve görev türleri | [Introducing Threads](bilingual_notes.md#introducing-threads) | [3](bilingual_notes.md#question-3--soru-3), [18](bilingual_notes.md#question-18--soru-18), [25](bilingual_notes.md#question-25--soru-25) | task / worker / callable | 3: allow; 5: whereas |
| 2 · Executor, Future ve zamanlama | [Creating Threads with the Concurrency API](bilingual_notes.md#creating-threads-with-the-concurrency-api) | [4](bilingual_notes.md#question-4--soru-4), [9](bilingual_notes.md#question-9--soru-9), [12](bilingual_notes.md#question-12--soru-12), [19](bilingual_notes.md#question-19--soru-19), [20](bilingual_notes.md#question-20--soru-20) | submit / await / timeout | 6: by; 19: prevent |
| 3 · Görünürlük, atomiklik ve kilit | [Writing Thread-Safe Code](bilingual_notes.md#writing-thread-safe-code) | [2](bilingual_notes.md#question-2--soru-2), [5](bilingual_notes.md#question-5--soru-5), [16](bilingual_notes.md#question-16--soru-16), [17](bilingual_notes.md#question-17--soru-17), [22](bilingual_notes.md#question-22--soru-22), [24](bilingual_notes.md#question-24--soru-24) | visibility / atomic / acquire / release | 9: if; 17: even though |
| 4 · Koleksiyonlar ve ilerleme sorunları | [Using Concurrent Collections](bilingual_notes.md#using-concurrent-collections) | [7](bilingual_notes.md#question-7--soru-7), [10](bilingual_notes.md#question-10--soru-10), [14](bilingual_notes.md#question-14--soru-14), [23](bilingual_notes.md#question-23--soru-23) | deadlock / starvation / livelock | 18: because of; 20: result in |
| 5 · Paralel akış ve indirgeme | [Working with Parallel Streams](bilingual_notes.md#working-with-parallel-streams) | [1](bilingual_notes.md#question-1--soru-1), [6](bilingual_notes.md#question-6--soru-6), [8](bilingual_notes.md#question-8--soru-8), [11](bilingual_notes.md#question-11--soru-11), [13](bilingual_notes.md#question-13--soru-13), [15](bilingual_notes.md#question-15--soru-15), [21](bilingual_notes.md#question-21--soru-21) | decompose / reduction / nondeterministic | 15: regardless of; 23: no matter |
| 6 · Karışık kontrol | [Teknik hafıza notu](technical_memory_notes.md): önce karar kuralını bellekten yaz | Önceki oturumların en zor 3 sorusu + [özgün quiz 7–8](practice_quiz.md#soru-7) | Yanlış yaptığın 5 kelime | Bir uzun cümlede özne, yüklem ve bağlacı işaretle |

Kaynak soruların seçenek sayısı ve “Choose all that apply” yönergesi korunmuştur.
Cevaplara geçmeden seçtiğin her şık için bir gerekçe yaz. Kaynak cevapla Java 17
notu ayrışıyorsa ilgili editör notunu da oku; yalnız harf ezberleme.

### 1 / 3 / 7 / 14 gün tekrar döngüsü

Her oturumun tekrarını kendi çalışma tarihinden itibaren planla:

- **1. gün · 5 dk:** O günün 3–5 kelimesini Türkçeden İngilizceye üret; kuralı bir örnekle anlat.
- **3. gün · 8 dk:** Yanlış veya tahminle doğru yaptığın iki soruyu seçenekleri kapatarak yeniden çöz.
- **7. gün · 10 dk:** Farklı konulardan üç soru ve bir cümle çözümlemesi yap.
- **14. gün · 10 dk:** Hâlâ karıştırdığın kuralları ve kelimeleri tekrar yokla; doğru cevapla birlikte nedenini söyle.

Hata kaydına tek satır yeter: **soru → benim gerekçem → doğru kural →
yeni örnek → tekrar tarihi**. Hatanın türünü `Java kuralı`, `kod izleme`,
`kelime` veya `cümle yapısı` olarak belirt; böylece bir sonraki kısa oturumun
hedefi belli olur.

**Geçiş ölçütü:** İki ayrı günde özgün quiz'de en az **7/8**; kaynaklarda
yanlış yapılan soruların doğru gerekçesi; seçilen 5 kelimeden en az 4'ünü
cümlenin içinde kullanma; bir İngilizce cümlede ana yüklemi ve koşul/karşıtlık
ilişkisini açıklama. Sağlanmayan beceri için yalnız ilgili oturumu yinele.

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 13 physical PDF pages: **721–784**
- Chapter içerik sayfaları: **721–783**
- Physical page 784: **boş chapter separator**
- Chapter 13 Appendix official answers: **951–955**
- Chapter gövdesi: **64/64 kaynak sayfa**
- Appendix: **5/5 cevap kaynağı sayfası**
- Bölüm sonu: Summary, Exam Essentials ve kaynak **Review Questions 1–25**
- Kaynak Appendix: Official Answers **1–25**, bütün sonuç ve gerekçeleriyle

Physical page 721 chapter title/objective sayfasıdır. Kaynak review içeriği page
783'te biter; page 784 bilinçli olarak boş bırakılmış separator'dır ve Chapter 14
physical page 785'te başlar. Appendix page 951'in üst bölümü Chapter 12'ye,
`Chapter 13: Concurrency` heading'inden sonraki bölümü bu üniteye aittir.
Appendix page 955'in üstündeki Answer 25 bu ünitede tutulmuş, alttaki Chapter 14
cevapları dışarıda bırakılmıştır.

## Ana konu başlıkları

1. **Introducing Threads** — page 722
2. **Creating Threads with the Concurrency API** — page 730
3. **Writing Thread-Safe Code** — page 740
4. **Using Concurrent Collections** — page 754
5. **Identifying Threading Problems** — page 758
6. **Working with Parallel Streams** — page 761
7. **Summary** — page 770
8. **Exam Essentials** — page 770
9. **Review Questions** — page 772

## Figure envanteri

| Figure | Başlık | Physical page |
|---|---|---:|
| 13.1 | Process model | 723 |
| 13.2 | Thread states | 727 |
| 13.3 | `ExecutorService` life cycle | 731 |
| 13.4 | Lack of thread synchronization | 741 |
| 13.5 | Thread synchronization using atomic operations | 743 |
| 13.6 | Race condition on user creation | 761 |

## Table envanteri

| Table | Başlık | Physical page |
|---|---|---:|
| 13.1 | `ExecutorService` methods | 733 |
| 13.2 | `Future` methods | 734 |
| 13.3 | `TimeUnit` values | 735 |
| 13.4 | `ScheduledExecutorService` methods | 737 |
| 13.5 | `Executors` factory methods | 739 |
| 13.6 | Atomic classes | 743 |
| 13.7 | Common atomic methods | 744 |
| 13.8 | `Lock` methods | 749 |
| 13.9 | Concurrent collection classes | 756 |
| 13.10 | Synchronized Collections methods | 757 |

## Önkoşul ve konu haritası

**Önkoşul:** Lambda ve functional interface'ler, collection/stream pipeline'ı,
exception handling ve mutable object state konularını hatırlamak gerekir.

- Thread, process, task, concurrency, scheduler ve context switch
- `Runnable`, `Thread.start()`, `run()`, user/system ve daemon thread
- Altı `Thread.State`, polling, `sleep()` ve cooperative interruption
- `ExecutorService` lifecycle, shutdown ve task submission
- `Future`, timeout, cancellation, `Callable` ve termination bekleme
- `ScheduledExecutorService`, fixed rate/fixed delay ve thread pool factory'leri
- Shared mutable state, lost update, visibility ve atomicity
- `volatile`, atomic class'lar, intrinsic monitor ve `synchronized`
- `Lock`, `ReentrantLock`, `tryLock()`, fairness ve reentrant hold count
- `CyclicBarrier` ile phase coordination
- Concurrent collection, copy-on-write, blocking queue ve synchronized wrapper
- Deadlock, starvation, livelock ve race condition
- Parallel stream creation, decomposition, ordering ve performance
- Parallel `reduce()`/`collect()`, collector characteristics ve stateless pipeline

## Hazır mıyım?

- [ ] `run()` ile `start()` farkını ve altı `Thread.State` değerini
  açıklayabiliyorum.
- [ ] `execute()`, `submit()`, `shutdown()` ve `Future.get()` sonuçlarını
  doğru sınıflandırabiliyorum.
- [ ] Visibility, atomicity ve mutual exclusion ihtiyaçlarını ayrı ayrı
  belirleyebiliyorum.
- [ ] `volatile`, atomic class, `synchronized` ve `Lock` arasında amaca göre
  seçim yapabiliyorum.
- [ ] Concurrent collection iterator davranışlarını ve synchronized wrapper
  iteration kuralını biliyorum.
- [ ] Deadlock, starvation, livelock ve race condition'ı ayırabiliyorum.
- [ ] Parallel reduction'da identity, associativity ve ordering tuzaklarını
  kontrol edebiliyorum.
- [ ] Practice quiz'de en az **7/8** doğru yapıp yanlış seçenekleri
  gerekçelendirebiliyorum.

## Java 17 teknik doğruluk notları

- `Thread.run()` ordinary synchronous method call'dur; yalnız `start()` yeni
  thread başlatır.
- Aynı `Thread` instance'ında ikinci `start()` compile-time değil runtime
  `IllegalThreadStateException` üretir.
- `interrupt()` thread'i zorla öldürmez. Canlı bir waiting/sleeping thread'de
  interruptible operation `InterruptedException` oluşturabilir; canlı fakat o
  anda interruptible blocking call'da olmayan thread'de interrupt status set
  edilir. Henüz alive olmayan veya terminated thread'de çağrının etkisi
  olmayabilir.
- Yeni bir platform thread daemon status'unu creator thread'den miras alır.
  `main` gibi non-daemon bir thread tarafından oluşturulan ve status'u
  değiştirilmemiş worker non-daemon'dır; tamamlanana kadar JVM'i canlı tutabilir.
- Java 17'de `ExecutorService`, `AutoCloseable` değildir; try-with-resources
  resource olarak kullanılamaz.
- `shutdown()` accepted task'leri tamamlar, yeni task'leri reddeder.
  `shutdownNow()` yalnızca interruption denemesi yapar; anında termination
  garantilemez.
- `execute(Runnable)` `void`; `submit(Runnable)` ise successful `get()` sonucu
  `null` olan `Future<?>` döndürür.
- `Callable<V>` value döndürebilir ve checked exception declare edebilir;
  `Runnable.run()` `void` döndürür.
- `scheduleAtFixedRate()` aynı periodic execution'ın concurrent kopyalarını
  başlatmaz; iş uzarsa sonraki execution hedef schedule'ın gerisine düşebilir.
- `volatile` visibility ve ordering sağlar; mutual exclusion sağlamaz ve
  `counter++` işlemini atomic yapmaz.
- Instance `synchronized` method `this`, static `synchronized` method class
  object'i lock eder. Bunlar farklı monitor'lerdir.
- `tryLock()` sonucu mutlaka kontrol edilmelidir. Başarılı her reentrant
  acquisition aynı sayıda `unlock()` gerektirir.
- `CyclicBarrier` party sayısına normal biçimde ulaştığında **trip** olur ve
  yeniden kullanılabilir; yalnızca limite ulaştığı için broken sayılmaz.
- `ConcurrentHashMap` iterator'ı weakly consistent, `CopyOnWriteArrayList`
  iterator'ı snapshot tabanlıdır.
- `Collections.synchronizedXxx()` wrapper üzerinde iteration yapılırken wrapper
  üzerinde ayrıca synchronization gerekir.
- `findAny()` parallel veya serial stream'de first element garantilemez;
  `findFirst()` ordered stream'de encounter order'ı korur.
- Parallel reduction için identity neutral, operation'lar associative,
  non-interfering ve stateless olmalıdır.
- `Collectors.toSet()` parallel pipeline'da kullanılabilir; ancak
  `CONCURRENT` characteristic taşımadığından tek shared result içine concurrent
  accumulation yapmaz.
- Kaynak Review Question 9, concrete executor türünü belirtmeden task'ın mutlaka
  internal queue'ya alınacağını varsayar. Generic `ExecutorService` için bu garanti
  yoktur; ilgili resmî cevabın altında Java 17 editör notu bulunur.
- Kaynak Review Question 25'in resmî anahtarı C ve D'dir. Timed `Future.get()` çalışan
  task'ı cancel etmediği ve `shutdown()` task'ı interrupt etmediği için Java 17'de E de
  mümkündür; teknik olarak savunulabilir küme C, D ve E'dir. Ana notta kaynak cevap ile
  teknik düzeltme ayrı gösterilir.

## Önerilen çalışma sırası

1. `bilingual_notes.md` içinde thread–task–process ayrımını ve lifecycle
   state'lerini oku.
2. Her kodu **Does not compile**, runtime exception, nondeterministic output,
   possible nontermination veya deterministic success olarak sınıflandır.
3. Executor sorularında static type, submission method, worker count, queue ve
   shutdown sırasını yaz.
4. Shared state sorularında önce visibility, atomicity ve mutual exclusion
   gereksinimlerini ayır.
5. Lock sorularında monitor identity ve acquisition/release sayısını; barrier
   sorularında party ile available worker sayısını kontrol et.
6. Parallel stream sorularında encounter order, stateful lambda, identity,
   accumulator ve combiner contract'larını işaretle.
7. `technical_memory_notes.md` karar tablolarıyla tekrar yap; ardından kaynak
   Review Questions 1–25'i çöz.
8. Son olarak kaynak Appendix 1–25 resmî sonuç/gerekçelerini karşılaştır ve
   vocabulary/grammar mini quiz'lerini tamamla.

Vocabulary, grammar ve teknik hafıza quiz'leri özgün çalışma sorularıdır; gerçek
sınavdan çıkmış gibi sunulmaz. Ana çift dilli nottaki Review Questions ise kaynak
chapter'ın bölüm sonu sorularıdır ve Appendix'teki resmî cevaplarla eşleştirilir.
