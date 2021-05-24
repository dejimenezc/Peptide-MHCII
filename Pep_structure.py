# -*- coding: utf-8 -*-
"""
Input : CSV with a list of peptides
Output : Scripts of tleap.
El programa recibe un archivo .csv con una lista de peptidos y devuelve un archivo 
.tleap con los comandos para contruir un archivo .pdb para cada uno de los péptidos
"""

aminoacids = {"D":"ASP", "E":"GLU", "R":"ARG", "K":"LYS", "N":"ASN", "H":"HIS", 
              "Q":"GLN", "S":"SER", "T":"THR", "A":"ALA", "G":"GLY", "V":"VAL", 
              "P":"PRO", "L":"LEU", "F":"PHE", "Y":"TYR", "I":"ILE", "M":"MET", 
              "W":"TRP", "C":"CYS" }

Pep_selection = open("prueba.csv", "r", encoding='utf-8-sig')
peptides = Pep_selection.readlines()
list_peptides = []
for peptide in peptides:
    list_peptides.append(peptide.strip())

Pep_selection.close()

Pep_structure = open("pep_pdb.tleap", "w")
Pep_structure.write("source leaprc.protein.ff14SB" + "\n" + "source leaprc.gaff" + 
                    "\n" + "source leaprc.water.tip3p" + "\n")

conditional_1= []
for peptide in list_peptides:
    conditional_1.append(peptide)
    aas = list(peptide)
    Pep_structure.write("\n" + "prot = sequence { " )
    conditional_2 = []
    for aa in aas:
        conditional_2.append(aa)
        Pep_structure.write(aminoacids[aa] + " ") 
        if len(aas) == len(conditional_2):
            Pep_structure.write("NME }" + "\n" + "savepdb prot sequence_" + 
                                str(list_peptides.index(peptide)+1) + ".pdb" + 
                                "\n")
    if len(list_peptides) == len(conditional_1):
        Pep_structure.write("\n" + "quit")
                     
Pep_structure.close()
