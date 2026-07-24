# Unit 13 · Concurrency — Vocabulary

Bu sözlük, [ana çift dilli nottaki](bilingual_notes.md) thread lifecycle,
executor, synchronization, liveness ve parallel stream bağlamında geçen
teknik/YDS kelimelerini alfabetik olarak toplar.

## A–C

### acquire · verb

- **Türkçe:** elde etmek, kilidi almak
- **Java bağlamı:** Thread'in monitor veya `Lock` ownership kazanması.
- **Example:** “The thread enters the block only after it acquires the lock.”
- **Çeviri:** “Thread yalnız lock'u aldıktan sonra block'a girer.”
- **Related:** acquisition, acquired; antonym: release

### atomic · adjective

- **Türkçe:** bölünmez, atomik
- **Java bağlamı:** Diğer thread'lerin aradaki state'i göremeyeceği tek logical
  operation.
- **Example:** “Incrementing an `AtomicInteger` is an atomic operation.”
- **Çeviri:** “`AtomicInteger`ı artırmak atomic operation'dır.”
- **Related:** atomically, atomicity; contrast: compound

### await · verb

- **Türkçe:** beklemek
- **Java bağlamı:** `CyclicBarrier.await()` veya executor termination için
  belirli event'i beklemek.
- **Example:** “Each worker awaits the other parties at the barrier.”
- **Çeviri:** “Her worker barrier'da diğer party'leri bekler.”
- **Related:** wait, awaiting

### barrier · noun

- **Türkçe:** bariyer, eşgüdüm noktası
- **Java bağlamı:** Belirli sayıda thread ulaşana kadar ilerlemeyi durduran
  coordination object.
- **Example:** “The barrier releases the workers after the final arrival.”
- **Çeviri:** “Barrier son arrival'dan sonra worker'ları serbest bırakır.”
- **Related:** `CyclicBarrier`, barrier action

### blocking · adjective / noun

- **Türkçe:** engelleyici, bekleten
- **Java bağlamı:** Thread'in result, lock veya queue item gelene kadar
  ilerleyememesi.
- **Example:** “A blocking call may put the thread into a waiting state.”
- **Çeviri:** “Blocking call thread'i waiting state'e geçirebilir.”
- **Related:** block, blocked; antonym: nonblocking

### callable · noun / adjective

- **Türkçe:** sonuç döndüren çağrılabilir görev
- **Java bağlamı:** Value döndürebilen ve checked exception declare edebilen
  `Callable<V>` task.
- **Example:** “The callable returns an integer through a future.”
- **Çeviri:** “Callable future üzerinden bir integer döndürür.”
- **Related:** call, calling; contrast: runnable

### cancel · verb

- **Türkçe:** iptal etmek
- **Java bağlamı:** `Future.cancel()` ile task'ın execution'ını önlemeye veya
  interrupt etmeye çalışmak.
- **Example:** “Cancellation does not always stop a running task immediately.”
- **Çeviri:** “Cancellation running task'ı her zaman hemen durdurmaz.”
- **Related:** cancellation, cancelled

### concurrent · adjective

- **Türkçe:** eşzamanlı ilerleyen
- **Java bağlamı:** Execution interval'ları overlap eden task/thread'ler.
- **Example:** “Concurrent tasks may access the same object.”
- **Çeviri:** “Concurrent task'lar aynı object'e erişebilir.”
- **Related:** concurrently, concurrency

### context switch · noun phrase

- **Türkçe:** bağlam değişimi
- **Java bağlamı:** Scheduler'ın bir thread state'ini saklayıp başka thread'e
  execution vermesi.
- **Example:** “Too many context switches can reduce throughput.”
- **Çeviri:** “Çok fazla context switch throughput'u azaltabilir.”
- **Related:** switch, scheduling

## D–H

### deadlock · noun

- **Türkçe:** kilitlenme
- **Java bağlamı:** Thread'lerin cycle halinde birbirinin lock'unu süresiz
  beklemesi.
- **Example:** “A consistent lock order helps prevent deadlock.”
- **Çeviri:** “Tutarlı lock order deadlock'ı önlemeye yardımcı olur.”
- **Related:** deadlocked; liveness failure

### decompose · verb

- **Türkçe:** parçalara ayırmak
- **Java bağlamı:** Parallel stream source'unu bağımsız işlenebilen
  partition'lara bölmek.
- **Example:** “The framework decomposes the source before parallel reduction.”
- **Çeviri:** “Framework parallel reduction öncesinde source'u parçalara
  ayırır.”
- **Related:** decomposition, decomposable

### deterministic · adjective

- **Türkçe:** belirlenebilir, her seferinde aynı kurala bağlı
- **Java bağlamı:** Scheduling değişse bile aynı guaranteed sonuç/order'a sahip
  davranış.
- **Example:** “The single-thread executor preserves a deterministic task
  order.”
- **Çeviri:** “Single-thread executor deterministic task order'ını korur.”
- **Related:** deterministically; antonym: nondeterministic

### executor · noun

- **Türkçe:** görev yürütücü
- **Java bağlamı:** Task submission, queue ve worker lifecycle'ını yöneten
  Concurrency API abstraction'ı.
- **Example:** “The executor reuses worker threads.”
- **Çeviri:** “Executor worker thread'leri yeniden kullanır.”
- **Related:** execute, execution, `ExecutorService`

### fairness · noun

- **Türkçe:** adillik
- **Java bağlamı:** Waiting thread'lere yaklaşık arrival order'da lock verme
  policy'si.
- **Example:** “Fairness may reduce starvation but can lower throughput.”
- **Çeviri:** “Fairness starvation'ı azaltabilir fakat throughput'u
  düşürebilir.”
- **Related:** fair, fairly; antonym: unfairness

### future · noun

- **Türkçe:** gelecekteki sonuç temsilcisi
- **Java bağlamı:** Asynchronous task result, exception veya cancellation
  state'ini temsil eden `Future<V>`.
- **Example:** “The future blocks when `get()` waits for an unfinished task.”
- **Çeviri:** “`get()` tamamlanmamış task'ı beklediğinde future blocking olur.”
- **Related:** `Future`, future result

## I–M

### interrupt · verb / noun

- **Türkçe:** kesme sinyali vermek; kesme
- **Java bağlamı:** Cooperative cancellation/wakeup signal'ı göndermek.
- **Example:** “Interrupting a thread while it is sleeping causes an
  `InterruptedException`.”
- **Çeviri:** “Bir thread'i sleep durumundayken interrupt etmek
  `InterruptedException` oluşmasına neden olur.”
- **Related:** interruption, interrupted, interruptible

### invariant · noun

- **Türkçe:** değişmez koşul
- **Java bağlamı:** Shared state update'leri arasında her zaman doğru kalması
  gereken business rule.
- **Example:** “The lock protects the account invariant.”
- **Çeviri:** “Lock account invariant'ını korur.”
- **Related:** invariant condition; maintain, preserve

### livelock · noun

- **Türkçe:** canlı kilit
- **Java bağlamı:** Thread'lerin aktif state değiştirdiği halde yararlı progress
  üretememesi.
- **Example:** “The workers remain active but make no progress in a livelock.”
- **Çeviri:** “Worker'lar livelock durumunda active kalır fakat ilerleyemez.”
- **Related:** liveness, retry loop

### liveness · noun

- **Türkçe:** ilerleyebilme özelliği
- **Java bağlamı:** Thread'lerin sonunda faydalı progress sağlayabilmesi.
- **Example:** “Deadlock is a liveness failure.”
- **Çeviri:** “Deadlock bir liveness failure'dır.”
- **Related:** live, progress; contrast: safety

### lock · noun / verb

- **Türkçe:** kilit; kilitlemek
- **Java bağlamı:** Critical section'a mutual exclusion sağlayan monitor veya
  `Lock` object.
- **Example:** “Always release an explicit lock in a finally block.”
- **Çeviri:** “Explicit lock'u her zaman finally block'ta bırakın.”
- **Related:** locking, locked, unlock

### memory consistency · noun phrase

- **Türkçe:** bellek tutarlılığı
- **Java bağlamı:** Thread'lerin shared write/read'leri uygun visibility ve
  ordering ile gözlemlemesi.
- **Example:** “Volatile fields help prevent memory consistency errors.”
- **Çeviri:** “Volatile field'lar memory consistency error'larını önlemeye
  yardımcı olur.”
- **Related:** consistent, consistency; visibility

### mutual exclusion · noun phrase

- **Türkçe:** karşılıklı dışlama
- **Java bağlamı:** Bir anda yalnız bir thread'in critical section'a girmesi.
- **Example:** “Synchronization provides mutual exclusion for the update.”
- **Çeviri:** “Synchronization update için mutual exclusion sağlar.”
- **Related:** mutually exclusive, mutex

## N–R

### nondeterministic · adjective

- **Türkçe:** sonucu/sırası kesin belirlenemeyen
- **Java bağlamı:** Valid output'un scheduler interleaving'ine göre
  değişebilmesi.
- **Example:** “Parallel `forEach` has nondeterministic output order.”
- **Çeviri:** “Parallel `forEach` nondeterministic output order'a sahiptir.”
- **Related:** nondeterminism; antonym: deterministic

### parallel · adjective / adverb

- **Türkçe:** paralel
- **Java bağlamı:** Task/stream partition'larının birden fazla worker üzerinde
  aynı anda yürütülebilmesi.
- **Example:** “A parallel stream may process several partitions at once.”
- **Çeviri:** “Parallel stream birden çok partition'ı aynı anda işleyebilir.”
- **Related:** parallelism, parallelize; contrast: sequential

### pool · noun

- **Türkçe:** havuz
- **Java bağlamı:** Task'lar arasında reuse edilen worker thread grubu.
- **Example:** “A fixed pool limits the number of active workers.”
- **Çeviri:** “Fixed pool active worker sayısını sınırlar.”
- **Related:** thread pool, pooling

### race condition · noun phrase

- **Türkçe:** yarış durumu
- **Java bağlamı:** Sonucun thread timing/interleaving'ine bağlı olarak invalid
  hale gelmesi.
- **Example:** “The unsynchronized increment contains a race condition.”
- **Çeviri:** “Unsynchronized increment race condition içerir.”
- **Related:** race, data race

### reduction · noun

- **Türkçe:** indirgeme
- **Java bağlamı:** Stream element'lerini identity, accumulator ve combiner ile
  tek result'a dönüştürmek.
- **Example:** “An associative operator is required for safe parallel
  reduction.”
- **Çeviri:** “Safe parallel reduction için associative operator gerekir.”
- **Related:** reduce, reducer

### release · verb

- **Türkçe:** serbest bırakmak
- **Java bağlamı:** Lock ownership'ini bırakmak veya barrier'daki waiting
  thread'leri devam ettirmek.
- **Example:** “The finally block releases the lock.”
- **Çeviri:** “Finally block lock'u serbest bırakır.”
- **Related:** release, released; antonym: acquire

### runnable · noun / adjective

- **Türkçe:** çalıştırılabilir void görev
- **Java bağlamı:** `void run()` contract'ına sahip `Runnable` task.
- **Example:** “The executor accepts the runnable without a return value.”
- **Çeviri:** “Executor return value olmayan runnable'ı kabul eder.”
- **Related:** run, running; contrast: callable

## S–Z

### schedule · verb / noun

- **Türkçe:** zamanlamak; zamanlama
- **Java bağlamı:** Task'ı gecikmeli veya periodic execution için planlamak.
- **Example:** “The service schedules the task with a fixed delay.”
- **Çeviri:** “Service task'ı fixed delay ile schedule eder.”
- **Related:** scheduler, scheduling, scheduled

### shutdown · noun / verb

- **Türkçe:** kapatma; düzenli biçimde kapatmak
- **Java bağlamı:** Executor'ın yeni task kabulünü durdurup lifecycle'ını
  sonlandırma.
- **Example:** “Shutdown allows previously submitted tasks to finish.”
- **Çeviri:** “Shutdown önceden submitted task'ların bitmesine izin verir.”
- **Related:** shut down, termination

### starvation · noun

- **Türkçe:** kaynak açlığı
- **Java bağlamı:** Bir thread'in sürekli diğerleri tercih edildiği için
  resource/CPU/lock alamaması.
- **Example:** “An unfair policy can contribute to starvation.”
- **Çeviri:** “Unfair policy starvation'a katkıda bulunabilir.”
- **Related:** starve, starved; liveness

### submit · verb

- **Türkçe:** görevi sunmak
- **Java bağlamı:** Task'ı executor'a verip çoğunlukla `Future` almak.
- **Example:** “Submit the callable and retain its future.”
- **Çeviri:** “Callable'ı submit edin ve future'ını saklayın.”
- **Related:** submission, submitted

### synchronized · adjective / Java keyword

- **Türkçe:** eşzamanlanmış
- **Java bağlamı:** Intrinsic monitor ile mutual exclusion ve happens-before
  sağlayan keyword.
- **Example:** “The synchronized method locks the current instance.”
- **Çeviri:** “Synchronized method current instance'ı lock eder.”
- **Related:** synchronize, synchronization

### task · noun

- **Türkçe:** görev
- **Java bağlamı:** Thread tarafından gerçekleştirilen tek work unit.
- **Example:** “A worker completes one task at a time.”
- **Çeviri:** “Worker bir seferde bir task tamamlar.”
- **Related:** work, operation

### thread-safe · adjective

- **Türkçe:** thread güvenli
- **Java bağlamı:** Bütün valid interleaving'lerde invariant'ları koruyan code.
- **Example:** “The class is thread-safe because all state changes use the same
  lock.”
- **Çeviri:** “Bütün state değişiklikleri aynı lock'u kullandığı için class
  thread-safe'tir.”
- **Related:** thread safety; antonym: unsafe

### throughput · noun

- **Türkçe:** birim zamanda yapılan iş miktarı
- **Java bağlamı:** Executor/parallel pipeline'ın belirli sürede tamamladığı
  task veya element sayısı.
- **Example:** “Excessive synchronization can reduce throughput.”
- **Çeviri:** “Aşırı synchronization throughput'u azaltabilir.”
- **Related:** performance, capacity

### timeout · noun / verb

- **Türkçe:** zaman aşımı
- **Java bağlamı:** `Future.get` veya `tryLock` gibi waiting operation için
  maksimum süre.
- **Example:** “The timed `get()` throws a timeout exception.”
- **Çeviri:** “Timed `get()` timeout exception fırlatır.”
- **Related:** time out, timed

### visibility · noun

- **Türkçe:** görünürlük
- **Java bağlamı:** Bir thread'in yaptığı write'ın başka thread tarafından
  gözlemlenebilmesi.
- **Example:** “Volatile improves visibility but not compound atomicity.”
- **Çeviri:** “Volatile visibility'yi iyileştirir fakat compound atomicity
  sağlamaz.”
- **Related:** visible, visibly; memory consistency

### volatile · adjective / Java keyword

- **Türkçe:** değişken; görünürlük sağlayan Java keyword'ü
- **Java bağlamı:** Field read/write için memory visibility ve ordering
  garantisi sağlar.
- **Example:** “A volatile flag can publish a shutdown request.”
- **Çeviri:** “Volatile flag shutdown request'i görünür kılabilir.”
- **Related:** volatility; contrast: atomic

### worker · noun

- **Türkçe:** işi yürüten thread
- **Java bağlamı:** Executor pool içindeki submitted task'ları çalıştıran
  thread.
- **Example:** “The pool reuses an idle worker for the next task.”
- **Çeviri:** “Pool sıradaki task için idle worker'ı yeniden kullanır.”
- **Related:** work, workload

## Mini quiz · Vocabulary recall

1. Thread'lerin birbirinin lock'unu cycle halinde beklemesi: __________
2. Active oldukları halde progress sağlayamamaları: __________
3. Bir thread'in sürekli resource alamaması: __________
4. Task result'ını gelecekte temsil eden object: __________
5. Source'u parallel partition'lara ayırma fiili: __________
6. Bir anda yalnız tek thread'in critical section'a girmesi: __________
7. Output'un scheduling'e göre değişebilmesi: __________
8. Lock'u elde etmek: __________
9. Lock'u bırakmak: __________
10. Unit time başına tamamlanan work miktarı: __________
11. Shared update'in bölünmez olma niteliği: __________
12. Bir write'ın diğer thread tarafından görülebilmesi: __________

## Cevaplar

1. deadlock
2. livelock
3. starvation
4. future
5. decompose
6. mutual exclusion
7. nondeterministic
8. acquire
9. release
10. throughput
11. atomic / atomicity
12. visibility
