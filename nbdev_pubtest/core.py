# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['linandFile', 'ligandList', 'human_ligandList', 'mouse_ligandList', 'mainSpec_ligandList',
           'input_ligandList', 'aa_length', 'mk_fragments', 'all_aa_fragments', 'unique_aa_fragments']

# Cell
import os
import warnings
import matplotlib.pyplot as plt
from subprocess import call
import subprocess
import glob
import pandas as pd
import tempfile
import numpy as np

# Cell
linandFile="./TEST.csv"
ligandList=pd.read_csv(linandFile, sep=',', header=0)

# Cell
human_ligandList = ligandList.loc[((ligandList['Species'] == 'Human') & (ligandList['Interact human'] == 'Y'))]
mouse_ligandList = ligandList.loc[((ligandList['Species'] == 'Mouse') & (ligandList['Interact mouse'] == 'Y'))]
mainSpec_ligandList = human_ligandList.append(mouse_ligandList)

# Cell
input_ligandList = mainSpec_ligandList
aa_length=9

# Cell
def mk_fragments(aa_seq,aa_length):
    last_aa=len(aa_seq)-aa_length
    aa_seq[last_aa:len(aa_seq)]
    aa_fragments = []

    for start_aa in range(last_aa):
        aa_fragments.append(aa_seq[start_aa:start_aa+aa_length])

    return aa_fragments

# Cell
all_aa_fragments = pd.DataFrame([])
for aa_seq in input_ligandList.Sequence:
    all_aa_fragments = all_aa_fragments.append(mk_fragments(aa_seq,aa_length))

# Cell
unique_aa_fragments=all_aa_fragments.drop_duplicates()