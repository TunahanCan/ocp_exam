# Ünite 07 · Implementing queries in a microservice architecture — Vocabulary

**Amaç:** Bu ünitenin 220–252. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 224, 225, 231, 235, 237 ve devamı:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 224, 235, 236, 239, 241 ve devamı:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### API composition · noun phrase

**Türkçe:** API sonuçlarını birleştirme

**Bağlam — kaynak s. 220, 221, 222, 223, 224 ve devamı:** Birden fazla servisten veri okuyup tek sorgu sonucu oluşturma yaklaşımıdır.

> **English:** API composition combines responses from several services.
>
> **Türkçe:** API composition, birkaç servisin yanıtlarını birleştirir.

**İlişkili sözcükler:** compose; composer; aggregate results

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 227, 228:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 227, 228, 235, 236, 238:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 240, 242:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### concurrency · noun

**Türkçe:** eşzamanlılık

**Bağlam — kaynak s. 239, 252:** Birden fazla işlemin zaman bakımından çakışacak biçimde ilerlemesidir.

> **English:** Concurrency can expose inconsistent intermediate states.
>
> **Türkçe:** Eşzamanlılık, tutarsız ara durumların görülmesine yol açabilir.

**İlişkili sözcükler:** concurrent; concurrently

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 221, 229, 230, 232, 242 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### CQRS · abbreviation / noun

**Türkçe:** komut ve sorgu sorumluluklarının ayrılması

**Bağlam — kaynak s. 220, 221, 228, 229, 230 ve devamı:** Command Query Responsibility Segregation; güncelleme işlemleriyle okuma işlemleri için ayrı modeller kullanılmasını sağlar.

> **English:** CQRS separates the command model from the query model.
>
> **Türkçe:** CQRS, komut modelini sorgu modelinden ayırır.

**İlişkili sözcükler:** command; query; read model; write model

### CQRS view · noun phrase

**Türkçe:** CQRS sorgu görünümü

**Bağlam — kaynak s. 221, 235, 236, 237, 238 ve devamı:** Belirli sorgulara uygun biçimde düzenlenmiş veri kopyasıdır; kaynak verideki değişiklikleri olaylar aracılığıyla izler.

> **English:** The CQRS view stores data in a form suited to its queries.
>
> **Türkçe:** CQRS görünümü, veriyi kendi sorgularına uygun bir biçimde saklar.

**İlişkili sözcükler:** query model; view database; event handler

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 220, 227, 228:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 232, 241:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed system · noun phrase

**Türkçe:** dağıtık sistem

**Bağlam — kaynak s. 227:** Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.

> **English:** A distributed system must handle partial failures.
>
> **Türkçe:** Dağıtık bir sistem, kısmi arızaları ele almalıdır.

**İlişkili sözcükler:** distribute, distribution; ilişkili: remote call, interprocess communication.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 232, 233:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### domain model · noun phrase

**Türkçe:** alan modeli

**Bağlam — kaynak s. 232, 235:** İş kurallarını ve alan kavramlarını nesneler ve ilişkilerle temsil eder.

> **English:** The domain model contains business rules.
>
> **Türkçe:** Alan modeli, iş kurallarını içerir.

**İlişkili sözcükler:** domain-driven design

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 227, 228, 230, 235, 236:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 223, 224, 227, 242:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 232, 235:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

### event store · noun phrase

**Türkçe:** olay deposu

**Bağlam — kaynak s. 235:** Aggregate olaylarını sıralı geçmiş olarak kalıcı biçimde saklayan altyapıdır.

> **English:** The event store preserves the event sequence.
>
> **Türkçe:** Olay deposu, olay sırasını korur.

**İlişkili sözcükler:** event stream; persistence

### eventually consistent · adjective phrase

**Türkçe:** nihai olarak tutarlı

**Bağlam — kaynak s. 232, 241:** Yeni güncellemeler durduğunda ve bekleyen güncellemeler işlendiğinde kopyalar aynı duruma yaklaşır; arada eski veri okunabilir.

> **English:** The query view is eventually consistent.
>
> **Türkçe:** Sorgu görünümü, nihai olarak tutarlıdır.

**İlişkili sözcükler:** eventual consistency

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 238:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

## I

### idempotent · adjective

**Türkçe:** aynı işlem yinelendiğinde ek etki üretmeyen

**Bağlam — kaynak s. 237, 239, 240, 244, 248 ve devamı:** Aynı mesajın tekrar işlenmesi, iş etkisini çoğaltmaz.

> **English:** An idempotent handler tolerates duplicate messages.
>
> **Türkçe:** Idempotent bir işleyici, yinelenen mesajları tolere eder.

**İlişkili sözcükler:** idempotency; idempotence

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 224:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

### isolation · noun

**Türkçe:** yalıtım

**Bağlam — kaynak s. 228:** Eşzamanlı transaction işlemlerinin ara etkilerini birbirinden koruma özelliğidir.

> **English:** Sagas do not provide transaction isolation automatically.
>
> **Türkçe:** Saga'lar transaction yalıtımını kendiliğinden sağlamaz.

**İlişkili sözcükler:** isolate; isolated

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 227, 241:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 220, 221, 228, 231, 232 ve devamı:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

## O

### optimistic locking · noun phrase

**Türkçe:** iyimser kilitleme

**Bağlam — kaynak s. 240, 248:** Çakışma yok varsayımıyla çalışır; yazma anında sürümü kontrol eder.

> **English:** Optimistic locking detects conflicting updates.
>
> **Türkçe:** İyimser kilitleme, çakışan güncellemeleri saptar.

**İlişkili sözcükler:** version; concurrency control

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 227:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 220, 221, 222, 223, 224 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### primary key · noun phrase

**Türkçe:** birincil anahtar

**Bağlam — kaynak s. 221, 224, 233, 235, 238 ve devamı:** Bir kaydı benzersiz olarak tanımlar; DynamoDB bağlamında partition key ve isteğe bağlı sort key içerebilir.

> **English:** The primary key uniquely identifies an item.
>
> **Türkçe:** Birincil anahtar, bir öğeyi benzersiz olarak tanımlar.

**İlişkili sözcükler:** partition key; sort key; composite key

### provider · noun

**Türkçe:** sağlayıcı

**Bağlam — kaynak s. 223, 224, 225, 226, 227 ve devamı:** Bir API, mesaj veya hizmet sunan taraftır.

> **English:** The provider must satisfy its API contract.
>
> **Türkçe:** Sağlayıcı, API sözleşmesini karşılamalıdır.

**İlişkili sözcükler:** provide; consumer

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 220, 221, 222, 223, 224 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### reliability · noun

**Türkçe:** güvenilirlik

**Bağlam — kaynak s. 228:** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.

> **English:** Frequent failures reduce the reliability of the application.
>
> **Türkçe:** Sık arızalar, uygulamanın güvenilirliğini azaltır.

**İlişkili sözcükler:** reliable, reliably, unreliable; karşılaştırma: availability.

### replication lag · noun phrase

**Türkçe:** replikasyon gecikmesi

**Bağlam — kaynak s. 236, 237:** Ana verideki değişiklik ile kopyanın bu değişikliği yansıtması arasındaki gecikmedir.

> **English:** Replication lag can make the query return stale data.
>
> **Türkçe:** Replikasyon gecikmesi, sorgunun eski veri döndürmesine yol açabilir.

**İlişkili sözcükler:** replicate; replica; stale data

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 220, 221, 222, 223, 224 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 225:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 220:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 237:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### snapshot · noun

**Türkçe:** belirli bir andaki durumun kopyası

**Bağlam — kaynak s. 242:** Geçmiş olayların hepsini tekrar okumadan yeniden yüklemeyi hızlandırabilir.

> **English:** The snapshot reduces the number of events to replay.
>
> **Türkçe:** Snapshot, yeniden yürütülecek olay sayısını azaltır.

**İlişkili sözcükler:** snapshotting; restore

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 220, 221, 231, 239:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

## T

### take into account · verb phrase

**Türkçe:** hesaba katmak, dikkate almak

**Bağlam — kaynak s. 232:** Bir tasarım veya uygulama kararında ilgili gereksinimleri, sınırlamaları ve başka etkenleri hesaba katmaktır.

> **English:** The migration plan must take team structure into account.
>
> **Türkçe:** Geçiş planı, ekip yapısını hesaba katmalıdır.

**İlişkili sözcükler:** synonym: consider, allow for; karşıt: overlook, disregard.

### throughput · noun

**Türkçe:** birim zamanda işlenen iş miktarı

**Bağlam — kaynak s. 242:** Sistemin belirli sürede tamamladığı istek veya mesaj sayısını anlatır.

> **English:** Throughput measures completed requests per second.
>
> **Türkçe:** Throughput, saniyede tamamlanan istekleri ölçer.

**İlişkili sözcükler:** processing rate; compare: latency

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 220, 228, 237, 238, 241:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 221, 225, 228, 229, 233 ve devamı:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** eşzamanlılık

**3.** dağıtık sistem

**4.** olay deposu

**5.** gecikme

**6.** sağlayıcı

**7.** yerel transaction adımlarından oluşan iş akışı

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. concurrency** — Birden fazla işlemin zaman bakımından çakışacak biçimde ilerlemesidir.

**3. distributed system** — Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.

**4. event store** — Aggregate olaylarını sıralı geçmiş olarak kalıcı biçimde saklayan altyapıdır.

**5. latency** — Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

**6. provider** — Bir API, mesaj veya hizmet sunan taraftır.

**7. saga** — Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
