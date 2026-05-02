# DNA Sequence Analyzer
dna = input("Enter DNA sequence: ").upper()
# Lists to store positions
a_pos = []
t_pos = []
g_pos = []
c_pos = []
# Check and analyze DNA
    for i in range(len(dna)):
        if dna[i] == "A":
             a_pos.append(i + 1)
        elif dna[i] == "T":
                    t_pos.append(i + 1)
        elif dna[i] == "G":
                    g_pos.append(i + 1)
        elif dna[i] == "C":
                    c_pos.append(i + 1)
        else:
print("Invalid base found at position", i + 1)

 # Print results
print("\n--- DNA Analysis ---")
print("Length:", len(dna))

print("A → count:", len(a_pos), "positions:", a_pos)
print("T → count:", len(t_pos), "positions:", t_pos)
print("G → count:", len(g_pos), "positions:", g_pos)
print("C → count:", len(c_pos), "positions:", c_pos)

 #each base content
print("A %:", (len(a_pos)/len(dna)) * 100)
print("T %:", (len(t_pos)/len(dna)) * 100)
print("G %:", (len(g_pos)/len(dna)) * 100)
print("C %:", (len(c_pos)/len(dna)) * 100)
