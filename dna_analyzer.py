
def count_nucleotides(dna_sequence):
    return {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'G': dna_sequence.count('G'),
        'C': dna_sequence.count('C')
    }

def gc_content(dna_sequence):
    g = dna_sequence.count('G')
    c = dna_sequence.count('C')
    return (g + c) / len(dna_sequence) * 100

# Sample usage
if __name__ == "__main__":
    sequence = "ATGCGCATTAAGCG"
    print("Nucleotide Count:", count_nucleotides(sequence))
    print("GC Content: {:.2f}%".format(gc_content(sequence)))
