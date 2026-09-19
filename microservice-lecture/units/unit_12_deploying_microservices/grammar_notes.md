# Ünite 12 · Deploying microservices — Grammar Notes

**Amaç:** Kaynak PDF’nin 383–427. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 386):** It’s worthwhile exploring this option, because even though I recommend using one of the other options, its drawbacks motivate the other options.
>
> **Türkçe:** Diğer seçeneklerden birini kullanmanızı önersem de bu seçeneği incelemek yararlıdır; çünkü sakıncaları diğer seçeneklere neden ihtiyaç duyulduğunu açıklar.

> **English — Kaynak örneği (s. 390):** Although you would get some benefit from using the cloud, this approach suffers from the drawbacks described in the preceding section.
>
> **Türkçe:** Bulut kullanmanın bazı yararlarını elde etseniz de bu yaklaşım önceki bölümde açıklanan sakıncaları taşır.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 407):** On the other hand, this approach assumes that once a service version has passed the tests in the staging environment, it will work in production.
>
> **Türkçe:** Diğer yandan bu yaklaşım, staging ortamındaki testleri geçen bir servis sürümünün canlı ortamda da çalışacağını varsayar.

> **English — Kaynak örneği (s. 426):** On the other hand, modern clouds such as Amazon EC2 are highly automated and provide a rich set of features.
>
> **Türkçe:** Diğer yandan Amazon EC2 gibi modern bulutlar büyük ölçüde otomatikleştirilmiştir ve zengin özellikler sağlar.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 417):** For lambda functions that handle HTTP requests that are proxied by an AWS API Gateway, I and O are APIGatewayProxyRequestEvent and APIGatewayProxyResponseEvent, respectively.
>
> **Türkçe:** AWS API Gateway’in proxy olarak ilettiği HTTP isteklerini işleyen lambda function’larda I ve O sırasıyla APIGatewayProxyRequestEvent ve APIGatewayProxyResponseEvent türleridir.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 385):** An application might have tens or hundreds of services written in a variety of languages and frameworks.
>
> **Türkçe:** Bir uygulama, çeşitli diller ve framework’lerle yazılmış onlarca ya da yüzlerce servise sahip olabilir.

> **English — Kaynak örneği (s. 391):** Interestingly, Elastic Beanstalk combines elements of the three deployment patterns described in this chapter.
>
> **Türkçe:** İlginç biçimde Elastic Beanstalk, bu bölümde anlatılan üç dağıtım örüntüsünün öğelerini birleştirir.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 419):** Limited event/request-based programming model—AWS Lambda isn’t intended to be used to deploy long-running services, such as a service that consumes messages from a third-party message broker.
>
> **Türkçe:** Sınırlı olay/istek tabanlı programlama modeli — AWS Lambda, üçüncü taraf mesaj aracısından mesaj tüketen bir servis gibi uzun süre çalışan servisleri dağıtmak amacıyla tasarlanmamıştır.

> **English — Kaynak örneği (s. 395):** It specifies the base container image, a series of instructions for installing software and configuring the container, and the shell command to run when the container is created.
>
> **Türkçe:** Temel container imajını, yazılım kurma ve container’ı yapılandırmaya yönelik talimatları ve container oluşturulduğunda çalıştırılacak shell komutunu belirtir.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 398):** The Docker engine provides some basic management features, such as automatically restarting containers if they crash or if the machine is rebooted.
>
> **Türkçe:** Docker engine, container çöktüğünde veya makine yeniden başlatıldığında container’ları otomatik yeniden başlatmak gibi bazı temel yönetim özellikleri sağlar.

> **English — Kaynak örneği (s. 418):** Otherwise, if it invokes the lambda function asynchronously, the web service response indicates whether the execution of the lambda was successfully initiated.
>
> **Türkçe:** Asenkron çağırırsa web servisinin yanıtı, lambda’nın çalıştırılmasının başarıyla başlatılıp başlatılmadığını belirtir.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 383):** The deployment process consists of the steps that must be performed by people— developers and operations—in order to get software into production.
>
> **Türkçe:** Dağıtım süreci, yazılımı canlı ortama almak için insanların — geliştiricilerin ve operasyon ekibinin — gerçekleştirmesi gereken adımlardan oluşur.

> **English — Kaynak örneği (s. 410):** A pod should have an app label such as app: ftgo-consumer-service, which identifies the service, in order to support Istio distributed tracing.
>
> **Türkçe:** Istio’nun distributed tracing özelliğini desteklemek için pod, servisi tanımlayan app: ftgo-consumer-service gibi bir app label’ına sahip olmalıdır.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 402):** Now that we’ve reviewed the key Kubernetes concepts, let’s see them in action by looking at how to deploy an application service on Kubernetes.
>
> **Türkçe:** Temel Kubernetes kavramlarını gözden geçirdiğimize göre bir uygulama servisinin Kubernetes üzerinde nasıl dağıtılacağını inceleyerek bunları uygulamada görelim.

> **English — Kaynak örneği (s. 404):** Fortunately, we can avoid doing that by using the service discovery mechanism built in to Kubernetes and define a Kubernetes service.
>
> **Türkçe:** Neyse ki Kubernetes’in yerleşik servis keşif mekanizmasını kullanıp bir Kubernetes Service tanımlayarak buna gerek bırakmayabiliriz.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 391):** It deploys the application as VMs, but rather than building an AMI, it uses a base image that installs the application on startup.
>
> **Türkçe:** Uygulamayı VM olarak dağıtır; ancak AMI oluşturmak yerine uygulamayı başlangıç sırasında kuran bir temel imaj kullanır.

> **English — Kaynak örneği (s. 392):** Unlike a Docker orchestration framework, covered later in the chapter, the unit of scaling is the EC2 instance rather than a container.
>
> **Türkçe:** Bölümün ilerleyen kısmında ele alınan Docker orkestrasyon framework’lerinden farklı olarak ölçeklendirme birimi container değil, EC2 instance’ıdır.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 390):** It’s important to assign service instances to machines in a way that uses the machines efficiently without overloading them.
>
> **Türkçe:** Servis örneklerini, makineleri aşırı yüklemeden verimli kullanacak biçimde makinelere atamak önemlidir.

> **English — Kaynak örneği (s. 408):** Deploy the new version into production without routing any end-user requests to it.
>
> **Türkçe:** Yeni sürümü canlı ortama dağıtın, fakat hiçbir son kullanıcı isteğini ona yönlendirmeyin.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 408):** In this section, I show you how to use Istio, a popular, open source service mesh originally developed by Google, IBM, and Lyft.
>
> **Türkçe:** Bu bölümde, ilk olarak Google, IBM ve Lyft tarafından geliştirilen yaygın açık kaynak service mesh Istio’nun nasıl kullanılacağını gösteriyorum.

> **English — Kaynak örneği (s. 399):** Now that we’ve looked at containers and their trade-offs, let’s look at how to deploy the FTGO application’s Restaurant Service using Kubernetes.
>
> **Türkçe:** Container’ları ve getirdikleri ödünleşimleri incelediğimize göre FTGO uygulamasındaki Restaurant Service’in Kubernetes ile nasıl dağıtılacağına bakalım.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

### Whether ile belirsizliği koruma

**İşlev:** Bir işlemin başarıyla sonuçlanıp sonuçlanmadığını açık bırakır. Whether, olumlu bir sonuç garantisi değildir.

> **Formül:** indicate / determine + whether + S + V

> **English — Kaynak örneği (s. 418):** The web service response indicates whether the execution of the lambda was successfully initiated.
>
> **Türkçe:** Web servisinin yanıtı, lambda’nın çalıştırılmasının başarıyla başlatılıp başlatılmadığını belirtir.

> **Common mistake:** “Başarıyla başlatıldığını gösterir” çevirisi whether anlamını siler. Ayrıca başlatılması ile işin başarıyla tamamlanması aynı değildir. 6. ve 11. bölümlerdeki koşul ve dolaylı soru açıklamalarıyla birlikte okuyun.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 397):** That’s because a Docker image has what’s known as a layered file system, which enables Docker to only transfer part of the image over the network.
>
> **Türkçe:** Çünkü Docker imajı, Docker’ın ağ üzerinden yalnızca imajın bir bölümünü aktarmasını sağlayan katmanlı bir dosya sistemine sahiptir.

> **English — Kaynak örneği (s. 404):** As described in chapter 11, a health check endpoint enables Kubernetes to determine the health of the service instance.
>
> **Türkçe:** 11. bölümde açıklandığı gibi health check endpoint’i, Kubernetes’in servis örneğinin sağlığını belirlemesini sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 391):** Elastic Beanstalk is perhaps not quite as fashionable as, say, Kubernetes, but it’s an easy way to deploy a microservices-based application on EC2.
>
> **Türkçe:** Elastic Beanstalk, örneğin Kubernetes kadar gözde olmayabilir; fakat mikroservis tabanlı bir uygulamayı EC2 üzerinde dağıtmak için kolay bir yoldur.

> **English — Kaynak örneği (s. 398):** For example, on my laptop it takes as little as five seconds to package a Spring Boot application as a container image.
>
> **Türkçe:** Örneğin benim dizüstü bilgisayarımda bir Spring Boot uygulamasını container imajı olarak paketlemek beş saniye kadar kısa sürebilir.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 398):** One is that docker run isn’t a reliable way to deploy a service, because it creates a container running on a single machine.
>
> **Türkçe:** Bunlardan biri, docker run’ın tek makinede çalışan bir container oluşturduğu için servisi dağıtmanın güvenilir bir yolu olmamasıdır.

> **English — Kaynak örneği (s. 426):** A serverless deployment isn’t a good fit for every service, because of long-tail latencies and the requirement to use an event/request-based programming model.
>
> **Türkçe:** Gecikme dağılımının uzun kuyruğu ve olay/istek tabanlı programlama modeli kullanma zorunluluğu nedeniyle serverless dağıtım her servis için uygun değildir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 392):** Once a service has been packaged as a virtual machine, it becomes a black box that encapsulates your service’s technology stack.
>
> **Türkçe:** Bir servis sanal makine olarak paketlendiğinde, teknoloji yığınını kapsülleyen bir kara kutuya dönüşür.

> **English — Kaynak örneği (s. 408):** Traditionally, separating deployments and releases in this way has been challenging because it requires a lot of work to implement it.
>
> **Türkçe:** Geleneksel olarak deployment ve release süreçlerini bu şekilde ayırmak zordur; çünkü gerçekleştirmek için çok fazla iş gerekir.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 399):** It endeavors to keep the desired number of instances of each service running at all times, even when service instances or machines crash.
>
> **Türkçe:** Servis örnekleri veya makineler çöktüğünde bile, her servisin istenen sayıda örneğini her zaman çalışır durumda tutmaya çalışır.

> **English — Kaynak örneği (s. 386):** When using this pattern, what’s deployed in production and what’s managed by the service runtime is a service in its language-specific package.
>
> **Türkçe:** Bu örüntüde canlı ortama dağıtılan ve servis çalışma zamanı tarafından yönetilen şey, dile özgü paketi içindeki servistir.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 17. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 426):** Consequently, it may sometimes be easier to deploy a small, simple application using virtual machines than to set up a Docker orchestration framework.
>
> **Türkçe:** Bu nedenle küçük, basit bir uygulamayı sanal makinelerle dağıtmak bazen Docker orkestrasyon framework’ü kurmaktan daha kolay olabilir.

> **English — Kaynak örneği (s. 387):** Sometimes you might deploy a single service instance on a machine, while retaining the option to deploy multiple service instances on the same machine.
>
> **Türkçe:** Bazen bir makineye tek bir servis örneği dağıtırken aynı makineye birden fazla servis örneği dağıtma seçeneğini de korumak isteyebilirsiniz.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 18. Correlative comparison — as many ... as are needed

**İşlev:** İstenen miktarı gereksinimle eşleştirir; sınırsız kaynak garantisi vermez.

> **Formül:** as many + plural noun + as + clause

> **English — Kaynak örneği (s. 418):** AWS Lambda runs as many instances of your application as are needed to handle the load.
>
> **Türkçe:** AWS Lambda, yükü karşılamak için gereken sayıda uygulama örneği çalıştırır.

> **YDS ipucu:** Sayılabilen çoğul isimle many, miktar bildiren sayılamayan isimle much kullanılır. Buradaki as ... as, “gerektiği kadar” ilişkisini verir.

## 19. Neither ... nor — iki seçeneği birlikte dışlama

**İşlev:** İki özne, nesne veya eylem için olumsuzluğu birlikte kurar.

> **Formül:** neither A nor B

> **English — Kaynak örneği (s. 417):** But the notion that neither you as a developer nor anyone in your organization need worry about any aspect of servers, virtual machines, or containers is incredibly powerful.
>
> **Türkçe:** Ancak geliştirici olarak sizin de kuruluşunuzdaki diğer kişilerin de sunucuların, sanal makinelerin veya container’ların hiçbir yönüyle uğraşmak zorunda kalmaması fikri son derece güçlüdür.

> **YDS ipucu:** Buradaki yapı iki grubun da sorumluluğu taşımadığını anlatır. Türkçede daha açık bir alternatif: “Sunucu yönetimiyle ne sizin ne de kuruluşunuzdaki başka birinin uğraşmak zorunda kalmaması fikri çok güçlüdür.” Neither zaten olumsuzluk içerir; otomatik olarak ek not kullanmayın.

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
