# Unit 12 · Modules — Grammar Notes

Bu dosya, [ana çift dilli nottaki](bilingual_notes.md) module, service ve
migration anlatımından seçilen gerçek teknik İngilizce yapılarını YDS okuma
stratejisiyle açıklar.

## 1. `consist of + noun`

### Yapı

```text
subject + consist(s) of + noun / noun phrase
```

Bir bütünün hangi parçalardan oluştuğunu belirtir. Passive kullanılmaz.

> **English:** “A real project consists of hundreds of classes grouped into
> packages.”
>
> **Türkçe:** “Gerçek bir proje, package'lar halinde gruplanmış yüzlerce
> class'tan oluşur.”

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
> **Türkçe:** “Module system related package'ları module'lar halinde
> gruplandırır.”

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
> **Türkçe:** “Code derlemeye ek olarak tool'lar module'ları açıklayabilir.”

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
> **Türkçe:** “Care module feeding module'a bağlıdır.”

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
> **Türkçe:** “Module adının descriptor ile eşleştiğinden emin olun.”

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
> **Türkçe:** “Explicit named module'ın module descriptor'a sahip olması
> gerekir.”

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
> **Türkçe:** “Qualified export seçilen module'ların package'a erişmesine izin
> verir.”

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

> **English:** “An automatic module is a JAR that lacks an explicit module
> descriptor.”
>
> **Türkçe:** “Automatic module explicit module descriptor içermeyen bir
> JAR'dır.”

Defining clause'ta comma kullanılmaz. Teknik tanımlarda `that` çok yaygındır.

## 10. Non-defining relative clause: `which`

### Yapı

```text
complete noun phrase, which + clause,
```

Zorunlu olmayan ek bilgi verir.

> **English:** “The descriptor declares dependencies, which makes the graph
> explicit.”
>
> **Türkçe:** “Descriptor dependency'leri declare eder; bu da graph'ı explicit
> hale getirir.”

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
> **Türkçe:** “Module path, named module'ların keşfedildiği konumdur.”

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
> **Türkçe:** “Command doğrudur; ancak class name slash kullanmaktadır.”

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
> **Türkçe:** “Public API'yi erişilebilir yapmak için package'ı export edin.”

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
> **Türkçe:** “Legacy JAR module path'e konduğunda automatic module olur.”

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
> **Türkçe:** “Consumer implementation yerine service interface'e bağlıdır.”

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
> **Türkçe:** “Class public olsa da package gizli kalır.”

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
> **Türkçe:** “Module geçerli bir `provides` directive'i declare ettiği sürece
> provider implementation package'ı export edilmeden kalabilir.”

Süre anlamındaki literal `as long as` ile koşul anlamını context'ten ayır.

## 18. `unlike + noun`

### Yapı

```text
unlike + noun/pronoun, clause
```

İki öğe arasında contrast kurar.

> **English:** “Unlike an explicit named module, an unnamed module has no
> effective descriptor.”
>
> **Türkçe:** “Explicit named module'ın aksine unnamed module'ın effective
> descriptor'ı yoktur.”

`unlike` preposition'dır; ardından clause değil noun phrase gelir.

## 19. `by + V-ing`

### Yapı

```text
result + by + gerund
```

Bir sonucun hangi yöntemle elde edildiğini anlatır.

> **English:** “You can inspect dependencies by running `jdeps`.”
>
> **Türkçe:** “`jdeps` çalıştırarak dependency'leri inceleyebilirsiniz.”

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
> **Türkçe:** “Automatic module package'larını tek tek declare etmeden export
> eder.”

Preposition sonrası infinitive değil gerund kullanılır: `without declaring`.

## 21. `the first/next + noun + to + V1`

### Yapı

```text
the first/next/last + noun + to + base verb
```

Sıralamadaki kişi/nesnenin yaptığı işi compact relative clause ile verir.

> **English:** “The lowest-level library is the first component to migrate.”
>
> **Türkçe:** “En alt seviyedeki library migrate edilecek ilk component'tir.”

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
> **Türkçe:** “Module'lar yalnız explicit dependency değil, strong
> encapsulation da sağlar.”

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
> **Türkçe:** “JAR filename değiştiğinde consumer'ların bozulmaması için stable
> module name kullanın.”

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
