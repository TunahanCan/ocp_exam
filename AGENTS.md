# OCP Java 17 ve YDS Çalışma Projesi Kuralları

## Projenin amacı

Bu proje iki bağlantılı çalışma amacı taşır:

1. Java SE 17 Developer (OCP Java 17) sınavına sistemli biçimde hazırlanmak.
2. İngilizce teknik kaynakları Türkçeye çevirerek İngilizce okuma, kelime ve YDS becerilerini geliştirmek.

Ana çalışma alanı `exam_lecture/` klasörüdür. Ders notları özellikle
`exam_lecture/units/` altındaki mevcut ünite yapısı korunarak hazırlanmalı ve
zaman içinde birlikte geliştirilmelidir.

## İletişim dili ve öğretim yaklaşımı

- Kullanıcıyla varsayılan olarak Türkçe iletişim kur.
- Java anahtar kelimelerini, API adlarını, sınıf/metot adlarını ve sınavda
  karşılaşılabilecek önemli İngilizce terimleri özgün halleriyle koru.
- Yeni bir terim ilk geçtiğinde mümkünse `İngilizce terim (Türkçe karşılık)`
  biçimini kullan.
- Yalnızca sonucu verme; kuralın nedenini kısa ve anlaşılır şekilde açıkla.
- Konuları ezber listesi gibi değil, küçük örnekler ve karşılaştırmalarla öğret.
- Kullanıcının mevcut seviyesini küçümsemeden, belirsiz kalan ön bilgileri kısa
  hatırlatmalarla tamamla.
- Bir soru veya örnek birden fazla yoruma açıksa varsayımını açıkça belirt.

## Java ve OCP kapsamı

- Tüm Java açıklamaları ve örnekleri Java 17 davranışını esas almalıdır.
- Daha yeni Java sürümlerine ait özellikleri Java 17 kapsamında gibi sunma.
- OCP açısından önemli olan derleme hatası, çalışma zamanı hatası ve çıktı
  ayrımını her zaman açıkça belirt:
  - `Does not compile` / derlenmez
  - exception veya çalışma zamanı hatası
  - başarıyla derlenir ve ürettiği çıktı
- Sınav sorularında erişim belirleyicileri, kapsam, tür çıkarımı, overload,
  override, promotion, casting, generics, exception ve evaluation order gibi
  ince ayrıntıları gözden kaçırma.
- Bir kod örneğinin sonucunu iddia etmeden önce mümkünse Java 17 ile derle veya
  çalıştır. Derlenmesi özellikle beklenmeyen örneklerde hata mesajını doğrula.
- Test amaçlı geçici dosyaları ders klasörlerine bırakma. Kalıcı örnek kod
  eklenmesi istenirse Maven proje düzenini (`src/main/java`, `src/test/java`)
  koru.
- OCP sınav kapsamı veya güncel sınav politikaları hakkında kesin ve zamana
  duyarlı bir iddia gerekiyorsa güvenilir/öncelikli kaynakla doğrula; doğrulama
  yapılmadıysa bunu açıkça söyle.
- Her önemli başlıkta uygun olduğunda şu unsurları kullan:
  - temel kural
  - kısa Java örneği
  - beklenen sonuç veya derleme durumu
  - OCP sınav tuzağı
  - kısa kontrol sorusu

## `exam_lecture` içerik düzeni

- Mevcut ünite adlarını ve sıralamasını gerekmedikçe değiştirme.
- Yeni konu notunu ilgili `exam_lecture/units/unit_*` klasörüne yerleştir.
- Bir ünitenin `README.md` dosyasını ünitenin giriş ve içindekiler sayfası gibi
  kullan. Büyük konuları anlaşılır isimli ayrı Markdown dosyalarına böl.
- Dosya adlarında mevcut klasör düzeniyle uyumlu, küçük harfli ve açıklayıcı
  `snake_case` adları tercih et.
- Başlık seviyelerini düzenli kullan; aynı sayfada gereksiz tekrar oluşturma.
- Başka bir ünitede ayrıntılı anlatılan konuyu kopyalamak yerine göreli bağlantı
  ver ve burada yalnızca gereken özeti yaz.
- İçeriği küçük, takip edilebilir değişikliklerle ekle. Kullanıcı istemedikçe
  bütün üniteleri tek seferde yüzeysel biçimde doldurma.
- Yeni bir dosya eklediğinde ilgili ünite `README.md` içindekiler bölümünü de
  güncelle.
- Ders notlarında doğrulanmamış bilgi, uydurma kaynak veya uydurma sınav sorusu
  kullanma. Özgün pratik soru yazıldığında bunun çalışma sorusu olduğunu belirt;
  gerçek sınavdan çıkmış gibi sunma.

## Çeviri ve YDS çalışma kuralları

- Her ünitenin kendi İngilizce-Türkçe sözlük kaynağını tut. Sözlüğü ilgili
  `exam_lecture/units/unit_*/vocabulary.md` dosyasında sakla; dosya yoksa o
  ünitedeki ilk ihtiyaçta oluştur. Proje genelinde tek ve sürekli büyüyen bir
  sözlük dosyası oluşturma.
- Çalışmalarda karşılaşılan, YDS veya teknik İngilizce açısından öğrenmeye değer
  her yeni kelimeyi ve kalıbı çalışılan ünitenin sözlüğüne ekle. Aynı kelimeyi
  o ünite içinde tekrar eklemeden önce mevcut kayıtları kontrol et; yeni bağlam
  farklı bir anlam kazandırıyorsa aynı madde altında ayrı anlam veya örnek
  olarak işle. Bir kelime farklı ünitelerde önemliyse her ünitenin kendi
  bağlamına uygun biçimde bulunabilir.
- Sözlük maddelerinde mümkün olduğunda şu yapıyı kullan:
  - İngilizce kelime veya phrase
  - sözcük türü
  - Türkçe karşılığı
  - Java/teknik metindeki bağlamsal anlamı
  - kısa İngilizce örnek ve Türkçe çevirisi
  - yaygın synonym, antonym veya word family bilgisi
- Her ünitenin sözlüğünü alfabetik ve kolay taranabilir tut. Yeni bir terim
  eklendiğinde ilgili konu notundan ünitenin sözlüğüne göreli bağlantı ver.
- Her ünitenin kendi grammar kaynağını tut. Grammar notlarını ilgili
  `exam_lecture/units/unit_*/grammar_notes.md` dosyasında sakla; dosya yoksa o
  ünitedeki ilk ihtiyaçta oluştur. Proje genelinde tek bir grammar dosyası
  oluşturma.
- Çeviri sırasında daha önce kaydedilmemiş her yeni grammar veya sentence
  structure ile karşılaşıldığında grammar kaynağına kısa bir açıklama ekle.
  Açıklama şu bilgileri mümkün olduğunca içersin:
  - yapının adı
  - kısa ve sade Türkçe açıklaması
  - temel formülü veya cümle dizilimi
  - kaynak bağlamdan kısa bir İngilizce örnek
  - örneğin doğal Türkçe çevirisi
  - varsa YDS çözüm ipucu veya sık yapılan hata
- Ünitenin grammar kaynağına ekleme yapmadan önce aynı veya eşdeğer yapının o
  ünitede daha önce açıklanıp açıklanmadığını kontrol et. Varsa yeni başlık
  açmak yerine mevcut açıklamayı yeni örnek ya da önemli bir ayrıntıyla
  geliştir. Aynı yapı başka bir ünitede yeniden önemli hale gelirse o ünitenin
  bağlamına uygun kısa bir açıklama eklenebilir.
- Ünite içindeki çeviri notunda grammar yapısını kısaca işaretle ve ayrıntılı
  ünite grammar notuna göreli bağlantı ver. İlgili ünitenin `README.md`
  dosyasında hem `vocabulary.md` hem de `grammar_notes.md` bağlantılarını
  içindekiler bölümüne ekle.

## Ünite bazlı vocabulary ve grammar PDF'leri

- Her ünitede `vocabulary.md` ve `grammar_notes.md` kaynaklarına karşılık gelen
  `vocabulary.pdf` ve `grammar_notes.pdf` çalışma materyallerini hazırla.
- Markdown dosyalarını düzenlenebilir ana kaynak kabul et. PDF içeriğini ayrı ve
  bağımsız biçimde elle çoğaltma; kaynak değiştiğinde ilgili PDF'yi de güncelle.
- PDF'ler düz metnin sayfaya dökülmüş hali olmamalıdır. Okumayı ve hatırlamayı
  kolaylaştırmak için konuya uygun biçimde şunlardan yararlan:
  - dengeli renk paleti ve belirgin başlık hiyerarşisi
  - kelime kartları, tablolar ve kısa karşılaştırma kutuları
  - grammar formülleri ve cümle parçalarını ayıran renk kodları
  - Java bağlamlı örnekler ve doğal Türkçe çevirileri
  - memory tip, exam tip ve common mistake kutuları
  - mini quiz, eşleştirme veya boşluk doldurma alıştırmaları
  - yalnızca gerçekten fayda sağladığında küçük şema veya görsel çağrışımlar
- Görsel tasarım dikkat çekici fakat sade olmalı; aşırı renk, dekorasyon ve
  sıkışık yerleşim öğrenilecek içeriğin önüne geçmemelidir. Aynı ünite içindeki
  vocabulary ve grammar PDF'lerinde ortak bir görsel dil kullan.
- PDF'lerde Türkçe karakterleri destekleyen okunaklı fontlar, yeterli punto,
  tutarlı boşluklar ve yüksek kontrast kullan. Kod örneklerini monospace fontla
  ve satırları kesilmeyecek biçimde göster.
- İçeriği hatırlanabilir kılmak için uzun paragrafları kısa açıklamalara,
  örneklere ve anlamlı gruplara böl. Ancak görsel çekicilik uğruna teknik veya
  dilbilgisel doğruluktan ödün verme.
- Her PDF'de ünite adı, belgenin amacı ve sayfa numarası bulunsun. Uygun olduğunda
  son sayfaya kısa tekrar özeti ve cevap anahtarı ekle.
- Oluşturulan PDF'leri ilgili `unit_*` klasöründe sakla ve ünitenin `README.md`
  dosyasından hem Markdown hem PDF sürümlerine bağlantı ver.
- PDF üretildikten sonra sayfaları görsel olarak render edip kontrol et. Taşan
  veya kesilen metin, bozuk Türkçe karakter, okunamayacak küçük yazı, boş/eksik
  sayfa, kötü sayfa kırılması ve tutarsız hizalama varsa teslim etmeden önce
  düzelt.
- Bir ünitenin vocabulary veya grammar içeriği henüz boşsa sırf dosya üretmiş
  olmak için anlamsız PDF oluşturma. Yeterli içerik oluştuğunda PDF'yi üret ve
  sonraki içerik değişikliklerinde güncel tut.
- Çeviriyi yalnızca kelime kelime aktarma olarak ele alma. Önce cümlenin teknik
  anlamını koruyan doğal Türkçe çeviriyi ver, ardından öğrenmeye değer dil
  yapılarını açıkla.
- Kaynak metindeki Java terminolojisini bozma. Teknik doğruluğu korumak için
  gerekli İngilizce terimi Türkçe karşılığının yanında göster.
- Çeviri çalışması istendiğinde uygun olan şu düzeni kullan:
  1. özgün İngilizce cümle veya kısa bölüm
  2. doğal Türkçe çeviri
  3. önemli kelime ve kalıplar
  4. grammar / sentence structure notu
  5. YDS açısından eş anlamlı, bağlaç veya çıkarım ipucu
- Kelime listelerinde mümkün olduğunda şu bilgileri ekle:
  - kelime veya phrase
  - sözcük türü
  - bağlama uygun Türkçe anlam
  - kısa İngilizce örnek cümle
  - yaygın eş anlamlı veya karşıt anlamlı kelime
- YDS notlarını teknik metinden kopuk, rastgele kelime yığınlarına dönüştürme;
  üzerinde çalışılan Java metnindeki gerçek bağlamı esas al.
- İngilizce bir cümle doğal fakat birden fazla şekilde çevrilebiliyorsa temel
  çeviriyi ver ve önemli alternatifi kısaca açıkla.
- Kullanıcının yaptığı çeviriyi incelerken önce anlam hatalarını, sonra dil
  bilgisi ve doğallık sorunlarını göster; düzeltilmiş sürümü en sonda ver.
- Kaynak materyali gereksiz yere uzun ve birebir kopyalama. Alıntı ile özgün
  açıklama/özet arasındaki ayrımı koru.

## Önerilen ders notu şablonu

Her dosyanın bütün bölümleri taşıması zorunlu değildir; konuya uygun olanları
kullan:

```markdown
# Konu başlığı

## Learning objectives

## Temel kavramlar

## Kurallar ve Java 17 örnekleri

## OCP exam traps

## English → Turkish translation practice

## YDS vocabulary and structures

## Mini quiz

## Cevaplar ve açıklamalar

## Kısa tekrar özeti
```

## Soru hazırlama standardı

- Sorular Java 17 kurallarına göre tek ve savunulabilir bir cevaba sahip olsun;
  özellikle birden çok cevap seçilecekse kaç seçeneğin beklendiğini belirt.
- Kod sorularında gerekli import, package ve bağlam bilgisini eksik bırakma;
  eksikliğin bizzat ölçülen nokta olduğu durumlar hariç.
- Cevabı sorunun hemen içinde ele verme. Cevap anahtarında yalnızca doğru şıkkı
  değil, yanlış seçeneklerin neden yanlış olduğunu da kısa biçimde açıkla.
- Kolay tanım soruları ile derleme analizi, çıktı tahmini ve kavramsal tuzakları
  dengeli dağıt.
- Gerçek sınav sorularını bildiğini iddia etme; hazırlanan soruları OCP tarzı
  özgün çalışma soruları olarak tanımla.

## Değişiklik ve kalite kontrolü

- Mevcut kullanıcı içeriğini habersizce silme veya baştan yazma. Büyük yeniden
  düzenlemelerde önce mevcut amacı ve bağlantıları koru.
- Projede kullanıcının başka değişiklikleri varsa bunlara dokunma.
- Java dosyası veya Maven yapılandırması değiştiğinde uygun olan durumda
  `mvn test` çalıştır.
- Yalnızca Markdown değiştiğinde en azından bağlantıları, başlık yapısını, kod
  bloklarını ve yazım tutarlılığını gözden geçir.
- Kod bloklarında dil etiketi olarak `java`, terminal komutlarında `bash`
  kullan.
- Kullanıcı açıkça istemedikçe bağımlılık ekleme, Git commit oluşturma, branch
  değiştirme veya uzak depoya gönderme yapma.
- Tamamlanan işin sonunda hangi ders dosyalarının eklendiğini/değiştirildiğini ve
  hangi doğrulamanın yapıldığını kısa biçimde bildir.

## Öncelik sırası

Karar verirken şu öncelik sırasını izle:

1. Java 17 teknik doğruluğu
2. OCP sınavına yararlılık
3. İngilizce metnin anlamını koruyan doğru çeviri
4. YDS için öğretici dil analizi
5. Düzenli, sürdürülebilir ve tekrar etmeyen not yapısı
