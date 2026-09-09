# Unit 15 · JDBC

Bu ünite Java 17 `java.sql` API'sini; relational database temelleri, JDBC
interface'leri, prepared/callable statement, `ResultSet`, transaction,
savepoint ve resource management konularıyla birlikte işler. Çift dilli ana
ders, teknik hafıza, vocabulary ve grammar materyalleri aynı kaynak akışını
tamamlar.

## Amaç ve öğrenme hedefleri

Bu ünitenin sonunda JDBC interface/driver implementation sınırını
gösterebilmen; statement ve execute method'unu SQL türüne göre seçebilmen;
cursor, parameter, transaction ve resource sorularında compile-time kontrol ile
driver/database runtime kontrolünü ayırabilmen hedeflenir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| JDBC konularını English → Türkçe eşleşmesiyle kaynak sırasından öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Statement, cursor ve transaction kararlarını hızla tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| JDBC ve SQL terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Teknik İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi kaynaklar kapalıyken sekiz soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## Çalışan biri için çalışma rotası · 25–30 dakikalık oturumlar

Bu tablo bir **ilk tur rotasıdır**; bütün üniteyi tek oturumda bitirme hedefi değildir.
Yoğun başlığı veya uzun soru grubunu aynı rota satırında ikinci güne böl.
Her oturumda **3 dk kapalı kitap hatırlama → 9 dk okuma → 10 dk soru →
5 dk dil çalışması → 3 dk hata kaydı** uygula. Okuma bölümünde önce İngilizce
paragrafı sesli veya yazılı özetle, sonra Türkçe çeviriyle karşılaştır.

| Oturum | Okuma ve teknik hedef | Kaynak Review Questions | Kelime odağı | Grammar odağı |
|---|---|---|---|---|
| 1 · JDBC arayüzü ve bağlantı | [Introducing the Interfaces of JDBC](bilingual_notes.md#introducing-the-interfaces-of-jdbc) | [1](bilingual_notes.md#question-1--soru-1), [2](bilingual_notes.md#question-2--soru-2), [4](bilingual_notes.md#question-4--soru-4), [20](bilingual_notes.md#question-20--soru-20) | interface / concrete / vendor | 1: stand for; 3: refer to |
| 2 · PreparedStatement ve parametre | [Working with a PreparedStatement](bilingual_notes.md#working-with-a-preparedstatement) | [3](bilingual_notes.md#question-3--soru-3), [5](bilingual_notes.md#question-5--soru-5), [7](bilingual_notes.md#question-7--soru-7), [9](bilingual_notes.md#question-9--soru-9), [16](bilingual_notes.md#question-16--soru-16) | bind variable / placeholder / execute | 10: allow; 12: before |
| 3 · ResultSet ve SQL NULL | [Getting Data from a ResultSet](bilingual_notes.md#getting-data-from-a-resultset) | [12](bilingual_notes.md#question-12--soru-12), [13](bilingual_notes.md#question-13--soru-13), [17](bilingual_notes.md#question-17--soru-17), [18](bilingual_notes.md#question-18--soru-18) | cursor / column / retrieve | 14: once; 15: if |
| 4 · CallableStatement ve kaynak kapanışı | [Calling a CallableStatement](bilingual_notes.md#calling-a-callablestatement) | [8](bilingual_notes.md#question-8--soru-8), [10](bilingual_notes.md#question-10--soru-10), [11](bilingual_notes.md#question-11--soru-11), [14](bilingual_notes.md#question-14--soru-14), [19](bilingual_notes.md#question-19--soru-19) | callable / register / stored procedure | 17: so that; 24: order in which |
| 5 · Transaction ve kayıt noktaları | [Controlling Data with Transactions](bilingual_notes.md#controlling-data-with-transactions) | [6](bilingual_notes.md#question-6--soru-6), [15](bilingual_notes.md#question-15--soru-15), [21](bilingual_notes.md#question-21--soru-21) | commit / rollback / savepoint | 13: when; 20: as long as |
| 6 · Karışık kontrol | [Teknik hafıza notu](technical_memory_notes.md): önce karar kuralını bellekten yaz | Önceki oturumların en zor 3 sorusu + [özgün quiz 7–8](practice_quiz.md#soru-7) | Yanlış yaptığın 5 kelime | Bir uzun cümlede özne, yüklem ve bağlacı işaretle |

Kaynak soruların seçenek sayısı ve “Choose all that apply” yönergesi korunmuştur.
Cevaplara geçmeden seçtiğin her şık için bir gerekçe yaz. Kaynak cevapla Java 17
notu ayrışıyorsa ilgili editör notunu da oku; yalnız harf ezberleme.

### 1 / 3 / 7 / 14 gün tekrar döngüsü

Her oturumun tekrarını kendi çalışma tarihinden itibaren planla:

- **1. gün · 5 dk:** O günün 3–5 kelimesini Türkçeden İngilizceye üret; kuralı bir örnekle anlat.
- **3. gün · 8 dk:** Yanlış veya tahminle doğru yaptığın iki soruyu seçenekleri kapatarak yeniden çöz.
- **7. gün · 10 dk:** Farklı konulardan üç soru ve bir cümle çözümlemesi yap.
- **14. gün · 10 dk:** Hâlâ karıştırdığın kuralları ve kelimeleri tekrar yokla; doğru cevapla birlikte nedenini söyle.

Hata kaydına tek satır yeter: **soru → benim gerekçem → doğru kural →
yeni örnek → tekrar tarihi**. Hatanın türünü `Java kuralı`, `kod izleme`,
`kelime` veya `cümle yapısı` olarak belirt; böylece bir sonraki kısa oturumun
hedefi belli olur.

**Geçiş ölçütü:** İki ayrı günde özgün quiz'de en az **7/8**; kaynaklarda
yanlış yapılan soruların doğru gerekçesi; seçilen 5 kelimeden en az 4'ünü
cümlenin içinde kullanma; bir İngilizce cümlede ana yüklemi ve koşul/karşıtlık
ilişkisini açıklama. Sağlanmayan beceri için yalnız ilgili oturumu yinele.

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 15 physical PDF pages: **863–908**
- Chapter gövdesi: **46/46 kaynak sayfa**
- Chapter 15 Appendix official answers: **959–961**
- Appendix: **3/3 cevap kaynağı sayfası**
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

## Önkoşul ve konu haritası

**Önkoşul:** Interface/concrete class, checked exception,
try-with-resources ve temel relational database/SQL kavramlarını hatırlamak
yararlıdır.

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

## Hazır mıyım?

- [ ] JDK'nin sağladığı JDBC API type'larıyla driver implementation'larını
  ayırabiliyorum.
- [ ] JDBC URL bölümlerini ve `DriverManager.getConnection()` rolünü
  açıklayabiliyorum.
- [ ] Query/update/procedure için prepare ve execute method'larını doğru
  seçebiliyorum.
- [ ] Bind variable ve `ResultSet` column index'lerinin 1 tabanlı olduğunu,
  cursor için önce `next()` gerektiğini biliyorum.
- [ ] `IN`, `OUT` ve `INOUT` parameter işlemlerini setter/register adımlarıyla
  gösterebiliyorum.
- [ ] Autocommit, savepoint, explicit commit/rollback ve close sınırlarını
  izleyebiliyorum.
- [ ] JDBC resource'larının reverse close order'ını ve `SQLException`
  zincirini açıklayabiliyorum.
- [ ] Practice quiz'de en az **7/8** doğru yapıp yanlış seçenekleri
  gerekçelendirebiliyorum.

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

<details>
<summary>Soruları çözdükten sonra cevap anahtarını aç</summary>

| Soru | Cevap | Soru | Cevap | Soru | Cevap |
|---:|:---:|---:|:---:|---:|:---:|
| 1 | B, F | 8 | A, B | 15 | C, D |
| 2 | A | 9 | E | 16 | E |
| 3 | B, D | 10 | D | 17 | D |
| 4 | C | 11 | D | 18 | D |
| 5 | B | 12 | C | 19 | E |
| 6 | B | 13 | B, F | 20 | B |
| 7 | C | 14 | C | 21 | B, D |

</details>

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
