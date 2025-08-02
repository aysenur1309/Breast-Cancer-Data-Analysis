#skleran: ML Library 

from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
import pandas as pd

# (1) Veri Seti İncelemesi ve Analizi

cancer = load_breast_cancer()
df = pd.DataFrame(data = cancer.data, columns = cancer.feature_names)
df["target"] = cancer.target

# (2) ML Modelinin Seçilmesi - KNN Sınıflandırıcı 

# (3) Modelin Train Edilmesi 

X = cancer.data   #features
y = cancer.target   #target 

knn = KNeighborsClassifier()  # Model oluşturma 
knn.fit(X,y) # fit fonksiyonu verimizi(samples + target) kullanarak knn algoritmasını eğitir

# (4) Sonuçların Değerlendirilmesi : test 

y_pred = knn.predict(X)
accuracy_score()