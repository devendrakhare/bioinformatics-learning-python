# FASTQ File Analyzer

## Overview
This project is a Python-based FASTQ analyzer designed to process and analyze biological sequencing data from FASTQ files. The program reads sequencing reads, 
extracts nucleotide sequences and quality scores, performs sequence-based analysis, 
and generates statistical reports for each read as well as overall dataset summaries.

The analyzer processes FASTQ records in 4-line blocks containing:
1. Read identifier
2. DNA sequence
3. Separator line (`+`)
4. Quality score sequence
The project demonstrates fundamental bioinformatics workflow concepts including biological file parsing, nucleotide composition analysis, sequencing quality assessment, and dataset-level statistical aggregation.

## Features
- FASTQ file parsing
- Multi-read sequence processing
- GC content analysis
- AT content analysis
- Read length calculation
- Sequencing quality score decoding
- Low-quality read detection
- Individual read reporting
- Final dataset statistics generation
- Blank-line handling and preprocessing

## Bioinformatics Concepts Used
- FASTQ file structure
- DNA sequence analysis
- GC percentage calculation
- Phred quality score conversion
- Sequencing read quality assessment
- Biological data preprocessing
- Statistical aggregation
## Programming Concepts Practiced
- Loops and nested loops
- Conditional statements
- String traversal
- Lists
- Data aggregation
- Sequence parsing
- Data cleaning

## Future Improvements
-FASTA file support
-Invalid nucleotide detection
-Reverse complement generation
-Codon translation analysis
-CSV report export
-Quality score visualization
-Multi-file batch processing
-Integration with bioinformatics libraries

## Author
Devendra khare
