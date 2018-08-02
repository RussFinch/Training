# ================= Compulsory Task 1 ==================
# Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html 
# Note the 'SLC' code for each Amino Acid.
# Create a program called SickleCellDisease.py .
# We will simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease. 
# Write a function called translate that, when given a DNA sequence of arbitrary length,
# identifies and returns the amino acid sequence of the DNA using the amino acid SLC code found in that table.
#   EG DNA Input: ATTATTATT
#          Output: III
# There are many different amino acids so this may get a bit repetitive. Just do the first five Amino Acids (i.e. I L V F M) and make any other codon be printed as the amino acid 'X' 
# So basically, you would use an if - elif - elif .... else structure to translate each codon of DNA into the correct Amino Acid
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3. 

# Remember: 
#	- len(DNA)  Will return the length of a String
#	- DNA[0:3]  Will get the first 3 characters of the string stored in DNA
#	- num = 3
#	  DNA[0:num]  Will also get the first 3 characters of the string stored in DNA

# ================= Compulsory Task 2 ==================
# Add another function to the program SickleCellDisease.py called 'mutate'.
# This function must read in the contents of the text file named 'DNA.txt'
# It must then identify the first occurrence of the lowercase letter 'a' in 'DNA.txt'.
# You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.
# The normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to an 'A'.
# The mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.
# Now create a new function, txtTranslate, that calls the translate function that you wrote in Part 1, to take in text file input.
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.

aminoSeq = list()

def translate(dna):
    codonList = [dna[i:i+3] for i in range(0, len(dna), 3)]
    del aminoSeq[:]
    for codon in codonList:
        if codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
            aminoSeq.append('I')
        elif codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG' or codon == 'TTA' or codon == 'TTG':
            aminoSeq.append('L')
        elif codon == 'GTT' or codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
            aminoSeq.append('V')
        elif codon == 'TTT' or codon == 'TTC':
            aminoSeq.append('F')
        elif codon == 'ATG':
            aminoSeq.append('M')
        else:
            aminoSeq.append('X')    
    return aminoSeq

def mutate():
    inputDNA = open('DNA.txt', 'r')
    outNormalDNA = open('normalDNA.txt', 'r+')
    normalList = ''.join(inputDNA).replace('\n', '').replace('a', 'A')
    outNormalDNA.write(normalList)
    outNormalDNA.close()
    inputDNA.close()

    inputDNA = open('DNA.txt', 'r')
    outMutatedDNA = open('mutatedDNA.txt', 'r+')
    mutatedList = ''.join(inputDNA).replace('\n', '').replace('a', 'T')
    outMutatedDNA.write(mutatedList)
    outMutatedDNA.close()
    inputDNA.close()

def txtTranslate(normal, mutated):
    dnaNormalList = list(open(normal, 'r'))
    normalDNAString = ''.join(dnaNormalList)
    translate(normalDNAString)
    print("\nNormal DNA Sequence\n\n" + str(aminoSeq))
    dnaMutatedList = list(open(mutated, 'r'))
    mutatedDNAString = ''.join(dnaMutatedList)
    translate(mutatedDNAString)
    print("\nMutated DNA Sequence\n\n" + str(aminoSeq))

mutate()
txtTranslate('normalDNA.txt', 'mutatedDNA.txt')