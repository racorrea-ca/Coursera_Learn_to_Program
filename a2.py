def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return (len(dna1) > len(dna2))

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)
    

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1


def is_valid_sequence(dna_seq):
    """ is_valid_sequence(str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than \verb|'A'|’A’, \verb|'T'|’T’, \verb|'C'|’C’ and \verb|'G'|’G’). 
    A string is not a valid DNA sequence if it contains lowercase letters.
    
    >>> is_valid_sequence("ATCG")
    True
    >>> is_valid_sequence("ATCg")
    False
    >>> is_valid_sequence("atcg")
    False
    >>> is_valid_sequence("ATCF")
    False
    >>> is_valid_sequence("ATCf")
    False
    """

    IsValid = True
    
    for char in dna_seq:
        if char not in 'ATGC':
            IsValid = False

    return IsValid


def insert_sequence (dna_seq1, dna_seq2, ndx):
    """insert_sequence (str, str, int) -> str
 
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. 
    Assume that the index is valid
    
    >>> insert_sequence ('CCGG', 'AT', 2)
​    'CCATGG'
    >>> insert_sequence ('AATT', 'CG', 4)
​    'AATTCG'
    >>> insert_sequence ('TTCC', 'AA', 0)
​    'AATTCC'
    """ 

    return dna_seq1[:ndx] + dna_seq2 + dna_seq1[ndx:]



def get_complement(nucleotide):
    """get_complement(str) -> str

    Return the nucleotide's complement.
    A and T can be bonded together, and thus complement each other;
    similarly, C and G are complements of each other.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

    if nucleotide == 'A':
        nucleotide_compl = 'T'

    if nucleotide == 'T':
        nucleotide_compl = 'A'

    if nucleotide == 'C':
        nucleotide_compl = 'G'

    if nucleotide == 'G':
        nucleotide_compl = 'C'

    return nucleotide_compl


def get_complementary_sequence(dna_seq):
    """get_complementary_sequence(str) -> str
​	
    Return the DNA sequence that is complementary to the given DNA sequence.
 
    >>> get_complementary_sequence('ATCGGACT')
    TAGCCTGA
    >>> get_complementary_sequence('GCACTCC')
    CGTGAGG
    >>> get_complementary_sequence('ATCGATCG')
    TAGCTAGC
    """

    compl_seq = ''
    
    for char in dna_seq:
        compl_seq = compl_seq + get_complement(char)

    return compl_seq

