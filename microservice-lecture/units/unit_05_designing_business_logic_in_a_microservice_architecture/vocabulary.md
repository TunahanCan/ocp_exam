# Ünite 05 · Designing business logic in a microservice architecture — Vocabulary

**Amaç:** Bu ünitenin 146–182. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 146, 147, 151, 154, 175:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### adopt · verb

**Türkçe:** benimsemek, kullanmaya başlamak

**Bağlam — kaynak s. 151:** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

> **English:** The team plans to adopt continuous delivery.
>
> **Türkçe:** Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.

**İlişkili sözcükler:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 146, 147, 152, 153, 154 ve devamı:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### aggregate root · noun phrase

**Türkçe:** aggregate kökü

**Bağlam — kaynak s. 155, 156, 164, 165, 171 ve devamı:** Aggregate dışındaki nesnelerin bütünle etkileşim kurduğu, erişimi ve tutarlılık kurallarını yöneten kök entity’dir.

> **English:** Other objects reference the aggregate root.
>
> **Türkçe:** Diğer nesneler aggregate köküne referans verir.

**İlişkili sözcükler:** root entity

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 164, 168, 172, 175:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

### authorization · noun

**Türkçe:** yetkilendirme

**Bağlam — kaynak s. 179:** Bir kimliğin veya istemcinin belirli bir kaynak üzerinde hangi işlemleri yapmaya yetkili olduğunu belirleme ve denetleme sürecidir.

> **English:** Authorization controls access to an operation.
>
> **Türkçe:** Yetkilendirme, bir işleme erişimi denetler.

**İlişkili sözcükler:** authorize; authorized

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 151, 155, 156, 158:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### bounded context · noun phrase

**Türkçe:** sınırlı bağlam

**Bağlam — kaynak s. 151, 169:** DDD modelindeki terimlerin tek ve tutarlı anlam taşıdığı sınırdır.

> **English:** A bounded context has its own domain model.
>
> **Türkçe:** Bir bounded context, kendi alan modeline sahiptir.

**İlişkili sözcükler:** boundary; domain model

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 147, 160, 164, 166, 167:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### choreography · noun

**Türkçe:** koreografi; olaylarla dağıtık koordinasyon

**Bağlam — kaynak s. 160, 182:** Saga katılımcıları merkezi bir yöneticinin komutları yerine birbirlerinin olaylarına tepki verir.

> **English:** Choreography coordinates services through events.
>
> **Türkçe:** Koreografi, servisleri olaylar aracılığıyla koordine eder.

**İlişkili sözcükler:** choreography-based; compare: orchestration

### concurrency · noun

**Türkçe:** eşzamanlılık

**Bağlam — kaynak s. 155:** Birden fazla işlemin zaman bakımından çakışacak biçimde ilerlemesidir.

> **English:** Concurrency can expose inconsistent intermediate states.
>
> **Türkçe:** Eşzamanlılık, tutarsız ara durumların görülmesine yol açabilir.

**İlişkili sözcükler:** concurrent; concurrently

### constraint · noun

**Türkçe:** kısıt, sınırlayıcı koşul

**Bağlam — kaynak s. 146, 147, 157, 181:** Bir tasarım veya işlemin uyması gereken kısıttır.

> **English:** Past decisions impose constraints on the new design.
>
> **Türkçe:** Geçmiş kararlar, yeni tasarıma kısıtlar getirir.

**İlişkili sözcükler:** constrain, constrained; synonym: restriction, limitation.

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 152, 153, 154, 156, 158 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 146, 159, 160, 181:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### decompose · verb

**Türkçe:** bileşenlere ayırmak

**Bağlam — kaynak s. 154:** Uygulamayı sorumlulukları belirli modül veya servislere bölmektir.

> **English:** We decompose the application by business capability.
>
> **Türkçe:** Uygulamayı iş yetkinliğine göre ayırırız.

**İlişkili sözcükler:** decomposition; compose

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 146, 147, 160, 161, 162 ve devamı:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### domain model · noun phrase

**Türkçe:** alan modeli

**Bağlam — kaynak s. 146, 147, 150, 151, 152 ve devamı:** İş kurallarını ve alan kavramlarını nesneler ve ilişkilerle temsil eder.

> **English:** The domain model contains business rules.
>
> **Türkçe:** Alan modeli, iş kurallarını içerir.

**İlişkili sözcükler:** domain-driven design

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 149, 158, 161, 162, 164 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 152:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 151, 152, 154, 156, 170:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 182:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

## F

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 147, 153:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

## I

### inbound · adjective

**Türkçe:** içe gelen

**Bağlam — kaynak s. 147, 159, 168, 171, 173 ve devamı:** İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

> **English:** An inbound adapter invokes the business logic.
>
> **Türkçe:** Gelen yönlü bir adapter, iş mantığını çağırır.

**İlişkili sözcükler:** antonym: outbound

### invariant · noun

**Türkçe:** değişmez iş kuralı

**Bağlam — kaynak s. 153, 155, 156:** Bir aggregate'ın geçerli durumunda her zaman sağlanması gereken kısıttır.

> **English:** The invariant requires a nonnegative total.
>
> **Türkçe:** Değişmez kural, toplamın negatif olmamasını gerektirir.

**İlişkili sözcükler:** constraint; consistency rule

## L

### loosely coupled · adjective phrase

**Türkçe:** gevşek bağlı

**Bağlam — kaynak s. 156:** Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

> **English:** Loosely coupled teams coordinate less frequently.
>
> **Türkçe:** Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.

**İlişkili sözcükler:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 146, 147, 150, 151, 157 ve devamı:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 147, 174:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

## O

### optimistic locking · noun phrase

**Türkçe:** iyimser kilitleme

**Bağlam — kaynak s. 176:** Çakışma yok varsayımıyla çalışır; yazma anında sürümü kontrol eder.

> **English:** Optimistic locking detects conflicting updates.
>
> **Türkçe:** İyimser kilitleme, çakışan güncellemeleri saptar.

**İlişkili sözcükler:** version; concurrency control

### outbound · adjective

**Türkçe:** dışa giden

**Bağlam — kaynak s. 147, 159, 168, 175:** İş mantığından dış sistemlere doğru yapılan çağrıyı anlatır.

> **English:** An outbound adapter accesses the database.
>
> **Türkçe:** Giden yönlü bir adapter, veritabanına erişir.

**İlişkili sözcükler:** antonym: inbound

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 161:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 146, 147, 149, 150, 151 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### persistence · noun

**Türkçe:** kalıcı saklama

**Bağlam — kaynak s. 156, 182:** Nesne veya verinin süreç sona erdikten sonra da tutulmasıdır.

> **English:** Persistence stores the aggregate's state.
>
> **Türkçe:** Kalıcı saklama, aggregate'ın durumunu kaydeder.

**İlişkili sözcükler:** persist; persistent

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 160, 161:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### repository · noun

**Türkçe:** veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 152, 156, 159:** Domain nesnelerinin bulunması ve saklanması için arayüz sağlar.

> **English:** The repository loads an aggregate.
>
> **Türkçe:** Repository, bir aggregate yükler.

**İlişkili sözcükler:** retrieve; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 153, 159, 161, 165, 167 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 146, 157, 159, 160, 168 ve devamı:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 158:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### semantic lock · noun phrase

**Türkçe:** anlamsal kilit

**Bağlam — kaynak s. 176:** İş durumuyla, örneğin PENDING ile, eşzamanlı işlemleri kontrollü biçimde sınırlar.

> **English:** The pending status acts as a semantic lock.
>
> **Türkçe:** Bekleme durumu, anlamsal bir kilit işlevi görür.

**İlişkili sözcükler:** pending state; countermeasure

### span · verb

**Türkçe:** birden fazla alanı kapsamak, yayılmak

**Bağlam — kaynak s. 146, 156, 159:** Fiil olarak birden fazla servis, alan veya zaman aralığına yayılmayı anlatır.

> **English:** The transaction spans several services.
>
> **Türkçe:** Transaction, birkaç servisi kapsar.

**İlişkili sözcükler:** spans, spanning; synonym: extend across, cover.

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 156:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### subdomain · noun

**Türkçe:** alt alan

**Bağlam — kaynak s. 151:** İş alanının kendi sorumluluklarına sahip bir parçasıdır.

> **English:** Order management is a subdomain of the business.
>
> **Türkçe:** Sipariş yönetimi, işletmenin bir alt alanıdır.

**İlişkili sözcükler:** domain; bounded context

## T

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 146, 147, 149, 150, 153 ve devamı:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transition · noun / verb

**Türkçe:** geçiş; bir durumdan diğerine geçmek

**Bağlam — kaynak s. 160, 176:** Bağlama göre sistemin, nesnenin veya iş akışının bir durumdan başka bir duruma geçmesini anlatır.

> **English:** The order makes a transition from pending to approved.
>
> **Türkçe:** Sipariş, bekleme durumundan onaylanmış duruma geçer.

**İlişkili sözcükler:** state transition; transition to; transitional

## V

### value object · noun phrase

**Türkçe:** kimliğinden çok değeriyle tanımlanan nesne

**Bağlam — kaynak s. 151, 152, 154, 161, 175:** Eşitliği ayrı bir kimlikle değil, içerdiği değerlerle belirlenir.

> **English:** Money can be modeled as a value object.
>
> **Türkçe:** Money, bir value object olarak modellenebilir.

**İlişkili sözcükler:** immutable; entity

### viable · adjective

**Türkçe:** uygulanabilir, işleyebilir

**Bağlam — kaynak s. 165:** Verilen koşullarda uygulanabilir ve çalışabilir bir seçeneği niteler.

> **English:** The team must find a viable way to maintain consistency.
>
> **Türkçe:** Ekip, tutarlılığı korumanın uygulanabilir bir yolunu bulmalıdır.

**İlişkili sözcükler:** viability; synonym: feasible, workable; antonym: unviable, impractical.

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 169:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## W

### webhook · noun

**Türkçe:** olay gerçekleştiğinde yapılan HTTP bildirimi

**Bağlam — kaynak s. 160:** Bir sistemin başka sisteme HTTP çağrısıyla haber vermesidir.

> **English:** The webhook notifies another service.
>
> **Türkçe:** Webhook, başka bir servise bildirim gönderir.

**İlişkili sözcükler:** callback; notification

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** yarar; yarar sağlamak

**3.** tüketici

**4.** kapsüllemek

**5.** gevşek bağlı

**6.** örüntü; belirli bağlamda tekrarlanabilir çözüm

**7.** ölçeklenebilirlik

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. benefit** — Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

**3. consumer** — Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

**4. encapsulate** — İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

**5. loosely coupled** — Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

**6. pattern** — Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

**7. scalability** — Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
