# Breast-Cancer-Dataset-Analysis
Bu proje, **Scikit-learn** kütüphanesinde yer alan **"Breast Cancer Wisconsin (Diagnostic)"** veri seti kullanılarak gerçekleştirilmiş **keşifsel veri analizi (EDA)**, görselleştirme, veri ön işleme ve **lojistik regresyon** modeli ile **meme kanseri teşhis sınıflandırması** uygulamasını içermektedir.  •  

## Proje İçeriği 
 ✅ Veri Setinin Yüklenmesi ve İlk İnceleme

 ✅ Özellik (Feature) İsimlerinin Türkçeleştirilmesi

 ✅ Eksik Değer Analizi

 ✅ Sınıf Dağılımının Görselleştirilmesi

 ✅ Pozitif ve Negatif Korelasyon İncelemeleri

 ✅ Korelasyon Matrisi ve Isı Haritası

 ✅ Etiket Dönüşümü (Label Encoding)

 ✅ Ölçeklendirme (MinMaxScaler)

 ✅ Lojistik Regresyon ile Sınıflandırma

 ✅ Model Performans Değerlendirmesi:

✅ Confusion Matrix

✅ ROC Curve & AUC Skoru


##  📊 Görselleştirme Örnekleri

#### Sınıf Dağılımı
Bar grafiği ve pasta grafiği ile "iyi huylu" ve "kötü huylu" tümör sayıları görselleştirildi.

#### Korelasyon Analizi
Scatter plotlar ile pozitif ve negatif ilişkiler gösterildi.
Isı haritası (heatmap) ile tüm özellikler arası korelasyon incelendi.


##  Modelleme Süreci
#### 1. Etiket Dönüştürme
LabelEncoder ile tani sütunu 0 ve 1 olacak şekilde dönüştürüldü.

#### 2. Ölçeklendirme
Tüm veriler MinMaxScaler ile 0-1 aralığına ölçeklendirildi.

#### 3. Lojistik Regresyon
Veri %80 eğitim, %20 test olarak ayrıldı.
LogisticRegression modeli ile sınıflandırma gerçekleştirildi.
confusion_matrix ve roc_curve ile model performansı ölçüldü.


##  Model Performansı

- Confusion Matrix: Gerçek vs Tahmin
- ROC Eğrisi: Doğru pozitif oranı vs Yanlış pozitif oranı
- AUC Skoru: %90+ başarı oranı (örnek çıktılara bağlıdır)


## Kullanılan Kütüphaneler
-  **pandas**
-  **numpy**
-  **seaborn**
-  **matplotlib**
-  **scikit-learn** (datasets, model_selection, preprocessing, metrics, linear_model)


## 🛠️ Projeyi Çalıştırmak İçin
Anaconda veya Jupyter Notebook ortamında Python 3 ile çalıştırabilirsiniz.
Gerekli kütüphaneler yüklü değilse:

```bash
pip install pandas seaborn scikit-learn matplotlib


## 📚 Kaynak
**Breast Cancer Wisconsin Diagnostic Data Set**
