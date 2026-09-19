# Ünite 06 · Developing business logic with event sourcing — Vocabulary

**Amaç:** Bu ünitenin 183–219. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 201, 210, 213:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 183, 184, 185, 186, 187 ve devamı:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### aggregate root · noun phrase

**Türkçe:** aggregate kökü

**Bağlam — kaynak s. 189, 191, 193:** Aggregate dışındaki nesnelerin bütünle etkileşim kurduğu, erişimi ve tutarlılık kurallarını yöneten kök entity’dir.

> **English:** Other objects reference the aggregate root.
>
> **Türkçe:** Diğer nesneler aggregate köküne referans verir.

**İlişkili sözcükler:** root entity

### atomicity · noun

**Türkçe:** atomiklik; işlemin bir bütün sayılması

**Bağlam — kaynak s. 205:** Bir transaction içindeki değişikliklerin birlikte kabul edilmesi veya geri alınması özelliğidir.

> **English:** Atomicity prevents a partially committed transaction.
>
> **Türkçe:** Atomiklik, bir transaction işleminin kısmen commit edilmesini önler.

**İlişkili sözcükler:** atomic; atomically

### audit log · noun phrase

**Türkçe:** denetim günlüğü

**Bağlam — kaynak s. 186, 198, 199, 218:** Neyin ne zaman değiştiğini incelemek için tutulan kayıttır.

> **English:** An audit log records changes to the data.
>
> **Türkçe:** Denetim günlüğü, verilerdeki değişiklikleri kaydeder.

**İlişkili sözcükler:** auditing; audit trail

## B

### backward compatible · adjective phrase

**Türkçe:** geriye dönük uyumlu

**Bağlam — kaynak s. 199:** Yeni sürümün önceki istemci veya verilerle çalışmayı sürdürmesidir.

> **English:** A backward-compatible update preserves existing behavior.
>
> **Türkçe:** Geriye dönük uyumlu bir güncelleme, mevcut davranışı korur.

**İlişkili sözcükler:** backward compatibility, compatible; antonym: incompatible; karşılaştırma: breaking change.

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 184, 199, 212, 218:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 194, 195, 197, 200, 202 ve devamı:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### choreography · noun

**Türkçe:** koreografi; olaylarla dağıtık koordinasyon

**Bağlam — kaynak s. 183, 209, 210, 219:** Saga katılımcıları merkezi bir yöneticinin komutları yerine birbirlerinin olaylarına tepki verir.

> **English:** Choreography coordinates services through events.
>
> **Türkçe:** Koreografi, servisleri olaylar aracılığıyla koordine eder.

**İlişkili sözcükler:** choreography-based; compare: orchestration

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 188, 194, 197, 199, 201 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### coupling · noun

**Türkçe:** bağlılık

**Bağlam — kaynak s. 212:** Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

> **English:** Loose coupling supports independent changes.
>
> **Türkçe:** Gevşek bağlılık, bağımsız değişiklikleri destekler.

**İlişkili sözcükler:** coupled; decouple

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 183, 209:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 205:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 183, 184, 186, 187, 188 ve devamı:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### domain model · noun phrase

**Türkçe:** alan modeli

**Bağlam — kaynak s. 185, 198:** İş kurallarını ve alan kavramlarını nesneler ve ilişkilerle temsil eder.

> **English:** The domain model contains business rules.
>
> **Türkçe:** Alan modeli, iş kurallarını içerir.

**İlişkili sözcükler:** domain-driven design

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 184, 185, 199, 200, 210 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 207:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 188, 203, 204:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 183, 184, 186, 187, 188 ve devamı:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

### event store · noun phrase

**Türkçe:** olay deposu

**Bağlam — kaynak s. 183, 184, 186, 187, 191 ve devamı:** Aggregate olaylarını sıralı geçmiş olarak kalıcı biçimde saklayan altyapıdır.

> **English:** The event store preserves the event sequence.
>
> **Türkçe:** Olay deposu, olay sırasını korur.

**İlişkili sözcükler:** event stream; persistence

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 186, 200, 202:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

## I

### idempotent · adjective

**Türkçe:** aynı işlem yinelendiğinde ek etki üretmeyen

**Bağlam — kaynak s. 197, 200, 210, 213:** Aynı mesajın tekrar işlenmesi, iş etkisini çoğaltmaz.

> **English:** An idempotent handler tolerates duplicate messages.
>
> **Türkçe:** Idempotent bir işleyici, yinelenen mesajları tolere eder.

**İlişkili sözcükler:** idempotency; idempotence

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 183, 186, 193, 209:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 205, 217:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

## O

### optimistic locking · noun phrase

**Türkçe:** iyimser kilitleme

**Bağlam — kaynak s. 193, 204:** Çakışma yok varsayımıyla çalışır; yazma anında sürümü kontrol eder.

> **English:** Optimistic locking detects conflicting updates.
>
> **Türkçe:** İyimser kilitleme, çakışan güncellemeleri saptar.

**İlişkili sözcükler:** version; concurrency control

### orchestration · noun

**Türkçe:** orkestrasyon; merkezi koordinasyon

**Bağlam — kaynak s. 209, 210, 211, 212, 213:** Saga adımlarını merkezi bir orchestrator yönlendirir.

> **English:** Orchestration makes the sequence of steps explicit.
>
> **Türkçe:** Orkestrasyon, adımların sırasını açıkça belirler.

**İlişkili sözcükler:** orchestrator; orchestrate

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 183, 184, 196:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### persistence · noun

**Türkçe:** kalıcı saklama

**Bağlam — kaynak s. 184, 185, 186, 193:** Nesne veya verinin süreç sona erdikten sonra da tutulmasıdır.

> **English:** Persistence stores the aggregate's state.
>
> **Türkçe:** Kalıcı saklama, aggregate'ın durumunu kaydeder.

**İlişkili sözcükler:** persist; persistent

### polling · noun

**Türkçe:** düzenli aralıklarla sorgulama

**Bağlam — kaynak s. 194, 205:** Yeni veri veya iş olup olmadığını tekrar tekrar denetleme tekniğidir.

> **English:** Polling checks the table for new messages.
>
> **Türkçe:** Polling, tabloda yeni mesaj olup olmadığını denetler.

**İlişkili sözcükler:** poll; poller

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 183, 184, 194, 195, 200 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### refactor · verb

**Türkçe:** davranışı koruyarak yapıyı değiştirmek

**Bağlam — kaynak s. 189, 190:** Kodun dışarıdan görülen davranışını koruyarak iç tasarımını iyileştirmektir.

> **English:** We refactor the module before extracting a service.
>
> **Türkçe:** Bir servis çıkarmadan önce modülün yapısını düzenleriz.

**İlişkili sözcükler:** refactoring; restructure

### replay · verb / noun

**Türkçe:** yeniden yürütmek; yeniden yürütme

**Bağlam — kaynak s. 184, 187, 188, 218:** Olay geçmişini sırayla uygulayıp aggregate durumunu yeniden üretmektir.

> **English:** Replay the events to rebuild the aggregate.
>
> **Türkçe:** Aggregate'ı yeniden oluşturmak için olayları sırayla yürütün.

**İlişkili sözcükler:** playback; rebuild

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 188, 194, 199, 203, 204 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 183, 184, 197, 209, 210 ve devamı:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 202:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### serialization · noun

**Türkçe:** serileştirme

**Bağlam — kaynak s. 196:** Bir nesneyi iletilebilir veya saklanabilir bir veri biçimine dönüştürür.

> **English:** Serialization converts an object into a message payload.
>
> **Türkçe:** Serileştirme, bir nesneyi mesaj içeriğine dönüştürür.

**İlişkili sözcükler:** serialize; deserialize

### silver bullet · idiomatic noun phrase

**Türkçe:** bütün sorunları çözeceği sanılan sihirli çözüm

**Bağlam — kaynak s. 200, 218:** Microservice mimarisinin her uygulama için kusursuz çözüm olmadığını vurgulayan benzetme.

> **English:** No architecture is a silver bullet.
>
> **Türkçe:** Hiçbir mimari, bütün sorunları çözen sihirli bir çözüm değildir.

**İlişkili sözcükler:** synonym: magic solution, panacea; kalıp: no silver bullet.

### snapshot · noun

**Türkçe:** belirli bir andaki durumun kopyası

**Bağlam — kaynak s. 195, 196, 200, 201, 203 ve devamı:** Geçmiş olayların hepsini tekrar okumadan yeniden yüklemeyi hızlandırabilir.

> **English:** The snapshot reduces the number of events to replay.
>
> **Türkçe:** Snapshot, yeniden yürütülecek olay sayısını azaltır.

**İlişkili sözcükler:** snapshotting; restore

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 183, 199, 202, 210, 211 ve devamı:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

## T

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 186, 193, 194, 195, 197 ve devamı:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transition · noun / verb

**Türkçe:** geçiş; bir durumdan diğerine geçmek

**Bağlam — kaynak s. 188, 195:** Bağlama göre sistemin, nesnenin veya iş akışının bir durumdan başka bir duruma geçmesini anlatır.

> **English:** The order makes a transition from pending to approved.
>
> **Türkçe:** Sipariş, bekleme durumundan onaylanmış duruma geçer.

**İlişkili sözcükler:** state transition; transition to; transitional

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 183:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

<!-- page-break -->

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** yarar; yarar sağlamak

**3.** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**4.** durumu olay geçmişiyle saklama

**5.** iyimser kilitleme

**6.** davranışı koruyarak yapıyı değiştirmek

**7.** bütün sorunları çözeceği sanılan sihirli çözüm

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. benefit** — Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

**3. deploy** — Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

**4. event sourcing** — Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

**5. optimistic locking** — Çakışma yok varsayımıyla çalışır; yazma anında sürümü kontrol eder.

**6. refactor** — Kodun dışarıdan görülen davranışını koruyarak iç tasarımını iyileştirmektir.

**7. silver bullet** — Microservice mimarisinin her uygulama için kusursuz çözüm olmadığını vurgulayan benzetme.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
