# Unit 14 · I/O — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) file, path, stream,
serialization ve directory traversal anlatımından seçilen teknik İngilizce
yapılarını YDS/teknik okuma açısından açıklar.


Örnekler kaynak bağlamını öğretmek için seçilmiş veya sadeleştirilmiştir;
“kaynak alıntısı” diye belirtilmeyen cümleler birebir kitap alıntısı değildir.
Her oturumda bir yapıyı çalış: **ana yüklem → özne → bağlaç → yan cümle →
doğal Türkçe** sırasını izle. Yapıyı ertesi gün örneğe bakmadan yeniden kur.

## 1. `so that` — amaç ve sonuç

### Yapı

```text
main clause + so that + subject + modal/verb
```

Bir action'ın amacını veya ortaya çıkardığı sonucu açıklar.

> **English:** “Applications save data so that information is not lost when
> the program terminates.”
>
> **Türkçe:** “Uygulamalar, program sona erdiğinde bilgi kaybolmasın diye verileri kaydeder.”

YDS ipucu: `so that + can/could/may/might` çoğunlukla amaç; bağlama göre
sonuç da bildirebilir. `so + adjective + that` ile karıştırma.

## 2. `every time + clause`

### Yapı

```text
every time + subject + verb, main clause
```

Her tekrarlandığında aynı action/result'ın gerçekleştiğini bildirir.

> **English:** “The program writes its state every time the application is
> closed.”
>
> **Türkçe:** “Program, uygulama her kapatıldığında durumunu kaydeder.”

`every time` burada conjunction gibi clause başlatır; ardından ayrıca `when`
getirilmez.

## 3. `rather than`

### Yapı

```text
noun/V-ing + rather than + parallel noun/V-ing
```

Tercih veya karşıt seçenek bildirir.

> **English:** “Use NIO.2 rather than legacy I/O where possible.”
>
> **Türkçe:** “Mümkün olduğunda legacy I/O yerine NIO.2 kullan.”

Parallelism önemlidir: `using X rather than using Y` veya
`use X rather than Y`.

## 4. `as well as`

### Yapı

```text
A as well as B
```

“B'nin yanı sıra A” anlamı verir. Grammatical head çoğunlukla A'dır.

> **English:** “A directory can contain files as well as other directories.”
>
> **Türkçe:** “Bir dizin, başka dizinlerin yanı sıra dosyalar da içerebilir.”

YDS tuzağı: `A as well as B` subject olduğunda verb agreement genellikle A'ya
göredir; yapı basit `and` ile tamamen aynı değildir.

## 5. `be in charge of + V-ing/noun`

### Yapı

```text
be + in charge of + noun / gerund
```

Sorumluluk bildirir.

> **English:** “The file system is in charge of reading and writing data.”
>
> **Türkçe:** “Dosya sistemi, verileri okumaktan ve yazmaktan sorumludur.”

`of` preposition olduğu için ardından verb gelirse `V-ing` kullanılır.

## 6. `allow + object + to + V1`

### Yapı

```text
allow + object + to-infinitive
```

Bir component'e action gerçekleştirme olanağı verir.

> **English:** “The JVM allows the same operations to run across multiple
> platforms.”
>
> **Türkçe:** “JVM, aynı işlemlerin birden fazla platformda çalışmasına olanak verir.”

Passive form:

```text
object + be allowed + to + V1
```

Sık hata: object'ten sonra `to`yu düşürmek.

## 7. `from which`

### Yapı

```text
noun + from which + clause
```

Preposition'ı relative pronoun önüne taşıyan formal relative clause'dur.

> **English:** “The root is the topmost directory from which all other paths
> descend.”
>
> **Türkçe:** “Kök, diğer bütün yolların türediği en üst dizindir.”

Daha gündelik karşılık: `which ... from`. YDS metinlerinde preposition +
`which/whom` yapısı sık görülür.

## 8. `whereas`

### Yapı

```text
clause, whereas contrasting clause
```

İki özellik arasında belirgin karşıtlık kurar.

> **English:** “Unix systems use a forward slash, whereas Windows systems use
> a backslash.”
>
> **Türkçe:** “Unix sistemleri eğik çizgi kullanırken Windows sistemleri ters eğik çizgi kullanır.”

`whereas` neden değil contrast bildirir. Türkçede “oysa”, “-iken” veya “buna
karşılık” olabilir.

## 9. `assuming (that)`

### Yapı

```text
assuming (that) + clause, main clause
```

Sonucun bağlı olduğu varsayımı açıklar.

> **English:** “Assuming that the target exists, the method returns its real
> path.”
>
> **Türkçe:** “Hedefin var olduğunu varsayarsak metot, onun gerçek yolunu döndürür.”

OCP sorularında `assuming`, environment-dependent belirsizliği daraltır.
Sorunun verdiği assumption'ı Java language guarantee ile karıştırma.

## 10. `whether ... or ...`

### Yapı

```text
whether + alternative A + or + alternative B
```

İki olasılığın ikisini de kapsar.

> **English:** “The Path can represent a record whether it is a file or a
> directory.”
>
> **Türkçe:** “`Path`, bir dosyayı da bir dizini de temsil edebilir.”

`whether or not` = “olup olmadığı”. Indirect question'da `if` bazen mümkün
olsa da preposition sonrası ve `to-infinitive` öncesi `whether` gerekir.

## 11. `not only ... but also`

### Yapı

```text
not only + X + but also + parallel Y
```

İkinci unsuru ekleyip vurgular.

> **English:** “The API can not only read attributes but also modify them
> through a view.”
>
> **Türkçe:** “API, öznitelikleri okumakla kalmaz; bir görünüm aracılığıyla değiştirebilir de.”

X ve Y grammatical olarak parallel olmalıdır. Cümle `Not only` ile başlarsa
ilk clause'da inversion görülebilir:

```text
Not only does the method read data, but it also closes the stream.
```

## 12. `with + noun + V-ing / past participle`

### Yapı

```text
with + noun + present participle
with + noun + past participle
```

Eşlik eden durum veya background condition verir.

> **English:** “The method returns the path with symbolic links resolved.”
>
> **Türkçe:** “Method, symbolic link'leri çözülmüş path'i döndürür.”

`resolved` passive/result state'tir. `with the stream remaining open` ise active
devam eden durumu bildirir.

## 13. `by + V-ing`

### Yapı

```text
main clause + by + gerund
```

Bir sonucun hangi yöntemle elde edildiğini açıklar.

> **English:** “The code improves performance by buffering the output.”
>
> **Türkçe:** “Kod, çıktıyı buffer’da biriktirerek performansı artırır.”

YDS sorusunda `by` çoğunlukla “-erek/-arak, yoluyla”; `because of` ise neden
bildirir.

## 14. `without + V-ing`

### Yapı

```text
without + gerund
```

Bir action gerçekleşmeden başka bir action'ın olduğunu bildirir.

> **English:** “normalize() simplifies the path without accessing the file
> system.”
>
> **Türkçe:** “`normalize()`, dosya sistemine erişmeden yolu sadeleştirir.”

`without to access` yanlış; `without` preposition olduğu için gerund gerekir.

## 15. `be required to`

### Yapı

```text
subject + be required + to-infinitive
```

Zorunluluk belirten formal passive yapıdır.

> **English:** “The caller is required to handle or declare the checked
> exception.”
>
> **Türkçe:** “Çağıran kodun, checked exception’ı ele alması veya bildirmesi gerekir.”

Yakın anlam:

- `must`
- `have to`
- `be obliged to`

Technical specification'da `is required to`, tavsiyeden daha güçlüdür.

## 16. `provided (that)`

### Yapı

```text
main clause + provided (that) + condition
```

“Şu koşulla ki / olması şartıyla” anlamında condition bildirir.

> **English:** “The reset succeeds provided that the mark is still valid.”
>
> **Türkçe:** “İşaretlenen konum hâlâ geçerliyse sıfırlama işlemi başarılı olur.”

Yakın anlam: `as long as`, `on condition that`. `provided` burada past
participle değil conjunction'dır.

## 17. `unless`

### Yapı

```text
main clause + unless + affirmative condition
```

`if ... not` anlamı verir.

> **English:** “For an existing target file and a different source, the copy fails unless REPLACE_EXISTING is supplied.”
>
> **Türkçe:** “Hedef dosya zaten mevcutsa ve kaynak farklı bir dosyaysa, `REPLACE_EXISTING` verilmedikçe kopyalama başarısız olur.”

Sık hata: Türkçedeki “-medikçe” ekini gördüğün için `unless` yanına otomatik olarak `not` eklemek; önce koşulun anlamını denetle.


**Öncülü koru:** Hedef dosya mevcutsa, farklı bir kaynak dosyayı onun üzerine kopyalamak için `REPLACE_EXISTING` gerekir. Hedefin olmadığı bir durumda bu seçenek olmadan da kopyalama yapılabilir. İngilizce koşulu çevirirken soru kökündeki varsayımı atlama.

**Cümleyi parçala:** `[The copy]` özne, `[fails]` ana yüklem, `[unless REPLACE_EXISTING is supplied]` olumsuz koşul. `unless` yerine `if … not` koyarak anlamı kontrol et. `unless … not` her durumda dilbilgisi hatası değildir; iki olumsuzluk bu sorudaki anlamı değiştireceğinden gelişigüzel eklenmez.

**Kaynak bağlamı:** [Creating, Moving, and Deleting Files and Directories](bilingual_notes.md#creating-moving-and-deleting-files-and-directories).

## 18. `once + clause`

### Yapı

```text
once + event clause, result clause
```

Bir event tamamlanır tamamlanmaz veya tamamlandıktan sonra ortaya çıkan sonucu
bildirir.

> **English:** “Once the stream is closed, further writes may throw an
> exception.”
>
> **Türkçe:** “Stream kapatıldıktan sonraki yazma işlemleri exception fırlatabilir.”

`once` burada “bir kez” sayısı değil temporal conjunction'dır.

## 19. `rather` discourse marker

### Yapı

```text
not X; rather, Y
```

Önceki ifadeyi düzeltir veya daha doğru alternatifi verir.

> **English:** “The Path does not contain the file data; rather, it represents
> a location.”
>
> **Türkçe:** “`Path`, dosya verisini içermez; bir konumu temsil eder.”

`rather than` karşılaştırma/preference yapısı; standalone `rather` düzeltme
bağlacıdır.

## 20. `respectively`

### Yapı

```text
A and B correspond to X and Y, respectively.
```

İki listenin üyelerini aynı sırayla eşler.

> **English:** “InputStream and OutputStream read and write bytes,
> respectively.”
>
> **Türkçe:** “`InputStream` ve `OutputStream`, sırasıyla bayt okur ve yazar.”

Eşlemeyi çapraz yapma:

```text
A ↔ X
B ↔ Y
```

## 21. `as opposed to`

### Yapı

```text
X, as opposed to Y
```

İki kavramı karşılaştırıp X'i Y'den ayırır.

> **English:** “A character stream processes text, as opposed to raw bytes.”
>
> **Türkçe:** “Character stream, ham byte verisi yerine metin işler.”

Yakın anlam: `in contrast to`, `rather than`. `opposed` sonrasında `to`
preposition'dır.

## 22. `the more ..., the more ...`

### Yapı

```text
the + comparative + clause, the + comparative + clause
```

İki değişken arasında paralel artış/azalış ilişkisi kurar.

> **English:** “The larger the buffer is, the fewer individual I/O calls may
> be needed.”
>
> **Türkçe:** “Tampon ne kadar büyükse o kadar az tekil I/O çağrısı gerekebilir.”

Bu yapı ordinary definite article değildir; iki comparative clause birlikte
okunur.

## 23. Reduced relative clause

### Yapı

```text
noun + V-ing        ← noun that is V-ing
noun + V3           ← noun that is/was V3
```

> **English:** “A process monitoring the file system does not see an
> incomplete atomic move.”
>
> **Türkçe:** “Dosya sistemini izleyen bir process, atomic move işlemini kısmen tamamlanmış hâliyle
> görmez.”

> **English:** “The path returned by the method is absolute.”
>
> **Türkçe:** “Metodun döndürdüğü path mutlak bir yoldur.”

`monitoring` active; `returned` passive anlam taşır.


**Özne–yüklem denetimi:** “The path returned by the method is absolute.” cümlesinde `[The path returned by the method]` bütün olarak öznedir; ana yüklem `[is]` olur. `returned` ana geçmiş zaman yüklemi değildir: `the path that was returned by the method` biçiminde açılır.

**Özgün çeviri:** “Metodun döndürdüğü yol mutlaktır.” Önce ana cümleyi bul: `The path is absolute`; sonra yolu niteleyen parçayı çevir.

**Kaynak bağlamı:** [Interacting with NIO.2 Paths](bilingual_notes.md#interacting-with-nio2-paths).

## 24. `which` ile non-defining relative clause

### Yapı

```text
complete noun/clause, which + additional information
```

Ana iddiaya ek bilgi verir; comma ile ayrılır.

> **English:** “Files.lines() returns a stream, which must be closed.”
>
> **Türkçe:** “Files.lines(), kapatılması gereken bir stream döndürür.”

`which` bütün önceki clause'a da gönderme yapabilir. Defining clause'da comma
yoktur ve hangi öğeden söz edildiğini sınırlar.

## 25. `if` clause ve modal result

### Yapı

```text
if + present, may/can/will + base verb
```

Technical metinde koşula bağlı possibility veya consequence bildirir.

> **English:** “If the provider does not support atomic moves, the call may
> throw an exception.”
>
> **Türkçe:** “Sağlayıcı atomik taşıma işlemlerini desteklemiyorsa çağrı bir exception fırlatabilir.”

`may`, garantiyi değil olasılığı gösterir. OCP sorularında `may`, `must` ve
`will` ayrımı sonucu tamamen değiştirebilir.

## Mini quiz

1. “Target varsa method path'i döndürür.” cümlesini `provided that` ile çevir.
2. `rather than` ile `rather` discourse marker arasındaki fark nedir?
3. Boşluğu doldur:
   “The stream must be closed ___ it opens a file-system resource.”
   (`because` / `although`)
4. “Path file system'e erişilmeden normalize edilir.” cümlesini
   `without + V-ing` ile yaz.
5. `InputStream` ve `Reader` için byte/character eşlemesini `respectively`
   kullanarak kur.
6. `unless` kullanarak yaz:
   “If the mark is not valid, reset fails.”
7. “File'ı izleyen process” ifadesini reduced relative clause ile yaz.
8. `System.console()` hakkında certainty değil possibility bildiren bir cümle
   kur.

## Cevaplar

1. “The method returns the path provided that the target exists.”
2. `rather than` iki parallel seçeneği karşılaştırır; standalone `rather`
   önceki iddiayı düzeltip alternatif sunar.
3. `because`
4. “The path is normalized without accessing the file system.”
5. “InputStream and Reader process bytes and characters, respectively.”
6. “Reset fails unless the mark is valid.”
7. “the process monitoring the file”
8. Örnek: “System.console() may return null.”

## Kısa tekrar özeti

- Preposition sonrası verb çoğunlukla `V-ing`: `by reading`, `without closing`,
  `in charge of writing`.
- `so that` amaç/sonuç; `so ... that` derece-sonuç yapısıdır.
- `whereas`, `as opposed to` ve `rather than` contrast kurar.
- `assuming`, `provided that`, `unless` ve `if` sonucu koşula bağlar.
- `may`, `can`, `must` ve `will` aynı certainty düzeyinde değildir.
- Reduced relative clause'da `V-ing` active, `V3` çoğunlukla passive anlam
  taşır.
- `respectively` iki listeyi aynı sırayla eşler.
