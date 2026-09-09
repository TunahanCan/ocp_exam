# Unit 12 · Modules — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) module, service ve
migration anlatımından seçilen gerçek teknik İngilizce yapılarını YDS okuma
stratejisiyle açıklar.


Örnekler kaynak bağlamını öğretmek için seçilmiş veya sadeleştirilmiştir;
“kaynak alıntısı” diye belirtilmeyen cümleler birebir kitap alıntısı değildir.
Her oturumda bir yapıyı çalış: **ana yüklem → özne → bağlaç → yan cümle →
doğal Türkçe** sırasını izle. Yapıyı ertesi gün örneğe bakmadan yeniden kur.

## 1. `consist of + noun`

### Yapı

```text
subject + consist(s) of + noun / noun phrase
```

Bir bütünün hangi parçalardan oluştuğunu belirtir. Passive kullanılmaz.

> **English:** “A real project consists of hundreds of classes grouped into
> packages.”
>
> **Türkçe:** “Gerçek bir proje, paketler hâlinde gruplanmış yüzlerce sınıftan oluşur.”

YDS ipucu: `consist of` = `be composed of`. `is consisted of` biçimi standart
kullanımda yanlıştır.

## 2. `group A into B`

### Yapı

```text
group + objects + into + categories/containers
objects + be grouped into + categories
```

Dağınık öğelerin gruplara ayrılmasını anlatır.

> **English:** “The module system groups related packages into modules.”
>
> **Türkçe:** “Modül sistemi, ilişkili paketleri modüller hâlinde gruplandırır.”

Passive cümlede asıl nesne subject olur: `Packages are grouped into modules.`

## 3. `in addition to + noun/gerund`

### Yapı

```text
in addition to + noun / pronoun / V-ing
```

“...e ek olarak” anlamı verir. `to` preposition olduğu için ardından verb
gelirse gerund kullanılır.

> **English:** “In addition to compiling code, the tools can describe
> modules.”
>
> **Türkçe:** “Araçlar, kod derlemeye ek olarak modülleri açıklayabilir.”

YDS ipucu: `in addition to` additive anlamlı bir prepositional phrase'dir;
contrast bildirmez.

## 4. `be referred to as`

### Yapı

```text
subject + be + referred to as + name/term
```

Bir kavramın hangi adla anıldığını bildirir.

> **English:** “A complex chain of conflicting JARs is often referred to as
> JAR hell.”
>
> **Türkçe:** “Çakışan JAR'lardan oluşan karmaşık zincir çoğu zaman JAR hell
> olarak adlandırılır.”

`refer to A as B` active; `A is referred to as B` passive biçimidir.

## 5. `depend on + noun`

### Yapı

```text
subject + depend(s) on + noun
depending on + noun
```

Bağımlılık veya sonucun bir koşula bağlı olduğunu anlatır.

> **English:** “The care module depends on the feeding module.”
>
> **Türkçe:** “Bakım modülü, besleme modülüne bağlıdır.”

YDS'de `dependent on` adjective, `dependency/dependence` noun family
üyeleridir.

## 6. `make sure (that) + clause`

### Yapı

```text
make sure (that) + subject + verb
make sure to + V1
```

Bir koşulun gerçekleşmesini güvenceye alır.

> **English:** “Make sure that the module name matches the descriptor.”
>
> **Türkçe:** “Modül adının tanımlayıcıyla eşleştiğinden emin olun.”

`make sure to compile` aynı subject'in eylemidir; `make sure that it compiles`
tam clause içerir.

## 7. `be required to + V1`

### Yapı

```text
subject + be required to + base verb
```

Kural veya zorunluluk bildirir.

> **English:** “An explicit named module is required to have a module
> descriptor.”
>
> **Türkçe:** “Açıkça tanımlanmış isimli bir modülün modül tanımlayıcısına sahip olması gerekir.”

YDS ipucu: Passive zorunluluk, `must` veya `have to` anlamına yaklaşır.

## 8. `allow + object + to + V1`

### Yapı

```text
allow + someone/something + to + base verb
allow + noun/gerund
```

İzin veya olanak sağlar.

> **English:** “A qualified export allows selected modules to access the
> package.”
>
> **Türkçe:** “Hedefleri belirtilmiş bir dışa açma yönergesi, seçilen modüllerin pakete erişmesine izin verir.”

`allow selected modules access` double-object yapısı da grammatical'dır;
`allow selected modules to access the package` teknik bağlamda hedef eylemi
daha açık gösterir.

## 9. Defining relative clause: `that/which`

### Yapı

```text
noun + that/which + verb
noun + that/which + subject + verb
```

Hangi nesneden söz edildiğini sınırlar.

> **English:** “An automatic module is a JAR on the module path that lacks an explicit module descriptor.”
>
> **Türkçe:** “Otomatik modül, module path üzerinde bulunan ve açık modül tanımlayıcısı içermeyen bir JAR’dır.”

Defining clause'ta comma kullanılmaz. Teknik tanımlarda `that` çok yaygındır.


**Cümleyi parçala:** `[An automatic module]` özne; `[is]` ana yüklem; `[a JAR …]` tanım; `[that lacks an explicit module descriptor]` JAR'ı niteleyen yan cümle. `that`, yan cümlenin öznesidir; ardından ikinci bir `it` eklenmez.

**Teknik anlam kontrolü:** Tanım, JAR'ın **module path üzerinde** bulunmasını da gerektirir. Descriptor içermeyen bir JAR classpath üzerinde olduğunda isimsiz modüle katılır.

**Kaynak bağlamı:** [Automatic Modules](bilingual_notes.md#automatic-modules).

## 10. Non-defining relative clause: `which`

### Yapı

```text
complete noun phrase, which + clause,
```

Zorunlu olmayan ek bilgi verir.

> **English:** “The descriptor declares dependencies, which makes the graph
> explicit.”
>
> **Türkçe:** “Modül tanımlayıcısı bağımlılıkları bildirir; bu da grafiği açık hâle getirir.”

YDS ipucu: Comma'dan sonraki `which`, bazen önceki clause'un tamamına gönderme
yapar.

## 11. `where + clause`

### Yapı

```text
place/system/situation + where + subject + verb
```

Fiziksel konumun yanında soyut environment veya situation da tanımlar.

> **English:** “The module path is the location where named modules are
> discovered.”
>
> **Türkçe:** “Module path, isimli modüllerin keşfedildiği konumdur.”

`where` ≈ `in which`; ancak her `which` yerine `where` kullanılamaz.

## 12. `except (that) / except for`

### Yapı

```text
statement + except that + clause
statement + except for + noun
```

Genel ifadeye istisna ekler.

> **English:** “The command is correct except that the class name uses
> slashes.”
>
> **Türkçe:** “Komut doğrudur; ancak sınıf adında eğik çizgiler kullanılmaktadır.”

`except that` tam clause, `except for` noun phrase alır.

## 13. `in order to + V1`

### Yapı

```text
in order to + base verb
in order not to + base verb
```

Amaç bildirir.

> **English:** “Export the package in order to make its public API
> accessible.”
>
> **Türkçe:** “`public` API’yi erişilebilir kılmak için paketi dışa açın.”

YDS'de çoğunlukla `to + V1` ile eş anlamlıdır; `in order that` ise clause alır.

## 14. `once + clause/past participle`

### Yapı

```text
once + subject + verb, main clause
once + past participle, main clause
```

Bir aşama tamamlandıktan sonraki sonucu anlatır.

> **English:** “Once placed on the module path, the legacy JAR becomes an
> automatic module.”
>
> **Türkçe:** “Eski yapıdaki JAR, module path üzerine konulduğunda otomatik modüle dönüşür.”

Reduced clause'ta gizli subject main clause subject'iyle aynı olmalıdır.

## 15. `rather than + parallel structure`

### Yapı

```text
noun rather than noun
V-ing rather than V-ing
to V rather than (to) V
```

Bir seçeneği diğerine tercih eder veya karşılaştırır.

> **English:** “The consumer depends on the service interface rather than the
> implementation.”
>
> **Türkçe:** “Tüketici, gerçekleştirim yerine servis arayüzüne bağımlıdır.”

YDS ipucu: `rather than` iki tarafta parallel form bekler.

## 16. `regardless of + noun`

### Yapı

```text
regardless of + noun / wh-clause
```

“...e bakılmaksızın” anlamında concessive yapı kurar.

> **English:** “The package remains concealed regardless of the class being
> public.”
>
> **Türkçe:** “Sınıf `public` olsa da paket gizli kalır.”

`regardless of whether ...` iki olasılığın sonucu değiştirmediğini gösterir.

## 17. `as long as + clause`

### Yapı

```text
main clause + as long as + condition
```

Koşul anlamında “...dığı sürece” demektir.

> **English:** “The provider implementation package can remain unexported as
> long as the module declares a valid `provides` directive.”
>
> **Türkçe:** “Modül geçerli bir `provides` yönergesi bildirdiği sürece sağlayıcının gerçekleştirim paketi dışa açılmadan kalabilir.”

Süre anlamındaki literal `as long as` ile koşul anlamını context'ten ayır.


**Koşulun yönünü çöz:** `A only if B`, “A varsa B gereklidir” demektir. `A if B`, B'yi A için yeterli koşul olarak sunar. Modül sorularında yalnız `public` görerek erişim sonucuna atlama.

**Özgün örnek:** “A public type is accessible only if its package is exported to the reading module.” → “Bir public türe ancak paketi, onu okuyan modüle dışa açılmışsa erişilebilir.” `[A public type]` özne, `[is accessible]` ana yüklem; `[only if …]` gerekli koşuldur. Bu cümle, dışa açmanın tek başına bütün erişim koşullarını sağladığını söylemez.

**Kaynak bağlamı:** [Exporting a Package](bilingual_notes.md#exporting-a-package).

## 18. `unlike + noun`

### Yapı

```text
unlike + noun/pronoun, clause
```

İki öğe arasında contrast kurar.

> **English:** “Unlike an explicit named module, an unnamed module has no
> effective descriptor.”
>
> **Türkçe:** “Açıkça tanımlanmış isimli modülden farklı olarak isimsiz modülün etkin bir tanımlayıcısı yoktur.”

`unlike` preposition'dır; ardından clause değil noun phrase gelir.

## 19. `by + V-ing`

### Yapı

```text
result + by + gerund
```

Bir sonucun hangi yöntemle elde edildiğini anlatır.

> **English:** “You can inspect dependencies by running `jdeps`.”
>
> **Türkçe:** “`jdeps` çalıştırarak bağımlılıkları inceleyebilirsiniz.”

YDS ipucu: `by` burada agent değil method bildirir.

## 20. `without + V-ing`

### Yapı

```text
without + noun / gerund
```

Bir eylemin başka bir eylem gerçekleşmeden yapıldığını bildirir.

> **English:** “An automatic module exports its packages without declaring
> them individually.”
>
> **Türkçe:** “Otomatik modül, paketlerini tek tek bildirmeden dışa açar.”

Preposition sonrası infinitive değil gerund kullanılır: `without declaring`.

## 21. `the first/next + noun + to + V1`

### Yapı

```text
the first/next/last + noun + to + base verb
```

Sıralamadaki kişi/nesnenin yaptığı işi compact relative clause ile verir.

> **English:** “The lowest-level library is the first component to migrate.”
>
> **Türkçe:** “En alt düzeydeki kütüphane, yeni yapıya taşınacak ilk bileşendir.”

`to migrate` burada amaç değil, noun'u niteleyen infinitive'dir.

## 22. `not only ... but also`

### Yapı

```text
not only + X + but also + Y
```

İki öğeyi emphasis ile ekler; X ve Y parallel olmalıdır.

> **English:** “Modules provide not only explicit dependencies but also strong
> encapsulation.”
>
> **Türkçe:** “Modüller, açık bağımlılıkların yanı sıra güçlü kapsülleme de sağlar.”

Clause başında `Not only` kullanılırsa inversion gerekebilir:
`Not only does it compile, but it also runs.`

## 23. `so that + clause`

### Yapı

```text
action + so that + subject + finite verb
```

Amaç veya hedeflenen sonucu bildirir. `can`, `could`, `will` ve `would` gibi
modal verb'ler yaygındır fakat zorunlu değildir.

> **English:** “Use a stable module name so that consumers do not break when
> the JAR filename changes.”
>
> **Türkçe:** “JAR dosyasının adı değiştiğinde tüketiciler bozulmasın diye sabit bir modül adı kullanın.”

`so that` clause alır; `so ... that` ise derece-sonuç yapısıdır.

## 24. `whether ... or ...`

### Yapı

```text
whether + alternative A + or + alternative B
```

İki olasılığı birlikte kapsar.

> **English:** “Module-level normal access depends on whether the package is
> exported to the caller or concealed.”
>
> **Türkçe:** “Module düzeyindeki normal erişim, package'ın caller'a export
> edilmiş mi yoksa gizlenmiş mi olduğuna bağlıdır.”

Preposition'dan sonra `if` yerine çoğunlukla `whether` gerekir:
`depends on whether`.

## Mini quiz · Özgün YDS/teknik İngilizce çalışması

1. An explicit named module consists ___ packages and a descriptor.
2. Packages are grouped ___ modules.
3. The JAR is referred to ___ an automatic module.
4. The application depends ___ two library modules.
5. The package remains hidden regardless ___ its public classes.
6. Choose the correct form: `without declare / without declaring` dependencies.
7. Complete: “Use `exports` in order ___ expose the public API.”
8. Which is correct: “Unlike an explicit named module, ...” or “Unlike an
   explicit named module has ...”?
9. Complete: “Not only ___ the tool list modules, but it also describes
   them.” (`does / do`)
10. Rewrite with a reduced clause: “Once the JAR is placed on the module path,
    it gets a name.”
11. Choose: “The result depends on `if / whether` the module is observable.”
12. `by running jdeps` yapısındaki `by` ne bildirir: agent, method, contrast?

## Cevaplar ve kısa açıklamalar

1. **of** — `consist of`.
2. **into** — Öğeler category/container içine gruplanır.
3. **as** — Passive naming pattern: `be referred to as`.
4. **on** — `depend on`.
5. **of** — `regardless of`.
6. **without declaring** — Preposition sonrası gerund gerekir.
7. **to** — `in order to + V1`.
8. **Unlike an explicit named module, an unnamed module has ...** — `unlike`
   sonrasında noun phrase, ardından tam main clause gelir.
9. **does** — Clause başındaki negative/additive yapı inversion gerektirir.
10. **Once placed on the module path, the JAR gets a name.**
11. **whether** — `depend on whether` tercih edilir.
12. **Method/yöntem** — Dependency analizinin nasıl yapıldığını gösterir.

## Hızlı YDS özeti

```text
parça/bütün       consist of
gruplama          group into
ekleme            in addition to / not only ... but also
isimlendirme      be referred to as
dependency        depend on
zorunluluk        be required to
amaç              in order to / so that
istisna           except that / except for
koşul             as long as
ödünleme          regardless of
karşılaştırma     unlike / rather than
yöntem            by + V-ing
yokluk            without + V-ing
alternatif        whether ... or
```
