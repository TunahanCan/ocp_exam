# Ünite 07 · Implementing queries in a microservice architecture — Grammar Notes

**Amaç:** Kaynak PDF’nin 220–252. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 245):** Although an item is the equivalent to a row in an RDBMS, it’s a lot more flexible and can store an entire aggregate.
>
> **Türkçe:** Bir öğe RDBMS'deki bir satırla eşdeğer olsa da, çok daha esnek ve tüm aggregate'yi depolayabilir.

> **English — Kaynak örneği (s. 230):** But first, let’s look at an example of a query operation that’s challenging to implement, despite being local to a single service.
>
> **Türkçe:** Ama önce, tek bir servis için yerel olmasına rağmen uygulamak zor olan bir sorgu operasyonunun bir örneğine bakalım.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 222):** In contrast, in the microservices-based version of the FTGO application, the data is scattered around the following services:
>
> **Türkçe:** Öte yandan, FTGO uygulamasının mikroservislere dayalı sürümünde veriler aşağıdaki servislerin etrafında dağılmıştır:

> **English — Kaynak örneği (s. 228):** For example, an Order retrieved from Order Service might be in the CANCELLED state, whereas the corresponding Ticket retrieved from Kitchen Service might not yet have been cancelled.
>
> **Türkçe:** Örneğin, Order'den alınan bir Order Service, CANCELLED durumunda olabilirken, Kitchen Service'den alınan karşılıklı Ticket henüz iptal edilmemiş olabilir.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 235):** The CQRS pattern avoids the limitations of a single datastore by defining one or more views, each of which efficiently implements specific queries.
>
> **Türkçe:** CQRS örneği, her biri belirli sorguları verimli bir şekilde uygulayan bir veya daha fazla görünüm tanımlayarak tek bir veri depolarının sınırlamalarından kaçınır.

> **English — Kaynak örneği (s. 241):** The client then passes the token to a query operation, which returns an error if the view hasn’t been updated by that event.
>
> **Türkçe:** istemci daha sonra simgeyi bir sorgu işlemine aktarır, bu durum görüntü güncelleştirilmediğinde bir hata gönderir.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 232):** The query side keeps its data model synchronized with the command-side data model by subscribing to the events published by the command side.
>
> **Türkçe:** Sorgu tarafı, komut tarafı tarafından yayınlanan olaylara abonelik ederek veri modelini komut tarafı veri modeli ile senkronize eder.

> **English — Kaynak örneği (s. 233):** It implements the query operations by querying a database that it keeps up-to-date by subscribing to events published by one or more other services.
>
> **Türkçe:** Bir veya daha fazla diğer servis tarafından yayınlanan olaylara abonelik ederek güncel tuttuğu bir veritabanına sorgu sorarak sorgu işlemlerini uyguluyor.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 252):** The API composition pattern, which gathers data from multiple services, is the simplest way to implement queries and should be used whenever possible.
>
> **Türkçe:** Çoklu servislerden verileri toplayan API kompozisyon örneği, sorguları uygulamanın en basit yoludur ve mümkün olduğunca kullanılmalıdır.

> **English — Kaynak örneği (s. 225):** This operation can also be used for externally accessible query operations whose aggregation logic is too complex to be part of an API gateway.
>
> **Türkçe:** Bu işlem, bir API geçitinin bir parçası olmak için çok karmaşık olan toplama mantığı olan dıştan erişilebilir sorgu işlemleri için de kullanılabilir.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 240):** If a DAO implements updates by reading a record and then writing the updated record, it must use either pessimistic or optimistic locking.
>
> **Türkçe:** Bir DAO bir kaydı okuyarak ve sonra güncelleştirilmiş kaydı yazarak güncellemeleri uyguluyorsa, pesimist ya da iyimser bir kilitleme kullanmalıdır.

> **English — Kaynak örneği (s. 248):** The condition expression only allows the update if the attribute doesn’t exist or the eventId is greater than the last processed event ID.
>
> **Türkçe:** Şart ifadesi, güncellemeyi yalnızca özelliğin bulunmadığı veya eventId son işlenmiş olay ID'den daha büyükse izin verir.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 227):** Whenever possible, an API composer should call provider services in parallel in order to minimize the response time for a query operation.
>
> **Türkçe:** Mümkün olduğunda, bir API kompozyonu bir sorgu işleminin yanıt zamanını en aza indirmek için sağlayıcı servislerini paralel olarak çağırmalıdır.

> **English — Kaynak örneği (s. 236):** One drawback of this approach is that the UI code may need to duplicate server-side code in order to update its model.
>
> **Türkçe:** Bu yaklaşımın bir dezavantajı, kullanıcı ortamı kodunun modelini güncelleştirmek için sunucu tarafı kodunun kopyalanması gerekebilir.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 228):** Implement a query that needs data from several services by using events to maintain a read-only view that replicates data from the services.
>
> **Türkçe:** servislerden verileri çoğaltan sadece okuma görünümünü korumak için olayları kullanarak birkaç servisten verilere ihtiyaç duyan bir sorgulama uygulayın.

> **English — Kaynak örneği (s. 240):** In the next section you’ll see an example of a DAO that handles concurrent updates by updating database records without reading them first.
>
> **Türkçe:** Bir sonraki bölümde, önce bunları okumadan veritabanı kayıtlarını güncelleyerek eşzamanlı güncellemeleri işleyen DAO'un bir örneğini göreceksiniz.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 224):** But the concept is the same if the services used some other interprocess communication protocol, such as gRPC, instead of HTTP.
>
> **Türkçe:** Ancak servisler HTTP yerine gRPC gibi diğer süreçler arası iletişim protokollerini kullanırsa konsept aynıdır.

> **English — Kaynak örneği (s. 225):** Instead of routing a request to another service, the API gateway implements the API composition logic.
>
> **Türkçe:** Bir talebi başka bir servise yönlendirmek yerine, API kapısı API kompozisyon mantığını uyguluyor.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 236):** A UI application such as a native mobile application or single page JavaScript application can handle replication lag by updating its local model once the command is successful without issuing a query.
>
> **Türkçe:** Doğal bir mobil uygulama veya tek sayfalık JavaScript uygulaması gibi bir UI uygulaması, komut başarılı olduktan sonra bir sorgu vermeden yerel modelini güncelleyerek çoğaltma gecikmesini ele alabilir.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 221):** After discussing these two patterns, I will talk about how to design CQRS views, followed by the implementation of an example view.
>
> **Türkçe:** Bu iki örneği tartıştıktan sonra, CQRS görünümlerini nasıl tasarlayacağımı, ardından örnek görünümün uygulanmasını konuşacağım.

> **English — Kaynak örneği (s. 245):** But before finalizing this decision, let’s first explore how a table’s primary key impacts the kinds of data access operations it supports.
>
> **Türkçe:** Ama bu kararı sonlandırmadan önce, önce bir tabloun ana anahtarının desteklediği veri erişim operasyonlarının türlerini nasıl etkilediğini araştıralım.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 225):** This approach enables a client, such as a mobile device, that’s running outside of the firewall to efficiently retrieve data from numerous services with a single API call.
>
> **Türkçe:** Bu yaklaşım, güvenlik duvarının dışında çalışan bir mobil cihaz gibi bir istemciye, tek bir API çağrısı ile çok sayıda servisten verileri verimli bir şekilde geri almasını sağlar.

> **English — Kaynak örneği (s. 231):** This service enables restaurant owners to manage their restaurant’s profile and menu items.
>
> **Türkçe:** Bu servis, restoran sahiplerinin restoranlarının profilini ve menü öğelerini yönetmelerini sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 244):** Like many NoSQL databases, DynamoDB has data access operations that are much less powerful than those that are provided by an RDBMS.
>
> **Türkçe:** Birçok NoSQL veritabanı gibi, DynamoDB de bir RDBMS tarafından sağlananlardan çok daha az güçlü veri erişim operasyonlarına sahiptir.

> **English — Kaynak örneği (s. 221):** The Command query responsibility segregation (CQRS) pattern—This is more powerful than the API composition pattern, but it’s also more complex.
>
> **Türkçe:** Komut sorgu sorumluluk ayrımı (CQRS) örneği - Bu API kompozisyon örneğinden daha güçlü, ama aynı zamanda daha karmaşık.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 228):** The API Composer for the findOrder() query operation could omit that service’s data from the response, because the UI can still display useful information.
>
> **Türkçe:** findOrder() sorgu operasyonu için API Composer, bu servisin verilerini yanıtdan atmak olabilir, çünkü kullanıcı arazi hala yararlı bilgileri görüntüleyebilir.

> **English — Kaynak örneği (s. 238):** It’s unaffected by the limitations of a NoSQL database, because it only uses simple transactions and executes a fixed set of queries.
>
> **Türkçe:** NoSQL veritabanının sınırları tarafından etkilenmez, çünkü sadece basit işlemler kullanır ve sabit bir set sorguları yürütür.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 241):** At other times you might need to re-create a view because the schema has changed or you need to fix a bug in code that updates the view.
>
> **Türkçe:** Başka zamanlarda bir görüntü yeniden oluşturmanız gerekebilir çünkü şema değişti veya görüntüyi güncelleyen bir kodda bir hata düzeltmeniz gerekebilir.

> **English — Kaynak örneği (s. 242):** Instead, an application must also read older events that have been archived in, for example, AWS S3.
>
> **Türkçe:** Bunun yerine, bir uygulama, örneğin, AWS S3'de arşivlenen eski olayları da okumalıdır.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 220):** Then they discovered that transaction management wasn’t the only distributed data-related challenge they had to worry about when migrating the FTGO application to microservices.
>
> **Türkçe:** Sonra FTGO uygulamasını mikroservislere aktarırken endişelenmeleri gereken tek dağıtılmış veriyle ilgili zorluk işlem yönetimi olmadığını keşfettiler.

> **English — Kaynak örneği (s. 235):** Even when a database has extensions to support a particular kind of query, using a specialized database is often more efficient.
>
> **Türkçe:** Veritabanın belirli bir soruyu desteklemek için uzantıları olduğu durumlarda bile, özel bir veri tabanı kullanmak genellikle daha verimli olur.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 17. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 229):** It may appear that the API composer only has to execute the same query against each Provider service and combine the results.
>
> **Türkçe:** API kompozitörünün sadece her Provider service'a karşı aynı soruyu gerçekleştirmesi ve sonuçları birleştirmesi gerektiği görünebilir.

> **English — Kaynak örneği (s. 232):** The need to separate concerns means that the service that owns the data isn’t the service that should implement the query operation.
>
> **Türkçe:** Sorunları ayırma ihtiyacı, verilerin sahibi olan servisin sorgu işlemini uygulayacak servis olmadığını gösterir.

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
