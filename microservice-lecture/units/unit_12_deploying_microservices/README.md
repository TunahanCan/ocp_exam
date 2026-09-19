# Ünite 12 · Deploying microservices

**Mikroservisleri dağıtma** — *Microservices Patterns*, bölüm 12, kaynak PDF sayfaları **383–427**.

Bu ünite, dile özgü paket, sanal makine, container ve serverless seçeneklerini karşılaştırır; Kubernetes, Istio ve AWS Lambda örnekleri üzerinden dağıtım ile kullanıma açma arasındaki farkı öğretir.

## İçindekiler

| Materyal | Düzenlenebilir kaynak | Çalışma PDF’si |
|---|---|---|
| Bütün bölümün çift dilli ana dersi; 15 özgün şekil, 26 kod/komut bloğu | [Markdown](bilingual_notes.md) | [PDF](bilingual_notes.pdf) |
| 63 bağlamsal vocabulary kartı, karşılaştırmalar ve mini quiz | [Markdown](vocabulary.md) | [PDF](vocabulary.pdf) |
| 19 grammar başlığı, kaynak cümleleri ve mini quiz | [Markdown](grammar_notes.md) | [PDF](grammar_notes.pdf) |
| Üretim, kaynak aktarımı ve görsel kontrol kaydı | [Kontrol raporu](review_report.md) | — |
| Kaynak şekil sayfaları ve kırpım bilgileri | [Görsel manifesti](assets/manifest.json) | — |

## Konu sırası

1. **12.1:** Dile özgü paketleme: hızlı dağıtım, kaynak paylaşımı ve yalıtım sınırları.
2. **12.2:** VM imajları: teknoloji yığınını kapsülleme, yalıtım ve ek kaynak maliyeti.
3. **12.3:** Container imajı oluşturma, registry’ye gönderme ve çalıştırma.
4. **12.4:** Kubernetes nesneleri, readiness/liveness, kademeli güncelleme; Istio ile deployment ve release ayrımı.
5. **12.5:** AWS Lambda programlama modeli, çağırma yolları ve ödünleşimler.
6. **12.6:** RESTful servisin handler sınıfları, ZIP paketlemesi ve Serverless yapılandırması.

## Çalışma rotası

- İlk oturumda 12.1–12.3’ü okuyup dört dağıtım seçeneğinin yalıtım ve yönetim maliyetlerini karşılaştırın.
- İkinci oturumda 12.4’ü ve 12.9–12.12 şekillerini çalışın. Bir isteğin hangi pod’a neden yönlendirildiğini anlatın.
- Üçüncü oturumda 12.5–12.6’yı okuyun. Lambda function ile Java lambda expression’ın farklı kavramlar olduğunu hatırlayın.
- Her oturumda sözlükten beş terim, grammar notlarından iki yapı seçin. Ana dersin sonundaki özgün soruları cevap anahtarına bakmadan çözün.

## Kaynak ve teknik açıklamalar

Ana metin, kitaptaki başlık ve kayıt sırasını koruyan İngilizce–Türkçe çiftlerden oluşur. Kaynak şekiller yeniden çizilmemiştir. YDS ayrıntıları okuma akışından ayrılıp ünite sözlüğü ve grammar kaynağına alınmıştır.

Örneklerdeki Java 8, Istio 0.8, eski Kubernetes API’leri ve ürün değerlendirmeleri kitabın dönemine aittir. Güncel platformlara dağıtım testi yapılmamıştır. Kodlardaki baskı/satır kırılması sorunları giderilmiş; readiness süresi, NodePort, servlet imzası ve benzeri kaynak uyuşmazlıkları ayrı editör notlarında belirtilmiştir. Java 17 için bağımsız çalışır uygulama iddiası yoktur.

[Microservices çalışma merkezine dön](../../README.md)
