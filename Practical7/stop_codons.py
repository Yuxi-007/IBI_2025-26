#Open and create the file
import re

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'
#Create blank character, make it easier to add things in it
header = ''
sequence = ''
#Find the gene name
def get_gene_name(header):
    m = re.search(r'gene:([^\s]+)', header)
    if m:
        return m.group(1)
    else:
        return 'unknown_gene'

infile = open(input_file, 'r')
outfile = open(output_file, 'w')

for line in infile:
    line = line.rstrip()

    if line.startswith('>'):
        #Store the gene before a new start
        if sequence != '':
            stop_list = re.findall(r'(?=(?:ATG(?:[ATCG]{3})*?(TAA|TAG|TGA)))', sequence)
            stop_list = sorted(list(set(stop_list)))

            if stop_list:
                gene_name = get_gene_name(header)
                stop_text = ','.join(stop_list)
                outfile.write('>' + gene_name + ' ' + stop_text + '\n')
                outfile.write(sequence + '\n')

        header = line
        sequence = ''
#Set all the sequence as a whole thing
    else:
        sequence += line
#Deal with the last gene
if sequence != '':
    stop_list = re.findall(r'(?=(?:ATG(?:[ATCG]{3})*?(TAA|TAG|TGA)))', sequence)
    stop_list = sorted(list(set(stop_list)))

    if stop_list:
        gene_name = get_gene_name(header)
        stop_text = ','.join(stop_list)
        outfile.write('>' + gene_name + ' ' + stop_text + '\n')
        outfile.write(sequence + '\n')

infile.close()
outfile.close()
        
            
