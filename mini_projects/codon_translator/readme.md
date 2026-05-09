# Codon Translator

## Overview

This project is a Python-based DNA codon translation tool that simulates a simplified biological translation process. The program reads a DNA sequence, divides it into codons (groups of three nucleotides), and maps each codon to its corresponding amino acid using a dictionary-based codon table.
The project demonstrates how computational logic can be applied to model a fundamental bioinformatics concept: the translation of nucleotide sequences into protein sequences.

## Features
* Accepts user-input DNA sequence
* Converts input to uppercase for standardized processing
* Reads the sequence codon-by-codon
* Uses dictionary mapping for codon translation
* Translates codons into amino acids
* Stops translation at STOP codon
* Handles incomplete codons safely
* Labels unknown codons as `"unknown"`

## Technical Concepts Used
* Functions (`def`)
* Dictionaries (key-value mapping)
* Loops with step size
* String slicing
* Conditional logic
* Lists and `append()`
* `return` for reusable outputs

## Learning Outcomes
This project helped in understanding:
* Codon-based biological translation
* Relationship between sequence indexing and slicing
* Data mapping using dictionaries
* Function-based program structure
* Data flow using `return`

## Future Improvements
* Add complete 64-codon translation table
* Support RNA codons
* Convert amino acids to single-letter notation
* Read sequences from FASTA files
* Build multi-step bioinformatics pipeline

## Author
Devendra Khare
B.Pharm Student | Learning Python & Bioinformatics
