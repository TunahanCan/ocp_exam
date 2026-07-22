# Unit 03 Vocabulary · Making Decisions

Bu sözlük Unit 03 review metnindeki control flow, loop, switch ve pattern
matching bağlamlarından seçilmiştir.

## A–F

### accessible · adjective

- **Türkçe:** erişilebilir
- **Teknik bağlam:** Bir pattern variable'ın belirli control-flow path'inde
  kullanılabilir olması.
- **Example:** The pattern variable is accessible only on matching paths.
- **Çeviri:** Pattern variable yalnız eşleşen path'lerde erişilebilirdir.
- **Word family:** access (n./v.), accessibility (n.); **antonym:** inaccessible

### account for · phrasal verb

- **Türkçe:** hesaba katmak, kapsamına almak
- **Teknik bağlam:** Switch'in olası bütün enum veya selector value'larını
  karşılaması.
- **Example:** The cases account for every enum constant.
- **Çeviri:** Case'ler her enum constant'ı kapsar.
- **Synonym:** cover, include

### branching · noun / adjective

- **Türkçe:** dallanma, akışı dallara ayırma
- **Teknik bağlam:** Bir condition veya selector değerine göre program
  execution'ının farklı path'lerden birine yönelmesi.
- **Example:** Branching redirects control to the first matching case.
- **Çeviri:** Branching, kontrolü ilk eşleşen case'e yönlendirir.
- **Word family:** branch (n./v.); **related:** control flow, path

### discern · verb

- **Türkçe:** ayırt etmek, kesin olarak belirlemek
- **Teknik bağlam:** Compiler'ın bir flow path'inde pattern type'ını kesin
  bilmesi.
- **Example:** The compiler can discern the pattern variable's type.
- **Çeviri:** Compiler pattern variable'ın type'ını belirleyebilir.
- **Word family:** discernible (adj.), discernment (n.)

### distinct · adjective

- **Türkçe:** birbirinden farklı
- **Teknik bağlam:** Birden fazla kez basılsa bile unique output value'larını
  istemek.
- **Example:** The method prints two distinct numbers.
- **Çeviri:** Method birbirinden farklı iki sayı yazdırır.
- **Synonym:** different, separate

### exhaustive · adjective

- **Türkçe:** bütün olasılıkları kapsayan
- **Teknik bağlam:** Switch expression'ın her selector/path için result üretmesi.
- **Example:** A switch expression must be exhaustive.
- **Çeviri:** Switch expression bütün olasılıkları kapsamalıdır.
- **Word family:** exhaustively (adv.); **synonym:** comprehensive

### extraneous · adjective

- **Türkçe:** gereksiz, fazladan
- **Teknik bağlam:** Sonuca etkisi olmayan loop variable veya syntax öğesi.
- **Example:** The variable `j` is extraneous in this loop.
- **Çeviri:** `j` variable'ı bu loop'ta gereksizdir.
- **Synonym:** unnecessary, redundant

### fall-through · noun / adjective

- **Türkçe:** bir sonraki case'e akış
- **Teknik bağlam:** Colon-style switch'te `break` yoksa execution'ın sonraki
  case'e geçmesi.
- **Example:** Arrow cases prevent fall-through.
- **Çeviri:** Arrow case'ler fall-through'u önler.
- **Related:** branching

### flow scoping · noun phrase

- **Türkçe:** akışa bağlı kapsam
- **Teknik bağlam:** Pattern variable'ın yalnız match'in kesin olduğu path'te
  erişilmesi.
- **Example:** Flow scoping makes the variable available after a successful match.
- **Çeviri:** Flow scoping başarılı match sonrasında variable'ı erişilebilir yapar.
- **Related:** pattern matching, scope

## I–R

### infinite loop · noun phrase

- **Türkçe:** sonsuz döngü
- **Teknik bağlam:** Termination condition hiçbir zaman false olmayan loop.
- **Example:** The unchanged condition produces an infinite loop.
- **Çeviri:** Değişmeyen condition sonsuz döngü oluşturur.
- **Related:** terminate, iteration

### iteration · noun

- **Türkçe:** döngü adımı, yineleme
- **Teknik bağlam:** Loop body'nin tek bir çalışması.
- **Example:** The value changes after each iteration.
- **Çeviri:** Değer her iteration sonrasında değişir.
- **Word family:** iterate (v.), iterative (adj.)

### matching path · noun phrase

- **Türkçe:** eşleşmenin geçerli olduğu akış yolu
- **Teknik bağlam:** Pattern variable'ın definitely matched kabul edildiği
  control-flow branch'i.
- **Example:** The variable remains in scope on the matching path.
- **Çeviri:** Variable eşleşen path üzerinde scope içinde kalır.
- **Related:** flow scoping, branch

### preceding · adjective

- **Türkçe:** önce gelen
- **Teknik bağlam:** Bir `else` statement'ın bağlanabileceği daha önceki `if`.
- **Example:** The final `else` has no preceding `if`.
- **Çeviri:** Son `else`in önünde eşleşen bir `if` yoktur.
- **Word family:** precede (v.); **antonym:** following

### reverse order · noun phrase

- **Türkçe:** ters sıra
- **Teknik bağlam:** Array'i son index'ten sıfıra doğru dolaşma.
- **Example:** The loop prints the array in reverse order.
- **Çeviri:** Loop array'i ters sırada yazdırır.
- **Antonym:** declaration order, forward order

## S–Y

### scope · noun

- **Türkçe:** kapsam
- **Teknik bağlam:** Bir variable veya label'ın source code içinde erişilebilir
  olduğu bölge.
- **Example:** The local variable is out of scope in the condition.
- **Çeviri:** Local variable condition içinde scope dışındadır.
- **Related:** visibility, lifetime

### selector · noun

- **Türkçe:** seçici ifade
- **Teknik bağlam:** Switch'in hangi case branch'ini değerlendireceğini
  belirleyen expression.
- **Example:** A `long` value is not a valid Java 17 switch selector.
- **Çeviri:** `long` değer Java 17 için geçerli switch selector değildir.
- **Related:** select (v.), selection (n.)

### skip · verb

- **Türkçe:** atlamak
- **Teknik bağlam:** `continue` ile current iteration'ın kalanını çalıştırmamak.
- **Example:** Continue skips the rest of the iteration.
- **Çeviri:** Continue iteration'ın kalanını atlar.
- **Word family:** skipping (n./adj.)

### terminate · verb

- **Türkçe:** sonlanmak, sonlandırmak
- **Teknik bağlam:** Loop execution'ın bitmesi.
- **Example:** The loop does not terminate at runtime.
- **Çeviri:** Loop runtime'da sonlanmaz.
- **Word family:** termination (n.), terminal (adj.); **antonym:** continue

### termination condition · noun phrase

- **Türkçe:** sonlandırma koşulu
- **Teknik bağlam:** Bir loop'un sürüp sürmeyeceğini belirleyen boolean
  expression.
- **Example:** Update the variable so the termination condition is eventually met.
- **Çeviri:** Termination condition'ın sonunda sağlanması için variable'ı güncelle.
- **Related:** infinite loop, iteration, terminate

### unreachable · adjective

- **Türkçe:** erişilemez
- **Teknik bağlam:** Control flow'un hiçbir durumda ulaşamayacağı statement.
- **Example:** The statement after an unconditional break is unreachable.
- **Çeviri:** Koşulsuz break sonrasındaki statement erişilemezdir.
- **Word family:** reach (v.), reachability (n.)

### yield · verb / contextual keyword

- **Türkçe:** değer üretmek
- **Teknik bağlam:** Switch-expression block'undan result value döndürmek.
- **Example:** Every reachable case block must yield a value.
- **Çeviri:** Her reachable case block bir value üretmelidir.
- **Related:** return, result

## Mini quiz

1. `iteration`, `terminate` ve `infinite loop` terimlerini ilişkilendir.
2. `preceding` kelimesini unmatched `else` bağlamında kullan.
3. `exhaustive` bir switch expression neyi garanti eder?
4. `reverse order` ifadesinin karşıtını yaz.
5. `branching` ile `termination condition` arasındaki farkı açıkla.

## Cevap anahtarı

1. Condition değişmezse iteration'lar sürer ve loop terminate olmayabilir.
2. Örnek: *An else statement requires a preceding if statement.*
3. Her selector/path için value veya abrupt completion bulunmasını.
4. `forward order` veya `declaration order`
5. `branching` execution'ı farklı path'lere ayırır; `termination condition` ise
   loop'un ne zaman duracağını belirler.
