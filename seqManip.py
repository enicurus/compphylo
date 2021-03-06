# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 11:26:29 2015
@author: ryanterrill github.com/enicurus
First assignment for Computational Phylogenetics
"""

# DNA sequence copied from from https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)###

seq="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"

print(seq)

# Print the length of the DNA sequence seq with an explanation #


lengthExplanation = "The DNA sequence contains "+str(len(seq))+" base pairs"
print(lengthExplanation)

# create RNA equivalent to seq by replacing lower case DNA codon with uper case RNA iteratively#

RNAseqCtoG = seq.replace("c","G")
RNAseqGtoC = RNAseqCtoG.replace("g","C")
RNAseqAtoU = RNAseqGtoC.replace("a","U")
RNAseq = RNAseqAtoU.replace("t","A")



# print the RNA sequence in lower case letters #		
print(RNAseq.lower())		
 		 
# make a new string with the reverse complement DNA sequence #		
seqrev=seq[::-1]		
 		 
#print reversed sequence
		
print(seqrev)		
		
#extract 13th and 14th codons#		
		
seq1314 = seq[13]+seq[14]		
 		 
# print 13th and 14th codons #		
 		 
print(seq1314)

# Amino Acid Translation table from https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt


# Copy the sequences of Amino Acids and base pairs in as a strings #

AAs = str("FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG")
Base1 = str("TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG")
Base2 = str("TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG")
Base3 = str("TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG")


# split DNA sequence into three strings by codon position #

# check length of the sequence #

len(seq)

# find the positions of the first codons by counting by threes starting at the first #
codon1Position = range(0,621,3)

print(codon1Position)

# find the position of the second and third codons by counting by threes starting at second and third codons, respectively #

codon2Position = range(1,621,3)
codon3Position = range(2,621,3)

# check that this looks right #

print(codon2Position)
print(codon3Position)

# make string containing each codon, with the orphan bases left out #
   
cod1 = []
for i in range(0,618,3):
    cod1.append(seq[i]) 
    
cod2 = []
for i in range(1,618,3):
    cod2.append(seq[i]) 
    
cod3 = []
for i in range(2,618,3):
    cod3.append(seq[i]) 
    
# Define a new list#
    
AA=[]

# Convert the strings of bases from the reference to lower case #
base1=Base1.lower()
base2=Base2.lower()
base3=Base3.lower()

"""
Nested for loop searches each of the lists of codons above and compares them to the
base pair lists provided by location, if all three match up, it returns the Amino Acid
listed in the same row. If not, it keeps looking. The list is then merged into a string
and printed
"""
for i in range(0,206):
    for j in range(0,64):
        if cod1[i]==base1[j] and cod2[i]==base2[j] and cod3[i]==base3[j]:
                AA.append(AAs[j])
                
AAlist=''.join(AA)
print(AAlist)
   
#Put everything done above in a generalized function that takes a 3'->5' DNA sequence 
#as an input but assumes the library has been loaded as four separate strings as above


   
def translate(sequence):
   
    cod1 = [] # make string containing each codon, with the orphan bases left out #
    for i in range(0,len(sequence),3):
        cod1.append(sequence[i]) 
    
    cod2 = []
    for i in range(1,len(sequence),3):
        cod2.append(sequence[i]) 
    
    cod3 = []
    for i in range(2,len(sequence),3):
        cod3.append(sequence[i]) 
    AA=[] # Define a new list #

    #Nested for loop searches each of the lists of codons above and compares them to the#
    #base pair lists provided by location, if all three match up, it returns the Amino Acid#
    #listed in the same row. If not, it keeps looking. The list is then merged into a string#
    #and printed#
    for i in range(0,206):
        for j in range(0,64):
            if cod1[i]==Base1[j] and cod2[i]==Base2[j] and cod3[i]==Base3[j]:
                AA.append(AAs[j])
                
    AAlist=''.join(AA)

    print(AAlist) 
#see if the function works
translate(seq)

# BLASTed the sequence to genbank to find the alignment and check translation
# sequence and independent translation here: http://www.ncbi.nlm.nih.gov/nucleotide/594593097?report=genbank&log$=nuclalign&blast_rank=1&RID=C293HBK7014
