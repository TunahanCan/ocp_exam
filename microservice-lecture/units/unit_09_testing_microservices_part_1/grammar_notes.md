# Ünite 09 · Testing microservices: Part 1 — Grammar Notes

**Amaç:** Kaynak PDF’nin 292–317. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 303):** That’s because even though the focus of consumer-driven contract testing is to test a provider, contracts are also used to verify that the consumer conforms to the contract.
>
> **Türkçe:** Çünkü tüketici odaklı sözleşme testlerinin odak noktası bir tedarikçiyi test etmek olsa da, sözleşmeler aynı zamanda tüketicinin sözleşmeye uygun olup olmadığını doğrulamak için de kullanılır.

> **English — Kaynak örneği (s. 296):** The terms stubs and mocks are often used interchangeably, although they have slightly different behavior.
>
> **Türkçe:** stub’lar ve mock’lar terimleri genellikle biraz farklı davranışlara sahip olsalar da birbirleriyle değiştirilmektedir.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 297):** Whether the test is business facing or technology facing—A business-facing test is described using the terminology of a domain expert, whereas a technology-facing test is described using the terminology of developers and the implementation.
>
> **Türkçe:** Sınavın iş veya teknolojiye yönelik olup olmadığı - İşle ilgili bir test, alan uzmanının terminolojisini kullanarak tanımlanırken, teknolojiye yönelik bir test geliştiricilerin terminolojisini ve uygulamayı kullanarak tanımlanır.

> **English — Kaynak örneği (s. 299):** In contrast, interprocess communication is central to microservice architecture.
>
> **Türkçe:** Öte yandan, süreçler arası iletişim mikroservis mimarisi için merkezdir.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 305):** As code flows through the pipeline, the test suites subject it to increasingly more thorough testing in environments that are more production like.
>
> **Türkçe:** Kodu boru hattı boyunca akıtırken, test süitleri daha fazla üretime benzer ortamlarda giderek daha kapsamlı testlere maruz kalır.

> **English — Kaynak örneği (s. 293):** It’s the only way to have a short lead time, which is the time it takes to get committed code into production.
>
> **Türkçe:** Sadece kısa bir süreliğine sahip olmanın tek yolu, yani kodun üretime girmesi için gereken zaman.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 317):** And they don’t verify that the RestaurantCreated event processed by OrderEventConsumer has the same structure as the event published by Restaurant Service.
>
> **Türkçe:** RestaurantCreated olayının OrderEventConsumer tarafından işlenmesinin, Restaurant Service tarafından yayınlanan olayın aynı yapıya sahip olduğunu doğrulamıyorlar.

> **English — Kaynak örneği (s. 315):** Order Service, for example, has OrderEventConsumer, which is a message adapter that handles domain events published by other services.
>
> **Türkçe:** Order Service, örneğin, OrderEventConsumer, diğer servisler tarafından yayınlanan alan olaylarını ele alan bir mesaj adaptörüdür.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 309):** Value objects, such as Money, which as described in chapter 5 are objects that are collections of values, are tested using sociable unit tests.
>
> **Türkçe:** 5. bölümde açıklandığı gibi değer nesneleri olan Money gibi değer nesneleri, sosyal birim testleri kullanarak test edilir.

> **English — Kaynak örneği (s. 309):** Entities, such as Order, which as described in chapter 5 are objects with persistent identity, are tested using sociable unit tests.
>
> **Türkçe:** entity’ler, Order gibi, 5. bölümde açıklandığı gibi kalıcı kimliği olan nesneler, sosyal birim testleri kullanarak test edilir.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 301):** A test might also need to invoke complex, high-level functionality such as business logic, even if its goal is to test relatively low-level IPC.
>
> **Türkçe:** Bir testin amacı nispeten düşük düzeyde IPC'yi test etmek olsa bile, iş mantığı gibi karmaşık, yüksek düzeyde işlevsel özelliklere de başvurması gerekebilir.

> **English — Kaynak örneği (s. 307):** If these tests were the compile-time tests for the Order class, you’d waste a lot of time waiting for it to finish.
>
> **Türkçe:** Eğer bu testler Order sınıfı için hazırlama zaman testi olsaydı, bitmesini beklemek için çok zaman harcayacaktın.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 297):** In order to stay in the flow, these tests need to execute quickly—ideally, no more than a few seconds.
>
> **Türkçe:** Bu testler akışta kalmak için hızlı bir şekilde - ideal olarak birkaç saniyeden fazla değil - yapılmalıdır.

> **English — Kaynak örneği (s. 317):** In order to verify that a service properly interacts with other services, we must write integration tests.
>
> **Türkçe:** Bir servisin diğer servislerle düzgün bir şekilde etkileşime girdiğini doğrulamak için entegrasyon testleri yazmalıyız.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 296):** For example, section 9.2.5 shows how to test the OrderController class in isolation by using a test double for the OrderService class.
>
> **Türkçe:** Örneğin, bölüm 9.2.5'de OrderController sınıfını OrderService sınıfı için bir test çiftini kullanarak nasıl izole olarak test edileceğini göstermektedir.

> **English — Kaynak örneği (s. 296):** It wouldn’t be practical to test the OrderController class by running a large portion of the system.
>
> **Türkçe:** OrderController sınıfını sistemin büyük bir kısmını çalıştırarak test etmek pratik olmaz.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 314):** These frameworks enable you to test HTTP request routing and conversion of Java objects to and from JSON without having to make real network calls.
>
> **Türkçe:** Bu çerçeveler, gerçek ağ çağrıları yapmadan Java nesneleri'nin JSON'a ve JSON'a yönlendirilmesini ve dönüştürülmesini test etmenizi sağlar.

> **English — Kaynak örneği (s. 298):** Because we don’t have unlimited budget for development and testing, we want to focus on writing tests that have small scope without compromising the effectiveness of the test suite.
>
> **Türkçe:** Geliştirme ve test için sınırsız bütçemiz olmadığından, test takımının etkinliğini tehlikeye atmadan küçük kapsamlı testler yazmaya odaklanmak istiyoruz.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 10. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 303):** The FTGO application is a Spring framework-based application, so in this chapter I’m going to describe how to use Spring Cloud Contract.
>
> **Türkçe:** FTGO uygulaması Spring Framework tabanlı bir uygulamadır, bu yüzden bu bölümde Spring Cloud Sözleşmesini nasıl kullanacağımı açıklayacağım.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 11. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 305):** It enables API Gateway to be tested without running Order Service.
>
> **Türkçe:** Order Service çalıştırmadan API Gateway'in test edilmesini sağlar.

> **English — Kaynak örneği (s. 314):** These frameworks enable you to test HTTP request routing and conversion of Java objects to and from JSON without having to make real network calls.
>
> **Türkçe:** Bu çerçeveler, gerçek ağ çağrıları yapmadan Java nesneleri'nin JSON'a ve JSON'a yönlendirilmesini ve dönüştürülmesini test etmenizi sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 12. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 297):** Integration tests, as you’ll see in the next chapter, have a relatively small scope, but they’re more complex than pure unit tests.
>
> **Türkçe:** İntegrasyon testleri, sonraki bölümde göreceğiniz gibi, nispeten küçük bir kapsamına sahiptir, ancak saf birim testlerinden daha karmaşıklardır.

> **English — Kaynak örneği (s. 298):** Unreliable tests are almost as bad as no tests, because if you can’t trust a test, you’re likely to ignore failures.
>
> **Türkçe:** Güvenilir olmayan testler neredeyse hiçbir test kadar kötüdür, çünkü eğer bir test'e güvenemezseniz, başarısızlıkları görmezden gelebilirsiniz.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 13. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 310):** You must also write tests for the various scenarios where the saga rolls back because a saga participant sent back a failure message.
>
> **Türkçe:** Ayrıca saga'nin geri döndüğü çeşitli senaryolar için testler yazmalısınız çünkü bir saga katılımcısı bir başarısızlık mesajı gönderdi.

> **English — Kaynak örneği (s. 293):** That’s because we need to verify that services can interact correctly while minimizing the number of slow, complex, and unreliable end-to-end-tests that launch many services.
>
> **Türkçe:** Çünkü servislerin doğru şekilde etkileşime girebildiklerini ve aynı zamanda çok sayıda servis başlatan yavaş, karmaşık ve güvenilir olmayan uçtan son testi sayısını en aza indirerek doğrultmamız gerekiyor.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 14. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 299):** The complexity of testing has moved from the individual services to the interactions between them.
>
> **Türkçe:** Testlerin karmaşıklığı, bireysel servislerden, bunlar arasındaki etkileşime geçmiştir.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 15. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 306):** In such a scenario, the code progresses to the next stage when a tester clicks a button to indicate that it was successful.
>
> **Türkçe:** Böyle bir senaryoda, bir tester başarılı olduğunu göstermek için bir düğmeye tıkladığında kod bir sonraki aşamaya ilerler.

> **English — Kaynak örneği (s. 293):** These strategies enable you to be confident that your software works, while minimizing test complexity and execution time.
>
> **Türkçe:** Bu stratejiler, yazılımınızın çalıştığına güvenmenizi sağlarken test karmaşıklığını ve işleme süresini en aza indirir.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 16. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 294):** After that, I discuss the test pyramid, which describes the relative proportions of the different types of tests that you should write.
>
> **Türkçe:** Bundan sonra, yazmanız gereken farklı test türlerinin nispet oranlarını açıklayan test piramitini tartışacağım.

> **English — Kaynak örneği (s. 298):** The key idea of the test pyramid is that as we move up the pyramid we should write fewer and fewer tests.
>
> **Türkçe:** Test piramitinin temel fikri, piramitten yukarı doğru ilerledikçe daha az test yazmamız gerektiğidir.

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
