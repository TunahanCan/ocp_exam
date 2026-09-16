# Ünite 08 · External API patterns — Vocabulary

**Amaç:** Bu ünitenin 253–291. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 259:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### asynchronous · adjective

**Türkçe:** eşzamansız

**Bağlam — kaynak s. 268, 269, 270, 277:** Gönderici, alıcının işlemi bitirmesini aynı çağrıda beklemek zorunda değildir.

> **English:** The service uses asynchronous messaging.
>
> **Türkçe:** Servis, eşzamansız mesajlaşma kullanır.

**İlişkili sözcükler:** asynchronously; antonym: synchronous

### authentication · noun

**Türkçe:** kimlik doğrulama

**Bağlam — kaynak s. 259, 262, 263, 271, 272 ve devamı:** İsteği yapanın kim olduğunu doğrulamadır.

> **English:** Authentication establishes the user's identity.
>
> **Türkçe:** Kimlik doğrulama, kullanıcının kimliğini belirler.

**İlişkili sözcükler:** authenticate; authenticated

### authorization · noun

**Türkçe:** yetkilendirme

**Bağlam — kaynak s. 262, 263:** Bir kimliğin veya istemcinin belirli bir kaynak üzerinde hangi işlemleri yapmaya yetkili olduğunu belirleme ve denetleme sürecidir.

> **English:** Authorization controls access to an operation.
>
> **Türkçe:** Yetkilendirme, bir işleme erişimi denetler.

**İlişkili sözcükler:** authorize; authorized

### autonomous · adjective

**Türkçe:** özerk, kendi kararlarını verebilen

**Bağlam — kaynak s. 264:** Bir ekibin sorumluluğunu üstlendiği işlerde bağımsız karar alabilmesidir.

> **English:** An autonomous team owns the delivery of its service.
>
> **Türkçe:** Özerk bir ekip, kendi servisinin tesliminden sorumludur.

**İlişkili sözcükler:** autonomy; synonym: self-governing; antonym: dependent.

### availability · noun

**Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu

**Bağlam — kaynak s. 278:** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

> **English:** The team monitors the availability of the application.
>
> **Türkçe:** Ekip, uygulamanın kullanılabilirliğini izler.

**İlişkili sözcükler:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 259, 263, 266, 267, 268 ve devamı:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

## C

### circuit breaker · noun phrase

**Türkçe:** devre kesici

**Bağlam — kaynak s. 270:** Tekrarlanan başarısızlıklardan sonra çağrıları geçici olarak durduran korumadır.

> **English:** The circuit breaker rejects calls while it is open.
>
> **Türkçe:** Devre kesici, açık durumdayken çağrıları reddeder.

**İlişkili sözcükler:** open; closed; half-open

### code base · noun phrase

**Türkçe:** kod tabanı

**Bağlam — kaynak s. 264:** Bir uygulama veya servisin üzerinde çalışılan kaynak kod bütünü.

> **English:** Several teams modify the same code base.
>
> **Türkçe:** Birden fazla ekip aynı kod tabanını değiştiriyor.

**İlişkili sözcükler:** yaygın yazım: codebase; ilişkili: source code, repository. Repository kodun tutulduğu yerdir.

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 254, 255, 258, 283, 284 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### container · noun

**Türkçe:** konteyner

**Bağlam — kaynak s. 267, 272:** Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

> **English:** The container runs one service instance.
>
> **Türkçe:** Konteyner, bir servis örneğini çalıştırır.

**İlişkili sözcükler:** containerize; container image

## D

### decompose · verb

**Türkçe:** bileşenlere ayırmak

**Bağlam — kaynak s. 257:** Uygulamayı sorumlulukları belirli modül veya servislere bölmektir.

> **English:** We decompose the application by business capability.
>
> **Türkçe:** Uygulamayı iş yetkinliğine göre ayırırız.

**İlişkili sözcükler:** decomposition; compose

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 253, 264, 267, 271, 291:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 254, 257, 258, 259, 263 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 259, 267:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 255, 269, 271, 274, 275 ve devamı:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 260, 271, 281, 290:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 254, 262, 267:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

### force · verb

**Türkçe:** zorlamak, mecbur bırakmak

**Bağlam — kaynak s. 257, 259, 267, 280:** Bu ünitede force + object + to + verb yapısıyla birini veya sistemi belirli bir davranışa zorlamak anlamındadır.

> **English:** An incompatible API change can force clients to upgrade.
>
> **Türkçe:** Uyumsuz bir API değişikliği, istemcileri sürüm yükseltmeye zorlayabilir.

**İlişkili sözcükler:** force someone to do something; forced; synonym: compel. İsim olarak forces, örüntü tasarımında çözümü etkileyen etkenlerdir.

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 254, 257, 258, 263, 270:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

### load balancer · noun phrase

**Türkçe:** yük dengeleyici

**Bağlam — kaynak s. 270, 272:** Gelen istekleri uygun servis örnekleri arasında dağıtır.

> **English:** The load balancer selects a service instance.
>
> **Türkçe:** Yük dengeleyici, bir servis örneği seçer.

**İlişkili sözcükler:** load balancing

### loosely coupled · adjective phrase

**Türkçe:** gevşek bağlı

**Bağlam — kaynak s. 264:** Birbirinin iç ayrıntılarına sınırlı ölçüde bağımlı bileşenleri niteler.

> **English:** Loosely coupled teams coordinate less frequently.
>
> **Türkçe:** Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.

**İlişkili sözcükler:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 259, 280:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### monolith · noun

**Türkçe:** monolit; tek dağıtılabilir bütün

**Bağlam — kaynak s. 253:** Kaynakta tek WAR dosyası gibi tek birim olarak paketlenip dağıtılan uygulama.

> **English:** The monolith is packaged as a single WAR file.
>
> **Türkçe:** Monolit, tek bir WAR dosyası olarak paketlenir.

**İlişkili sözcükler:** monolithic; karşılaştırma: independently deployable services. Monolith tek başına kötü tasarım demek değildir.

## O

### observability · noun

**Türkçe:** gözlemlenebilirlik

**Bağlam — kaynak s. 266, 267, 270:** Sistemin iç durumunu log, metric ve trace gibi dış çıktılardan anlayabilmektir.

> **English:** Logs and traces support observability.
>
> **Türkçe:** Log'lar ve iz kayıtları, gözlemlenebilirliği destekler.

**İlişkili sözcükler:** observe, observable, observation; ilişkili: metrics, tracing, logging.

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 268:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 253, 254, 259, 262, 264 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### projection · noun

**Türkçe:** olaylardan türetilen görünüm

**Bağlam — kaynak s. 280:** Olayların sorgulanabilir bir veri modeline uygulanmış halidir.

> **English:** The projection is updated when an event arrives.
>
> **Türkçe:** Görünüm, bir olay geldiğinde güncellenir.

**İlişkili sözcükler:** project; view

## Q

### query · noun / verb

**Türkçe:** sorgu; sorgulamak

**Bağlam — kaynak s. 254, 271, 273, 279, 280 ve devamı:** Bilgi okuma isteğidir; CQRS bağlamında durumu değiştiren command'dan ayrılır.

> **English:** The query returns the order status.
>
> **Türkçe:** Sorgu, siparişin durumunu döndürür.

**İlişkili sözcükler:** read; command

## R

### reliability · noun

**Türkçe:** güvenilirlik

**Bağlam — kaynak s. 266, 267, 270:** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.

> **English:** Frequent failures reduce the reliability of the application.
>
> **Türkçe:** Sık arızalar, uygulamanın güvenilirliğini azaltır.

**İlişkili sözcükler:** reliable, reliably, unreliable; karşılaştırma: availability.

### repository · noun

**Türkçe:** depo; veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 264, 290:** Bağlama göre kaynak kodunun/paketlerin saklandığı depo veya domain nesnelerine erişimi soyutlayan Repository nesnesidir; kullanıldığı cümleye göre ayrılmalıdır.

> **English:** The team publishes the package to a repository.
>
> **Türkçe:** Ekip, paketi bir depoya yayımlar.

**İlişkili sözcükler:** source repository; Maven repository; Repository pattern; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 254, 255, 256, 257, 261 ve devamı:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 259, 260, 262, 263, 264 ve devamı:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### scalability · noun

**Türkçe:** ölçeklenebilirlik

**Bağlam — kaynak s. 268:** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.

> **English:** The scale cube describes different approaches to scalability.
>
> **Türkçe:** Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.

**İlişkili sözcükler:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### service discovery · noun phrase

**Türkçe:** servis keşfi

**Bağlam — kaynak s. 270:** Çağrılabilecek servis örneklerinin ağ konumlarını bulma mekanizmasıdır.

> **English:** Service discovery locates available instances.
>
> **Türkçe:** Servis keşfi, kullanılabilir örneklerin konumunu bulur.

**İlişkili sözcükler:** discover; registry

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 254, 279, 290:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### synchronous · adjective

**Türkçe:** eşzamanlı; yanıtı bekleyen

**Bağlam — kaynak s. 268:** İstek yapan taraf, ilgili yanıtı aynı etkileşimin parçası olarak bekler.

> **English:** A synchronous call waits for a response.
>
> **Türkçe:** Eşzamanlı bir çağrı, yanıtı bekler.

**İlişkili sözcükler:** synchronously; antonym: asynchronous

## T

### technology stack · noun phrase

**Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü

**Bağlam — kaynak s. 265:** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.

> **English:** A service may use a different technology stack.
>
> **Türkçe:** Bir servis farklı bir teknoloji yığını kullanabilir.

**İlişkili sözcükler:** tech stack; ilişkili: framework, language, infrastructure.

### throughput · noun

**Türkçe:** birim zamanda işlenen iş miktarı

**Bağlam — kaynak s. 268:** Sistemin belirli sürede tamamladığı istek veya mesaj sayısını anlatır.

> **English:** Throughput measures completed requests per second.
>
> **Türkçe:** Throughput, saniyede tamamlanan istekleri ölçer.

**İlişkili sözcükler:** processing rate; compare: latency

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 255:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** kullanılabilirlik, hizmete erişilebilir olma durumu

**3.** konteyner

**4.** API erişim noktası

**5.** yük dengeleyici

**6.** ek yük

**7.** depo; veri erişimini soyutlayan nesne

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. availability** — Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.

**3. container** — Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

**4. endpoint** — İstemcinin belirli bir işlev için istek gönderdiği adrestir.

**5. load balancer** — Gelen istekleri uygun servis örnekleri arasında dağıtır.

**6. overhead** — Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

**7. repository** — Bağlama göre kaynak kodunun/paketlerin saklandığı depo veya domain nesnelerine erişimi soyutlayan Repository nesnesidir; kullanıldığı cümleye göre ayrılmalıdır.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
