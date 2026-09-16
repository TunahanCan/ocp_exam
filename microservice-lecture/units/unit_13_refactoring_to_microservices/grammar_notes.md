# Ünite 13 · Refactoring to microservices — Grammar Notes

**Amaç:** Kaynak PDF’nin 428–471. sayfalarındaki cümleleri yapı, anlam ilişkisi ve teknik bağlam bakımından çözümlemek. İngilizce örnekler belirtilen kaynak sayfalardan alınmıştır.

[Ana ders](bilingual_notes.md) · [Ünite sözlüğü](vocabulary.md) · [Grammar PDF](grammar_notes.pdf)

**Gösterimler:** S = subject (özne); V = verb (fiil); V1 = yalın fiil; V3 = past participle (üçüncü biçim). Bir cümle birden fazla yapı içerebilir; başlık o örnekte odaklanılan yapıyı belirtir.

## 1. Concession — although / even though / despite

**İşlev:** Beklenenin tersine gerçekleşen durumu, “rağmen” ilişkisiyle verir.

> **Formül:** although / even though + S + V; despite + noun / -ing

> **English — Kaynak örneği (s. 457):** Even though a service that implements a new feature defines its own entity classes, it usually accesses data that’s owned by the monolith.
>
> **Türkçe:** Yeni bir özelliği uygulayan bir servis kendi entity sınıflarını tanımlarken, genellikle monolit'in sahip olduğu verilere erişir.

> **English — Kaynak örneği (s. 430):** Although starting from scratch and leaving the legacy code base behind sounds appealing, it’s extremely risky and will likely end in failure.
>
> **Türkçe:** Baştan başlamak ve eski kod tabanını çekici bir şekilde bırakmak son derece riskli ve muhtemelen başarısızlıkla sonuçlanacak.

> **YDS ipucu:** Despite of kullanılmaz. Çekimli cümle varsa although; isim grubu varsa despite düşünün.

## 2. Contrast — whereas / on the other hand / in contrast

**İşlev:** İki yaklaşımın veya aynı yaklaşımın farklı yönlerini karşılaştırır.

> **Formül:** S + V, whereas S + V; On the other hand / In contrast, S + V

> **English — Kaynak örneği (s. 446):** For example, Delayed Delivery Service has a Delivery entity with narrowly focused responsibilities, whereas the FTGO monolith has an Order entity with an excessive number of responsibilities.
>
> **Türkçe:** Örneğin, Delayed Delivery Service, dar odaklı sorumluluklara sahip Delivery entity'ye sahipken, FTGO monolitinde aşırı sayıda sorumluluklara sahip Order entity'ye sahiptir.

> **English — Kaynak örneği (s. 452):** As we just saw, extracting Kitchen Service requires the monolith to implement compensating transactions, whereas extracting Order Service doesn’t.
>
> **Türkçe:** Gördüğümüz gibi, Kitchen Service çıkarmak için monolit telafi işlemleri uygulamasını gerektirir, Order Service çıkarmak için değil.

> **YDS ipucu:** Whereas karşıtlık kurar; zaman bildiren when ile aynı değildir. On the other hand cümleler arasında geçiş ifadesidir.

## 3. Relative clauses — which / that / whose

**İşlev:** Bir isim hakkında tanımlayıcı veya ek bilgi verir. Önce hangi ismi nitelediğini bulun.

> **Formül:** noun + that/which + clause; noun, which + clause

> **English — Kaynak örneği (s. 452):** The second transaction, which is in the monolith, verifies that the consumer can place orders, authorizes their credit card, and creates a Ticket.
>
> **Türkçe:** İkinci işlem, monolitte olan, tüketicinin sipariş verebileceğini doğruladı, kredi kartını onayladı ve Ticket oluşturdu.

> **English — Kaynak örneği (s. 436):** This API is a natural seam along which you can split the monolith into two smaller applications, as shown in figure 13.3.
>
> **Türkçe:** Bu API, monolit'i 13.3'te gösterildiği gibi iki daha küçük uygulamaya bölmek için doğal bir dikiştir.

> **YDS ipucu:** Virgüllü ek bilgi cümleciğinde that kullanılmaz. Edat + which yapısında edatın anlamını çeviriye katın. Bir fiilin içeriğini veren “ensure that ...” ise isim niteleyen relative clause değildir; that öncesindeki yapıyı kontrol edin.

## 4. Reduced relative clauses — described / implemented

**İşlev:** İsimden sonraki V3, çoğunlukla edilgen ilgi cümleciğinin kısaltılmasıdır.

> **Formül:** noun + (that/which + be) + V3 → noun + V3

> **English — Kaynak örneği (s. 448):** A monolith also uses an ACL when invoking the service and when subscribing to domain events published by a service.
>
> **Türkçe:** Bir monolit, servisi çağırdığında ve bir servis tarafından yayınlanan alan olaylarına abone olduğunda ACL'yi de kullanır.

> **English — Kaynak örneği (s. 458):** Consequently, Delayed Delivery Service must use the second, more complex option and maintain a replica of Orders and Restaurants by subscribing to events published by the monolith.
>
> **Türkçe:** Sonuç olarak, Delayed Delivery Service ikinci, daha karmaşık seçeneği kullanmalı ve monolit tarafından yayınlanan olaylara abonelik ederek sipariş ve Restoranların bir kopyasını korumalıyız.

> **YDS ipucu:** Cümlenin asıl çekimli fiilini ayrı bulun. İsimden sonra gelen V3 her zaman yeni bir ana yüklem değildir.

## 5. Passive voice — be + V3

**İşlev:** İşi yapan kişiden çok işlem gören şeyi öne çıkarır. Teknik metinlerde yaygındır.

> **Formül:** S + be + V3; S + modal + be + V3

> **English — Kaynak örneği (s. 434):** If a new feature can’t be implemented as a service, the solution is often to initially implement the new feature in the monolith.
>
> **Türkçe:** Eğer yeni bir özellik bir servis olarak uygulanamazsa, çözüm genellikle yeni özelliği ilk olarak monolitte uygulamaktır.

> **English — Kaynak örneği (s. 437):** Another benefit of this approach is that it exposes a remote API that can be called by the microservices you develop later.
>
> **Türkçe:** Bu yaklaşımın başka bir faydası da, daha sonra geliştirdiğiniz mikroservisler tarafından çağrılabilen uzak bir API'yi ortaya çıkarmasıdır.

> **YDS ipucu:** Must be deployed doğrudur; must deployed yanlıştır. By + kişi/araç ile by + -ing yöntem yapısını bağlamdan ayırın.

## 6. Conditionals — if clauses

**İşlev:** Sonucun hangi koşulda gerçekleştiğini bildirir. Gerçek olasılık ile varsayımı zaman biçiminden ayırın.

> **Formül:** If + present, present / will / can + V1; If + past, would + V1

> **English — Kaynak örneği (s. 442):** For instance, it requires you to extract services even if you’re making a small change to a relatively stable part of the system.
>
> **Türkçe:** Örneğin, sistemin nispeten istikrarlı bir kısmına küçük bir değişiklik yaparsanız bile servisleri çıkarmanızı gerektirir.

> **English — Kaynak örneği (s. 452):** For example, if we first extract Order Service from the FTGO monolith and then extract Consumer Service, extracting Kitchen Service will be straightforward.
>
> **Türkçe:** Örneğin, eğer önce FTGO monolitinden Order Service çıkarırsak ve sonra Consumer Service çıkarırsak, Kitchen Service çıkarılması kolay olacaktır.

> **YDS ipucu:** If cümleciğindeki past bazen geçmiş zamanı değil varsayımı gösterir. Türkçedeki “olsaydı” tek başına zamanı belirlemez.

## 7. Purpose — in order to / so that

**İşlev:** Bir işlemin hangi amaçla yapıldığını açıklar.

> **Formül:** in order to + V1; so that + S + can/will + V1

> **English — Kaynak örneği (s. 460):** But in order to minimize the development effort, we’ll leave those operations in the monolith and just extract the core of the algorithm.
>
> **Türkçe:** Ama geliştirme çabalarını en aza indirmek için, bu işlemleri monolitte bırakacağız ve sadece algoritmanın çekirdekini çıkarırız.

> **English — Kaynak örneği (s. 445):** Which one you should use depends on what one party—the service or monolith—needs in order to query or update the other party.
>
> **Türkçe:** Hangisini kullanmanız gerekir, diğer tarafı sorgulamak veya güncelleştirmek için bir tarafın - servisi veya monolit - neye ihtiyacı olduğuna bağlıdır.

> **YDS ipucu:** To sonrasında yalın fiil; so that sonrasında özne ve çekimli fiil gelir. So ... that derece-sonuç yapısıyla karıştırmayın.

## 8. Method — by + -ing

**İşlev:** Bir sonuca hangi yöntemle ulaşıldığını açıklar.

> **Formül:** by + V-ing → ... yaparak

> **English — Kaynak örneği (s. 466):** Instead, a better approach is for the monolith to replicate the data to Delivery Service by publishing Courier domain events, CourierLocationUpdated and CourierAvailabilityUpdated.
>
> **Türkçe:** Bunun yerine, monolit için daha iyi bir yaklaşım, Courier alan olayları, CourierLocationUpdated ve CourierAvailabilityUpdated yayınlayarak verileri Delivery Service'ye kopyalamaktır.

> **English — Kaynak örneği (s. 439):** Later in this section, I describe how to reduce the scope of the change by replicating data between the service and monolith.
>
> **Türkçe:** Daha sonra bu bölümde, servis ve monolit arasında verileri kopyalayarak değişimin kapsamını nasıl azaltacağımı açıklarım.

> **YDS ipucu:** By implementing “uygulayarak” anlamındadır. Edat by sonrasında yalın fiil kullanılmaz.

## 9. Replacement — instead of / rather than

**İşlev:** Bir seçeneğin yerine başka bir seçeneğin kullanıldığını anlatır.

> **Formül:** instead of + noun / -ing; rather than + parallel structure

> **English — Kaynak örneği (s. 459):** What’s more, it enables you to implement the feature using a brand new technology stack instead of the monolith’s older one.
>
> **Türkçe:** Dahası, monolitenin eski birini yerine yeni bir teknoloji yığınını kullanarak özelliği uygulayabilmenizi sağlar.

> **English — Kaynak örneği (s. 442):** Instead of implementing features or fixing bugs in the monolith, you extract the necessary service or service(s) and change those.
>
> **Türkçe:** Monolit'te özellikleri uygulamak veya hataları düzeltmek yerine, gerekli servisi veya servisleri çıkarıp değiştirirsiniz.

> **YDS ipucu:** Instead of sonrasında doğrudan çekimli cümle gelmez. Rather than ile karşılaştırılan parçaların dilbilgisel biçimini izleyin.

## 10. Absence — without + -ing

**İşlev:** Bir eylem gerçekleşmeden diğer eylemin yapılabildiğini veya yapılamadığını gösterir.

> **Formül:** without + V-ing; without + noun

> **English — Kaynak örneği (s. 428):** Fortunately, there are strategies you can use to escape from monolithic hell without having to rewrite your application from scratch.
>
> **Türkçe:** Neyse ki, uygulamanızu sıfırdan yeniden yazmadan monolit cehennemden kaçmak için kullanabileceğiniz stratejiler var.

> **English — Kaynak örneği (s. 470):** This allows, for example, the UI team to iterate more easily on the UI design without impacting the backend.
>
> **Türkçe:** Bu, örneğin UI ekibinin UI tasarımı üzerinde arka uç üzerinde etkisi olmadan daha kolay tekrarlamasına olanak sağlar.

> **YDS ipucu:** Without not ile otomatik birleşmez. “Without losing data”, “veri kaybetmeden” anlamındadır.

## 11. Embedded questions — whether / how / what

**İşlev:** Bir soruyu başka bir cümlenin nesnesi veya içeriği haline getirir.

> **Formül:** verb + whether + S + V; verb + how to + V1; verb + what + clause

> **English — Kaynak örneği (s. 438):** But first, let’s look in more detail at some of the challenges you’ll face when extracting a service and how to address them.
>
> **Türkçe:** Ama önce, bir servisi elde ederken karşılaşacağınız bazı zorluklara ve bunları nasıl ele alacağınız konusunda daha ayrıntılı bir bakış açısı verelim.

> **English — Kaynak örneği (s. 464):** Also, as described earlier in section 13.3, we need to carefully consider how to maintain data consistency between the service and the monolith.
>
> **Türkçe:** Ayrıca, 13.3 bölümünde daha önce açıklandığı gibi, servis ve monolit arasında veri tutarlılığını nasıl koruyacağımızı dikkatlice düşünmemiz gerekir.

> **YDS ipucu:** Dolaylı soruda düz cümle sırası kullanılır: how the service works. How does the service work doğrudan sorudur.

## 12. Causative meaning — enable / allow / make

**İşlev:** Bir işlemin başka bir eylemi mümkün kıldığını veya bir sonucu doğurduğunu anlatır.

> **Formül:** enable/allow + object + to + V1; make + object + V1 / adjective

> **English — Kaynak örneği (s. 434):** It enables the service to access data owned by the monolith and to invoke functionality implemented by the monolith.
>
> **Türkçe:** Servisin, monolit'in sahip olduğu verilere erişmesini ve monolit tarafından uygulanan işlevselliklere başvurmasını sağlar.

> **English — Kaynak örneği (s. 437):** It enables you to develop, deploy, and scale the two applications independently of one another.
>
> **Türkçe:** İki uygulamayı birbirinden bağımsız olarak geliştirmenizi, uygulamanızı ve ölçeklendirmenizi sağlar.

> **YDS ipucu:** Enable/allow + object + to + V1; make + object + V1/adjective yapılarını arayın. Make a request gibi make + noun kullanımları bu yapı değildir. Edilgende make ile to geri gelir: be made to do.

## 13. Comparisons — more / less / as ... as

**İşlev:** Seçenekleri derece, maliyet veya özellik bakımından karşılaştırır.

> **Formül:** more/less + adjective + than; as + adjective + as; as + few/little + ... + as

> **English — Kaynak örneği (s. 452):** As a result, all the complexity of supporting compensatable transactions is in Order Service, which is much more testable than the monolith.
>
> **Türkçe:** Sonuç olarak, tazminatlı işlemleri desteklemenin tüm karmaşıklığı, monolitten çok daha test edilebilir olan Order Service'de bulunmaktadır.

> **YDS ipucu:** Much ve far, comparative yapıyı güçlendirir. More easier biçiminde çift karşılaştırma kullanmayın. As well as ekleme yapabilir; “As simple as it sounds, ...” ise ödünleme/karşıtlık bildirir.

## 14. Cause and result — because / therefore / as a result

**İşlev:** Neden ile sonucu ayırmayı sağlar. Because neden cümlesini, therefore sonuç yargısını başlatır.

> **Formül:** because + S + V; because of + noun; therefore / as a result + clause

> **English — Kaynak örneği (s. 429):** As a result, it’s likely that the business will only support the adoption of microservices if it solves a significant business problem.
>
> **Türkçe:** Sonuç olarak, işletmenin yalnızca önemli bir iş sorunu çözülürse mikroservislerin kabulünü destekleyeceği muhtemeldir.

> **English — Kaynak örneği (s. 439):** For example, imagine that, as figure 13.5 shows, you extract Order Service, and as a result its Order class references the monolith’s Restaurant class.
>
> **Türkçe:** Örneğin, Figure 13.5'in gösterdiği gibi, Order Service'i çıkarırsanız, Order sınıfının sonucunda monolit'in Restaurant sınıfına atıfta bulunur.

> **YDS ipucu:** Because ile because of sonrasındaki yapı farklıdır. As a result of + noun, neden belirtir.

## 15. Present perfect — have / has + V3

**İşlev:** Geçmişte başlayan veya tamamlanan durumun şimdiyle ilişkisini kurar.

> **Formül:** S + have/has + V3; S + have/has + been + V3

> **English — Kaynak örneği (s. 439):** It’s possible that classes that remain in the monolith will reference classes that have been moved to the service or vice versa.
>
> **Türkçe:** Monolit'te kalan sınıfların, serviste veya tam tersi taşındığı sınıflara atıfta bulunması mümkündür.

> **YDS ipucu:** Have/has ile V3 birlikte aranır. Been + V3 edilgen olabilir; been + -ing ise continuous yapıdır.

## 16. Past perfect — had + V3

**İşlev:** Geçmişteki bir anlatım noktasından daha önce olmuş olayı gösterir.

> **Formül:** S + had + V3

> **English — Kaynak örneği (s. 455):** The only communication from the company was an email the next morning saying my order had been canceled.
>
> **Türkçe:** Şirketten gelen tek iletişim ertesi sabah e-postayla siparişimin iptal edildiğini söyledi.

> **YDS ipucu:** Had tek başına past perfect değildir; had a meeting gibi yapılarda ana fiildir.

## 17. Time clauses — when / once / until / while

**İşlev:** Olayların zamanını, sırasını veya eşzamanlılığını belirtir; while bazen karşıtlık da kurar.

> **Formül:** when/once/until/while + S + V; while + -ing

> **English — Kaynak örneği (s. 431):** Over time, the amount of functionality implemented by the monolithic application shrinks until either it disappears entirely or it becomes just another microservice.
>
> **Türkçe:** Zamanla, monolit uygulama tarafından uygulanan işlevsellik miktarı tamamen kaybolana kadar ya da başka bir mikroservis haline gelene kadar küçülür.

> **English — Kaynak örneği (s. 432):** A recurring theme in this chapter is that you should avoid making widespread changes to the monolith when migrating to a microservice architecture.
>
> **Türkçe:** Bu bölümde tekrarlanan bir konu, mikroservis mimarisine taşınırken monolit'te yaygın değişiklikler yapmaktan kaçınmanız gerektiğidir.

> **YDS ipucu:** Geleceğe yönelik zaman cümleciğinde genellikle present kullanılır: when it arrives. Until, “... olana kadar” sınırını verir. While eşzamanlılık ya da karşıtlık bildirebilir; anlam ilişkisini kontrol edin. Until + noun bir zaman ifadesidir, tam zaman cümleciği değildir.

## 18. Obligation and possibility — must / should / might

**İşlev:** Zorunluluk, tavsiye ve olasılığı ayırır. Teknik gereksinimlerde bu ayrım önemlidir.

> **Formül:** modal + V1; modal + be + V3

> **English — Kaynak örneği (s. 447):** The class that implements the CustomerContactInfoRepository interface must translate between the ubiquitous language of Delayed Delivery Service and that of the FTGO monolith.
>
> **Türkçe:** CustomerContactInfoRepository arayüzünü uygulayan sınıf, Delayed Delivery Service'nin her yerde bulunan dili ile FTGO monoliğinin arasında tercüme etmelidir.

> **English — Kaynak örneği (s. 449):** A service operation might need to update data in the monolith, or a monolith operation might need to update data in the service.
>
> **Türkçe:** Bir servis operasyonu, monolitdeki verileri güncelleme gerekebilir veya bir monolit operasyonu, servisdeki verileri güncelleme gerekebilir.

> **YDS ipucu:** Must not yasak; do not have to zorunluluk yokluğu bildirir. Might ve may olasılık anlatır, kesinlik vermez.

## 19. Degree — too ... to / enough to

**İşlev:** Too aşırı derece nedeniyle engeli; enough gerekli yeterliliği anlatır.

> **Formül:** too + adjective + to + V1; adjective + enough + to + V1

> **English — Kaynak örneği (s. 434):** A feature might, for instance, be too small to be a meaningful service.
>
> **Türkçe:** Örneğin, bir özellik anlamlı bir servis olmak için çok küçük olabilir.

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
