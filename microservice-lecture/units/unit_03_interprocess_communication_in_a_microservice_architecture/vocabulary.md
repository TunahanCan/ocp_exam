# Ünite 03 · Interprocess communication in a microservice architecture — Vocabulary

**Amaç:** Bu ünitenin 65–109. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 80, 81, 83, 84, 86 ve devamı:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### adopt · verb

**Türkçe:** benimsemek, kullanmaya başlamak

**Bağlam — kaynak s. 89, 101:** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

> **English:** The team plans to adopt continuous delivery.
>
> **Türkçe:** Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.

**İlişkili sözcükler:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 80, 102:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 65, 66, 67, 68, 85 ve devamı:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

### atomicity · noun

**Türkçe:** atomiklik; işlemin bir bütün sayılması

**Bağlam — kaynak s. 97:** Bir transaction içindeki değişikliklerin birlikte kabul edilmesi veya geri alınması özelliğidir.

> **English:** Atomicity prevents a partially committed transaction.
>
> **Türkçe:** Atomiklik, bir transaction işleminin kısmen commit edilmesini önler.

**İlişkili sözcükler:** atomic; atomically

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 66, 67, 68, 72, 75 ve devamı:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### backward compatible · adjective phrase

**Türkçe:** geriye dönük uyumlu

**Bağlam — kaynak s. 70, 71, 76, 108:** Yeni sürümün önceki istemci veya verilerle çalışmayı sürdürmesidir.

> **English:** A backward-compatible update preserves existing behavior.
>
> **Türkçe:** Geriye dönük uyumlu bir güncelleme, mevcut davranışı korur.

**İlişkili sözcükler:** backward compatibility, compatible; antonym: incompatible; karşılaştırma: breaking change.

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 65, 74, 75, 77, 83 ve devamı:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 68, 75, 85, 90, 91 ve devamı:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### circuit breaker · noun phrase

**Türkçe:** devre kesici

**Bağlam — kaynak s. 65, 77, 78, 79, 108:** Tekrarlanan başarısızlıklardan sonra çağrıları geçici olarak durduran korumadır.

> **English:** The circuit breaker rejects calls while it is open.
>
> **Türkçe:** Devre kesici, açık durumdayken çağrıları reddeder.

**İlişkili sözcükler:** open; closed; half-open

### constraint · noun

**Türkçe:** kısıt, sınırlayıcı koşul

**Bağlam — kaynak s. 73:** Bir tasarım veya işlemin uyması gereken kısıttır.

> **English:** Past decisions impose constraints on the new design.
>
> **Türkçe:** Geçmiş kararlar, yeni tasarıma kısıtlar getirir.

**İlişkili sözcükler:** constrain, constrained; synonym: restriction, limitation.

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 66, 71, 72, 74, 75 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### correlation id · noun phrase

**Türkçe:** ilişkilendirme kimliği

**Bağlam — kaynak s. 88, 89:** Dağıtık bir isteğe ait mesaj ve kayıtları birbirine bağlar.

> **English:** The correlation ID links the reply to the request.
>
> **Türkçe:** İlişkilendirme kimliği, yanıtı istekle eşleştirir.

**İlişkili sözcükler:** correlate; correlation

### coupling · noun

**Türkçe:** bağlılık

**Bağlam — kaynak s. 93:** Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

> **English:** Loose coupling supports independent changes.
>
> **Türkçe:** Gevşek bağlılık, bağımsız değişiklikleri destekler.

**İlişkili sözcükler:** coupled; decouple

## D

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 68, 83, 85:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed system · noun phrase

**Türkçe:** dağıtık sistem

**Bağlam — kaynak s. 70, 77:** Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.

> **English:** A distributed system must handle partial failures.
>
> **Türkçe:** Dağıtık bir sistem, kısmi arızaları ele almalıdır.

**İlişkili sözcükler:** distribute, distribution; ilişkili: remote call, interprocess communication.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 86, 89, 97, 100, 101 ve devamı:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 71, 75, 76, 77, 83 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

### durability · noun

**Türkçe:** kalıcılık

**Bağlam — kaynak s. 92:** Commit edilmiş değişikliklerin daha sonra kaybolmaması özelliğidir.

> **English:** Durability protects committed data.
>
> **Türkçe:** Kalıcılık, commit edilmiş veriyi korur.

**İlişkili sözcükler:** durable; persist

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 72, 73, 86:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 73, 74, 75, 79, 80 ve devamı:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 98:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 101:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 69, 87, 91, 101:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 92:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

### force · verb

**Türkçe:** zorlamak, mecbur bırakmak

**Bağlam — kaynak s. 69, 70, 72, 76:** Bu ünitede force + object + to + verb yapısıyla birini veya sistemi belirli bir davranışa zorlamak anlamındadır.

> **English:** An incompatible API change can force clients to upgrade.
>
> **Türkçe:** Uyumsuz bir API değişikliği, istemcileri sürüm yükseltmeye zorlayabilir.

**İlişkili sözcükler:** force someone to do something; forced; synonym: compel. İsim olarak forces, örüntü tasarımında çözümü etkileyen etkenlerdir.

## H

### health check · noun phrase

**Türkçe:** sağlık kontrolü

**Bağlam — kaynak s. 81:** Bir servis örneğinin çalışıp çalışmadığını veya trafik alabilecek durumda olup olmadığını sınar.

> **English:** A health check reports the service's condition.
>
> **Türkçe:** Sağlık kontrolü, servisin durumunu bildirir.

**İlişkili sözcükler:** liveness; readiness

## I

### idempotent · adjective

**Türkçe:** aynı işlem yinelendiğinde ek etki üretmeyen

**Bağlam — kaynak s. 75, 95, 96:** Aynı mesajın tekrar işlenmesi, iş etkisini çoğaltmaz.

> **English:** An idempotent handler tolerates duplicate messages.
>
> **Türkçe:** Idempotent bir işleyici, yinelenen mesajları tolere eder.

**İlişkili sözcükler:** idempotency; idempotence

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 65, 66, 93, 108:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 73, 74, 91, 92, 108:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

### loosely coupled · adjective phrase

**Türkçe:** gevşek bağlı

**Bağlam — kaynak s. 66, 68, 106:** Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

> **English:** Loosely coupled teams coordinate less frequently.
>
> **Türkçe:** Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.

**İlişkili sözcükler:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 91, 105:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 68, 69, 86, 87, 89 ve devamı:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

## O

### outage · noun

**Türkçe:** hizmet kesintisi

**Bağlam — kaynak s. 77:** Uygulamanın production ortamında hizmet veremediği olay veya süre.

> **English:** The production outage affected every customer.
>
> **Türkçe:** Production ortamındaki hizmet kesintisi bütün müşterileri etkiledi.

**İlişkili sözcükler:** service interruption, downtime; karşılaştırma: recovery, restoration.

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 71:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 65, 72, 76, 77, 78 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### persistence · noun

**Türkçe:** kalıcı saklama

**Bağlam — kaynak s. 92:** Nesne veya verinin süreç sona erdikten sonra da tutulmasıdır.

> **English:** Persistence stores the aggregate's state.
>
> **Türkçe:** Kalıcı saklama, aggregate'ın durumunu kaydeder.

**İlişkili sözcükler:** persist; persistent

### polling · noun

**Türkçe:** düzenli aralıklarla sorgulama

**Bağlam — kaynak s. 65, 98, 100, 109:** Yeni veri veya iş olup olmadığını tekrar tekrar denetleme tekniğidir.

> **English:** Polling checks the table for new messages.
>
> **Türkçe:** Polling, tabloda yeni mesaj olup olmadığını denetler.

**İlişkili sözcükler:** poll; poller

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 74, 75, 79, 81, 82 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### recover · verb

**Türkçe:** toparlanmak, yeniden çalışır duruma gelmek

**Bağlam — kaynak s. 78, 79:** Production sorunundan sonra hizmetin yeniden işler duruma gelmesi.

> **English:** The team works to recover from the outage.
>
> **Türkçe:** Ekip, hizmet kesintisinin ardından sistemi yeniden çalışır duruma getirmek için uğraşır.

**İlişkili sözcükler:** recovery, recoverable; kalıp: recover from; ilişkili: restore service.

### registry · noun

**Türkçe:** kayıt servisi veya dizini

**Bağlam — kaynak s. 81, 82, 83, 84, 85:** Çalışan servis örneklerinin adresleri gibi bilgileri tutar.

> **English:** The registry stores the locations of service instances.
>
> **Türkçe:** Kayıt servisi, servis örneklerinin konumlarını saklar.

**İlişkili sözcükler:** register; registration

### reliability · noun

**Türkçe:** güvenilirlik

**Bağlam — kaynak s. 78, 94:** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.

> **English:** Frequent failures reduce the reliability of the application.
>
> **Türkçe:** Sık arızalar, uygulamanın güvenilirliğini azaltır.

**İlişkili sözcükler:** reliable, reliably, unreliable; karşılaştırma: availability.

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 74, 75, 83, 104, 109:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 83, 84:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 101, 106:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 73, 92:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### serialization · noun

**Türkçe:** serileştirme

**Bağlam — kaynak s. 71:** Bir nesneyi iletilebilir veya saklanabilir bir veri biçimine dönüştürür.

> **English:** Serialization converts an object into a message payload.
>
> **Türkçe:** Serileştirme, bir nesneyi mesaj içeriğine dönüştürür.

**İlişkili sözcükler:** serialize; deserialize

### service discovery · noun phrase

**Türkçe:** servis keşfi

**Bağlam — kaynak s. 66, 72, 76, 80, 81 ve devamı:** Çağrılabilecek servis örneklerinin ağ konumlarını bulma mekanizmasıdır.

> **English:** Service discovery locates available instances.
>
> **Türkçe:** Servis keşfi, kullanılabilir örneklerin konumunu bulur.

**İlişkili sözcükler:** discover; registry

### silver bullet · idiomatic noun phrase

**Türkçe:** bütün sorunları çözeceği sanılan sihirli çözüm

**Bağlam — kaynak s. 66:** Microservice mimarisinin her uygulama için kusursuz çözüm olmadığını vurgulayan benzetme.

> **English:** No architecture is a silver bullet.
>
> **Türkçe:** Hiçbir mimari, bütün sorunları çözen sihirli bir çözüm değildir.

**İlişkili sözcükler:** synonym: magic solution, panacea; kalıp: no silver bullet.

### span · verb

**Türkçe:** birden fazla alanı kapsamak, yayılmak

**Bağlam — kaynak s. 97:** Fiil olarak birden fazla servis, alan veya zaman aralığına yayılmayı anlatır.

> **English:** The transaction spans several services.
>
> **Türkçe:** Transaction, birkaç servisi kapsar.

**İlişkili sözcükler:** spans, spanning; synonym: extend across, cover.

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 69, 76, 77, 89, 97 ve devamı:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### stub · noun

**Türkçe:** önceden belirlenmiş yanıt veren test nesnesi

**Bağlam — kaynak s. 74, 76:** Bağımlılığın davranışını test için kontrollü yanıtlarla taklit eder.

> **English:** The stub returns a fixed response.
>
> **Türkçe:** Stub, önceden belirlenmiş bir yanıt döndürür.

**İlişkili sözcükler:** stubbing; compare: mock

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 66, 67, 68, 72, 77 ve devamı:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### throughput · noun

**Türkçe:** birim zamanda işlenen iş miktarı

**Bağlam — kaynak s. 94:** Sistemin belirli sürede tamamladığı istek veya mesaj sayısını anlatır.

> **English:** Throughput measures completed requests per second.
>
> **Türkçe:** Throughput, saniyede tamamlanan istekleri ölçer.

**İlişkili sözcükler:** processing rate; compare: latency

### trade-off · noun

**Türkçe:** bir kazanım karşılığında başka bir alanda verilen ödün

**Bağlam — kaynak s. 65, 66, 90, 92, 103 ve devamı:** Mimari seçimin yarar ve maliyetlerini birlikte değerlendirmeyi gerektiren denge.

> **English:** The design involves a trade-off between simplicity and flexibility.
>
> **Türkçe:** Tasarım, sadelik ile esneklik arasında bir ödünleşim içerir.

**İlişkili sözcükler:** trade off (fiil); yakın anlamlı: compromise; kalıp: a trade-off between A and B.

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 65, 66, 85, 96, 97 ve devamı:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transactional outbox · noun phrase

**Türkçe:** mesajı aynı transaction içinde çıkış tablosuna yazma

**Bağlam — kaynak s. 65, 97, 98, 109:** İş verisi ile gönderilecek mesaj aynı veritabanı transaction'ında saklanır.

> **English:** The transactional outbox prevents a lost event between two writes.
>
> **Türkçe:** Transactional outbox, iki yazma işlemi arasında bir olayın kaybolmasını önler.

**İlişkili sözcükler:** outbox; message relay

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** mesaj aracısı

**3.** alan olayı

**4.** uygunluk; uymak; uygun

**5.** mesaj kanalı

**6.** kayıt servisi veya dizini

**7.** bütün sorunları çözeceği sanılan sihirli çözüm

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. broker** — Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

**3. domain event** — İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

**4. fit** — Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

**5. message channel** — Mesajların gönderildiği mantıksal iletişim yoludur.

**6. registry** — Çalışan servis örneklerinin adresleri gibi bilgileri tutar.

**7. silver bullet** — Microservice mimarisinin her uygulama için kusursuz çözüm olmadığını vurgulayan benzetme.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
