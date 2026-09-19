# Ünite 08 · External API patterns — Grammar Notes

**Amaç:** Kaynak PDF’nin 253–291. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 262):** It might provide a RESTful API to external clients, even though the application services use a mixture of protocols internally, including REST and gRPC.
>
> **Türkçe:** Uygulama servisleri içeride REST ve gRPC dahil farklı protokolleri birlikte kullansa da dış istemcilere RESTful API sunabilir.

> **English — Kaynak örneği (s. 268):** For example, it’s the basis of the widely used Java EE servlet framework, although this framework provides the option of completing a request asynchronously.
>
> **Türkçe:** Örneğin yaygın kullanılan Java EE servlet framework'ünün temelidir; ancak bu framework bir isteği asenkron tamamlama seçeneği de sunar.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 258):** On the other hand, JavaScript applications that access the services over the internet have the same problems with network latency as mobile applications.
>
> **Türkçe:** Öte yandan servislere internet üzerinden erişen JavaScript uygulamaları, mobil uygulamalarla aynı ağ gecikmesi sorunlarını yaşar.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 270):** Another way to ensure that an API gateway is reliable is to properly handle failed requests and requests that have unacceptably high latency.
>
> **Türkçe:** API gateway'in güvenilir olmasını sağlamanın başka bir yolu, başarısız istekleri ve gecikmesi kabul edilemeyecek kadar yüksek olan istekleri doğru ele almaktır.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 271):** The AWS API gateway, one of the many services provided by Amazon Web Services, is a service for deploying and managing APIs.
>
> **Türkçe:** Amazon Web Services'in sunduğu birçok servisten biri olan AWS API Gateway, API'leri dağıtmak ve yönetmek için kullanılan bir servistir.

> **English — Kaynak örneği (s. 280):** One way to tailor the data returned by the endpoint, as described in chapter 3, is to give the client the ability to specify the data they need.
>
> **Türkçe:** Bölüm 3'te anlatıldığı gibi endpoint'in döndürdüğü verileri ihtiyaca uyarlamanın bir yolu, istemcinin ihtiyaç duyduğu verileri belirtmesine olanak vermektir.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 281):** The GraphQL-based API gateway, shown in figure 8.10, is written in JavaScript using the NodeJS Express web framework and the Apollo GraphQL server.
>
> **Türkçe:** Şekil 8.10'da gösterilen GraphQL tabanlı API gateway, NodeJS Express web framework'ü ve Apollo GraphQL sunucusu kullanılarak JavaScript ile yazılmıştır.

> **English — Kaynak örneği (s. 288):** Let’s now look at how to integrate the GraphQL engine with a web framework so that it can be invoked by clients.
>
> **Türkçe:** Şimdi GraphQL motorunu, istemcilerin çağırabileceği şekilde bir web framework'üyle nasıl bütünleştireceğimize bakalım.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 258):** Even if the HTML is primarily generated by a server-side web application, it’s common for JavaScript running in the browser to invoke services.
>
> **Türkçe:** HTML büyük ölçüde sunucu tarafındaki web uygulaması tarafından üretilse bile tarayıcıda çalışan JavaScript'in servisleri çağırması yaygındır.

> **English — Kaynak örneği (s. 256):** If the mobile client invokes the services directly, then it must, as figure 8.2 shows, make multiple calls to retrieve this data.
>
> **Türkçe:** Mobil istemci servisleri doğrudan çağırıyorsa Şekil 8.2'nin gösterdiği gibi bu verileri almak için birden fazla çağrı yapmalıdır.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 290):** The makeContextWithDependencies() function would pass the user information to each repository’s constructor so that they can propagate the user information to the services.
>
> **Türkçe:** makeContextWithDependencies() fonksiyonu, kullanıcı bilgisini servislere aktarabilmeleri için bu bilgiyi her repository'nin constructor'ına geçirirdi.

> **English — Kaynak örneği (s. 259):** Section 8.1.1 described the drawbacks of clients, such as the FTGO mobile application, making multiple requests in order to display information to the user.
>
> **Türkçe:** Kısım 8.1.1, FTGO mobil uygulaması gibi istemcilerin kullanıcıya bilgi göstermek için birden fazla istek yapmasının dezavantajlarını anlattı.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 280):** The client retrieves data by executing a query that specifies the required data in terms of the graph’s nodes and their properties and relationships.
>
> **Türkçe:** İstemci, gerekli verileri grafın düğümleri, bu düğümlerin özellikleri ve ilişkileri üzerinden belirten bir sorgu yürüterek verileri alır.

> **English — Kaynak örneği (s. 285):** You associate a GraphQL schema with the data sources by attaching resolver functions to the fields of the object types defined by the schema.
>
> **Türkçe:** Şemanın tanımladığı nesne türlerinin alanlarına resolver fonksiyonları bağlayarak GraphQL şemasını veri kaynaklarıyla ilişkilendirirsiniz.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 259):** Rather than expose services directly to third-party developers, organizations should have a separate public API that’s developed by a separate team.
>
> **Türkçe:** Kuruluşlar, servisleri üçüncü taraf geliştiricilere doğrudan açmak yerine ayrı bir ekip tarafından geliştirilen ayrı bir public API sunmalıdır.

> **English — Kaynak örneği (s. 280):** It’s as if, rather than force clients to retrieve data via stored procedures that you need to write and maintain, you let them execute queries against the underlying database.
>
> **Türkçe:** Bu, istemcileri sizin yazıp bakımını yapmanız gereken stored procedure'ler aracılığıyla veri almaya zorlamak yerine, alttaki veritabanına sorgu göndermelerine izin vermenize benzer.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 278):** As you can see, because getOrderDetails() uses Monos, it concurrently invokes the services and combines the results without using messy, difficult-to-read callbacks.
>
> **Türkçe:** Gördüğünüz gibi getOrderDetails(), Mono nesneleri kullandığından servisleri eşzamanlı çağırır ve karmaşık, okunması zor callback'ler kullanmadan sonuçları birleştirir.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 254):** To learn more about these drawbacks, let’s take a look at how the FTGO mobile application for consumers retrieves data from the services.
>
> **Türkçe:** Bu dezavantajları daha iyi anlamak için müşterilere yönelik FTGO mobil uygulamasının servislerden nasıl veri aldığına bakalım.

> **English — Kaynak örneği (s. 268):** A key design decision that affects performance and scalability is whether the API gateway should use synchronous or asynchronous I/O.
>
> **Türkçe:** Performansı ve ölçeklenebilirliği etkileyen temel bir tasarım kararı, API gateway'in senkron mu asenkron mu I/O kullanması gerektiğidir.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 254):** The lack of encapsulation caused by clients knowing about each service and its API makes it difficult to change the architecture and the APIs.
>
> **Türkçe:** İstemcilerin her servisi ve API'sini bilmesinden kaynaklanan encapsulation eksikliği, mimariyi ve API'leri değiştirmeyi zorlaştırır.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 258):** To make matters worse, browser-based UIs, especially those for the desktop, are usually more sophisticated and need to compose more services than mobile applications.
>
> **Türkçe:** Daha da kötüsü, tarayıcı tabanlı kullanıcı arayüzleri, özellikle masaüstüne yönelik olanlar, genellikle daha gelişmiştir ve mobil uygulamalara göre daha fazla servisin sonuçlarını birleştirmek zorundadır.

> **English — Kaynak örneği (s. 267):** It’s important that the process for updating the API gateway be as lightweight as possible.
>
> **Türkçe:** API gateway'i güncelleme sürecinin mümkün olduğunca hafif olması önemlidir.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

> **Ek yapı — mandative subjunctive:** “It’s important that ... **be** ...” kalıbında gereklilik vurgusu nedeniyle yalın **be** kullanılır; özne tekil olsa bile “is” beklenmez. Temel kalıp: **It is important that + S + V1**. “As lightweight as possible” ise “mümkün olduğunca hafif” anlamındadır.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 263):** As a result, it’s often convenient to use the third option and implement these edge functions, especially authorization, in the API gateway itself.
>
> **Türkçe:** Sonuç olarak üçüncü seçeneği kullanıp bu sınır işlevlerini, özellikle authorization işlemini, doğrudan API gateway içinde uygulamak çoğu zaman uygundur.

> **English — Kaynak örneği (s. 285):** That’s because a query is a field of the Query object, and a query document specifies which of those fields the server should return.
>
> **Türkçe:** Çünkü bir sorgu, Query nesnesinin bir alanıdır ve sorgu belgesi sunucunun bu alanlardan hangilerini döndürmesi gerektiğini belirtir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 269):** The callback accumulates results, and once all of them have been received it sends back the response to the client.
>
> **Türkçe:** Callback sonuçları biriktirir ve hepsi alındığında yanıtı istemciye gönderir.

> **English — Kaynak örneği (s. 270):** An API gateway, like other services in the architecture, must implement the patterns that have been selected for the architecture.
>
> **Türkçe:** API gateway de mimarideki diğer servisler gibi mimari için seçilmiş örüntüleri uygulamalıdır.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 257):** Unlike when updating a server-side application, it takes hours or perhaps even days to roll out a new version of a mobile application.
>
> **Türkçe:** Sunucu tarafındaki uygulamanın güncellenmesinden farklı olarak mobil uygulamanın yeni sürümünü kullanıma sunmak saatler, hatta günler sürebilir.

> **English — Kaynak örneği (s. 270):** The code will be tangled, difficult to understand, and error prone, especially when composition requires a mixture of parallel and sequential requests.
>
> **Türkçe:** Özellikle composition işlemi paralel ve sıralı isteklerin birlikte kullanılmasını gerektiriyorsa kod iç içe geçmiş, anlaşılması zor ve hataya açık olacaktır.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 17. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 284):** These queries may seem not different from the equivalent REST endpoints, but GraphQL gives the client tremendous control over the data that’s returned.
>
> **Türkçe:** Bu sorgular eşdeğer REST endpoint'lerinden farklı görünmeyebilir; ancak GraphQL istemciye döndürülen veriler üzerinde çok geniş denetim sağlar.

> **English — Kaynak örneği (s. 272):** When configuring an Application Load Balancer, you define routing rules that route requests to backend services, which must be running on AWS EC2 instances.
>
> **Türkçe:** Application Load Balancer'ı yapılandırırken istekleri backend servislerine yönlendiren kurallar tanımlarsınız; bu servislerin AWS EC2 instance'larında çalışması gerekir.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 18. Degree — too ... to / enough to

**İşlev:** Too aşırı derece nedeniyle engeli; enough gerekli yeterliliği anlatır.

> **Formül:** too + adjective + to + V1; adjective + enough + to + V1

> **English — Kaynak örneği (s. 291):** It lets you implement an API that’s flexible enough to support a diverse set of clients.
>
> **Türkçe:** Farklı türlerdeki istemcileri destekleyecek kadar esnek bir API uygulamanızı sağlar.

> **English — Kaynak örneği (s. 280):** Consequently, developing a single API that’s flexible enough to support diverse clients becomes feasible.
>
> **Türkçe:** Sonuç olarak farklı türlerdeki istemcileri destekleyecek kadar esnek tek bir API geliştirmek mümkün hale gelir.

> **YDS ipucu:** Enough sıfattan sonra, isimden önce gelir: fast enough; enough memory.

## Mini quiz — Özgün çalışma soruları

Parantez içindeki iki seçenekten uygun olanı seçin.

**1.** The message can ___ twice. (deliver / be delivered)

**2.** The service updates its state ___ applying the event. (by / although)

**3.** ___ the test passes, the pipeline proceeds. (When / Despite)

**4.** The adapter allows the application ___ another service. (call / to call)

**5.** The application runs without ___ the remote service. (contacting / contact)

**6.** The object ___ in this chapter is an example. (described / describes)

<!-- page-break -->

## Cevaplar ve açıklamalar

**1. be delivered.** Mesaj teslim edilir: modal + be + V3. Deliver seçilirse mesajın teslim etme işini kendisinin yaptığı söylenir.

**2. by.** By + -ing yöntem bildirir: olayı uygulayarak. Although ardından özne ve çekimli fiil gerekir.

**3. When.** Ardından tam cümle gelir ve zaman ilişkisi kurulur. Despite isim veya -ing ister.

**4. to call.** Allow + object + to + V1 kullanılır.

**5. contacting.** Without bir edattır; ardından fiil gelecekse -ing biçimi kullanılır.

**6. described.** The object that is described kısaltılmıştır. Describes seçimi ikinci bir bağımsız yüklem oluşturur.

## Kısa tekrar haritası

| İlişki | Aranacak işaret | Okuma sorusu |
|---|---|---|
| Neden | because / because of | Neden gerçekleşiyor? |
| Sonuç | therefore / as a result | Bunun sonucu ne? |
| Koşul | if | Hangi koşulda? |
| Amaç | in order to / so that | Ne amaçla? |
| Yöntem | by + -ing | Nasıl yapılıyor? |
| Niteleme | which / that / V3 | Hangi nesne anlatılıyor? |
| Edilgen | be + V3 | İşlem gören şey ne? |
