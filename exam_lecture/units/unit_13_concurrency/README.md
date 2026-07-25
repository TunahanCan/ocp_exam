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
| Bilgiyi kaynaklar kapalıyken altı soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasından executor, shared state veya parallel stream
   kümelerinden birini seç.
2. **5–25 dk:** Ana çift dilli notta ilgili English → Türkçe blokları ve kodları
   oku; her kod için result category'yi önceden söyle.
3. **25–35 dk:** Teknik hafıza notunda lifecycle, lock veya reduction karar
   kartını kaynak kapalıyken yeniden kur.
4. **35–43 dk:** Vocabulary'den 6–8 terimi birbirleriyle ilişkilendirerek kısa
   bir concurrency senaryosu anlat.
5. **43–50 dk:** Grammar notes içinden concession veya cause/result yapısını
   örnekleriyle çözümle.
6. **50–60 dk:** [Practice quiz](practice_quiz.md)'i cevap anahtarı kapalıyken
   çöz; yanlışını compile, runtime, nondeterminism veya English etiketiyle yaz.

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
- [ ] Practice quiz'de en az **5/6** doğru yapıp yanlış seçenekleri
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
