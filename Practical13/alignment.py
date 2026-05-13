# Read a FASTA file and return the sequence name and protein sequence
def read_fasta(filename):
    name = ""
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                name = line[1:]
            else:
                sequence += line

    return name, sequence

# Read the BLOSUM62 matrix and store the scores in a dictionary
def read_blosum62(filename):
    blosum = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    # Use the first line as the column amino acid names
    amino_acids = lines[0].split()

    # Read each remaining row of the matrix
    for line in lines[1:]:
        parts = line.split()

        if len(parts) == 0:
            continue

        row_aa = parts[0]
        scores = parts[1:]

        blosum[row_aa] = {}

        # Match each score to the correct row and column amino acid
        for i in range(len(amino_acids)):
            col_aa = amino_acids[i]
            blosum[row_aa][col_aa] = int(scores[i])

    return blosum

# Compare two sequences position by position
def compare_sequences(name1, seq1, name2, seq2, blosum):
    if len(seq1) != len(seq2):
        print("Error: sequences are not the same length.")
        print(name1, "length:", len(seq1))
        print(name2, "length:", len(seq2))
        return

    total_score = 0
    identical_count = 0

    # For each amino acid position, compare the two residues
    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]

        # Count identical amino acids
        if aa1 == aa2:
            identical_count += 1

        # Look up the BLOSUM62 score for this amino acid pair
        score = blosum[aa1][aa2]

        # Add the score to the total alignment score
        total_score += score

    # Calculate percentage identity and normalised score
    percentage_identity = identical_count / len(seq1) * 100
    score_per_amino_acid = total_score / len(seq1)

    # Print the alignment results
    print("=" * 60)
    print("Comparison:")
    print(name1)
    print("vs")
    print(name2)
    print()
    print("BLOSUM62 total score:", total_score)
    print("BLOSUM62 score per amino acid:", round(score_per_amino_acid, 2))
    print("Identical amino acids:", identical_count)
    print("Percentage identity:", round(percentage_identity, 2), "%")


# Read the BLOSUM62 scoring matrix
blosum62 = read_blosum62("BLOSUM62.txt")


# Read the three protein sequences from FASTA files
human_name, human_seq = read_fasta("human_DLX5.fasta.txt")
mouse_name, mouse_seq = read_fasta("mouse_DLX5.fasta.txt")
random_name, random_seq = read_fasta("random.fasta.txt")


# Compare human DLX5 with mouse DLX5
compare_sequences(human_name, human_seq, mouse_name, mouse_seq, blosum62)


# Compare human DLX5 with the random protein sequence
compare_sequences(human_name, human_seq, random_name, random_seq, blosum62)


# Compare mouse DLX5 with the random protein sequence
compare_sequences(mouse_name, mouse_seq, random_name, random_seq, blosum62)