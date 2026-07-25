# Unit 15 · JDBC — Practice Quiz

Bu belge altı adet **OCP tarzı özgün çalışma sorusu** içerir; sorular gerçek
sınavdan alınmamıştır. Önerilen süre 15–20 dakikadır. JDBC sorularında Java
compiler'ın kontrol ettiği type/checked-exception kurallarıyla driver veya
database tarafından runtime'da kontrol edilen SQL kurallarını ayır.

## Sorular

### Soru 1

**Odak:** JDBC interface ve implementation ayrımı

Aşağıdaki programın çıktısı nedir?

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class JdbcTypes {
    public static void main(String[] args) {
        System.out.print(Connection.class.isInterface() + ":"
                + DriverManager.class.isInterface() + ":"
                + PreparedStatement.class.isInterface());
    }
}
```

A. `true:false:true`

B. `false:true:false`

C. `true:true:true`

D. Kod derlenmez.

### Soru 2

**Odak:** Checked `SQLException`

Aşağıdaki class için hangisi doğrudur?

```java
import java.sql.Connection;

public class TransactionStart {
    void begin(Connection connection) {
        connection.setAutoCommit(false);
    }
}
```

A. Başarıyla derlenir; method `void` olduğu için exception bildirimi gerekmez.

B. **Does not compile**; `setAutoCommit()` tarafından bildirilen checked
`SQLException` handle veya declare edilmelidir.

C. Derlenir; yalnız connection `null` ise runtime'da `SQLException` oluşur.

D. Derlenir ve autocommit her durumda `false` olur.

<!-- page-break -->

### Soru 3

**Odak:** Doğru execute method'unu yorumlama

`PreparedStatement.execute()` method'unun döndürdüğü `boolean` neyi gösterir?

A. SQL statement'ın hatasız tamamlandığını

B. Transaction'ın commit edildiğini

C. İlk result'ın bir `ResultSet` olup olmadığını

D. En az bir row'un etkilendiğini

### Soru 4

**Odak:** Bind variable, cursor ve `INOUT`

Aşağıdaki ifadelerden **hangi ikisi doğrudur?**

A. İlk bind variable index'i `0`dır.

B. Yeni bir `ResultSet` üzerinde `next()` çağırmadan getter kullanmak ilk row'u
okur.

C. `INOUT` parameter için input value set edilmeli ve output type
`registerOutParameter()` ile kaydedilmelidir.

D. JDBC bind parameter index'leri `1`den başlar.

E. Java compiler SQL metnindeki placeholder sayısını setter çağrılarıyla
karşılaştırır.

### Soru 5

**Odak:** Transaction boundary ve portability

Autocommit `false` iken açık bir transaction bulunan `Connection` kapatılmadan
önce portable ve açık davranış için ne yapılmalıdır?

A. Hiçbir şey; `close()` bütün driver'larda transaction'ı kesin commit eder.

B. Hiçbir şey; `close()` bütün driver'larda transaction'ı kesin rollback eder.

C. Uygun iş kuralına göre açıkça `commit()` veya `rollback()` çağrılmalıdır.

D. Bir savepoint oluşturmak transaction'ı otomatik tamamlar.

### Soru 6

**Odak:** English → Turkish / YDS

Aşağıdaki cümleyi doğal Türkçeye çevir ve `as long as` yapısının anlamını
belirt:

> A prepared statement can be reused as long as values have been assigned to
> all required bind variables before execution.

<!-- page-break -->

## Cevaplar ve açıklamalar

### Soru 1 — A

- **A doğru:** `Connection` ve `PreparedStatement` JDBC interface'leridir;
  `DriverManager` ise JDK'nin sağladığı concrete class'tır. Çıktı
  `true:false:true` olur.
- **B yanlış:** Interface/class rolleri ters çevrilmiştir.
- **C yanlış:** `DriverManager` interface değildir.
- **D yanlış:** Type'ların tamamı Java 17 `java.sql` API'sinde bulunur ve code
  classpath'te derlenir.

### Soru 2 — B

- **A yanlış:** Return type'ın `void` olması checked exception kuralını
  değiştirmez.
- **B doğru:** `Connection.setAutoCommit(boolean)`, `SQLException` declare eder;
  `begin()` bunu catch etmediği veya `throws SQLException` ile bildirmediği
  için kod derlenmez.
- **C yanlış:** `null` connection bir `NullPointerException` nedeni olurdu,
  fakat mevcut kod compilation aşamasını geçemez.
- **D yanlış:** Driver call başarısız olabilir; ayrıca checked exception önce
  ele alınmalıdır.

### Soru 3 — C

- **A yanlış:** `false`, failure anlamına gelmez; update count veya no-result
  durumunu gösterebilir.
- **B yanlış:** `execute()` tek başına transaction commit sonucu bildirmez.
- **C doğru:** `true`, ilk result'ın `ResultSet` olduğunu; `false`, update count
  veya result bulunmadığını belirtir.
- **D yanlış:** Etkilenen row sayısı için uygun update method'u veya update
  count incelenir; boolean “en az bir row” testi değildir.

### Soru 4 — C ve D

- **A yanlış:** JDBC parameter index'leri zero-based değil one-based'dir.
- **B yanlış:** Initial cursor first row'dan önce konumlanır; önce `next()`
  çağrılmalıdır.
- **C doğru:** `INOUT`, hem input setter hem output registration gerektirir.
- **D doğru:** İlk placeholder index'i `1`dir.
- **E yanlış:** SQL sıradan bir `String`dir; placeholder count ve SQL validity
  çoğunlukla driver/database tarafından runtime'da denetlenir.

### Soru 5 — C

- **A yanlış:** Active transaction ile `close()` için portable JDBC contract
  bütün driver'larda commit garantisi vermez.
- **B yanlış:** Aynı şekilde bütün driver'larda rollback garantisi de yoktur.
- **C doğru:** Explicit `commit()` veya `rollback()` transaction'ın sonucunu
  açık, niyetli ve portable hâle getirir.
- **D yanlış:** Savepoint transaction içinde bir bookmark'tır; transaction'ı
  tamamlamaz.

### Soru 6 — Örnek çeviri

“Execution'dan önce gerekli bütün bind variable'lara değer atanmış olduğu
sürece bir prepared statement yeniden kullanılabilir.”

`as long as`, burada süre değil **koşul** bildirir ve “-dığı sürece” diye
çevrilir. `can be reused` modal passive'dir; `have been assigned` ise present
perfect passive yapısıdır. Önceki parameter value temizlenmediyse setter'ın her
execution öncesinde yeniden çağrılması gerekmez.
