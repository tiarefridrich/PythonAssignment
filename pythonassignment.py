#!/usr/bin/#!/usr/bin/env python3

#import the packages
import pandas as pd
import matplotlib.pyplot as plt

#Part 1: Create a sequence object that accepts a string
class Seq(object): #this is general so it can accept more than one sequence
    def __init__(self,sequence): #in this case the sequence is mysequence, which is stated outside the sequence object
        self.sequence = sequence

#Part 2: add a method to count kmers of size k
    #this function counts the observed kmers
    def count_kmers(self,k):
        counter = {} #empty counter
        for i,base in enumerate(self.sequence): #go through the string and get position and base
            kmer = self.sequence[i:i+k] #take a slice of the string to get the kmer
            if kmer in counter:
                counter[kmer] += 1 #if you run into it for a second time, add 1
            else:
                counter[kmer] = 1 #if you run into it for the first time its equal to 1
        return(counter) #this returns the number and type of kmers

mysequence = Seq("ATTTGGATT")
print(mysequence.count_kmers(k))
print('Number of kmers: ',len(mysequence.count_kmers(1))) #have to include a number in here for it to work
#how do I make it so it outputs the kmers without k specified as a number?

counter_df = pandas.DataFrame(mysequence.count_kmers(1), index=['kmer']) #creates a dataframe
print(counter_df)#prints dataframe
counter_df.plot(kind='bar'); #makes dataframe into a bar chart

#as of right now, still don't have the dataframe set up correctly, or the possible kmers
