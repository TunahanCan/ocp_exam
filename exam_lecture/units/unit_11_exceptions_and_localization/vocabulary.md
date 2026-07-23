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
- **Çeviri:** “Localization application'ın farklı region'lara uyum sağlamasına
  yardımcı olur.”
- **Related:** adaptation, adaptable; synonym: adjust

### alter · verb

- **Türkçe:** değiştirmek
- **Java bağlamı:** Exception'ın normal program flow'unu değiştirmesi.
- **Example:** “An exception alters the normal program flow.”
- **Çeviri:** “Exception normal program flow'unu değiştirir.”
- **Related:** alteration; synonym: change

### anticipate · verb

- **Türkçe:** önceden öngörmek, beklemek
- **Java bağlamı:** Checked exception'ın application tarafından düşünülmesi
  beklenen failure durumunu temsil etmesi.
- **Example:** “Checked exceptions often represent anticipated problems.”
- **Çeviri:** “Checked exception'lar çoğunlukla öngörülen problem'ları temsil
  eder.”
- **Related:** anticipation, anticipated; synonym: foresee

### bundle · noun

- **Türkçe:** demet, paket
- **Java bağlamı:** `ResourceBundle`, localized key/value kaynaklarını bir
  hierarchy içinde sunar.
- **Example:** “The bundle contains user-facing messages.”
- **Çeviri:** “Bundle, user-facing mesajları içerir.”
- **Related:** resource bundle, bundle name

### catch · verb / noun

- **Türkçe:** yakalamak; yakalama block'u
- **Java bağlamı:** Compatible exception'ı handle eden `catch` clause.
- **Example:** “Catch the checked exception or declare it.”
- **Çeviri:** “Checked exception'ı catch edin veya declare edin.”
- **Related:** catcher; phrase: catch block

### category · noun

- **Türkçe:** kategori
- **Java bağlamı:** `Locale.Category.DISPLAY` ve `FORMAT`, default locale
  kullanım alanlarını ayırır.
- **Example:** “The FORMAT category affects default number formatting.”
- **Çeviri:** “FORMAT category default number formatting'i etkiler.”
- **Related:** categorize, categorical

### checked exception · noun phrase

- **Türkçe:** kontrollü istisna
- **Java bağlamı:** Compiler'ın handle or declare rule uyguladığı exception
  type'ı.
- **Example:** “An `IOException` is a checked exception.”
- **Çeviri:** “`IOException` checked exception'dır.”
- **Related:** check, handle or declare; antonym: unchecked exception

## D–H

### declare · verb

- **Türkçe:** bildirmek, declare etmek
- **Java bağlamı:** Method signature'da `throws` ile exception olasılığını
  belirtmek.
- **Example:** “The method declares that it may throw an exception.”
- **Çeviri:** “Method exception throw edebileceğini declare eder.”
- **Related:** declaration, declarative

### default · adjective / noun

- **Türkçe:** varsayılan
- **Java bağlamı:** Explicit locale verilmediğinde JVM'in kullandığı locale.
- **Example:** “The JVM supplies a default locale.”
- **Çeviri:** “JVM bir default locale sağlar.”
- **Related:** default setting; contrast: explicit

### effectively final · adjective phrase

- **Türkçe:** fiilen final
- **Java bağlamı:** `final` yazılmasa da initialization sonrasında reassign
  edilmeyen local variable.
- **Example:** “An existing resource must be final or effectively final.”
- **Çeviri:** “Existing resource final veya effectively final olmalıdır.”
- **Related:** reassignment; final variable

### exception · noun

- **Türkçe:** istisna, program akışını bozan olay
- **Java bağlamı:** `Throwable` hierarchy'sindeki failure object'i.
- **Example:** “The exception carries a message and a stack trace.”
- **Çeviri:** “Exception bir message ve stack trace taşır.”
- **Related:** exceptional, except; throw/catch

### explicit · adjective

- **Türkçe:** açıkça belirtilmiş
- **Java bağlamı:** Factory method'a doğrudan geçirilen locale, default locale'ı
  geçersiz kılar.
- **Example:** “An explicit locale determines the currency format.”
- **Çeviri:** “Explicit locale currency format'ını belirler.”
- **Related:** explicitly; antonym: implicit

### fallback · noun / adjective

- **Türkçe:** yedek seçenek, geri dönüş seçeneği
- **Java bağlamı:** Requested resource bundle veya key bulunamadığında parent
  bundle'a dönme.
- **Example:** “The base bundle provides a fallback value.”
- **Çeviri:** “Base bundle fallback value sağlar.”
- **Related:** fall back (verb); backup

### format · verb / noun

- **Türkçe:** biçimlendirmek; biçim
- **Java bağlamı:** Number/date/value'yu locale-aware `String`e dönüştürmek.
- **Example:** “Format the amount as German currency.”
- **Çeviri:** “Tutarı German currency olarak format edin.”
- **Related:** formatter, formatting

### handle · verb

- **Türkçe:** ele almak, işlemek
- **Java bağlamı:** Exception'ı compatible `catch` block içinde çözmek.
- **Example:** “The caller handles the exception.”
- **Çeviri:** “Caller exception'ı handle eder.”
- **Related:** handler, handling; contrast: declare

### hierarchy · noun

- **Türkçe:** hiyerarşi
- **Java bağlamı:** Exception inheritance veya resource bundle parent chain.
- **Example:** “The search follows the selected bundle hierarchy.”
- **Çeviri:** “Arama seçilen bundle hierarchy'sini izler.”
- **Related:** hierarchical

## I–P

### internationalization · noun

- **Türkçe:** uluslararasılaştırma
- **Java bağlamı:** Application'ı farklı dil ve region'lara uyarlanabilir
  tasarlama; sıkça `i18n` diye kısaltılır.
- **Example:** “Internationalization separates messages from the source code.”
- **Çeviri:** “Internationalization mesajları source code'dan ayırır.”
- **Related:** internationalize, i18n

### locale · noun

- **Türkçe:** dil/bölge ayarı
- **Java bağlamı:** Language, optional region ve varyant bilgisini taşıyan
  `java.util.Locale`.
- **Example:** “The locale controls language-sensitive formatting.”
- **Çeviri:** “Locale, language-sensitive formatting'i kontrol eder.”
- **Related:** local, locality, localization

### localization · noun

- **Türkçe:** yerelleştirme
- **Java bağlamı:** Message, date, number ve currency'yi belirli locale'a göre
  sunma; sıkça `l10n`.
- **Example:** “Localization changes user-facing output.”
- **Çeviri:** “Localization user-facing output'u değiştirir.”
- **Related:** localize, localized, l10n

### parse · verb

- **Türkçe:** çözümlemek, metni yapılandırılmış değere çevirmek
- **Java bağlamı:** Localized `String`i `Number` veya temporal value'ya
  dönüştürmek.
- **Example:** “Parse the localized number before using it.”
- **Çeviri:** “Localized number'ı kullanmadan önce parse edin.”
- **Related:** parser, parsing; contrast: format

### primary exception · noun phrase

- **Türkçe:** birincil exception
- **Java bağlamı:** TWR'da dışarı taşınan asıl exception; close failure'ları
  suppressed olabilir.
- **Example:** “The exception from the try body remains primary.”
- **Çeviri:** “Try body'den gelen exception primary kalır.”
- **Related:** suppressed exception

### propagate · verb

- **Türkçe:** yukarı iletmek, yayılmak
- **Java bağlamı:** Handle edilmeyen exception'ın call stack boyunca caller'a
  gitmesi.
- **Example:** “The checked exception propagates to the caller.”
- **Çeviri:** “Checked exception caller'a propagate eder.”
- **Related:** propagation; synonym: pass on

## R–S

### recover · verb

- **Türkçe:** toparlanmak, kurtarmak
- **Java bağlamı:** Failure sonrasında programın meaningful biçimde devam
  etmesi.
- **Example:** “The catch block may recover from the failure.”
- **Çeviri:** “Catch block failure'dan sonra toparlanabilir.”
- **Related:** recovery, recoverable

### region · noun

- **Türkçe:** bölge, ülke kodu
- **Java bağlamı:** Locale'ın optional uppercase country/region parçası.
- **Example:** “The region code distinguishes `en_US` from `en_GB`.”
- **Çeviri:** “Region code `en_US` ile `en_GB`yi ayırır.”
- **Related:** regional

### resource · noun

- **Türkçe:** kaynak
- **Java bağlamı:** File/connection gibi kapatılması gereken
  `AutoCloseable` object.
- **Example:** “The resources close in reverse order.”
- **Çeviri:** “Resource'lar reverse order'da kapanır.”
- **Related:** resource management

### resource bundle · noun phrase

- **Türkçe:** yerelleştirme kaynak demeti
- **Java bağlamı:** Locale'a göre seçilen message/config key/value container'ı.
- **Example:** “Load the most specific resource bundle.”
- **Çeviri:** “En specific resource bundle'ı load edin.”
- **Related:** properties file, base bundle

### stack trace · noun phrase

- **Türkçe:** çağrı yığını izi
- **Java bağlamı:** Exception'ın oluştuğu call sequence'i ve source
  location'ları gösterir.
- **Example:** “The stack trace starts at the throw point.”
- **Çeviri:** “Stack trace throw noktasından başlar.”
- **Related:** call stack

### suppress · verb

- **Türkçe:** bastırmak, ikincil duruma almak
- **Java bağlamı:** TWR close exception'ını primary exception üzerinde
  saklamak.
- **Example:** “Java suppresses the exception thrown during close.”
- **Çeviri:** “Java close sırasında throw edilen exception'ı suppress eder.”
- **Related:** suppression, suppressed exception

## T–Z

### throw · verb

- **Türkçe:** fırlatmak
- **Java bağlamı:** `throw` keyword'üyle exception object'ini program flow'a
  vermek.
- **Example:** “The method may throw an `IOException`.”
- **Çeviri:** “Method `IOException` throw edebilir.”
- **Related:** throws declaration; throw point

### traversal · noun

- **Türkçe:** izlenen yol, dolaşma
- **Java bağlamı:** Stack trace veya bundle hierarchy boyunca ilerleme.
- **Example:** “Bundle traversal starts with the most specific candidate.”
- **Çeviri:** “Bundle traversal en specific candidate ile başlar.”
- **Related:** traverse

### unchecked exception · noun phrase

- **Türkçe:** kontrolsüz istisna
- **Java bağlamı:** `RuntimeException` veya `Error` kolunda olup compiler'ın
  handle/declare zorunluluğu getirmediği type.
- **Example:** “A `NullPointerException` is unchecked.”
- **Çeviri:** “`NullPointerException` unchecked'tır.”
- **Related:** runtime exception; antonym: checked exception

### user-facing · adjective

- **Türkçe:** kullanıcıya gösterilen
- **Java bağlamı:** Localization gerektiren message, label, date ve currency
  output'ları.
- **Example:** “Translate user-facing text, not class names.”
- **Çeviri:** “Class adlarını değil user-facing text'i çevirin.”
- **Related:** interface, display

### wrap · verb

- **Türkçe:** sarmalamak
- **Java bağlamı:** Bir exception'ı başka exception'ın cause'u olarak taşımak.
- **Example:** “Wrap the original exception without losing its cause.”
- **Çeviri:** “Original exception'ı cause bilgisini kaybetmeden wrap edin.”
- **Related:** wrapper, cause chain

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
