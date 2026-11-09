import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Panggil data untuk dipelajari
df = pd.read_csv('data_test/data.csv')

# Bersihkan Tabel Yang tidak diperlukan dalam pembelajaran
df_clean = df.drop(['id', 'Unnamed: 32'], axis=1)

df_clean['diagnosis'] = df_clean['diagnosis'].map({'M':1, 'B':0})

y = df_clean['diagnosis']

X = df_clean.drop(['diagnosis'], axis=1)

# Tes Pembelajaran
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree
data_cancer = DecisionTreeClassifier(random_state=42)

data_cancer.fit(X_train, y_train)

predic_cancer = data_cancer.predict(X_test)

result_cm = confusion_matrix(y_test, predic_cancer)
result_cr = classification_report(y_test, predic_cancer)

# Random Forest
model_rf = RandomForestClassifier(random_state=42)

model_rf.fit(X_train, y_train)

predict_rf = model_rf.predict(X_test)

result_rf = accuracy_score(y_test, predict_rf)

# KNeighbors
model_knn = KNeighborsClassifier()

model_knn.fit(X_train, y_train)

predict_knn = model_knn.predict(X_test)

result_knn = accuracy_score(y_test, predict_knn)

print(f"Dataset awal:\n {df}")
print(60*"-=")
print(f"Tabel data yang siap dipelajari: \n{X}" )
print(f"Dimensi Data Latih (X_train): {X_train.shape}\n")
print(f"Dimensi Data Latih (X_test): {X_test.shape}\n")      
print(60*"-=")
print(f"Akurasi Mesin Model Confusion Matrix:\n {result_cm}\n")
print(60*"-=")
print(f"Akurasi Mesin Model Classification Report:\n {result_cr}\n")
print(60*"-=")
print(f"Akurasi Mesin Model Random Forest: {result_rf}\n")
print(f"Akurasi Mesin Model KNeighbors: {result_knn}")