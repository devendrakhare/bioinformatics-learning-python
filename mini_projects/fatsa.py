def read_fasta(filename):
    #fasta reader
    file = open(filename , "r")
    fatsa_data={}
    current_header=""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_header=line[1:]
            fatsa_data[current_header]=""
        else:
            fatsa_data[current_header]+=line.upper()
    file.close()     
    return fatsa_data
#main
filename=input("enter file name:")
result=read_fasta(filename)
#analyzer
for header in result:
    A, T,G,C=[],[],[],[]
    seq=result[header]
    for i in range(len(seq)):
        if seq[i] =="A":
            A.append(i+1)
        elif seq[i] =="T":
            T.append(i+1)
        elif seq[i] =="G":
            G.append(i+1)
        elif seq[i] =="C":
            C.append(i+1)
#result printed
    print("header",header,"sequence", result[header],
            "\nA base position", A,"length",len(A),
            "\nT base position", T,"length",len(T),
            "\nG base position", G,"length",len(G),
            "\nC base position", C,"length",len(C)
        )