#!/usr/bin/env python3

import argparse
import gzip
from Bio import SeqIO
from sys import stdin, stdout

def getLowerCase(fa, bed_low):
    """
    Cool function to detect lowercase characters in a FASTA file
    
    fa: FASTA file
    bed: BED file
    """
    
    f_in = fa
    if fa.endswith('.gz'):
        with gzip.open(fa, 'rb') as f_unzip:
            f_in = f_unzip.read()
    
    for seq_record in SeqIO.parse(fa, "fasta"):
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
            print('%s\t%i\t%i' % (chr_id, start, end), file = bed_low)
    bed.close()

# TODO 
# def getUppercase(in, out)

def getBothCases(fa, bed_low, bed_up):
    '''
    Merge function to get 2 bed files: 1 with uppercase and 1 with lowercase 
    '''
    for seq_record in SeqIO.parse(fa, "fasta"):
        chr_id = seq_record.id
        chr = str(seq_record.seq)
        start_ind_low = []
        start_ind_up = []
        end_ind_low = []
        end_ind_up = []
        
        for i in range (0, len(chr)):
            if chr[0].islower() and i==0:
                start_ind_low.append(i)
            
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
            print('%s\t%i\t%i' % (chr_id, start, end), file = bed_low)
    bed.close()
   '''
        for i in range (0, len(chr)):
            if chr[0].isupper() and i==0:
                start_ind.append(i)
            
            elif chr[i-1].islower() and chr[i].isupper():
                start_ind.append(i) 
        
        for i in range (0, len(chr)):
            if chr[0].islower() and i==0:
                continue
        
            elif chr[i-1].isupper() and chr[i].islower():
                end_ind.append(i-1) 
    
        if chr[i].isupper():
            end_ind.append(i)
    
        for start, end in zip(start_ind, end_ind):
            print('%s\t%i\t%i' % (chr_id, start, end), file = bed_up)
    bed_up.close()
'''
def isSameCase(fasta, case="upper"):
    """
    This function checks if the fasta file contains just upper or lower case letters
    
    fasta: FASTA file
    case: either "upper" or "lower"
    """
    for seq_record in SeqIO.parse(f_in, "fasta"):
        chr_id = seq_record.id
        chr = str(seq_record.seq)
        
    
    return True # or False if not all the letters have the same case
    
#getLowercase(f_in, f_out)
#isSameCase(f_in)
     # this is one of the ways we could print corresponding elements from two lists
    #for i in range(1, len(start_ind)):
    #    strat_ind[i], end_ind[i]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Locate lower case letters in fasta file")
    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'), 
                        help="input fasta file")
    args = parser.parse_args()

    getLowerCase(args.file, stdout)
