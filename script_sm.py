#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:52:35 2019

@author: cnavarrete
"""
#I don't need to open the input file, you can use the function directly
#f_inp = '/home/cnavarrete/Desktop/Maciek_Task/test.sm.fa'
import argparse
from Bio import SeqIO
from sys import stdin, stdout

def getLowerCase(f_in, f_out):
    """
    Cool function to detect lowercase characters in a FASTA file
    
    f_in: FASTA file
    f_out: BED file
    """
    for seq_record in SeqIO.parse(f_in, "fasta"):
        chr_id = seq_record.id
        chr = str(seq_record.seq)
        start_ind = []
        end_ind = []
   
        for i in range (0, len(chr)):
            if chr[0].islower() and i==0:
                start_ind.append(i)
            
            elif chr[i-1].isupper() and chr[i].islower():
                start_ind.append(i) 
        
        for i in range (0, len(chr)):
            if chr[0].isupper() and i==0:
                continue
        
            elif chr[i-1].islower() and chr[i].isupper():
                end_ind.append(i-1) 
    
        if chr[i].islower():
            end_ind.append(i)
    
        for start, end in zip(start_ind, end_ind):
            print('%s\t%i\t%i' % (chr_id, start, end), file = f_out)
    f_out.close()

# TODO 
# def getUppercase(in, out)

def isSameCase(fasta, case="upper"):
    """
    This function checks if the fasta file contains just upper or lower case letters
    
    fasta: FASTA file
    case: either "upper" or "lower"
    """
    return True # or False if not all the letters have the same case
    
#getLowercase(f_in, f_out)
#isSameCase(f_in)
     # this is one of the ways we could print corresponding elements from two lists
    #for i in range(1, len(start_ind)):
    #    strat_ind[i], end_ind[i]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Locate lower case latters in fasta file")
    parser.add_argument('infile', type=argparse.FileType('r'), help="input fasta file")
    args = parser.parse_args()

    getLowerCase(args.infile, stdout)
