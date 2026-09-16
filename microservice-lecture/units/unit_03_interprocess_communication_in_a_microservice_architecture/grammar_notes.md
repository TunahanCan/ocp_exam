# Ünite 03 · Interprocess communication in a microservice architecture — Grammar Notes

**Amaç:** Kaynak PDF’nin 65–109. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 76):** Despite these drawbacks, REST seems to be the de facto standard for APIs, though there are a couple of interesting alternatives.
>
> **Türkçe:** Bu dezavantajlara rağmen, REST, API'ler için gerçek standart gibi görünüyor, ancak birkaç ilginç alternatif vardır.

> **English — Kaynak örneği (s. 100):** One approach is to use the message broker’s client library, although there are several problems with using such a library directly:
>
> **Türkçe:** Bir yaklaşım, mesaj aracı'nın istemci kütüphanesini kullanmaktır, ancak bu kütüphanenin doğrudan kullanılması için birkaç sorun vardır:

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 66):** In contrast, as you saw in chapter 2, the microservice architecture structures an application as a set of services.
>
> **Türkçe:** Öte yandan, 2. bölümde gördüğünüz gibi, mikroservis mimarisi bir uygulamayı bir dizi servis olarak yapılandırır.

> **English — Kaynak örneği (s. 83):** Application-level service discovery using Eureka, for example, works across both environments, whereas Kubernetes-based service discovery only works within Kubernetes.
>
> **Türkçe:** Örneğin Eureka'yı kullanan uygulama düzeyinde servis keşfi, her iki ortamda da çalışırken, Kubernetes tabanlı servis keşfi sadece Kubernetes içinde çalışır.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 68):** As described in chapter 2, a service’s API consists of operations, which clients can invoke, and events, which are published by the service.
>
> **Türkçe:** Bölüm 2'de açıklandığı gibi, bir servisin API'si, istemcilerin çağırabileceği işlemlerden ve servis tarafından yayınlanan olaylardan oluşur.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 99):** This approach can be used to publish messages written to an OUTBOX table in an RDBMS or messages appended to records in a NoSQL database.
>
> **Türkçe:** Bu yaklaşım OUTBOX tablosuna yazılmış mesajları RDBMS'de veya NoSQL veritabanındaki kayıtlara eklenmiş mesajları yayınlamak için kullanılabilir.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 104):** Mathematically speaking, the availability of a system operation is the product of the availability of the services that are invoked by that operation.
>
> **Türkçe:** Matematik açıdan bir sistem operasyonunun kullanılabilirliği, bu işlem tarafından talep edilen servislerin kullanılabilirliğinin ürünüdür.

> **English — Kaynak örneği (s. 85):** One drawback of platform-provided service discovery is that it only supports the discovery of services that have been deployed using the platform.
>
> **Türkçe:** Platform sağlanan servis keşfinin bir dezavantajı, yalnızca platform kullanılarak dağıtılmış servislerin keşfini desteklemesidir.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 70):** If you’re implementing a REST API, you can, as mentioned below, use the major version as the first element of the URL path.
>
> **Türkçe:** REST API uygulamaya koyulursanız, aşağıda belirtildiği gibi, URL yolunun ilk elementi olarak ana versiyonu kullanabilirsiniz.

> **English — Kaynak örneği (s. 68):** Moreover, because Java is a statically typed language, if the interface changes to be incompatible with the client, the application won’t compile.
>
> **Türkçe:** Dahası, Java statik bir dil olduğundan, arayüz istemciyle uyumsuz hale gelirse, uygulama birleştirilmez.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 66):** Finally, I go through the concept of self-contained services that handle synchronous requests without communicating with other services in order to improve availability.
>
> **Türkçe:** Son olarak, erişilebilirliği artırmak için diğer servislerle iletişim kurmadan eşzamanlı istekleri ele alan bağımsız servisler kavramını inceledim.

> **English — Kaynak örneği (s. 80):** In order to make a request, your code needs to know the network location (IP address and port) of a service instance.
>
> **Türkçe:** Bir istek yapmak için, kodunuz bir servis örneğinin ağ konumunu (IP adresi ve portu) bilmelidir.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 97):** As part of the database transaction that creates, updates, and deletes business objects, the service sends messages by inserting them into the OUTBOX table.
>
> **Türkçe:** İşleme nesneleri oluşturan, güncelleyen ve silen veritabanı işleminin bir parçası olarak, servis mesajları OUTBOX tabloya ekleyerek gönderir.

> **English — Kaynak örneği (s. 79):** For example, chapter 7 describes how the API gateway could implement the findOrder() query operation by using the API composition pattern.
>
> **Türkçe:** Örneğin, bölüm 7 API kapısı API kompozisyon örneğini kullanarak findOrder() sorgu operasyonunu nasıl uygulayabileceğini açıklar.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 97):** Another option is for a message handler to record message ids in an application table instead of a dedicated table.
>
> **Türkçe:** Başka bir seçenek, mesaj işleyicisi için özel bir tablo yerine bir uygulama tablosunda mesaj kimliklerini kaydetmektir.

> **English — Kaynak örneği (s. 98):** That’s because rather than querying an OUTBOX table, the application must query the business entities, and that may or may not be possible to do efficiently.
>
> **Türkçe:** Çünkü bir OUTBOX tablosunu sormak yerine, uygulama iş entity’ler'i sormalıdır ve bu verimli bir şekilde yapılması mümkün olmayabilir.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 105):** This would enable Order Service to handle a request to create an order without having to interact with those services.
>
> **Türkçe:** Bu, Order Service'ın bu servislerle etkileşime girmeden sipariş oluşturma talebini ele almasını sağlar.

> **English — Kaynak örneği (s. 104):** Fortunately, there are ways to handle synchronous requests without making synchronous requests.
>
> **Türkçe:** Neyse ki, eşzamanlı istekleri yapmadan eşzamanlı istekleri ele alma yolları vardır.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 74):** Consequently, a common problem when designing a REST API is how to enable the client to retrieve multiple related objects in a single request.
>
> **Türkçe:** Sonuç olarak, REST API'si tasarlanırken yaygın bir sorun, istemcinin birden fazla ilgili nesneyi tek bir talepte nasıl geri almasını sağlamak.

> **English — Kaynak örneği (s. 75):** Another common REST API design problem is how to map the operations you want to perform on a business object to an HTTP verb.
>
> **Türkçe:** Diğer yaygın REST API tasarım sorunu, bir işletme nesnesinde yapmak istediğiniz işlemleri HTTP fiiline nasıl eşleme yapacağınızdır.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 71):** This format enables a consumer of a message to pick out the values of interest and ignore the rest.
>
> **Türkçe:** Bu biçim, bir mesajın tüketicisinin ilgi çekici değerleri seçmesini ve geri kalanı görmezden gelmesini sağlar.

> **English — Kaynak örneği (s. 76):** As a result, gRPC enables APIs to evolve while remaining backward-compatible.
>
> **Türkçe:** Sonuç olarak, gRPC, API'lerin geriye doğru uyumlu kalırken gelişmesini sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Addition — as well as

**İşlev:** Bir öğeye veya eyleme başka bir öğe ya da eylem ekler: “... yanı sıra”.

> **Formül:** A as well as B; as well as + noun / V-ing

> **English — Kaynak örneği (s. 100):** That’s why I created the Eventuate Tram framework, which provides the messaging APIs as well as transaction tailing and polling.
>
> **Türkçe:** Bu yüzden Eventuate Tram çerçevesini yarattım, mesajlaşma API'lerini yanı sıra işlem takip ve anketleri sağlayan.

> **English — Kaynak örneği (s. 71):** As well as being useful documentation, a JSON schema can be used by an application to validate incoming messages.
>
> **Türkçe:** Bir JSON şeması yararlı bir belge olmaktan başka, gelen mesajları doğrulamak için bir uygulama tarafından kullanılabilir.

> **YDS ipucu:** As well as burada ekleme yapar; as fast as gibi eşitlik karşılaştırması değildir. İki as sözcüğü görünce yapıyı otomatik olarak karşılaştırma saymayın.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 94):** Because of delays due to network issues or garbage collections, messages might be processed out of order, which would result in strange behavior.
>
> **Türkçe:** Ağ sorunları veya çöp toplamaları nedeniyle gecikmeler nedeniyle, mesajlar düzensiz olarak işlenebilir, bu da garip davranışlara neden olabilir.

> **English — Kaynak örneği (s. 75):** Because the client and service communicate directly without an intermediary to buffer messages, they must both be running for the duration of the exchange.
>
> **Türkçe:** istemci ve servis, tampon mesajlarını bir aracı olmadan doğrudan iletişim kurduğu için, ikisinin de değişimin süresi boyunca çalışması gerekir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 108):** After the Order has been validated, Order Service completes the rest of the order-creation process, discussed in the next chapter.
>
> **Türkçe:** Order onaylandıktan sonra, Order Service, sonraki bölümde tartışılan sipariş oluşturma sürecinin geri kalanını tamamlar.

> **English — Kaynak örneği (s. 79):** If the limit has been reached, it’s probably pointless to make additional requests, and those attempts should fail immediately.
>
> **Türkçe:** Eğer bu limit ulaştıysa, daha fazla talep yapmak muhtemelen anlamsızdır ve bu girişimler hemen başarısız olmalıdır.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 95):** The message broker will deliver the unacknowledged message again, either to that client when it restarts or to another replica of the client.
>
> **Türkçe:** Mesaj aracı, onaylanmamış mesajı tekrar, yeniden başlatıldığında ya da istemcinin başka bir kopyasına teslim edecektir.

> **English — Kaynak örneği (s. 106):** One way to solve that problem is for a service to delay interacting with other services until after it responds to its client.
>
> **Türkçe:** Bu sorunu çözmenin bir yolu, bir servisin diğer servislerle etkileşimi istemcisine cevap verdikten sonra geciktirmesi.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 17. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 103):** The problem with REST, though, is that it’s a synchronous protocol: an HTTP client must wait for the service to send a response.
>
> **Türkçe:** REST'in sorunu ise senkron bir protokol olmasıdır: HTTP istemcisi, servisin bir yanıt göndermesini beklemek zorunda.

> **English — Kaynak örneği (s. 70):** In order for this to be painless, clients and services must use a request and response format that supports the Robustness principle.
>
> **Türkçe:** Bu durum ağrısız olması için, istemciler ve servisler dayanıklılık ilkesini destekleyen bir talep ve yanıt biçimi kullanmalıdır.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 18. Degree — too ... to / enough to

**İşlev:** Too aşırı derece nedeniyle engeli; enough gerekli yeterliliği anlatır.

> **Formül:** too + adjective + to + V1; adjective + enough + to + V1

> **English — Kaynak örneği (s. 87):** One of the valuable features of messaging is that it’s flexible enough to support all the interaction styles described in section 3.1.1.
>
> **Türkçe:** Mesajlaşmaların değerli özelliklerinden biri, bölüm 3.1.1'de açıklanan tüm etkileşim stillerini destekleyecek kadar esnek olmasıdır.

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
