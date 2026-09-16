# Ünite 13 · Refactoring to microservices — Vocabulary

**Amaç:** Bu ünitenin 428–471. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 438:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### adopt · verb

**Türkçe:** benimsemek, kullanmaya başlamak

**Bağlam — kaynak s. 428, 430, 434:** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

> **English:** The team plans to adopt continuous delivery.
>
> **Türkçe:** Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.

**İlişkili sözcükler:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 439:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### anti-corruption layer · noun phrase

**Türkçe:** uyumsuz modelleri birbirinden koruyan çeviri katmanı

**Bağlam — kaynak s. 446, 447, 448, 470:** Eski modelin kavramlarının yeni modele doğrudan yayılmasını engeller.

> **English:** The anti-corruption layer translates between the models.
>
> **Türkçe:** Anti-corruption layer, modeller arasında çeviri yapar.

**İlişkili sözcükler:** ACL; translation layer

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 435, 450, 465:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

### authentication · noun

**Türkçe:** kimlik doğrulama

**Bağlam — kaynak s. 453:** İsteği yapanın kim olduğunu doğrulamadır.

> **English:** Authentication establishes the user's identity.
>
> **Türkçe:** Kimlik doğrulama, kullanıcının kimliğini belirler.

**İlişkili sözcükler:** authenticate; authenticated

### authorization · noun

**Türkçe:** yetkilendirme

**Bağlam — kaynak s. 453, 454, 455:** Bir kimliğin veya istemcinin belirli bir kaynak üzerinde hangi işlemleri yapmaya yetkili olduğunu belirleme ve denetleme sürecidir.

> **English:** Authorization controls access to an operation.
>
> **Türkçe:** Yetkilendirme, bir işleme erişimi denetler.

**İlişkili sözcükler:** authorize; authorized

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 445, 460, 463, 464, 465 ve devamı:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 428, 429, 432, 437, 438 ve devamı:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### bounded context · noun phrase

**Türkçe:** sınırlı bağlam

**Bağlam — kaynak s. 459:** DDD modelindeki terimlerin tek ve tutarlı anlam taşıdığı sınırdır.

> **English:** A bounded context has its own domain model.
>
> **Türkçe:** Bir bounded context, kendi alan modeline sahiptir.

**İlişkili sözcükler:** boundary; domain model

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 436, 449:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

### business capability · noun phrase

**Türkçe:** iş yetkinliği; işletmenin yapabildiği iş

**Bağlam — kaynak s. 437:** İşletmenin sipariş yönetimi gibi gerçekleştirebildiği bir iş yetkinliğidir.

> **English:** Order management is a business capability.
>
> **Türkçe:** Sipariş yönetimi bir iş yetkinliğidir.

**İlişkili sözcükler:** capable, capability; genel synonym: ability. Buradaki capability, tek bir teknik metot değildir.

## C

### code base · noun phrase

**Türkçe:** kod tabanı

**Bağlam — kaynak s. 430, 434, 437, 440, 446 ve devamı:** Bir uygulama veya servisin üzerinde çalışılan kaynak kod bütünü.

> **English:** Several teams modify the same code base.
>
> **Türkçe:** Birden fazla ekip aynı kod tabanını değiştiriyor.

**İlişkili sözcükler:** yaygın yazım: codebase; ilişkili: source code, repository. Repository kodun tutulduğu yerdir.

### compensating transaction · noun phrase

**Türkçe:** telafi işlemi

**Bağlam — kaynak s. 449, 450, 451, 452:** Tamamlanmış bir yerel transaction'ın iş etkisini yeni bir işlemle telafi eder.

> **English:** A compensating transaction releases the reservation.
>
> **Türkçe:** Bir telafi işlemi, rezervasyonu serbest bırakır.

**İlişkili sözcükler:** compensate; compensation

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 445, 446, 450, 451, 452 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### coupling · noun

**Türkçe:** bağlılık

**Bağlam — kaynak s. 465:** Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

> **English:** Loose coupling supports independent changes.
>
> **Türkçe:** Gevşek bağlılık, bağımsız değişiklikleri destekler.

**İlişkili sözcükler:** coupled; decouple

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 432, 434, 443, 444, 446 ve devamı:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 428, 432, 436, 437, 459 ve devamı:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 434, 443, 444, 446, 448 ve devamı:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### domain model · noun phrase

**Türkçe:** alan modeli

**Bağlam — kaynak s. 437, 438, 439, 440, 446 ve devamı:** İş kurallarını ve alan kavramlarını nesneler ve ilişkilerle temsil eder.

> **English:** The domain model contains business rules.
>
> **Türkçe:** Alan modeli, iş kurallarını içerir.

**İlişkili sözcükler:** domain-driven design

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 428, 442, 445, 446, 449 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 436, 444, 467:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 437, 457, 458:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 440, 441, 446, 448, 450 ve devamı:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 448:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

## F

### fault isolation · noun phrase

**Türkçe:** arıza yalıtımı

**Bağlam — kaynak s. 429:** Bir bileşendeki hatanın diğer bileşenlere yayılmasını sınırlamadır.

> **English:** Fault isolation limits the impact of a failing component.
>
> **Türkçe:** Arıza yalıtımı, arızalanan bir bileşenin etkisini sınırlar.

**İlişkili sözcükler:** fault, faulty, isolate, isolation; ilişkili: containment. Servislerin ayrılması bütün arıza yayılımını kendiliğinden engellemez.

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 428, 429, 430, 432, 433 ve devamı:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 428:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

### force · verb

**Türkçe:** zorlamak, mecbur bırakmak

**Bağlam — kaynak s. 442:** Bu ünitede force + object + to + verb yapısıyla birini veya sistemi belirli bir davranışa zorlamak anlamındadır.

> **English:** An incompatible API change can force clients to upgrade.
>
> **Türkçe:** Uyumsuz bir API değişikliği, istemcileri sürüm yükseltmeye zorlayabilir.

**İlişkili sözcükler:** force someone to do something; forced; synonym: compel. İsim olarak forces, örüntü tasarımında çözümü etkileyen etkenlerdir.

## I

### inbound · adjective

**Türkçe:** içe gelen

**Bağlam — kaynak s. 437, 470:** İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

> **English:** An inbound adapter invokes the business logic.
>
> **Türkçe:** Gelen yönlü bir adapter, iş mantığını çağırır.

**İlişkili sözcükler:** antonym: outbound

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 434, 437:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

### isolation · noun

**Türkçe:** yalıtım

**Bağlam — kaynak s. 429, 449, 450:** Bağlama göre arızaların yayılmasını sınırlama veya eşzamanlı transaction işlemlerinin ara etkilerini ayırma anlamındadır. Servis ayırmak, saga işlemlerine kendiliğinden transaction yalıtımı kazandırmaz.

> **English:** Sagas do not provide transaction isolation automatically.
>
> **Türkçe:** Saga'lar transaction yalıtımını kendiliğinden sağlamaz.

**İlişkili sözcükler:** isolate; isolated

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 458:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

### loosely coupled · adjective phrase

**Türkçe:** gevşek bağlı

**Bağlam — kaynak s. 434:** Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

> **English:** Loosely coupled teams coordinate less frequently.
>
> **Türkçe:** Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.

**İlişkili sözcükler:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 429, 430, 432, 434, 443 ve devamı:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### monolith · noun

**Türkçe:** monolit; tek dağıtılabilir bütün

**Bağlam — kaynak s. 428, 429, 430, 431, 432 ve devamı:** Kaynakta tek WAR dosyası gibi tek birim olarak paketlenip dağıtılan uygulama.

> **English:** The monolith is packaged as a single WAR file.
>
> **Türkçe:** Monolit, tek bir WAR dosyası olarak paketlenir.

**İlişkili sözcükler:** monolithic; karşılaştırma: independently deployable services. Monolith tek başına kötü tasarım demek değildir.

## O

### observability · noun

**Türkçe:** gözlemlenebilirlik

**Bağlam — kaynak s. 433:** Sistemin iç durumunu log, metric ve trace gibi dış çıktılardan anlayabilmektir.

> **English:** Logs and traces support observability.
>
> **Türkçe:** Log'lar ve iz kayıtları, gözlemlenebilirliği destekler.

**İlişkili sözcükler:** observe, observable, observation; ilişkili: metrics, tracing, logging.

### outbound · adjective

**Türkçe:** dışa giden

**Bağlam — kaynak s. 437, 470:** İş mantığından dış sistemlere doğru yapılan çağrıyı anlatır.

> **English:** An outbound adapter accesses the database.
>
> **Türkçe:** Giden yönlü bir adapter, veritabanına erişir.

**İlişkili sözcükler:** antonym: inbound

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 446:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 431, 432, 447:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### polling · noun

**Türkçe:** düzenli aralıklarla sorgulama

**Bağlam — kaynak s. 449:** Yeni veri veya iş olup olmadığını tekrar tekrar denetleme tekniğidir.

> **English:** Polling checks the table for new messages.
>
> **Türkçe:** Polling, tabloda yeni mesaj olup olmadığını denetler.

**İlişkili sözcükler:** poll; poller

### provider · noun

**Türkçe:** sağlayıcı

**Bağlam — kaynak s. 445, 446:** Bir API, mesaj veya hizmet sunan taraftır.

> **English:** The provider must satisfy its API contract.
>
> **Türkçe:** Sağlayıcı, API sözleşmesini karşılamalıdır.

**İlişkili sözcükler:** provide; consumer

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 444, 445, 446, 456, 457 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### refactor · verb

**Türkçe:** davranışı koruyarak yapıyı değiştirmek

**Bağlam — kaynak s. 428, 429, 430, 431, 432 ve devamı:** Kodun dışarıdan görülen davranışını koruyarak iç tasarımını iyileştirmektir.

> **English:** We refactor the module before extracting a service.
>
> **Türkçe:** Bir servis çıkarmadan önce modülün yapısını düzenleriz.

**İlişkili sözcükler:** refactoring; restructure

### reliability · noun

**Türkçe:** güvenilirlik

**Bağlam — kaynak s. 442:** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.

> **English:** Frequent failures reduce the reliability of the application.
>
> **Türkçe:** Sık arızalar, uygulamanın güvenilirliğini azaltır.

**İlişkili sözcükler:** reliable, reliably, unreliable; karşılaştırma: availability.

### repository · noun

**Türkçe:** veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 444, 445:** Domain nesnelerinin bulunması ve saklanması için arayüz sağlar.

> **English:** The repository loads an aggregate.
>
> **Türkçe:** Repository, bir aggregate yükler.

**İlişkili sözcükler:** retrieve; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 434, 443, 444, 445, 447 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 455, 459:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 432, 443, 444, 446, 449 ve devamı:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 430, 442:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### semantic lock · noun phrase

**Türkçe:** anlamsal kilit

**Bağlam — kaynak s. 450, 451:** İş durumuyla, örneğin PENDING ile, eşzamanlı işlemleri kontrollü biçimde sınırlar.

> **English:** The pending status acts as a semantic lock.
>
> **Türkçe:** Bekleme durumu, anlamsal bir kilit işlevi görür.

**İlişkili sözcükler:** pending state; countermeasure

### service discovery · noun phrase

**Türkçe:** servis keşfi

**Bağlam — kaynak s. 433:** Çağrılabilecek servis örneklerinin ağ konumlarını bulma mekanizmasıdır.

> **English:** Service discovery locates available instances.
>
> **Türkçe:** Servis keşfi, kullanılabilir örneklerin konumunu bulur.

**İlişkili sözcükler:** discover; registry

### span · verb

**Türkçe:** birden fazla alanı kapsamak, yayılmak

**Bağlam — kaynak s. 439:** Fiil olarak birden fazla servis, alan veya zaman aralığına yayılmayı anlatır.

> **English:** The transaction spans several services.
>
> **Türkçe:** Transaction, birkaç servisi kapsar.

**İlişkili sözcükler:** spans, spanning; synonym: extend across, cover.

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 448, 450, 452, 453:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 435, 445:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### take into account · verb phrase

**Türkçe:** hesaba katmak, dikkate almak

**Bağlam — kaynak s. 442:** Bir tasarım veya uygulama kararında ilgili gereksinimleri, sınırlamaları ve başka etkenleri hesaba katmaktır.

> **English:** The migration plan must take team structure into account.
>
> **Türkçe:** Geçiş planı, ekip yapısını hesaba katmalıdır.

**İlişkili sözcükler:** synonym: consider, allow for; karşıt: overlook, disregard.

### technology stack · noun phrase

**Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü

**Bağlam — kaynak s. 429, 430, 432, 459:** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.

> **English:** A service may use a different technology stack.
>
> **Türkçe:** Bir servis farklı bir teknoloji yığını kullanabilir.

**İlişkili sözcükler:** tech stack; ilişkili: framework, language, infrastructure.

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 443, 444, 449, 450, 451 ve devamı:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transition · noun / verb

**Türkçe:** geçiş, değişime uyum süreci; geçiş yapmak

**Bağlam — kaynak s. 441:** Mimari değişimin yanında insanların yeni çalışma biçimine uyum sağlaması.

> **English:** People need support during the transition.
>
> **Türkçe:** İnsanlar, geçiş sürecinde desteğe ihtiyaç duyar.

**İlişkili sözcükler:** transitional; ilişkili: change, adaptation. Kaynak, dış değişiklik ile ona verilen duygusal yanıtı ayırır.

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 446, 462:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** yarar; yarar sağlamak

**3.** veri tutarlılığı

**4.** durumu olay geçmişiyle saklama

**5.** gecikme

**6.** düzenli aralıklarla sorgulama

**7.** yerel transaction adımlarından oluşan iş akışı

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. benefit** — Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

**3. data consistency** — Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

**4. event sourcing** — Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

**5. latency** — Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

**6. polling** — Yeni veri veya iş olup olmadığını tekrar tekrar denetleme tekniğidir.

**7. saga** — Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
