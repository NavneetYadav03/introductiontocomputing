"""
5.
Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon, and oxygen atoms in the molecule.
The program should prompt the user to enter the number of hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms.
The program then prints the total combined molecular weight of all the atoms based on these individual atom weights:
Atom Weight(grams / mole)
H  1.00794
C  12.0107
O  15.9994
For example, the molecular weight of water (H20) is: 2(1.00794) + 15.9994 = 18.01528.
"""
a=int(input("number of H: "))
b=int(input("number of C: "))
c=int(input("number of O: "))
print("molecular weight of compound",((a*1.00794)+(b*12.0107)+(c*15.9994)))
