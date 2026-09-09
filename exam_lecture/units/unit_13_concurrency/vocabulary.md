# Unit 13 · Concurrency — Vocabulary

Bu sözlük, [ana çift dilli nottaki](bilingual_notes.md) thread lifecycle,
executor, synchronization, liveness ve parallel stream bağlamında geçen
teknik/YDS kelimelerini alfabetik olarak toplar.

## A–C

### acquire · verb

- **Türkçe:** elde etmek, kilidi almak
- **Java bağlamı:** Thread'in monitor veya `Lock` ownership kazanması.
- **Example:** “The thread enters the block only after it acquires the lock.”
- **Çeviri:** “İş parçacığı, ancak kilidi edindikten sonra bloğa girer.”
- **Related:** acquisition, acquired; antonym: release

### atomic · adjective

- **Türkçe:** bölünmez, atomik
- **Java bağlamı:** Diğer thread'lerin aradaki state'i göremeyeceği tek logical
  operation.
- **Example:** “Incrementing an `AtomicInteger` is an atomic operation.”
- **Çeviri:** “Bir `AtomicInteger` değerini artırmak atomik bir işlemdir.”
- **Related:** atomically, atomicity; contrast: compound

### await · verb

- **Türkçe:** beklemek
- **Java bağlamı:** `CyclicBarrier.await()` veya executor termination için
  belirli event'i beklemek.
- **Example:** “Each worker awaits the other parties at the barrier.”
- **Çeviri:** “Her çalışan, bariyerde diğer katılımcıları bekler.”
- **Related:** wait, awaiting

### barrier · noun

- **Türkçe:** bariyer, eşgüdüm noktası
- **Java bağlamı:** Belirli sayıda thread ulaşana kadar ilerlemeyi durduran
  coordination object.
- **Example:** “The barrier releases the workers after the final arrival.”
- **Çeviri:** “Bariyer, son katılımcı geldikten sonra çalışanları serbest bırakır.”
- **Related:** `CyclicBarrier`, barrier action

### blocking · adjective / noun

- **Türkçe:** engelleyici, bekleten
- **Java bağlamı:** Thread'in result, lock veya queue item gelene kadar
  ilerleyememesi.
- **Example:** “A blocking call may put the thread into a waiting state.”
- **Çeviri:** “Bloklayan bir çağrı, iş parçacığını bekleme durumuna sokabilir.”
- **Related:** block, blocked; antonym: nonblocking

### callable · noun / adjective

- **Türkçe:** sonuç döndüren çağrılabilir görev
- **Java bağlamı:** Value döndürebilen ve checked exception declare edebilen
  `Callable<V>` task.
- **Example:** “The callable returns an integer through a future.”
- **Çeviri:** “`Callable`, sonucu bir `Future` üzerinden tamsayı olarak döndürür.”
- **Related:** call, calling; contrast: runnable

### cancel · verb

- **Türkçe:** iptal etmek
- **Java bağlamı:** `Future.cancel()` ile task'ın execution'ını önlemeye veya
  interrupt etmeye çalışmak.
- **Example:** “Cancellation does not always stop a running task immediately.”
- **Çeviri:** “İptal işlemi, çalışan bir görevi her zaman hemen durdurmaz.”
- **Related:** cancellation, cancelled

### concurrent · adjective

- **Türkçe:** eşzamanlı ilerleyen
- **Java bağlamı:** Execution interval'ları overlap eden task/thread'ler.
- **Example:** “Concurrent tasks may access the same object.”
- **Çeviri:** “Eşzamanlı görevler aynı nesneye erişebilir.”
- **Related:** concurrently, concurrency

### context switch · noun phrase

- **Türkçe:** bağlam değişimi
- **Java bağlamı:** Scheduler'ın bir thread state'ini saklayıp başka thread'e
  execution vermesi.
- **Example:** “Too many context switches can reduce throughput.”
- **Çeviri:** “Çok fazla bağlam değişimi, birim zamanda tamamlanan iş miktarını azaltabilir.”
- **Related:** switch, scheduling

## D–H

### deadlock · noun

- **Türkçe:** kilitlenme
- **Java bağlamı:** Thread'lerin cycle halinde birbirinin lock'unu süresiz
  beklemesi.
- **Example:** “A consistent lock order helps prevent deadlock.”
- **Çeviri:** “Tutarlı bir kilit edinme sırası, deadlock oluşmasını önlemeye yardımcı olur.”
- **Related:** deadlocked; liveness failure

### decompose · verb

- **Türkçe:** parçalara ayırmak
- **Java bağlamı:** Parallel stream source'unu bağımsız işlenebilen
  partition'lara bölmek.
- **Example:** “The framework decomposes the source before parallel reduction.”
- **Çeviri:** “Çatı, paralel indirgemeden önce kaynağı parçalara ayırır.”
- **Related:** decomposition, decomposable

### deterministic · adjective

- **Türkçe:** belirlenebilir, her seferinde aynı kurala bağlı
- **Java bağlamı:** Scheduling değişse bile aynı guaranteed sonuç/order'a sahip
  davranış.
- **Example:** “The single-thread executor preserves a deterministic task
  order.”
- **Çeviri:** “Tek iş parçacıklı yürütücü, belirli bir görev sırasını korur.”
- **Related:** deterministically; antonym: nondeterministic

### discard · verb

- **Türkçe:** atmak, işleme almadan bırakmak
- **Java bağlamı:** shutdownNow() sırasında yürütülmeyi bekleyen görevlerin işleme alınmaması.
- **Example · özgün:** “The executor discards waiting tasks during an immediate shutdown.”
- **Çeviri:** “Yürütücü, hemen kapatma sırasında bekleyen görevleri işleme almadan bırakır.”
- **Related:** discarded; synonym: abandon; contrast: retain.
- **Kaynak bağlamı:** [shutting down a thread executor](bilingual_notes.md#shutting-down-a-thread-executor)

### executor · noun

- **Türkçe:** görev yürütücü
- **Java bağlamı:** Task submission, queue ve worker lifecycle'ını yöneten
  Concurrency API abstraction'ı.
- **Example:** “The executor reuses worker threads.”
- **Çeviri:** “Yürütücü, çalışan iş parçacıklarını yeniden kullanır.”
- **Related:** execute, execution, `ExecutorService`

### fairness · noun

- **Türkçe:** adillik
- **Java bağlamı:** Waiting thread'lere yaklaşık arrival order'da lock verme
  policy'si.
- **Example:** “Fairness may reduce starvation but can lower throughput.”
- **Çeviri:** “Adil erişim, sürekli bekletilmeyi azaltabilir; ancak birim zamanda tamamlanan işi düşürebilir.”
- **Related:** fair, fairly; antonym: unfairness

### future · noun

- **Türkçe:** gelecekteki sonuç temsilcisi
- **Java bağlamı:** Asynchronous task result, exception veya cancellation
  state'ini temsil eden `Future<V>`.
- **Example:** “Calling `get()` blocks the caller until the task completes.”
- **Çeviri:** “Tamamlanmamış bir görevi bekleyen `get()` çağrısı, çağıran iş parçacığını bloklar.”
- **Related:** `Future`, future result

## I–M

### interrupt · verb / noun

- **Türkçe:** kesme sinyali vermek; kesme
- **Java bağlamı:** Cooperative cancellation/wakeup signal'ı göndermek.
- **Example:** “Interrupting a thread while it is sleeping causes an
  `InterruptedException`.”
- **Çeviri:** “Uyuyan bir iş parçacığına kesme isteği göndermek `InterruptedException` oluşmasına yol açar.”
- **Related:** interruption, interrupted, interruptible

### invariant · noun

- **Türkçe:** değişmez koşul
- **Java bağlamı:** Shared state update'leri arasında her zaman doğru kalması
  gereken business rule.
- **Example:** “The lock protects the account invariant.”
- **Çeviri:** “Kilit, hesaba ilişkin korunması gereken koşulu korur.”
- **Related:** invariant condition; maintain, preserve

### livelock · noun

- **Türkçe:** canlı kilit
- **Java bağlamı:** Thread'lerin aktif state değiştirdiği halde yararlı progress
  üretememesi.
- **Example:** “The workers remain active but make no progress in a livelock.”
- **Çeviri:** “Livelock durumunda çalışanlar etkin kalır; ancak ilerleme kaydedemez.”
- **Related:** liveness, retry loop

### liveness · noun

- **Türkçe:** ilerleyebilme özelliği
- **Java bağlamı:** Thread'lerin sonunda faydalı progress sağlayabilmesi.
- **Example:** “Deadlock is a liveness failure.”
- **Çeviri:** “Deadlock, işin ilerleyebilmesi özelliğinin bozulmasıdır.”
- **Related:** live, progress; contrast: safety

### lock · noun / verb

- **Türkçe:** kilit; kilitlemek
- **Java bağlamı:** Critical section'a mutual exclusion sağlayan monitor veya
  `Lock` object.
- **Example:** “Always release an explicit lock in a finally block.”
- **Çeviri:** “Açıkça edinilmiş bir kilidi her zaman `finally` bloğunda bırakın.”
- **Related:** locking, locked, unlock

### memory consistency · noun phrase

- **Türkçe:** bellek tutarlılığı
- **Java bağlamı:** Thread'lerin shared write/read'leri uygun visibility ve
  ordering ile gözlemlemesi.
- **Example:** “Volatile fields help prevent memory consistency errors.”
- **Çeviri:** “`volatile` alanlar, bellek tutarlılığı hatalarını önlemeye yardımcı olur.”
- **Related:** consistent, consistency; visibility

### mutual exclusion · noun phrase

- **Türkçe:** karşılıklı dışlama
- **Java bağlamı:** Bir anda yalnız bir thread'in critical section'a girmesi.
- **Example:** “Synchronization provides mutual exclusion for the update.”
- **Çeviri:** “Senkronizasyon, güncelleme sırasında karşılıklı dışlama sağlar.”
- **Related:** mutually exclusive, mutex

## N–R

### nondeterministic · adjective

- **Türkçe:** sonucu/sırası kesin belirlenemeyen
- **Java bağlamı:** Valid output'un scheduler interleaving'ine göre
  değişebilmesi.
- **Example:** “Parallel `forEach` has nondeterministic output order.”
- **Çeviri:** “Paralel `forEach` çıktısının sırası kesin belirlenemez.”
- **Related:** nondeterminism; antonym: deterministic

### parallel · adjective / adverb

- **Türkçe:** paralel
- **Java bağlamı:** Task/stream partition'larının birden fazla worker üzerinde
  aynı anda yürütülebilmesi.
- **Example:** “A parallel stream may process several partitions at once.”
- **Çeviri:** “Paralel bir akış, birden fazla parçayı aynı anda işleyebilir.”
- **Related:** parallelism, parallelize; contrast: sequential

### pool · noun

- **Türkçe:** havuz
- **Java bağlamı:** Task'lar arasında reuse edilen worker thread grubu.
- **Example:** “A fixed pool limits the number of active workers.”
- **Çeviri:** “Sabit büyüklükteki havuz, etkin çalışan sayısını sınırlar.”
- **Related:** thread pool, pooling

### potential · adjective / noun

- **Türkçe:** olası; potansiyel
- **Java bağlamı:** Gerçekleşmesi mümkün olan iş parçacığı sorunu; kesin gerçekleşme değildir.
- **Example · özgün:** “Shared mutable state is a source of potential problems.”
- **Çeviri:** “Paylaşılan değiştirilebilir durum, olası sorunların kaynağıdır.”
- **Related:** potentially; contrast: actual.
- **Kaynak bağlamı:** [identifying threading problems](bilingual_notes.md#identifying-threading-problems)

### race condition · noun phrase

- **Türkçe:** yarış durumu
- **Java bağlamı:** Sonucun thread timing/interleaving'ine bağlı olarak invalid
  hale gelmesi.
- **Example:** “The unsynchronized increment contains a race condition.”
- **Çeviri:** “Senkronize edilmemiş artırma işleminde yarış durumu vardır.”
- **Related:** race, data race

### reduction · noun

- **Türkçe:** indirgeme
- **Java bağlamı:** Stream element'lerini identity, accumulator ve combiner ile
  tek result'a dönüştürmek.
- **Example:** “An associative operator is required for safe parallel
  reduction.”
- **Çeviri:** “Güvenli paralel indirgeme için birleşme özelliğine sahip bir işlem gerekir.”
- **Related:** reduce, reducer

### release · verb

- **Türkçe:** serbest bırakmak
- **Java bağlamı:** Lock ownership'ini bırakmak veya barrier'daki waiting
  thread'leri devam ettirmek.
- **Example:** “The finally block releases the lock.”
- **Çeviri:** “`finally` bloğu kilidi bırakır.”
- **Related:** release, released; antonym: acquire

### runnable · noun / adjective

- **Türkçe:** çalıştırılabilir void görev
- **Java bağlamı:** `void run()` contract'ına sahip `Runnable` task.
- **Example:** “The executor accepts the runnable without a return value.”
- **Çeviri:** “Yürütücü, dönüş değeri olmayan `Runnable` görevini kabul eder.”
- **Related:** run, running; contrast: callable

## S–Z

### schedule · verb / noun

- **Türkçe:** zamanlamak; zamanlama
- **Java bağlamı:** Task'ı gecikmeli veya periodic execution için planlamak.
- **Example:** “The service schedules the task with a fixed delay.”
- **Çeviri:** “Servis, görevi sabit gecikmeyle çalışacak şekilde zamanlar.”
- **Related:** scheduler, scheduling, scheduled

### shutdown · noun / verb

- **Türkçe:** kapatma; düzenli biçimde kapatmak
- **Java bağlamı:** Executor'ın yeni task kabulünü durdurup lifecycle'ını
  sonlandırma.
- **Example:** “Shutdown allows previously submitted tasks to finish.”
- **Çeviri:** “Kapatma süreci, daha önce gönderilmiş görevlerin tamamlanmasına izin verir.”
- **Related:** shut down, termination

### starvation · noun

- **Türkçe:** kaynak açlığı
- **Java bağlamı:** Bir thread'in sürekli diğerleri tercih edildiği için
  resource/CPU/lock alamaması.
- **Example:** “An unfair policy can contribute to starvation.”
- **Çeviri:** “Adil olmayan bir politika, bir iş parçacığının sürekli bekletilmesine katkıda bulunabilir.”
- **Related:** starve, starved; liveness

### submit · verb

- **Türkçe:** görevi sunmak
- **Java bağlamı:** Task'ı executor'a verip çoğunlukla `Future` almak.
- **Example:** “Submit the callable and retain its future.”
- **Çeviri:** “`Callable` görevini gönderin ve dönen `Future` nesnesini saklayın.”
- **Related:** submission, submitted

### synchronized · adjective / Java keyword

- **Türkçe:** eşzamanlanmış
- **Java bağlamı:** Intrinsic monitor ile mutual exclusion ve happens-before
  sağlayan keyword.
- **Example:** “The synchronized instance method locks the current instance.”
- **Çeviri:** “Senkronize edilmiş örnek metodu, geçerli nesneyi kilitler.”
- **Related:** synchronize, synchronization

### task · noun

- **Türkçe:** görev
- **Java bağlamı:** Thread tarafından gerçekleştirilen tek work unit.
- **Example:** “A worker completes one task at a time.”
- **Çeviri:** “Bir çalışan, bir seferde tek bir görevi tamamlar.”
- **Related:** work, operation

### thread-safe · adjective

- **Türkçe:** thread güvenli
- **Java bağlamı:** Bütün valid interleaving'lerde invariant'ları koruyan code.
- **Example:** “The class is thread-safe because all state changes use the same
  lock.”
- **Çeviri:** “Bütün durum değişiklikleri aynı kilidi kullandığından sınıf eşzamanlı erişimde güvenlidir.”
- **Related:** thread safety; antonym: unsafe

### throughput · noun

- **Türkçe:** birim zamanda yapılan iş miktarı
- **Java bağlamı:** Executor/parallel pipeline'ın belirli sürede tamamladığı
  task veya element sayısı.
- **Example:** “Excessive synchronization can reduce throughput.”
- **Çeviri:** “Aşırı senkronizasyon, birim zamanda tamamlanan iş miktarını azaltabilir.”
- **Related:** performance, capacity

### timeout · noun / verb

- **Türkçe:** zaman aşımı
- **Java bağlamı:** `Future.get` veya `tryLock` gibi waiting operation için
  maksimum süre.
- **Example:** “The timed `get()` may throw a timeout exception.”
- **Çeviri:** “Süre sınırlı `get()` çağrısı, zaman aşımı istisnası fırlatabilir.”
- **Related:** time out, timed

### visibility · noun

- **Türkçe:** görünürlük
- **Java bağlamı:** Bir thread'in yaptığı write'ın başka thread tarafından
  gözlemlenebilmesi.
- **Example:** “Volatile improves visibility but not compound atomicity.”
- **Çeviri:** “`volatile`, görünürlüğü iyileştirir; birleşik işlemleri atomik hâle getirmez.”
- **Related:** visible, visibly; memory consistency

### volatile · adjective / Java keyword

- **Türkçe:** değişken; görünürlük sağlayan Java keyword'ü
- **Java bağlamı:** Field read/write için memory visibility ve ordering
  garantisi sağlar.
- **Example:** “A volatile flag can publish a shutdown request.”
- **Çeviri:** “`volatile` bir bayrak, kapatma isteğini diğer iş parçacıklarına görünür kılabilir.”
- **Related:** volatility; contrast: atomic

### worker · noun

- **Türkçe:** işi yürüten thread
- **Java bağlamı:** Executor pool içindeki submitted task'ları çalıştıran
  thread.
- **Example:** “The pool reuses an idle worker for the next task.”
- **Çeviri:** “Havuz, sonraki görev için boşta duran bir çalışanı yeniden kullanır.”
- **Related:** work, workload

## Karıştırılan anlamları ayır

**concurrent / parallel:** `concurrent`, görevlerin ilerleyişinin aynı zaman aralığında örtüşmesidir; tek çekirdekte sırayla ilerleyebilirler. `parallel`, işlerin aynı anda yürütülmesini anlatır.

`visibility`, bir yazmanın görülebilmesi; `atomicity`, işlemin bölünmezliği. `throughput`, birim zamanda iş miktarı; tek görevin tamamlanma süresiyle aynı ölçü değildir.

## Kapalı kitap hatırlama · 5 dakika

Her oturumda en fazla 5 kelime seç. Önce Türkçeyi kapatıp İngilizce cümleyi
çevir; ardından İngilizceyi kapatıp Türkçe anlamdan sözcüğü ve kendi örneğini
üret. Yalnız “tanıdık geldi” yanıtını başarı sayma: **0 = çıkaramadım,
1 = anlamını söyledim, 2 = doğru teknik cümlede kullandım**. 0–1 puanlıları
ünite [tekrar rotasına](README.md) göre geri getir.

**Özgün aktarım sorusu:** `volatile` bir sayacı neden `atomic` yapmaz? `visibility`, `compound`, `although` kullan.

Cevabını yazdıktan sonra kontrol et.

**Örnek yanıt:** Although volatile provides visibility, a compound increment is not atomic.

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
