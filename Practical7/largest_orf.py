seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG' 
#建一个空字符，如果没找到也不会报错
longest_orf = ''
#三个一循环，一个个找
for i in range(len(seq)-2):
    cod=seq[i:i+3]
    #找到AUG，以后就是3个3个加
    if cod=="AUG":
        #起始，结束，步长
        for j in range(i+3,len(seq)-2,3):
            stop=seq[j:j+3]
#如果是这些，则决定了长度，一个就break即可
            if stop== 'UAA' or stop== 'UAG' or stop== 'UGA':
                orf=seq[i:j+3]
                if len(orf) > len(longest_orf):
                    longest_orf = orf
                break
if longest_orf != '':
    print('Longest ORF:', longest_orf)
    print('Length:', len(longest_orf))
else:
    print('No ORF found')


