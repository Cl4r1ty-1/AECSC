codon_dict = {
    "TTT": "Phenylalanine",
    "TTC": "Phenylalanine",
    "TTA": "Leucine",
    "TTG": "Leucine",
    "TCT": "Serine",
    "TCC": "Serine",
    "TCA": "Serine",
    "TCG": "Serine",
    "TAT": "Tyrosine",
    "TAC": "Tyrosine",
    "TGT": "Cysteine",
    "TGC": "Cysteine",
    "TGG": "Tryptophan",
    "CTT": "Leucine",
    "CTC": "Leucine",
    "CTA": "Leucine",
    "CTG": "Leucine",
    "CCT": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "CAT": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "CGT": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "ATT": "Isoleucine",
    "ATC": "Isoleucine",
    "ATA": "Isoleucine",
    "ATG": "Methionine",
    "ACT": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "AAT": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "AGT": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",
    "GTT": "Valine",
    "GTC": "Valine",
    "GTA": "Valine",
    "GTG": "Valine",
    "GCT": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "GAT": "Aspartate",
    "GAC": "Aspartate",
    "GAA": "Glutamate",
    "GAG": "Glutamate",
    "GGT": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"
}

try:
    file_name = input("Please specify the DNA Data File name: ").strip()
    amino_acid = input("Enter name of amino acid to count: ").strip()
    
    with open(file_name, 'r') as file:
        n = 3
        count = 0
        sequences = file.readlines()
        for sequence in sequences:
            string = sequence.strip()
            dna = [(string[i:i+n]) for i in range(0, len(string), n)]
            for acid in dna:
                if codon_dict[acid] == amino_acid:
                    count =+ 1
        
except FileNotFoundError:
    print("The file doesn't exist!")
else:
    print(f'There are {count} of the {amino_acid} acid in this sequence.')