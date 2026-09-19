# Ünite 10 · Testing microservices: Part 2 — Grammar Notes

**Amaç:** Kaynak PDF’nin 318–347. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 340):** Despite not being a test class, OrderServiceComponentTestStepDefinitions is still annotated with @ContextConfiguration, which is part of the Spring Testing framework.
>
> **Türkçe:** Test sınıfı olmamasına rağmen OrderServiceComponentTestStepDefinitions, Spring Testing framework'ünün parçası olan @ContextConfiguration ile işaretlenmiştir.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 327):** Each test method invokes a hook method defined by MessagingBase, which is expected to trigger the publication of an event by the service.
>
> **Türkçe:** Her test metodu, MessagingBase'in tanımladığı ve servisin olay yayımlamasını tetiklemesi beklenen bir hook metodunu çağırır.

> **English — Kaynak örneği (s. 340):** This section describes the component tests for Order Service that use the out-of-process strategy to test the service running as a Docker container.
>
> **Türkçe:** Bu kısım, Docker container olarak çalışan servisi sınamak için out-of-process stratejiyi kullanan Order Service component testlerini anlatır.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 3. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 329):** Each test method first invokes Spring Cloud to publish the event defined in the contract and then verifies that OrderHistoryEventHandlers invokes OrderHistoryDao correctly.
>
> **Türkçe:** Her test metodu önce sözleşmede tanımlanan olayı yayımlamak için Spring Cloud'u çağırır, sonra OrderHistoryEventHandlers'ın OrderHistoryDao'yu doğru çağırdığını doğrular.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 4. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 328):** It also defines the methods, such as orderCreated(), which are invoked by the generated tests to trigger the publishing of the event.
>
> **Türkçe:** Ayrıca üretilen testlerin olay yayımlanmasını tetiklemek için çağırdığı orderCreated() gibi metotları tanımlar.

> **English — Kaynak örneği (s. 344):** The verifyEventPublished() method uses the MessageTracker class, a test helper class that records the events that have been published during the test.
>
> **Türkçe:** verifyEventPublished() metodu, test sırasında yayımlanmış olayları kaydeden bir test yardımcı sınıfı olan MessageTracker'ı kullanır.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 5. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 345):** Also, if your test needs to deploy a large number of services, there’s a good chance one of them will fail to deploy, making the tests unreliable.
>
> **Türkçe:** Ayrıca testiniz çok sayıda servis dağıtmak zorundaysa bunlardan birinin dağıtımının başarısız olma olasılığı yüksektir; bu da testleri güvenilmez kılar.

> **English — Kaynak örneği (s. 346):** Imagine if there were hundreds of containers and many more tests.
>
> **Türkçe:** Yüzlerce container ve çok daha fazla test olduğunu düşünün.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 6. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 323):** In order to be confident that API Gateway and Order Service can communicate without using an end-to-end test, we need to write integration tests.
>
> **Türkçe:** End-to-end test kullanmadan API Gateway ile Order Service'in iletişim kurabildiğinden emin olmak için integration testler yazmamız gerekir.

> **English — Kaynak örneği (s. 335):** In order to verify that a service as a whole works, we’ll move up the pyramid and look at how to write component tests.
>
> **Türkçe:** Bir servisin bütün olarak çalıştığını doğrulamak için piramitte yukarı çıkıp component testlerin nasıl yazıldığına bakacağız.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 7. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 320):** Similarly, in section 10.1.3 you’ll see a test that verifies that Order Service publishes correctly structured domain events by testing the OrderDomainEventPublisher class.
>
> **Türkçe:** Benzer biçimde 10.1.3 kısmında OrderDomainEventPublisher sınıfını test ederek Order Service'in doğru yapılandırılmış domain event'ler yayımladığını doğrulayan bir test göreceksiniz.

> **English — Kaynak örneği (s. 340):** Instead, it defines the tests by reading the Gherkin features and uses the OrderServiceComponentTestStepDefinitions class to make them executable.
>
> **Türkçe:** Bunun yerine Gherkin feature'larını okuyarak testleri tanımlar ve bunları yürütülebilir hale getirmek için OrderServiceComponentTestStepDefinitions sınıfını kullanır.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 8. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 345):** For example, rather than test create order, revise order, and cancel order separately, you can write a single test that does all three.
>
> **Türkçe:** Örneğin sipariş oluşturma, değiştirme ve iptal etme işlemlerini ayrı ayrı test etmek yerine üçünü de yapan tek test yazabilirsiniz.

> **English — Kaynak örneği (s. 320):** The benefit of testing only a small number of classes rather than the entire service is that the tests are significantly simpler and faster.
>
> **Türkçe:** Tüm servis yerine az sayıda sınıfı test etmenin yararı, testlerin belirgin biçimde daha basit ve hızlı olmasıdır.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 9. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 320):** Instead, we use a couple of strategies that significantly simplify the tests without impacting their effectiveness.
>
> **Türkçe:** Bunun yerine testlerin etkililiğini azaltmadan onları önemli ölçüde basitleştiren birkaç strateji kullanırız.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 10. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 335):** I begin by briefly describing how to use a testing DSL called Gherkin to write acceptance tests for services, such as Order Service.
>
> **Türkçe:** Order Service gibi servisler için kabul testleri yazmakta Gherkin adlı test DSL'inin nasıl kullanıldığını kısaca anlatarak başlıyorum.

> **English — Kaynak örneği (s. 340):** Now that we’ve looked at how to design component tests, let’s consider how to write component tests for the FTGO Order Service.
>
> **Türkçe:** Component testlerin tasarımına baktığımıza göre şimdi FTGO Order Service için bu testlerin nasıl yazıldığını ele alalım.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 11. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 321):** They use the contracts to configure stubs that simulate the provider, enabling you to write integration tests for a consumer that don’t require a running provider.
>
> **Türkçe:** Sağlayıcıyı taklit eden stub'ları yapılandırmak için sözleşmeleri kullanırlar; böylece çalışan bir sağlayıcı gerektirmeden tüketici için integration test yazabilirsiniz.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 12. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 339):** The drawback is that this type of test is more complex to write, slower to execute, and potentially more brittle than an in-process component test.
>
> **Türkçe:** Dezavantajı, bu tür testin in-process component teste göre daha karmaşık yazılması, daha yavaş çalışması ve daha kırılgan olabilmesidir.

> **English — Kaynak örneği (s. 345):** As I’ve explained, it’s best to write as few of these as possible.
>
> **Türkçe:** Açıkladığım gibi bu testlerden mümkün olduğunca az yazmak en iyisidir.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 13. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 339):** Because Order Service interacts with those services using messaging, these stubs would consume messages from Apache Kafka and send back reply messages.
>
> **Türkçe:** Order Service bu servislerle mesajlaşarak etkileştiği için stub'lar Apache Kafka'dan mesajları alır ve yanıt mesajları gönderir.

> **English — Kaynak örneği (s. 339):** A key benefit of out-of-process component testing is that it improves test coverage, because what’s being tested is much closer to what’s being deployed.
>
> **Türkçe:** Out-of-process component testing'in temel yararı, test edilen şey dağıtıma alınana çok daha yakın olduğu için test kapsamını iyileştirmesidir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

> **Cümle çözümü — what + clause:** “what’s being tested” = “test edilen şey”; “what’s being deployed” = “dağıtıma alınan şey”. What burada soru değil isim cümleciği başlatır. **Is being + V3**, present continuous passive yapısıdır; işlemden etkilenen şeyi öne çıkarır.

## 14. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 323):** The consumer-side OrderServiceProxyTest invokes OrderServiceProxy, which has been configured to make HTTP requests to WireMock.
>
> **Türkçe:** Tüketici tarafındaki OrderServiceProxyTest, WireMock'a HTTP istekleri yapacak şekilde yapılandırılmış OrderServiceProxy'yi çağırır.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 15. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 344):** We can use the Gradle Docker Compose plugin to run the containers before executing the tests and stop the containers once the tests complete:
>
> **Türkçe:** Testlerden önce container'ları çalıştırmak ve testler tamamlandığında durdurmak için Gradle Docker Compose eklentisini kullanabiliriz:

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 16. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 322):** The client must send an HTTP request to the correct endpoint, and the service must send back the response that the client expects.
>
> **Türkçe:** İstemci doğru endpoint'e HTTP isteği göndermeli ve servis de istemcinin beklediği yanıtı döndürmelidir.

> **English — Kaynak örneği (s. 346):** That may not seem like a long time, but this is a relatively simple application with just a handful of containers and tests.
>
> **Türkçe:** Bu uzun bir süre gibi görünmeyebilir; ancak söz konusu uygulama, yalnızca birkaç container ve test içeren görece basit bir uygulamadır.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

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
