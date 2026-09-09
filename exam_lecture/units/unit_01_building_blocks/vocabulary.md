# Unit 01 Vocabulary · Building Blocks

Bu sözlük Unit 01 ana notundaki **Java environment**, **class structure**,
**classpath**, **object initialization**, **data types**, **scope** ve
**garbage collection** bağlamlarından seçilmiştir. Kelimeleri tek başına ezberlemek yerine
örnek cümledeki teknik bağlamla birlikte çalış.

> **Memory tip:** Önce Türkçe tarafı kapatıp İngilizce kelimenin anlamını
> hatırla; sonra İngilizce tarafı kapatıp Türkçe anlamdan kelimeyi geri çağır.
> Son olarak ikisini de kapatıp bir Java cümlesi kur.

## A–C

### accessible · adjective

- **Türkçe:** erişilebilir
- **Teknik bağlam:** Programın hâlâ bir reference zinciri üzerinden ulaşabildiği
  object'i anlatır.
- **Example:** The object is eligible when no accessible references remain.
- **Çeviri:** Erişilebilir hiçbir reference kalmadığında object eligible olur.
- **Word family:** access (n./v.), accessibility (n.); **antonym:** inaccessible

### alternatively · adverb

- **Türkçe:** alternatif olarak, başka bir seçenek olarak
- **Teknik bağlam:** Aynı işlemi yapan ikinci bir komut veya yaklaşım sunar.
- **Example:** Alternatively, you can specify a different output directory.
- **Çeviri:** Alternatif olarak farklı bir çıktı dizini belirtebilirsin.
- **Related:** alternative (n./adj.), option (n.); **synonym:** instead

### ambiguous · adjective

- **Türkçe:** belirsiz, birden fazla yoruma açık
- **Teknik bağlam:** Aynı simple name'i sağlayan import'lar compiler açısından
  hangi class'ın kullanılacağını belirsiz hâle getirir.
- **Example:** The imports are ambiguous because both packages contain `Date`.
- **Çeviri:** Her iki package da `Date` içerdiği için import'lar belirsizdir.
- **Word family:** ambiguity (n.); **antonym:** unambiguous

### archive · noun / verb

- **Türkçe:** arşiv; arşivlemek
- **Teknik bağlam:** JAR, class ve kaynak dosyalarını taşıyabilen ZIP tabanlı bir
  archive biçimidir.
- **Example:** The tool creates an archive containing the compiled classes.
- **Çeviri:** Araç, derlenmiş sınıfları içeren bir arşiv oluşturur.
- **Word family:** archival (adj.), archive (v.)

### associated · adjective

- **Türkçe:** ilişkili, bağlantılı
- **Teknik bağlam:** Bir reference variable ile onun işaret ettiği object
  arasındaki bağı niteler.
- **Example:** A final variable does not keep its associated object alive.
- **Çeviri:** Final variable, ilişkili object'ini hayatta tutmaz.
- **Word family:** associate (v.), association (n.); **synonym:** related

### assume · verb

- **Türkçe:** varsaymak, kabul etmek
- **Teknik bağlam:** Soruda açıkça aksi söylenmediğinde kullanılacak kabulü
  belirtir.
- **Example:** Assume that the public classes are in separate files.
- **Çeviri:** Public sınıfların ayrı dosyalarda olduğunu varsay.
- **Word family:** assumption (n.); **synonym:** suppose

### available · adjective

- **Türkçe:** mevcut, kullanılabilir
- **Teknik bağlam:** Bir araçta başka seçeneklerin de bulunduğunu söyler.
- **Example:** Many other command-line options are available.
- **Çeviri:** Başka birçok komut satırı seçeneği mevcuttur.
- **Word family:** availability (n.); **antonym:** unavailable

### classpath · noun

- **Türkçe:** sınıf arama yolu
- **Teknik bağlam:** `javac` veya `java` aracının class ve JAR dosyalarını
  arayacağı konumlar dizisi.
- **Example:** Add the library to the classpath before running the program.
- **Çeviri:** Programı çalıştırmadan önce kütüphaneyi classpath'e ekle.
- **Related:** path (n.), class loader (n.)

### compatible · adjective

- **Türkçe:** uyumlu
- **Teknik bağlam:** Bytecode'u çalıştırabilen JVM veya birlikte çalışabilen
  sürümleri anlatır.
- **Example:** A compatible JVM can run the compiled bytecode.
- **Çeviri:** Uyumlu bir JVM derlenmiş bytecode'u çalıştırabilir.
- **Word family:** compatibility (n.); **antonym:** incompatible

### compile · verb

- **Türkçe:** derlemek
- **Teknik bağlam:** Java source code'u bytecode içeren `.class` dosyasına
  dönüştürmek.
- **Example:** The source file does not compile because the declarations are out
  of order.
- **Çeviri:** Bildirimler yanlış sırada olduğu için kaynak dosya derlenmez.
- **Word family:** compiler (n.), compilation (n.), compiled (adj.)

### contain · verb

- **Türkçe:** içermek
- **Teknik bağlam:** Bir JAR'ın veya class'ın içinde bulunan öğeleri anlatır.
- **Example:** The JAR contains several class files.
- **Çeviri:** JAR birkaç class dosyası içerir.
- **Word family:** container (n.), content (n.); **synonym:** include

### current directory · noun phrase

- **Türkçe:** mevcut/geçerli dizin
- **Teknik bağlam:** Classpath içinde nokta (`.`) ile gösterilir.
- **Example:** A period represents the current directory.
- **Çeviri:** Nokta, mevcut dizini temsil eder.
- **Related:** working directory, path

## D–I

### declaration · noun

- **Türkçe:** bildirim
- **Teknik bağlam:** Bir package, class, field veya method'un programa
  tanıtılması.
- **Example:** A package declaration must precede the import statements.
- **Çeviri:** Package bildirimi import ifadelerinden önce gelmelidir.
- **Word family:** declare (v.), declarative (adj.)

### definite assignment · noun phrase

- **Türkçe:** kesin atanmışlık
- **Teknik bağlam:** Compiler'ın local variable'ın okunmadan önce her reachable
  path'te değer aldığını kanıtlaması.
- **Example:** Definite assignment is checked at compile time.
- **Çeviri:** Kesin atanmışlık compile time'da kontrol edilir.
- **Related:** initialize, reachable path

### eligibility · noun

- **Türkçe:** uygunluk, hak kazanma durumu
- **Teknik bağlam:** Bir object'in garbage collection için artık reachable
  olmaması.
- **Example:** Scope loss alone does not guarantee garbage collection eligibility.
- **Çeviri:** Yalnız scope kaybı garbage collection uygunluğunu garanti etmez.
- **Word family:** eligible (adj.)

### elsewhere · adverb

- **Türkçe:** başka bir yerde
- **Teknik bağlam:** Class dosyalarının mevcut dizinden farklı bir konumda
  bulunmasını anlatır.
- **Example:** Use a classpath when the required classes are located elsewhere.
- **Çeviri:** Gerekli sınıflar başka bir yerde bulunuyorsa classpath kullan.
- **Related:** somewhere, anywhere; **antonym:** here

### essential whitespace · noun phrase

- **Türkçe:** değerin parçası olarak kalan boşluk
- **Teknik bağlam:** Text block içinde biçimsel ortak girinti temizlendikten sonra kalan anlamlı boşluk.
- **Example:** The text block keeps its essential whitespace.
- **Çeviri:** Metin bloğu, değerinin parçası olan boşlukları korur.
- **Word family / karşılaştırma:** essential (adj.); karşıt bağlam: incidental whitespace
- **Kaynak bağlam:** [İlgili ana not](bilingual_notes.md#defining-text-blocks).

### explicitly · adverb

- **Türkçe:** açıkça, doğrudan
- **Teknik bağlam:** Bir konumun, constructor'ın veya koşulun kullanıcı
  tarafından açıkça belirtilmesi.
- **Example:** The developer explicitly declared a constructor.
- **Çeviri:** Geliştirici açıkça bir constructor bildirdi.
- **Word family:** explicit (adj.); **antonym:** implicitly

### field · noun

- **Türkçe:** alan, üye değişken
- **Teknik bağlam:** Class gövdesinde tanımlanan ve object/class durumunu taşıyan
  variable.
- **Example:** The constructor assigns a value to the field.
- **Çeviri:** Constructor field'a bir değer atar.
- **Related:** instance variable, member variable

### frequently · adverb

- **Türkçe:** sık sık, sıklıkla
- **Teknik bağlam:** Geliştiricilerin yaygın bir seçimini veya sınavda sık
  görülen durumu anlatır.
- **Example:** Developers frequently use the short classpath option.
- **Çeviri:** Geliştiriciler kısa classpath seçeneğini sıklıkla kullanır.
- **Word family:** frequent (adj.), frequency (n.); **synonym:** often

### guarantee · noun / verb

- **Türkçe:** garanti, güvence; garanti etmek
- **Teknik bağlam:** Bir olayın mutlaka gerçekleşeceğine ilişkin kesinlik. GC'ye
  uygunluk, belleğin hemen geri kazanılacağını garanti etmez.
- **Example:** Calling `System.gc()` does not guarantee that collection occurs.
- **Çeviri:** `System.gc()` çağrısı, çöp toplamanın gerçekleşeceğini garanti etmez.
- **Word family:** guaranteed (adj./V3), guarantee (n./v.); **related:** ensure
- **Anlam ayrımı:** `eligible` = koşulları karşılayan; `guaranteed` = gerçekleşmesi
  güvence altına alınmış. “Uygun” ile “kesin” aynı şey değildir.
- **Kaynak bağlam:** [Understanding Garbage Collection](bilingual_notes.md#understanding-garbage-collection).

### incidental whitespace · noun phrase

- **Türkçe:** rastlantısal/biçimsel girinti boşluğu
- **Teknik bağlam:** Text block source code'unu okunur kılan, fakat String
  değerinin zorunlu bir parçası olmayan whitespace.
- **Example:** Java removes incidental whitespace from a text block.
- **Çeviri:** Java, text block'taki incidental whitespace'i kaldırır.
- **Antonym:** essential whitespace

### include · verb

- **Türkçe:** içermek, dahil etmek
- **Teknik bağlam:** Bir dizini ya da JAR'ı classpath kapsamına almak.
- **Example:** The wildcard does not include JARs in subdirectories.
- **Çeviri:** Wildcard, alt dizinlerdeki JAR'ları dahil etmez.
- **Word family:** inclusion (n.), inclusive (adj.); **antonym:** exclude

### independently · adverb

- **Türkçe:** birbirinden bağımsız olarak
- **Teknik bağlam:** Her seçeneğin diğerleri eklenmeden ayrı ayrı denenmesini
  belirtir.
- **Example:** Insert each declaration independently into the method.
- **Çeviri:** Her declaration'ı method'a birbirinden bağımsız olarak yerleştir.
- **Word family:** independent (adj.), independence (n.); **antonym:** dependently

### initialize · verb

- **Türkçe:** başlangıç değeri vermek, ilklendirmek
- **Teknik bağlam:** Field veya object'i ilk kullanılabilir durumuna getirmek.
- **Example:** The constructor initializes the name field.
- **Çeviri:** Constructor, `name` field'ına başlangıç değeri verir.
- **Word family:** initialization (n.), initializer (n.), initial (adj.)

### instance · noun

- **Türkçe:** örnek
- **Teknik bağlam:** Bir class'tan oluşturulan somut object.
- **Example:** Each call to `new Bird()` creates a new instance.
- **Çeviri:** Her `new Bird()` çağrısı yeni bir örnek oluşturur.
- **Related:** object; **phrase:** instance of

## L–R

### lazy · adjective

- **Türkçe:** tembel
- **Teknik bağlam:** Kaynak metinde kısa `-cp` yazımını seçen geliştiricileri
  mizahi biçimde anlatır.
- **Example:** Lazy typists tend to prefer shorter options.
- **Çeviri:** Yazmaya üşenenler daha kısa seçenekleri tercih etme eğilimindedir.
- **Word family:** laziness (n.), lazily (adv.); **antonym:** diligent

### lifetime · noun

- **Türkçe:** yaşam süresi
- **Teknik bağlam:** Nesnenin yaratılmasıyla belleğinin geri kazanılması
  arasındaki yaşam süresi. Erişilemez olmak, belleğin o anda geri kazanıldığı
  anlamına gelmez; scope ise kaynak koddaki görünürlük bölgesidir.
- **Example:** A variable's scope and an object's lifetime are different concepts.
- **Çeviri:** Variable scope'u ile object yaşam süresi farklı kavramlardır.
- **Related:** lifecycle, reachability

### locate · verb

- **Türkçe:** yerini bulmak; bir yerde bulunmak
- **Teknik bağlam:** Class veya JAR dosyasının konumunu belirtmek/bulmak.
- **Example:** Java must locate the class before it can run the program.
- **Çeviri:** Java, programı çalıştırabilmeden önce sınıfın yerini bulmalıdır.
- **Word family:** location (n.), located (adj.); **synonym:** find

### match · verb

- **Türkçe:** eşleştirmek, eşleşmek
- **Teknik bağlam:** Wildcard'ın belirli dosya adlarını kapsaması.
- **Example:** The asterisk matches all JAR files in the directory.
- **Çeviri:** Yıldız işareti dizindeki tüm JAR dosyalarıyla eşleşir.
- **Word family:** matching (n./adj.); **antonym:** mismatch

### maximum · adjective / noun

- **Türkçe:** en fazla; azami değer
- **Teknik bağlam:** Kaldırılabilecek import sayısının üst sınırını sorar.
- **Example:** What is the maximum number of removable imports?
- **Çeviri:** Kaldırılabilir import'ların en fazla sayısı kaçtır?
- **Related:** minimum; **synonym:** greatest

### merely · adverb

- **Türkçe:** yalnızca, sadece
- **Teknik bağlam:** Bir kuralın düşündüğümüzden daha sınırlı olduğunu vurgular.
- **Example:** Fields merely have to remain inside a class body.
- **Çeviri:** Field'ların yalnızca bir class gövdesi içinde bulunması gerekir.
- **Synonym:** simply, only

### otherwise · adverb

- **Türkçe:** aksi, başka türlü; aksi takdirde
- **Teknik bağlam:** `unless the question says otherwise`, soru açıkça başka
  bir durum belirtmediği sürece verilen varsayımı korumanı ister.
- **Example:** Assume separate files unless the question says otherwise.
- **Çeviri:** Soru aksini söylemedikçe dosyaların ayrı olduğunu varsay.
- **Anlam ayrımı:** `says otherwise` = aksini söyler; `Do X; otherwise, Y` =
  X'i yap; aksi takdirde Y. Her kullanımda “aksi takdirde” diye çevrilmez.
- **Related:** differently, or else (bağlama göre)
- **Kaynak bağlam:** [Classes and Source Files](bilingual_notes.md#classes-and-source-files);
  koşul çözümlemesi için [grammar notu](grammar_notes.md#6-koşul-yapıları-if-ve-unless).

### parentheses · plural noun

- **Türkçe:** parantezler
- **Teknik bağlam:** Constructor/method çağrılarındaki `()` işaretleri. Süslü
  parantezler için doğru terim `braces` (`{}`) olur.
- **Example:** Add parentheses after the class name to call the constructor.
- **Çeviri:** Constructor'ı çağırmak için class adından sonra parantez ekle.
- **Related:** parenthesis (singular), braces, brackets

### precede · verb

- **Türkçe:** önce gelmek
- **Teknik bağlam:** Java bildirimlerinin zorunlu sırasını anlatır.
- **Example:** The package declaration must precede every import.
- **Çeviri:** Package bildirimi her import'tan önce gelmelidir.
- **Word family:** preceding (adj.); **antonym:** follow

### purpose · noun

- **Türkçe:** amaç
- **Teknik bağlam:** Constructor veya bir komut seçeneğinin görevini açıklar.
- **Example:** The purpose of a constructor is to initialize a new object.
- **Çeviri:** Constructor'ın amacı yeni bir nesneyi başlatmaktır.
- **Word family:** purposeful (adj.), purposely (adv.); **synonym:** aim

### reachable · adjective

- **Türkçe:** erişilebilir, ulaşılabilir
- **Teknik bağlam:** Bir object'e live reference zinciriyle hâlâ ulaşılabildiğini
  belirtir.
- **Example:** The object remains reachable through the first reference.
- **Çeviri:** Object ilk reference üzerinden erişilebilir kalır.
- **Word family:** reach (v./n.), reachability (n.); **antonym:** unreachable

### reclaim · verb

- **Türkçe:** geri kazanmak
- **Teknik bağlam:** JVM'in unreachable object'lerin kapladığı memory'yi yeniden
  kullanılabilir hâle getirmesini anlatır.
- **Example:** Garbage collection may reclaim memory for other objects.
- **Çeviri:** Garbage collection başka object'ler için memory'yi geri kazanabilir.
- **Word family:** reclamation (n.); **synonym:** recover

### redundant · adjective

- **Türkçe:** gereksiz, fazladan
- **Teknik bağlam:** Kaldırılması kodun anlamını veya derlenmesini değiştirmeyen import.
- **Example:** An import from java.lang is redundant here.
- **Çeviri:** Burada java.lang paketinden yapılan import gereksizdir.
- **Word family / karşılaştırma:** redundancy (n.); unnecessary
- **Kaynak bağlam:** [İlgili ana not](bilingual_notes.md#redundant-imports).

### require · verb

- **Türkçe:** gerektirmek
- **Teknik bağlam:** Bir komutun, syntax kuralının veya işlemin zorunlu
  girdilerini belirtir.
- **Example:** The long option requires two dashes.
- **Çeviri:** Uzun seçenek iki tire gerektirir.
- **Word family:** requirement (n.), required (adj.); **synonym:** necessitate

### restricted identifier · noun phrase

- **Türkçe:** kısıtlı tanımlayıcı
- **Teknik bağlam:** `var` gibi yalnız belirli syntax konumlarında özel anlamı
  olan identifier.
- **Example:** `var` is a restricted identifier, not a dynamic type.
- **Çeviri:** `var` kısıtlı bir tanımlayıcıdır, dynamic type değildir.
- **Related:** identifier, keyword

## S–W

### run · verb

- **Türkçe:** çalışmak, çalıştırmak
- **Teknik bağlam:** Bir programı JVM üzerinde yürütmek; bağlama göre bir
  initializer'ın yürütülmesi.
- **Example:** The constructor runs after the instance initializer blocks.
- **Çeviri:** Constructor, instance initializer block'larından sonra çalışır.
- **Related:** execute (v.), execution (n.), runtime (n./adj.)

### snippet · noun

- **Türkçe:** kısa kod parçası
- **Teknik bağlam:** Tam program olmayan, belirli bir kuralı ölçen küçük code
  example.
- **Example:** Determine whether the snippet compiles.
- **Çeviri:** Kod parçasının derlenip derlenmediğini belirle.
- **Related:** code fragment, extract

### specify · verb

- **Türkçe:** belirtmek
- **Teknik bağlam:** Classpath, dizin veya dosya adını komuta açıkça vermek.
- **Example:** Specify the classpath before the main class name.
- **Çeviri:** Main class adından önce classpath'i belirt.
- **Word family:** specification (n.), specific (adj.); **synonym:** state

### statement · noun

- **Türkçe:** ifade, deyim
- **Teknik bağlam:** Programda bir eylemi gerçekleştiren Java instruction;
  kaynak metinde `import statement` kalıbında da geçer.
- **Example:** The `println` statement displays the field value.
- **Çeviri:** `println` ifadesi field değerini gösterir.
- **Word family:** state (v.), stated (adj.)

### supply · verb

- **Türkçe:** sağlamak, temin etmek
- **Teknik bağlam:** Compiler'ın otomatik olarak default constructor eklemesi.
- **Example:** The compiler supplies a default constructor when none is declared.
- **Çeviri:** Hiç constructor bildirilmediğinde compiler bir default constructor
  sağlar.
- **Word family:** supplier (n.); **synonym:** provide

### throughout · preposition / adverb

- **Türkçe:** boyunca, tamamında
- **Teknik bağlam:** Bir kitap veya programın tüm kapsamına yayılan kuralı
  belirtir.
- **Example:** This convention is used throughout the chapter.
- **Çeviri:** Bu kullanım bölümün tamamında uygulanır.
- **Related:** across, during

### throwaway · adjective

- **Türkçe:** geçici, sonradan atılacak
- **Teknik bağlam:** Default package'ın yalnızca kısa ömürlü deneme kodu için
  uygun olduğunu anlatır.
- **Example:** Use the default package only for throwaway code.
- **Çeviri:** Default package'ı yalnızca geçici kod için kullan.
- **Synonym:** disposable; **related:** temporary

### trailing whitespace · noun phrase

- **Türkçe:** satır sonundaki boşluk karakterleri
- **Teknik bağlam:** Text block satırında görünen son karakterden sonra korunan
  space veya tab karakterlerini anlatır.
- **Example:** The `\s` escape preserves trailing whitespace.
- **Çeviri:** `\s` escape'i satır sonundaki boşluğu korur.
- **Related:** leading whitespace, indentation

### wildcard · noun

- **Türkçe:** joker karakter
- **Teknik bağlam:** Birden fazla dosya veya adı eşleştiren `*` gibi sembol.
- **Example:** A wildcard can match every JAR in one directory.
- **Çeviri:** Bir wildcard tek bir dizindeki her JAR'ı eşleştirebilir.
- **Related:** asterisk, pattern matching

## Hızlı eşleştirme

Kelimeleri anlamlarıyla eşleştir:

1. `precede`
2. `supply`
3. `elsewhere`
4. `wildcard`
5. `initialize`

A. başka bir yerde\
B. başlangıç değeri vermek\
C. önce gelmek\
D. sağlamak\
E. joker karakter

## Cevap anahtarı

1-C, 2-D, 3-A, 4-E, 5-B

## Kısa tekrar özeti

- Komut kelimeleri: `specify`, `include`, `locate`, `match`, `require`
- Class yapısı: `declaration`, `field`, `instance`, `initialize`
- YDS bağlaç/zarfları: `alternatively`, `elsewhere`, `explicitly`, `frequently`,
  `merely`, `throughout`
- Temel karşıtlıklar: include ↔ exclude, available ↔ unavailable, precede ↔
  follow

## 5 dakikalık aktif tekrar

Notlara bakmadan aşağıdaki görevleri tamamla:

1. `compile`, `run` ve `initialize` fiillerinin farkını birer cümleyle açıkla.
2. “Package bildirimi import'lardan önce gelmelidir.” cümlesini `precede`
   kullanarak İngilizce yaz.
3. `include` kelimesinin karşıt anlamlısını söyle.
4. `classpath`, `current directory` ve `wildcard` kelimelerini aynı teknik
   cümlede kullan.
5. `explicitly` ve `implicitly` arasındaki anlam farkını default constructor
   üzerinden açıkla.

> **Self-check:** Bir kelimenin Türkçe karşılığını bilmek ilk adımdır. Hedef,
> kelimeyi yeni bir Java cümlesinde doğru sözcük türüyle kullanabilmektir.
