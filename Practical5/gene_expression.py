import matplotlib.pyplot as plt
#Create the dictionary
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print(gene_expression)
#add MYC
gene_expression["MYC"]=11.6
#Create bar chart
genes = gene_expression.keys()
values = gene_expression.values()
plt.bar(genes, values)
plt.xlabel("Gene")
plt.ylabel("Expression level")
plt.title("Gene Expression Levels")
plt.show()
#Check exist or not
gene_interest="MYC"
if gene_interest in gene_expression:
    print("Expresion value :",gene_expression[gene_interest])
else:
    print("Error: the gene is not found")
#Calculate average
average = sum(gene_expression.values()) / len(gene_expression)
print("Average gene expression:", average)