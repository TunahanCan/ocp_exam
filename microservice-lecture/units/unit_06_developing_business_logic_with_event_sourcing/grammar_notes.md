# Ünite 06 · Developing business logic with event sourcing — Grammar Notes

**Amaç:** Kaynak PDF’nin 183–219. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 216):** An application that uses a NoSQL-based event store, such as Eventuate SaaS, can use an analogous approach, despite having a very limited transaction model.
>
> **Türkçe:** Eventuate SaaS gibi NoSQL tabanlı bir event store (olay deposu) kullanan uygulama, çok sınırlı bir transaction modeline sahip olmasına rağmen benzer bir yaklaşım kullanabilir.

> **English — Kaynak örneği (s. 218):** But despite these drawbacks, event sourcing has a major role to play in a microservice architecture.
>
> **Türkçe:** Ancak bu sakıncalara rağmen event sourcing'in (olay geçmişinden durum oluşturmanın) mikroservis mimarisinde önemli bir rolü vardır.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 200):** In contrast, an event sourcing-based application can immediately market to customers who have done this in the past.
>
> **Türkçe:** Buna karşılık event sourcing tabanlı bir uygulama, bunu geçmişte yapmış müşterilere yönelik pazarlamaya hemen başlayabilir.

> **English — Kaynak örneği (s. 198):** On the other hand, it creates a challenge, because the structure of events often changes over time.
>
> **Türkçe:** Öte yandan bu bir zorluk yaratır; çünkü olayların yapısı çoğu zaman zaman içinde değişir.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 194):** The problem with this approach is that transactions can commit in an order that’s different from the order in which they generate events.
>
> **Türkçe:** Bu yaklaşımın sorunu, transaction'ların olay üretme sıralarından farklı bir sırada commit edilebilmesidir.

> **English — Kaynak örneği (s. 204):** If a snapshot exists, the find() operation queries the events table to find all events whose event_id is greater than the snapshot’s entity_version.
>
> **Türkçe:** Bir snapshot (anlık görüntü) varsa find() işlemi, event_id değeri snapshot'ın entity_version değerinden büyük olan tüm olayları bulmak için events tablosunu sorgular.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin. İlk örnekte odak “an order that’s different ...” ve “the order in which ...” yapılarıdır; “the problem ... is that ...” içerik bildirir.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 190):** The Eventuate Client framework, an event-sourcing framework described in more detail in section 6.2.2, names these methods process() and apply().
>
> **Türkçe:** Kısım 6.2.2'de daha ayrıntılı anlatılan bir event sourcing framework'ü olan Eventuate Client, bu metotları process() ve apply() olarak adlandırır.

> **English — Kaynak örneği (s. 205):** The aggregate ID is used as the partition key, which preserves the ordering of events published by a given aggregate.
>
> **Türkçe:** Aggregate ID'si partition key (bölümleme anahtarı) olarak kullanılır; böylece belirli bir aggregate'ın yayımladığı olayların sırası korunur.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 195):** One solution to this problem is to add an extra column to the EVENTS table that tracks whether an event has been published.
>
> **Türkçe:** Bu sorunun bir çözümü, EVENTS tablosuna bir olayın yayımlanıp yayımlanmadığını izleyen ek bir sütun eklemektir.

> **English — Kaynak örneği (s. 200):** A traditional application wouldn’t preserve this information, so could only market to customers who add and remove items after the feature is implemented.
>
> **Türkçe:** Geleneksel bir uygulama bu bilgiyi saklamazdı; dolayısıyla yalnızca özellik geliştirildikten sonra öğe ekleyip çıkaran müşterilere yönelik pazarlama yapabilirdi.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 210):** For example, if updating an aggregate would violate a business rule, then the aggregate must emit an event to report the error.
>
> **Türkçe:** Örneğin bir aggregate'ı güncellemek bir iş kuralını ihlal edecekse aggregate, hatayı bildirmek için bir olay üretmelidir.

> **English — Kaynak örneği (s. 211):** If a service uses an RDBMS-based event store, it can update the event store and create a saga orchestrator within the same ACID transaction.
>
> **Türkçe:** Bir servis RDBMS tabanlı bir event store kullanıyorsa aynı ACID transaction içinde event store'u güncelleyebilir ve bir saga orchestrator (saga orkestratörü) oluşturabilir.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez. İlk kaynak örneğindeki “if updating ... would violate” yapısında would, önerilen güncellemenin doğuracağı olası sonucu anlatır; sıradan gelecek zaman ifadesi değildir.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 196):** The application only needs to load the snapshot and the two events that follow it in order to restore the state of the aggregate.
>
> **Türkçe:** Aggregate'ın durumunu geri oluşturmak için uygulamanın yalnızca snapshot'ı ve onu izleyen iki olayı yüklemesi yeterlidir.

> **English — Kaynak örneği (s. 205):** In order to restart correctly, it periodically saves the current position in the binlog—filename and offset—in a special Apache Kafka topic.
>
> **Türkçe:** Doğru biçimde yeniden başlayabilmek için binlog'daki mevcut konumu — dosya adı ve offset değerini — özel bir Apache Kafka topic'inde düzenli aralıklarla saklar.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 213):** Before updating an aggregate, the saga participant verifies that it hasn’t processed the message before by looking for the message ID in the events.
>
> **Türkçe:** Saga katılımcısı, aggregate'ı güncellemeden önce olaylar içinde mesaj ID'sini arayarak mesajı daha önce işlemediğini doğrular.

> **English — Kaynak örneği (s. 184):** After all, event sourcing eliminates a source of programming errors by guaranteeing that an event will be published whenever an aggregate is created or updated.
>
> **Türkçe:** Sonuçta event sourcing, her aggregate oluşturulduğunda veya güncellendiğinde bir olayın yayımlanacağını garanti ederek programlama hatalarının bir kaynağını ortadan kaldırır.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 199):** But instead of migrating events to the new schema version in situ, event sourcing frameworks transform events when they’re loaded from the event store.
>
> **Türkçe:** Ancak event sourcing framework'leri, saklanan olayları bulundukları yerde yeni şema sürümüne taşımak yerine, olayları event store'dan yüklenirken dönüştürür.

> **English — Kaynak örneği (s. 194):** The main difference is that it permanently stores events in an EVENTS table rather than temporarily saving events in an OUTBOX table and then deleting them.
>
> **Türkçe:** Temel fark, olayları OUTBOX tablosunda geçici olarak saklayıp sonra silmek yerine EVENTS tablosunda kalıcı olarak saklamasıdır.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin. In situ, “bulunduğu yerde” anlamındadır: kaynak kayıtları yerinde değiştirmek ile yükleme sırasında dönüştürmek karşılaştırılır.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 189):** It validates its arguments, and without changing the state of the aggregate, returns a list of events representing the state changes.
>
> **Türkçe:** Argümanlarını doğrular ve aggregate'ın durumunu değiştirmeden, durum değişikliklerini temsil eden olayların listesini döndürür.

> **English — Kaynak örneği (s. 201):** The application somehow must forget about the user without deleting the events.
>
> **Türkçe:** Uygulama, olayları silmeden kullanıcıya ilişkin bilgileri bir şekilde unutmalıdır.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 212):** Now that we’ve looked at how to reliably create a saga orchestrator, let’s see how event sourcing-based services can participate in orchestration-based sagas.
>
> **Türkçe:** Bir saga orchestrator'ın nasıl güvenilir biçimde oluşturulacağını gördüğümüze göre event sourcing tabanlı servislerin orkestrasyon tabanlı saga'lara nasıl katılabileceğine bakalım.

> **English — Kaynak örneği (s. 196):** Figure 6.8 shows how to recreate a Customer from a snapshot corresponding to the state of a Customer as of event #103.
>
> **Türkçe:** Şekil 6.8, 103 numaralı olay itibarıyla Customer'ın durumunu temsil eden bir snapshot'tan Customer'ın nasıl yeniden oluşturulduğunu gösterir.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 205):** The Eventuate client framework enables developers to write event sourcing-based applications that use the Eventuate Local event store.
>
> **Türkçe:** Eventuate client framework'ü, geliştiricilerin Eventuate Local event store'u kullanan event sourcing tabanlı uygulamalar yazmasını sağlar.

> **English — Kaynak örneği (s. 202):** To make matters worse, a NoSQL-based event store will typically only support primary key-based lookup.
>
> **Türkçe:** Daha da kötüsü, NoSQL tabanlı bir event store genellikle yalnızca birincil anahtara dayalı aramayı destekler.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do. “To make matters worse” kalıbı burada bir amaç değil, “daha da kötüsü” anlamında geçiş ifadesidir.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 188):** This is a much more stringent requirement than before, when an aggregate only emitted events that were of interest to consumers.
>
> **Türkçe:** Bu, aggregate'ın yalnızca tüketicileri ilgilendiren olayları ürettiği önceki duruma göre çok daha katı bir gereksinimdir.

> **English — Kaynak örneği (s. 188):** A state change might be as simple as changing the value of the field of an object, such as Order.state.
>
> **Türkçe:** Bir durum değişikliği, örneğin Order.state gibi bir nesne alanının değerini değiştirmek kadar basit olabilir.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 188):** Because events are used to persist an aggregate, you no longer have the option of using a minimal OrderCreated event that contains the orderId.
>
> **Türkçe:** Aggregate'ı kalıcı olarak saklamak için olaylar kullanıldığından, artık yalnızca orderId içeren asgari bir OrderCreated olayı kullanma seçeneğiniz yoktur.

> **English — Kaynak örneği (s. 186):** Consequently, as with history and auditing, developers must bolt on event-generation logic, which risks not being synchronized with the business logic.
>
> **Türkçe:** Bu nedenle, geçmiş tutma ve denetim kaydı oluşturmada olduğu gibi, geliştiriciler olay üretme mantığını da sonradan eklemek zorundadır; bu mantığın iş mantığıyla uyumlu kalmama riski vardır.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 185):** To be fair, I’ve used Hibernate successfully to develop applications where the database schema has been derived from the object model.
>
> **Türkçe:** Hakkını teslim etmek gerekirse, veritabanı şemasının nesne modelinden türetildiği uygulamaları geliştirmek için Hibernate'i başarıyla kullandım.

> **English — Kaynak örneği (s. 193):** The second one will fail because the version number has changed, so it won’t accidentally overwrite the first transaction’s changes.
>
> **Türkçe:** Sürüm numarası değiştiği için ikinci işlem başarısız olur; böylece ilk transaction'ın değişikliklerinin üzerine yanlışlıkla yazmaz.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Past perfect — had + V3

**İşlev:** Geçmişteki bir anlatım noktasından daha önce olmuş olayı gösterir.

> **Formül:** S + had + V3

> **English — Kaynak örneği (s. 184):** Many years ago, Mary had learned about event sourcing, an event-centric way of writing business logic and persisting domain objects.
>
> **Türkçe:** Mary, yıllar önce iş mantığı yazmanın ve domain nesnelerini kalıcı olarak saklamanın olay merkezli bir yolu olan event sourcing'i öğrenmişti.

> **YDS ipucu:** Had tek başına past perfect değildir; had a meeting gibi yapılarda ana fiildir.

## 17. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 211):** One issue to keep in mind when writing an event handler that creates a saga orchestrator is that it must handle duplicate events.
>
> **Türkçe:** Saga orchestrator oluşturan bir event handler (olay işleyici) yazarken akılda tutulması gereken bir konu, yinelenen olayları ele alması gerektiğidir.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 18. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 211):** Instead, a service must have an event handler that creates the saga orchestrator in response to a domain event emitted by the aggregate.
>
> **Türkçe:** Bunun yerine serviste, aggregate'ın ürettiği bir domain event'e yanıt olarak saga orchestrator oluşturan bir olay işleyici bulunmalıdır.

> **English — Kaynak örneği (s. 186):** It is time consuming to implement an aggregate history mechanism and involves duplicating code that must be synchronized with the business logic.
>
> **Türkçe:** Aggregate geçmişini tutan bir mekanizmayı gerçekleştirmek zaman alır ve iş mantığıyla uyumlu tutulması gereken kodu yinelemeyi gerektirir.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 19. Degree — too ... to / enough to

**İşlev:** Too aşırı derece nedeniyle engeli; enough gerekli yeterliliği anlatır.

> **Formül:** too + adjective + to + V1; adjective + enough + to + V1

> **English — Kaynak örneği (s. 190):** The process() method either returns an OrderRevisionProposed event, or throws an exception if it’s too late to revise the Order or if the proposed revision doesn’t meet the order minimum.
>
> **Türkçe:** process() metodu ya bir OrderRevisionProposed olayı döndürür ya da Order'ı değiştirmek için çok geçse veya önerilen değişiklik asgari sipariş tutarını karşılamıyorsa exception fırlatır.

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
