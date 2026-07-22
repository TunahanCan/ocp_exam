# Unit 03 · Technical Memory Notes · Making Decisions

Bu dosya eksiksiz [çift dilli Chapter 3 notunu](bilingual_notes.md), bütün decision ve loop
yapılarını kapsayan bir karar haritasıyla tamamlar. Ana soru şudur:
**Compiler bu path'i görebiliyor mu ve runtime bu path'e gerçekten giriyor mu?**
Dil çalışması: [vocabulary](vocabulary.md).

## Kapsam denetimi

Ana çift dilli kaynak `do/while`, enhanced `for`, switch expression, labels ve
pattern variable kurallarını tam kapsar. Bu hafıza notu şu çekirdek bağları
birlikte tekrar ettirir:

- switch statement ile switch expression farklarının tek tabloda görülmesi,
- selector/case type ve compile-time constant kuralları,
- loop'ların condition kontrol zamanı,
- label ile `break`/`continue` target kısıtları,
- pattern matching için flow scoping'in `&&`/`||` ile ilişkisi.

## 1. `if/else`: en yakındaki eşleşme

Condition mutlaka `boolean` olmalıdır; Java numeric value'ları truthy/falsy kabul
etmez.

```java
int x = 1;
if (x > 0)
    if (x > 10)
        System.out.print("large");
    else
        System.out.print("small"); // nearest unmatched if
```

Braces yoksa `else`, en yakındaki unmatched `if`e bağlanır.

**Hafıza cümlesi:** **`else` indentation'a değil, grammar'a bakar.**

## 2. Pattern matching for `instanceof`

```java
Object value = "lion";
if (value instanceof String text && text.length() > 3) {
    System.out.println(text.toUpperCase());
}
```

Pattern variable `text`, yalnız compiler'ın match'in kesin olduğunu bildiği
flow path'lerinde scope içindedir. `&&` sağında kullanılabilir; aşağıdaki
`||` örneğinde kullanılamaz:

```java
// if (value instanceof String text || text.isEmpty()) {} // Does not compile
```

Sol taraf `false` olduğunda `||` sağ tarafı çalışabileceği için `text` henüz
tanımlı olmayabilir.

## 3. Switch selector ve case kontrolü

Java 17'de klasik switch selector şu type'larla çalışır:

- `byte`, `short`, `char`, `int` ve wrapper karşılıkları,
- `String`,
- enum types.

`boolean`, `long`, `float` ve `double` klasik switch selector olamaz. `case`
label değerleri compile-time constant, selector ile compatible ve unique olmalıdır.

```java
final int one = 1;
int two = 2;
switch (value) {
    case one: break;  // geçerli constant variable
    // case two:      // Does not compile
}
```

## 4. Switch statement versus expression

| Özellik | Colon statement | Arrow statement/expression |
|---|---|---|
| Fall-through | Var | Yok |
| Sonuç üretme | Hayır | Expression ise zorunlu |
| Çok satırlı sonuç | N/A | Block + `yield` |
| Exhaustive olma | Zorunlu değil | Zorunlu |

```java
int length = switch (season) {
    case "WINTER", "SUMMER" -> 6;
    case "SPRING" -> {
        int base = 3;
        yield base + 3;
    }
    default -> 4;
};
```

Switch expression'ın her reachable path'i bir value üretmeli veya exception
fırlatmalıdır. Enum'un tüm constants'ı kapsanıyorsa explicit `default` her zaman
zorunlu değildir.

**Hafıza cümlesi:** Colon akabilir; arrow tek kola girer. Expression sonuçsuz
çıkamaz.

## 5. Loop zaman çizelgesi

| Loop | İlk condition'dan önce body çalışabilir mi? | Tipik kullanım |
|---|---:|---|
| `while` | Hayır | iteration sayısı bilinmiyor |
| `do/while` | Evet, tam bir kez | body en az bir kez gerekli |
| basic `for` | Hayır | init/condition/update birlikte |
| enhanced `for` | Collection/array elemanları kadar | index gerekmiyor |

Basic `for` akışı:

```text
initializer → condition → body → update → condition → ...
```

Initializer ve update bölümleri birden fazla expression taşıyabilir; declaration
varsa aynı statement'taki variable'lar compatible ortak type kullanmalıdır.

```java
for (int i = 0, j = 3; i < j; i++, j--) {}
```

Enhanced `for` yalnız array veya `Iterable` üzerinde çalışır:

```java
for (var item : items) {
    System.out.println(item);
}
```

Loop variable'a assignment yapmak array/collection elemanını otomatik değiştirmez.

## 6. Labels, `break`, `continue`, `return`

- Unlabeled `break`, nearest loop veya switch'ten çıkar.
- Labeled `break`, adı verilen labeled statement'ı sonlandırabilir.
- `continue`, yalnız loop target'ına gider; labeled target da loop olmalıdır.
- `return`, current method'u tamamen bitirir.

```java
OUTER: for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) continue OUTER;
    }
}
```

**Hafıza cümlesi:** `break` dışarı çıkar; `continue` sonraki turu çağırır;
`return` method'u kapatır.

## 7. Scope ve unreachable code

Bir block'ta bildirilen variable o block dışından erişilemez. `for` initializer
variable'ı yalnız loop header/body kapsamındadır. Compiler kesin biçimde hiçbir
zaman ulaşılamayan bazı statement'ları reddeder:

```java
while (true) {
    break;
    // System.out.println("never"); // unreachable
}
```

Infinite loop her zaman compilation error değildir; exit path gerekip gerekmediği
çevredeki statement'lara ve reachability kurallarına bağlıdır.

## OCP için 20 saniyelik analiz sırası

1. Önce compile-time scope: variable bu path'te erişilebilir mi?
2. Condition gerçekten boolean mı?
3. Switch case constant/compatible/unique mi?
4. Switch expression exhaustive ve bütün path'ler value üretiyor mu?
5. Loop'ta condition ne zaman, update ne zaman çalışıyor?
6. `break`/`continue` hangi exact target'a gidiyor?

## Aktif hatırlama · Özgün çalışma soruları

1. Pattern variable neden `instanceof ... || ...` sağında genellikle kullanılamaz?
2. Switch expression ile `yield` ne zaman gerekir?
3. Hangi loop body'yi condition'dan önce çalıştırır?
4. Labeled `continue` herhangi bir labeled block'a gidebilir mi?

## Cevaplar

1. Sol match `false` iken sağ taraf çalışabilir; pattern variable oluşmamıştır.
2. Arrow case block'u bir value üretirken.
3. `do/while`.
4. Hayır; target bir loop olmalıdır.
