import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 불러오기
data_path = r"C:\Users\spark\Documents\jonghuenkim_documents\CCEL_intern\과제\AuTiO2\density of state\Au_NP_TiO2_DOS.xlsx"
df_with_Au_NP = pd.read_excel(data_path, sheet_name='Au_NP')
df_only_TiO2 = pd.read_excel(data_path, sheet_name='only_TiO2')

# Energy 및 TDOS 값 추출
E1 = df_only_TiO2['Energy'].values
DOS1 = df_only_TiO2['TDOS-UP'].values

E2 = df_with_Au_NP['Energy'].values
DOS2 = df_with_Au_NP['TDOS-UP'].values

# TDOS의 가중 평균 (TDOS 중심, center of mass) 계산
center_E1 = np.average(E1, weights=DOS1)
center_E2 = np.average(E2, weights=DOS2)

# 에너지 shift 계산
energy_shift = center_E2 - center_E1

print(f"TDOS 중심 기준 에너지 shift: {energy_shift:.3f} eV")

# Energy 및 TDOS 값
E1 = df_only_TiO2['Energy'].values
DOS1 = df_only_TiO2['TDOS-UP'].values
E2 = df_with_Au_NP['Energy'].values
DOS2 = df_with_Au_NP['TDOS-UP'].values

# 에너지 범위 설정 (예: -5 eV ~ 2 eV)
E_min, E_max = 0, 5
#E_min, E_max = -25, -12

# TiO2 범위 제한
mask1 = (E1 >= E_min) & (E1 <= E_max)
E1_masked = E1[mask1]
DOS1_masked = DOS1[mask1]

# Au-NP@TiO2 범위 제한
mask2 = (E2 >= E_min) & (E2 <= E_max)
E2_masked = E2[mask2]
DOS2_masked = DOS2[mask2]

# 제한된 범위 내 TDOS peak 위치
peak_E1 = E1_masked[np.argmax(DOS1_masked)]
peak_E2 = E2_masked[np.argmax(DOS2_masked)]

# shift 계산
peak_shift = peak_E2 - peak_E1

print(f"제한된 에너지 범위 ({E_min} eV ~ {E_max} eV) 기준 TDOS 최대값 shift: {peak_shift:.3f} eV")

# 그래프 생성
fig, ax = plt.subplots(figsize=(8, 5))

# 두 그래프를 하나의 plot에 그림
ax.plot(df_with_Au_NP['Energy'], df_with_Au_NP['TDOS-UP'], label='Au NP on TiO₂', linewidth=1.5)
ax.plot(df_only_TiO2['Energy'], df_only_TiO2['TDOS-UP'], label='Pure TiO₂', linewidth=1.5, linestyle='-')

# 그래프 설정
ax.axvline(x=0, color='red', linestyle='-', linewidth=1.5)  # Fermi level 기준선
ax.set_xlabel('Energy (eV)')
ax.set_ylabel('Total Density of States (TDOS)')
ax.set_title('TDOS Comparison: Pure TiO₂ vs Au NP on TiO₂')
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
