# Unit 14 · I/O

Bu ünite Java 17 legacy `File`, NIO.2 `Path`/`Files`, byte ve character
stream'leri, serialization, `Console`, file attribute ve directory traversal
konularını çift dilli ana ders akışı; teknik hafıza, vocabulary ve grammar
materyalleriyle birlikte ele alır.

## Amaç ve öğrenme hedefleri

Bu ünitenin sonunda `File`, `Path` ve `Files` rollerini ayırabilmen; path ve
file operation'larında textual/runtime etkileri izleyebilmen; stream,
serialization, attributes ve traversal sorularında resource ownership ile
exception sonucunu doğru sınıflandırabilmen hedeflenir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| I/O konularını English → Türkçe eşleşmesiyle kaynak sırasından öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Path, stream ve serialization kararlarını hızla tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| I/O terimlerini teknik bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Teknik İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi kaynaklar kapalıyken altı soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasından path, stream/serialization veya advanced API
   kümelerinden birini seç.
2. **5–25 dk:** Ana çift dilli notta ilgili English → Türkçe blokları, API
   tabloları ve kod örneklerini çalış.
3. **25–35 dk:** Teknik hafıza notunda textual operation → file-system access →
   checked exception karar sırasını seçtiğin örneğe uygula.
4. **35–43 dk:** Vocabulary'den 6–8 terimle byte/character ve
   input/output ayrımını sözlü anlat.
5. **43–50 dk:** Grammar notes içinden cause, condition veya reduced relative
   clause yapısını tekrar et.
6. **50–60 dk:** [Practice quiz](practice_quiz.md)'i çöz; yanlışını path,
   resource, serialization veya English etiketiyle kaydet.

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 14 physical PDF pages: **785–862**
- Chapter gövdesi: **78/78 kaynak sayfa**
- Chapter 14 Appendix official answers: **955–959**
- Appendix: **5/5 cevap kaynağı sayfası**
- Bölüm sonu: Summary, Exam Essentials ve kaynak **Review Questions 1–25**
- Kaynak Appendix: Official Answers **1–25**, bütün sonuç ve gerekçeleriyle

Physical page 785 chapter title/objective sayfasıdır. Chapter content ve Review
Question 25 physical page 862'de biter; Chapter 15 physical page 863'te başlar.
Appendix page 955'in üst kısmındaki Chapter 13 Answer 25 dışarıda bırakılmış,
`Chapter 14: I/O` heading'inden sonraki content alınmıştır. Appendix page
959'daki Chapter 14 Answer 24–25 tutulmuş, alttaki `Chapter 15: JDBC` bölümü
dışarıda bırakılmıştır.

## Ana konu başlıkları

1. **Referencing Files and Directories** — page 786
2. **Operating on File and Path** — page 793
3. **Introducing I/O Streams** — page 811
4. **Reading and Writing Files** — page 817
5. **Serializing Data** — page 824
6. **Interacting with Users** — page 832
7. **Working with Advanced APIs** — page 837
8. **Review of Key APIs** — page 848
9. **Summary** — page 850
10. **Exam Essentials** — page 851
11. **Review Questions** — pages 852–862

## Figure envanteri

| Figure | Başlık | Physical page |
|---|---|---:|
| 14.1 | Directory and file hierarchy | 787 |
| 14.2 | Relative paths using path symbols | 789 |
| 14.3 | I/O and NIO.2 class/interface relationships | 791 |
| 14.4 | Comparing file uniqueness | 810 |
| 14.5 | Visual representation of an I/O stream | 811 |
| 14.6 | Serialization process | 825 |
| 14.7 | File system with cycle | 846 |
| 14.8 | Diagram of I/O stream classes | 849 |

## Table envanteri

| Table | Başlık | Physical page |
|---|---|---:|
| 14.1 | File-system symbols | 788 |
| 14.2 | Options for creating `File` and `Path` | 792 |
| 14.3 | Common `File` and `Path` operations | 793 |
| 14.4 | Common `File` and `Files` operations | 793–794 |
| 14.5 | Common NIO.2 method arguments | 797–798 |
| 14.6 | `Path` APIs | 805 |
| 14.7 | The `java.io` abstract stream base classes | 816 |
| 14.8 | The `java.io` concrete I/O stream classes | 816–817 |
| 14.9 | Common I/O read and write methods | 823–824 |
| 14.10 | Common `Files` NIO.2 read and write methods | 824 |
| 14.11 | Common I/O stream methods | 839 |
| 14.12 | The attributes and view types | 841 |
| 14.13 | Walking a directory with a cycle using breadth-first search | 846–847 |
| 14.14 | Key APIs | 848 |

## Önkoşul ve konu haritası

**Önkoşul:** Exception handling ve try-with-resources, object graph,
collection/stream işlemleri ve temel `java.nio.file` path kavramlarına aşinalık
yararlıdır.

- File-system hierarchy, root, absolute/relative path, `.` ve `..`
- Symbolic link ve provider-dependent path davranışı
- `File`, `Path`, `Paths`, `Files`, `FileSystem` ve `FileSystems`
- `Path` immutability, element access, `resolve()`, `relativize()`,
  `normalize()`, `toAbsolutePath()` ve `toRealPath()`
- NIO.2 method'larında `IOException`, optional parameters ve link behavior
- Directory creation; copy, move, delete, identity ve content comparison
- Byte/character, input/output, low-level/high-level stream sınıflandırması
- Buffer, correct read/write loop, `flush()`, `close()` ve resource ownership
- `Files` convenience API'leri ve lazy file stream'leri
- `Serializable`, `transient`, object graph ve `serialVersionUID`
- Standard stream'ler, `Console`, password ve formatted input/output
- `mark()`, `reset()`, `skip()` ve concrete stream capability
- Basic/DOS/POSIX/owner/user-defined file attribute view'ları
- `Files.walk()`, `Files.find()`, max depth, symbolic-link cycle ve search

## Hazır mıyım?

- [ ] `File`, `Path` ve `Files` rollerini ve immutability farkını
  açıklayabiliyorum.
- [ ] `resolve()`, `relativize()`, `normalize()` ve `toRealPath()` sonuçlarını
  file-system erişimi açısından ayırabiliyorum.
- [ ] Copy/move/delete operation'larında target, optional parameter ve checked
  exception durumunu belirleyebiliyorum.
- [ ] Stream adından byte/character, input/output ve low/high-level
  sınıflandırmasını yapabiliyorum.
- [ ] Correct copy loop'ta `read()` count, EOF, flush ve close akışını
  gösterebiliyorum.
- [ ] Serialization hierarchy'sinde constructor ve `transient` field
  davranışını izleyebiliyorum.
- [ ] `Files.walk()` / `find()` için depth, symbolic link ve resource close
  kurallarını uygulayabiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapıp yanlış seçenekleri
  gerekçelendirebiliyorum.

## Java 17 teknik doğruluk notları

- Kaynak NIO'yu yalnız “non-blocking I/O” diye açar. NIO, **New I/O** adıyla
  da bilinir; NIO.2 file operation'larının genel olarak non-blocking olduğu
  sonucu çıkarılamaz.
- `Path` immutable'dır. `normalize()`, `resolve()` ve benzeri method result'ı
  yeniden atanmazsa original path değişmez.
- `normalize()` file system'e erişmeyen textual operation'dır;
  `toRealPath()` target'ın varlığını kontrol eder ve varsayılan olarak symbolic
  link'leri çözer.
- `Files.list()`, `lines()`, `walk()` ve `find()` resource-backed
  `Stream` döndürebilir; try-with-resources ile kapatılmalıdır.
- `Files.copy()` directory tree'yi recursive kopyalamaz. Copy/move target
  argument'ı directory değil exact destination path'tir.
- Kaynaktaki örnek recursive copy anlatımında kullanılan `Files.list()` ve
  default `Files.isDirectory()` davranışı directory symbolic link target'ını
  izleyebilir; explicit link policy olmadan “örnek hiçbir symbolic link
  izlemez” genellemesi yapılmamalıdır.
- `Files.delete()` ve `deleteIfExists()` checked `IOException` declare eder;
  nonempty directory tek çağrıyla silinemez.
- `Reader`/`Writer` character, `InputStream`/`OutputStream` byte
  hierarchy'sidir. Bridge gerekmeden iki hierarchy constructor chain'inde
  karıştırılamaz.
- Buffer copy loop'unda `read(buffer)` return count'u
  `write(buffer, 0, count)` çağrısına verilmelidir.
- `InputStream.read() == -1` EOF demektir; geçici olarak byte bulunmaması
  değildir. `available()` ise blocking olmadan okunabileceği tahmin edilen byte
  miktarını verir, bütün remaining length'i garanti etmez.
- `Serializable` marker interface'tir. Non-`static`, non-`transient` reachable
  runtime field graph serialize edilebilir olmalıdır.
- Serializable class'ın constructor/instance initializer'ı deserialization
  sırasında çalışmaz; ilk non-serializable superclass'ın no-arg constructor'ı
  çalışır.
- Serializable record istisnadır: Deserialization sırasında canonical
  constructor çağrılır. `serialVersionUID` da her class edit'inde artırılan
  sıradan bir counter değildir.
- `System.console()` environment'a göre `null` dönebilir.
- `readPassword()` için `char[]` avantajı iş bitince içeriğin
  temizlenebilmesidir. `System.in/out/err` kapatılmamalıdır; ancak
  `System.setIn/Out/Err()` nedeniyle “hiçbir koşulda değiştirilemez” de doğru
  değildir.
- Mark desteklenmiyorsa `mark()` no-op olabilir ve `reset()` `IOException`
  üretebilir.
- `Reader.skip(n)` actual skipped count döndürür; generic contract tam `n`
  garantisi vermez.
- `Files.walk()` ve `Files.find()` default olarak symbolic link izlemez.
  `FileVisitOption.FOLLOW_LINKS` kullanıldığında cycle
  `FileSystemLoopException` üretebilir.
- Directory walking API'lerini genel olarak guaranteed breadth-first diye
  sınıflandırma. Kaynak Table 14.13 yalnız kendi örneğini açıklamak için
  breadth-first varsayımı kullanır; Java 17 `Files.walk()` API'si depth-first
  traversal tanımlar.
- Kaynak page 847 prose'da tekil `FOLLOW_LINK` yazar. Gerçek Java 17 enum
  constant'ı `FileVisitOption.FOLLOW_LINKS`tir.
- Kaynak Review Question 15'in option F path'inde `winer` yazdığı halde
  Appendix F'yi doğru sayar. Literal kod başka path'i temsil ettiğinden formal
  Java 17 correct set **B, E**; resmî anahtar **B, E, F** olarak korunup editor
  note ile ayrılmıştır.
- Kaynak Review Question 17'nin resmî anahtarı **B, C, E**dir. Appendix
  explanation'ın “option D is correct” cümlesi seçenek metni ve anahtarla
  çelişen editorial typo'dur.
- Kaynak Review Question 18'in resmî **C** cevabı, mark destekleyen reader'ın
  requested skip miktarını tam karşılaması varsayımına dayanır. General
  `Reader.skip()` actual count döndürür.

## Önerilen çalışma sırası

1. `bilingual_notes.md` içinde önce `File`–`Path`–`Files` rollerini ayır.
2. Path sorularında root/name element'lerini yaz; operation result'ının yeniden
   atanıp atanmadığını kontrol et.
3. Her NIO.2 call için checked exception, symbolic-link default'u ve
   file-system erişimi olup olmadığını işaretle.
4. Stream adını byte/character, input/output ve low/high-level parçalarına ayır.
5. Copy loop'larında `read()` result, buffer length, flush ve close sırasını
   kontrol et.
6. Serialization sorularında hierarchy'yi çiz; `static`, `transient`,
   serializable ve non-serializable field'ları işaretle.
7. Traversal sorularında root depth, max depth, follow-links ve resource close
   durumunu yaz.
8. `technical_memory_notes.md` karar tablolarıyla tekrar yap; ardından kaynak
   Review Questions 1–25'i çöz.
9. Son olarak Appendix 1–25 resmî sonuç/gerekçelerini Java 17 editor notlarıyla
   karşılaştır ve vocabulary/grammar mini quiz'lerini tamamla.

Vocabulary, grammar ve teknik hafıza quiz'leri özgün çalışma sorularıdır; gerçek
sınavdan çıkmış gibi sunulmaz. Ana çift dilli nottaki Review Questions kaynak
chapter'ın bölüm sonu sorularıdır ve Appendix'teki resmî cevaplarla
eşleştirilir.
