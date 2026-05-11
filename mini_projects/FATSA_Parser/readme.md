# Multi-FASTA Sequence Parser & Analyzer
## Overview
This project is a Python-based multi-FASTA parser designed to read and organize biological sequence data from FASTA files. The program identifies FASTA headers, associates them with their corresponding DNA sequences, and stores the data using a dictionary-based structure for efficient retrieval and analysis.
The project demonstrates core bioinformatics concepts such as biological file parsing, sequence-data mapping, and structured storage of genomic information.

## Features
Reads multi-FASTA files
Detects and extracts FASTA headers
Associates sequences with their respective headers
Stores biological records using dictionaries
Supports multi-line DNA sequences
Converts sequences to uppercase for standardization
Calculates sequence length for each entry
Handles multiple sequence records dynamically

## Technical Concepts Used
File handling (open, read)
FASTA parsing
Dictionaries (key-value mapping)
Loops and iteration
Conditional statements
String manipulation
Dynamic data accumulation
Functions and return

## Data Structure Used
The parsed FASTA records are stored in the following format:
{    "Gene1": "ATGCTTAA",    "Gene2": "GGCCAATT"}
Where:
Dictionary key → FASTA header / sequence identifier
Dictionary value → corresponding biological sequence

## Learning Outcomes
This project helped in understanding:
Biological sequence file formats
Relationship between metadata and sequence data
Parsing structured biological datasets
Dictionary-based storage systems
Sequence accumulation across multiple lines
Data organization and retrieval logic

## Future Improvements
Add GC-content calculation
Add nucleotide frequency analysis
Detect invalid DNA bases
Export parsed data to CSV
Integrate Biopython FASTA utilities
Support FASTQ parsing

## Author
Devendra Khare
B.Pharm Student | Learning Python & Bioinformatics
