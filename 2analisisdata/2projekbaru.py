import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('2analisisdata/2nilai_siswa.csv')

data.info()
data.head()
data.describe()

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Mapel'] == 'Matematika']
print(matematika)

data.groupby('Mapel')['Nilai'].agg(['max','min'])

rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()