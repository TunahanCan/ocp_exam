# Unit 15 · JDBC

Bu ünite Java 17 `java.sql` API'sini; relational database temelleri, JDBC
interface'leri, prepared/callable statement, `ResultSet`, transaction,
savepoint ve resource management konularıyla birlikte işler. Çift dilli ana
ders, teknik hafıza, vocabulary ve grammar materyalleri aynı kaynak akışını
tamamlar.

## Çalışma kaynakları

1. **Ana çift dilli ders**
   - [Markdown kaynağı](bilingual_notes.md)
   - [PDF çalışma sürümü](bilingual_notes.pdf)
2. **Teknik hafıza ve karar notları**
   - [Technical memory notes](technical_memory_notes.md)
   - [PDF çalışma sürümü](technical_memory_notes.pdf)
3. **Ünite vocabulary çalışması**
   - [Markdown kaynağı](vocabulary.md)
   - [PDF çalışma sürümü](vocabulary.pdf)
4. **Ünite grammar çalışması**
   - [Markdown kaynağı](grammar_notes.md)
   - [PDF çalışma sürümü](grammar_notes.pdf)

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 15 physical PDF pages: **863–908**
- Chapter gövdesi: **46/46 source marker**
- Chapter 15 Appendix official answers: **959–961**
- Appendix: **3/3 appendix source marker**
- Bölüm sonu: Summary, Exam Essentials ve kaynak **Review Questions 1–21**
- Kaynak Appendix: Official Answers **1–21**, sonuç ve gerekçeleriyle

Physical page 863 chapter title/objective sayfasıdır. Chapter 15 gövdesi page
908'de Review Question 21 ile biter. Appendix page 959'un üst bölümü Chapter 14
Answer 24–25'e aittir; yalnız `Chapter 15: JDBC` heading'inden sonraki içerik
bu üniteye alınmıştır. Appendix page 961'de Answer 21 ile ünite sona erer.

## Ana konu başlıkları

1. **Introducing Relational Databases and SQL** — page 864
2. **Introducing the Interfaces of JDBC** — page 868
3. **Connecting to a Database** — page 870
4. **Working with a PreparedStatement** — page 873
5. **Getting Data from a ResultSet** — page 882
6. **Calling a CallableStatement** — page 887
7. **Controlling Data with Transactions** — page 892
8. **Closing Database Resources** — page 895
9. **Summary** — page 897
10. **Exam Essentials** — page 898
11. **Review Questions** — page 900

## Figure envanteri

| Figure | Başlık | Physical page |
|---|---|---:|
| 15.1 | Tables in our relational database | 866 |
| 15.2 | Key JDBC interfaces | 869 |
| 15.3 | The JDBC URL format | 871 |
| 15.4 | Types of statements | 873 |
| 15.5 | The `ResultSet` cursor | 883 |

## Table envanteri

| Table | Başlık | Physical page |
|---|---|---:|
| 15.1 | CRUD operations | 867 |
| 15.2 | SQL | 867–868 |
| 15.3 | SQL runnable by the execute method | 877 |
| 15.4 | Return types of execute methods | 878 |
| 15.5 | `PreparedStatement` methods | 880 |
| 15.6 | `ResultSet` get methods | 886 |
| 15.7 | Sample stored procedures | 888 |
| 15.8 | Stored procedure parameter types | 891 |
| 15.9 | `Connection` APIs for transactions | 895 |

## Konu haritası

- Relational database, table, row, column, SQL ve CRUD
- JDBC interface'lerinin JDK/driver implementation ayrımı
- JDBC URL: protocol, subprotocol ve subname
- `DriverManager.getConnection()` factory kullanımı
- `PreparedStatement` oluşturma ve doğru execute method'u
- Bind variable, 1-based index, setter ve batch update
- `ResultSet` cursor, `next()` ve column getter'ları
- `CallableStatement`, stored procedure ve JDBC escape syntax
- `IN`, `OUT`, `INOUT` parameter contract'ları
- `ResultSet` type/concurrency options
- Autocommit, explicit commit/rollback ve transaction boundary
- Savepoint oluşturma ve invalidation
- JDBC resource ownership, reverse close order ve `SQLException`

## Java 17 teknik doğruluk notları

- JDBC interface'leri `java.sql` module/package alanındadır. Modüler code
  `requires java.sql;` directive'ine ihtiyaç duyar.
- `DriverManager` JDK'deki concrete class'tır; `Driver`, `Connection`,
  `PreparedStatement`, `CallableStatement` ve `ResultSet` interface'lerinin
  concrete implementation'ları driver tarafından sağlanır.
- `Connection.prepareStatement()` no-argument overload'a sahip değildir; SQL
  oluşturma çağrısında verilmelidir.
- `execute()` dönüşündeki `boolean`, success değil ilk sonucun `ResultSet`
  olup olmadığını gösterir.
- SQL bir `String` olduğu için Java compiler bind count, table/column veya
  execute-method uyumunu doğrulamaz; pek çok hata runtime `SQLException`dır.
- Bind parameter ve `ResultSet` column index'i 1 tabanlıdır.
- `ResultSet` getter'ından önce `next()` cursor'ı valid row'a taşımalıdır.
- `INOUT` parameter için hem setter hem `registerOutParameter()` gerekir.
- Autocommit `true` yapıldığında current transaction commit edilir. Autocommit
  `false` iken açık transaction ile `Connection.close()` çağrısının sonucu
  portable JDBC contract'ta implementation-defined'dır; explicit
  `commit()`/`rollback()` kullanılmalıdır.
- Kaynak Review Question 21'in resmî anahtarı **B, D** olarak korunur. B,
  `setAutoCommit(true)` çağrısının current transaction'ı commit etmesi
  nedeniyle portably doğrudur. Line W çıkarıldığında try-with-resources
  `Connection.close()` active transaction ile çalışır; source D'yi kesin kabul
  etse de table'ın boş kalması driver-independent garanti değildir. Ana notta
  ayrıca Java 17/JDBC contract editör notu bulunur.
- Kaynak Review Question 8'deki `{call ...}` biçimi portable JDBC escape
  syntax'tır. Native database procedure syntax'i farklı olabilir; kaynak
  resmî anahtarı **A, B** korunur.
- Kaynak Review Question 14'ün resmî anahtarı **C**'dir. JDBC escape grammar'da
  leading `?=` function return value'dur; generic procedure `OUT` parameter'ı
  değildir. “Bir IN ve bir OUT parameter alan stored procedure” öncülüyle
  `{call learn(?,?)}` gerekir; ana notta bu uyuşmazlık ayrıca işaretlenmiştir.
- Kaynak Review Question 15'in resmî anahtarı **C, D**'dir. JDBC contract'ta
  `rollback(curly)` target savepoint'i otomatik release etmez; aynı valid
  savepoint'e yeniden rollback yapılabilir. Bu nedenle portable değerlendirmede
  B de geçerlidir ve savunulabilir küme **B, C, D** olur.
- Kaynak Review Question 19 için `prepareCall()` çağrısına plain `SELECT`
  veya `UPDATE` geçirmek portable kullanım değildir; exact failure point ve message
  driver'a bağlı olabilir. Sınavın resmî **E** sonucu korunur.
- `SQLException` checked exception'dır; handle veya declare edilmezse code
  derlenmez.
- Try-with-resources resource'ları reverse declaration order'da kapatır.

## Resmî cevap anahtarı

| Soru | Cevap | Soru | Cevap | Soru | Cevap |
|---:|:---:|---:|:---:|---:|:---:|
| 1 | B, F | 8 | A, B | 15 | C, D |
| 2 | A | 9 | E | 16 | E |
| 3 | B, D | 10 | D | 17 | D |
| 4 | C | 11 | D | 18 | D |
| 5 | B | 12 | C | 19 | E |
| 6 | B | 13 | B, F | 20 | B |
| 7 | C | 14 | C | 21 | B, D |

## Önerilen çalışma sırası

1. `bilingual_notes.md` içinde interface–implementation ve URL yapısını oku.
2. Her code example'ını **Does not compile**, runtime `SQLException` veya
   driver/data-dependent output olarak sınıflandır.
3. Statement sorularında önce SQL'in query/update/procedure türünü, sonra doğru
   prepare ve execute method'unu seç.
4. Bind variable ve column erişiminde index'in 1'den başladığını işaretle.
5. `ResultSet` sorularında getter öncesi cursor position'ını yaz.
6. Callable sorularında her parameter için `IN`, `OUT` veya `INOUT` tablosunu
   uygula.
7. Transaction sorularında autocommit state'ini, savepoint order'ını ve
   explicit completion çağrısını sırayla izle.
8. `technical_memory_notes.md` karar ağacıyla tekrar yap; ardından kaynak
   Review Questions 1–21'i çöz.
9. Appendix cevaplarını karşılaştırırken özellikle Answer 8, 19 ve 21
   editör notlarını ayır.

Vocabulary, grammar ve teknik hafıza quiz'leri özgün çalışma sorularıdır; gerçek
sınavdan çıkmış gibi sunulmaz. Ana çift dilli nottaki Review Questions kaynak
chapter'ın bölüm sonu sorularıdır ve Appendix'teki resmî cevaplarla eşleşir.
