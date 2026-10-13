
def validate_dna(sequence):
    """Check whether a DNA sequence contains only A, T, G, and C."""
    sequence = sequence.strip().upper()

    if not sequence:
        return False

    for nucleotide in sequence:
        if nucleotide not in "ATGC":
            return False

    return True


def count_nucleotides(sequence):
    """Count each nucleotide in a DNA sequence."""
    sequence = sequence.strip().upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
    }


def generate_complement(sequence):
    """Generate the complementary DNA strand."""
    sequence = sequence.strip().upper()

    pairing = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }

    return "".join(pairing[nucleotide] for nucleotide in sequence)


def main():
    """Run the DNA analyzer."""
    dna = input("Enter a DNA sequence: ").strip().upper()

    if not validate_dna(dna):
        print("Invalid DNA sequence!")
        return

    print("Valid DNA sequence!")
    print("Nucleotide counts:", count_nucleotides(dna))
    print("Complementary strand:", generate_complement(dna))


if __name__ == "__main__":
    main()
