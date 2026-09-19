# Ünite 11 · Developing production-ready services — Grammar Notes

**Amaç:** Kaynak PDF’nin 348–382. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

> **Kaynak bağlamı:** OAuth/JWT cümleleri kitabın örnekleridir. OAuth–OpenID Connect ayrımı ve JWT iptalinin sınırları için [ana dersin teknik notlarını](bilingual_notes.md) okuyun. Grammar çözümlemesi kaynak yargısını güncel güvenlik önerisine dönüştürmez.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 357):** Although the original focus of OAuth 2.0 was authorizing access to public cloud services, you can also use it for authentication and authorization in your application.
>
> **Türkçe:** OAuth 2.0 başlangıçta genel bulut servislerine erişimi yetkilendirmeye odaklansa da uygulamanızda kimlik doğrulama ve yetkilendirme için de kullanılabilir.

> **English — Kaynak örneği (s. 380):** It also implements client-side service discovery, although the FTGO application relies on the infrastructure for service discovery.
>
> **Türkçe:** FTGO uygulaması servis keşfi için altyapıya dayansa da bu framework istemci tarafında servis keşfini de gerçekleştirir.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 366):** Similarly, for the Log aggregation pattern, a developer is responsible for ensuring that their services log useful information, whereas operations is responsible for log aggregation.
>
> **Türkçe:** Benzer şekilde Log aggregation örüntüsünde geliştirici, servislerin yararlı bilgiler loglamasından; operasyon ekibi ise logların merkezde toplanmasından sorumludur.

> **English — Kaynak örneği (s. 351):** In contrast, the Passport framework stores the security context as the user attribute of the request.
>
> **Türkçe:** Buna karşılık Passport framework'ü güvenlik bağlamını isteğin user özelliğinde saklar.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 357):** As a result, there’s no practical way to revoke an individual JWT that has fallen into the hands of a malicious third party.
>
> **Türkçe:** Sonuç olarak kötü niyetli bir üçüncü tarafın eline geçmiş tek bir JWT'yi iptal etmenin pratik bir yolu yoktur.

> **English — Kaynak örneği (s. 364):** One challenge of using encryption, though, is that usually the service instance needs to decrypt them, which means it needs the encryption keys.
>
> **Türkçe:** Ancak şifreleme kullanmanın güçlüklerinden biri, genellikle servis örneğinin bu verilerin şifresini çözmesi gerekmesidir; bu da şifreleme anahtarlarına ihtiyaç duyduğu anlamına gelir.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 368):** By using convention over configuration, Spring Boot Actuator implements a sensible set of health checks based on the infrastructure services used by the service.
>
> **Türkçe:** Spring Boot Actuator, yapılandırma yerine yerleşik kabulleri kullanarak servisin yararlandığı altyapı servislerine uygun bir sağlık kontrolü kümesi oluşturur.

> **English — Kaynak örneği (s. 352):** The sequence of events shown in Figure 11.2 is as follows:
>
> **Türkçe:** Şekil 11.2'de gösterilen olay sırası şöyledir:

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 352):** The login request is handled by LoginHandler, which verifies the credentials, creates the session, and stores information about the principal in the session.
>
> **Türkçe:** Oturum açma isteğini işleyen LoginHandler, kimlik bilgilerini doğrular, oturumu oluşturur ve principal hakkındaki bilgileri oturumda saklar.

> **English — Kaynak örneği (s. 357):** In this chapter, I can only provide a brief overview and describe how it can be used in a microservice architecture.
>
> **Türkçe:** Bu bölümde yalnızca kısa bir genel bakış sunabilir ve bunun mikroservis mimarisinde nasıl kullanılabileceğini anlatabilirim.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 366):** The deployment infrastructure periodically invokes this endpoint to determine the health of the service instance and takes the appropriate action if it’s unhealthy.
>
> **Türkçe:** Dağıtım altyapısı, servis örneğinin sağlık durumunu belirlemek için bu uç noktayı düzenli aralıklarla çağırır ve örnek sağlıksızsa uygun işlemi yapar.

> **English — Kaynak örneği (s. 368):** Similarly, if the service uses the RabbitMQ message broker, it automatically configures a health check that verifies that the RabbitMQ server is up.
>
> **Türkçe:** Benzer şekilde servis RabbitMQ mesaj broker'ını kullanıyorsa RabbitMQ sunucusunun çalıştığını doğrulayan sağlık kontrolü otomatik olarak yapılandırılır.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 349):** In order to make it easier to understand the behavior of your application and troubleshoot problems, you must implement several observability patterns.
>
> **Türkçe:** Uygulamanızın davranışını anlamayı ve sorunları gidermeyi kolaylaştırmak için çeşitli gözlemlenebilirlik örüntülerini uygulamalısınız.

> **English — Kaynak örneği (s. 364):** What’s more, in order to eliminate duplicate configuration properties, some implementations let you define global defaults, which can be overridden on a per-service basis.
>
> **Türkçe:** Üstelik yinelenen yapılandırma özelliklerini ortadan kaldırmak için bazı gerçekleştirimler, servis bazında geçersiz kılınabilen genel varsayılanlar tanımlamanıza izin verir.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 358):** The API gateway authenticates the API client by making a request to the OAuth 2.0 authorization server, which returns an access token.
>
> **Türkçe:** API gateway, erişim belirteci döndüren OAuth 2.0 yetkilendirme sunucusuna istek göndererek API istemcisinin kimliğini doğrular.

> **English — Kaynak örneği (s. 367):** The health check code can, for example, verify that it’s connected to an RDBMS by obtaining a database connection and executing a test query.
>
> **Türkçe:** Örneğin sağlık kontrolü kodu, bir veritabanı bağlantısı alıp test sorgusu çalıştırarak RDBMS'e bağlı olduğunu doğrulayabilir.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 370):** The trouble with this option is that it’s an average across requests rather than the timing breakdown for an individual request.
>
> **Türkçe:** Bu seçeneğin sorunu, tek bir istekte zamanın nasıl dağıldığını göstermek yerine istekler genelinde bir ortalama vermesidir.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 363):** The deployment infrastructure might not allow you to change the externalized configuration of a running service without restarting it.
>
> **Türkçe:** Dağıtım altyapısı, çalışan servisi yeniden başlatmadan dış yapılandırmasını değiştirmenize izin vermeyebilir.

> **English — Kaynak örneği (s. 357):** OAuth 2.0 is an authorization protocol that was originally designed to enable a user of a public cloud service, such as GitHub or Google, to grant a third-party application access to its information without revealing its password.
>
> **Türkçe:** OAuth 2.0, başlangıçta GitHub veya Google gibi genel bulut servislerinin kullanıcılarının parolalarını açıklamadan üçüncü taraf uygulamalara kendi bilgilerine erişim izni vermesini sağlamak için tasarlanmış bir yetkilendirme protokolüdür.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 370):** You can then see how the services interact during the handling of external requests, including a breakdown of where the time is spent.
>
> **Türkçe:** Böylece haricî istekler işlenirken servislerin nasıl etkileştiğini, zamanın nerede harcandığının dökümüyle birlikte görebilirsiniz.

> **English — Kaynak örneği (s. 353):** A request handler uses the security context to determine whether to allow a user to perform the requested operation and obtain their identity.
>
> **Türkçe:** Request handler, kullanıcının istenen işlemi yapmasına izin verilip verilmeyeceğini belirlemek ve kimliğini almak için güvenlik bağlamını kullanır.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 365):** But there are several patterns that you, as a service developer, must implement to make your service easier to manage and troubleshoot.
>
> **Türkçe:** Ancak servis geliştirici olarak servisinizi yönetmeyi ve sorunlarını gidermeyi kolaylaştırmak için uygulamanız gereken çeşitli örüntüler vardır.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Addition — as well as

**İşlev:** Bir öğeye veya eyleme başka bir öğe ya da eylem ekler: “... yanı sıra”.

> **Formül:** A as well as B; as well as + noun / V-ing

> **English — Kaynak örneği (s. 370):** Examples of logging servers include cloud services, such as AWS CloudWatch Logs, as well as numerous commercial offerings.
>
> **Türkçe:** Log sunucularına, çok sayıda ticari ürünün yanı sıra AWS CloudWatch Logs gibi bulut servisleri örnek verilebilir.

> **YDS ipucu:** As well as burada ekleme yapar; as fast as gibi eşitlik karşılaştırması değildir. İki as sözcüğü görünce yapıyı otomatik olarak karşılaştırma saymayın.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 375):** Because this library is on the classpath, Spring Boot exposes a GET /actuator/prometheus endpoint, which returns metrics in the format that Prometheus expects.
>
> **Türkçe:** Bu kütüphane classpath'te bulunduğu için Spring Boot, metrikleri Prometheus'un beklediği biçimde döndüren GET /actuator/prometheus uç noktasını sunar.

> **English — Kaynak örneği (s. 367):** But because it may contain sensitive information, some frameworks, such as Spring Boot Actuator, let you configure the level of detail in the health endpoint response.
>
> **Türkçe:** Ancak hassas bilgiler içerebileceğinden Spring Boot Actuator gibi bazı framework'ler sağlık uç noktasının yanıtındaki ayrıntı düzeyini yapılandırmanıza izin verir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 378):** This chapter has described numerous concerns that a service must implement, including metrics, reporting exceptions to an exception tracker, logging and health checks, externalized configuration, and security.
>
> **Türkçe:** Bu bölümde; metrikler, istisnaları takip sistemine bildirme, loglama ve sağlık kontrolleri, dışarıdan yapılandırma ve güvenlik dâhil servisin gerçekleştirmesi gereken çok sayıda ortak gereksinim anlatıldı.

> **English — Kaynak örneği (s. 354):** It must also verify that the request has been authenticated.
>
> **Türkçe:** İsteğin kimliğinin doğrulanmış olduğunu da denetlemelidir.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Past perfect — had + V3

**İşlev:** Geçmişteki bir anlatım noktasından daha önce olmuş olayı gösterir.

> **Formül:** S + had + V3

> **English — Kaynak örneği (s. 349):** The FTGO team knew that much of what they had learned over the years developing the monolith also applied to microservices.
>
> **Türkçe:** FTGO ekibi, monoliti geliştirirken yıllar içinde öğrendiklerinin büyük bölümünün mikroservisler için de geçerli olduğunu biliyordu.

> **English — Kaynak örneği (s. 349):** The FTGO team had implemented monitoring and logging for the existing application.
>
> **Türkçe:** FTGO ekibi mevcut uygulama için izleme ve loglama geliştirmişti.

> **YDS ipucu:** Had tek başına past perfect değildir; had a meeting gibi yapılarda ana fiildir.

## 17. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 370):** It records information (for example, start time and end time) about the tree of service calls that are made when handling a request.
>
> **Türkçe:** Bir istek işlenirken yapılan servis çağrılarının ağacı hakkında başlangıç ve bitiş zamanı gibi bilgileri kaydeder.

> **English — Kaynak örneği (s. 366):** It would be pointless for the deployment infrastructure to route HTTP requests to a service instance until it’s ready to process them.
>
> **Türkçe:** Dağıtım altyapısının HTTP isteklerini, bunları işlemeye hazır olmayan bir servis örneğine yönlendirmesi anlamsız olur.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 18. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 353):** You must, for example, implement a session draining mechanism that waits for all sessions to expire before shutting down an application instance.
>
> **Türkçe:** Örneğin uygulama örneğini kapatmadan önce tüm oturumların süresinin dolmasını bekleyen bir oturum boşaltma mekanizması uygulamalısınız.

> **English — Kaynak örneği (s. 366):** For example, a bug might cause an instance of Consumer Service to run out of database connections and be unable to access the database.
>
> **Türkçe:** Örneğin bir hata, Consumer Service örneğinin veritabanı bağlantılarını tüketmesine ve veritabanına erişememesine yol açabilir.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## Cümle çözümleme — özne ve zamir bağlantısı

**Örnek:** One challenge of using encryption is that the service instance needs to decrypt them, which means it needs the encryption keys.

- **Ana özne:** One challenge of using encryption.
- **Ana yüklem:** is; ardından that ile açıklama gelir.
- **decrypt them:** hassas verilerin şifresini çözmek; encrypt ile ters yöndedir.
- **which means:** tek bir ismi değil, önceki yargının sonucunu açıklar.
- **it:** servis örneğine döner; encryption keys nesnedir.

> **Common mistake:** RabbitMQ server is up → sunucu çalışıyor. Bu olumlu ifadeye Türkçede olumsuzluk eklenmez.

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
