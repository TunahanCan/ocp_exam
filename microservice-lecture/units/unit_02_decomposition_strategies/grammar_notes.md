# Ünite 02 · Decomposition strategies — Grammar Notes

**Amaç:** Kaynak PDF’nin 33–64. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 58):** In contrast, in a microservice architecture, even though each service’s database is consistent, you can’t obtain a globally consistent view of the data.
>
> **Türkçe:** Buna karşılık mikroservis mimarisinde her servisin veritabanı kendi içinde tutarlı olsa bile verilerin bütün sistem genelinde tutarlı bir görünümünü elde edemezsiniz.

> **English — Kaynak örneği (s. 62):** Moreover, even though the term operation suggests some kind of synchronous request/response-based IPC mechanism, you’ll see that asynchronous messaging plays a significant role.
>
> **Türkçe:** Üstelik operation terimi senkron istek/yanıt tabanlı bir IPC mekanizmasını çağrıştırsa da asenkron mesajlaşmanın önemli rol oynadığını göreceksiniz.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 34):** But on the other hand, it leaves several questions unanswered, including how does the microservice architecture relate to the broader concepts of software architecture?
>
> **Türkçe:** Ancak diğer yandan, mikroservis mimarisinin yazılım mimarisinin daha geniş kavramlarıyla nasıl ilişkilendiği de dâhil olmak üzere çeşitli soruları yanıtsız bırakır.

> **English — Kaynak örneği (s. 43):** On the other hand, consider what happens when the requirements change in a way that affects the Order business object.
>
> **Türkçe:** Diğer yandan gereksinimlerin, Order iş nesnesini etkileyecek biçimde değiştiğinde ne olduğunu düşünün.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 35):** This view consists of modules, which represent packaged code, and components, which are executable or deployable units consisting of one or more modules.
>
> **Türkçe:** Bu görünüm, paketlenmiş kodu temsil eden modüllerden ve bir veya daha fazla modülden oluşan çalıştırılabilir ya da dağıtılabilir birimler olan bileşenlerden oluşur.

> **English — Kaynak örneği (s. 58):** If you need to update some data atomically, then it must reside within a single service, which can be an obstacle to decomposition.
>
> **Türkçe:** Bazı verileri atomik olarak güncellemeniz gerekiyorsa bu veriler tek bir servis içinde bulunmalıdır; bu da ayrıştırmaya engel olabilir.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 53):** Having said that, it’s important to remember that the services shown in figure 2.8 are merely the first attempt at defining the architecture.
>
> **Türkçe:** Bununla birlikte Şekil 2.8’deki servislerin, mimariyi tanımlamaya yönelik yalnızca ilk girişim olduğunu hatırlamak önemlidir.

> **Yapı ayrımı:** Bu örnekte reduced relative clause, “the services **shown in figure 2.8**” bölümüdür: services that are shown. Baştaki “Having said that” ise “bununla birlikte” anlamında ayrı bir geçiş kalıbıdır.

> **English — Kaynak örneği (s. 63):** It keeps the replica up-to-date by subscribing to events published by the Restaurant Service whenever it updates its data.
>
> **Türkçe:** Restaurant Service’in verilerini her güncellediğinde yayımladığı olaylara abone olarak replikayı güncel tutar.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 38):** Single presentation layer—It doesn’t represent the fact that an application is likely to be invoked by more than just a single system.
>
> **Türkçe:** Tek sunum katmanı — Uygulamanın yalnızca tek bir sistemden daha fazlası tarafından çağrılmasının olası olduğu gerçeğini yansıtmaz.

> **English — Kaynak örneği (s. 45):** The behavior of each system operation is described in terms of its effect on one or more domain objects and the relationships between them.
>
> **Türkçe:** Her sistem işleminin davranışı, bir veya daha fazla domain nesnesi ve bunlar arasındaki ilişkiler üzerindeki etkisiyle açıklanır.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 56):** The idea is that if two classes change in lockstep because of the same underlying reason, then they belong in the same package.
>
> **Türkçe:** Temel düşünce şudur: İki sınıf aynı temel nedenle birlikte değişiyorsa aynı pakette bulunmalıdır.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 62):** After having assigned operations to services, the next step is to decide how the services collaborate in order to handle each system operation.
>
> **Türkçe:** İşlemleri servislere atadıktan sonraki adım, servislerin her sistem işlemini gerçekleştirmek için nasıl işbirliği yapacağına karar vermektir.

> **English — Kaynak örneği (s. 34):** In order to answer those questions, we need to take a step back and look at what is meant by software architecture.
>
> **Türkçe:** Bu soruları yanıtlamak için bir adım geri çekilip yazılım mimarisiyle ne kastedildiğine bakmalıyız.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 38):** Instead of the presentation layer, the application has one or more inbound adapters that handle requests from the outside by invoking the business logic.
>
> **Türkçe:** Sunum katmanı yerine uygulamada, iş mantığını çağırarak dışarıdan gelen istekleri işleyen bir veya daha fazla inbound adapter (giriş uyarlayıcısı) bulunur.

> **English — Kaynak örneği (s. 57):** Sometimes, you can reduce the latency to an acceptable amount by implementing a batch API for fetching multiple objects in a single round trip.
>
> **Türkçe:** Bazen tek bir ağ gidiş-dönüşünde birden fazla nesneyi getiren bir batch API (toplu işlem API’si) gerçekleştirerek gecikmeyi kabul edilebilir bir düzeye indirebilirsiniz.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 48):** Instead of committing to a specific protocol, therefore, it makes sense to use the more abstract notion of a system operation to represent requests.
>
> **Türkçe:** Bu nedenle belirli bir protokole bağlanmak yerine, istekleri temsil etmek için daha soyut olan sistem işlemi kavramını kullanmak mantıklıdır.

> **English — Kaynak örneği (s. 50):** But with all strategies, the end result is the same: an architecture consisting of services that are primarily organized around business rather than technical concepts.
>
> **Türkçe:** Ancak bütün stratejilerde sonuç aynıdır: öncelikle teknik kavramlar yerine iş kavramları etrafında düzenlenen servislerden oluşan bir mimari.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 42):** Keeping the data private enables a developer to change their service’s database schema without having to spend time coordinating with developers working on other services.
>
> **Türkçe:** Veriyi servise özel tutmak, geliştiricinin diğer servislerde çalışan geliştiricilerle koordinasyona zaman harcamadan kendi servisinin veritabanı şemasını değiştirmesini sağlar.

> **English — Kaynak örneği (s. 43):** Developers often package functionality in a library (module) so that it can be reused by multiple applications without duplicating code.
>
> **Türkçe:** Geliştiriciler, kodu tekrarlamadan birden fazla uygulamada yeniden kullanılabilmesi için işlevleri çoğu zaman bir kütüphanede (modülde) paketler.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 53):** In particular, an important step in the architecture definition process is investigating how the services collaborate in each of the key architectural services.
>
> **Türkçe:** Özellikle mimari tanımlama sürecinin önemli bir adımı, servislerin temel mimari senaryoların her birinde nasıl işbirliği yaptığını araştırmaktır.

> **Kaynak notu:** İngilizce cümlede “key architectural services” yazılıdır. Ana dersteki açıklamayla tutarlı olarak, izleyen işbirliği örneklerine dayanarak “temel mimari senaryolar” anlamı kullanıldı. Bu, kaynak bağlamından yapılan editör çıkarımıdır; [ana ders](bilingual_notes.md) içindeki ilgili notla birlikte okuyun.

> **English — Kaynak örneği (s. 45):** After that, we’ll look at strategies and guidelines for decomposing an application into services, and at obstacles to decomposition and how to address them.
>
> **Türkçe:** Ardından uygulamayı servislere ayırmaya yönelik strateji ve ilkelere, ayrıştırmanın önündeki engellere ve bunların nasıl ele alınacağına bakacağız.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 43):** As a result, it improves the development time attributes—maintainability, testability, deployability, and so on—and enables an organization to develop better software faster.
>
> **Türkçe:** Böylece bakım yapılabilirlik, test edilebilirlik, dağıtılabilirlik gibi geliştirme zamanına ilişkin özellikleri iyileştirir ve kuruluşun daha iyi yazılımı daha hızlı geliştirmesini sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Addition — as well as

**İşlev:** Bir öğeye veya eyleme başka bir öğe ya da eylem ekler: “... yanı sıra”.

> **Formül:** A as well as B; as well as + noun / V-ing

> **English — Kaynak örneği (s. 63):** As well as reliably updating data scattered across multiple services, a saga is also a way to implement a self-contained service.
>
> **Türkçe:** Saga, birden fazla servise dağılmış verileri güvenilir biçimde güncellemenin yanı sıra kendi kendine yeterli bir servis gerçekleştirmenin de yoludur.

> **English — Kaynak örneği (s. 45):** A system operation can create, update, or delete domain objects, as well as create or destroy relationships between them.
>
> **Türkçe:** Bir sistem işlemi, domain nesnelerini oluşturabilir, güncelleyebilir veya silebilir; ayrıca aralarındaki ilişkileri oluşturabilir veya kaldırabilir.

> **YDS ipucu:** As well as burada ekleme yapar; as fast as gibi eşitlik karşılaştırması değildir. İki as sözcüğü görünce yapıyı otomatik olarak karşılaştırma saymayın.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 46):** The application won’t even have a single domain model because, as you’ll soon learn, each service has its own domain model.
>
> **Türkçe:** Uygulamanın tek bir domain modeli bile olmayacaktır; çünkü birazdan öğreneceğiniz gibi her servisin kendi domain modeli vardır.

> **English — Kaynak örneği (s. 52):** I combined the Courier availability management and Delivery management capabilities and mapped them to a single service because they’re deeply intertwined.
>
> **Türkçe:** Kurye müsaitliği yönetimi ile teslimat yönetimi yetkinliklerini, birbirleriyle çok iç içe oldukları için birleştirip tek bir servise eşledim.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 50):** Once the system operations have been defined, the next step is to identify the application’s services.
>
> **Türkçe:** Sistem işlemleri tanımlandıktan sonraki adım, uygulamanın servislerini belirlemektir.

> **English — Kaynak örneği (s. 34):** Traditionally, the goal of architecture has been scalability, reliability, and security.
>
> **Türkçe:** Geleneksel olarak mimarinin hedefi ölçeklenebilirlik, güvenilirlik ve güvenlik olmuştur.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Past perfect — had + V3

**İşlev:** Geçmişteki bir anlatım noktasından daha önce olmuş olayı gösterir.

> **Formül:** S + had + V3

> **English — Kaynak örneği (s. 33):** After an intense lobbying effort, Mary had finally convinced the business that migrating to a microservice architecture was the right thing to do.
>
> **Türkçe:** Mary, yoğun ikna çabalarının ardından iş tarafını mikroservis mimarisine geçmenin doğru karar olduğuna sonunda ikna etmişti.

> **YDS ipucu:** Had tek başına past perfect değildir; had a meeting gibi yapılarda ana fiildir.

## 17. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 42):** Later in chapter 12, when I discuss deployment technologies, you’ll see that the implementation view of a service can take many forms.
>
> **Türkçe:** İleride 12. bölümde dağıtım teknolojilerini ele aldığımda, bir servisin implementation view (gerçekleştirim görünümü) açısından birçok farklı biçim alabileceğini göreceksiniz.

> **English — Kaynak örneği (s. 56):** The goal is that when that business rule changes, developers only need to change code in a small number of packages (ideally only one).
>
> **Türkçe:** Amaç, bu iş kuralı değiştiğinde geliştiricilerin yalnızca az sayıda pakette — ideal olarak tek bir pakette — kod değiştirmesinin yeterli olmasıdır.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 18. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 61):** An application must translate between the user experience, which is its own domain model, and the domain models of each of the services.
>
> **Türkçe:** Uygulama, kendine özgü bir domain modeli olan kullanıcı deneyimi ile servislerin her birinin domain modelleri arasında dönüşüm yapmalıdır.

> **English — Kaynak örneği (s. 42):** The component might be a standalone process, a web application or OSGI bundle running in a container, or a serverless cloud function.
>
> **Türkçe:** Bileşen; bağımsız bir süreç, bir container içinde çalışan web uygulaması veya OSGI bundle’ı ya da serverless bulut fonksiyonu olabilir.

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
