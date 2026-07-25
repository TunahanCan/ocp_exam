# Unit 14 · I/O — Vocabulary

Bu sözlük, [ana çift dilli nottaki](bilingual_notes.md) file system, path,
stream, serialization, console ve file attribute bağlamında geçen teknik/YDS
kelimelerini alfabetik olarak toplar.

## A–C

### absolute · adjective

- **Türkçe:** mutlak, tam
- **Java bağlamı:** Root'tan başlayan ve current working directory'den bağımsız
  path.
- **Example:** “An absolute path contains the route from the root.”
- **Çeviri:** “Absolute path, root'tan başlayan yolu içerir.”
- **Related:** absolutely; antonym: relative

### access · noun / verb

- **Türkçe:** erişim; erişmek
- **Java bağlamı:** File data veya metadata'yı okuma/değiştirme yeteneği.
- **Example:** “The process may not have permission to access the file.”
- **Çeviri:** “Process file'a erişme iznine sahip olmayabilir.”
- **Related:** accessible, accessibility; antonym: inaccessible

### ancestor · noun

- **Türkçe:** üst ata, üst directory
- **Java bağlamı:** Directory tree'de bir path'in parent, grandparent veya daha
  yukarıdaki node'ları.
- **Example:** “The walk visits the ancestors before their descendants.”
- **Çeviri:** “Walk, descendant'lardan önce ancestor'ları ziyaret eder.”
- **Related:** ancestry; antonym: descendant

### append · verb

- **Türkçe:** sona eklemek
- **Java bağlamı:** Existing content'i silmeden file'ın sonuna data yazmak.
- **Example:** “The option appends the text to the existing file.”
- **Çeviri:** “Option, text'i existing file'ın sonuna ekler.”
- **Related:** appendable, appended; contrast: overwrite

### attribute · noun

- **Türkçe:** nitelik, öznitelik
- **Java bağlamı:** Size, creation time, permission veya file type gibi
  metadata.
- **Example:** “Reading the attributes together can reduce file-system calls.”
- **Çeviri:** “Attribute'ları birlikte okumak file-system çağrılarını
  azaltabilir.”
- **Related:** attributable; synonym: property, metadata

### backing · adjective

- **Türkçe:** altta destekleyen
- **Java bağlamı:** Stream, buffer veya view'ın veriyi aldığı underlying
  resource.
- **Example:** “The wrapper closes its backing stream.”
- **Çeviri:** “Wrapper, backing stream'ini kapatır.”
- **Related:** back, backed; synonym: underlying

### binary · adjective / noun

- **Türkçe:** ikili, binary data
- **Java bağlamı:** Character decoding uygulanmadan byte olarak işlenen data.
- **Example:** “Use an input stream to read binary content.”
- **Çeviri:** “Binary content okumak için input stream kullan.”
- **Related:** byte-oriented; contrast: textual

### buffer · noun / verb

- **Türkçe:** tampon; tamponlamak
- **Java bağlamı:** I/O call sayısını azaltmak için data'yı geçici bölgede
  toplamak.
- **Example:** “The buffer improves performance for many small writes.”
- **Çeviri:** “Buffer, çok sayıda küçük write için performance'ı iyileştirir.”
- **Related:** buffered, buffering

### chain · noun / verb

- **Türkçe:** zincir; zincirlemek
- **Java bağlamı:** High-level stream'leri birbirinin constructor'ına vererek
  işlevleri birleştirmek.
- **Example:** “The two readers can be chained together.”
- **Çeviri:** “İki reader birbiriyle zincirlenebilir.”
- **Related:** chained; synonym: wrap, compose

### close · verb

- **Türkçe:** kapatmak
- **Java bağlamı:** Resource'u serbest bırakıp stream'i daha fazla operation'a
  kapatmak.
- **Example:** “The resource is closed at the end of the statement.”
- **Çeviri:** “Resource, statement sonunda kapatılır.”
- **Related:** closure, closed; antonym: open

### convenience · noun used attributively

- **Türkçe:** kolaylık sağlayan
- **Java bağlamı:** Common operation'ı daha az kodla sunan API method'ı.
- **Example:** “Files provides convenience methods for reading text.”
- **Çeviri:** “Files, text okumak için convenience method'lar sağlar.”
- **Related:** convenient, conveniently

### copy · noun / verb

- **Türkçe:** kopya; kopyalamak
- **Java bağlamı:** Source data veya entry'yi ayrı target'a çoğaltmak.
- **Example:** “Copying a directory does not copy its contents recursively.”
- **Çeviri:** “Bir directory'yi kopyalamak içeriğini recursive olarak
  kopyalamaz.”
- **Related:** copied, copying; contrast: move

## D–H

### decode · verb

- **Türkçe:** kod çözmek
- **Java bağlamı:** Byte sequence'i charset aracılığıyla character sequence'e
  çevirmek.
- **Example:** “The reader decodes bytes as UTF-8 characters.”
- **Çeviri:** “Reader, byte'ları UTF-8 character'ları olarak decode eder.”
- **Related:** decoder, decoding; antonym: encode

### descendant · noun

- **Türkçe:** alt öğe, alt directory
- **Java bağlamı:** Directory tree'de bir node'un child veya daha derindeki
  üyeleri.
- **Example:** “A depth limit prevents deeper descendants from being visited.”
- **Çeviri:** “Depth limit daha derindeki descendant'ların ziyaret edilmesini
  önler.”
- **Related:** descend; antonym: ancestor

### deserialize · verb

- **Türkçe:** seriden nesneye dönüştürmek
- **Java bağlamı:** Stored byte representation'dan object graph oluşturmak.
- **Example:** “ObjectInputStream deserializes the stored object.”
- **Çeviri:** “ObjectInputStream stored object'i deserialize eder.”
- **Related:** deserialization; antonym: serialize

### directory · noun

- **Türkçe:** dizin, klasör
- **Java bağlamı:** File ve başka directory entry'leri içerebilen file-system
  node'u.
- **Example:** “A nonempty directory cannot be deleted with one call.”
- **Çeviri:** “Nonempty directory tek çağrıyla silinemez.”
- **Related:** folder, directory entry

### eager · adjective

- **Türkçe:** hemen değerlendiren
- **Java bağlamı:** Method result dönmeden bütün data'yı memory'ye yükleyen
  operation.
- **Example:** “readAllLines() is eager and returns a list.”
- **Çeviri:** “readAllLines() eager'dır ve list döndürür.”
- **Related:** eagerly; antonym: lazy

### encoding · noun

- **Türkçe:** karakter kodlama
- **Java bağlamı:** Character ile byte arasındaki mapping, örneğin UTF-8.
- **Example:** “An explicit encoding avoids platform-dependent output.”
- **Çeviri:** “Explicit encoding, platform-dependent output'u önler.”
- **Related:** encode, encoded; antonym: decoding

### encounter · noun / verb

- **Türkçe:** karşılaşma; karşılaşmak
- **Java bağlamı:** Tree traversal sırasında path'e ulaşılması; stream'de
  encounter order.
- **Example:** “The visitor may encounter a symbolic-link cycle.”
- **Çeviri:** “Visitor symbolic-link cycle ile karşılaşabilir.”
- **Related:** encountered; synonym: meet

### entry · noun

- **Türkçe:** kayıt, directory girdisi
- **Java bağlamı:** Directory içindeki file, directory veya symbolic link.
- **Example:** “Each entry is represented by a Path.”
- **Çeviri:** “Her entry bir Path ile temsil edilir.”
- **Related:** directory entry

### exist · verb

- **Türkçe:** var olmak
- **Java bağlamı:** Referenced file-system record'ın erişilebilir biçimde
  bulunması.
- **Example:** “Creating a Path does not require the target to exist.”
- **Çeviri:** “Path oluşturmak target'ın var olmasını gerektirmez.”
- **Related:** existence, existing; antonym: absent

### file system · noun phrase

- **Türkçe:** dosya sistemi
- **Java bağlamı:** File/directory storage, naming ve access kurallarını
  sağlayan provider yapısı.
- **Example:** “Path behavior can depend on the file-system provider.”
- **Çeviri:** “Path davranışı file-system provider'a bağlı olabilir.”
- **Related:** `FileSystem`, provider

### flush · verb

- **Türkçe:** tamponu hedefe aktarmak
- **Java bağlamı:** Buffered output'u downstream resource'a zorlamak.
- **Example:** “Flush the writer before inspecting the file.”
- **Çeviri:** “File'ı incelemeden önce writer'ı flush et.”
- **Related:** flushed, flushing

### hierarchy · noun

- **Türkçe:** hiyerarşi
- **Java bağlamı:** Directory tree veya stream class inheritance düzeni.
- **Example:** “Reader belongs to the character-stream hierarchy.”
- **Çeviri:** “Reader character-stream hierarchy'sine aittir.”
- **Related:** hierarchical, hierarchically

<!-- page-break -->

## I–M

### immutable · adjective

- **Türkçe:** değişmez
- **Java bağlamı:** Operation sonrası mevcut `Path` yerine yeni value
  döndürülmesi.
- **Example:** “Path is immutable, so normalize() returns another value.”
- **Çeviri:** “Path immutable olduğu için normalize() başka bir value
  döndürür.”
- **Related:** immutability; antonym: mutable

### input · noun / adjective

- **Türkçe:** girdi
- **Java bağlamı:** Programın file, console veya başka source'tan okuduğu data.
- **Example:** “The input stream reads one byte.”
- **Çeviri:** “Input stream bir byte okur.”
- **Related:** input stream; antonym: output

### lazily · adverb

- **Türkçe:** ihtiyaç oldukça, tembel biçimde
- **Java bağlamı:** Stream element'lerinin terminal operation sırasında
  okunması.
- **Example:** “Files.lines() reads the file lazily.”
- **Çeviri:** “Files.lines() file'ı ihtiyaç oldukça okur.”
- **Related:** lazy, laziness; antonym: eagerly

### link · noun / verb

- **Türkçe:** bağlantı; bağlamak
- **Java bağlamı:** Başka file-system entry'sine işaret eden symbolic link.
- **Example:** “The option prevents the method from following the link.”
- **Çeviri:** “Option, method'ın link'i izlemesini önler.”
- **Related:** symbolic link, linked; synonym: reference

### marker interface · noun phrase

- **Türkçe:** işaretleyici interface
- **Java bağlamı:** Method içermeden bir class'a semantic property bildiren
  `Serializable` gibi interface.
- **Example:** “Serializable is a marker interface.”
- **Çeviri:** “Serializable bir marker interface'tir.”
- **Related:** mark, marker

### metadata · noun

- **Türkçe:** veri hakkında veri, üstveri
- **Java bağlamı:** File size, owner, time veya permissions gibi content dışı
  bilgi.
- **Example:** “The attribute view exposes file metadata.”
- **Çeviri:** “Attribute view file metadata'sını açar.”
- **Related:** attribute

### mismatch · noun / verb

- **Türkçe:** uyuşmazlık; uyuşmamak
- **Java bağlamı:** İki file content'i arasındaki ilk farklı byte position'ı.
- **Example:** “A return value of minus one means no mismatch was found.”
- **Çeviri:** “Eksi bir return value, mismatch bulunmadığı anlamına gelir.”
- **Related:** match; antonym: correspondence

### move · noun / verb

- **Türkçe:** taşıma; taşımak
- **Java bağlamı:** Source path'i target location'a yeniden yerleştirmek veya
  rename etmek.
- **Example:** “An atomic move exposes no incomplete intermediate file.”
- **Çeviri:** “Atomic move incomplete intermediate file göstermez.”
- **Related:** relocation, rename; contrast: copy

## N–R

### normalize · verb

- **Türkçe:** normalleştirmek
- **Java bağlamı:** Redundant `.` ve uygun `name/..` path parçalarını textual
  olarak temizlemek.
- **Example:** “Normalize the value without accessing the disk.”
- **Çeviri:** “Disk'e erişmeden value'yu normalize et.”
- **Related:** normalized, normalization

### output · noun / adjective

- **Türkçe:** çıktı
- **Java bağlamı:** Programın file, console veya başka sink'e yazdığı data.
- **Example:** “The output stream writes binary data.”
- **Çeviri:** “Output stream binary data yazar.”
- **Related:** output stream; antonym: input

### overwrite · verb

- **Türkçe:** üzerine yazmak
- **Java bağlamı:** Existing target content'ini yeni data ile değiştirmek.
- **Example:** “REPLACE_EXISTING allows the copy to overwrite the target.”
- **Çeviri:** “REPLACE_EXISTING copy operation'ının target üzerine yazmasına
  izin verir.”
- **Related:** replacement; contrast: append

### parent · noun

- **Türkçe:** üst öğe
- **Java bağlamı:** Bir path element'ini doğrudan içeren directory.
- **Example:** “The root has no parent.”
- **Çeviri:** “Root'un parent'ı yoktur.”
- **Related:** parental; antonym: child

### persist · verb

- **Türkçe:** kalıcı olmak, kalıcılaştırmak
- **Java bağlamı:** Program execution sona erdikten sonra data'nın storage'da
  tutulması.
- **Example:** “Serialization can persist object state.”
- **Çeviri:** “Serialization object state'i kalıcılaştırabilir.”
- **Related:** persistence, persistent; antonym: transient

### provider · noun

- **Türkçe:** sağlayıcı
- **Java bağlamı:** `Path` ve `Files` operation'larının concrete file-system
  davranışını uygulayan bileşen.
- **Example:** “The provider may not support atomic moves.”
- **Çeviri:** “Provider atomic move'u desteklemeyebilir.”
- **Related:** provide, provision

### read-ahead limit · noun phrase

- **Türkçe:** ileri okuma sınırı
- **Java bağlamı:** `mark(int)` sonrasında mark'ın korunması için bildirilen
  character miktarı.
- **Example:** “Reading beyond the limit may invalidate the mark.”
- **Çeviri:** “Limit'in ötesinde okumak mark'ı geçersiz kılabilir.”
- **Related:** mark, reset

### reciprocal · adjective / noun

- **Türkçe:** karşılıklı, ters yöndeki karşılık
- **Java bağlamı:** Serialization ile deserialization arasındaki ters işlem
  ilişkisi.
- **Example:** “Deserialization is the reciprocal process.”
- **Çeviri:** “Deserialization karşı yöndeki işlemdir.”
- **Related:** reciprocally; synonym: inverse

### reference · noun / verb

- **Türkçe:** başvuru, referans; işaret etmek
- **Java bağlamı:** File-system location'ı temsil eden object veya symbolic
  link pointer'ı.
- **Example:** “The Path references a location that may not exist.”
- **Çeviri:** “Path, var olmayabilecek bir location'ı referans eder.”
- **Related:** refer, referenced

### relative · adjective

- **Türkçe:** göreli
- **Java bağlamı:** Current working directory veya başka base'e göre yorumlanan
  path.
- **Example:** “The relative path does not start at the root.”
- **Çeviri:** “Relative path root'tan başlamaz.”
- **Related:** relatively; antonym: absolute

### resolve · verb

- **Türkçe:** çözmek, base ile birleştirmek
- **Java bağlamı:** Bir path'i başka bir path'e göre konumlandırmak.
- **Example:** “Resolve the filename against the directory.”
- **Çeviri:** “Filename'i directory'ye göre resolve et.”
- **Related:** resolution, resolved

### resource leak · noun phrase

- **Türkçe:** kaynak sızıntısı
- **Java bağlamı:** Açılan file/stream resource'un kapatılmaması.
- **Example:** “The unclosed reader causes a resource leak.”
- **Çeviri:** “Kapatılmayan reader resource leak'e yol açar.”
- **Related:** leak, leaked resource

<!-- page-break -->

## S–Z

### serialize · verb

- **Türkçe:** nesneyi serileştirmek
- **Java bağlamı:** Object graph'ı stored/transmittable byte representation'a
  dönüştürmek.
- **Example:** “Every non-transient reference value must be null or
  serializable.”
- **Çeviri:** “Her non-transient reference value `null` veya serializable
  olmalıdır; primitive field'lar doğrudan serialize edilir.”
- **Related:** serialization, serializable; antonym: deserialize

### sink · noun

- **Türkçe:** çıktı hedefi
- **Java bağlamı:** Output stream'in data yazdığı file, memory veya network
  endpoint.
- **Example:** “A FileOutputStream uses a file as its sink.”
- **Çeviri:** “FileOutputStream sink olarak bir file kullanır.”
- **Related:** destination; contrast: source

### skip · verb

- **Türkçe:** atlamak
- **Java bağlamı:** Input üzerindeki bazı byte/character'ları result'a almadan
  ilerlemek.
- **Example:** “The method returns the number of characters actually skipped.”
- **Çeviri:** “Method gerçekten atlanan character sayısını döndürür.”
- **Related:** skipped, skipping

### storage · noun

- **Türkçe:** depolama
- **Java bağlamı:** File data'nın program execution'ları arasında kalıcı
  tutulduğu ortam.
- **Example:** “The object is written to persistent storage.”
- **Çeviri:** “Object persistent storage'a yazılır.”
- **Related:** store, stored

### stream · noun

- **Türkçe:** veri akışı
- **Java bağlamı:** Source ile sink arasında sıralı byte veya character
  taşıyan abstraction.
- **Example:** “A stream processes data in sequence.”
- **Çeviri:** “Stream data'yı sıra halinde işler.”
- **Related:** streaming

### structured · adjective

- **Türkçe:** yapılandırılmış
- **Java bağlamı:** Field/type ilişkileri olan object formundaki data.
- **Example:** “The binary data is restored as a structured object.”
- **Çeviri:** “Binary data structured object olarak geri yüklenir.”
- **Related:** structure, structurally

### symbolic link · noun phrase

- **Türkçe:** sembolik bağlantı
- **Java bağlamı:** Başka file-system entry'sine yönlendiren özel entry.
- **Example:** “The walk does not follow symbolic links by default.”
- **Çeviri:** “Walk varsayılan olarak symbolic link'leri izlemez.”
- **Related:** symlink, target

### target · noun

- **Türkçe:** hedef
- **Java bağlamı:** Copy/move destination veya symbolic link'in gösterdiği
  entry.
- **Example:** “The target is the complete destination path.”
- **Çeviri:** “Target, destination path'in tamamıdır.”
- **Related:** destination; antonym: source

### transient · adjective / Java modifier

- **Türkçe:** geçici
- **Java bağlamı:** Ordinary serialization'a dahil edilmeyen instance field.
- **Example:** “The transient cache returns to its default value.”
- **Çeviri:** “Transient cache default value'suna döner.”
- **Related:** transience; antonym: persistent

### traverse · verb

- **Türkçe:** baştan sona dolaşmak
- **Java bağlamı:** Directory tree node'larını belirli strategy ve depth ile
  ziyaret etmek.
- **Example:** “Files.walk() traverses the directory tree lazily.”
- **Çeviri:** “Files.walk() directory tree'yi lazy biçimde dolaşır.”
- **Related:** traversal

### underlying · adjective

- **Türkçe:** altta yatan
- **Java bağlamı:** Wrapper'ın çevrelediği stream veya file-system resource.
- **Example:** “Closing the wrapper closes the underlying stream.”
- **Çeviri:** “Wrapper'ı kapatmak underlying stream'i kapatır.”
- **Related:** underlying resource; synonym: backing

### wrap · verb

- **Türkçe:** sarmalamak
- **Java bağlamı:** Bir stream instance'ını high-level stream constructor'ına
  vererek behavior eklemek.
- **Example:** “Wrap the file reader in a buffered reader.”
- **Çeviri:** “File reader'ı buffered reader ile wrap et.”
- **Related:** wrapper, wrapped; synonym: decorate

## Mini quiz

1. `absolute` kelimesinin bu ünitedeki karşıtı nedir?
2. “File'ın üzerine yazmak” için hangi verb kullanılır?
3. `backing stream` ile `underlying stream` arasında nasıl bir anlam ilişkisi
   vardır?
4. “Actual skipped count” ifadesini doğal Türkçeye çevir.
5. Object state'i program kapandıktan sonra korumak için kullanılan `persist`
   kelimesinin noun formu nedir?
6. `ancestor` ve `descendant` hangi yapıyı tarif eder?
7. `eager` ve `lazy` API arasındaki temel fark nedir?
8. “Bir stream'i başka bir stream ile sarmalamak” için hangi iki yakın anlamlı
   verb kullanılabilir?

## Cevap anahtarı

1. `relative`
2. `overwrite`
3. Yakın anlamlıdır; wrapper'ın veri aldığı veya yönettiği alttaki resource'u
   anlatır.
4. “Gerçekte atlanan character/byte sayısı.”
5. `persistence`
6. Directory tree'deki üst ve alt node ilişkisini.
7. Eager operation data'yı hemen işler/yükler; lazy operation ihtiyaç
   oldukça, çoğunlukla terminal operation sırasında işler.
8. `wrap` ve `chain`
