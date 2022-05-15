""""
2.Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate
"""

GI=int(input("Enter Gross Income ",)) #GI is Gross Income
DP=int(input("Enter No. of Dependents ",))#DP is No. of Dependents
standard_deduction=10000
tax_rate=20#in percentage
TI=GI-standard_deduction-(DP*3000)#TI is Taxable Income
T=TI*(tax_rate)/100#T is Tax to be paid
print("Tax to be paid ",T)
