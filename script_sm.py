#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:52:35 2019

@author: cnavarrete
"""
#I don't need to open the input file, you can use the function directly
#f_inp = '/home/cnavarrete/Desktop/Maciek_Task/test.sm.fa'
from Bio import SeqIO
from sys import argv

if len(argv) == 3:
    f_in = argv[1] 
    f_out = argv[2] 
else:
    print('Usage: script_sm.py input_FASTA output_BED')
#f_in = '/home/cnavarrete/Desktop/Maciek_Task/test.sm.fa'
#f_out = '/home/cnavarrete/Desktop/Maciek_Task/file1_sm_output.bed'

def getLowerCase(f_in, f_out):
    """
    Cool function to detect lowercase characters in a FASTA file
    
    f_in: FASTA file
    f_out: BED file
    """
    fo = open(f_out, "w")
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
            print('%s\t%i\t%i' % (chr_id, start, end), file = fo)
    fo.close()

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