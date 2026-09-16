# Ünite 09 · Testing microservices: Part 1 — Vocabulary

**Amaç:** Bu ünitenin 292–317. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### adopt · verb

**Türkçe:** benimsemek, kullanmaya başlamak

**Bağlam — kaynak s. 292:** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

> **English:** The team plans to adopt continuous delivery.
>
> **Türkçe:** Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.

**İlişkili sözcükler:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### agile · adjective

**Türkçe:** çevik

**Bağlam — kaynak s. 297:** Kısa geri bildirim döngüleriyle değişen gereksinimlere yanıt veren geliştirme yaklaşımıdır.

> **English:** Agile practices do not remove every architectural limitation.
>
> **Türkçe:** Çevik uygulamalar, mimarinin bütün sınırlamalarını ortadan kaldırmaz.

**İlişkili sözcükler:** agility; genel synonym: adaptable, nimble; bağlamsal karşılaştırma: waterfall.

### assertion · noun

**Türkçe:** beklenen sonucu doğrulayan test ifadesi

**Bağlam — kaynak s. 295, 309, 310, 314:** Bir testin koşulun doğru olduğunu denetlemesidir.

> **English:** The assertion checks the returned status.
>
> **Türkçe:** Doğrulama ifadesi, döndürülen durumu denetler.

**İlişkili sözcükler:** assert; verify

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 299, 300, 305:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 317:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### brittle · adjective

**Türkçe:** kırılgan, değişikliklerden kolayca etkilenen

**Bağlam — kaynak s. 298, 317:** Küçük veya ilgisiz değişikliklerden kolayca etkilenen test ya da tasarımı anlatır.

> **English:** A brittle test may fail after an unrelated change.
>
> **Türkçe:** Kırılgan bir test, ilgisiz bir değişiklikten sonra başarısız olabilir.

**İlişkili sözcükler:** brittleness; synonym: fragile; antonym: robust.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 311, 315:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### code base · noun phrase

**Türkçe:** kod tabanı

**Bağlam — kaynak s. 305:** Bir uygulama veya servisin üzerinde çalışılan kaynak kod bütünü.

> **English:** Several teams modify the same code base.
>
> **Türkçe:** Birden fazla ekip aynı kod tabanını değiştiriyor.

**İlişkili sözcükler:** yaygın yazım: codebase; ilişkili: source code, repository. Repository kodun tutulduğu yerdir.

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 299, 300, 301, 302, 303 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### container · noun

**Türkçe:** konteyner

**Bağlam — kaynak s. 314:** Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

> **English:** The container runs one service instance.
>
> **Türkçe:** Konteyner, bir servis örneğini çalıştırır.

**İlişkili sözcükler:** containerize; container image

### continuous delivery · noun phrase

**Türkçe:** sürekli teslim

**Bağlam — kaynak s. 305:** Yazılımın güvenli ve sürdürülebilir biçimde her an yayımlanabilir durumda tutulması.

> **English:** Continuous delivery keeps the software releasable.
>
> **Türkçe:** Sürekli teslim, yazılımı yayımlanabilir durumda tutar.

**İlişkili sözcükler:** deliver, delivery, releasable; karşılaştırma: continuous deployment.

### contract test · noun phrase

**Türkçe:** sözleşme testi

**Bağlam — kaynak s. 301, 302, 303, 305:** İstemci ve sağlayıcının üzerinde anlaştığı API davranışını doğrular.

> **English:** A contract test verifies the provider's response.
>
> **Türkçe:** Sözleşme testi, sağlayıcının yanıtını doğrular.

**İlişkili sözcükler:** consumer-driven contract

## D

### data consistency · noun phrase

**Türkçe:** veri tutarlılığı

**Bağlam — kaynak s. 309:** Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

> **English:** The saga maintains data consistency across services.
>
> **Türkçe:** Saga, servisler arasında veri tutarlılığını korur.

**İlişkili sözcükler:** consistent; inconsistent

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 304, 305, 306:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed system · noun phrase

**Türkçe:** dağıtık sistem

**Bağlam — kaynak s. 299:** Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.

> **English:** A distributed system must handle partial failures.
>
> **Türkçe:** Dağıtık bir sistem, kısmi arızaları ele almalıdır.

**İlişkili sözcükler:** distribute, distribution; ilişkili: remote call, interprocess communication.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 300, 305, 312, 315, 316:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 307:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 300, 301, 305, 313:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 309:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 297:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fixture · noun

**Türkçe:** test hazırlık verisi ve ortamı

**Bağlam — kaynak s. 295, 296:** Testin gerektirdiği nesne ve koşulların hazırlanmış bütünüdür.

> **English:** The test fixture contains an order and its customer.
>
> **Türkçe:** Test fixture, bir siparişi ve bu siparişin müşterisini içerir.

**İlişkili sözcükler:** setup; teardown

### force · verb

**Türkçe:** zorlamak, mecbur bırakmak

**Bağlam — kaynak s. 293:** Bu ünitede force + object + to + verb yapısıyla birini veya sistemi belirli bir davranışa zorlamak anlamındadır.

> **English:** An incompatible API change can force clients to upgrade.
>
> **Türkçe:** Uyumsuz bir API değişikliği, istemcileri sürüm yükseltmeye zorlayabilir.

**İlişkili sözcükler:** force someone to do something; forced; synonym: compel. İsim olarak forces, örüntü tasarımında çözümü etkileyen etkenlerdir.

## I

### immutable · adjective

**Türkçe:** oluşturulduktan sonra değiştirilmeyen

**Bağlam — kaynak s. 310:** Nesne veya dağıtım örneği yerinde değiştirilmek yerine yenisiyle değiştirilir.

> **English:** An immutable value cannot be changed in place.
>
> **Türkçe:** Değişmez bir değer, yerinde değiştirilemez.

**İlişkili sözcükler:** immutability; antonym: mutable

### in isolation · prepositional phrase

**Türkçe:** diğerlerinden ayrı olarak, yalıtılmış biçimde

**Bağlam — kaynak s. 292, 296, 301, 307, 308 ve devamı:** Bir nesneyi, bileşeni veya servisi diğerlerinden ayrı olarak inceleme ya da sınama bağlamında kullanılır.

> **English:** The component test checks the service in isolation.
>
> **Türkçe:** Bileşen testi, servisi diğerlerinden ayrı olarak sınar.

**İlişkili sözcükler:** isolate, isolated, isolation; karşılaştırma: test services together.

### inbound · adjective

**Türkçe:** içe gelen

**Bağlam — kaynak s. 309:** İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

> **English:** An inbound adapter invokes the business logic.
>
> **Türkçe:** Gelen yönlü bir adapter, iş mantığını çağırır.

**İlişkili sözcükler:** antonym: outbound

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 299:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

### isolation · noun

**Türkçe:** yalıtım; diğer bileşenlerden ayrı sınama

**Bağlam — kaynak s. 292, 296, 301, 307, 308 ve devamı:** Bu ünitede test edilen nesnenin veya servisin bağımlılıklarını ayırarak davranışını sınamayı anlatır. Transaction isolation ise ayrı bir anlamdır.

> **English:** Isolation lets the test control the service’s dependencies.
>
> **Türkçe:** Yalıtım, testin servisin bağımlılıklarını kontrol etmesini sağlar.

**İlişkili sözcükler:** in isolation; isolate; isolated; test double

## L

### lead time · noun phrase

**Türkçe:** teslim süresi; değişikliğin dağıtıma ulaşma süresi

**Bağlam — kaynak s. 293:** Başlangıcı kullanılan ölçüme göre değişebilen teslim süresidir. Bu kaynağın test bölümünde, commit edilmiş kodun production ortamına ulaşmasına kadar geçen süreyi anlatır.

> **English:** Long test queues increase lead time.
>
> **Türkçe:** Uzun test kuyrukları, değişikliğin dağıtıma ulaşma süresini artırır.

**İlişkili sözcükler:** ilişkili: deployment frequency, delivery time. Burada projenin bütün yaşam süresi kastedilmez.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 309:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 317:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

### mock · noun / verb

**Türkçe:** beklentileri denetleyen test taklidi

**Bağlam — kaynak s. 292, 296, 301, 303, 305 ve devamı:** Bir bağımlılığın yerine geçer; testte yapılan etkileşimleri de doğrulayabilir.

> **English:** The test verifies a call to the mock.
>
> **Türkçe:** Test, mock nesnesine yapılan bir çağrıyı doğrular.

**İlişkili sözcükler:** mocking; compare: stub

## O

### outbound · adjective

**Türkçe:** dışa giden

**Bağlam — kaynak s. 309:** İş mantığından dış sistemlere doğru yapılan çağrıyı anlatır.

> **English:** An outbound adapter accesses the database.
>
> **Türkçe:** Giden yönlü bir adapter, veritabanına erişir.

**İlişkili sözcükler:** antonym: inbound

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 302, 303:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### provider · noun

**Türkçe:** sağlayıcı

**Bağlam — kaynak s. 299, 301, 302, 303, 305:** Bir API, mesaj veya hizmet sunan taraftır.

> **English:** The provider must satisfy its API contract.
>
> **Türkçe:** Sağlayıcı, API sözleşmesini karşılamalıdır.

**İlişkili sözcükler:** provide; consumer

## R

### repository · noun

**Türkçe:** depo; veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 304, 305, 313:** Bağlama göre kaynak kodunun/paketlerin saklandığı depo veya domain nesnelerine erişimi soyutlayan Repository nesnesidir; kullanıldığı cümleye göre ayrılmalıdır.

> **English:** The team publishes the package to a repository.
>
> **Türkçe:** Ekip, paketi bir depoya yayımlar.

**İlişkili sözcükler:** source repository; Maven repository; Repository pattern; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 315:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 314:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 309, 310, 311, 312:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### stub · noun

**Türkçe:** önceden belirlenmiş yanıt veren test nesnesi

**Bağlam — kaynak s. 292, 296, 303, 305, 307 ve devamı:** Bağımlılığın davranışını test için kontrollü yanıtlarla taklit eder.

> **English:** The stub returns a fixed response.
>
> **Türkçe:** Stub, önceden belirlenmiş bir yanıt döndürür.

**İlişkili sözcükler:** stubbing; compare: mock

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 299:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 296:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

## V

### value object · noun phrase

**Türkçe:** kimliğinden çok değeriyle tanımlanan nesne

**Bağlam — kaynak s. 308, 309, 310, 312:** Eşitliği ayrı bir kimlikle değil, içerdiği değerlerle belirlenir.

> **English:** Money can be modeled as a value object.
>
> **Türkçe:** Money, bir value object olarak modellenebilir.

**İlişkili sözcükler:** immutable; entity

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** benimsemek, kullanmaya başlamak

**2.** mesaj aracısı

**3.** veri tutarlılığı

**4.** kimliği bulunan alan nesnesi

**5.** içe gelen

**6.** beklentileri denetleyen test taklidi

**7.** yönlendirme

<!-- page-break -->

## Cevap anahtarı

**1. adopt** — Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.

**2. broker** — Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

**3. data consistency** — Verilerin tanımlanmış iş kurallarına ve birbirleriyle ilişkilerine uygun olmasıdır.

**4. entity** — Değerleri değişse de kimliğiyle izlenen nesnedir.

**5. inbound** — İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

**6. mock** — Bir bağımlılığın yerine geçer; testte yapılan etkileşimleri de doğrulayabilir.

**7. routing** — İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
