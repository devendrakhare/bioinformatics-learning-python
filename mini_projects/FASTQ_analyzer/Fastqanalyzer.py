file = open("sample.fastq", "r")
lines = []

for line in file:

    line = line.strip()

    if line != "":
        lines.append(line)
file.close()

total_reads = 0
total_gc = 0
total_quality = 0
low_quality_reads = 0
read_lengths = []
total_at=0
# PROCESS FASTQ
for i in range(0, len(lines), 4):
    
    header = lines[i]
    sequence = lines[i + 1]
    plus = lines[i + 2]
    quality = lines[i + 3]
    total_reads += 1

    # GC and AT CONTENT
    gc_count = 0
    at_count = 0
    for base in sequence:
        if base == "G" or base == "C":
            gc_count += 1

        elif base == "A" or base == "T":
            at_count += 1
    gc_percent = (gc_count / len(sequence)) * 100
    total_gc += gc_percent
    at_percent = (at_count / len(sequence)) * 100
    total_at += at_percent

    # QUALITY ANALYSIS
    quality_scores = []
    for char in quality:
        score = ord(char) - 33
        quality_scores.append(score)

    avg_quality = sum(quality_scores) / len(quality_scores)
    total_quality += avg_quality

    # LOW QUALITY CHECK
    if avg_quality < 20:
        low_quality_reads += 1

    # READ LENGTH
    read_lengths.append(len(sequence))

    # INDIVIDUAL REPORT
    print(
        "\n---new set---",
        "\nRead ID:", header,
        "\nSequence:", sequence,
        "\nRead Length:", len(sequence),
        "\nGC Content:", round(gc_percent, 2), "%",
        "\nAT Content:", round(at_percent, 2), "%",
        "\nAverage Quality:", round(avg_quality, 2),
        )

# FINAL STATISTICS
overall_gc = total_gc / total_reads
overall_at = total_at / total_reads
overall_quality = total_quality / total_reads
shortest_read = min(read_lengths)
longest_read = max(read_lengths)
average_length = sum(read_lengths) / len(read_lengths)

print(
    "\nFINAL REPORT",
    "\nTotal Reads:", total_reads,
    "\nAverage GC Content:", round(overall_gc, 2), "%",
    "\nAverage AT Content:", round(overall_at, 2), "%",
    "\nAverage Quality:", round(overall_quality, 2),
    "\nShortest Read:", shortest_read,
    "\nLongest Read:", longest_read,
    "\nAverage Read Length:", round(average_length, 2),
    "\nLow Quality Reads:", low_quality_reads
)
