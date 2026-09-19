# Ünite 13 · Refactoring to microservices

Bu ünite, kullanıcının sağladığı *Microservices Patterns* kitabının 13. bölümünü (kaynak PDF s. 428–471) İngilizce–Türkçe karşılaştırmalı çalışır. Monolitten geçişin gerekçelerini, Strangler application yaklaşımını, servis çıkarma sırasını ve FTGO teslimat örneklerini kaynak sırasıyla içerir.

## İçindekiler

- [Ana çift dilli ders — Markdown](bilingual_notes.md) · [PDF](bilingual_notes.pdf)
- [Ünite sözlüğü — Markdown](vocabulary.md) · [PDF](vocabulary.pdf)
- [Grammar notları — Markdown](grammar_notes.md) · [PDF](grammar_notes.pdf)
- [İçerik ve PDF kontrol raporu](review_report.md)

## Öğrenme hedefleri

- Yazılım teslimat sorunlarının mimariden mi, geliştirme sürecinden mi kaynaklandığını ayırmak.
- Yeni özellikleri servis olarak geliştirmek, sunum katmanını ayırmak ve iş yeteneklerini servis olarak çıkarmak arasındaki farkları açıklamak.
- Domain model ve veritabanı ayrımında primary key, veri çoğaltma ve anti-corruption layer kullanımını anlamak.
- Saga adımlarını dikkate alarak monolitteki değişiklikleri azaltan çıkarma sırasını değerlendirmek.
- Delayed Order Service ile Delivery Service örneklerini ve feature toggle ile aşamalı geçişi izlemek.

## Çalışma sırası

Önce ana dersin bir alt bölümündeki İngilizce metni okuyup hemen altındaki Türkçeyle karşılaştırın. Şekillerin İngilizce etiketlerini iki dilli açıklamalarla birlikte inceleyin. Ardından aynı bağlamdaki sözlük kartlarını ve grammar örneklerini çalışın; bu iki kaynağın sonundaki özgün mini quiz sorularını cevap anahtarını kapatarak çözün.

Kaynak bazı servis adlarını tutarsız kullanır. Ana dersteki editör notları bu adları ve anlamı etkileyen kaynak hatalarını açıklar. Kitabın kod parçaları bağımsız Java 17 programı değildir; iki arayüz parçasının derlenmeme nedenleri ilgili yerde belirtilmiştir.
