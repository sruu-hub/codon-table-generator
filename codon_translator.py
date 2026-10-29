# codon_translator.py

CODON_TABLE = {
    # T (U in RNA) - First Base
    'TTT': 'Phenylalanine', 'TTC': 'Phenylalanine', 'TTA': 'Leucine',       'TTG': 'Leucine',
    'TCT': 'Serine',        'TCC': 'Serine',        'TCA': 'Serine',        'TCG': 'Serine',
    'TAT': 'Tyrosine',      'TAC': 'Tyrosine',      'TAA': 'Stop',          'TAG': 'Stop',
    'TGT': 'Cysteine',      'TGC': 'Cysteine',      'TGA': 'Stop',          'TGG': 'Tryptophan',
    
    # C - First Base
    'CTT': 'Leucine',       'CTC': 'Leucine',       'CTA': 'Leucine',       'CTG': 'Leucine',
    'CCT': 'Proline',       'CCC': 'Proline',       'CCA': 'Proline',       'CCG': 'Proline',
    'CAT': 'Histidine',     'CAC': 'Histidine',     'CAA': 'Glutamine',     'CAG': 'Glutamine',
    'CGT': 'Arginine',      'CGC': 'Arginine',      'CGA': 'Arginine',      'CGG': 'Arginine',
    
    # A - First Base
    'ATT': 'Isoleucine',    'ATC': 'Isoleucine',    'ATA': 'Isoleucine',    'ATG': 'Methionine',
    'ACT': 'Threonine',     'ACC': 'Threonine',     'ACA': 'Threonine',     'ACG': 'Threonine',
    'AAT': 'Asparagine',    'AAC': 'Asparagine',    'AAA': 'Lysine',        'AAG': 'Lysine',
    'AGT': 'Serine',        'AGC': 'Serine',        'AGA': 'Arginine',      'AGG': 'Arginine',
    
    # G - First Base
    'GTT': 'Valine',        'GTC': 'Valine',        'GTA': 'Valine',        'GTG': 'Valine',
    'GCT': 'Alanine',       'GCC': 'Alanine',       'GCA': 'Alanine',       'GCG': 'Alanine',
    'GAT': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    'GGT': 'Glycine',       'GGC': 'Glycine',       'GGA': 'Glycine',       'GGG': 'Glycine'
}

def display_codon_table():
    """Displays all 64 codons and their corresponding amino acids in a 4-column table."""
    print("\n" + "=" * 78)
    print(f"{'STANDARD GENETIC CODE TABLE (64 CODONS)':^78}")
    print("=" * 78)
    items = list(CODON_TABLE.items())
    for i in range(0, len(items), 4):
        row = items[i:i+4]
        print(" | ".join([f"{codon}: {aa:<14}" for codon, aa in row]))
    print("=" * 78 + "\n")


if __name__ == "__main__":
    display_codon_table()

def get_valid_sequence():
    """Prompts user for a DNA sequence and validates that only A, T, G, C are present."""
    raw_seq = input("Enter a DNA sequence: ").strip().upper()
    if not raw_seq:
        print("Error: Input sequence cannot be empty.")
        return None

    valid_bases = {'A', 'T', 'G', 'C'}
    invalid_bases = set(raw_seq) - valid_bases
    if invalid_bases:
        print(f"Error: Invalid nucleotide(s) detected: {', '.join(sorted(invalid_bases))}. Only A, T, G, C are allowed.")
        return None

    return raw_seq


if __name__ == "__main__":
    display_codon_table()
    seq = get_valid_sequence()
    if seq:
        print(f"Validated DNA sequence: {seq}")