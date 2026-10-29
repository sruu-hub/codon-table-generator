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

def get_valid_sequence():
    """Prompts user for a DNA or RNA sequence and validates its characters."""
    raw_seq = input("Enter a DNA or RNA sequence (e.g., ATGGCTTTTTAA): ").strip().upper()
    if not raw_seq:
        print("Error: Input sequence cannot be empty.")
        return None

    valid_bases = {'A', 'T', 'G', 'C', 'U'}
    invalid_bases = set(raw_seq) - valid_bases
    if invalid_bases:
        print(f"Error: Invalid nucleotide(s) detected: {', '.join(sorted(invalid_bases))}.")
        print("Please enter only valid DNA (A, T, G, C) or RNA (A, U, G, C) nucleotides.")
        return None

    if 'T' in raw_seq and 'U' in raw_seq:
        print("Error: Sequence cannot mix DNA (T) and RNA (U) nucleotides simultaneously.")
        return None

    return raw_seq

def split_into_codons(sequence):
    """Splits a nucleotide sequence into triplets and handles trailing incomplete bases."""
    remainder = len(sequence) % 3
    incomplete = ""
    if remainder != 0:
        incomplete = sequence[-remainder:]
        sequence = sequence[:-remainder]

    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    return codons, incomplete

def translate_codons(codons):
    """Translates a list of DNA or RNA codons into their corresponding amino acids."""
    amino_acids = []
    for codon in codons:
        lookup_codon = codon.replace('U', 'T')
        amino_acids.append(CODON_TABLE.get(lookup_codon, "Unknown"))
    return amino_acids

def identify_start_stop_codons(codons):
    """Identifies start and stop codons present in the sequence."""
    start_set = {'ATG', 'AUG'}
    stop_set = {'TAA', 'TAG', 'TGA', 'UAA', 'UAG', 'UGA'}

    starts = [c for c in codons if c in start_set]
    stops = [c for c in codons if c in stop_set]
    return starts, stops

def display_translation_results(codons, amino_acids, starts, stops, incomplete):
    """Displays the translated output in both a structured table and summary format."""
    if not codons:
        print("No complete codons (3 nucleotides) available to translate.")
        return

    print("\n" + "-" * 52)
    print(f"{'Pos':<6} | {'Codon':<8} | {'Amino Acid':<20} | {'Role':<10}")
    print("-" * 52)
    for idx, (codon, aa) in enumerate(zip(codons, amino_acids), start=1):
        role = "Start" if codon in {'ATG', 'AUG'} else ("Stop" if aa == "Stop" else "Coding")
        print(f"{idx:<6} | {codon:<8} | {aa:<20} | {role:<10}")
    print("-" * 52)

    if incomplete:
        print(f"Incomplete trailing bases ignored: {incomplete}")

    print("\nExpected Output Summary:")
    print(f"Codons: {'-'.join(codons)}")
    print(f"Amino acids: {' - '.join(amino_acids)}")
    print(f"Start codon: {', '.join(starts) if starts else 'None'}")
    print(f"Stop codon: {', '.join(stops) if stops else 'None'}")

if __name__ == "__main__":
    display_codon_table()
    seq = get_valid_sequence()
    if seq:
        codons, incomplete = split_into_codons(seq)
        amino_acids = translate_codons(codons)
        starts, stops = identify_start_stop_codons(codons)
        display_translation_results(codons, amino_acids, starts, stops, incomplete)