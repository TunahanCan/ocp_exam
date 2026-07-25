# Unit 12 · Modules

Bu ünite Java 17 Java Platform Module System (JPMS) konularını; module
oluşturma/çalıştırma, strong encapsulation, services, discovery tools, module
türleri ve migration stratejileri boyunca çift dilli ana ders akışıyla ele alır.

## Amaç ve öğrenme hedefleri

Bu ünitenin sonunda bir module graph'ı readability ve accessibility açısından
çözebilmen; descriptor directive'lerini doğru role yerleştirebilmen; command,
service ve migration sorularında named/automatic/unnamed module ayrımını
uygulayabilmen hedeflenir.

## Hangi belgeyi ne zaman kullanmalıyım?

| İhtiyacın | Kullanacağın belge | Markdown | PDF |
|---|---|---|---|
| JPMS konularını English → Türkçe eşleşmesiyle kaynak sırasından öğrenmek | Ana çift dilli ders notu | [Aç](bilingual_notes.md) | [Aç](bilingual_notes.pdf) |
| Directive, command ve migration kararlarını hızla tekrar etmek | Teknik hafıza notu | [Aç](technical_memory_notes.md) | [Aç](technical_memory_notes.pdf) |
| Module ve service terimlerini bağlamıyla çalışmak | Vocabulary | [Aç](vocabulary.md) | [Aç](vocabulary.pdf) |
| Teknik İngilizce yapıları ve YDS ipuçlarını pekiştirmek | Grammar notes | [Aç](grammar_notes.md) | [Aç](grammar_notes.pdf) |
| Bilgiyi kaynaklar kapalıyken altı soruyla ölçmek | Özgün practice quiz | [Aç](practice_quiz.md) | [Aç](practice_quiz.pdf) |
| Kaynaktaki bölüm sonu sorularını özgün kod ve seçenekleriyle çözmek | Review Questions | [Sorulara git](bilingual_notes.md#review-questions) | [Ana PDF](bilingual_notes.pdf) |

> Practice quiz içindeki sorular OCP tarzı **özgün çalışma sorularıdır**;
> gerçek sınavdan alınmış sorular olarak sunulmaz.

## 45–60 dakikalık önerilen çalışma rotası

1. **0–5 dk:** Konu haritasından descriptor/access, services veya migration
   kümelerinden birini seç.
2. **5–25 dk:** Ana çift dilli notta seçtiğin English → Türkçe paragraf
   çiftlerini ve ilgili figure/table'ı çalış.
3. **25–35 dk:** Teknik hafıza notunda module location → readability →
   `exports`/`opens` karar sırasını kaynak kapalıyken uygula.
4. **35–43 dk:** Vocabulary'den 6–8 terimle küçük bir module graph'ı sözlü
   anlat.
5. **43–50 dk:** Grammar notes içinden bir condition ve bir passive yapıyı
   örnekleriyle tekrar et.
6. **50–60 dk:** [Practice quiz](practice_quiz.md)'i çöz; her yanlış için
   descriptor, command, readability veya English etiketi koy.

## Kaynak kapsamı

- Ana kaynak:
  [OCP Java SE 17 PDF](../../OCP_Java_SE17_Chapter1den_Itibaren.pdf)
- Chapter 12 physical PDF pages: **661–720**
- Chapter 12 Appendix official answers: **949–951**
- Chapter gövdesi: **60/60 kaynak sayfa**
- Bölüm sonu: Summary, Exam Essentials ve Review Questions **1–25**
- Appendix: Official Answers **1–25** ve Java 17 gerekçeleri
- Görsel kaynaklar: **Figure 12.1–12.19** ve **Table 12.1–12.18**

Physical page 720 chapter'ın son review-question sayfasıdır; Chapter 13 physical
page 721'de başlar. Appendix page 951'in üst kısmı Chapter 12 Answers 20–25'i,
alt kısmı Chapter 13 cevaplarını içerir. Ana not yalnız Chapter 12 bölümünü alır.

## Önkoşul ve konu haritası

**Önkoşul:** Package, access modifier, classpath, JAR ve interface/implementation
ayrımını hatırlamak; temel terminal command sözdizimine aşina olmak yararlıdır.

- JPMS amacı, JAR hell, strong encapsulation ve module graph
- `module-info.java` konumu, module kaynak düzeni ve modular JAR
- `javac`, `java` ve `jar` ile compile, launch ve package workflow'u
- `exports`, qualified export, `requires` ve `requires transitive`
- `opens`, qualified opens ve `open module`
- Service provider interface, locator, consumer ve provider rolleri
- `uses`, `provides ... with ...` ve `ServiceLoader`
- Built-in `java.*` / `jdk.*` module'leri ve implicit `java.base`
- `java --describe-module`, `--list-modules`, `--show-module-resolution`
- `jar --describe-module`, `jdeps`, `--jdk-internals`, `jmod` ve `jlink`
- Named, automatic ve unnamed module karşılaştırması
- `Automatic-Module-Name` ve filename'dan module adı türetme algoritması
- Bottom-up / top-down migration ve cyclic dependency çözümü

## Hazır mıyım?

- [ ] Classpath ile module path'i ve unnamed/automatic/explicit named module'ü
  ayırabiliyorum.
- [ ] `requires`, `requires transitive`, `exports` ve `opens` etkilerini module
  graph üzerinde gösterebiliyorum.
- [ ] Service API, consumer ve provider için `uses` / `provides ... with ...`
  directive'lerini yerleştirebiliyorum.
- [ ] `javac`, `java`, `jar`, `jdeps` ve `jlink` option'larını doğru araçla
  eşleştirebiliyorum.
- [ ] Automatic module adını manifest veya filename kurallarından
  türetebiliyorum.
- [ ] Bottom-up ve top-down migration sırasını, cycle çözümüyle birlikte
  açıklayabiliyorum.
- [ ] Practice quiz'de en az **5/6** doğru yapıp yanlış seçenekleri
  gerekçelendirebiliyorum.

## Figure ve Table envanteri

### Figure 12.1–12.13 · Module ve service yapısı

- Zoo module graph'ı ve module iç yapısı
- Feeding, care, talks ve staff package/dependency şemaları
- Modular launch syntax'ı
- Transitive dependency graph'ı
- Service API, locator, consumer ve provider ilişkisi

### Figure 12.14–12.19 · Migration

- Dependency order ve birden fazla geçerli order
- Bottom-up ve top-down migration adımları
- Büyük project decomposition
- Cyclic dependency'nin shared module ile kırılması

### Table 12.1–12.18 · Sınav karar tabloları

- `javac`, `java`, `jar`, `jdeps`, `jmod` ve `jlink` seçenekleri
- Module-aware access control ve directive özeti
- Service rollerinin gerekli directive'leri
- Built-in module adları
- Automatic module-name dönüşümü
- Named/automatic/unnamed module özellikleri
- Bottom-up/top-down migration karşılaştırması

## Java 17 teknik doğruluk notları

- Explicit named module source tree'sinin kökünde `module-info.java`, compiled
  module/JAR kökünde `module-info.class` bulunur ve compiled artifact module
  path'ten kullanılır. Java API anlamında automatic module de bir ada sahiptir;
  OCP karşılaştırmasında ayrı tür olarak gösterilir.
- `exports`, package'ı normal erişime; `opens`, deep reflection'a açar.
- `requires transitive`, ordinary `requires` davranışına ek olarak readability'yi
  caller module'lere yayar; aynı dependency iki biçimde tekrar yazılamaz.
- `open module` bütün package'ları reflection'a açtığı için ayrıca `opens`
  directive içeremez; kod **Does not compile**.
- Export edilmeyen package içindeki `main()` command line'dan çalıştırılabilir;
  export, launch için değil inter-module erişim içindir.
- `ServiceLoader.stream()` bir `Stream<Provider<S>>` döndürür; service value için
  `Provider::get` gerekir.
- Automatic module module path'tedir; bütün package'ları export ve open kabul
  edilir, configuration'daki resolved named module'ları ve runtime'da her
  unnamed module'ı okur.
- Unnamed module classpath'tedir; içindeki `module-info.java` yok sayılır.
- JLS 17'nin formal modelinde unnamed module ilişkili bütün package'ları export
  ve open eder. Ordinary explicit named module'ün bunlara erişememesinin nedeni
  export değil, default readability ilişkisinin bulunmamasıdır.
- Unnamed module resolved named module'ları okuyabilir. Explicit named module
  ise command-line override yoksa unnamed module'ı okuyamaz; automatic module
  migration amaçlı istisnadır.
- Module'ler arası cyclic dependency **Does not compile**; aynı module içindeki
  package cycle'ları bu JPMS yasağının kapsamında değildir.
- `java.base` dışındaki her named module için `java.base` implicit
  dependency'dir ve describe çıktısında `requires java.base mandated`
  görünür.
- `jdeps` için `--module-path` vardır fakat bunun `-p` kısa biçimi yoktur.
- Kaynak Table 12.17 ile Official Answer 22, unnamed module export semantics'ini
  readability ile karıştırır; kaynak anahtarı korunmuş, formal Java 17
  düzeltmesi ana notta ayrı editör kutusunda verilmiştir.

## Önerilen çalışma sırası

1. `bilingual_notes.md` içindeki English → Türkçe paragraph çiftlerini chapter
   sırasıyla oku.
2. Her module örneğinde location, readability, `exports` ve `opens` adımlarını
   ayrı ayrı kontrol et.
3. Command sorularında önce aracı (`javac`, `java`, `jar`, `jdeps`, `jlink`),
   sonra option'ın o araçtaki anlamını belirle.
4. Service sorularında API → locator → consumer/provider rollerini ve her
   module'ün directive'lerini tablo hâlinde yaz.
5. Named/automatic/unnamed module ve migration tablolarıyla hızlı tekrar yap.
6. Review Questions 1–25'i Appendix'e bakmadan çöz; sonra doğru seçeneklerin yanı
   sıra yanlış seçeneklerin hangi Java 17 kuralına takıldığını incele.

Vocabulary, grammar ve teknik hafıza mini quiz'leri kitaptan alınmış gerçek sınav
soruları değil, açıkça belirtilmiş özgün çalışma sorularıdır.
