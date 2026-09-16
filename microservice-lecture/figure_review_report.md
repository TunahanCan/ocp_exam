# Ünite 02–13 özgün görsel kontrol raporu

## Kapsam

Kaynak PDF: `Microservices_Patterns_1_Bolumden_Itibaren.pdf`. Ünite 01 görselleri değiştirilmedi. Ünite 02–13 içindeki 172 numaralı şekil çıkarıldı.

| Ünite | Şekil sayısı |
| --- | ---: |
| [unit_02_decomposition_strategies](units/unit_02_decomposition_strategies/assets/manifest.json) | 13 |
| [unit_03_interprocess_communication_in_a_microservice_architecture](units/unit_03_interprocess_communication_in_a_microservice_architecture/assets/manifest.json) | 18 |
| [unit_04_managing_transactions_with_sagas](units/unit_04_managing_transactions_with_sagas/assets/manifest.json) | 15 |
| [unit_05_designing_business_logic_in_a_microservice_architecture](units/unit_05_designing_business_logic_in_a_microservice_architecture/assets/manifest.json) | 14 |
| [unit_06_developing_business_logic_with_event_sourcing](units/unit_06_developing_business_logic_with_event_sourcing/assets/manifest.json) | 13 |
| [unit_07_implementing_queries_in_a_microservice_architecture](units/unit_07_implementing_queries_in_a_microservice_architecture/assets/manifest.json) | 14 |
| [unit_08_external_api_patterns](units/unit_08_external_api_patterns/assets/manifest.json) | 11 |
| [unit_09_testing_microservices_part_1](units/unit_09_testing_microservices_part_1/assets/manifest.json) | 11 |
| [unit_10_testing_microservices_part_2](units/unit_10_testing_microservices_part_2/assets/manifest.json) | 8 |
| [unit_11_developing_production_ready_services](units/unit_11_developing_production_ready_services/assets/manifest.json) | 17 |
| [unit_12_deploying_microservices](units/unit_12_deploying_microservices/assets/manifest.json) | 15 |
| [unit_13_refactoring_to_microservices](units/unit_13_refactoring_to_microservices/assets/manifest.json) | 23 |

## Çıkarma ve doğrulama

- Kaynak sayfalar Poppler `pdftoppm` ile 240 dpi çözünürlükte render edildi; renkler, oklar ve şekil içindeki İngilizce etiketler korundu.
- Caption metinleri ayrı tutuldu. Her `assets/manifest.json` kaynak sayfa, şekil/caption koordinatları, İngilizce caption, piksel boyutu, SHA-256 ve çözünürlük bilgisini içerir.
- 172 şeklin tamamı 34 contact sheet üzerinde görsel olarak kontrol edildi. Metin bulaşması, kesilen etiket, kaybolan ok ve hatalı sınırlar incelendi.
- Figure 4.7: Caption, son durum dairesiyle aynı satırda bulunduğundan caption alanı beyazla dışarı alındı. Şeklin çizim ve etiket pikselleri değiştirilmedi. Bu istisna manifestte belirtildi.
- Figure 9.1 ve Figure 11.16: Yandaki caption nedeniyle ilk otomatik kırpmanın kestiği alt bölümler genişletilerek düzeltildi. Üç özel şekil tam çözünürlükte yeniden kontrol edildi.
- Tüm varlıkların dosya varlığı, SHA-256, kaydedilmiş piksel boyutu, 240 dpi bilgisi, dolu caption alanı ve kesintisiz şekil numarası doğrulandı. Koyu çizim piksellerinin görüntü kenarına dayanmadığı otomatik olarak kontrol edildi.

Bu rapor, özgün şekillerin çıkarılmasını doğrular; oluşturulacak çift dilli PDF sayfalarının yerleşim kontrolü ayrıca yapılmalıdır.
