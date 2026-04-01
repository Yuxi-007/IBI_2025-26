import matplotlib.pyplot as plt

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

stop_codon = input('Enter a stop codon (TAA, TAG, TGA): ').upper()
#规定特定输入
if stop_codon not in ['TAA', 'TAG', 'TGA']:
    print('Invalid stop codon')
    quit()

codon_counts = {}
gene_count = 0

#规定一个函数，以后出现这个函数就会这么操作，这里是用来截片段的
def count_codons_in_longest_orf(sequence, chosen_stop, codon_counts):
    longest_orf = ''

    for i in range(len(sequence) - 2):
        start_codon = sequence[i:i+3]

        if start_codon == 'ATG':
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]

                # 如果先遇到的是用户指定的 stop codon
                if codon == chosen_stop:
                    orf = sequence[i:j+3]

                    if len(orf) > len(longest_orf):
                        longest_orf = orf

                    break

                # 如果先遇到的是其他 stop codon，这个 reading frame 就结束
                elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                    break
#统计codon出现种类与次数
    if longest_orf != '':
        # 只统计 stop codon 上游的 codons，不统计最后的 stop codon
        for k in range(0, len(longest_orf) - 3, 3):
            codon = longest_orf[k:k+3]

            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

        return True

    return False


infile = open(input_file, 'r')

header = ''
sequence = ''
#依旧处理上一条gene
for line in infile:
    line = line.rstrip()

    if line.startswith('>'):
        if sequence != '':
            found = count_codons_in_longest_orf(sequence, stop_codon, codon_counts)
            if found:
                gene_count += 1

        header = line
        sequence = ''

    else:
        sequence += line

# 处理最后一条基因
if sequence != '':
    found = count_codons_in_longest_orf(sequence, stop_codon, codon_counts)
    if found:
        gene_count += 1

infile.close()

print('Stop codon:', stop_codon)
print('Number of genes used:', gene_count)
print('Codon counts:')

for codon in sorted(codon_counts):
    print(codon, codon_counts[codon])
#画图
if len(codon_counts) > 0:
    labels = list(codon_counts.keys())
    sizes = list(codon_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Codon usage upstream of ' + stop_codon)
    plt.savefig('codon_usage_' + stop_codon + '.png')
    plt.show()
    plt.close()

    print('Pie chart saved as', 'codon_usage_' + stop_codon + '.png')
else:
    print('No genes found with this stop codon')