#!/usr/bin/env python3

import argparse
import gzip
import sys
from sys import stdout
from Bio import SeqIO

def getBothCases(fa, bed_low, bed_up):
    '''
    Function that detects lowercase and uppercase characters in a FASTA file

    fa: FASTA file
    bed_low: BED file containing lowercase characters positions
    bed_up: BED file containing uppercase characters positions
    '''

    for seq_record in SeqIO.parse(fa, "fasta"):
        chr_id = seq_record.id
        chr = str(seq_record.seq)
        start_ind_low = []
        start_ind_up = []
        end_ind_low = []
        end_ind_up = []


        for i in range (0, len(chr)):

            # 1st character is lowercase
            if chr[0].islower() and i==0:
                start_ind_low.append(i)

            # 1st character is uppercase
            elif chr[0].isupper() and i==0:
                start_ind_up.append(i)

            # i starts a new lowercase string + i ends an uppercase string
            elif chr[i-1].isupper() and chr[i].islower():
                start_ind_low.append(i)
                end_ind_up.append(i-1)

            # i starts a new uppercase string + i ends a lowercase string
            elif chr[i-1].islower() and chr[i].isupper():
                start_ind_up.append(i)
                end_ind_low.append(i-1)

        # Last character is lowercase
        if chr[i].islower():
            end_ind_low.append(i)

        # Last character is uppercase
        elif chr[i].isupper():
            end_ind_up.append(i)


        for start, end in zip(start_ind_low, end_ind_low):
            print('%s\t%i\t%i' % (chr_id, start, end), file=bed_low)

        for start, end in zip(start_ind_up, end_ind_up):
            print('%s\t%i\t%i' % (chr_id, start, end), file=bed_up)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Locate lowercase and uppercase case characters in a FASTA file")
    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'),
                        help="input fasta file")
    parser.add_argument('-bl', "--bedlow",
                        type=argparse.FileType('w'),
                        help="output lowercase bed file")
    parser.add_argument('-bu', "--bedup",
                        type=argparse.FileType('w'),
                        help="output uppercase bed file")
    args = parser.parse_args()

    getBothCases(args.file, args.bedlow, args.bedup)
