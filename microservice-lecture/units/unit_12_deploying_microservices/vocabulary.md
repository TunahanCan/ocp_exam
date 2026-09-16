# Ünite 12 · Deploying microservices — Vocabulary

**Amaç:** Bu ünitenin 383–427. kaynak sayfalarındaki teknik terimleri ve YDS açısından yararlı ifadeleri bağlam içinde öğrenmek. Alfabetik kartlarda kaynak sayfa, anlam, sözcük ailesi ve iki dilli örnek bulunur.

[Ana ders](bilingual_notes.md) · [Grammar](grammar_notes.md) · [Vocabulary PDF](vocabulary.pdf)

**Çalışma yöntemi:** Türkçe satırını kapatıp örneği çevirin. Örnekler, bu ünitenin kavramlarını çalıştırmak için yazılmış **özgün çalışma cümleleridir**; kitaptan alıntı değildir. Eş anlamlı ve ilişkili sözcükler her bağlamda birbirinin yerine geçmez.

## A

### address · verb

**Türkçe:** ele almak, çözüm üretmeye çalışmak

**Bağlam — kaynak s. 393, 402, 404, 405, 406 ve devamı:** Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

> **English:** The pattern addresses a data consistency issue.
>
> **Türkçe:** Bu örüntü, bir veri tutarlılığı sorununu ele alır.

**İlişkili sözcükler:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

## B

### benefit · noun / verb

**Türkçe:** yarar; yarar sağlamak

**Bağlam — kaynak s. 383, 388, 389, 390, 392 ve devamı:** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.

> **English:** Independent deployment is a benefit of loose coupling.
>
> **Türkçe:** Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.

**İlişkili sözcükler:** beneficial; noun synonym: advantage; karşıt: drawback.

### broker · noun

**Türkçe:** mesaj aracısı

**Bağlam — kaynak s. 398, 419:** Mesajı gönderen ile alan arasında iletim ve yönlendirme sağlayan bileşendir.

> **English:** The broker routes messages to consumers.
>
> **Türkçe:** Mesaj aracısı, mesajları tüketicilere yönlendirir.

**İlişkili sözcükler:** message broker; messaging

## C

### circuit breaker · noun phrase

**Türkçe:** devre kesici

**Bağlam — kaynak s. 408, 409:** Tekrarlanan başarısızlıklardan sonra çağrıları geçici olarak durduran korumadır.

> **English:** The circuit breaker rejects calls while it is open.
>
> **Türkçe:** Devre kesici, açık durumdayken çağrıları reddeder.

**İlişkili sözcükler:** open; closed; half-open

### constraint · noun

**Türkçe:** kısıt, sınırlayıcı koşul

**Bağlam — kaynak s. 416:** Bir tasarım veya işlemin uyması gereken kısıttır.

> **English:** Past decisions impose constraints on the new design.
>
> **Türkçe:** Geçmiş kararlar, yeni tasarıma kısıtlar getirir.

**İlişkili sözcükler:** constrain, constrained; synonym: restriction, limitation.

### consumer · noun

**Türkçe:** tüketici

**Bağlam — kaynak s. 406, 410, 411, 412, 413 ve devamı:** Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

> **English:** The consumer processes a message.
>
> **Türkçe:** Tüketici, bir mesajı işler.

**İlişkili sözcükler:** consume; producer

### container · noun

**Türkçe:** konteyner

**Bağlam — kaynak s. 383, 384, 385, 386, 387 ve devamı:** Uygulamayı ve bağımlılıklarını süreç yalıtımıyla çalıştıran dağıtım birimidir.

> **English:** The container runs one service instance.
>
> **Türkçe:** Konteyner, bir servis örneğini çalıştırır.

**İlişkili sözcükler:** containerize; container image

### cross-cutting concern · noun phrase

**Türkçe:** birden fazla alanı kesen ortak sorumluluk

**Bağlam — kaynak s. 410:** Birden fazla bileşende ortak biçimde ele alınması gereken sorumluluktur.

> **English:** Configuration is a cross-cutting concern.
>
> **Türkçe:** Yapılandırma, birçok servisi ilgilendiren ortak bir sorumluluktur.

**İlişkili sözcükler:** concern: ilgilenilmesi gereken konu; ilişkili: shared responsibility, infrastructure.

## D

### deploy · verb

**Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek

**Bağlam — kaynak s. 383, 385, 386, 387, 388 ve devamı:** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.

> **English:** The team deploys the service independently.
>
> **Türkçe:** Ekip, servisi bağımsız olarak dağıtır.

**İlişkili sözcükler:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed tracing · noun phrase

**Türkçe:** dağıtık izleme

**Bağlam — kaynak s. 409, 410:** Bir isteğin farklı servisler boyunca izlediği çağrı zincirini kaydeder.

> **English:** Distributed tracing shows where a request spends time.
>
> **Türkçe:** Dağıtık izleme, bir isteğin nerede zaman harcadığını gösterir.

**İlişkili sözcükler:** trace; span

### drawback · noun

**Türkçe:** dezavantaj, olumsuz yön

**Bağlam — kaynak s. 383, 386, 388, 389, 390 ve devamı:** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

> **English:** Operational complexity is a significant drawback.
>
> **Türkçe:** İşletim karmaşıklığı önemli bir dezavantajdır.

**İlişkili sözcükler:** synonym: disadvantage, downside; antonym: benefit, advantage.

## E

### encapsulate · verb

**Türkçe:** kapsüllemek

**Bağlam — kaynak s. 386, 392, 419:** İç ayrıntıları bir sınır arkasında tutup denetimli bir arayüz sunmaktır.

> **English:** The service encapsulates its database.
>
> **Türkçe:** Servis, veritabanını kapsüller.

**İlişkili sözcükler:** encapsulation; encapsulated

### endpoint · noun

**Türkçe:** API erişim noktası

**Bağlam — kaynak s. 396, 403, 404, 405, 417 ve devamı:** İstemcinin belirli bir işlev için istek gönderdiği adrestir.

> **English:** The endpoint accepts a request.
>
> **Türkçe:** Erişim noktası, bir isteği kabul eder.

**İlişkili sözcükler:** route; API

### entity · noun

**Türkçe:** kimliği bulunan alan nesnesi

**Bağlam — kaynak s. 419, 420:** Değerleri değişse de kimliğiyle izlenen nesnedir.

> **English:** An entity has a stable identity.
>
> **Türkçe:** Bir entity, kalıcı bir kimliğe sahiptir.

**İlişkili sözcükler:** identity; compare: value object

## F

### feature · noun

**Türkçe:** özellik, işlev

**Bağlam — kaynak s. 383, 392, 398, 408, 409 ve devamı:** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.

> **English:** The new feature changes two services.
>
> **Türkçe:** Yeni özellik, iki serviste değişiklik yapıyor.

**İlişkili sözcükler:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

**Türkçe:** uygunluk; uymak; uygun

**Bağlam — kaynak s. 419, 426:** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

> **English:** This architecture is a good fit for the application.
>
> **Türkçe:** Bu mimari, uygulama için uygundur.

**İlişkili sözcükler:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

## H

### health check · noun phrase

**Türkçe:** sağlık kontrolü

**Bağlam — kaynak s. 396, 403, 404, 406:** Bir servis örneğinin çalışıp çalışmadığını veya trafik alabilecek durumda olup olmadığını sınar.

> **English:** A health check reports the service's condition.
>
> **Türkçe:** Sağlık kontrolü, servisin durumunu bildirir.

**İlişkili sözcükler:** liveness; readiness

## I

### immutable · adjective

**Türkçe:** oluşturulduktan sonra değiştirilmeyen

**Bağlam — kaynak s. 385:** Nesne veya dağıtım örneği yerinde değiştirilmek yerine yenisiyle değiştirilir.

> **English:** An immutable value cannot be changed in place.
>
> **Türkçe:** Değişmez bir değer, yerinde değiştirilemez.

**İlişkili sözcükler:** immutability; antonym: mutable

### in isolation · prepositional phrase

**Türkçe:** diğerlerinden ayrı olarak, yalıtılmış biçimde

**Bağlam — kaynak s. 398:** Bir nesneyi, bileşeni veya servisi diğerlerinden ayrı olarak inceleme ya da sınama bağlamında kullanılır.

> **English:** The component test checks the service in isolation.
>
> **Türkçe:** Bileşen testi, servisi diğerlerinden ayrı olarak sınar.

**İlişkili sözcükler:** isolate, isolated, isolation; karşılaştırma: test services together.

### isolation · noun

**Türkçe:** yalıtım

**Bağlam — kaynak s. 388, 389, 390, 392, 398:** Dağıtım bağlamında servislerin süreçlerini ve kaynak kullanımını birbirinden ayırmayı anlatır; VM ve container seçenekleri farklı düzeylerde yalıtım sağlar.

> **English:** Process isolation limits interference between services.
>
> **Türkçe:** Süreç yalıtımı, servislerin birbirlerini etkilemesini sınırlar.

**İlişkili sözcükler:** process isolation; resource isolation; fault isolation

## L

### latency · noun

**Türkçe:** gecikme

**Bağlam — kaynak s. 419, 426:** Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

> **English:** Network latency increases response time.
>
> **Türkçe:** Ağ gecikmesi, yanıt süresini artırır.

**İlişkili sözcükler:** response time; compare: throughput

### load balancer · noun phrase

**Türkçe:** yük dengeleyici

**Bağlam — kaynak s. 391, 406:** Gelen istekleri uygun servis örnekleri arasında dağıtır.

> **English:** The load balancer selects a service instance.
>
> **Türkçe:** Yük dengeleyici, bir servis örneği seçer.

**İlişkili sözcükler:** load balancing

## M

### maintain · verb

**Türkçe:** sürdürmek, korumak; bakımını yapmak

**Bağlam — kaynak s. 407:** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmak anlamına gelir.

> **English:** The team maintains the service and its documentation.
>
> **Türkçe:** Ekip, servisin ve dokümantasyonunun bakımını yapar.

**İlişkili sözcükler:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

## O

### observability · noun

**Türkçe:** gözlemlenebilirlik

**Bağlam — kaynak s. 386:** Sistemin iç durumunu log, metric ve trace gibi dış çıktılardan anlayabilmektir.

> **English:** Logs and traces support observability.
>
> **Türkçe:** Log'lar ve iz kayıtları, gözlemlenebilirliği destekler.

**İlişkili sözcükler:** observe, observable, observation; ilişkili: metrics, tracing, logging.

### orchestration · noun

**Türkçe:** orkestrasyon; merkezi koordinasyon

**Bağlam — kaynak s. 386, 390, 392, 393, 398 ve devamı:** Saga adımlarını merkezi bir orchestrator yönlendirir.

> **English:** Orchestration makes the sequence of steps explicit.
>
> **Türkçe:** Orkestrasyon, adımların sırasını açıkça belirler.

**İlişkili sözcükler:** orchestrator; orchestrate

### overhead · noun

**Türkçe:** ek yük

**Bağlam — kaynak s. 388, 389, 392, 393:** Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

> **English:** Remote calls introduce communication overhead.
>
> **Türkçe:** Uzak çağrılar, iletişim ek yükü getirir.

**İlişkili sözcükler:** extra cost; overheads

## P

### pattern · noun

**Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm

**Bağlam — kaynak s. 383, 386, 387, 388, 389 ve devamı:** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.

> **English:** A pattern solves a recurring problem in a particular context.
>
> **Türkçe:** Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.

**İlişkili sözcükler:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

## R

### registry · noun

**Türkçe:** kayıt servisi veya dizini

**Bağlam — kaynak s. 394, 395, 396, 397, 398 ve devamı:** Çalışan servis örneklerinin adresleri gibi bilgileri tutar.

> **English:** The registry stores the locations of service instances.
>
> **Türkçe:** Kayıt servisi, servis örneklerinin konumlarını saklar.

**İlişkili sözcükler:** register; registration

### reliability · noun

**Türkçe:** güvenilirlik

**Bağlam — kaynak s. 427:** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.

> **English:** Frequent failures reduce the reliability of the application.
>
> **Türkçe:** Sık arızalar, uygulamanın güvenilirliğini azaltır.

**İlişkili sözcükler:** reliable, reliably, unreliable; karşılaştırma: availability.

### repository · noun

**Türkçe:** depo; veri erişimini soyutlayan nesne

**Bağlam — kaynak s. 396, 420:** Bağlama göre kaynak kodunun/paketlerin saklandığı depo veya domain nesnelerine erişimi soyutlayan Repository nesnesidir; kullanıldığı cümleye göre ayrılmalıdır.

> **English:** The team publishes the package to a repository.
>
> **Türkçe:** Ekip, paketi bir depoya yayımlar.

**İlişkili sözcükler:** source repository; Maven repository; Repository pattern; persistence

### retrieve · verb

**Türkçe:** alıp getirmek, veriye erişip almak

**Bağlam — kaynak s. 403, 409:** Bir sorgunun farklı servislerdeki verileri elde etmesi.

> **English:** The query retrieves data from two services.
>
> **Türkçe:** Sorgu, iki servisten veri alır.

**İlişkili sözcükler:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### rollback · verb / noun

**Türkçe:** geri almak; geri alma

**Bağlam — kaynak s. 402:** Commit edilmemiş değişiklikleri transaction sınırı içinde geri döndürmektir.

> **English:** The transaction rolls back when the operation fails.
>
> **Türkçe:** İşlem başarısız olduğunda transaction geri alınır.

**İlişkili sözcükler:** roll back; compare: compensation

### rollout · noun

**Türkçe:** devreye alma, kullanıma sunma süreci

**Bağlam — kaynak s. 407:** Yeni sürümün hedef ortama veya kullanıcılara alınması sürecidir; aşamalı olabilir. Rollout plan, bu sürecin adımlarını ve sırasını belirler.

> **English:** The rollout plan specifies the deployment order.
>
> **Türkçe:** Devreye alma planı, dağıtım sırasını belirtir.

**İlişkili sözcükler:** roll out (fiil); ilişkili: deployment plan. Rollback, önceki duruma geri dönüştür.

### routing · noun

**Türkçe:** yönlendirme

**Bağlam — kaynak s. 385, 386, 401, 408, 409 ve devamı:** İsteğin veya mesajın hangi hedefe gönderileceğinin belirlenmesidir.

> **English:** Routing sends the request to the correct service.
>
> **Türkçe:** Yönlendirme, isteği doğru servise gönderir.

**İlişkili sözcükler:** route; router

## S

### serverless · adjective

**Türkçe:** sunucu yönetimi platforma bırakılmış

**Bağlam — kaynak s. 383, 385, 386, 393, 415 ve devamı:** Geliştirici kodu dağıtır; çalıştırma altyapısının önemli bölümü platform tarafından yönetilir.

> **English:** Serverless deployment runs the handler on demand.
>
> **Türkçe:** Serverless dağıtım, işleyiciyi talep üzerine çalıştırır.

**İlişkili sözcükler:** function as a service

### service discovery · noun phrase

**Türkçe:** servis keşfi

**Bağlam — kaynak s. 402, 404, 408:** Çağrılabilecek servis örneklerinin ağ konumlarını bulma mekanizmasıdır.

> **English:** Service discovery locates available instances.
>
> **Türkçe:** Servis keşfi, kullanılabilir örneklerin konumunu bulur.

**İlişkili sözcükler:** discover; registry

### service mesh · noun phrase

**Türkçe:** servisler arası iletişimi yöneten altyapı

**Bağlam — kaynak s. 383, 407, 408, 415, 427:** Trafik yönetimi gibi iletişim görevlerini uygulama kodundan ayırır.

> **English:** A service mesh can manage traffic between services.
>
> **Türkçe:** Bir service mesh, servisler arasındaki trafiği yönetebilir.

**İlişkili sözcükler:** sidecar; proxy

### straightforward · adjective

**Türkçe:** anlaşılır, açık; uygulanması görece kolay

**Bağlam — kaynak s. 407, 410, 418:** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.

> **English:** Deploying a single application is relatively straightforward.
>
> **Türkçe:** Tek bir uygulamayı dağıtmak görece kolaydır.

**İlişkili sözcükler:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

## T

### technology stack · noun phrase

**Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü

**Bağlam — kaynak s. 386, 389, 392, 398:** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.

> **English:** A service may use a different technology stack.
>
> **Türkçe:** Bir servis farklı bir teknoloji yığını kullanabilir.

**İlişkili sözcükler:** tech stack; ilişkili: framework, language, infrastructure.

### trade-off · noun

**Türkçe:** bir kazanım karşılığında başka bir alanda verilen ödün

**Bağlam — kaynak s. 399:** Mimari seçimin yarar ve maliyetlerini birlikte değerlendirmeyi gerektiren denge.

> **English:** The design involves a trade-off between simplicity and flexibility.
>
> **Türkçe:** Tasarım, sadelik ile esneklik arasında bir ödünleşim içerir.

**İlişkili sözcükler:** trade off (fiil); yakın anlamlı: compromise; kalıp: a trade-off between A and B.

## V

### view · noun

**Türkçe:** görünüm

**Bağlam — kaynak s. 385:** Bağlama göre mimari bakış açısı veya sorgulama için düzenlenmiş veri modelidir.

> **English:** The view combines data from several services.
>
> **Türkçe:** Görünüm, birkaç servisten gelen verileri birleştirir.

**İlişkili sözcükler:** materialized view; perspective

## Mini quiz — Özgün çalışma soruları

Aşağıdaki açıklamaların İngilizce karşılıklarını yazın. Cevapları alttaki anahtardan kontrol edin.

**1.** ele almak, çözüm üretmeye çalışmak

**2.** tüketici

**3.** dezavantaj, olumsuz yön

**4.** uygunluk; uymak; uygun

**5.** gecikme

**6.** ek yük

**7.** alıp getirmek, veriye erişip almak

<!-- page-break -->

## Cevap anahtarı

**1. address** — Bir sorunu ele almak veya çözmek için üzerinde çalışmak anlamına gelir.

**2. consumer** — Bağlama göre API'yi kullanan istemci, mesaj alan bileşen veya FTGO müşterisidir.

**3. drawback** — Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.

**4. fit** — Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.

**5. latency** — Bir isteğin gönderilmesi ile yanıt alınması arasındaki süredir.

**6. overhead** — Asıl işi yapmanın yanında gereken zaman, bellek veya yönetim maliyetidir.

**7. retrieve** — Bir sorgunun farklı servislerdeki verileri elde etmesi.

## Kısa tekrar

Bir terimi yalnızca Türkçe karşılığıyla değil, yaptığı işle birlikte hatırlayın. Örnekte özneyi ve fiili bulun; terimin isim mi, fiil mi, yoksa sıfat mı olduğuna bakın. Ardından ana derste verilen kaynak sayfanın paragrafını tekrar okuyun.
