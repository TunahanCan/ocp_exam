# Unit 15 · JDBC — Vocabulary

Bu sözlük, [ana çift dilli notta](bilingual_notes.md) geçen JDBC, relational
database, transaction ve resource-management kelimelerini teknik/YDS bağlamıyla
alfabetik olarak toplar.

## A–C

### acquire · verb

- **Türkçe:** edinmek, elde etmek
- **JDBC bağlamı:** Bir `Connection` veya başka database resource'u edinmek.
- **Example:** “The application acquires a connection from the driver.”
- **Çeviri:** “Application driver'dan bir connection edinir.”
- **Word family:** acquisition, acquired; synonym: obtain

### affected · adjective

- **Türkçe:** etkilenen
- **JDBC bağlamı:** `executeUpdate()` sonucunda eklenen, değiştirilen veya
  silinen row'lar.
- **Example:** “The method returns the number of affected rows.”
- **Çeviri:** “Method etkilenen row sayısını döndürür.”
- **Word family:** affect, effect; synonym: modified

### agnostic · adjective

- **Türkçe:** belirli bir üründen bağımsız
- **JDBC bağlamı:** Exam kuralının tek bir database vendor'ına bağlı olmaması.
- **Example:** “The JDBC objective is database agnostic.”
- **Çeviri:** “JDBC kazanımı belirli bir database'den bağımsızdır.”
- **Related:** vendor-neutral, independent of

### autocommit · noun / adjective

- **Türkçe:** otomatik commit modu
- **JDBC bağlamı:** Her statement'ın tamamlandığında otomatik commit edilmesi.
- **Example:** “Autocommit is enabled by default.”
- **Çeviri:** “Autocommit varsayılan olarak etkindir.”
- **Related:** commit, transaction

### bind variable · noun phrase

- **Türkçe:** bağlama değişkeni, parameter placeholder'ı
- **JDBC bağlamı:** Prepared SQL içindeki `?`; value runtime'da setter ile
  verilir.
- **Example:** “Each bind variable must receive a value before execution.”
- **Çeviri:** “Her bind variable execution öncesinde bir değer almalıdır.”
- **Related:** placeholder, parameter

### bookmark · noun / verb

- **Türkçe:** yer imi; yer imi koymak
- **JDBC bağlamı:** Transaction içinde rollback hedefi oluşturan `Savepoint`
  için kullanılan benzetme.
- **Example:** “A savepoint bookmarks the current transaction state.”
- **Çeviri:** “Savepoint current transaction state'ine yer imi koyar.”
- **Related:** marker, savepoint

### callable · adjective

- **Türkçe:** çağrılabilir
- **JDBC bağlamı:** Stored procedure çalıştıran `CallableStatement`.
- **Example:** “A callable statement may expose output parameters.”
- **Çeviri:** “Callable statement output parameter'lar sunabilir.”
- **Word family:** call, calling

### column · noun

- **Türkçe:** sütun
- **JDBC bağlamı:** Table'daki tek attribute; `ResultSet`te name veya 1-based
  index ile okunur.
- **Example:** “Column indexes begin with one.”
- **Çeviri:** “Column index'leri birden başlar.”
- **Related:** field, column name

### commit · verb / noun

- **Türkçe:** kalıcılaştırmak; kalıcılaştırma
- **JDBC bağlamı:** Current transaction değişikliklerini database'de kalıcı
  hale getirmek.
- **Example:** “Commit the transaction only after both updates succeed.”
- **Çeviri:** “Transaction'ı yalnız iki update de başarılı olduktan sonra
  commit edin.”
- **Antonym:** rollback; word family: committed, commitment

### concrete · adjective

- **Türkçe:** somut
- **JDBC bağlamı:** Interface'i gerçekten uygulayan vendor-specific class.
- **Example:** “The driver JAR supplies the concrete implementation.”
- **Çeviri:** “Driver JAR concrete implementation'ı sağlar.”
- **Antonym:** abstract

### connection · noun

- **Türkçe:** bağlantı
- **JDBC bağlamı:** Database session ve transaction context'ini temsil eden
  `Connection`.
- **Example:** “Close the connection after the work is complete.”
- **Çeviri:** “İş tamamlandıktan sonra connection'ı kapatın.”
- **Word family:** connect, connected, connectivity

### cursor · noun

- **Türkçe:** imleç
- **JDBC bağlamı:** `ResultSet` içinde current row konumunu gösteren pointer.
- **Example:** “The cursor initially points before the first row.”
- **Çeviri:** “Cursor başlangıçta ilk row'un önünü gösterir.”
- **Related:** position, advance

## D–H

### database-specific · adjective

- **Türkçe:** veritabanına özgü
- **JDBC bağlamı:** URL subname, driver class veya error code gibi vendor'a
  bağlı ayrıntı.
- **Example:** “The final part of the URL is database-specific.”
- **Çeviri:** “URL'nin son bölümü database'e özgüdür.”
- **Synonym:** vendor-specific; antonym: portable

### execute · verb

- **Türkçe:** yürütmek, çalıştırmak
- **JDBC bağlamı:** Prepared SQL veya stored procedure'ü database'e göndermek.
- **Example:** “The statement executes after all parameters are set.”
- **Çeviri:** “Statement bütün parameter'lar set edildikten sonra çalışır.”
- **Word family:** execution, executable

### factory · noun / adjective

- **Türkçe:** üretici, factory
- **JDBC bağlamı:** `DriverManager.getConnection()` gibi interface type'ında
  concrete object üreten API.
- **Example:** “The factory returns a driver-specific connection.”
- **Çeviri:** “Factory driver'a özgü bir connection döndürür.”
- **Related:** factory method, create

## I–M

### implementation · noun

- **Türkçe:** uygulama, gerçekleştirim
- **JDBC bağlamı:** JDBC interface contract'ını gerçekleştiren driver class'ı.
- **Example:** “The implementation is packaged in the driver JAR.”
- **Çeviri:** “Implementation driver JAR'ında paketlenir.”
- **Word family:** implement, implemented

### implementation-defined · adjective

- **Türkçe:** gerçekleştirim tarafından belirlenen
- **JDBC bağlamı:** Active manual transaction ile `Connection.close()`
  çağrısının commit/rollback sonucunun driver implementation'ına bırakılması.
- **Example:** “Closing an active manual transaction has an
  implementation-defined result.”
- **Çeviri:** “Active manual transaction'ı kapatmanın sonucu implementation
  tarafından belirlenir.”
- **Word family:** implement, implementation; contrast: portable guarantee

### in advance · adverb phrase

- **Türkçe:** önceden
- **JDBC bağlamı:** Stored procedure'ün database'de önceden compile edilmesi.
- **Example:** “The procedure is compiled in advance.”
- **Çeviri:** “Procedure önceden derlenir.”
- **Synonym:** beforehand

### invalidate · verb

- **Türkçe:** geçersiz kılmak
- **JDBC bağlamı:** Rollback işleminin daha sonraki savepoint'leri kullanılamaz
  hale getirmesi.
- **Example:** “Rolling back to the first savepoint invalidates the second.”
- **Çeviri:** “İlk savepoint'e rollback yapmak ikincisini geçersiz kılar.”
- **Word family:** invalid, invalidation; antonym: validate

### mandatory · adjective

- **Türkçe:** zorunlu
- **JDBC bağlamı:** SQL'in `prepareStatement()` çağrısında verilmesi veya OUT
  parameter'ın register edilmesi.
- **Example:** “Passing the SQL during statement creation is mandatory.”
- **Çeviri:** “Statement oluşturulurken SQL'i vermek zorunludur.”
- **Synonym:** required, compulsory; antonym: optional

## N–R

### obtain · verb

- **Türkçe:** edinmek, elde etmek
- **JDBC bağlamı:** DriverManager'dan `Connection` veya statement'tan
  `ResultSet` almak.
- **Example:** “The program obtains a result set from the query.”
- **Çeviri:** “Program query'den bir result set elde eder.”
- **Word family:** obtainable; synonym: acquire

### parameter · noun

- **Türkçe:** parametre
- **JDBC bağlamı:** Prepared statement bind value'su veya stored procedure
  `IN`/`OUT`/`INOUT` value'su.
- **Example:** “The first parameter has index one.”
- **Çeviri:** “İlk parameter'ın index'i birdir.”
- **Related:** parameterize, parameterized

### placeholder · noun

- **Türkçe:** yer tutucu
- **JDBC bağlamı:** SQL içindeki `?` işareti.
- **Example:** “The question mark is a placeholder for a runtime value.”
- **Çeviri:** “Question mark runtime value için bir placeholder'dır.”
- **Related:** bind variable

### portable · adjective

- **Türkçe:** taşınabilir, farklı ortamlarda geçerli
- **JDBC bağlamı:** Tek bir driver'ın toleransına değil JDBC contract'ına uyan
  code.
- **Example:** “Portable code registers every output parameter.”
- **Çeviri:** “Portable code her output parameter'ı register eder.”
- **Word family:** portability; antonym: database-specific

### prepared · adjective

- **Türkçe:** hazırlanmış
- **JDBC bağlamı:** SQL text'i oluşturma aşamasında verilen
  `PreparedStatement`.
- **Example:** “A prepared statement separates SQL from parameter values.”
- **Çeviri:** “Prepared statement SQL'i parameter value'larından ayırır.”
- **Word family:** prepare, preparation

### retrieve · verb

- **Türkçe:** geri almak, elde etmek
- **JDBC bağlamı:** `SELECT` ile data veya getter ile column value okumak.
- **Example:** “The query retrieves matching rows.”
- **Çeviri:** “Query eşleşen row'ları getirir.”
- **Word family:** retrieval; synonym: fetch

### rollback · verb / noun

- **Türkçe:** geri almak; geri alma
- **JDBC bağlamı:** Uncommitted transaction değişikliklerini tamamen veya
  savepoint'e kadar geri çevirmek.
- **Example:** “Rollback removes the uncommitted changes.”
- **Çeviri:** “Rollback commit edilmemiş değişiklikleri geri alır.”
- **Antonym:** commit; word family: roll back

### row · noun

- **Türkçe:** satır, kayıt
- **JDBC bağlamı:** Relational table'daki tek record.
- **Example:** “Each call to `next()` advances toward another row.”
- **Çeviri:** “Her `next()` çağrısı başka bir row'a doğru ilerler.”
- **Related:** record, tuple

## S–Z

### sanitize · verb

- **Türkçe:** güvenli hale getirmek, temizlemek
- **JDBC bağlamı:** User input'un SQL injection'a yol açmasını önleyecek
  biçimde işlenmesi.
- **Example:** “Bind variables reduce the need to sanitize concatenated SQL.”
- **Çeviri:** “Bind variable'lar birleştirilmiş SQL'i sanitize etme
  gereksinimini azaltır.”
- **Word family:** sanitized, sanitization

### savepoint · noun

- **Türkçe:** kayıt noktası
- **JDBC bağlamı:** Transaction içinde partial rollback hedefi.
- **Example:** “The second savepoint marks the optional update.”
- **Çeviri:** “İkinci savepoint optional update'i işaretler.”
- **Related:** bookmark, rollback

### statement · noun

- **Türkçe:** ifade, deyim
- **JDBC bağlamı:** Database'e gönderilen prepared SQL command veya callable
  procedure invocation.
- **Example:** “The statement returns a result set.”
- **Çeviri:** “Statement bir result set döndürür.”
- **Related:** `PreparedStatement`, `CallableStatement`

### stored procedure · noun phrase

- **Türkçe:** saklı yordam
- **JDBC bağlamı:** Database'de saklanan ve önceden compile edilen SQL code.
- **Example:** “A callable statement invokes the stored procedure.”
- **Çeviri:** “Callable statement stored procedure'ü çağırır.”
- **Related:** procedure, `prepareCall()`

### subname · noun

- **Türkçe:** alt ad, bağlantı ayrıntısı bölümü
- **JDBC bağlamı:** JDBC URL'nin vendor-specific son bölümü.
- **Example:** “The subname may include a host and port.”
- **Çeviri:** “Subname host ve port içerebilir.”
- **Related:** subprotocol, JDBC URL

### subprotocol · noun

- **Türkçe:** alt protokol
- **JDBC bağlamı:** JDBC URL'de database product/driver ailesini tanımlayan
  ikinci parça.
- **Example:** “PostgreSQL is the subprotocol in this URL.”
- **Çeviri:** “Bu URL'de PostgreSQL subprotocol'dür.”
- **Related:** protocol, vendor

### transaction · noun

- **Türkçe:** işlem, transaction
- **JDBC bağlamı:** Birlikte commit veya rollback edilen database operation
  grubu.
- **Example:** “Both updates belong to one transaction.”
- **Çeviri:** “İki update de tek transaction'a aittir.”
- **Word family:** transactional, transactionally

### vendor · noun

- **Türkçe:** sağlayıcı, üretici firma
- **JDBC bağlamı:** Database ve driver implementation'ını sağlayan kuruluş.
- **Example:** “The vendor defines the URL subname.”
- **Çeviri:** “Vendor URL subname'ini tanımlar.”
- **Related:** vendor-specific, provider

### warrant · verb

- **Türkçe:** gerektirmek, haklı çıkarmak
- **JDBC bağlamı:** Bir query'nin stored procedure olacak kadar complex olup
  olmadığını anlatmak.
- **Example:** “A simple query may not warrant a stored procedure.”
- **Çeviri:** “Basit bir query stored procedure kullanılmasını
  gerektirmeyebilir.”
- **Synonym:** justify, merit

## Word family özeti

| Verb | Noun | Adjective |
|---|---|---|
| affect | effect | affected |
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
