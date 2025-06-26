from ase.io.vasp import read_vasp
from ase.io import write
from ase import Atoms
import numpy as np

# POSCAR 읽기
atoms = read_vasp('POSCAR')

# selective_dynamics 플래그 확인
sd_flags = atoms.arrays.get('selective_dynamics', None)

# 원하는 정렬 순서
sort_order = ['Ti', 'O', 'Au', 'C', 'H']

# 원자 인덱스를 정렬 순서대로 정렬
sorted_indices = []
for symbol in sort_order:
    for i, atom in enumerate(atoms):
        if atom.symbol == symbol:
            sorted_indices.append(i)

# 원자 재정렬
sorted_atoms = atoms[sorted_indices]

# selective_dynamics도 정렬해서 재설정
if sd_flags is not None:
    sorted_atoms.set_array('selective_dynamics', sd_flags[sorted_indices])

# POSCAR 저장
write('POSCAR_sorted', sorted_atoms, format='vasp', vasp5=True, direct=False)  # Cartesian 유지
