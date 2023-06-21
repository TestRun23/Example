#Michael Saban, BIOL 500, Rosalind #1
#Given: A DNA string Text and an integer k.
#Return: All most frequent k-mers in Text (in any order).

#Desired file name for input file
filename = 'rosalind_ba1b.txt'

#Read the file contents into a list split by line
with open(filename,'r') as f_in:
    content = f_in.read().split()
    
Text = content[0] #Input text is the first line
k = int(content[1]) #k value for k-mer is the second line
        

#Store all possible k-mers of the input text as list 'kmers'
kmers = []
for i in range(len(Text)-k+1): #Iterate through every value in the length of the input text up until there aren't k values following (prevents adding too short of kmers)
    kmers.append(Text[i:i+k]) #Add substring of length k to kmers

#Count how many instances each kmer occurs
counts = {}
for i in kmers: #Iterate through every kmer
    if i in counts: #If already present in the counts dictionary as a key, increase the value by 1
        counts[i]+=1
    else: #Otherwise, add it as a key to the counts dictionary with a value of 1
        counts[i] = 1

#Determine the most frequent kmer(s)
most_frequent = []
max_count = max(counts.values()) #Largest kmer count

for k,v in counts.items(): #Iterate through the kmer-count dictionary
    if v == max_count: #Add the kmer to the list if it has value max_count (allows for multiple kmers with ties for highest count)
        most_frequent.append(k)
        
print(most_frequent)

#Write to output file
with open('Rosalind1_out.txt','w') as f_out:
    f_out.write(' '.join(most_frequent))
