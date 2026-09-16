# Ünite 11 · Developing production-ready services — Grammar Notes

**Amaç:** Kaynak PDF’nin 348–382. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 357):** Although the original focus of OAuth 2.0 was authorizing access to public cloud services, you can also use it for authentication and authorization in your application.
>
> **Türkçe:** OAuth 2.0'un orijinal odak noktası kamu bulut servislerine erişimi yetkilendirmek olmasına rağmen, uygulamanızda doğrulama ve yetkililik için de kullanabilirsiniz.

> **English — Kaynak örneği (s. 380):** It also implements client-side service discovery, although the FTGO application relies on the infrastructure for service discovery.
>
> **Türkçe:** Ayrıca, FTGO uygulaması servis keşfi için altyapıya dayanan olsa da, istemci tarafındaki servis keşfi uygulamasını da uyguluyor.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 366):** Similarly, for the Log aggregation pattern, a developer is responsible for ensuring that their services log useful information, whereas operations is responsible for log aggregation.
>
> **Türkçe:** Benzer şekilde, günlük toplama biçimi için, bir geliştiricinin servislerinin yararlı bilgiyi kayıt altına almasını sağlamak sorumluluğu vardır, operasyonlar ise günlük toplama sorumludur.

> **English — Kaynak örneği (s. 351):** In contrast, the Passport framework stores the security context as the user attribute of the request.
>
> **Türkçe:** Öte yandan Passport çerçevesinde güvenlik bağlamı, talebin kullanıcı özelliği olarak kaydedilir.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 357):** As a result, there’s no practical way to revoke an individual JWT that has fallen into the hands of a malicious third party.
>
> **Türkçe:** Sonuç olarak, JWT'ın kötü niyetli bir üçüncü tarafın eline düştüğünü bir bireyi iptal etmek için pratik bir yol yok.

> **English — Kaynak örneği (s. 364):** One challenge of using encryption, though, is that usually the service instance needs to decrypt them, which means it needs the encryption keys.
>
> **Türkçe:** Şifrelemeyi kullanmanın bir zorluğu ise genellikle servis örneğinin onları şifrelemesi gerektiğidir, yani şifreleme anahtarlarına ihtiyacı vardır.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 368):** By using convention over configuration, Spring Boot Actuator implements a sensible set of health checks based on the infrastructure services used by the service.
>
> **Türkçe:** Spring Boot Actuator, konfigürasyon üzerinde konvansiyon kullanılarak, servis tarafından kullanılan altyapı servislerine dayanan mantıklı bir sağlık kontrol kümesi uyguluyor.

> **English — Kaynak örneği (s. 351):** The sequence of events shown in Figure 11.2 is as follows:
>
> **Türkçe:** Resim 11.2'de gösterilen olay sırası şöyle:

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 352):** The login request is handled by LoginHandler, which verifies the credentials, creates the session, and stores information about the principal in the session.
>
> **Türkçe:** Giriş talebi, İttifak bilgileri doğrulayan, oturum oluşturan ve oturumdaki müdürle ilgili bilgileri saklayan LoginHandler tarafından ele alınır.

> **English — Kaynak örneği (s. 357):** In this chapter, I can only provide a brief overview and describe how it can be used in a microservice architecture.
>
> **Türkçe:** Bu bölümde, sadece kısa bir genel bakış verebilirim ve mikroservis mimarisinde nasıl kullanılabileceğini açıklayabilirim.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 366):** The deployment infrastructure periodically invokes this endpoint to determine the health of the service instance and takes the appropriate action if it’s unhealthy.
>
> **Türkçe:** Deployment altyapısı, servis durumunun sağlığını belirlemek için bu son noktayı düzenli olarak kullanır ve sağlıksızsa uygun eylemler görür.

> **English — Kaynak örneği (s. 368):** Similarly, if the service uses the RabbitMQ message broker, it automatically configures a health check that verifies that the RabbitMQ server is up.
>
> **Türkçe:** Benzer şekilde, servis RabbitMQ mesaj aracı kullanırsa, otomatik olarak RabbitMQ sunucusunun çalışmadığını doğrulayan bir sağlık kontrolü yapılandırır.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 349):** In order to make it easier to understand the behavior of your application and troubleshoot problems, you must implement several observability patterns.
>
> **Türkçe:** Uygulamanızın davranışını anlamak ve sorunları çözmek için birkaç gözlemsellik örneğini uygulamanız gerekir.

> **English — Kaynak örneği (s. 364):** What’s more, in order to eliminate duplicate configuration properties, some implementations let you define global defaults, which can be overridden on a per-service basis.
>
> **Türkçe:** Dahası, ikili yapılandırma özelliklerini ortadan kaldırmak için, bazı uygulamalar global öntanımları tanımlamanıza izin verir, bu da servis başına geçersiz kılabilir.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 358):** The API gateway authenticates the API client by making a request to the OAuth 2.0 authorization server, which returns an access token.
>
> **Türkçe:** API geçidi, bir erişim jetonu iade eden OAuth 2.0 yetki sunucusuna bir talep yaparak API istemcisini doğruluyor.

> **English — Kaynak örneği (s. 367):** The health check code can, for example, verify that it’s connected to an RDBMS by obtaining a database connection and executing a test query.
>
> **Türkçe:** Sağlık kontrol kodu, örneğin, bir veritabanı bağlantısı elde ederek ve bir test sorgusunu yürüterek RDBMS ile bağlantılı olduğunu doğrulayabilir.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 370):** The trouble with this option is that it’s an average across requests rather than the timing breakdown for an individual request.
>
> **Türkçe:** Bu seçeneğin sorunu, bireysel bir istek için zaman ayrımı yerine istekler arasında ortalama olmasıdır.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 363):** The deployment infrastructure might not allow you to change the externalized configuration of a running service without restarting it.
>
> **Türkçe:** Deployment altyapısı, çalışmakta olan bir servisin dışlandırılmış yapılandırmasını yeniden başlatmadan değiştirmenize izin vermeyebilir.

> **English — Kaynak örneği (s. 357):** OAuth 2.0 is an authorization protocol that was originally designed to enable a user of a public cloud service, such as GitHub or Google, to grant a third-party application access to its information without revealing its password.
>
> **Türkçe:** OAuth 2.0, başlangıçta GitHub veya Google gibi bir kamu bulut servisinin bir kullanıcısının, üçüncü taraf uygulamalarına şifresini açıklamadan bilgilerine erişim sağlaması için tasarlanmış bir yetki verme protokolüdür.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 370):** You can then see how the services interact during the handling of external requests, including a breakdown of where the time is spent.
>
> **Türkçe:** Daha sonra, servislerin dış taleplerin işlenmesi sırasında nasıl etkileşime girdiğini görebilirsiniz.

> **English — Kaynak örneği (s. 353):** A request handler uses the security context to determine whether to allow a user to perform the requested operation and obtain their identity.
>
> **Türkçe:** Bir istek yöneticisi, bir kullanıcının istekli işlem yapmasına ve kimliğini elde etmesine izin vermeyeceğini belirlemek için güvenlik bağlamını kullanır.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 365):** But there are several patterns that you, as a service developer, must implement to make your service easier to manage and troubleshoot.
>
> **Türkçe:** Ancak bir servis geliştiricisi olarak servisinizi yönetmeyi ve sorunları çözmeyi kolaylaştırmak için uygulamanız gereken birkaç örnektir.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Addition — as well as

**İşlev:** Bir öğeye veya eyleme başka bir öğe ya da eylem ekler: “... yanı sıra”.

> **Formül:** A as well as B; as well as + noun / V-ing

> **English — Kaynak örneği (s. 370):** Examples of logging servers include cloud services, such as AWS CloudWatch Logs, as well as numerous commercial offerings.
>
> **Türkçe:** Kayıtlama sunucularının örnekleri, AWS CloudWatch Logs gibi bulut servislerini ve birçok ticari teklifleri içerir.

> **YDS ipucu:** As well as burada ekleme yapar; as fast as gibi eşitlik karşılaştırması değildir. İki as sözcüğü görünce yapıyı otomatik olarak karşılaştırma saymayın.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 375):** Because this library is on the classpath, Spring Boot exposes a GET /actuator/prometheus endpoint, which returns metrics in the format that Prometheus expects.
>
> **Türkçe:** Bu kütüphanenin sınıf yolunda olduğu için, Spring Boot, Prometheus'un beklediği biçimdeki metrikleri iade eden GET /actuator/prometheus son noktasını ortaya çıkarır.

> **English — Kaynak örneği (s. 366):** But because it may contain sensitive information, some frameworks, such as Spring Boot Actuator, let you configure the level of detail in the health endpoint response.
>
> **Türkçe:** Ancak, hassas bilgileri içerebileceği için, Spring Boot Actuator gibi bazı çerçeveler sağlık son nokta tepkisinde detay seviyesini yapılandırmanıza izin verir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 378):** This chapter has described numerous concerns that a service must implement, including metrics, reporting exceptions to an exception tracker, logging and health checks, externalized configuration, and security.
>
> **Türkçe:** Bu bölüm, bir servisin uygulaması gereken birçok kaygıyı, ölçümleri, istisna izleyicisine istisnaları bildirmek, kayıt ve sağlık kontrolleri, dışlandırılmış yapılandırma ve güvenlik de dahil olmak üzere tanımladı.

> **English — Kaynak örneği (s. 354):** It must also verify that the request has been authenticated.
>
> **Türkçe:** Ayrıca talebin doğrulanmasını da kontrol etmelidir.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Past perfect — had + V3

**İşlev:** Geçmişteki bir anlatım noktasından daha önce olmuş olayı gösterir.

> **Formül:** S + had + V3

> **English — Kaynak örneği (s. 349):** The FTGO team knew that much of what they had learned over the years developing the monolith also applied to microservices.
>
> **Türkçe:** FTGO ekibi, monoliti geliştirmek yılları boyunca öğrendiklerinin çoğunun mikroservislere de uygulanacağını biliyordu.

> **English — Kaynak örneği (s. 349):** The FTGO team had implemented monitoring and logging for the existing application.
>
> **Türkçe:** FTGO ekibi mevcut uygulama için izleme ve kayıt yaptırmıştı.

> **YDS ipucu:** Had tek başına past perfect değildir; had a meeting gibi yapılarda ana fiildir.

## 17. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 370):** It records information (for example, start time and end time) about the tree of service calls that are made when handling a request.
>
> **Türkçe:** Bir istek işlenirken yapılan servis aramaları hakkında bilgi (örneğin başlangıç ve son saatleri) kaydeder.

> **English — Kaynak örneği (s. 366):** It would be pointless for the deployment infrastructure to route HTTP requests to a service instance until it’s ready to process them.
>
> **Türkçe:** Deployment altyapısının HTTP isteklerini işleme hazır olana kadar bir servis örneğine yönlendirmesi anlamsız olurdu.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 18. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 353):** You must, for example, implement a session draining mechanism that waits for all sessions to expire before shutting down an application instance.
>
> **Türkçe:** Örneğin, bir uygulama örneğini kapatmadan önce tüm seansların sona ermesini bekleyen bir oturum boşaltma mekanizmasını uygulamalısınız.

> **English — Kaynak örneği (s. 366):** For example, a bug might cause an instance of Consumer Service to run out of database connections and be unable to access the database.
>
> **Türkçe:** Örneğin, bir hata, Consumer Service'ın bir örneğinin veritabanı bağlantılarının bitmesine ve veritabanına erişemeye neden olabilir.

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
