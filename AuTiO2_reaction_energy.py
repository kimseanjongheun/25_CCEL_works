import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data_path = r"C:\Users\spark\Documents\jonghuenkim_documents\CCEL_intern\과제\AuTiO2\reaction\reaction_energy.xlsx"
df_R = pd.read_excel(data_path, sheet_name='reaction energy')
df_F = pd.read_excel(data_path, sheet_name='formation energy')

# 반응 에너지 계산
R_E_dic = {}
before_E = df_F['Glycerol Energy [eV]'].loc[0] + df_F['Slab Energy [eV]'].loc[0]

for i, p in enumerate(df_R['Position'].tolist()):
    after_E = df_R['Energy [eV]'].loc[i]
    R_E_dic[p] = after_E - before_E

R_min = min(R_E_dic.values()) - 0.15
R_max = max(R_E_dic.values()) + 0.15

# 막대 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(R_E_dic.keys(), R_E_dic.values(), width=0.4, align='center', color='g')
ax.set_ylim([R_min, R_max])
ax.set_xlabel('Position')
ax.set_ylabel('Energy [eV]')
ax.set_title('Reaction Energy vs. Position')
plt.xticks(rotation=45)  # x축 레이블 45도 회전

plt.tight_layout()
plt.show()
