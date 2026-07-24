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
- **Çeviri:** “Export edilmiş public type, yalnız client onun module'ını
  okuyorsa erişilebilirdir.”
- **Related:** access, accessibility; antonym: inaccessible

### automatic module · noun phrase

- **Türkçe:** otomatik modül
- **Java bağlamı:** Explicit module descriptor (`module-info`) içermeyen fakat
  module path'e konduğu için isim kazanan legacy JAR.
- **Example:** “The legacy JAR becomes an automatic module on the module path.”
- **Çeviri:** “Legacy JAR, module path üzerinde automatic module olur.”
- **Related:** automatically; contrast: explicit named module, unnamed module

### benefit · noun / verb

- **Türkçe:** yarar; yarar sağlamak
- **Java bağlamı:** Encapsulation, dependency control ve daha küçük runtime
  image gibi JPMS kazanımları.
- **Example:** “A modular application benefits from explicit dependencies.”
- **Çeviri:** “Modular application explicit dependency'lerden yararlanır.”
- **Related:** beneficial, beneficiary; synonym: advantage

### classpath · noun

- **Türkçe:** sınıf yolu
- **Java bağlamı:** Legacy class ve JAR arama yolu; üzerindeki code unnamed
  module içinde değerlendirilir.
- **Example:** “Code on the classpath belongs to the unnamed module.”
- **Çeviri:** “Classpath üzerindeki code unnamed module'a aittir.”
- **Related:** class-path option; contrast: module path

### compile · verb

- **Türkçe:** derlemek
- **Java bağlamı:** `javac` ile source code'u class file'a dönüştürmek.
- **Example:** “Compile the modules into separate output directories.”
- **Çeviri:** “Module'ları ayrı output directory'lere derleyin.”
- **Related:** compiler, compilation, compilable

### consumer · noun

- **Türkçe:** tüketici, kullanan bileşen
- **Java bağlamı:** API veya locator üzerinden işlev kullanan module. Service
  aramayı locator'a bırakıyorsa consumer `uses` yazmaz; yalnız doğrudan
  referans verdiği module'ları `requires` eder.
- **Example:** “The consumer calls the locator without requiring a concrete
  provider.”
- **Çeviri:** “Consumer concrete provider'ı require etmeden locator'ı çağırır.”
- **Related:** consume, consumption; contrast: provider

### cyclic dependency · noun phrase

- **Türkçe:** döngüsel bağımlılık
- **Java bağlamı:** Module'ların birbirini bir cycle oluşturacak biçimde
  require etmesi.
- **Example:** “The compiler rejects a cyclic dependency between explicit
  named modules.”
- **Çeviri:** “Compiler explicit named module'lar arasındaki cyclic
  dependency'yi reddeder.”
- **Related:** cycle, cyclic; synonym: circular dependency

## D–H

### dependency · noun

- **Türkçe:** bağımlılık
- **Java bağlamı:** Bir module'ın başka bir module'ın API'sine ihtiyaç duyması.
- **Example:** “The descriptor makes every direct dependency visible.”
- **Çeviri:** “Descriptor her direct dependency'yi görünür kılar.”
- **Related:** depend, dependent, independently

### deploy · verb

- **Türkçe:** dağıtıma almak, konuşlandırmak
- **Java bağlamı:** Compiled module, modular JAR veya runtime image'ı hedef
  ortama sunmak.
- **Example:** “The team deploys the custom runtime with the application.”
- **Çeviri:** “Ekip custom runtime'ı application ile birlikte deploy eder.”
- **Related:** deployment, deployable

### descriptor · noun

- **Türkçe:** tanımlayıcı
- **Java bağlamı:** `module-info.java` içindeki module declaration.
- **Example:** “The descriptor lists required modules and exported packages.”
- **Çeviri:** “Descriptor required module'ları ve exported package'ları
  listeler.”
- **Related:** describe, description, descriptive

### directive · noun

- **Türkçe:** yönerge, bildirim
- **Java bağlamı:** `requires`, `exports`, `opens`, `uses` ve `provides` gibi
  module declaration öğesi.
- **Example:** “The directives may appear in any order.”
- **Çeviri:** “Directive'ler herhangi bir sırada bulunabilir.”
- **Related:** direct, direction; synonym: instruction

### discover · verb

- **Türkçe:** keşfetmek, bulmak
- **Java bağlamı:** `ServiceLoader` ile provider veya Java tool'larıyla module
  bilgisi bulmak.
- **Example:** “The service loader discovers providers at runtime.”
- **Çeviri:** “Service loader provider'ları runtime'da keşfeder.”
- **Related:** discovery, discoverable

### encapsulate · verb

- **Türkçe:** kapsüllemek
- **Java bağlamı:** Internal package'ları export etmeyerek implementation
  detail'larını module içinde tutmak.
- **Example:** “Modules encapsulate packages that are not part of the API.”
- **Çeviri:** “Module'lar API'nin parçası olmayan package'ları encapsulate
  eder.”
- **Related:** encapsulation, encapsulated; antonym: expose

### export · verb / noun

- **Türkçe:** dışa aktarmak; dışa açma
- **Java bağlamı:** Public package API'sini başka module'ların normal erişimine
  açmak.
- **Example:** “The API module exports exactly one package.”
- **Çeviri:** “API module tam olarak bir package'ı export eder.”
- **Related:** exported, exporter; contrast: open

### expose · verb

- **Türkçe:** dışarı açmak, görünür kılmak
- **Java bağlamı:** Package'ı `exports` veya reflection için `opens` ile
  erişilebilir hale getirmek.
- **Example:** “Do not expose implementation packages without a reason.”
- **Çeviri:** “Implementation package'larını gerekçe olmadan dışarı açmayın.”
- **Related:** exposure, exposed; antonym: conceal

## I–M

### implementation · noun

- **Türkçe:** gerçekleştirim, uygulama ayrıntısı
- **Java bağlamı:** Bir service interface'i gerçekleştiren veya API arkasında
  kalan concrete code.
- **Example:** “The provider implementation package does not need to be
  exported.”
- **Çeviri:** “Provider implementation package'ının export edilmesi gerekmez.”
- **Related:** implement, implementer; contrast: interface

### internal · adjective

- **Türkçe:** iç, dahili
- **Java bağlamı:** Public API'nin parçası olmayan package veya JDK API.
- **Example:** “The analysis reports calls to internal JDK APIs.”
- **Çeviri:** “Analiz internal JDK API çağrılarını raporlar.”
- **Related:** internally, internalize; antonym: external

### invoke · verb

- **Türkçe:** çağırmak
- **Java bağlamı:** Main class, Java tool veya method çalıştırmak.
- **Example:** “Invoke the main class with the module launcher syntax.”
- **Çeviri:** “Main class'ı module launcher syntax'ı ile çağırın.”
- **Related:** invocation, invocable; synonym: call

### JAR hell · noun phrase

- **Türkçe:** JAR bağımlılık karmaşası
- **Java bağlamı:** Çakışan/missing version ve belirsiz dependency'lerin
  classpath'te yarattığı problem.
- **Example:** “Explicit module dependencies reduce some forms of JAR hell.”
- **Çeviri:** “Explicit module dependency'leri JAR hell'in bazı biçimlerini
  azaltır.”
- **Related:** version conflict, dependency conflict

### launcher · noun

- **Türkçe:** başlatıcı
- **Java bağlamı:** `java` command'ının application/module başlatan rolü.
- **Example:** “The launcher expects a slash between the module and class.”
- **Çeviri:** “Launcher module ile class arasında slash bekler.”
- **Related:** launch, launching

### migrate · verb

- **Türkçe:** taşımak, geçiş yapmak
- **Java bağlamı:** Classpath application'ını aşamalı olarak JPMS'e geçirmek.
- **Example:** “The team migrates the lowest-level library first.”
- **Çeviri:** “Ekip önce en alt seviyedeki library'yi migrate eder.”
- **Related:** migration, migratory

### module path · noun phrase

- **Türkçe:** modül yolu
- **Java bağlamı:** Named/automatic module'ların bulunacağı path.
- **Example:** “Place the modular JAR on the module path.”
- **Çeviri:** “Modular JAR'ı module path üzerine koyun.”
- **Related:** `--module-path`, `-p`; contrast: classpath

## N–R

### named module · noun phrase

- **Türkçe:** adlandırılmış modül
- **Java bağlamı:** Java API anlamında adı bulunan explicit veya automatic
  module. OCP'nin üçlü karşılaştırmalarında “named” çoğunlukla descriptor'lı
  **explicit named module** için kullanılır; automatic module ayrı gösterilir.
- **Example:** “An explicit named module can require another named module.”
- **Çeviri:** “Explicit named module başka bir named module'ı require
  edebilir.”
- **Related:** name, naming; contrast: unnamed module

### observable · adjective

- **Türkçe:** gözlemlenebilir, çözümleyici tarafından görülebilir
- **Java bağlamı:** Module resolution sırasında finder'ın görebildiği module.
- **Example:** “Only observable modules can enter the resolved graph.”
- **Çeviri:** “Yalnız observable module'lar resolved graph'a girebilir.”
- **Related:** observe, observation, observer

### open · verb / adjective

- **Türkçe:** açmak; açık
- **Java bağlamı:** Package'ı deep reflection'a açmak veya bütün module'ı
  `open module` olarak declare etmek.
- **Example:** “Open the model package only to the reflection framework.”
- **Çeviri:** “Model package'ını yalnız reflection framework'e açın.”
- **Related:** openness, opening; contrast: export

### package · noun / verb

- **Türkçe:** paket; paketlemek
- **Java bağlamı:** Related type grubu veya compiled code'u JAR'a dönüştürme.
- **Example:** “Package the compiled module as a modular JAR.”
- **Çeviri:** “Compiled module'ı modular JAR olarak package edin.”
- **Related:** packaging, packaged

### provider · noun

- **Türkçe:** sağlayıcı
- **Java bağlamı:** Service interface için implementation sunan class ve bunu
  `provides ... with ...` ile bildiren module.
- **Example:** “The provider module declares its implementation with
  `provides`.”
- **Çeviri:** “Provider module implementation'ını `provides` ile declare eder.”
- **Related:** provide, provision; contrast: consumer

### qualified · adjective

- **Türkçe:** sınırlandırılmış, nitelikli
- **Java bağlamı:** `exports ... to` veya `opens ... to` ile yalnız belirli
  target module'lara izin verilmesi.
- **Example:** “A qualified export names its permitted modules.”
- **Çeviri:** “Qualified export izin verilen module'ları adlandırır.”
- **Related:** qualify, qualification; contrast: unqualified

### readability · noun

- **Türkçe:** okunabilirlik ilişkisi
- **Java bağlamı:** Bir module'ın başka module'daki type'lara referans
  verebilmesinin graph düzeyindeki koşulu.
- **Example:** “A transitive requirement passes readability to consumers.”
- **Çeviri:** “Transitive requirement readability'yi consumer'lara aktarır.”
- **Related:** readable, read

### require · verb

- **Türkçe:** gerektirmek
- **Java bağlamı:** Descriptor'da başka module dependency'si bildirmek.
- **Example:** “The care module requires the feeding module.”
- **Çeviri:** “Care module feeding module'ını require eder.”
- **Related:** requirement, required; synonym: depend on

### resolve · verb

- **Türkçe:** çözümlemek
- **Java bağlamı:** Root module ve dependency'lerinden valid module graph
  oluşturmak.
- **Example:** “The launcher resolves the module graph before running main.”
- **Çeviri:** “Launcher main'i çalıştırmadan önce module graph'ını resolve
  eder.”
- **Related:** resolution, resolved, resolver

### runtime image · noun phrase

- **Türkçe:** çalışma zamanı imajı
- **Java bağlamı:** `jlink` ile application için gereken module'lardan üretilen
  özel Java runtime.
- **Example:** “The runtime image contains only the selected module graph.”
- **Çeviri:** “Runtime image yalnız seçilen module graph'ını içerir.”
- **Related:** runtime, image; custom runtime

## S–Z

### service locator · noun phrase

- **Türkçe:** servis bulucu
- **Java bağlamı:** `ServiceLoader` aracılığıyla provider implementation'larını
  bulan locator module/class; consumer bu exported locator API'sini çağırabilir.
- **Example:** “The service locator avoids a direct dependency on providers.”
- **Çeviri:** “Service locator provider'lara direct dependency kurulmasını
  önler.”
- **Related:** locate, location, locator

### split package · noun phrase

- **Türkçe:** bölünmüş paket
- **Java bağlamı:** Standart application configuration'ında aynı package'ın
  birden fazla resolved named module'a bölünmesi.
- **Example:** “A split package prevents a reliable module configuration.”
- **Çeviri:** “Split package güvenilir module configuration'ını engeller.”
- **Related:** split, package boundary

### transitive · adjective

- **Türkçe:** geçişli, aktarılan
- **Java bağlamı:** `requires transitive` ile dependency readability'sinin
  consumer'lara aktarılması.
- **Example:** “The API module declares the dependency as transitive because
  its types appear in exported signatures.”
- **Çeviri:** “API module, type'ları exported signature'larda yer aldığı için
  dependency'yi transitive olarak declare eder.”
- **Related:** transitively, transitivity

### unnamed module · noun phrase

- **Türkçe:** adsız modül
- **Java bağlamı:** Classpath üzerindeki code'un ait olduğu, adı ve effective
  descriptor'ı bulunmayan module.
- **Example:** “An explicit named module cannot require the unnamed module by
  name.”
- **Çeviri:** “Explicit named module unnamed module'ı adıyla require edemez.”
- **Related:** unnamed, name; contrast: automatic module

### visibility · noun

- **Türkçe:** görünürlük
- **Java bağlamı:** Java access modifier ve module export/readability
  kurallarının birleşik sonucu.
- **Example:** “Public visibility does not bypass module encapsulation.”
- **Çeviri:** “Public visibility module encapsulation'ı aşmaz.”
- **Related:** visible, visibly; antonym: invisibility

### with · preposition / JPMS keyword

- **Türkçe:** ile
- **Java bağlamı:** `provides Service with Implementation` declaration'ında
  service'i implementation'a bağlayan keyword.
- **Example:** “The declaration connects the service to its implementation with
  the `with` keyword.”
- **Çeviri:** “Declaration, `with` keyword'ü ile service'i implementation'ına
  bağlar.”
- **Related:** provide with; service declaration

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
