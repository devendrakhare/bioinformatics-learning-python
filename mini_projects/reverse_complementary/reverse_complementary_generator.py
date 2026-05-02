def reverse_complement(dna):
    dna = dna.upper()

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    result = ""

    for base in reversed(dna):
        if base in complement:
            result += complement[base]
        else:
            print("Invalid base found:", base)
            return

    print("Reverse Complement:", result)
# main
dna_input = input("Enter DNA sequence: ")
reverse_complement(dna_input)
