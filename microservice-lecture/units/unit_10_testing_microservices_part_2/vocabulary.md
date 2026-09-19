# Ünite 10 · Testing microservices: Part 2 — Vocabulary

**Amaç:** Bu ünitenin 318–347. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.


## A

### acceptance test · noun phrase

**Türkçe:** kabul testi

**Bağlam — kaynak s. 318, 335, 336, 337, 341 ve devamı:** Bileşenin dışarıdan gözlenen davranışının iş gereksinimlerini karşılayıp karşılamadığını denetler.

> **English:** An acceptance test describes the expected business behavior.
>
> **Türkçe:** Bir kabul testi, beklenen iş davranışını tanımlar.

**İlişkili sözcükler:** acceptance criteria; scenario; business-facing

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 321, 326, 327, 328:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### assertion · noun

**Türkçe:** beklenen sonucu doğrulayan test ifadesi

**Bağlam — kaynak s. 321, 343:** Bir testin koşulun doğru olduğunu denetlemesidir.

> **English:** The assertion checks the returned status.
>
> **Türkçe:** Doğrulama ifadesi, döndürülen durumu denetler.

**İlişkili sözcükler:** assert; verify

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 320, 330, 331, 332, 334 ve devamı:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 320, 339:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### brittle · adjective

**Türkçe:** kırılgan, değişikliklerden kolayca etkilenen

**Bağlam — kaynak s. 319, 335, 339, 345, 347:** Küçük veya ilgisiz değişikliklerden kolayca etkilenen test ya da tasarımı anlatır.

> **English:** A brittle test may fail after an unrelated change.
>
> **Türkçe:** Kırılgan bir test, ilgisiz bir değişiklikten sonra başarısız olabilir.

**İlişkili sözcükler:** brittleness; synonym: fragile; antonym: robust.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 339:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### component test · noun phrase

**Türkçe:** bileşen testi

**Bağlam — kaynak s. 318, 322, 335, 336, 338 ve devamı:** Bir servisin bütün olarak davranışını, diğer servisleri test taklitleriyle değiştirerek sınar.

> **English:** A component test verifies the service as a whole.
>
> **Türkçe:** Bir bileşen testi, servisi bir bütün olarak doğrular.

**İlişkili sözcükler:** in-process; out-of-process; test double

### conform to · verb phrase

**Türkçe:** uygun olmak, uymak

**Bağlam — kaynak s. 324–334:** İstek ya da yanıtın sözleşmeyle tanımlanan biçimi karşılamasıdır.

> **English:** The command must conform to the contract.
>
> **Türkçe:** Komut sözleşmeye uymalıdır.

**İlişkili sözcükler:** conformance; synonym: comply with

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 318, 321, 323, 324, 325 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### consumer-driven contract · noun phrase

**Türkçe:** tüketicinin beklentileriyle tanımlanan sözleşme

**Bağlam — kaynak s. 318, 323, 324, 328, 334:** Tüketicinin sağlayıcıdan beklediği istek, yanıt veya mesaj davranışını kaydeder.

> **English:** A consumer-driven contract captures the client’s expectations.
>
> **Türkçe:** Consumer-driven contract, istemcinin beklentilerini kaydeder.

**İlişkili sözcükler:** consumer; provider; contract testing

### container · noun

**Türkçe:** konteyner

**Bağlam — kaynak s. 339, 340, 344, 346:** Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

> **English:** The container runs one service instance.
>
> **Türkçe:** Konteyner, bir servis örneğini çalıştırır.

**İlişkili sözcükler:** containerize; container image

### contract test · noun phrase

**Türkçe:** sözleşme testi

**Bağlam — kaynak s. 318, 323, 328, 329, 330 ve devamı:** İstemci ve sağlayıcının üzerinde anlaştığı API davranışını doğrular.

> **English:** A contract test verifies the provider's response.
>
> **Türkçe:** Sözleşme testi, sağlayıcının yanıtını doğrular.

**İlişkili sözcükler:** consumer-driven contract

## D

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 335, 339, 340, 344, 345:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### domain event · noun phrase

**Türkçe:** alan olayı

**Bağlam — kaynak s. 319, 320, 326, 328, 330 ve devamı:** İş alanında gerçekleşmiş ve diğer parçalar açısından anlamlı bir değişimi bildirir.

> **English:** A domain event describes something that has happened.
>
> **Türkçe:** Bir domain event, gerçekleşmiş bir durumu anlatır.

**İlişkili sözcükler:** event handler; publish

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 339, 340:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 322, 323, 325, 336, 338:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### eventually · adverb

**Türkçe:** sonunda, bir süre sonra

**Bağlam — kaynak s. 343:** Asenkron işin hemen tamamlanmayabileceğini anlatır; örnekte eventually() doğrulamayı tekrarlar.

> **English:** The order eventually reaches the expected state.
>
> **Türkçe:** Sipariş bir süre sonra beklenen duruma ulaşır.

**İlişkili sözcükler:** eventual; related: retry, eventual consistency

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 337, 340:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

## G

### Gherkin · proper noun

**Türkçe:** davranış senaryosu yazım dili

**Bağlam — kaynak s. 335, 336, 337, 338, 339 ve devamı:** Given, When ve Then gibi anahtar sözcüklerle iş davranışını anlaşılır senaryolar biçiminde yazar.

> **English:** The team writes the acceptance scenario in Gherkin.
>
> **Türkçe:** Ekip, kabul senaryosunu Gherkin ile yazar.

**İlişkili sözcükler:** feature; scenario; step definition

## H

### hook method · noun phrase

**Türkçe:** özelleştirme veya tetikleme noktası sunan metot

**Bağlam — kaynak s. 327–328:** Üretilen testin çağırdığı üst sınıf metodu, örnekte olay yayımını tetikler.

> **English:** The generated test invokes a hook method.
>
> **Türkçe:** Üretilen test bir hook metodu çağırır.

**İlişkili sözcükler:** hook; related: extension point

## I

### in isolation · prepositional phrase

**Türkçe:** diğerlerinden ayrı olarak, yalıtılmış biçimde

**Bağlam — kaynak s. 318, 335, 336, 339, 345 ve devamı:** Bir nesneyi, bileşeni veya servisi diğerlerinden ayrı olarak inceleme ya da sınama bağlamında kullanılır.

> **English:** The component test checks the service in isolation.
>
> **Türkçe:** Bileşen testi, servisi diğerlerinden ayrı olarak sınar.

**İlişkili sözcükler:** isolate, isolated, isolation; karşılaştırma: test services together.

### in-process · adjective

**Türkçe:** aynı süreç içinde çalışan

**Bağlam — kaynak s. 339:** Test ve servis aynı JVM sürecinde çalışır; bağımlılıklar bellek içi taklitlerle değiştirilebilir.

> **English:** The in-process test runs the service in the same JVM.
>
> **Türkçe:** Süreç içi test, servisi aynı JVM içinde çalıştırır.

**İlişkili sözcükler:** compare: out-of-process

### isolation · noun

**Türkçe:** yalıtım; diğer bileşenlerden ayrı sınama

**Bağlam — kaynak s. 318, 335, 336, 339, 345 ve devamı:** Bu ünitede test edilen nesnenin veya servisin bağımlılıklarını ayırarak davranışını sınamayı anlatır. Transaction isolation ise ayrı bir anlamdır.

> **English:** Isolation lets the test control the service’s dependencies.
>
> **Türkçe:** Yalıtım, testin servisin bağımlılıklarını kontrol etmesini sağlar.

**İlişkili sözcükler:** in isolation; isolate; isolated; test double

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 321:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### message channel · noun phrase

**Türkçe:** mesaj kanalı

**Bağlam — kaynak s. 326, 330, 331, 336:** Mesajların gönderildiği mantıksal iletişim yoludur.

> **English:** The producer sends a message to a channel.
>
> **Türkçe:** Üretici, bir kanala mesaj gönderir.

**İlişkili sözcükler:** queue; topic

### mock · noun / verb

**Türkçe:** beklentileri denetleyen test taklidi

**Bağlam — kaynak s. 321, 323, 324, 325, 326 ve devamı:** Bir bağımlılığın yerine geçer; testte yapılan etkileşimleri de doğrulayabilir.

> **English:** The test verifies a call to the mock.
>
> **Türkçe:** Test, mock nesnesine yapılan bir çağrıyı doğrular.

**İlişkili sözcükler:** mocking; compare: stub

## O

### out-of-process · adjective

**Türkçe:** ayrı süreçte çalışan

**Bağlam — kaynak s. 339–345:** Servis testten ayrı süreçte, örneğin Docker container içinde çalıştırılır.

> **English:** The out-of-process test starts a container.
>
> **Türkçe:** Süreç dışı test bir container başlatır.

**İlişkili sözcükler:** compare: in-process

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 347:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 335:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### persistence · noun

**Türkçe:** kalıcı saklama

**Bağlam — kaynak s. 320, 321, 322:** Nesne veya verinin süreç sona erdikten sonra da tutulmasıdır.

> **English:** Persistence stores the aggregate's state.
>
> **Türkçe:** Kalıcı saklama, aggregate'ın durumunu kaydeder.

**İlişkili sözcükler:** persist; persistent

### provider · noun

**Türkçe:** sağlayıcı

**Bağlam — kaynak s. 321, 323, 324, 327, 328 ve devamı:** Bir API, mesaj veya hizmet sunan taraftır.

> **English:** The provider must satisfy its API contract.
>
> **Türkçe:** Sağlayıcı, API sözleşmesini karşılamalıdır.

**İlişkili sözcükler:** provide; consumer

## R

### repository · noun

**Türkçe:** yazılım paket deposu

**Bağlam — kaynak s. 340:** Burada sözleşmeleri içeren JAR dosyalarının yayımlandığı Maven deposunu anlatır; domain modelindeki Repository sınıfı değildir.

> **English:** The contract JAR is published to a Maven repository.
>
> **Türkçe:** Sözleşme JAR dosyası bir Maven deposuna yayımlanır.

**İlişkili sözcükler:** artifact; Maven repository; publish; dependency

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 321, 324, 326:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

## S

### saga · noun

**Türkçe:** yerel transaction adımlarından oluşan iş akışı

**Bağlam — kaynak s. 330, 342:** Birden fazla servis boyunca ilerler; başarısızlıkta uygun telafi işlemleri kullanabilir.

> **English:** A saga coordinates local transactions.
>
> **Türkçe:** Bir saga, yerel transaction işlemlerini koordine eder.

**İlişkili sözcükler:** saga participant; saga orchestrator

### sparingly · adverb

**Türkçe:** ölçülü biçimde, az miktarda

**Bağlam — kaynak s. 319:** Yavaş ve maliyetli end-to-end testlerin sayısını sınırlama önerisidir.

> **English:** Use expensive end-to-end tests sparingly.
>
> **Türkçe:** Pahalı uçtan uca testleri az sayıda kullanın.

**İlişkili sözcükler:** sparing; antonym in context: extensively

### step definition · noun phrase

**Türkçe:** senaryo adımının çalıştırılabilir tanımı

**Bağlam — kaynak s. 337–344:** Gherkin adımını gerçekleştiren Java metodudur.

> **English:** A step definition sends an HTTP request.
>
> **Türkçe:** Bir adım tanımı HTTP isteği gönderir.

**İlişkili sözcükler:** define, definition; related: scenario

### stub · noun

**Türkçe:** önceden belirlenmiş yanıt veren test nesnesi

**Bağlam — kaynak s. 318, 321, 323, 328, 329 ve devamı:** Bağımlılığın davranışını test için kontrollü yanıtlarla taklit eder.

> **English:** The stub returns a fixed response.
>
> **Türkçe:** Stub, önceden belirlenmiş bir yanıt döndürür.

**İlişkili sözcükler:** stubbing; compare: mock

## T

### test coverage · noun phrase

**Türkçe:** test kapsamı

**Bağlam — kaynak s. 339:** Testlerin kodun veya davranışın hangi bölümlerini sınadığını gösterir; tek başına doğruluğun garantisi değildir.

> **English:** The component test improves coverage of the service boundary.
>
> **Türkçe:** Bileşen testi, servis sınırına ilişkin test kapsamını artırır.

**İlişkili sözcükler:** cover; coverage; boundary

### test double · noun phrase

**Türkçe:** testte bağımlılığın yerine geçen taklit

**Bağlam — kaynak s. 318, 321, 323, 324, 325 ve devamı:** Testi kontrol edilebilir kılmak için gerçek bağımlılığın yerine geçen ortak nesne veya bileşen türüdür; stub ve mock bu gruptadır.

> **English:** The test double replaces a remote service.
>
> **Türkçe:** Test taklidi, uzak bir servisin yerine geçer.

**İlişkili sözcükler:** stub; mock; fake

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 321, 322:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

### transitive dependency · noun phrase

**Türkçe:** dolaylı bağımlılık

**Bağlam — kaynak s. 335, 347:** Doğrudan bağımlı olunan bir bileşenin başka bir bileşene bağımlılığı yoluyla oluşur.

> **English:** Starting one service may require its transitive dependencies.
>
> **Türkçe:** Bir servisi başlatmak, dolaylı bağımlılıklarını da gerektirebilir.

**İlişkili sözcükler:** transitively; compare: direct dependency

## U

### user journey · noun phrase

**Türkçe:** kullanıcı yolculuğu

**Bağlam — kaynak s. 345–347:** Kullanıcının uygulamada ardışık yaptığı işlemleri tek akışta temsil eder.

> **English:** The user journey creates, revises, and cancels an order.
>
> **Türkçe:** Kullanıcı yolculuğu bir sipariş oluşturur, değiştirir ve iptal eder.

**İlişkili sözcükler:** journey; related: workflow, scenario

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 321, 329:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** kabul testi

**2.** kırılgan, değişikliklerden kolayca etkilenen

**3.** konteyner

**4.** API erişim noktası

**5.** sürdürmek, korumak; bakımını yapmak

**6.** kalıcı saklama

**7.** önceden belirlenmiş yanıt veren test nesnesi

<!-- page-break -->

## Cevap anahtarı

**1. acceptance test** — Bileşenin dışarıdan gözlenen davranışının iş gereksinimlerini karşılayıp karşılamadığını denetler.

**2. brittle** — Küçük veya ilgisiz değişikliklerden kolayca etkilenen test ya da tasarımı anlatır.

**3. container** — Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

**4. endpoint** — İstemcinin belirli bir işlev için istek gönderdiği adrestir.

**5. maintain** — “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

**6. persistence** — Nesne veya verinin süreç sona erdikten sonra da tutulmasıdır.

**7. stub** — Bağımlılığın davranışını test için kontrollü yanıtlarla taklit eder.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
