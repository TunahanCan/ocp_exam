# Ünite 04 · Managing transactions with sagas — Grammar Notes

**Amaç:** Kaynak PDF’nin 110–145. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 123):** Note that in final step, the saga orchestrator sends a command message to Order Service, even though it’s a component of Order Service.
>
> **Türkçe:** Son adımda saga orchestrator’ın, Order Service’in bir bileşeni olmasına rağmen Order Service’e komut mesajı gönderdiğine dikkat edin.

> **English — Kaynak örneği (s. 145):** An application may even need to use locking in order to simplify the business logic, even though that risks deadlocks.
>
> **Türkçe:** Uygulamanın, deadlock (kilitlenme) riski doğursa bile iş mantığını basitleştirmek için kilitleme kullanması gerekebilir.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 112):** In contrast, implementing the same operation in a microservice architecture is much more complicated.
>
> **Türkçe:** Buna karşılık aynı işlemi mikroservis mimarisinde gerçekleştirmek çok daha karmaşıktır.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 143):** The following listing is an excerpt of the OrderServiceConfiguration class, which is an @Configuration class that instantiates and wires together the Spring @Beans.
>
> **Türkçe:** Sonraki kod bloğu, Spring @Bean’lerini oluşturup birbirine bağlayan bir @Configuration sınıfı olan OrderServiceConfiguration sınıfından bir bölümdür.

> **English — Kaynak örneği (s. 125):** Fortunately, you can avoid this problem by designing orchestrators that are solely responsible for sequencing and don’t contain any other business logic.
>
> **Türkçe:** Neyse ki yalnızca adımların sırasından sorumlu olan ve başka iş mantığı içermeyen orchestrator’lar tasarlayarak bu sorunu önleyebilirsiniz.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 125):** Less coupling—Each service implements an API that is invoked by the orchestrator, so it does not need to know about the events published by the saga participants.
>
> **Türkçe:** Daha az coupling (bağlılık) — Her servis, orchestrator’ın çağırdığı bir API gerçekleştirir; dolayısıyla saga katılımcılarının yayımladığı olayları bilmesi gerekmez.

> **English — Kaynak örneği (s. 133):** The SagaManager class is one of the classes provided by the Eventuate Tram Saga framework, which is a framework for writing saga orchestrators and participants, and is discussed a little later in this section.
>
> **Türkçe:** SagaManager, saga orchestrator’ları ve katılımcıları yazmak için kullanılan Eventuate Tram Saga framework’ünün sağladığı sınıflardan biridir. Bu framework bölümün biraz ilerleyen kısmında ele alınır.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 121):** As a result, there’s a risk that it would need to be updated in lockstep with the order lifecycle implemented by Order Service.
>
> **Türkçe:** Sonuç olarak bunun, Order Service’in gerçekleştirdiği sipariş yaşam döngüsüyle birlikte güncellenmek zorunda kalması riski vardır.

> **English — Kaynak örneği (s. 126):** An anomaly is when a transaction reads or writes data in a way that it wouldn’t if transactions were executed one at time.
>
> **Türkçe:** Bir transaction’ın, transaction’lar sırayla yürütülseydi gerçekleşmeyecek biçimde veri okuması veya yazması anomali oluşturur.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 115):** That’s because if the recipient of a message is temporarily unavailable, the message broker buffers the message until it can be delivered.
>
> **Türkçe:** Çünkü mesajın alıcısı geçici olarak kullanılamıyorsa mesaj aracısı, mesajı teslim edilebilir hâle gelene kadar tamponda tutar.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 131):** The version file countermeasure is so named because it records the operations that are performed on a record so that it can reorder them.
>
> **Türkçe:** Version file karşı önlemi, bir kayıt üzerinde gerçekleştirilen işlemleri yeniden sıralayabilmek için kaydettiğinden bu adı alır.

> **English — Kaynak örneği (s. 125):** As described in chapter 3, a service must use transactional messaging in order to atomically update the database and publish messages.
>
> **Türkçe:** 3. bölümde açıklandığı gibi servis, veritabanını güncelleme ile mesaj yayımlamayı atomik olarak gerçekleştirmek için transactional messaging (işlemsel mesajlaşma) kullanmalıdır.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 132):** Also, because Order Service participates in its own sagas, it has an OrderCommandHandlers adapter class that handles command messages by invoking OrderService.
>
> **Türkçe:** Ayrıca Order Service kendi saga’larına katıldığından, OrderService’i çağırarak komut mesajlarını işleyen OrderCommandHandlers adapter sınıfına sahiptir.

> **English — Kaynak örneği (s. 125):** Order Service processes the participant’s reply message by updating the state of the saga orchestrator and sending a command message to the next saga participant.
>
> **Türkçe:** Order Service, saga orchestrator’ın durumunu güncelleyip sonraki saga katılımcısına komut mesajı göndererek katılımcının yanıt mesajını işler.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 111):** Instead of an ACID transaction, an operation that spans services must use what’s known as a saga, a message-driven sequence of local transactions, to maintain data consistency.
>
> **Türkçe:** Servisler arasında yürütülen bir işlem, veri tutarlılığını korumak için ACID transaction yerine saga adı verilen, mesajlarla ilerleyen bir yerel transaction dizisi kullanmalıdır.

> **English — Kaynak örneği (s. 113):** Today, architects prefer to have a system that’s available rather than one that’s consistent.
>
> **Türkçe:** Kaynak anlatımında günümüz mimarları, tutarlı olan bir sistem yerine kullanılabilir durumda olan bir sistemi tercih eder.

> **Bağlam notu:** Bu tercih cümlesi, kaynak bölümündeki dağıtık sistem ve ağ bölünmesi bağlamında okunmalıdır; her mimarın her durumda tutarlılıktan vazgeçtiği yönünde evrensel bir kural değildir. Grammar odağı **rather than** ile tercih edilen seçeneklerin ayrılmasıdır.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 114):** Chapter 3 described how to send messages as part of a database transaction without using distributed transactions.
>
> **Türkçe:** 3. bölüm, dağıtık transaction kullanmadan veritabanı transaction’ının parçası olarak mesajların nasıl gönderileceğini açıkladı.

> **English — Kaynak örneği (s. 114):** Sagas are mechanisms to maintain data consistency in a microservice architecture without having to use distributed transactions.
>
> **Türkçe:** Saga’lar, dağıtık transaction kullanmak zorunda kalmadan mikroservis mimarisinde veri tutarlılığını korumaya yarayan mekanizmalardır.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 111):** I discuss how to use countermeasures to prevent or reduce the impact of concurrency anomalies caused by the lack of isolation between sagas.
>
> **Türkçe:** Saga’lar arasındaki yalıtım eksikliğinin yol açtığı eşzamanlılık anomalilerini önlemek veya etkilerini azaltmak için karşı önlemlerin nasıl kullanılacağını ele alıyorum.

> **English — Kaynak örneği (s. 125):** Later on in section 4.4, I’ll describe the implementation of the Create Order Saga orchestrator in more detail, including how it uses transaction messaging.
>
> **Türkçe:** İleride 4.4. bölümde, transaction messaging kullanımını da kapsayacak biçimde Create Order Saga orchestrator’ın gerçekleştirimini daha ayrıntılı açıklayacağım.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 120):** The solution is for a saga participant to publish events containing a correlation id, which is data that enables other participants to perform the mapping.
>
> **Türkçe:** Çözüm, saga katılımcısının correlation ID (ilişkilendirme kimliği) içeren olaylar yayımlamasıdır; bu kimlik, diğer katılımcıların eşlemeyi yapmasını sağlayan veridir.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 145):** Nevertheless, transaction management is certainly more complicated than in a monolithic architecture.
>
> **Türkçe:** Bununla birlikte transaction yönetimi, monolitik mimaridekinden kesinlikle daha karmaşıktır.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 121):** Choreography can work well for simple sagas, but because of these drawbacks it’s often better for more complex sagas to use orchestration.
>
> **Türkçe:** Choreography basit saga’larda iyi çalışabilir; ancak bu sakıncaları nedeniyle daha karmaşık saga’larda orchestration kullanmak çoğu zaman daha iyidir.

> **English — Kaynak örneği (s. 126):** That’s because the updates made by each of a saga’s local transactions are immediately visible to other sagas once that transaction commits.
>
> **Türkçe:** Çünkü saga’nın her yerel transaction’ının yaptığı güncellemeler, o transaction commit edildiği anda diğer saga’lar tarafından görülebilir.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 130):** You also need to decide on a case-by-case basis how a saga should deal with a record that has been locked.
>
> **Türkçe:** Saga’nın kilitlenmiş bir kayıtla nasıl başa çıkacağına da her durum için ayrı ayrı karar vermelisiniz.

> **English — Kaynak örneği (s. 131):** But if the Order has been cancelled, the transaction aborts the saga, which causes its compensating transactions to be executed.
>
> **Türkçe:** Ancak Order iptal edilmişse transaction saga’yı durdurur; bunun sonucunda saga’nın compensating transaction’ları (telafi işlemleri) yürütülür.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 117):** When a saga is initiated by system command, the coordination logic must select and tell the first saga participant to execute a local transaction.
>
> **Türkçe:** Saga bir sistem komutuyla başlatıldığında koordinasyon mantığı, ilk saga katılımcısını seçmeli ve ona yerel transaction’ı yürütmesini söylemelidir.

> **English — Kaynak örneği (s. 125):** For example, when using orchestration, the Order class has no knowledge of any of the sagas, so it has a simpler state machine model.
>
> **Türkçe:** Örneğin orchestration kullanıldığında Order sınıfı saga’ların hiçbirinden haberdar değildir; bu nedenle daha basit bir durum makinesi modeline sahiptir.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 17. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 119):** The Create Order Saga must also handle the scenario where a saga participant rejects the Order and publishes some kind of failure event.
>
> **Türkçe:** Create Order Saga, bir saga katılımcısının Order’ı reddedip bir tür başarısızlık olayı yayımladığı senaryoyu da ele almalıdır.

> **English — Kaynak örneği (s. 130):** It must also implement a deadlock detection algorithm that performs a rollback of a saga to break a deadlock and re-execute it.
>
> **Türkçe:** Ayrıca deadlock’u gidermek için saga’yı geri alıp yeniden yürüten bir deadlock detection (kilitlenme saptama) algoritması da gerçekleştirmelidir.

> **Terim notu:** Saga için rollback sözcüğü, uygun telafi adımlarıyla geri alma anlamında okunmalıdır; daha önce commit edilmiş bütün yerel transaction’ların tek bir veritabanı rollback’iyle silinmesi değildir.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 18. Degree — too ... to / enough to

**İşlev:** Too aşırı derece nedeniyle engeli; enough gerekli yeterliliği anlatır.

> **Formül:** too + adjective + to + V1; adjective + enough + to + V1

> **English — Kaynak örneği (s. 127):** Let’s imagine a scenario that interleaves the execution of the Cancel Order and Create Order Sagas, and the Cancel Order Saga is rolled back because it’s too late to cancel the delivery.
>
> **Türkçe:** Cancel Order ve Create Order saga’larının yürütülmesinin iç içe geçtiği ve teslimatı iptal etmek için artık çok geç olduğundan Cancel Order Saga’nın geri alındığı bir senaryo düşünelim.

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
