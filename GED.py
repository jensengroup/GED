'''
Written by Jan H. Jensen, 2020
'''

"calculation of graph edit distance"

from rdkit import Chem
import networkx as nx

def get_graph(mol):
  Chem.Kekulize(mol)
  atoms = [atom.GetAtomicNum() for atom in mol.GetAtoms()]
  am = Chem.GetAdjacencyMatrix(mol,useBO=True)
  for i,atom in enumerate(atoms):
    am[i,i] = atom
  G = nx.from_numpy_matrix(am)
  return G

def calc_GED(s1,s2):
  mol1 = Chem.MolFromSmiles(s1)
  mol2 = Chem.MolFromSmiles(s2)
  G1 = get_graph(mol1)
  G2 = get_graph(mol2)
  GDE = nx.graph_edit_distance(G1, G2, edge_match=lambda a, b: a['weight'] == b['weight'])
  return int(GDE)





