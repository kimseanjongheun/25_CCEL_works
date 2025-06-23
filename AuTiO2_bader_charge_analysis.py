import pandas as pd
import matplotlib.pyplot as plt
from ase.io import read
from ase.visualize.plot import plot_atoms

# 파일 경로
file_path = r"C:\Users\spark\Documents\jonghuenkim_documents\CCEL_intern\과제\AuTiO2\bader charge analysis\bader_charge_AuNP_on_TiO2.xlsx"
contcar_path = r"C:\Users\spark\Documents\jonghuenkim_documents\CCEL_intern\과제\AuTiO2\bader charge analysis\CONTCAR_whole.vasp"

# 필요한 열만 추출
cols_to_use = ['label in slab', 'bader']
df_au_np = pd.read_excel(file_path, sheet_name='Au_NP', usecols=cols_to_use)

# CONTCAR 읽기
atoms = read(contcar_path)

# label 기준으로 오름차순 정렬
df_sorted = df_au_np.sort_values(by='label in slab')
atom_indices = (df_sorted['label in slab'].astype(int) - 1).tolist()

# plot 그리기
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(atom_indices, df_sorted['bader'], marker='o')
ax.axhline(y=0, color='red', linewidth=1)

# x축 눈금 모두 표시
ax.set_xticks(atom_indices)  # 고정된 눈금
ax.tick_params(axis='x', rotation=45)  # 숫자가 겹치지 않도록 회전 (필요 시)

# 축 라벨 및 제목
ax.set_xlabel('Label in slab (in ase gui)')
ax.set_ylabel('Bader charge')
ax.set_title('Bader charge per label (Au_NP)')
ax.grid(True)

plt.tight_layout()
plt.show()
