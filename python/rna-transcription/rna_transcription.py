complements = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U' }
def to_rna(strand):
    return ''.join([complements[base] for base in strand])

