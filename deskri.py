import numpy as np
import pandas as pd

# Data keuntungan perusahaan (misalnya)
keuntungan = [500, 600, 550, 450, 400, 700, 800, 650, 750, 500, 450, 600, 
              620, 500, 560, 530, 470, 610, 680, 710, 590, 570, 480, 550, 
              600, 490, 520, 480, 580, 600]

# Konversi ke DataFrame dan urutkan data dari terendah ke tertinggi
df = pd.DataFrame({'Keuntungan': keuntungan})
#step 1 pengurutan
df_sorted = df.sort_values(by='Keuntungan').reset_index(drop=True)

# Jumlah data (n)
n = len(df_sorted)

# Hitung jumlah kelas (menggunakan aturan Sturges)
num_classes = int(1 + 3.3 * np.log10(n))

# Hitung interval kelas
interval = (df_sorted['Keuntungan'].max() - df_sorted['Keuntungan'].min()) / num_classes

# Buat batas kelas, boundary kelas, nilai tengah, frekuensi, dan frekuensi relatif
class_limits = []
class_boundaries = []
midpoints = []
frequencies = []
relative_frequencies = []

lower_limit = df_sorted['Keuntungan'].min()

for i in range(num_classes):
    upper_limit = lower_limit + interval
    class_limits.append(f"{lower_limit:.2f} - {upper_limit:.2f}")
    class_boundaries.append(f"{lower_limit - 0.5:.2f} - {upper_limit + 0.5:.2f}")
    midpoints.append((lower_limit + upper_limit) / 2)

    # Hitung frekuensi untuk kelas ini
    freq = df_sorted[(df_sorted['Keuntungan'] >= lower_limit) & (df_sorted['Keuntungan'] < upper_limit)]['Keuntungan'].count()
    frequencies.append(freq)
    relative_frequencies.append(freq / n)

    lower_limit = upper_limit

# Buat DataFrame untuk hasil analisis
df_class = pd.DataFrame({
    'Class Limit': class_limits,#batas kelas
    'Class Boundary': class_boundaries, #Batas Bawah dan Atas Kelas
    'Midpoint': midpoints,#nilai tengah
    'Frequency': frequencies, #frekuensi
    'Relative Frequency': relative_frequencies
})

# Tampilkan hasil
print(df_class)
