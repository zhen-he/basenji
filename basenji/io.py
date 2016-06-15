#!/usr/bin/env python

import numpy as np

################################################################################
# io.py
#
# Methods to load the training data.
################################################################################

def dna_1hot(seq, seq_len=None):
    ''' dna_1hot

    Args:
      seq: nucleotide sequence.
      seq_len: length to extend sequences to.

    Returns:
      seq_code: length by nucleotides array representation.
    '''
    if seq_len is None:
        seq_len = len(seq)
        seq_start = 0
    else:
        if seq_len <= len(seq):
            # trim the sequence
            seq_trim = (len(seq)-seq_len)//2
            seq = seq[seq_trim:seq_trim+seq_len]
            seq_start = 0
        else:
            seq_start = (seq_len-len(seq))//2

    seq = seq.upper()
    seq = seq.replace('A','0')
    seq = seq.replace('C','1')
    seq = seq.replace('G','2')
    seq = seq.replace('T','3')

    # map nt's to a matrix len(seq)x4 of 0's and 1's.
    #  dtype='int8' fails for N's
    seq_code = np.zeros((seq_len,4), dtype='float16')
    for i in range(seq_len):
        if i < seq_start:
            seq_code[i,:] = 0.25
        else:
            try:
                seq_code[i,int(seq[i-seq_start])] = 1
            except:
                seq_code[i,:] = 0.25

    return seq_code
