# Unit 13 · Concurrency — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) thread, synchronization
ve parallel processing anlatımından seçilen gerçek teknik İngilizce yapılarını
YDS/teknik okuma açısından açıklar.

## 1. `as compared to/with`

### Yapı

```text
as compared to/with + noun
```

Bir şeyi başka bir referansa göre karşılaştırır.

> **English:** “Disk operations are slow as compared to CPU operations.”
>
> **Türkçe:** “Disk operation'ları CPU operation'larına kıyasla yavaştır.”

YDS ipucu: `compared with/to`, `in comparison with` aynı comparison alanına
aittir.

## 2. `so + adjective/adverb + that`

### Yapı

```text
so + adjective/adverb + that + result clause
```

Derece ve onun sonucunu bildirir.

> **English:** “The operation may be so slow that the application appears to
> freeze.”
>
> **Türkçe:** “Operation o kadar yavaş olabilir ki application donmuş gibi
> görünür.”

`so that + clause` amaç; `so ... that` derece-sonuç yapısıdır.

## 3. `allow + object + to + V1`

### Yapı

```text
allow + noun/pronoun + to + base verb
```

Bir kişi veya bileşene eylem olanağı verir.

> **English:** “Multithreaded processing allows an application to execute
> several tasks.”
>
> **Türkçe:** “Multithreaded processing application'ın birden çok task
> yürütmesine olanak sağlar.”

Passive: `Tasks are allowed to continue.` Sık hata: object'ten sonra `to`
unutmak.

## 4. `what is known as`

### Yapı

```text
what is known as + term
```

“...olarak bilinen şey/kavram” anlamında free relative clause oluşturur.

> **English:** “Operating systems support what is known as multithreaded
> processing.”
>
> **Türkçe:** “Operating system'ler multithreaded processing olarak bilinen
> yapıyı destekler.”

`what` kendi antecedent'ını içerir; önüne ayrıca `the thing` getirilmez.

## 5. `whereas`

### Yapı

```text
clause, whereas + contrasting clause
```

İki özellik arasında açık contrast kurar.

> **English:** “`Runnable` returns no value, whereas `Callable` returns a
> generic value.”
>
> **Türkçe:** “`Runnable` value döndürmezken `Callable` generic value döndürür.”

YDS'de `whereas` çoğunlukla `while`ın contrast anlamına eşittir; zaman
bildirmez.

## 6. `by + V-ing`

### Yapı

```text
main clause + by + gerund
```

Bir sonuca ulaşma yöntemini açıklar.

> **English:** “The executor improves efficiency by reusing worker threads.”
>
> **Türkçe:** “Executor worker thread'leri yeniden kullanarak verimliliği
> artırır.”

`by` sonrası base verb değil gerund gerekir.

## 7. `when + present, present/future`

### Yapı

```text
when + present simple, present simple
when + present simple, will/can + V1
```

Genel kural veya gelecekteki koşullu zamanı anlatır.

> **English:** “When the final thread arrives, the barrier releases all
> parties.”
>
> **Türkçe:** “Son thread ulaştığında barrier bütün party'leri serbest
> bırakır.”

Future anlamında time clause içinde çoğunlukla `will arrive` değil `arrives`
kullanılır.

## 8. `while + clause`

### Yapı

```text
while + ongoing action, main clause
while + contrast clause, main clause
```

Eşzamanlılık veya contrast bildirir.

> **English:** “One thread waits while another thread holds the lock.”
>
> **Türkçe:** “Bir thread beklerken diğer thread lock'u tutar.”

Context'e göre “...iken” zaman, “oysa” contrast anlamını ayır.

## 9. Real conditional: `if + present`

### Yapı

```text
if + present simple, present simple / will / can + V1
```

Gerçek veya genel olasılığı anlatır.

> **English:** “If `tryLock()` returns false, the thread must not call
> `unlock()`.”
>
> **Türkçe:** “`tryLock()` false döndürürse thread `unlock()` çağırmamalıdır.”

YDS ipucu: Condition clause'ta future anlam olsa bile genellikle present
simple kullanılır.

## 10. `may/might/can + V1`

### Yapı

```text
subject + may/might/can + base verb
```

`may/might` possibility; `can` ability veya genel possibility bildirir.

> **English:** “A parallel operation may produce a different encounter order.”
>
> **Türkçe:** “Parallel operation farklı encounter order üretebilir.”

Modal'dan sonra `to` gelmez ve verb çekimlenmez.

## 11. `be capable of + V-ing`

### Yapı

```text
subject + be capable of + noun/gerund
```

Bir kapasite veya mümkün davranışı anlatır.

> **English:** “A `Callable` is capable of throwing a checked exception.”
>
> **Türkçe:** “`Callable` checked exception fırlatabilir.”

`of` preposition olduğu için `throwing` gerekir; `capable to throw` yanlıştır.

## 12. `tend to + V1`

### Yapı

```text
subject + tend(s) to + base verb
```

Kesin garanti değil, genel eğilim bildirir.

> **English:** “Small parallel workloads tend to run more slowly.”
>
> **Türkçe:** “Küçük parallel workload'lar daha yavaş çalışma eğilimindedir.”

YDS'de `tend to`yu `always` gibi mutlak yorumlama.

## 13. `in order to + V1`

### Yapı

```text
in order to + base verb
in order not to + base verb
```

Amaç bildirir.

> **English:** “Use the same lock in order to protect the invariant.”
>
> **Türkçe:** “Invariant'ı korumak için aynı lock'u kullanın.”

`in order that` sonrasında subject + verb içeren clause gelir.

## 14. `once + clause / past participle`

### Yapı

```text
once + subject + verb, main clause
once + past participle, main clause
```

Bir state transition tamamlandıktan sonraki sonucu anlatır.

> **English:** “Once terminated, a thread cannot be started again.”
>
> **Türkçe:** “Thread terminate olduktan sonra yeniden başlatılamaz.”

Reduced clause subject'i main clause subject'iyle uyumlu olmalıdır.

## 15. `regardless of whether`

### Yapı

```text
regardless of whether + clause A + or + clause B
```

İki olasılığın da sonucu değiştirmediğini gösterir.

> **English:** “`findAny()` may select any element regardless of whether the
> stream is sequential or parallel.”
>
> **Türkçe:** “Stream sequential veya parallel olsa da `findAny()` herhangi bir
> element seçebilir.”

`regardless` sonrasında `of` unutulmamalıdır.

## 16. `unlike + noun`

### Yapı

```text
unlike + noun/pronoun, complete clause
```

Farklı özellikleri contrast eder.

> **English:** “Unlike `execute()`, `submit()` returns a `Future`.”
>
> **Türkçe:** “`execute()`dan farklı olarak `submit()` bir `Future` döndürür.”

`unlike` preposition; `although` conjunction'dır. Ardından gelecek yapıyı buna
göre seç.

## 17. `even though + clause`

### Yapı

```text
even though + subject + verb, main clause
```

Güçlü concessive contrast bildirir.

> **English:** “Even though the field is volatile, the increment is not
> atomic.”
>
> **Türkçe:** “Field volatile olsa da increment atomic değildir.”

`even though` gerçek olgu; `even if` varsayımsal koşul için daha doğaldır.

## 18. `due to / because of + noun`

### Yapı

```text
due to + noun phrase
because of + noun phrase
because + clause
```

Neden bildirir.

> **English:** “The result varies because of different thread interleavings.”
>
> **Türkçe:** “Sonuç farklı thread interleaving'leri nedeniyle değişir.”

YDS ipucu: `because` tam clause, `because of` noun phrase alır.

## 19. `prevent + object + from + V-ing`

### Yapı

```text
prevent + noun/pronoun + from + gerund
```

Bir eylemin gerçekleşmesini engeller.

> **English:** “An unclosed executor may prevent the JVM from terminating.”
>
> **Türkçe:** “Kapatılmamış executor JVM'in terminate olmasını
> engelleyebilir.”

`from` sonrası gerund zorunludur: `from terminating`.

## 20. `result in + noun/gerund`

### Yapı

```text
subject/cause + result(s) in + noun/gerund (effect)
```

Neden → sonuç yönünde ilişki kurar.

> **English:** “Ignoring the return value may result in an invalid unlock.”
>
> **Türkçe:** “Return value'yu göz ardı etmek invalid unlock ile
> sonuçlanabilir.”

Ters yön: `result from + cause` = “...den kaynaklanmak”.

## 21. `cause + object + to + V1`

### Yapı

```text
cause + noun/pronoun + to + base verb
```

Bir durumun başka bir eylemi doğurmasını anlatır.

> **English:** “An interrupt can cause a sleeping thread to throw an
> exception.”
>
> **Türkçe:** “Interrupt sleeping thread'in exception fırlatmasına neden
> olabilir.”

Passive: `The thread is caused to wake` grammatical olsa da teknik metinde
çoğunlukla active neden yapısı kullanılır.

## 22. `be designed to + V1`

### Yapı

```text
subject + be designed to + base verb
```

Bir API/class'ın amaçlanan görevini bildirir.

> **English:** “Concurrent collections are designed to support safe concurrent
> access.”
>
> **Türkçe:** “Concurrent collection'lar safe concurrent access'i desteklemek
> üzere tasarlanmıştır.”

YDS'de “tasarım amacı” ile gerçek guarantee'yi karıştırma; object'in contract'ı
ayrıca okunmalıdır.

## 23. `no matter how/when/which`

### Yapı

```text
no matter how + adjective/adverb + clause
no matter when/which + clause
```

Seçenek veya derecenin sonucu değiştirmediğini gösterir.

> **English:** “The output is not guaranteed no matter how often one order is
> observed.”
>
> **Türkçe:** “Bir sıra ne kadar sık gözlemlenirse gözlemlensin output garanti
> değildir.”

`no matter how` concessive anlamlıdır; soru cümlesi değildir.

## 24. Comparative correlative: `the more ..., the more ...`

### Yapı

```text
the + comparative + clause, the + comparative + clause
```

İki değişkenin birlikte artış/azalış ilişkisini anlatır.

> **English:** “The more shared state a task modifies, the harder it is to
> reason about thread safety.”
>
> **Türkçe:** “Task ne kadar fazla shared state değiştirirse thread safety
> hakkında reasoning yapmak o kadar zorlaşır.”

İlk `the` article değil, comparative correlative marker'dır.

## 25. `either ... or ...`

### Yapı

```text
either + alternative A + or + alternative B
```

İki alternatif sunar.

> **English:** “A task either completes normally or records an exception in
> its future.”
>
> **Türkçe:** “Task ya normal tamamlanır ya da future'ına exception kaydeder.”

Subject agreement yakın öğeye göre değişebilir; teknik listelerde parallel
structure'ı koru.

## Mini quiz · Özgün YDS/teknik İngilizce çalışması

1. Disk access is slow as compared ___ CPU access.
2. The task was so slow ___ the timeout expired.
3. Executors allow tasks ___ run on reusable workers.
4. Complete: “`Runnable` returns void, ___ `Callable` returns a value.”
5. Choose: `capable of throwing / capable to throw`.
6. Complete: “The executor improves throughput by ___ workers.” (`reuse`)
7. Choose: “When the last party `will arrive / arrives`, the barrier trips.”
8. The JVM may fail to terminate because ___ an unclosed executor.
9. Rewrite with `prevent`: “An unclosed executor stops the JVM from
   terminating.”
10. Complete: “Even ___ the field is volatile, `count++` is unsafe.”
11. `result in` cause→result mı, result→cause mı gösterir?
12. Complete: “The more locks a task acquires, the ___ the deadlock analysis
   becomes.” (`complex`)
13. Choose: `regardless whether / regardless of whether`.
14. Rewrite compactly: “Once a thread is terminated, it cannot restart.”

## Cevaplar ve kısa açıklamalar

1. **to/with**
2. **that** — `so ... that` result clause.
3. **to** — `allow + object + to V1`.
4. **whereas** — Contrast.
5. **capable of throwing** — `of` sonrası gerund.
6. **reusing** — `by + V-ing`.
7. **arrives** — Future time clause'ta present simple.
8. **of** — `because of + noun phrase`.
9. **An unclosed executor may prevent the JVM from terminating.**
10. **though** — Gerçek concessive fact.
11. **Cause → result.** `result from` ters yönde cause'u gösterir.
12. **more complex**
13. **regardless of whether**
14. **Once terminated, a thread cannot restart.**

## Hızlı YDS özeti

```text
karşılaştırma     as compared to / whereas / unlike
derece-sonuç      so ... that
olanak            allow ... to / be capable of
eğilim            tend to
yöntem            by + V-ing
zaman             when / while / once
koşul             if
olasılık          may / might / can
amaç              in order to / be designed to
ödünleme          even though / regardless of whether / no matter how
neden             due to / because of / result from
sonuç             result in / cause ... to
engel             prevent ... from V-ing
oranlı değişim    the more ..., the more ...
alternatif        either ... or ...
```
