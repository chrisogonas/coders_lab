"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: “ACGAATTCCG”.
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example, given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", the output will be ["AAAAACCCCC", "CCCCCAAAAA"].

Given s = "TGTTCCAGGCCTAGTTCCAGGCCTTTCCAG", what would be our output?

Pseudocode
1. create a hashtable/dict
2. Traverse the DNA string from left to right stepping forward 1 letter at a time (per loop)
3. At each step, extract 10 letter substring
4. If substring exists in the hashtable, increment its value by 1, else insert it with a default value of 1
5. When above loop ends, traverse the hashtable, and return an array of keys whose values are greater than 1
"""


# Implementation
def get_multiple_dna_sequences(dna, seq_length=10):
    my_dna = {}
    # special cases
    if len(dna) <= seq_length:
        return []

    for i in range(len(dna)):
        new_dna = dna[i:]
        if len(new_dna) < seq_length:
            break
        else:
            if new_dna[0:10] in my_dna:
                my_dna[new_dna[0:10]] += 1
            else:
                my_dna[new_dna[0:10]] = 1

    # get and return the list of sequences that are repeated
    return [s for s in my_dna.keys() if my_dna[s] > 1]


print(get_multiple_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', 10))
print(get_multiple_dna_sequences('TGTTCCAGGCCTAGTTCCAGGCCTTTCCAG', 10))