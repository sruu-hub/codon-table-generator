# Python Project: Development of a Codon Table Generator

## Overview
This repository contains a Python program that generates the standard 64-codon genetic code table and translates user-provided DNA or RNA sequences into their corresponding amino acid chains.

## Features Implemented
1. **64-Codon Dictionary:** Maps all 64 standard genetic triplets (`A`, `T`, `G`, `C`) to their full amino acid names.
2. **Input Validation:** Verifies that input sequences contain only valid DNA (`A, T, G, C`) or RNA (`A, U, G, C`) nucleotides and prevents mixing `T` and `U`.
3. **RNA Translation Support (Additional Challenge):** Automatically detects RNA sequences containing Uracil (`U`) and translates them accurately.
4. **Triplet Splitting & Incomplete Codon Handling:** Divides sequences into groups of 3 nucleotides and safely ignores trailing 1- or 2-base overhangs with a user notification.
5. **Start and Stop Codon Identification:** Highlights translation initiation (`ATG`/`AUG`) and termination (`TAA`, `TAG`, `TGA` / `UAA`, `UAG`, `UGA`) codons.
6. **Formatted Table Output:** Displays both the complete 64-codon reference table and a step-by-step translation table.

## How to Run the Program
1. Clone this repository:
   ```bash
   git clone https://github.com/sruu-hub/codon-table-generator.git
   cd codon-table-generator
   ```
2. Run the Python script:
   ```bash
   python codon_translator.py
   ```

## Sample Input and Output
**Sample Input:**
```text
ATGGCTTTTTAA
```

**Expected Output:**
```text
----------------------------------------------------
Pos    | Codon    | Amino Acid           | Role      
----------------------------------------------------
1      | ATG      | Methionine           | Start     
2      | GCT      | Alanine              | Coding    
3      | TTT      | Phenylalanine        | Coding    
4      | TAA      | Stop                 | Stop      
----------------------------------------------------

Expected Output Summary:
Codons: ATG-GCT-TTT-TAA
Amino acids: Methionine - Alanine - Phenylalanine - Stop
Start codon: ATG
Stop codon: TAA
```

## Comparison with Custom Codon Tables on GitHub (Requirement 9)
When comparing our dictionary implementation (`CODON_TABLE`) with popular open-source bioinformatics repositories on GitHub (such as **Biopython's `Bio.Data.CodonTable`** and standard command-line sequence translators), key structural differences include:

| Feature | Our Implementation (`codon_translator.py`) | Online GitHub Repositories (e.g., Biopython) |
| :--- | :--- | :--- |
| **Amino Acid Representation** | Uses full amino acid names (`'Methionine'`, `'Alanine'`) for educational clarity and readability. | Typically uses 1-letter IUPAC codes (`'M'`, `'A'`, `'*'` for Stop) or 3-letter abbreviations (`'Met'`, `'Ala'`). |
| **Stop Codon Handling** | Explicitly maps `'TAA'`, `'TAG'`, and `'TGA'` to `'Stop'` inside the main dictionary. | Often stores stop codons in a separate list (`stop_codons = ['TAA', 'TAG', 'TGA']`) or maps them to `'*'`. |
| **Alternative Genetic Codes** | Focuses on the Standard Genetic Code. | Includes modular dictionaries for mitochondrial, plastid, and alternative nuclear genetic codes. |
| **RNA Handling** | Normalizes RNA (`U` -> `T`) prior to dictionary lookup to avoid duplicating 64 keys. | Generates separate DNA and RNA dictionary instances dynamically from a base table class. |