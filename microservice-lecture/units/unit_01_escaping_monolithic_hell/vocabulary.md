# Ünite 1 · Escaping monolithic hell — Vocabulary

Bu sözlük, kaynak kitabın **1–32. sayfalarındaki** mimari, ekip yapısı ve yazılım teslimi bağlamını çalıştırır. Amaç, teknik anlamı koruyarak İngilizce okuma ve YDS kelime becerisini geliştirmektir. Sayfa numaraları kaynak PDF ile aynıdır.

[Çift dilli ana ders](bilingual_notes.md) · [Grammar notları](grammar_notes.md) · [Sözlük PDF](vocabulary.pdf)

**Kullanım:** Önce Türkçe anlamı kapatıp English örneği yorumlayın; sonra bağlam ve ilişkili kelimelerle kontrol edin. Örnek cümleler, aksi belirtilmedikçe bu üniteye uygun **özgün çalışma cümleleridir**. Synonym (eş anlamlı) bilgileri bağlama yakındır; teknik terimler her cümlede birbirinin yerine geçmez.

## A–B

### access token · noun phrase

- **Türkçe:** erişim belirteci
- **Bağlam (s. 28):** API gateway'nin servislere kullanıcıyla ilgili bilgi aktarmasında kullanılan belirteç; kaynak JWT'yi örnek verir.
- **Example:** “The service validates the access token.”
- **Çeviri:** “Servis, erişim belirtecini doğrular.”
- **Related:** access, accessible; ilişkili: identity, authentication, authorization. Authentication kimliği, authorization yetkiyi ilgilendirir.

### address · verb

- **Türkçe:** ele almak, çözüm üretmeye çalışmak
- **Bağlam (s. 17, 19, 21):** “Address an issue” bir tasarım sorunuyla ilgilenmektir; ağ adresi belirtmek değildir.
- **Example:** “The pattern addresses a data consistency issue.”
- **Çeviri:** “Bu örüntü, bir veri tutarlılığı sorununu ele alır.”
- **Related:** synonym: tackle, deal with; karşıt yaklaşım: ignore.

### adopt · verb

- **Türkçe:** benimsemek, kullanmaya başlamak
- **Bağlam (s. 2, 17–19, 31):** Bir mimariyi veya çalışma yöntemini organizasyonun uygulamasına katmak.
- **Example:** “The team plans to adopt continuous delivery.”
- **Çeviri:** “Ekip, continuous delivery yaklaşımını benimsemeyi planlıyor.”
- **Related:** adoption, adopter; synonym: embrace. Adapt ise uyarlamak veya uyum sağlamak demektir.

### agile · adjective

- **Türkçe:** çevik
- **Bağlam (s. 2, 6, 30):** Kısa geri bildirim döngülerine dayalı geliştirme yaklaşımı; yalnızca takımı sprint'lere ayırmak mimari sorunları çözmez.
- **Example:** “Agile practices do not remove every architectural limitation.”
- **Çeviri:** “Çevik uygulamalar, mimarinin bütün sınırlamalarını ortadan kaldırmaz.”
- **Related:** agility; genel synonym: adaptable, nimble; bağlamsal karşılaştırma: waterfall.

### arduous · adjective

- **Türkçe:** zahmetli, güç ve yorucu
- **Bağlam (s. 5–6):** Kod değişikliğini production ortamına ulaştırmanın uzun ve emek isteyen süreci.
- **Example:** “Manual testing makes the release process arduous.”
- **Çeviri:** “Elle test yapılması, sürüm çıkarma sürecini zahmetli hâle getirir.”
- **Related:** synonym: demanding, strenuous; antonym: effortless.

### autonomous · adjective

- **Türkçe:** özerk, kendi kararlarını verebilen
- **Bağlam (s. 14–16, 29–32):** Ekibin kendi servislerini geliştirebilmesi, test edebilmesi ve dağıtabilmesi; tamamen iletişimsiz çalışması anlamına gelmez.
- **Example:** “An autonomous team owns the delivery of its service.”
- **Çeviri:** “Özerk bir ekip, kendi servisinin tesliminden sorumludur.”
- **Related:** autonomy; synonym: self-governing; antonym: dependent.

### availability · noun

- **Türkçe:** kullanılabilirlik, hizmete erişilebilir olma durumu
- **Bağlam (s. 9–10):** Uygulamanın ihtiyaç duyulduğunda istekleri karşılayabilir olması.
- **Example:** “The team monitors the availability of the application.”
- **Çeviri:** “Ekip, uygulamanın kullanılabilirliğini izler.”
- **Related:** available, unavailable; ilişkili: uptime. Reliability ile ilişkili olsa da aynı kavram değildir.

### backward compatible · adjective phrase

- **Türkçe:** geriye dönük uyumlu
- **Bağlam (s. 7):** Yeni sürümün önceki kullanımlarla uyumu; kaynak, framework yükseltme güçlüğünü bu bağlamda tartışır.
- **Example:** “A backward-compatible update preserves existing behavior.”
- **Çeviri:** “Geriye dönük uyumlu bir güncelleme, mevcut davranışı korur.”
- **Related:** backward compatibility, compatible; antonym: incompatible; karşılaştırma: breaking change.

### benefit · noun / verb

- **Türkçe:** yarar; yarar sağlamak
- **Bağlam (s. 4, 14–16, 21):** Bir mimari seçimin veya örüntünün kazandırdığı avantaj.
- **Example:** “Independent deployment is a benefit of loose coupling.”
- **Çeviri:** “Bağımsız dağıtım, gevşek bağlılığın sağladığı yararlardan biridir.”
- **Related:** beneficial; noun synonym: advantage; karşıt: drawback.

### brittle · adjective

- **Türkçe:** kırılgan, değişikliklerden kolayca etkilenen
- **Bağlam (s. 28):** Birçok servisi birlikte çalıştıran end-to-end testlerin bakım ve güvenilirlik sorunları.
- **Example:** “A brittle test may fail after an unrelated change.”
- **Çeviri:** “Kırılgan bir test, ilgisiz bir değişiklikten sonra başarısız olabilir.”
- **Related:** brittleness; synonym: fragile; antonym: robust.

### business capability · noun phrase

- **Türkçe:** iş yetkinliği; işletmenin yapabildiği iş
- **Bağlam (s. 13, 24, 29):** Servis sınırlarının sipariş yönetimi gibi iş alanlarına göre belirlenmesinde kullanılan kavram.
- **Example:** “Order management is a business capability.”
- **Çeviri:** “Sipariş yönetimi bir iş yetkinliğidir.”
- **Related:** capable, capability; genel synonym: ability. Buradaki capability, tek bir teknik metot değildir.

### by leaps and bounds · idiomatic phrase

- **Türkçe:** çok hızlı, büyük sıçramalarla
- **Bağlam (s. 2):** FTGO'nun kuruluşundan sonraki hızlı büyümesi.
- **Example:** “The business grew by leaps and bounds.”
- **Çeviri:** “İşletme çok hızlı büyüdü.”
- **Related:** synonym: rapidly, dramatically; karşıt: slowly, gradually.

> **Memory tip:** **Adopt** bir yaklaşımı benimsemektir; **adapt** onu koşullara uyarlamaktır. “Adopt microservices” ve “adapt the organization” aynı işi anlatmaz.

## C–D

### code base · noun phrase

- **Türkçe:** kod tabanı
- **Bağlam (s. 4–6, 15):** Bir uygulama veya servisin üzerinde çalışılan kaynak kod bütünü.
- **Example:** “Several teams modify the same code base.”
- **Çeviri:** “Birden fazla ekip aynı kod tabanını değiştiriyor.”
- **Related:** yaygın yazım: codebase; ilişkili: source code, repository. Repository kodun tutulduğu yerdir.

### communication overhead · noun phrase

- **Türkçe:** iletişimden doğan ek yük
- **Bağlam (s. 5, 29–30):** Büyüyen ekiplerde bilgi paylaşımı ve karar eşgüdümü için harcanan ek zaman ve emek.
- **Example:** “Large teams may face high communication overhead.”
- **Çeviri:** “Büyük ekipler yüksek iletişim yüküyle karşılaşabilir.”
- **Related:** ilişkili: coordination cost, management overhead. Overhead burada genel gider veya ek maliyettir.

### constraint · noun

- **Türkçe:** kısıt, sınırlayıcı koşul
- **Bağlam (s. 17):** Geçmiş teknoloji seçimlerinin yeni dil ve framework seçeneklerini sınırlaması; kaynakta constrain fiili de kullanılır.
- **Example:** “Past decisions impose constraints on the new design.”
- **Çeviri:** “Geçmiş kararlar, yeni tasarıma kısıtlar getirir.”
- **Related:** constrain, constrained; synonym: restriction, limitation.

### continuous delivery · noun phrase

- **Türkçe:** sürekli teslim
- **Bağlam (s. 15, 30–31):** Yazılımın güvenli ve sürdürülebilir biçimde her an yayımlanabilir durumda tutulması.
- **Example:** “Continuous delivery keeps the software releasable.”
- **Çeviri:** “Sürekli teslim, yazılımı yayımlanabilir durumda tutar.”
- **Related:** deliver, delivery, releasable; karşılaştırma: continuous deployment.

### continuous deployment · noun phrase

- **Türkçe:** sürekli dağıtım
- **Bağlam (s. 6, 15, 30–31):** Yayımlanmaya hazır kodun otomatik biçimde production ortamına dağıtılması.
- **Example:** “Continuous deployment automatically deploys releasable code.”
- **Çeviri:** “Sürekli dağıtım, yayımlanmaya hazır kodu otomatik olarak dağıtır.”
- **Related:** deploy, deployment, deployable; temel fark: delivery hazır tutar, deployment otomatik dağıtır.

### coordination · noun

- **Türkçe:** eşgüdüm, koordinasyon
- **Bağlam (s. 5, 18):** Birden fazla ekibin veya servisin değişiklik sırasını ve ortak çalışmasını düzenlemek.
- **Example:** “This feature requires coordination between three teams.”
- **Çeviri:** “Bu özellik, üç ekip arasında koordinasyon gerektiriyor.”
- **Related:** coordinate, coordinator; synonym: collaboration yakın anlamlıdır, ancak birlikte çalışma yönünü vurgular.

### cross-cutting concern · noun phrase

- **Türkçe:** birden fazla alanı kesen ortak sorumluluk
- **Bağlam (s. 28):** Yapılandırma ve observability gibi birçok servisin ele alması gereken ortak konular.
- **Example:** “Configuration is a cross-cutting concern.”
- **Çeviri:** “Yapılandırma, birçok servisi ilgilendiren ortak bir sorumluluktur.”
- **Related:** concern: ilgilenilmesi gereken konu; ilişkili: shared responsibility, infrastructure.

### cross-functional · adjective

- **Türkçe:** farklı uzmanlıkları bir araya getiren
- **Bağlam (s. 29, 31):** Geliştirme, test ve dağıtım için gerekli becerileri kendi içinde bulunduran ekip.
- **Example:** “A cross-functional team can develop and test its service.”
- **Çeviri:** “Farklı uzmanlıkları bir araya getiren bir ekip, servisini geliştirip test edebilir.”
- **Related:** yakın anlamlı: multidisciplinary; karşılaştırma: function-specific team.

### data consistency · noun phrase

- **Türkçe:** veri tutarlılığı
- **Bağlam (s. 17, 25–26):** Farklı servislerdeki verilerin iş kuralları bakımından uyumlu tutulması; saga bu sorunla ilişkilendirilir.
- **Example:** “The application must maintain data consistency across services.”
- **Çeviri:** “Uygulama, servisler arasında veri tutarlılığını korumalıdır.”
- **Related:** consistent, inconsistent, consistency; karşıt: inconsistency.

### decompose · verb

- **Türkçe:** bileşenlere ayırmak, ayrıştırmak
- **Bağlam (s. 10–13, 17, 24):** Uygulamayı belirli sorumluluklara sahip servislere bölmek.
- **Example:** “The architects decompose the application into services.”
- **Çeviri:** “Mimarlar, uygulamayı servislere ayırır.”
- **Related:** decomposition; synonym: break down, split; yapı: decompose X into Y.

### deploy · verb

- **Türkçe:** dağıtmak; yazılımı çalışacağı ortama yerleştirmek
- **Bağlam (s. 4–6, 18, 26–27):** Uygulama veya servisi hedef ortamda çalıştırılabilir hâle getirmek.
- **Example:** “The team deploys the service independently.”
- **Çeviri:** “Ekip, servisi bağımsız olarak dağıtır.”
- **Related:** deployment, deployable, redeploy. Release bağlama göre kullanıcılara sunmayı vurgulayabilir; her kullanımda bire bir eş değildir.

### distributed system · noun phrase

- **Türkçe:** dağıtık sistem
- **Bağlam (s. 17–18, 24):** Bileşenleri süreçler arası iletişimle işbirliği yapan sistem; iletişim ve kısmi arıza ek karmaşıklık getirir.
- **Example:** “A distributed system must handle partial failures.”
- **Çeviri:** “Dağıtık bir sistem, kısmi arızaları ele almalıdır.”
- **Related:** distribute, distribution; ilişkili: remote call, interprocess communication.

### drawback · noun

- **Türkçe:** dezavantaj, olumsuz yön
- **Bağlam (s. 17–19, 21):** Bir çözümü seçmenin beraberinde getirdiği güçlük veya sınırlama.
- **Example:** “Operational complexity is a significant drawback.”
- **Çeviri:** “İşletim karmaşıklığı önemli bir dezavantajdır.”
- **Related:** synonym: disadvantage, downside; antonym: benefit, advantage.

> **Common mistake:** **Continuous delivery** ile **continuous deployment** aynı ifade değildir. Kaynakta birincisi kodu yayımlanabilir tutar; ikincisi hazır kodu otomatik olarak production ortamına dağıtır.

## E–I

### elusive · adjective

- **Türkçe:** ulaşılması veya elde edilmesi güç
- **Bağlam (s. 2):** Mary'nin konferansta duyduğu gelişmiş çalışma yöntemlerinin günlük sorunlar arasında erişilmez görünmesi.
- **Example:** “Rapid delivery remained an elusive goal.”
- **Çeviri:** “Hızlı teslim, ulaşılması güç bir hedef olarak kaldı.”
- **Related:** elude; synonym: hard to attain; karşıt: attainable.

### encapsulate · verb

- **Türkçe:** kapsüllemek; ayrıntıları bir sınırın arkasında toplamak
- **Bağlam (s. 20, 27):** Strategy pattern içinde algoritmayı veya dağıtım biçiminde teknoloji yığınını kapsüllemek.
- **Example:** “The strategy encapsulates the overdraft algorithm.”
- **Çeviri:** “Strateji, kredili hesap algoritmasını kapsüller.”
- **Related:** encapsulation; ilişkili: hide implementation details. Genel dilde kısa biçimde özetlemek anlamı da vardır.

### fault isolation · noun phrase

- **Türkçe:** arıza yalıtımı
- **Bağlam (s. 6, 16):** Bir bileşendeki arızanın diğer bileşenlere etkisini sınırlama özelliği.
- **Example:** “Fault isolation limits the impact of a failing component.”
- **Çeviri:** “Arıza yalıtımı, arızalanan bir bileşenin etkisini sınırlar.”
- **Related:** fault, faulty, isolate, isolation; ilişkili: containment. Servislerin ayrılması bütün arıza yayılımını kendiliğinden engellemez.

### feature · noun

- **Türkçe:** özellik, işlev
- **Bağlam (s. 2, 15, 18):** Kullanıcıya veya işletmeye değer sağlayan uygulama yeteneği; bir özellik birden çok servise yayılabilir.
- **Example:** “The new feature changes two services.”
- **Çeviri:** “Yeni özellik, iki serviste değişiklik yapıyor.”
- **Related:** feature-rich; yakın anlamlı: functionality. Feature branch, belirli bir özellik için açılan geliştirme dalıdır.

### fit · noun / verb / adjective

- **Türkçe:** uygunluk; uymak; uygun
- **Bağlam (s. 5, 19, 23):** Bir mimarinin uygulamanın ihtiyaçlarına uyma derecesi.
- **Example:** “This architecture is a good fit for the application.”
- **Çeviri:** “Bu mimari, uygulama için uygundur.”
- **Related:** suitable, appropriate; karşıt: unsuitable; kalıp: a good fit for.

### force · noun

- **Türkçe:** tasarımı etkileyen gereksinim, kısıt veya etken
- **Bağlam (s. 21):** Pattern açıklamasında birlikte değerlendirilmesi gereken, bazen çatışan tasarım meseleleri.
- **Example:** “Readability and performance can be competing forces.”
- **Çeviri:** “Okunabilirlik ve performans, birbiriyle yarışan tasarım etkenleri olabilir.”
- **Related:** ilişkili: consideration, requirement, constraint. Burada fiziksel kuvvet anlamı kullanılmaz.

### in isolation · prepositional phrase

- **Türkçe:** diğerlerinden ayrı olarak, yalıtılmış biçimde
- **Bağlam (s. 28):** Bir servisi diğer servisleri birlikte çalıştırmadan test etme bağlamı.
- **Example:** “The component test checks the service in isolation.”
- **Çeviri:** “Bileşen testi, servisi diğerlerinden ayrı olarak sınar.”
- **Related:** isolate, isolated, isolation; karşılaştırma: test services together.

### in jeopardy · prepositional phrase

- **Türkçe:** tehlikede, risk altında
- **Bağlam (s. 2):** Geciken özellikler nedeniyle FTGO'nun yurtdışına genişleme planlarının riske girmesi.
- **Example:** “Release delays put the expansion plan in jeopardy.”
- **Çeviri:** “Sürüm gecikmeleri, genişleme planını tehlikeye atar.”
- **Related:** jeopardize; synonym: at risk; antonym: safe, secure.

### independently deployable · adjective phrase

- **Türkçe:** bağımsız olarak dağıtılabilir
- **Bağlam (s. 14–15, 32):** Bir servisin dağıtımının bütün uygulamanın birlikte dağıtılmasını gerektirmemesi.
- **Example:** “The architecture aims for independently deployable services.”
- **Çeviri:** “Mimari, bağımsız olarak dağıtılabilen servisler hedefler.”
- **Related:** independent, independence, deployment; karşılaştırma: services that must be deployed together.

### interprocess communication · noun phrase

- **Türkçe:** süreçler arası iletişim
- **Bağlam (s. 7, 17, 24):** Ayrı süreçlerde çalışan servislerin istek veya mesaj alışverişi; kısaltması IPC'dir.
- **Example:** “Services use interprocess communication to collaborate.”
- **Çeviri:** “Servisler, işbirliği yapmak için süreçler arası iletişim kullanır.”
- **Related:** process, communicate, communication; karşılaştırma: local method call.

## L–O

### latency · noun

- **Türkçe:** gecikme, yanıt için bekleme süresi
- **Bağlam (s. 17, 27):** Uzak servis iletişiminde ve isteklerin izlenmesinde değerlendirilmesi gereken gecikme.
- **Example:** “High latency makes remote calls slow.”
- **Çeviri:** “Yüksek gecikme, uzak çağrıları yavaşlatır.”
- **Related:** low-latency; yakın anlamlı: delay. Throughput, birim zamanda işlenen iş miktarıdır; latency ile aynı ölçüm değildir.

### lead time · noun phrase

- **Türkçe:** teslim süresi; değişikliğin dağıtıma ulaşma süresi
- **Bağlam (s. 31):** Kaynakta kod değişikliğinin kaydedilmesinden dağıtılmasına kadar geçen süre.
- **Example:** “Long test queues increase lead time.”
- **Çeviri:** “Uzun test kuyrukları, değişikliğin dağıtıma ulaşma süresini artırır.”
- **Related:** ilişkili: deployment frequency, delivery time. Burada projenin bütün yaşam süresi kastedilmez.

### loosely coupled · adjective phrase

- **Türkçe:** gevşek bağlı
- **Bağlam (s. 12, 16, 25, 30):** Bir bileşendeki değişikliğin diğer bileşenleri birlikte değiştirmeyi daha az gerektirdiği ilişki.
- **Example:** “Loosely coupled teams coordinate less frequently.”
- **Çeviri:** “Gevşek bağlı ekipler, daha seyrek koordinasyon kurar.”
- **Related:** loose coupling; antonym: tightly coupled. Gevşek bağlılık, hiçbir bağımlılık bulunmaması demek değildir.

### maintain · verb

- **Türkçe:** sürdürmek, korumak; bakımını yapmak
- **Bağlam (s. 5, 8, 17):** “Maintain data consistency” tutarlılığı korumak; “maintain an application” uygulamanın bakımını yapmaktır.
- **Example:** “The team maintains the service and its documentation.”
- **Çeviri:** “Ekip, servisin ve dokümantasyonunun bakımını yapar.”
- **Related:** maintenance, maintainable, maintainability; bağlamsal synonym: preserve, keep.

### memory leak · noun phrase

- **Türkçe:** bellek sızıntısı
- **Bağlam (s. 6, 16):** Kaynak, bir modüldeki bellek sorununun ortak process veya ayrı servisler üzerindeki etkisini karşılaştırır.
- **Example:** “A memory leak can exhaust the process's memory.”
- **Çeviri:** “Bellek sızıntısı, sürecin belleğini tüketebilir.”
- **Related:** leak, leakage; ilişkili: memory consumption, resource exhaustion.

### modularity · noun

- **Türkçe:** modülerlik
- **Bağlam (s. 8, 11–13):** Sistemin anlaşılabilir sorumluluklara ve korunabilir bileşen sınırlarına ayrılması.
- **Example:** “Clear API boundaries help preserve modularity.”
- **Çeviri:** “Açık API sınırları, modülerliği korumaya yardımcı olur.”
- **Related:** module, modular, modularize; ilişkili: separation of concerns.

### monolith · noun

- **Türkçe:** monolit; tek dağıtılabilir bütün
- **Bağlam (s. 2–6, 32):** Kaynakta tek WAR dosyası gibi tek birim olarak paketlenip dağıtılan uygulama.
- **Example:** “The monolith is packaged as a single WAR file.”
- **Çeviri:** “Monolit, tek bir WAR dosyası olarak paketlenir.”
- **Related:** monolithic; karşılaştırma: independently deployable services. Monolith tek başına kötü tasarım demek değildir.

### observability · noun

- **Türkçe:** gözlemlenebilirlik
- **Bağlam (s. 27–28):** Çalışan uygulamanın davranışını anlamayı ve sorunları teşhis etmeyi destekleyen özellikler.
- **Example:** “Logs and traces support observability.”
- **Çeviri:** “Log'lar ve iz kayıtları, gözlemlenebilirliği destekler.”
- **Related:** observe, observable, observation; ilişkili: metrics, tracing, logging.

### obsolete · adjective

- **Türkçe:** eskimiş, kullanım veya ihtiyaç bakımından geride kalmış
- **Bağlam (s. 6–7):** Değiştirilmesi güç eski teknoloji yığınının giderek güncelliğini kaybetmesi.
- **Example:** “The application depends on an obsolete framework.”
- **Çeviri:** “Uygulama, eskimiş bir framework'e bağımlıdır.”
- **Related:** obsolescence; synonym: outdated, out-of-date; karşıt: up-to-date.

### outage · noun

- **Türkçe:** hizmet kesintisi
- **Bağlam (s. 6, 31):** Uygulamanın production ortamında hizmet veremediği olay veya süre.
- **Example:** “The production outage affected every customer.”
- **Çeviri:** “Production ortamındaki hizmet kesintisi bütün müşterileri etkiledi.”
- **Related:** service interruption, downtime; karşılaştırma: recovery, restoration.

### outgrow · verb

- **Türkçe:** büyüyerek mevcut sınırları aşmak
- **Bağlam (s. 4, 7):** Başlangıçta uygun olan mimarinin, büyüyen uygulama ve ekibin ihtiyaçlarına yetmemesi.
- **Example:** “The application has outgrown its original architecture.”
- **Çeviri:** “Uygulama, büyüyerek başlangıçtaki mimarisinin sınırlarını aşmıştır.”
- **Related:** outgrew, outgrown; yakın anlamlı: grow beyond. Kalıp: outgrow an architecture.

### overlook · verb

- **Türkçe:** gözden kaçırmak, yeterince dikkate almamak
- **Bağlam (s. 19, 21):** Bir teknolojinin savunulurken dezavantajlarının veya bağlamının ihmal edilmesi.
- **Example:** “The proposal overlooks the cost of coordination.”
- **Çeviri:** “Öneri, koordinasyon maliyetini gözden kaçırıyor.”
- **Related:** synonym: miss, fail to notice; karşıt: notice, take into account.

> **Memory tip:** **Outage** hizmetin kesilmesi, **latency** yanıtın gecikmesidir. Servis yanıt veriyor ama yavaş çalışıyorsa bu durum otomatik olarak outage değildir.

## P–R

### pattern · noun

- **Türkçe:** örüntü; belirli bağlamda tekrarlanabilir çözüm
- **Bağlam (s. 20–21):** Problem, bağlam ve sonuçları birlikte açıklanan yeniden kullanılabilir tasarım bilgisi.
- **Example:** “A pattern solves a recurring problem in a particular context.”
- **Çeviri:** “Bir örüntü, belirli bir bağlamda tekrarlanan bir problemi çözer.”
- **Related:** design pattern, architectural pattern; ilişkili: reusable solution. Her bağlam için tek reçete değildir.

### pattern language · noun phrase

- **Türkçe:** örüntü dili
- **Bağlam (s. 20, 22–28):** Bir alandaki sorunları birlikte ele alan, ilişkili örüntüler bütünü.
- **Example:** “The pattern language connects related design decisions.”
- **Çeviri:** “Örüntü dili, birbiriyle ilişkili tasarım kararlarını bağlar.”
- **Related:** related patterns, predecessor, successor; language burada programlama dili anlamında değildir.

### predecessor · noun

- **Türkçe:** öncül
- **Bağlam (s. 21–22):** Bir örüntüye duyulan ihtiyacı ortaya çıkaran, önce uygulanmış örüntü.
- **Example:** “The predecessor pattern creates a need for another solution.”
- **Çeviri:** “Öncül örüntü, başka bir çözüme ihtiyaç doğurur.”
- **Related:** precede, preceding; karşıt ilişki: successor.

### recover · verb

- **Türkçe:** toparlanmak, yeniden çalışır duruma gelmek
- **Bağlam (s. 31):** Production sorunundan sonra hizmetin yeniden işler duruma gelmesi.
- **Example:** “The team works to recover from the outage.”
- **Çeviri:** “Ekip, hizmet kesintisinin ardından sistemi yeniden çalışır duruma getirmek için uğraşır.”
- **Related:** recovery, recoverable; kalıp: recover from; ilişkili: restore service.

### refactor · verb

- **Türkçe:** yapısını yeniden düzenlemek
- **Bağlam (s. 7, 18, 29):** Kaynakta monoliti servislere veya büyük ekibi küçük ekiplere dönüştürmek için yapıyı yeniden düzenlemek.
- **Example:** “The architects plan to refactor the monolith into services.”
- **Çeviri:** “Mimarlar, monoliti servisler biçiminde yeniden düzenlemeyi planlıyor.”
- **Related:** refactoring; ilişkili: restructure. Bu kitap bağlamındaki mimari dönüşüm, tek bir kod temizliği işleminden geniştir.

### reliability · noun

- **Türkçe:** güvenilirlik
- **Bağlam (s. 6, 24–25):** Uygulamanın veya servis iletişiminin beklenen işi güvenilir biçimde gerçekleştirmesi.
- **Example:** “Frequent failures reduce the reliability of the application.”
- **Çeviri:** “Sık arızalar, uygulamanın güvenilirliğini azaltır.”
- **Related:** reliable, reliably, unreliable; karşılaştırma: availability.

### resulting context · noun phrase

- **Türkçe:** çözüm uygulandıktan sonra oluşan bağlam
- **Bağlam (s. 21):** Bir örüntünün yararlarını, dezavantajlarını ve doğurduğu yeni meseleleri birlikte açıklayan bölüm.
- **Example:** “The resulting context includes benefits and new problems.”
- **Çeviri:** “Ortaya çıkan bağlam, yararları ve yeni problemleri içerir.”
- **Related:** result, consequence, outcome; resulting: sonuç olarak ortaya çıkan.

### retrieve · verb

- **Türkçe:** alıp getirmek, veriye erişip almak
- **Bağlam (s. 17, 26):** Bir sorgunun farklı servislerdeki verileri elde etmesi.
- **Example:** “The query retrieves data from two services.”
- **Çeviri:** “Sorgu, iki servisten veri alır.”
- **Related:** retrieval, retrievable; synonym: fetch, obtain; karşılaştırma: store.

### rollout · noun

- **Türkçe:** devreye alma, kullanıma sunma süreci
- **Bağlam (s. 18):** Servis bağımlılıklarını dikkate alarak dağıtımların sırasını belirleyen rollout plan.
- **Example:** “The rollout plan specifies the deployment order.”
- **Çeviri:** “Devreye alma planı, dağıtım sırasını belirtir.”
- **Related:** roll out (fiil); ilişkili: deployment plan. Rollback, önceki duruma geri dönüştür.

## S–V

### scalability · noun

- **Türkçe:** ölçeklenebilirlik
- **Bağlam (s. 8–11, 16, 30):** Yük veya organizasyon büyüdüğünde kapasiteyi artırabilme yeteneği.
- **Example:** “The scale cube describes different approaches to scalability.”
- **Çeviri:** “Scale cube, ölçeklenebilirliğe yönelik farklı yaklaşımları açıklar.”
- **Related:** scale, scalable, scaling; ilişkili: horizontal scaling, partitioning.

### silver bullet · idiomatic noun phrase

- **Türkçe:** bütün sorunları çözeceği sanılan sihirli çözüm
- **Bağlam (s. 17, 19, 32):** Microservice mimarisinin her uygulama için kusursuz çözüm olmadığını vurgulayan benzetme.
- **Example:** “No architecture is a silver bullet.”
- **Çeviri:** “Hiçbir mimari, bütün sorunları çözen sihirli bir çözüm değildir.”
- **Related:** synonym: magic solution, panacea; kalıp: no silver bullet.

### span · verb

- **Türkçe:** birden fazla alanı kapsamak, yayılmak
- **Bağlam (s. 17–18):** Bir özelliğin, transaction'ın veya sorgunun birden çok servisi ilgilendirmesi.
- **Example:** “The transaction spans several services.”
- **Çeviri:** “Transaction, birkaç servisi kapsar.”
- **Related:** spans, spanning; synonym: extend across, cover.

### state-of-the-art · adjective

- **Türkçe:** en ileri düzeydeki, dönemin en gelişmiş
- **Bağlam (s. 2, 5):** Anlatıda ileri yazılım geliştirme uygulamalarına verilen nitelik; değerlendirme kaynağın yazıldığı döneme aittir.
- **Example:** “The conference introduced state-of-the-art development practices.”
- **Çeviri:** “Konferans, dönemin en gelişmiş yazılım geliştirme uygulamalarını tanıttı.”
- **Related:** synonym: cutting-edge, advanced; karşıt: outdated. İsim kullanımı: the state of the art.

### straightforward · adjective

- **Türkçe:** anlaşılır, açık; uygulanması görece kolay
- **Bağlam (s. 4, 26–27):** Test, dağıtım veya istek işleme adımlarının kolay takip edilebilir olması.
- **Example:** “Deploying a single application is relatively straightforward.”
- **Çeviri:** “Tek bir uygulamayı dağıtmak görece kolaydır.”
- **Related:** straightforwardly; synonym: uncomplicated, clear; antonym: complicated.

### successor · noun

- **Türkçe:** ardıl
- **Bağlam (s. 21–22):** Başka bir örüntünün doğurduğu sorunu çözmek için uygulanan örüntü.
- **Example:** “A successor pattern addresses an issue created by its predecessor.”
- **Çeviri:** “Ardıl bir örüntü, öncülünün ortaya çıkardığı bir sorunu ele alır.”
- **Related:** succeed, succeeding, succession; karşıt ilişki: predecessor. Buradaki succeed, ardından gelmek anlamındadır.

### sustainable · adjective

- **Türkçe:** sürdürülebilir
- **Bağlam (s. 30):** Yazılımı güvenli ve hızlı teslim etmenin zaman içinde devam ettirilebilir olması.
- **Example:** “The team needs a sustainable delivery process.”
- **Çeviri:** “Ekibin sürdürülebilir bir teslim sürecine ihtiyacı var.”
- **Related:** sustain, sustainability; antonym: unsustainable.

### take into account · verb phrase

- **Türkçe:** hesaba katmak, dikkate almak
- **Bağlam (s. 30, 32):** Organizasyon yapısı veya çalışanların geçiş sürecindeki duyguları gibi etkenleri değerlendirmeye katmak.
- **Example:** “The migration plan must take team structure into account.”
- **Çeviri:** “Geçiş planı, ekip yapısını hesaba katmalıdır.”
- **Related:** synonym: consider, allow for; karşıt: overlook, disregard.

### technology stack · noun phrase

- **Türkçe:** teknoloji yığını; birlikte kullanılan teknolojiler bütünü
- **Bağlam (s. 6–7, 14, 16–17):** Uygulamanın dili, framework'leri ve ilgili altyapı teknolojilerinin bütünü.
- **Example:** “A service may use a different technology stack.”
- **Çeviri:** “Bir servis farklı bir teknoloji yığını kullanabilir.”
- **Related:** tech stack; ilişkili: framework, language, infrastructure.

### trade-off · noun

- **Türkçe:** bir kazanım karşılığında başka bir alanda verilen ödün
- **Bağlam (s. 19, 21):** Mimari seçimin yarar ve maliyetlerini birlikte değerlendirmeyi gerektiren denge.
- **Example:** “The design involves a trade-off between simplicity and flexibility.”
- **Çeviri:** “Tasarım, sadelik ile esneklik arasında bir ödünleşim içerir.”
- **Related:** trade off (fiil); yakın anlamlı: compromise; kalıp: a trade-off between A and B.

### transition · noun / verb

- **Türkçe:** geçiş, değişime uyum süreci; geçiş yapmak
- **Bağlam (s. 31–32):** Mimari değişimin yanında insanların yeni çalışma biçimine uyum sağlaması.
- **Example:** “People need support during the transition.”
- **Çeviri:** “İnsanlar, geçiş sürecinde desteğe ihtiyaç duyar.”
- **Related:** transitional; ilişkili: change, adaptation. Kaynak, dış değişiklik ile ona verilen duygusal yanıtı ayırır.

### viable · adjective

- **Türkçe:** uygulanabilir, işleyebilir
- **Bağlam (s. 25):** Bir teknik seçeneğin ele alınan koşullarda kullanışlı ve sürdürülebilir bir çözüm olup olmaması.
- **Example:** “The team must find a viable way to maintain consistency.”
- **Çeviri:** “Ekip, tutarlılığı korumanın uygulanabilir bir yolunu bulmalıdır.”
- **Related:** viability; synonym: feasible, workable; antonym: unviable, impractical.

> **Memory tip:** **Predecessor → successor** ilişkisini “ilk kararın doğurduğu ihtiyaç → o ihtiyacı ele alan çözüm” olarak hatırlayın. İki seçenek aynı probleme alternatif çözüm getiriyorsa ilişki farklıdır.

## Mini quiz — Özgün çalışma soruları

**A. Boşluğu uygun sözcükle tamamlayın.** Her sözcük bir kez kullanılacak: **arduous, drawback, outgrown, retrieve, span, trade-off**.

1. The application has ______ its original architecture.
2. A query may need to ______ data from several services.
3. Some business operations ______ multiple services.
4. A long manual release process can be ______.
5. There is a ______ between simplicity and flexibility.
6. Operational complexity is a ______ of the architecture.

**B. Doğru karşılaştırmayı seçin.** Her sorunun tek doğru cevabı vardır.

**7.** Yazılımı sürekli yayımlanabilir durumda tutmak hangi ifadeyle anlatılır? A) continuous delivery B) communication overhead C) memory leak

**8.** “Address the issue” ne demektir? A) Sorunun ağ adresini yazmak B) Sorunu ele almak C) Sorunu saklamak

**9.** Hangi çift birbirine karşılık gelen örüntü ilişkisini belirtir? A) latency / outage B) predecessor / successor C) feature / repository

**10.** “Take emotions into account” ifadesinin anlamı nedir? A) Duyguları gözden kaçırmak B) Duyguları hesaba katmak C) Duyguları kaldırmak


## Cevaplar ve kısa açıklamalar

1. **outgrown** — “Has + V3” gereklidir; uygulama önceki sınırları aşmıştır.
2. **retrieve** — Sorgu veriyi alıp getirir.
3. **span** — İşlem birden fazla servisi kapsar.
4. **arduous** — Sürecin zahmetli olduğunu niteler.
5. **trade-off** — İki nitelik arasında verilen ödünü anlatır.
6. **drawback** — Olumsuz yön veya dezavantajdır.
7. **A** — Continuous delivery kodu hazır tutar. B ek iletişim yükünü, C bellek sorununu anlatır.
8. **B** — Address fiilinin sorunlarla kullanımıdır. A farklı bir isim anlamına dayanır; C metnin tersini söyler.
9. **B** — Öncül ve ardıl ilişkisi. A farklı işletim kavramlarıdır; C özellik ile kod deposunu eşler.
10. **B** — Kalıp “dikkate almak”tır. A overlook'e yakındır; C bu kalıbın anlamı değildir.

## Kısa tekrar

- Mimariyi tartışırken **benefit, drawback, trade-off** birlikte düşünülür.
- Servis sınırlarında **modularity, loose coupling, independently deployable** anahtar kavramlardır.
- İşletimde **availability, reliability, latency, outage** farklı sorulara cevap verir.
- Dönüşüm **architecture, organization, process** boyutlarını ve insanların **transition** sürecini kapsar.
- Cümle yapılarının ayrıntıları için [grammar notlarına](grammar_notes.md), terimlerin özgün okuma bağlamı için [ana derse](bilingual_notes.md) dönün.
