def read_fasta(filename):

    file = open(filename, "r")

    fasta_data = {}

    current_header = ""

    # Read FASTA file
    for line in file:

        line = line.strip()

        # Header line
        if line.startswith(">"):

            current_header = line[1:]

            fasta_data[current_header] = ""

        # Sequence line
        else:

            fasta_data[current_header] += line.upper()

    file.close()

    return fasta_data
# main
filename = input("Enter FASTA filename: ")
result = read_fasta(filename)
# Print results
for header in result:
    print("\nHeader:", header)
    print("Sequence:", result[header])
    print("Length:", len(result[header]))
