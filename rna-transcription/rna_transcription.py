def to_rna(dna_strand: str) -> str:
    return dna_strand.translate(str.maketrans({
        "C": "G", "G": "C", "A": "U", "T": "A"
    }))
