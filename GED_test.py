import unittest
from GED import *


class MyTestCase(unittest.TestCase):

    def run_tests(self, d):
        for n, p in d.items():
            with self.subTest(p=p):
                GED = calc_GED(p[0], p[1])
                self.assertEqual(GED,p[2], msg='GED not correct for ' + n)


    def test_aromatic_aromatic(self):
        mol_dict = {
            'benzene->pyridine': ('c1ccccc1', 'n1ccccc1',1),
            'pyridine->pyridazine': ('n1ccccc1', 'n1ncccc1',1),
            'benzene->pyridazine': ('c1ccccc1', 'n1ncccc1', 2)
        }
        self.run_tests(mol_dict)

    def test_aromatic_substituents(self):
        mol_dict = {
            'benzene->toluene': ('c1ccccc1', 'c1ccccc1C',2),
            'benzene->chlorobenzene': ('c1ccccc1', 'c1ccccc1Cl', 2),
            'benzene->anisole':('c1ccccc1', 'c1ccccc1OC', 3)
        }
        self.run_tests(mol_dict)

    def test_aliphatic_aromatic(self):
        mol_dict = {
            'benzene->cyclohexane': ('c1ccccc1', 'C1CCCCC1',6)
        }
        self.run_tests(mol_dict)

    def test_aliphatic_ring_expansion(self):
        mol_dict = {
            'cyclopropane->cyclobutane': ('C1CC1', 'C1CCC1',4)
        }
        self.run_tests(mol_dict)

    def test_aliphatic_aliphatic(self):
        mol_dict = {
            'ethane->propane': ('CC', 'CCC',2)
        }
        self.run_tests(mol_dict)



if __name__ == '__main__':
    unittest.main()
