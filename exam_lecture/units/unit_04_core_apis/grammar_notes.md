# Unit 04 Grammar Notes · Core APIs

Bu notlar Chapter 4 metninde ve review questions bölümünde geçen, teknik
İngilizce ile YDS açısından yararlı sentence structure'ları toplar. Eşdeğer
yapılar tek başlık altında birleştirilmiştir.

## 1. `which of the following` ile seçim sorusu

Bir seçenek grubundan seçim ister; bu yapı bir doğrudan sorudur, relative clause
değildir. Seçilecek öğe tekilse `returns`, çoğulsa `return` kullanılır.

**Formül:** `Which of the following + singular/plural verb ...?`
**EN:** Which of the following return 5?
**TR:** Aşağıdakilerden hangileri 5 döndürür?

**YDS/OCP ipucu:** `Which of the following` özne, `return` yüklemdir.
`Which ... returns?` tek seçim, `Which ... return?` çoğul seçim niyeti gösterebilir;
OCP sorusunda kaç seçenek istendiğini ayrıca yönergeden kontrol et.

## 2. `whether ... (or not)` ile iki olasılık

Bir durumun doğru olup olmadığını tarafsız biçimde sorgular.

**Formül:** `whether + clause + (or not)`
**EN:** Check whether the arrays are equivalent.
**TR:** Array'lerin eşdeğer olup olmadığını kontrol edin.

**Sık hata:** Dolaylı soruda `whether are the arrays ...` biçiminde soru word
order'ı kullanılmaz.

## 3. `when + V3` reduced passive

Passive time/condition clause'un kısaltılmış biçimidir.

**Formül:** `when + past participle`
**EN:** Which expressions, when run independently, return 5?
**TR:** Birbirinden bağımsız çalıştırıldığında hangi ifadeler 5 döndürür?

Tam biçim: `when the expressions are run independently`.

## 4. `given + noun phrase / given that + clause`

Soru bağlamını “verilen ... dikkate alındığında” anlamıyla kurar.

**Formül:** `given + noun phrase` / `given that + clause`
**EN:** Given the following array, which calls are valid?
**TR:** Aşağıdaki array verildiğinde hangi çağrılar geçerlidir?

**YDS ipucu:** `given`, bu kullanımda “verilmiş”ten çok “dikkate alındığında”
anlamı taşır.

## 5. `since` ile neden

`since` zaman anlamının yanında reason clause başlatabilir.

**Formül:** `result + since + reason`
**EN:** The result is unchanged since `LocalDate` is immutable.
**TR:** `LocalDate` immutable olduğu için sonuç değişmez.

**YDS ipucu:** Cümlede başlangıç zamanı yoksa ve sebep-sonuç ilişkisi varsa
`since` çoğunlukla “çünkü/-dığı için” anlamındadır.

## 6. `because of / due to + noun phrase`

`because` tam clause, `because of` ve `due to` ise noun phrase alır.

**Formül:** `result + because of/due to + noun phrase`
**EN:** The local time changes because of daylight saving time.
**TR:** Local time, yaz saati uygulaması nedeniyle değişir.

**Sık hata:** `because of the clock changes` yerine tam clause isteniyorsa
`because the clock changes` kullanılır.

## 7. `rather than` ile tercih veya karşıtlık

İki seçenek ya da davranış arasındaki farkı vurgular.

**Formül:** `A rather than B` / `V-ing rather than V-ing`
**EN:** `String.equals()` checks content rather than reference identity.
**TR:** `String.equals()`, referans kimliği yerine içeriği kontrol eder.

Bu özellik bütün sınıfların `equals()` metotlarına genellenmez; `StringBuilder`
varsayılan identity davranışını korur.

Paralel yapı korunmalıdır: noun–noun veya V-ing–V-ing.

## 8. `by + V-ing` ile yöntem

Bir sonucun hangi yöntemle elde edildiğini açıklar.

**Formül:** `main clause + by + V-ing`
**EN:** Java saves memory by reusing common String literals.
**TR:** Java ortak String literal'larını yeniden kullanarak bellek tasarrufu yapar.

**YDS ipucu:** `by` burada araç/yöntem bildirir; edilgen cümledeki “tarafından”
anlamıyla karıştırılmamalıdır.

## 9. `without + noun / V-ing`

Bir eylemin başka bir işlem yapılmadan gerçekleştiğini veya gerçekleşemediğini
anlatır.

**Formül:** `without + noun/V-ing`
**EN:** You cannot convert a `LocalDateTime` to an `Instant` without supplying a zone or offset.
**TR:** Zone veya offset sağlamadan bir `LocalDateTime` değerini `Instant` değerine dönüştüremezsiniz.

Kural bu dönüşüme aittir; `Instant.now()` çağrısına zone vermek gerekmez.

**Sık hata:** `without to supply` kullanılmaz; `without supplying` gerekir.

## 10. `as if / as though + clause`

Gerçek veya varsayımsal bir benzerlik kurar.

**Formül:** `as if + subject + verb`
**EN:** A varargs parameter can be used as if a normal array were passed in.
**TR:** Varargs parametresi, normal bir array geçirilmiş gibi kullanılabilir.

**YDS ipucu:** Varsayımsal anlatımda `were`, tekil subject ile de görülebilir.

## 11. `so that + clause` ile amaç veya sonuç

Bir işlemin hangi amaçla yapıldığını açıklar.

**Formül:** `action + so that + subject + can/will + verb`
**EN:** The arrays are sorted so that binary search can be used reliably.
**TR:** Binary search güvenilir biçimde kullanılabilsin diye array'ler sıralanır.

`so + adjective + that` ise derece-sonuç yapısıdır; bu yapıdan farklıdır.

## 12. `if` ile gerçek ve varsayımsal sonuçlar

API kurallarında hem gerçek koşul hem de gerçekleşmemiş varsayım kullanılır.

**Formül 1:** `If + present, present/will`
**EN:** If either operand of `+` is a `String`, Java uses concatenation.
**TR:** `+` operator'ının operand'larından biri `String` ise Java concatenation uygular.

**Formül 2:** `If + past perfect, would have + V3`
**EN:** If the return value had been assigned, the date would have changed.
**TR:** Dönüş değeri atanmış olsaydı tarih değişmiş olurdu.

**OCP ipucu:** İlk yapı Java kuralını, üçüncü conditional ise kaybedilmiş
immutable dönüş değerini anlatır.

## 13. `even though / although` ile ödünleme

Beklenenin tersine gerçekleşen durumu gösterir.

**Formül:** `although/even though + clause, main clause`
**EN:** Even though all elements are `null`, the array length is still six.
**TR:** Bütün elemanlar `null` olsa da array uzunluğu yine altıdır.

**Sık hata:** `although ... but ...` birlikte kullanılmaz; bağlaçlardan biri
yeterlidir.

## 14. `whereas / while` ile karşılaştırma

İki öznenin karşıt özelliklerini tek cümlede karşılaştırır.

**Formül:** `clause, whereas/while + contrasting clause`
**EN:** `String` is immutable, whereas `StringBuilder` is mutable.
**TR:** `String` immutable iken `StringBuilder` mutable'dır.

`while` zaman anlamına da gelebildiği için bağlam kontrol edilmelidir.

## 15. `up to / until / right before` ile sınır anlatımı

String indekslerinde bitiş noktasının dahil olup olmadığını ifade eder.

**Formül:** `from A up to/right before B`
**EN:** `substring()` returns characters up to, but not including, `endIndex`.
**TR:** `substring()`, `endIndex`'e kadar olan fakat bu indeksi içermeyen
karakterleri döndürür.

**OCP/YDS ipucu:** `up to` tek başına bağlama göre sınırı içerebilir. Buradaki
`but not including` ifadesi `[beginIndex, endIndex)` aralığını kesinleştirir.

## 16. `one past + noun` teknik kalıbı

Bir sınırın hemen sonrasındaki konumu anlatır.

**Formül:** `one past the end of + noun`
**EN:** `endIndex` may be one past the end of the String.
**TR:** `endIndex`, String sonunun bir ilerisi olabilir.

**OCP ipucu:** Bu konum `substring()` için geçerli bir exclusive boundary'dir;
`charAt()` için geçerli bir karakter indeksi değildir.

## 17. `no matter + wh-word` ile koşuldan bağımsızlık

Sonucun belirtilen değişkenden etkilenmediğini vurgular.

**Formül:** `no matter how/what/where + clause`
**EN:** The rule applies no matter how the array was declared.
**TR:** Array nasıl bildirilmiş olursa olsun kural geçerlidir.

**Synonym structure:** `regardless of how ...`

## Cümleyi parçalayarak okuma

[İlgili kaynak bölümü](bilingual_notes.md#getting-a-substring). Aşağıdaki çalışma cümlesi
kaynak bağlamına dayanır; gerektiğinde öğretim amacıyla sadeleştirilmiştir.

**English:** The method returns characters up to, but not including, the end index.

**Çözümleme:** `The method` = özne; `returns` = ana fiil; `characters` = nesne. `up to ... the end index` sınırı belirtir; aradaki `but not including` bu sınırın dahil olmadığını kesinleştirir.

**Doğal Türkçe:** Metot, bitiş indeksine kadar olan karakterleri döndürür; bitiş indeksi dahil değildir.

**Kapalı kitap kontrolü:** `not` kaldırılırsa sınırda hangi karakterin dahil olduğu değişir? `[1, 3)` aralığında kaç karakter var?

## Mini quiz

1. `when run independently` yapısını tam passive clause'a çevir.
2. `whether` kullanarak iki array'in eşitliğini sorgula.
3. `by + V-ing` ile string pool'un bellek avantajını anlat.
4. `as if` ile varargs–array ilişkisini yaz.
5. `[beginIndex, endIndex)` aralığını `up to, but not including` ile açıkla.
6. Immutable dönüş değerinin atanmadığını third conditional ile ifade et.

## Cevaplar

1. `when the expressions are run independently`
2. *Check whether the two arrays are equal.*
3. *Java saves memory by reusing common String literals.*
4. *A varargs parameter is used as if a normal array were passed in.*
5. *The method reads up to, but not including, `endIndex`.*
6. *If the result had been assigned, the date would have changed.*
