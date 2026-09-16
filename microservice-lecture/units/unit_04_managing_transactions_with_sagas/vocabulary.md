# Ünite 04 · Managing transactions with sagas — Vocabulary

**Amaç:** Bu ünitenin 110–145. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 118:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### adopt · verb

**Türkçe:** benimsemek, kullanmaya başlamak

**Bağlam — kaynak s. 111:** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

> **English:** The team plans to adopt continuous delivery.
>
> **Türkçe:** Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.

**İlişkili sözcükler:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 114, 115, 122, 144:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

### atomicity · noun

**Türkçe:** atomiklik; işlemin bir bütün sayılması

**Bağlam — kaynak s. 110, 111, 126:** Bir transaction içindeki değişikliklerin birlikte kabul edilmesi veya geri alınması özelliğidir.

> **English:** Atomicity prevents a partially committed transaction.
>
> **Türkçe:** Atomiklik, bir transaction işleminin kısmen commit edilmesini önler.

**İlişkili sözcükler:** atomic; atomically

### authorization · noun

**Türkçe:** yetkilendirme

**Bağlam — kaynak s. 115, 116, 117, 119, 120 ve devamı:** Bir kimliğin veya istemcinin belirli bir kaynak üzerinde hangi işlemleri yapmaya yetkili olduğunu belirleme ve denetleme sürecidir.

> **English:** Authorization controls access to an operation.
>
> **Türkçe:** Yetkilendirme, bir işleme erişimi denetler.

**İlişkili sözcükler:** authorize; authorized

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 113, 131:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 114, 118, 121, 122, 125 ve devamı:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 112, 115:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### choreography · noun

**Türkçe:** koreografi; olaylarla dağıtık koordinasyon

**Bağlam — kaynak s. 110, 111, 117, 118, 119 ve devamı:** Saga katılımcıları merkezi bir yöneticinin komutları yerine birbirlerinin olaylarına tepki verir.

> **English:** Choreography coordinates services through events.
>
> **Türkçe:** Koreografi, servisleri olaylar aracılığıyla koordine eder.

**İlişkili sözcükler:** choreography-based; compare: orchestration

### compensating transaction · noun phrase

**Türkçe:** telafi işlemi

**Bağlam — kaynak s. 114, 115, 116, 117, 119 ve devamı:** Tamamlanmış bir yerel transaction'ın iş etkisini yeni bir işlemle telafi eder.

> **English:** A compensating transaction releases the reservation.
>
> **Türkçe:** Bir telafi işlemi, rezervasyonu serbest bırakır.

**İlişkili sözcükler:** compensate; compensation

### concurrency · noun

**Türkçe:** eşzamanlılık

**Bağlam — kaynak s. 111, 128, 131, 145:** Birden fazla işlemin zaman bakımından çakışacak biçimde ilerlemesidir.

> **English:** Concurrency can expose inconsistent intermediate states.
>
> **Türkçe:** Eşzamanlılık, tutarsız ara durumların görülmesine yol açabilir.

**İlişkili sözcükler:** concurrent; concurrently

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 112, 115, 116, 117, 119 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### coordination · noun

**Türkçe:** eşgüdüm, koordinasyon

**Bağlam — kaynak s. 114, 116, 117, 118, 125:** Birden fazla ekibin veya servisin değişiklik sırasını ve ortak çalışmasını düzenlemek.

> **English:** This feature requires coordination between three teams.
>
> **Türkçe:** Bu özellik, üç ekip arasında koordinasyon gerektiriyor.

**İlişkili sözcükler:** coordinate, coordinator; synonym: collaboration yakın anlamlıdır, ancak birlikte çalışma yönünü vurgular.

### correlation id · noun phrase

**Türkçe:** ilişkilendirme kimliği

**Bağlam — kaynak s. 120, 121:** Dağıtık bir isteğe ait mesaj ve kayıtları birbirine bağlar.

> **English:** The correlation ID links the reply to the request.
>
> **Türkçe:** İlişkilendirme kimliği, yanıtı istekle eşleştirir.

**İlişkili sözcükler:** correlate; correlation

### coupling · noun

**Türkçe:** bağlılık

**Bağlam — kaynak s. 121, 125:** Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

> **English:** Loose coupling supports independent changes.
>
> **Türkçe:** Gevşek bağlılık, bağımsız değişiklikleri destekler.

**İlişkili sözcükler:** coupled; decouple

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 110, 111, 112, 113, 114:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### deadlock · noun

**Türkçe:** kilitlenme

**Bağlam — kaynak s. 130, 145:** İşlemlerin birbirlerinin tuttuğu kaynakları bekleyerek ilerleyememesidir.

> **English:** A deadlock occurs when transactions wait for one another’s locks.
>
> **Türkçe:** Transaction işlemleri birbirlerinin kilitlerini beklediğinde deadlock oluşur.

**İlişkili sözcükler:** deadlocked; lock

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 134:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 118, 121, 122, 125, 130:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

### durability · noun

**Türkçe:** kalıcılık

**Bağlam — kaynak s. 110, 111, 126:** Commit edilmiş değişikliklerin daha sonra kaybolmaması özelliğidir.

> **English:** Durability protects committed data.
>
> **Türkçe:** Kalıcılık, commit edilmiş veriyi korur.

**İlişkili sözcükler:** durable; persist

## E

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 137, 138, 139:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 132:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

### eventually consistent · adjective phrase

**Türkçe:** nihai olarak tutarlı

**Bağlam — kaynak s. 111:** Yeni güncellemeler durduğunda ve bekleyen güncellemeler işlendiğinde kopyalar aynı duruma yaklaşır; arada eski veri okunabilir.

> **English:** The query view is eventually consistent.
>
> **Türkçe:** Sorgu görünümü, nihai olarak tutarlıdır.

**İlişkili sözcükler:** eventual consistency

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 111, 115:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 110, 145:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

## I

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 112:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

### isolation · noun

**Türkçe:** yalıtım

**Bağlam — kaynak s. 110, 111, 114, 115, 125 ve devamı:** Eşzamanlı transaction işlemlerinin ara etkilerini birbirinden koruma özelliğidir.

> **English:** Sagas do not provide transaction isolation automatically.
>
> **Türkçe:** Saga'lar transaction yalıtımını kendiliğinden sağlamaz.

**İlişkili sözcükler:** isolate; isolated

## L

### loosely coupled · adjective phrase

**Türkçe:** gevşek bağlı

**Bağlam — kaynak s. 114, 115:** Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

> **English:** Loosely coupled teams coordinate less frequently.
>
> **Türkçe:** Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.

**İlişkili sözcükler:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 110, 111, 112, 113, 114:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 135:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

### monolith · noun

**Türkçe:** monolit; tek dağıtılabilir bütün

**Bağlam — kaynak s. 129:** Kaynakta tek WAR dosyası gibi tek birim olarak paketlenip dağıtılan uygulama.

> **English:** The monolith is packaged as a single WAR file.
>
> **Türkçe:** Monolit, tek bir WAR dosyası olarak paketlenir.

**İlişkili sözcükler:** monolithic; karşılaştırma: independently deployable services. Monolith tek başına kötü tasarım demek değildir.

## O

### orchestration · noun

**Türkçe:** orkestrasyon; merkezi koordinasyon

**Bağlam — kaynak s. 110, 111, 118, 121, 122 ve devamı:** Saga adımlarını merkezi bir orchestrator yönlendirir.

> **English:** Orchestration makes the sequence of steps explicit.
>
> **Türkçe:** Orkestrasyon, adımların sırasını açıkça belirler.

**İlişkili sözcükler:** orchestrator; orchestrate

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 110, 114, 131, 145:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

## R

### repository · noun

**Türkçe:** veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 134:** Domain nesnelerinin bulunması ve saklanması için arayüz sağlar.

> **English:** The repository loads an aggregate.
>
> **Türkçe:** Repository, bir aggregate yükler.

**İlişkili sözcükler:** retrieve; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 121, 141:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### retry · verb / noun

**Türkçe:** yeniden denemek; yeniden deneme

**Bağlam — kaynak s. 130:** Başarısız olmuş işlemin belirli koşullarda tekrar yürütülmesidir.

> **English:** A retry can succeed after a transient failure.
>
> **Türkçe:** Geçici bir hatadan sonra yeniden deneme başarılı olabilir.

**İlişkili sözcükler:** retriable; retryable

### rollback · verb / noun

**Türkçe:** geri almak; geri alma

**Bağlam — kaynak s. 112, 115, 130:** Commit edilmemiş değişiklikleri transaction sınırı içinde geri döndürmektir.

> **English:** The transaction rolls back when the operation fails.
>
> **Türkçe:** İşlem başarısız olduğunda transaction geri alınır.

**İlişkili sözcükler:** roll back; compare: compensation

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 110, 111, 112, 114, 115 ve devamı:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 131:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### semantic lock · noun phrase

**Türkçe:** anlamsal kilit

**Bağlam — kaynak s. 128, 129, 130, 131, 132:** İş durumuyla, örneğin PENDING ile, eşzamanlı işlemleri kontrollü biçimde sınırlar.

> **English:** The pending status acts as a semantic lock.
>
> **Türkçe:** Bekleme durumu, anlamsal bir kilit işlevi görür.

**İlişkili sözcükler:** pending state; countermeasure

### span · verb

**Türkçe:** birden fazla alanı kapsamak, yayılmak

**Bağlam — kaynak s. 110, 111, 112:** Fiil olarak birden fazla servis, alan veya zaman aralığına yayılmayı anlatır.

> **English:** The transaction spans several services.
>
> **Türkçe:** Transaction, birkaç servisi kapsar.

**İlişkili sözcükler:** spans, spanning; synonym: extend across, cover.

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 111, 112, 115, 130:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 113, 144:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### technology stack · noun phrase

**Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü

**Bağlam — kaynak s. 112:** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.

> **English:** A service may use a different technology stack.
>
> **Türkçe:** Bir servis farklı bir teknoloji yığını kullanabilir.

**İlişkili sözcükler:** tech stack; ilişkili: framework, language, infrastructure.

### trade-off · noun

**Türkçe:** bir kazanım karşılığında başka bir alanda verilen ödün

**Bağlam — kaynak s. 131:** Mimari seçimin yarar ve maliyetlerini birlikte değerlendirmeyi gerektiren denge.

> **English:** The design involves a trade-off between simplicity and flexibility.
>
> **Türkçe:** Tasarım, sadelik ile esneklik arasında bir ödünleşim içerir.

**İlişkili sözcükler:** trade off (fiil); yakın anlamlı: compromise; kalıp: a trade-off between A and B.

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 110, 111, 112, 113, 114 ve devamı:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transition · noun / verb

**Türkçe:** geçiş; bir durumdan diğerine geçmek

**Bağlam — kaynak s. 123, 124, 125:** Bağlama göre sistemin, nesnenin veya iş akışının bir durumdan başka bir duruma geçmesini anlatır.

> **English:** The order makes a transition from pending to approved.
>
> **Türkçe:** Sipariş, bekleme durumundan onaylanmış duruma geçer.

**İlişkili sözcükler:** state transition; transition to; transitional

### two-phase commit · noun phrase

**Türkçe:** iki aşamalı commit

**Bağlam — kaynak s. 111, 112:** Dağıtık katılımcıların önce hazırlanıp sonra ortak kararı uyguladığı protokoldür.

> **English:** Two-phase commit coordinates the participants.
>
> **Türkçe:** İki aşamalı commit, katılımcıları koordine eder.

**İlişkili sözcükler:** 2PC; coordinator

## V

### viable · adjective

**Türkçe:** uygulanabilir, işleyebilir

**Bağlam — kaynak s. 112, 114:** Verilen koşullarda uygulanabilir ve çalışabilir bir seçeneği niteler.

> **English:** The team must find a viable way to maintain consistency.
>
> **Türkçe:** Ekip, tutarlılığı korumanın uygulanabilir bir yolunu bulmalıdır.

**İlişkili sözcükler:** viability; synonym: feasible, workable; antonym: unviable, impractical.

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 128, 130:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** mesaj aracısı

**3.** bağlılık

**4.** kimliği bulunan alan nesnesi

**5.** sürdürmek, korumak; bakımını yapmak

**6.** yeniden denemek; yeniden deneme

**7.** eşzamanlı; yanıtı bekleyen

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. broker** — Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

**3. coupling** — Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

**4. entity** — Değerleri değişse de kimliğiyle izlenen nesnedir.

**5. maintain** — “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

**6. retry** — Başarısız olmuş işlemin belirli koşullarda tekrar yürütülmesidir.

**7. synchronous** — İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
