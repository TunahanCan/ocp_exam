# Ünite 11 · Developing production-ready services — Vocabulary

**Amaç:** Bu ünitenin 348–382. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### access token · noun phrase

**Türkçe:** erişim belirteci

**Bağlam — kaynak s. 354, 357, 358, 359, 360:** İstemcinin korunan bir kaynağa erişme yetkisini temsil eden belirteçtir; tek başına kullanıcı kimliğini doğrulayan bir kimlik belgesiyle eş tutulmaz.

> **English:** The service validates the access token.
>
> **Türkçe:** Servis, erişim belirtecini doğrular.

**İlişkili sözcükler:** access, accessible; ilişkili: scope, authorization, bearer token. Access token ile ID token farklı amaçlar taşır.

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 349:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### aggregate · noun

**Türkçe:** tutarlılık sınırı oluşturan nesne bütünü

**Bağlam — kaynak s. 350, 356, 368, 370, 374:** DDD'de birlikte değişen nesneleri tek kök üzerinden yönetir.

> **English:** An aggregate protects its invariants.
>
> **Türkçe:** Bir aggregate, değişmez kurallarını korur.

**İlişkili sözcükler:** aggregate root; aggregation

### audit log · noun phrase

**Türkçe:** denetim günlüğü

**Bağlam — kaynak s. 377, 378:** Neyin ne zaman değiştiğini incelemek için tutulan kayıttır.

> **English:** An audit log records changes to the data.
>
> **Türkçe:** Denetim günlüğü, verilerdeki değişiklikleri kaydeder.

**İlişkili sözcükler:** auditing; audit trail

### authentication · noun

**Türkçe:** kimlik doğrulama

**Bağlam — kaynak s. 349, 350, 351, 353, 354 ve devamı:** İsteği yapanın kim olduğunu doğrulamadır.

> **English:** Authentication establishes the user's identity.
>
> **Türkçe:** Kimlik doğrulama, kullanıcının kimliğini belirler.

**İlişkili sözcükler:** authenticate; authenticated

### authorization · noun

**Türkçe:** yetkilendirme

**Bağlam — kaynak s. 349, 350, 351, 353, 355 ve devamı:** Bir kimliğin veya istemcinin belirli bir kaynak üzerinde hangi işlemleri yapmaya yetkili olduğunu belirleme ve denetleme sürecidir.

> **English:** Authorization controls access to an operation.
>
> **Türkçe:** Yetkilendirme, bir işleme erişimi denetler.

**İlişkili sözcükler:** authorize; authorized

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 356, 365:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 354, 360, 364:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 349, 360, 368, 373, 382:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### circuit breaker · noun phrase

**Türkçe:** devre kesici

**Bağlam — kaynak s. 378, 380, 381:** Tekrarlanan başarısızlıklardan sonra çağrıları geçici olarak durduran korumadır.

> **English:** The circuit breaker rejects calls while it is open.
>
> **Türkçe:** Devre kesici, açık durumdayken çağrıları reddeder.

**İlişkili sözcükler:** open; closed; half-open

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 350, 353, 356, 366:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### container · noun

**Türkçe:** konteyner

**Bağlam — kaynak s. 362, 369:** Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

> **English:** The container runs one service instance.
>
> **Türkçe:** Konteyner, bir servis örneğini çalıştırır.

**İlişkili sözcükler:** containerize; container image

### coupling · noun

**Türkçe:** bağlılık

**Bağlam — kaynak s. 354, 356:** Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

> **English:** Loose coupling supports independent changes.
>
> **Türkçe:** Gevşek bağlılık, bağımsız değişiklikleri destekler.

**İlişkili sözcükler:** coupled; decouple

### cross-cutting concern · noun phrase

**Türkçe:** birden fazla alanı kesen ortak sorumluluk

**Bağlam — kaynak s. 379, 380, 381, 382:** Birden fazla bileşende ortak biçimde ele alınması gereken sorumluluktur.

> **English:** Configuration is a cross-cutting concern.
>
> **Türkçe:** Yapılandırma, birçok servisi ilgilendiren ortak bir sorumluluktur.

**İlişkili sözcükler:** concern: ilgilenilmesi gereken konu; ilişkili: shared responsibility, infrastructure.

## D

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 348, 360, 364, 368, 377 ve devamı:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed system · noun phrase

**Türkçe:** dağıtık sistem

**Bağlam — kaynak s. 349:** Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.

> **English:** A distributed system must handle partial failures.
>
> **Türkçe:** Dağıtık bir sistem, kısmi arızaları ele almalıdır.

**İlişkili sözcükler:** distribute, distribution; ilişkili: remote call, interprocess communication.

### distributed tracing · noun phrase

**Türkçe:** dağıtık izleme

**Bağlam — kaynak s. 348, 366, 370, 371, 372 ve devamı:** Bir isteğin farklı servisler boyunca izlediği çağrı zincirini kaydeder.

> **English:** Distributed tracing shows where a request spends time.
>
> **Türkçe:** Dağıtık izleme, bir isteğin nerede zaman harcadığını gösterir.

**İlişkili sözcükler:** trace; span

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 353, 356, 357, 364, 378 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 359, 365, 366, 367, 368 ve devamı:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### event sourcing · noun phrase

**Türkçe:** durumu olay geçmişiyle saklama

**Bağlam — kaynak s. 378:** Son durumu güncellemek yerine değişim olaylarını kalıcılaştırır; durum olaylardan üretilir.

> **English:** Event sourcing stores changes as events.
>
> **Türkçe:** Event sourcing, değişiklikleri olaylar olarak saklar.

**İlişkili sözcükler:** event store; replay

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 366:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 380:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

### force · verb

**Türkçe:** zorlamak, mecbur bırakmak

**Bağlam — kaynak s. 349:** Bu ünitede force + object + to + verb yapısıyla birini veya sistemi belirli bir davranışa zorlamak anlamındadır.

> **English:** An incompatible API change can force clients to upgrade.
>
> **Türkçe:** Uyumsuz bir API değişikliği, istemcileri sürüm yükseltmeye zorlayabilir.

**İlişkili sözcükler:** force someone to do something; forced; synonym: compel. İsim olarak forces, örüntü tasarımında çözümü etkileyen etkenlerdir.

## H

### health check · noun phrase

**Türkçe:** sağlık kontrolü

**Bağlam — kaynak s. 348, 365, 366, 367, 368 ve devamı:** Bir servis örneğinin çalışıp çalışmadığını veya trafik alabilecek durumda olup olmadığını sınar.

> **English:** A health check reports the service's condition.
>
> **Türkçe:** Sağlık kontrolü, servisin durumunu bildirir.

**İlişkili sözcükler:** liveness; readiness

## I

### inbound · adjective

**Türkçe:** içe gelen

**Bağlam — kaynak s. 371:** İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

> **English:** An inbound adapter invokes the business logic.
>
> **Türkçe:** Gelen yönlü bir adapter, iş mantığını çağırır.

**İlişkili sözcükler:** antonym: outbound

### interprocess communication · noun phrase

**Türkçe:** süreçler arası iletişim

**Bağlam — kaynak s. 350, 380, 381:** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.

> **English:** Services use interprocess communication to collaborate.
>
> **Türkçe:** Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.

**İlişkili sözcükler:** process, communicate, communication; karşılaştırma: local method call.

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 349, 356, 370, 373:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 353, 364, 366:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### monolith · noun

**Türkçe:** monolit; tek dağıtılabilir bütün

**Bağlam — kaynak s. 349, 350:** Kaynakta tek WAR dosyası gibi tek birim olarak paketlenip dağıtılan uygulama.

> **English:** The monolith is packaged as a single WAR file.
>
> **Türkçe:** Monolit, tek bir WAR dosyası olarak paketlenir.

**İlişkili sözcükler:** monolithic; karşılaştırma: independently deployable services. Monolith tek başına kötü tasarım demek değildir.

## O

### observability · noun

**Türkçe:** gözlemlenebilirlik

**Bağlam — kaynak s. 348, 349, 365, 366, 368 ve devamı:** Sistemin iç durumunu log, metric ve trace gibi dış çıktılardan anlayabilmektir.

> **English:** Logs and traces support observability.
>
> **Türkçe:** Log'lar ve iz kayıtları, gözlemlenebilirliği destekler.

**İlişkili sözcükler:** observe, observable, observation; ilişkili: metrics, tracing, logging.

### outbound · adjective

**Türkçe:** dışa giden

**Bağlam — kaynak s. 372:** İş mantığından dış sistemlere doğru yapılan çağrıyı anlatır.

> **English:** An outbound adapter accesses the database.
>
> **Türkçe:** Giden yönlü bir adapter, veritabanına erişir.

**İlişkili sözcükler:** antonym: inbound

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 348, 349, 354, 360, 361 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### polling · noun

**Türkçe:** düzenli aralıklarla sorgulama

**Bağlam — kaynak s. 364:** Yeni veri veya iş olup olmadığını tekrar tekrar denetleme tekniğidir.

> **English:** Polling checks the table for new messages.
>
> **Türkçe:** Polling, tabloda yeni mesaj olup olmadığını denetler.

**İlişkili sözcükler:** poll; poller

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 348, 353, 356, 366, 367 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### recover · verb

**Türkçe:** toparlanmak, yeniden çalışır duruma gelmek

**Bağlam — kaynak s. 366:** Production sorunundan sonra hizmetin yeniden işler duruma gelmesi.

> **English:** The team works to recover from the outage.
>
> **Türkçe:** Ekip, hizmet kesintisinin ardından sistemi yeniden çalışır duruma getirmek için uğraşır.

**İlişkili sözcükler:** recovery, recoverable; kalıp: recover from; ilişkili: restore service.

### registry · noun

**Türkçe:** kayıt servisi veya dizini

**Bağlam — kaynak s. 375:** Çalışan servis örneklerinin adresleri gibi bilgileri tutar.

> **English:** The registry stores the locations of service instances.
>
> **Türkçe:** Kayıt servisi, servis örneklerinin konumlarını saklar.

**İlişkili sözcükler:** register; registration

### repository · noun

**Türkçe:** kaynak kod deposu

**Bağlam — kaynak s. 357:** Bu ünitedeki OAuth örneğinde GitHub üzerinde erişim izni verilen kaynak kod deposudur.

> **English:** The user grants the CI service access to the repository.
>
> **Türkçe:** Kullanıcı, CI servisine depoya erişim izni verir.

**İlişkili sözcükler:** GitHub repository; source code; access token

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 352, 356, 362, 363, 364 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 380:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### serverless · adjective

**Türkçe:** sunucu yönetimi platforma bırakılmış

**Bağlam — kaynak s. 369:** Geliştirici kodu dağıtır; çalıştırma altyapısının önemli bölümü platform tarafından yönetilir.

> **English:** Serverless deployment runs the handler on demand.
>
> **Türkçe:** Serverless dağıtım, işleyiciyi talep üzerine çalıştırır.

**İlişkili sözcükler:** function as a service

### service discovery · noun phrase

**Türkçe:** servis keşfi

**Bağlam — kaynak s. 378, 379, 380, 381:** Çağrılabilecek servis örneklerinin ağ konumlarını bulma mekanizmasıdır.

> **English:** Service discovery locates available instances.
>
> **Türkçe:** Servis keşfi, kullanılabilir örneklerin konumunu bulur.

**İlişkili sözcükler:** discover; registry

### service mesh · noun phrase

**Türkçe:** servisler arası iletişimi yöneten altyapı

**Bağlam — kaynak s. 350, 379, 380, 381, 382:** Trafik yönetimi gibi iletişim görevlerini uygulama kodundan ayırır.

> **English:** A service mesh can manage traffic between services.
>
> **Türkçe:** Bir service mesh, servisler arasındaki trafiği yönetebilir.

**İlişkili sözcükler:** sidecar; proxy

### span · noun / verb

**Türkçe:** iz kaydındaki iş adımı; kapsamak, yayılmak

**Bağlam — kaynak s. 371, 372, 373:** Distributed tracing bağlamında span, başlangıç ve bitiş zamanı olan tek bir işlem veya çağrı adımını temsil eder. Fiil olarak kapsamak anlamına da gelir.

> **English:** A trace contains a span for each recorded service call.
>
> **Türkçe:** Bir trace, kaydedilen her servis çağrısı için bir span içerir.

**İlişkili sözcükler:** trace; parent span; child span; verb: span several services

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 378:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 356:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### technology stack · noun phrase

**Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü

**Bağlam — kaynak s. 351, 373:** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.

> **English:** A service may use a different technology stack.
>
> **Türkçe:** Bir servis farklı bir teknoloji yığını kullanabilir.

**İlişkili sözcükler:** tech stack; ilişkili: framework, language, infrastructure.

### transaction · noun

**Türkçe:** bir bütün olarak yönetilen veri işlemi

**Bağlam — kaynak s. 348, 367:** Veri güncellemelerinin tanımlı commit veya rollback sınırı içinde yürütülmesidir.

> **English:** The transaction updates the order.
>
> **Türkçe:** Transaction, siparişi günceller.

**İlişkili sözcükler:** transactional; commit

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 350, 368, 369, 376, 377:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** erişim belirteci

**2.** kullanılabilirlik, hizmete erişilebilir olma durumu

**3.** bağlılık

**4.** API erişim noktası

**5.** içe gelen

**6.** dışa giden

**7.** kaynak kod deposu

<!-- page-break -->

## Cevap anahtarı

**1. access token** — İstemcinin korunan bir kaynağa erişme yetkisini temsil eden belirteçtir; tek başına kullanıcı kimliğini doğrulayan bir kimlik belgesiyle eş tutulmaz.

**2. availability** — Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

**3. coupling** — Bir bileşenin başka bir bileşenin ayrıntılarına bağımlı olma derecesidir.

**4. endpoint** — İstemcinin belirli bir işlev için istek gönderdiği adrestir.

**5. inbound** — İsteğin veya çağrının uygulama sınırının dışından içine doğru ilerlemesidir.

**6. outbound** — İş mantığından dış sistemlere doğru yapılan çağrıyı anlatır.

**7. repository** — Bu ünitedeki OAuth örneğinde GitHub üzerinde erişim izni verilen kaynak kod deposudur.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
