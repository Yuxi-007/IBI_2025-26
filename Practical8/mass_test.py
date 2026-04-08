def mass_test (sequence):
    "Takes an amino acid sequence and returns the total protein mass in amu. Raises a ValueError if an unknown amino acid is found."
    amino_acid_masses = {
        "A": 89.09,   # Alanine
        "R": 174.20,  # Arginine
        "N": 132.12,  # Asparagine
        "D": 133.10,  # Aspartic acid
        "C": 121.15,  # Cysteine
        "E": 147.13,  # Glutamic acid
        "Q": 146.15,  # Glutamine
        "G": 75.07,   # Glycine
        "H": 155.16,  # Histidine
        "I": 131.17,  # Isoleucine
        "L": 131.17,  # Leucine
        "K": 146.19,  # Lysine
        "M": 149.21,  # Methionine
        "F": 165.19,  # Phenylalanine
        "P": 115.13,  # Proline
        "S": 105.09,  # Serine
        "T": 119.12,  # Threonine
        "W": 204.23,  # Tryptophan
        "Y": 181.19,  # Tyrosine
        "V": 117.15   # Valine
    }
    sequence = sequence.upper()
    total_mass = 0
    for amino in sequence:
        if amino not in amino_acid_masses:
            return f"Error: '{amino}' has no recorded mass."
        else:
            total_mass +=amino_acid_masses[amino]
    return total_mass

protein_sequence = "ACDE"
try:
    mass = mass_test(protein_sequence)
    print(f"Protein sequence: {protein_sequence}")
    print(f"Total protein mass: {mass} amu")
except ValueError as error:
    print(error)
 
