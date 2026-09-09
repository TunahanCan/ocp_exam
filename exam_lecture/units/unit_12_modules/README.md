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
| 1 · Modül dosyası ve komutlar | [Creating and Running a Modular Program](bilingual_notes.md#creating-and-running-a-modular-program) | [1](bilingual_notes.md#question-1--soru-1), [3](bilingual_notes.md#question-3--soru-3), [14](bilingual_notes.md#question-14--soru-14) | descriptor / launcher / package | 1: consist of; 6: make sure |
| 2 · Okunabilirlik ve dışa açma | [Diving into the Module Declaration](bilingual_notes.md#diving-into-the-module-declaration) | [2](bilingual_notes.md#question-2--soru-2), [6](bilingual_notes.md#question-6--soru-6), [10](bilingual_notes.md#question-10--soru-10), [11](bilingual_notes.md#question-11--soru-11), [19](bilingual_notes.md#question-19--soru-19), [23](bilingual_notes.md#question-23--soru-23) | readability / accessible / qualified | 9–10: relative clause; 17: koşulun yönü |
| 3 · Servis rolleri | [Creating a Service](bilingual_notes.md#creating-a-service) | [4](bilingual_notes.md#question-4--soru-4), [9](bilingual_notes.md#question-9--soru-9), [13](bilingual_notes.md#question-13--soru-13), [16](bilingual_notes.md#question-16--soru-16), [21](bilingual_notes.md#question-21--soru-21), [25](bilingual_notes.md#question-25--soru-25) | consumer / service locator / provider | 8: allow; 15: rather than |
| 4 · JDK araçları | [Discovering Modules](bilingual_notes.md#discovering-modules) | [12](bilingual_notes.md#question-12--soru-12), [18](bilingual_notes.md#question-18--soru-18), [20](bilingual_notes.md#question-20--soru-20) | discover / internal / runtime image | 3: in addition to; 13: in order to |
| 5 · Modül türleri ve geçiş | [Comparing Types of Modules](bilingual_notes.md#comparing-types-of-modules) | [5](bilingual_notes.md#question-5--soru-5), [7](bilingual_notes.md#question-7--soru-7), [8](bilingual_notes.md#question-8--soru-8), [15](bilingual_notes.md#question-15--soru-15), [17](bilingual_notes.md#question-17--soru-17), [22](bilingual_notes.md#question-22--soru-22), [24](bilingual_notes.md#question-24--soru-24) | automatic / unnamed / migrate | 14: once; koşul çözümlemesi |
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
- [ ] Practice quiz'de en az **7/8** doğru yapıp yanlış seçenekleri
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
