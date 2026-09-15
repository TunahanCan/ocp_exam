# Unit 11 · Exceptions and Localization — Vocabulary

Bu sözlük, [ana çift dilli nottaki](bilingual_notes.md) exception handling,
formatting ve localization bağlamında geçen teknik/YDS kelimelerini alfabetik
olarak toplar.

## A–C

### adapt · verb

- **Türkçe:** uyarlamak, uyum sağlamak
- **Java bağlamı:** Application'ın farklı locale, input veya failure
  durumlarına uyarlanması.
- **Example:** “Localization helps the application adapt to different regions.”
- **Çeviri:** “Yerelleştirme, uygulamanın farklı bölgelere uyum sağlamasına yardımcı olur.”
- **Related:** adaptation, adaptable; synonym: adjust

### alter · verb

- **Türkçe:** değiştirmek
- **Java bağlamı:** Exception'ın normal program flow'unu değiştirmesi.
- **Example:** “An exception alters the normal program flow.”
- **Çeviri:** “Bir exception, programın normal akışını değiştirir.”
- **Related:** alteration; synonym: change

### anticipate · verb

- **Türkçe:** önceden öngörmek, beklemek
- **Java bağlamı:** Checked exception'ın application tarafından düşünülmesi
  beklenen failure durumunu temsil etmesi.
- **Example:** “Checked exceptions often represent anticipated problems.”
- **Çeviri:** “Checked exception'lar çoğunlukla öngörülen sorunları temsil eder.”
- **Related:** anticipation, anticipated; synonym: foresee

### bundle · noun

- **Türkçe:** demet, paket
- **Java bağlamı:** `ResourceBundle`, localized key/value kaynaklarını bir
  hierarchy içinde sunar.
- **Example:** “The bundle contains user-facing messages.”
- **Çeviri:** “Kaynak demeti, kullanıcıya gösterilen mesajları içerir.”
- **Related:** resource bundle, bundle name

### candidate · noun / adjective

- **Türkçe:** aday; aday olan
- **Java bağlamı:** Bundle aramasında sırayla değerlendirilen olası kaynak.
- **Example · özgün:** “Java checks candidate bundles from specific to general.”
- **Çeviri:** “Java, aday kaynak demetlerini en özelden en genele doğru kontrol eder.”
- **Related:** candidacy; candidate for; candidate bir garanti değil, değerlendirme adayıdır.
- **Kaynak bağlamı:** [exam essentials](bilingual_notes.md#exam-essentials)

### cast · noun / verb

- **Türkçe:** tür dönüşümü; bir türe dönüştürmek
- **Java bağlamı:** Referansın başka bir tür olarak kullanılmasını istemek; nesnenin gerçek türünü değiştirmez. Türkçe teknik anlatımda `cast etmek` korunur.
- **Example · özgün:** “The cast compiles but fails at runtime.”
- **Çeviri:** “Cast işlemi derlenir, ancak çalışma zamanında başarısız olur.”
- **Related:** casting, type cast; `ClassCastException`

### catch · verb / noun

- **Türkçe:** yakalamak; yakalama block'u
- **Java bağlamı:** Compatible exception'ı handle eden `catch` clause.
- **Example:** “Catch the checked exception or declare it.”
- **Çeviri:** “Checked exception'ı yakalayın veya bildirin.”
- **Related:** catcher; phrase: catch block

### category · noun

- **Türkçe:** kategori
- **Java bağlamı:** `Locale.Category.DISPLAY` ve `FORMAT`, default locale
  kullanım alanlarını ayırır.
- **Example:** “The FORMAT category affects default number formatting.”
- **Çeviri:** “FORMAT kategorisi, varsayılan sayı biçimlendirmesini etkiler.”
- **Related:** categorize, categorical

### checked exception · noun phrase

- **Türkçe:** derleyicinin ele alma veya bildirme zorunluluğu uyguladığı exception
- **Java bağlamı:** Compiler'ın handle or declare rule uyguladığı exception
  type'ı.
- **Example:** “An `IOException` is a checked exception.”
- **Çeviri:** “`IOException`, derleyicinin yakalama veya bildirme zorunluluğu uyguladığı bir istisnadır.”
- **Related:** check, handle or declare; antonym: unchecked exception

## D–H

### declare · verb

- **Türkçe:** bildirmek, declare etmek
- **Java bağlamı:** Method signature'da `throws` ile exception olasılığını
  belirtmek.
- **Example:** “The method declares that it may throw an exception.”
- **Çeviri:** “Metot, bir exception fırlatabileceğini bildirir.”
- **Related:** declaration, declarative

### default · adjective / noun

- **Türkçe:** varsayılan
- **Java bağlamı:** Explicit locale verilmediğinde JVM'in kullandığı locale.
- **Example:** “The JVM supplies a default locale.”
- **Çeviri:** “JVM varsayılan bir dil/bölge ayarı sağlar.”
- **Related:** default setting; contrast: explicit

### effectively final · adjective phrase

- **Türkçe:** fiilen final
- **Java bağlamı:** `final` yazılmasa da initialization sonrasında reassign
  edilmeyen local variable.
- **Example:** “An existing resource must be final or effectively final.”
- **Çeviri:** “Önceden oluşturulmuş kaynak değişkeni `final` veya effectively final olmalıdır.”
- **Related:** reassignment; final variable

### exception · noun

- **Türkçe:** istisna, program akışını bozan olay
- **Java bağlamı:** `Throwable` hierarchy'sindeki failure object'i.
- **Example:** “The exception carries a message and a stack trace.”
- **Çeviri:** “Exception, bir mesaj ve çağrı yığını izi taşır.”
- **Related:** exceptional, except; throw/catch

### explicit · adjective

- **Türkçe:** açıkça belirtilmiş
- **Java bağlamı:** Factory method'a doğrudan geçirilen locale, default locale'ı
  geçersiz kılar.
- **Example:** “An explicit locale determines the currency format.”
- **Çeviri:** “Açıkça verilen dil/bölge ayarı, para biriminin gösterim biçimini belirler.”
- **Related:** explicitly; antonym: implicit

### fallback · noun / adjective

- **Türkçe:** yedek seçenek, geri dönüş seçeneği
- **Java bağlamı:** Requested resource bundle veya key bulunamadığında parent
  bundle'a dönme.
- **Example:** “The base bundle provides a fallback value.”
- **Çeviri:** “Temel kaynak demeti, yedek bir değer sağlar.”
- **Related:** fall back (verb); backup

### format · verb / noun

- **Türkçe:** biçimlendirmek; biçim
- **Java bağlamı:** Number/date/value'yu locale-aware `String`e dönüştürmek.
- **Example:** “Format the amount as German currency.”
- **Çeviri:** “Tutarı Alman para birimi biçiminde gösterin.”
- **Related:** formatter, formatting

### handle · verb

- **Türkçe:** ele almak, işlemek
- **Java bağlamı:** Exception'ı compatible `catch` block içinde çözmek.
- **Example:** “The caller handles the exception.”
- **Çeviri:** “Çağıran kod, exception’ı ele alır.”
- **Related:** handler, handling; contrast: declare

### happy path · noun phrase

- **Türkçe:** her şeyin beklendiği gibi ilerlediği senaryo
- **Java bağlamı:** Exception oluşmadan tamamlanan olağan işlem akışı; “mutlu yol” diye kelimesi kelimesine çevrilmez.
- **Example · özgün:** “The happy path completes without an exception.”
- **Çeviri:** “Happy path, exception oluşmadan tamamlanır.”
- **Related:** success scenario; contrast: failure scenario

### hierarchy · noun

- **Türkçe:** hiyerarşi
- **Java bağlamı:** Exception inheritance veya resource bundle parent chain.
- **Example:** “The search follows the selected bundle hierarchy.”
- **Çeviri:** “Arama, seçilen kaynak demeti hiyerarşisini izler.”
- **Related:** hierarchical

## I–P

### internationalization · noun

- **Türkçe:** uluslararasılaştırma
- **Java bağlamı:** Application'ı farklı dil ve region'lara uyarlanabilir
  tasarlama; sıkça `i18n` diye kısaltılır.
- **Example:** “Internationalization separates messages from the source code.”
- **Çeviri:** “Uluslararasılaştırma, mesajları kaynak koddan ayırır.”
- **Related:** internationalize, i18n

### locale · noun

- **Türkçe:** dil/bölge ayarı
- **Java bağlamı:** Language, optional region ve varyant bilgisini taşıyan
  `java.util.Locale`.
- **Example:** “The locale controls language-sensitive formatting.”
- **Çeviri:** “Dil/bölge ayarı, dile duyarlı biçimlendirmeyi yönetir.”
- **Related:** local, locality, localization

### localization · noun

- **Türkçe:** yerelleştirme
- **Java bağlamı:** Message, date, number ve currency'yi belirli locale'a göre
  sunma; sıkça `l10n`.
- **Example:** “Localization changes user-facing output.”
- **Çeviri:** “Yerelleştirme, kullanıcıya gösterilen çıktıyı değiştirir.”
- **Related:** localize, localized, l10n

### parse · verb

- **Türkçe:** çözümlemek, metni yapılandırılmış değere çevirmek
- **Java bağlamı:** Localized `String`i `Number` veya temporal value'ya
  dönüştürmek.
- **Example:** “Parse the localized number before using it.”
- **Çeviri:** “Yerelleştirilmiş sayı metnini kullanmadan önce çözümleyin.”
- **Related:** parser, parsing; contrast: format

### permissible · adjective

- **Türkçe:** izin verilen, yapılması mümkün olan
- **Java bağlamı:** `It is permissible to handle or declare an unchecked exception` ifadesi, bu işlemin yasak olmadığını belirtir.
- **Example · özgün:** “It is permissible to declare an unchecked exception.”
- **Çeviri:** “Unchecked exception’ı bildirmek mümkündür.”
- **Related:** permit, permission; synonym: allowed; antonym: forbidden

### primary exception · noun phrase

- **Türkçe:** birincil exception
- **Java bağlamı:** TWR'da dışarı taşınan asıl exception; close failure'ları
  suppressed olabilir.
- **Example:** “The exception from the try body remains primary.”
- **Çeviri:** “`try` gövdesinden gelen exception birincil olarak kalır.”
- **Related:** suppressed exception

### propagate · verb

- **Türkçe:** yukarı iletmek, yayılmak
- **Java bağlamı:** Handle edilmeyen exception'ın call stack boyunca caller'a
  gitmesi.
- **Example:** “The checked exception propagates to the caller.”
- **Çeviri:** “Checked exception, çağıran koda iletilir.”
- **Related:** propagation; synonym: pass on

## R–S

### recover · verb

- **Türkçe:** toparlanmak, kurtarmak
- **Java bağlamı:** Failure sonrasında programın meaningful biçimde devam
  etmesi.
- **Example:** “The catch block may recover from the failure.”
- **Çeviri:** “`catch` bloğu, hata sonrasında programın toparlanmasını sağlayabilir.”
- **Related:** recovery, recoverable

### region · noun

- **Türkçe:** bölge, ülke kodu
- **Java bağlamı:** Locale'ın optional uppercase country/region parçası.
- **Example:** “The region code distinguishes `en_US` from `en_GB`.”
- **Çeviri:** “Bölge kodu, `en_US` ile `en_GB` ayarlarını birbirinden ayırır.”
- **Related:** regional

### resource · noun

- **Türkçe:** kaynak
- **Java bağlamı:** File/connection gibi kapatılması gereken
  `AutoCloseable` object.
- **Example:** “The resources close in reverse order.”
- **Çeviri:** “Kaynaklar ters sırayla kapanır.”
- **Related:** resource management

### resource bundle · noun phrase

- **Türkçe:** yerelleştirme kaynak demeti
- **Java bağlamı:** Locale'a göre seçilen message/config key/value container'ı.
- **Example:** “Load the most specific resource bundle.”
- **Çeviri:** “Dil ve bölgeye en özel kaynak demetini yükleyin.”
- **Related:** properties file, base bundle

### stack trace · noun phrase

- **Türkçe:** çağrı yığını izi
- **Java bağlamı:** Exception'ın oluştuğu call sequence'i ve source
  location'ları gösterir.
- **Example:** “The stack trace starts at the throw point.”
- **Çeviri:** “Çağrı yığını izi, istisnanın fırlatıldığı noktadan başlar.”
- **Related:** call stack

### suppress · verb

- **Türkçe:** bastırmak, ikincil duruma almak
- **Java bağlamı:** TWR close exception'ını primary exception üzerinde
  saklamak.
- **Example:** “Java suppresses the exception thrown during close.”
- **Çeviri:** “Java, kapanış sırasında fırlatılan exception’ı ikincil olarak saklar.”
- **Related:** suppression, suppressed exception

## T–Z

### throw · verb

- **Türkçe:** fırlatmak
- **Java bağlamı:** `throw` keyword'üyle exception object'ini program flow'a
  vermek.
- **Example:** “The method may throw an `IOException`.”
- **Çeviri:** “Metot bir `IOException` fırlatabilir.”
- **Related:** throws declaration; throw point

### traversal · noun

- **Türkçe:** izlenen yol, dolaşma
- **Java bağlamı:** Stack trace veya bundle hierarchy boyunca ilerleme.
- **Example:** “Bundle traversal starts with the most specific candidate.”
- **Çeviri:** “Kaynak demetlerini tarama, en özel adayla başlar.”
- **Related:** traverse

### unchecked exception · noun phrase

- **Türkçe:** ele alma veya bildirme zorunluluğu olmayan exception
- **Java bağlamı:** `RuntimeException` veya `Error` kolunda olup compiler'ın
  handle/declare zorunluluğu getirmediği type.
- **Example:** “A `NullPointerException` is unchecked.”
- **Çeviri:** “`NullPointerException` için yakalama veya bildirme zorunluluğu yoktur.”
- **Related:** runtime exception; antonym: checked exception

### user-facing · adjective

- **Türkçe:** kullanıcıya gösterilen
- **Java bağlamı:** Localization gerektiren message, label, date ve currency
  output'ları.
- **Example:** “Translate user-facing text, not class names.”
- **Çeviri:** “Kullanıcıya gösterilen metni çevirin; sınıf adlarını koruyun.”
- **Related:** interface, display

### wrap · verb

- **Türkçe:** sarmalamak
- **Java bağlamı:** Bir exception'ı başka exception'ın cause'u olarak taşımak.
- **Example:** “Wrap the original exception without losing its cause.”
- **Çeviri:** “Özgün exception’ı neden bilgisini kaybetmeden başka bir exception’la sarmalayın.”
- **Related:** wrapper, cause chain

## Karıştırılan anlamları ayır

**declare / throw / handle:** `declare` olasılığı imzada bildirir; `throw` gerçekten fırlatır; `handle` yakalayıp ele alır. `throws` yazmak exception fırlatmaz.

`parse` metinden değere; `format` değerden metne gider. `suppress`, bilgiyi silmek değildir; `getSuppressed()` ile saklanan exception’a erişilebilir.

## Kapalı kitap hatırlama · 5 dakika

Her oturumda en fazla 5 kelime seç. Önce Türkçeyi kapatıp İngilizce cümleyi
çevir; ardından İngilizceyi kapatıp Türkçe anlamdan sözcüğü ve kendi örneğini
üret. Yalnız “tanıdık geldi” yanıtını başarı sayma: **0 = çıkaramadım,
1 = anlamını söyledim, 2 = doğru teknik cümlede kullandım**. 0–1 puanlıları
ünite [tekrar rotasına](README.md) göre geri getir.

**Özgün aktarım sorusu:** Bir metot checked exception bildirdiğinde onu her çağrıda fırlatmak zorunda mıdır? İngilizce yanıtında `declare`, `throw`, `not required to` kullan.

Cevabını yazdıktan sonra kontrol et.

**Örnek yanıt:** No. A method is not required to throw every exception it declares.

## Mini quiz · Vocabulary recall

Bu bölüm özgün çalışma alıştırmasıdır.

1. Exception'ı signature'da bildirmek için kullanılan teknik fiil nedir?
2. Exception'ın caller'a doğru ilerlemesi hangi fiille anlatılır?
3. TWR'da asıl dışarı taşınan exception için hangi phrase kullanılır?
4. Locale-specific file bulunmadığında kullanılan yedek kaynak nedir?
5. Kullanıcıya gösterilen message/date/currency için hangi adjective kullanılır?
6. String'i number'a çevirme işleminin fiili nedir?

## Cevaplar

1. declare
2. propagate
3. primary exception
4. fallback / base bundle
5. user-facing
6. parse
