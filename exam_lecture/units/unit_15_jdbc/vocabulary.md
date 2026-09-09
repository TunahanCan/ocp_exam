# Unit 15 · JDBC — Vocabulary

Bu sözlük, [ana çift dilli notta](bilingual_notes.md) geçen JDBC, relational
database, transaction ve resource-management kelimelerini teknik/YDS bağlamıyla
alfabetik olarak toplar.

## A–C

### acquire · verb

- **Türkçe:** edinmek, elde etmek
- **JDBC bağlamı:** Bir `Connection` veya başka database resource'u edinmek.
- **Example:** “The application acquires a connection from the driver.”
- **Çeviri:** “Uygulama, sürücüden bir bağlantı edinir.”
- **Word family:** acquisition, acquired; synonym: obtain

### affected · adjective

- **Türkçe:** etkilenen
- **JDBC bağlamı:** `executeUpdate()` sonucunda eklenen, değiştirilen veya
  silinen row'lar.
- **Example:** “The method returns the number of affected rows.”
- **Çeviri:** “Metot, etkilenen satır sayısını döndürür.”
- **Word family:** affect, affected, affecting; karıştırma: effect (isim, etki/sonuç).

### agnostic · adjective

- **Türkçe:** belirli bir üründen bağımsız
- **JDBC bağlamı:** Exam kuralının tek bir database vendor'ına bağlı olmaması.
- **Example:** “The JDBC objective is database agnostic.”
- **Çeviri:** “JDBC kazanımı, belirli bir veritabanı ürününden bağımsızdır.”
- **Related:** vendor-neutral, independent of

### autocommit · noun / adjective

- **Türkçe:** otomatik commit modu
- **JDBC bağlamı:** Her statement'ın tamamlandığında otomatik commit edilmesi.
- **Example:** “Autocommit is enabled by default.”
- **Çeviri:** “Otomatik kalıcılaştırma modu varsayılan olarak etkindir.”
- **Related:** commit, transaction

### bind variable · noun phrase

- **Türkçe:** bağlama değişkeni, parameter placeholder'ı
- **JDBC bağlamı:** Prepared SQL içindeki `?`; value runtime'da setter ile
  verilir.
- **Example:** “Each bind variable must receive a value before execution.”
- **Çeviri:** “Her bağlama değişkenine, yürütme öncesinde bir değer verilmelidir.”
- **Related:** placeholder, parameter

### bookmark · noun / verb

- **Türkçe:** yer imi; yer imi koymak
- **JDBC bağlamı:** Transaction içinde rollback hedefi oluşturan `Savepoint`
  için kullanılan benzetme.
- **Example:** “A savepoint bookmarks the current transaction state.”
- **Çeviri:** “Kayıt noktası, işlemin mevcut durumunu işaretler.”
- **Related:** marker, savepoint

### callable · adjective

- **Türkçe:** çağrılabilir
- **JDBC bağlamı:** Stored procedure çalıştıran `CallableStatement`.
- **Example:** “A callable statement may expose output parameters.”
- **Çeviri:** “`CallableStatement`, çıktı parametreleri sunabilir.”
- **Word family:** call, calling

### column · noun

- **Türkçe:** sütun
- **JDBC bağlamı:** Table'daki tek attribute; `ResultSet`te name veya 1-based
  index ile okunur.
- **Example:** “Column indexes begin with one.”
- **Çeviri:** “Sütun indeksleri birden başlar.”
- **Related:** field, column name

### commit · verb / noun

- **Türkçe:** kalıcılaştırmak; kalıcılaştırma
- **JDBC bağlamı:** Current transaction değişikliklerini database'de kalıcı
  hale getirmek.
- **Example:** “Commit the transaction only after both updates succeed.”
- **Çeviri:** “İşlemi, yalnız her iki güncelleme de başarılı olduktan sonra kalıcılaştırın.”
- **Antonym:** rollback; word family: committed, commitment

### concrete · adjective

- **Türkçe:** somut
- **JDBC bağlamı:** Interface'i gerçekten uygulayan vendor-specific class.
- **Example:** “The driver JAR supplies the concrete implementation.”
- **Çeviri:** “Sürücünün JAR dosyası, somut gerçekleştirimi sağlar.”
- **Antonym:** abstract

### connection · noun

- **Türkçe:** bağlantı
- **JDBC bağlamı:** Database session ve transaction context'ini temsil eden
  `Connection`.
- **Example:** “Close the connection after the work is complete.”
- **Çeviri:** “İş tamamlandıktan sonra bağlantıyı kapatın.”
- **Word family:** connect, connected, connectivity

### cursor · noun

- **Türkçe:** imleç
- **JDBC bağlamı:** `ResultSet` içinde current row konumunu gösteren pointer.
- **Example:** “The cursor initially points before the first row.”
- **Çeviri:** “İmleç, başlangıçta ilk satırın önünde konumlanır.”
- **Related:** position, advance

## D–H

### database-specific · adjective

- **Türkçe:** veritabanına özgü
- **JDBC bağlamı:** URL subname, driver class veya error code gibi vendor'a
  bağlı ayrıntı.
- **Example:** “The final part of the URL is database-specific.”
- **Çeviri:** “URL'nin son bölümü, veritabanına özgüdür.”
- **Synonym:** vendor-specific; antonym: portable

### discard · verb

- **Türkçe:** vazgeçmek, geri almak
- **Java bağlamı:** rollback ile henüz kalıcılaştırılmamış değişikliklerin geri alınması.
- **Example · özgün:** “A rollback discards uncommitted changes.”
- **Çeviri:** “Geri alma işlemi, henüz kalıcılaştırılmamış değişiklikleri kaldırır.”
- **Related:** discarded; contrast: retain.
- **Kaynak bağlamı:** [committing and rolling back](bilingual_notes.md#committing-and-rolling-back)

### execute · verb

- **Türkçe:** yürütmek, çalıştırmak
- **JDBC bağlamı:** Prepared SQL veya stored procedure'ü database'e göndermek.
- **Example:** “The statement executes after all parameters are set.”
- **Çeviri:** “Deyim, bütün parametrelere değer atandıktan sonra çalışır.”
- **Word family:** execution, executable

### factory · noun / adjective

- **Türkçe:** üretici, factory
- **JDBC bağlamı:** `DriverManager.getConnection()` gibi interface type'ında
  concrete object üreten API.
- **Example:** “The factory returns a driver-specific connection.”
- **Çeviri:** “Üretici metot, sürücüye özgü bir bağlantı döndürür.”
- **Related:** factory method, create

## I–M

### implementation · noun

- **Türkçe:** uygulama, gerçekleştirim
- **JDBC bağlamı:** JDBC interface contract'ını gerçekleştiren driver class'ı.
- **Example:** “The implementation is packaged in the driver JAR.”
- **Çeviri:** “Gerçekleştirim, sürücünün JAR dosyasında paketlenir.”
- **Word family:** implement, implemented

### implementation-defined · adjective

- **Türkçe:** gerçekleştirim tarafından belirlenen
- **JDBC bağlamı:** Active manual transaction ile `Connection.close()`
  çağrısının commit/rollback sonucunun driver implementation'ına bırakılması.
- **Example:** “Closing an active manual transaction has an
  implementation-defined result.”
- **Çeviri:** “Etkin bir elle yönetilen işlem varken bağlantıyı kapatmanın sonucunu sürücünün gerçekleştirimi belirler.”
- **Word family:** implement, implementation; contrast: portable guarantee

### in advance · adverb phrase

- **Türkçe:** önceden
- **JDBC bağlamı:** Stored procedure'ün database'de önceden compile edilmesi.
- **Example:** “The procedure is compiled in advance.”
- **Çeviri:** “Saklı yordam önceden derlenir.”
- **Synonym:** beforehand

### invalidate · verb

- **Türkçe:** geçersiz kılmak
- **JDBC bağlamı:** Rollback işleminin daha sonraki savepoint'leri kullanılamaz
  hale getirmesi.
- **Example:** “Rolling back to the first savepoint invalidates the second.”
- **Çeviri:** “İlk kayıt noktasına geri dönmek, ikinciyi geçersiz kılar.”
- **Word family:** invalid, invalidation; antonym: validate

### mandatory · adjective

- **Türkçe:** zorunlu
- **JDBC bağlamı:** SQL'in `prepareStatement()` çağrısında verilmesi veya OUT
  parameter'ın register edilmesi.
- **Example:** “Passing the SQL during statement creation is mandatory.”
- **Çeviri:** “Deyim oluşturulurken SQL metnini vermek zorunludur.”
- **Synonym:** required, compulsory; antonym: optional

## N–R

### obtain · verb

- **Türkçe:** edinmek, elde etmek
- **JDBC bağlamı:** DriverManager'dan `Connection` veya statement'tan
  `ResultSet` almak.
- **Example:** “The program obtains a result set from the query.”
- **Çeviri:** “Program, sorgudan bir sonuç kümesi elde eder.”
- **Word family:** obtainable; synonym: acquire

### parameter · noun

- **Türkçe:** parametre
- **JDBC bağlamı:** Prepared statement bind value'su veya stored procedure
  `IN`/`OUT`/`INOUT` value'su.
- **Example:** “The first parameter has index one.”
- **Çeviri:** “İlk parametrenin indeksi birdir.”
- **Related:** parameterize, parameterized

### placeholder · noun

- **Türkçe:** yer tutucu
- **JDBC bağlamı:** SQL içindeki `?` işareti.
- **Example:** “The question mark is a placeholder for a runtime value.”
- **Çeviri:** “Soru işareti, çalışma zamanında verilecek değer için bir yer tutucudur.”
- **Related:** bind variable

### portable · adjective

- **Türkçe:** taşınabilir, farklı ortamlarda geçerli
- **JDBC bağlamı:** Tek bir driver'ın toleransına değil JDBC contract'ına uyan
  code.
- **Example:** “Portable code registers every output parameter.”
- **Çeviri:** “Farklı sürücülerde geçerli kod, her çıktı parametresini kaydeder.”
- **Word family:** portability; antonym: database-specific

### prepared · adjective

- **Türkçe:** hazırlanmış
- **JDBC bağlamı:** SQL text'i oluşturma aşamasında verilen
  `PreparedStatement`.
- **Example:** “A prepared statement separates SQL from parameter values.”
- **Çeviri:** “Hazırlanmış deyim, SQL metnini parametre değerlerinden ayırır.”
- **Word family:** prepare, preparation

### retain · verb

- **Türkçe:** saklamak, korumak
- **Java bağlamı:** PreparedStatement yeniden kullanılırken önceki parametre değerlerinin korunması.
- **Example · özgün:** “The statement retains parameter values until they are replaced or cleared.”
- **Çeviri:** “Deyim, parametre değerlerini değiştirilene veya temizlenene kadar korur.”
- **Related:** retention; synonym: keep; antonym: discard.
- **Kaynak bağlamı:** [working with parameters](bilingual_notes.md#working-with-parameters)

### retrieve · verb

- **Türkçe:** geri almak, elde etmek
- **JDBC bağlamı:** `SELECT` ile data veya getter ile column value okumak.
- **Example:** “The query retrieves matching rows.”
- **Çeviri:** “Sorgu, eşleşen satırları getirir.”
- **Word family:** retrieval; synonym: fetch

### rollback · noun / API name

- **Türkçe:** geri almak; geri alma
- **JDBC bağlamı:** Uncommitted transaction değişikliklerini tamamen veya
  savepoint'e kadar geri çevirmek.
- **Example:** “Rollback removes the uncommitted changes.”
- **Çeviri:** “Geri alma işlemi, henüz kalıcılaştırılmamış değişiklikleri kaldırır.”
- **Related:** roll back (iki sözcüklü fiil); rollback (isim ve API adı); contrast: commit

### row · noun

- **Türkçe:** satır, kayıt
- **JDBC bağlamı:** Relational table'daki tek record.
- **Example:** “Each call to `next()` advances toward another row.”
- **Çeviri:** “Her `next()` çağrısı, bir sonraki satıra doğru ilerler.”
- **Related:** record, tuple

## S–Z

### sanitize · verb

- **Türkçe:** güvenli hale getirmek, temizlemek
- **JDBC bağlamı:** User input'un SQL injection'a yol açmasını önleyecek
  biçimde işlenmesi.
- **Example:** “Bind variables reduce the need to sanitize concatenated SQL.”
- **Çeviri:** “Bağlama değişkenleri, birleştirilmiş SQL metnini temizleme ihtiyacını azaltır.”
- **Word family:** sanitized, sanitization

### savepoint · noun

- **Türkçe:** kayıt noktası
- **JDBC bağlamı:** Transaction içinde partial rollback hedefi.
- **Example:** “The second savepoint marks the optional update.”
- **Çeviri:** “İkinci kayıt noktası, isteğe bağlı güncellemeyi işaretler.”
- **Related:** bookmark, rollback

### statement · noun

- **Türkçe:** ifade, deyim
- **JDBC bağlamı:** Database'e gönderilen prepared SQL command veya callable
  procedure invocation.
- **Example:** “The statement returns a result set.”
- **Çeviri:** “Deyim bir sonuç kümesi döndürür.”
- **Related:** `PreparedStatement`, `CallableStatement`

### stored procedure · noun phrase

- **Türkçe:** saklı yordam
- **JDBC bağlamı:** Database'de saklanan ve önceden compile edilen SQL code.
- **Example:** “A callable statement invokes the stored procedure.”
- **Çeviri:** “`CallableStatement`, saklı yordamı çağırır.”
- **Related:** procedure, `prepareCall()`

### subname · noun

- **Türkçe:** alt ad, bağlantı ayrıntısı bölümü
- **JDBC bağlamı:** JDBC URL'nin vendor-specific son bölümü.
- **Example:** “The subname may include a host and port.”
- **Çeviri:** “Alt ad bölümü, sunucu adresi ve bağlantı noktası içerebilir.”
- **Related:** subprotocol, JDBC URL

### subprotocol · noun

- **Türkçe:** alt protokol
- **JDBC bağlamı:** JDBC URL'de database product/driver ailesini tanımlayan
  ikinci parça.
- **Example:** “PostgreSQL is the subprotocol in this URL.”
- **Çeviri:** “Bu URL'de PostgreSQL, alt protokoldür.”
- **Related:** protocol, vendor

### transaction · noun

- **Türkçe:** işlem, transaction
- **JDBC bağlamı:** Birlikte commit veya rollback edilen database operation
  grubu.
- **Example:** “Both updates belong to one transaction.”
- **Çeviri:** “Her iki güncelleme de tek bir işleme aittir.”
- **Word family:** transactional, transactionally

### vendor · noun

- **Türkçe:** sağlayıcı, üretici firma
- **JDBC bağlamı:** Database ve driver implementation'ını sağlayan kuruluş.
- **Example:** “The vendor defines the URL subname.”
- **Çeviri:** “Sağlayıcı, URL'nin alt ad bölümünü tanımlar.”
- **Related:** vendor-specific, provider

### warrant · verb

- **Türkçe:** gerektirmek, haklı çıkarmak
- **JDBC bağlamı:** Bir query'nin stored procedure olacak kadar complex olup
  olmadığını anlatmak.
- **Example:** “A simple query may not warrant a stored procedure.”
- **Çeviri:** “Basit bir sorgu, saklı yordam kullanılmasını gerektirmeyebilir.”
- **Synonym:** justify, merit

## Karıştırılan anlamları ayır

**statement / expression:** Java dilinde `statement` bir deyimdir; SQL bağlamında sorgu/güncelleme gibi komuttur. `expression` değer üreten ifadedir; her iki sözcüğü tek başına “ifade” diye ezberleme.

`affect` çoğunlukla fiil: etkilemek; `effect` çoğunlukla isim: etki/sonuç. Bunlar aynı sözcüğün basit çekimleri değildir. `retrieve` veriyi getirir; `retain` mevcut değeri korur.

## Kapalı kitap hatırlama · 5 dakika

Her oturumda en fazla 5 kelime seç. Önce Türkçeyi kapatıp İngilizce cümleyi
çevir; ardından İngilizceyi kapatıp Türkçe anlamdan sözcüğü ve kendi örneğini
üret. Yalnız “tanıdık geldi” yanıtını başarı sayma: **0 = çıkaramadım,
1 = anlamını söyledim, 2 = doğru teknik cümlede kullandım**. 0–1 puanlıları
ünite [tekrar rotasına](README.md) göre geri getir.

**Özgün aktarım sorusu:** Parametreleri her çalıştırmada yeniden atamak gerekir mi? `retain`, `unless`, `clear` kullan.

Cevabını yazdıktan sonra kontrol et.

**Örnek yanıt:** The statement retains parameter values unless they are replaced or cleared.

## Word family özeti

| Verb | Noun | Adjective |
|---|---|---|
| affect | — (etkileme eylemi) | affected |
| commit | commitment | committed |
| connect | connection, connectivity | connected |
| execute | execution | executable |
| implement | implementation | implemented |
| invalidate | invalidation | invalid |
| prepare | preparation | prepared |
| retrieve | retrieval | retrievable |
| sanitize | sanitization | sanitized |

<!-- page-break -->

## Özgün mini quiz

### A. Eşleştirme

1. `retrieve`
2. `invalidate`
3. `mandatory`
4. `portable`
5. `affected`

a. farklı driver'larda contract'a uygun çalışabilen<br>
b. zorunlu<br>
c. veri elde etmek<br>
d. geçersiz kılmak<br>
e. değişiklikten etkilenen

### B. Boşluk doldurma

1. A `Savepoint` acts as a ______ inside a transaction.
2. Each question mark is a bind variable or ______.
3. The driver JAR supplies the concrete ______.
4. The cursor must point to a valid ______ before a getter is called.
5. `commit()` and ______ have opposite effects.

## Cevap anahtarı

### A

1–c, 2–d, 3–b, 4–a, 5–e

### B

1. bookmark
2. placeholder
3. implementation
4. row
5. rollback
