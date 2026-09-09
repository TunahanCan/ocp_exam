# Unit 12 · Modules — Vocabulary

Bu sözlük, [ana çift dilli nottaki](bilingual_notes.md) JPMS, command-line
tool'ları, service ve migration bağlamında geçen teknik/YDS kelimelerini
alfabetik olarak toplar.

## A–C

### accessible · adjective

- **Türkçe:** erişilebilir
- **Java bağlamı:** Caller'ın target module'ı okuması, package'ın caller'a export
  edilmesi ve Java access modifier'larının izin vermesiyle type/member'ın
  kullanılabilmesi.
- **Example:** “An exported public type is accessible only if the client reads
  its module.”
- **Çeviri:** “Dışa açılmış `public` bir türe erişebilmek için istemcinin, bu türün modülünü okuyabilmesi gerekir.”
- **Related:** access, accessibility; antonym: inaccessible

### automatic module · noun phrase

- **Türkçe:** otomatik modül
- **Java bağlamı:** Explicit module descriptor (`module-info`) içermeyen fakat
  module path'e konduğu için isim kazanan legacy JAR.
- **Example:** “The legacy JAR becomes an automatic module on the module path.”
- **Çeviri:** “Eski yapıdaki JAR, module path üzerine konulduğunda otomatik modüle dönüşür.”
- **Related:** automatically; contrast: explicit named module, unnamed module

### benefit · noun / verb

- **Türkçe:** yarar; yarar sağlamak
- **Java bağlamı:** Encapsulation, dependency control ve daha küçük runtime
  image gibi JPMS kazanımları.
- **Example:** “A modular application benefits from explicit dependencies.”
- **Çeviri:** “Modüler bir uygulama, açıkça belirtilmiş bağımlılıklardan yarar sağlar.”
- **Related:** beneficial, beneficiary; synonym: advantage

### classpath · noun

- **Türkçe:** sınıf yolu
- **Java bağlamı:** Legacy class ve JAR arama yolu; üzerindeki code unnamed
  module içinde değerlendirilir.
- **Example:** “Code on the classpath belongs to the unnamed module.”
- **Çeviri:** “Classpath üzerindeki kod, isimsiz modüle aittir.”
- **Related:** class-path option; contrast: module path

### compile · verb

- **Türkçe:** derlemek
- **Java bağlamı:** `javac` ile source code'u class file'a dönüştürmek.
- **Example:** “Compile the modules into separate output directories.”
- **Çeviri:** “Modülleri ayrı çıktı dizinlerine derleyin.”
- **Related:** compiler, compilation, compilable

### consumer · noun

- **Türkçe:** tüketici, kullanan bileşen
- **Java bağlamı:** API veya locator üzerinden işlev kullanan module. Service
  aramayı locator'a bırakıyorsa consumer `uses` yazmaz; yalnız doğrudan
  referans verdiği module'ları `requires` eder.
- **Example:** “The consumer calls the locator without requiring a concrete
  provider.”
- **Çeviri:** “Tüketici, somut bir sağlayıcıya bağımlı olmadan servis bulucuyu çağırır.”
- **Related:** consume, consumption; contrast: provider

### cyclic dependency · noun phrase

- **Türkçe:** döngüsel bağımlılık
- **Java bağlamı:** Module'ların birbirini bir cycle oluşturacak biçimde
  require etmesi.
- **Example:** “The compiler rejects a cyclic dependency between explicit
  named modules.”
- **Çeviri:** “Derleyici, açıkça tanımlanmış isimli modüller arasındaki döngüsel bağımlılığı reddeder.”
- **Related:** cycle, cyclic; synonym: circular dependency

## D–H

### dependency · noun

- **Türkçe:** bağımlılık
- **Java bağlamı:** Bir module'ın başka bir module'ın API'sine ihtiyaç duyması.
- **Example:** “The descriptor makes every direct dependency visible.”
- **Çeviri:** “Modül tanımlayıcısı, her doğrudan bağımlılığı görünür kılar.”
- **Related:** depend, dependent, independently

### deploy · verb

- **Türkçe:** dağıtıma almak, konuşlandırmak
- **Java bağlamı:** Compiled module, modular JAR veya runtime image'ı hedef
  ortama sunmak.
- **Example:** “The team deploys the custom runtime with the application.”
- **Çeviri:** “Ekip, özelleştirilmiş çalışma ortamını uygulamayla birlikte dağıtıma alır.”
- **Related:** deployment, deployable

### descriptor · noun

- **Türkçe:** tanımlayıcı
- **Java bağlamı:** `module-info.java` içindeki module declaration.
- **Example:** “The descriptor lists required modules and exported packages.”
- **Çeviri:** “Modül tanımlayıcısı, gereken modülleri ve dışa açılan paketleri listeler.”
- **Related:** describe, description, descriptive

### directive · noun

- **Türkçe:** yönerge, bildirim
- **Java bağlamı:** `requires`, `exports`, `opens`, `uses` ve `provides` gibi
  module declaration öğesi.
- **Example:** “The directives may appear in any order.”
- **Çeviri:** “Yönergeler herhangi bir sırada yer alabilir.”
- **Related:** direct, direction; synonym: instruction

### discover · verb

- **Türkçe:** keşfetmek, bulmak
- **Java bağlamı:** `ServiceLoader` ile provider veya Java tool'larıyla module
  bilgisi bulmak.
- **Example:** “The service loader discovers providers at runtime.”
- **Çeviri:** “Servis yükleyici, sağlayıcıları çalışma zamanında bulur.”
- **Related:** discovery, discoverable

### encapsulate · verb

- **Türkçe:** kapsüllemek
- **Java bağlamı:** Internal package'ları export etmeyerek implementation
  detail'larını module içinde tutmak.
- **Example:** “Modules encapsulate packages that are not part of the API.”
- **Çeviri:** “Modüller, API'nin parçası olmayan paketleri kapsüller.”
- **Related:** encapsulation, encapsulated; antonym: expose

### export · verb / noun

- **Türkçe:** dışa aktarmak; dışa açma
- **Java bağlamı:** Public package API'sini başka module'ların normal erişimine
  açmak.
- **Example:** “The API module exports exactly one package.”
- **Çeviri:** “API modülü tam olarak bir paketi dışa açar.”
- **Related:** exported, exporter; contrast: open

### expose · verb

- **Türkçe:** dışarı açmak, görünür kılmak
- **Java bağlamı:** Package'ı `exports` veya reflection için `opens` ile
  erişilebilir hale getirmek.
- **Example:** “Do not expose implementation packages without a reason.”
- **Çeviri:** “Gerçekleştirim paketlerini gerekçe olmadan dışarı açmayın.”
- **Related:** exposure, exposed; antonym: conceal

## I–M

### implementation · noun

- **Türkçe:** gerçekleştirim, uygulama ayrıntısı
- **Java bağlamı:** Bir service interface'i gerçekleştiren veya API arkasında
  kalan concrete code.
- **Example:** “The provider implementation package does not need to be
  exported.”
- **Çeviri:** “Sağlayıcının gerçekleştirim paketinin dışa açılması gerekmez.”
- **Related:** implement, implementer; contrast: interface

### internal · adjective

- **Türkçe:** iç, dahili
- **Java bağlamı:** Public API'nin parçası olmayan package veya JDK API.
- **Example:** “The analysis reports calls to internal JDK APIs.”
- **Çeviri:** “Analiz, JDK'nin dahili API'lerine yapılan çağrıları raporlar.”
- **Related:** internally, internalize; antonym: external

### invoke · verb

- **Türkçe:** çağırmak
- **Java bağlamı:** Main class, Java tool veya method çalıştırmak.
- **Example:** “Invoke the main class with the module launcher syntax.”
- **Çeviri:** “Ana sınıfı, modül başlatma sözdizimiyle çalıştırın.”
- **Related:** invocation, invocable; synonym: call

### JAR hell · noun phrase

- **Türkçe:** JAR bağımlılık karmaşası
- **Java bağlamı:** Çakışan/missing version ve belirsiz dependency'lerin
  classpath'te yarattığı problem.
- **Example:** “Explicit module dependencies reduce some forms of JAR hell.”
- **Çeviri:** “Açık modül bağımlılıkları, bazı JAR çakışması türlerini azaltır.”
- **Related:** version conflict, dependency conflict

### launcher · noun

- **Türkçe:** başlatıcı
- **Java bağlamı:** `java` command'ının application/module başlatan rolü.
- **Example:** “The launcher expects a slash between the module and class.”
- **Çeviri:** “Başlatıcı, modül ile sınıf arasına eğik çizgi konulmasını bekler.”
- **Related:** launch, launching

### migrate · verb

- **Türkçe:** taşımak, geçiş yapmak
- **Java bağlamı:** Classpath application'ını aşamalı olarak JPMS'e geçirmek.
- **Example:** “The team migrates the lowest-level library first.”
- **Çeviri:** “Ekip önce en alt düzeydeki kütüphaneyi yeni yapıya taşır.”
- **Related:** migration, migratory

### module path · noun phrase

- **Türkçe:** modül yolu
- **Java bağlamı:** Named/automatic module'ların bulunacağı path.
- **Example:** “Place the modular JAR on the module path.”
- **Çeviri:** “Modüler JAR'ı module path üzerine yerleştirin.”
- **Related:** `--module-path`, `-p`; contrast: classpath

## N–R

### named module · noun phrase

- **Türkçe:** adlandırılmış modül
- **Java bağlamı:** Java API anlamında adı bulunan explicit veya automatic
  module. OCP'nin üçlü karşılaştırmalarında “named” çoğunlukla descriptor'lı
  **explicit named module** için kullanılır; automatic module ayrı gösterilir.
- **Example:** “An explicit named module can require another named module.”
- **Çeviri:** “Açıkça tanımlanmış isimli bir modül, başka bir isimli modüle bağımlılık bildirebilir.”
- **Related:** name, naming; contrast: unnamed module

### observable · adjective

- **Türkçe:** gözlemlenebilir, çözümleyici tarafından görülebilir
- **Java bağlamı:** Module resolution sırasında finder'ın görebildiği module.
- **Example:** “Only observable modules can enter the resolved graph.”
- **Çeviri:** “Çözümlenmiş modül grafiğine yalnız keşfedilebilir modüller girebilir.”
- **Related:** observe, observation, observer

### open · verb / adjective

- **Türkçe:** açmak; açık
- **Java bağlamı:** Package'ı deep reflection'a açmak veya bütün module'ı
  `open module` olarak declare etmek.
- **Example:** “Open the model package only to the reflection framework.”
- **Çeviri:** “Model paketini yalnız reflection çatısına açın.”
- **Related:** openness, opening; contrast: export

### package · noun / verb

- **Türkçe:** paket; paketlemek
- **Java bağlamı:** Related type grubu veya compiled code'u JAR'a dönüştürme.
- **Example:** “Package the compiled module as a modular JAR.”
- **Çeviri:** “Derlenmiş modülü modüler bir JAR olarak paketleyin.”
- **Related:** packaging, packaged

### prior to · preposition phrase

- **Türkçe:** -den önce
- **Java bağlamı:** JPMS öncesindeki erişim kuralları veya modüler çalıştırmadan önceki bir adım.
- **Example · özgün:** “Prior to launching the program, inspect its module dependencies.”
- **Çeviri:** “Programı başlatmadan önce modül bağımlılıklarını inceleyin.”
- **Related:** synonym: before; antonym: after; to burada edattır: prior to launching.
- **Kaynak bağlamı:** [using the   jdk internals flag](bilingual_notes.md#using-the---jdk-internals-flag)

### provider · noun

- **Türkçe:** sağlayıcı
- **Java bağlamı:** Service interface için implementation sunan class ve bunu
  `provides ... with ...` ile bildiren module.
- **Example:** “The provider module declares its implementation with
  `provides`.”
- **Çeviri:** “Sağlayıcı modül, gerçekleştirimini `provides` ile bildirir.”
- **Related:** provide, provision; contrast: consumer

### qualified · adjective

- **Türkçe:** sınırlandırılmış, nitelikli
- **Java bağlamı:** `exports ... to` veya `opens ... to` ile yalnız belirli
  target module'lara izin verilmesi.
- **Example:** “A qualified export names its permitted modules.”
- **Çeviri:** “Hedefleri belirtilmiş bir dışa açma yönergesi, izin verilen modülleri adlandırır.”
- **Related:** qualify, qualification; contrast: unqualified

### readability · noun

- **Türkçe:** okunabilirlik ilişkisi
- **Java bağlamı:** Bir module'ın başka module'daki type'lara referans
  verebilmesinin graph düzeyindeki koşulu.
- **Example:** “A transitive requirement passes readability to consumers.”
- **Çeviri:** “Geçişli bağımlılık, tüketicilerin bağımlı olunan modülü de okuyabilmesini sağlar.”
- **Related:** readable, read

### require · verb

- **Türkçe:** gerektirmek
- **Java bağlamı:** Descriptor'da başka module dependency'si bildirmek.
- **Example:** “The care module requires the feeding module.”
- **Çeviri:** “Bakım modülü, besleme modülüne bağımlıdır.”
- **Related:** requirement, required; synonym: depend on

### resolve · verb

- **Türkçe:** çözümlemek
- **Java bağlamı:** Root module ve dependency'lerinden valid module graph
  oluşturmak.
- **Example:** “The launcher resolves the module graph before running main.”
- **Çeviri:** “Başlatıcı, `main` çalışmadan önce modül grafiğini çözümler.”
- **Related:** resolution, resolved, resolver

### runtime image · noun phrase

- **Türkçe:** çalışma zamanı imajı
- **Java bağlamı:** `jlink` ile application için gereken module'lardan üretilen
  özel Java runtime.
- **Example:** “The runtime image contains only the selected module graph.”
- **Çeviri:** “Çalışma ortamı imajı, yalnız seçilen modül grafiğini içerir.”
- **Related:** runtime, image; custom runtime

## S–Z

### service locator · noun phrase

- **Türkçe:** servis bulucu
- **Java bağlamı:** `ServiceLoader` aracılığıyla provider implementation'larını
  bulan locator module/class; consumer bu exported locator API'sini çağırabilir.
- **Example:** “The service locator avoids a direct dependency on providers.”
- **Çeviri:** “Servis bulucu, sağlayıcılara doğrudan bağımlılığı önler.”
- **Related:** locate, location, locator

### split package · noun phrase

- **Türkçe:** bölünmüş paket
- **Java bağlamı:** Standart application configuration'ında aynı package'ın
  birden fazla resolved named module'a bölünmesi.
- **Example:** “A split package may prevent a reliable module configuration.”
- **Çeviri:** “Birden fazla modüle bölünmüş paket, güvenilir bir modül yapılandırılmasını engelleyebilir.”
- **Related:** split, package boundary

### transitive · adjective

- **Türkçe:** geçişli, aktarılan
- **Java bağlamı:** `requires transitive` ile dependency readability'sinin
  consumer'lara aktarılması.
- **Example:** “The API module declares the dependency as transitive because
  its types appear in exported signatures.”
- **Çeviri:** “API modülü, bağımlılığın türleri dışa açılan metot imzalarında göründüğü için bu bağımlılığı geçişli olarak bildirir.”
- **Related:** transitively, transitivity

### unnamed module · noun phrase

- **Türkçe:** adsız modül
- **Java bağlamı:** Classpath üzerindeki code'un ait olduğu, adı ve effective
  descriptor'ı bulunmayan module.
- **Example:** “An explicit named module cannot require the unnamed module by
  name.”
- **Çeviri:** “Açıkça tanımlanmış isimli bir modül, isimsiz modüle adıyla bağımlılık bildiremez.”
- **Related:** unnamed, name; contrast: automatic module

### visibility · noun

- **Türkçe:** görünürlük
- **Java bağlamı:** Java access modifier ve module export/readability
  kurallarının birleşik sonucu.
- **Example:** “Public visibility does not bypass module encapsulation.”
- **Çeviri:** “`public` erişim düzeyi, modül kapsüllemesini aşmaz.”
- **Related:** visible, visibly; antonym: invisibility

### with · preposition / JPMS keyword

- **Türkçe:** ile
- **Java bağlamı:** `provides Service with Implementation` declaration'ında
  service'i implementation'a bağlayan keyword.
- **Example:** “The declaration connects the service to its implementation with
  the `with` keyword.”
- **Çeviri:** “Bildirim, `with` anahtar kelimesiyle servisi gerçekleştirimine bağlar.”
- **Related:** provide with; service declaration

## Karıştırılan anlamları ayır

**readable / accessible:** `readable`, modüller arasındaki okuma ilişkisini; `accessible`, bu ilişkiye ek olarak dışa açma ve Java erişim kurallarının izin verdiği kullanımı anlatır.

`export` normal API erişimini; `open` özellikle derin reflection erişimini düzenler. `observable` bulunabilen adaydır; `resolved` seçilmiş modül grafiğine dahil olandır.

## Kapalı kitap hatırlama · 5 dakika

Her oturumda en fazla 5 kelime seç. Önce Türkçeyi kapatıp İngilizce cümleyi
çevir; ardından İngilizceyi kapatıp Türkçe anlamdan sözcüğü ve kendi örneğini
üret. Yalnız “tanıdık geldi” yanıtını başarı sayma: **0 = çıkaramadım,
1 = anlamını söyledim, 2 = doğru teknik cümlede kullandım**. 0–1 puanlıları
ünite [tekrar rotasına](README.md) göre geri getir.

**Özgün aktarım sorusu:** İstemci modülü hedefi okuyabiliyor ama paket dışa açılmıyor. Neden bu yeterli değil? `readable`, `accessible`, `exported` ile açıkla.

Cevabını yazdıktan sonra kontrol et.

**Örnek yanıt:** The module is readable, but its public type is not accessible because the package is not exported to the client.

## Mini quiz · Vocabulary recall

1. `module-info` olmadan module path'e konan JAR: __________
2. Classpath üzerindeki code'un module type'ı: __________
3. Module graph'ını oluşturmaya verilen fiil: __________
4. Aynı package'ın iki named module'da bulunması: __________
5. Service implementation sunan bileşen: __________
6. Dependency'nin consumer'a aktarılmasını anlatan adjective: __________
7. `jlink` çıktısının genel adı: __________
8. Çakışan legacy JAR dependency karmaşası: __________
9. Bir package'ı deep reflection için açmayı anlatan fiil: __________
10. Bir module'ın diğerini okuyabilme ilişkisi: __________

## Cevaplar

1. automatic module
2. unnamed module
3. resolve
4. split package
5. provider
6. transitive
7. runtime image
8. JAR hell
9. open
10. readability
