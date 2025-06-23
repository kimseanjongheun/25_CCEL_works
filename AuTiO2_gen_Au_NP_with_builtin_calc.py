from ase.cluster import Octahedron, Icosahedron, Decahedron
from ase.build import bulk
from ase.visualize import view
from ase.atoms import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import read, write
import numpy as np


filepath = "Au_NP/"


# 무작위 원자 배치
element = 'Au'
cell_size = 20
atom_num = 8
iteration_number = 1
for i in range(iteration_number):
    positions = np.random.rand(atom_num, 3) * 8  # 10 Å 범위 안에 무작위 배치
    cluster = Atoms(f'{element}{atom_num}', positions=positions, cell=[cell_size, cell_size, cell_size])
    cluster.center()
    cluster.calc = EMT()
    view(cluster)
    optimizer = BFGS(cluster)
    optimizer.run(fmax=0.01)
    view(cluster)

write(filepath+element+'_'+'manually'+'.vasp', cluster, format='vasp')


'''
#환경 설정
element = 'Au'
num = 6

NP = Atoms(f'Au{num}',
           positions=[(0,0,0),
                      (0,0,2.5),
                      (0, 2, 1.25),
                      (0, -2, 1.25),
                      (2, 0, 1.25),
                      (-2, 0, 1.25),
                      ],
           cell=[20, 20, 20])
NP.center()
view(NP)
write(filepath+element+str(num)+'.vasp', NP, format='vasp')
'''

'''
element = 'Au'
layers = 3
cut_off = 1
size = 10
structure = 'fcc'
num = 13

#nano_particle = Octahedron(element, layers, cut_off)
#nano_particle = Icosahedron(element, 2)
#nano_particle = Decahedron(element, p=2, q=2, r=0)
nano_particle.set_cell([20, 20, 20])
nano_particle.center()
print(nano_particle.get_number_of_atoms)
view(nano_particle)
'''
