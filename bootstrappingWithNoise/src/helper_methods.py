'''
Created on 05.12.2016

@author: marisa

This module includes all helper methods to read the data, edit the data and write the data
'''

from numpy import *
import re
import glob

def read_matrices(f):
    '''
    read all the distance matrices from a folder
    the distance matrices calculated with the pmi method and not edited yet
    '''
    list_matrices = glob.glob(f)
    return list_matrices


def transform_distance_matrices(matrix):
    """
    !!!When language names are stored in an extra file, delete the comments in the corresponding line
    Read interleaved phylip distance matrix into a numpy matrix.
    Return taxon names, matrix
    """
    #only needed when the language names are stored in an extra file
    #names, longnames = get_language_sample() 
    #reads the matrix into a list
    elements = open(matrix,'rU').read().split()
    #removes the first row (the number of taxa in the matrix)
    N = int(elements.pop(0))
    #creates a list for the taxa
    taxa = []
    #fills the default matrix with -inf
    S = asarray(-Inf*ones([N,N]))
    
    #got through the list and save the distances in the matrix
    for row, i in enumerate(range(0, len(elements), N+1)):
        #append the first element of the list to the list of taxa
        taxa.append(elements[i])
        #fill the matrix
        S[row,:] = [float(x) for x in elements[i+1:i+N+1]]
        
    
    #ONLY needed when the language names are in an extra file
    #taxa = longnames.tolist()
    
    #returns the taxa and the matrix
    return taxa, S


def phylip_output(m,names=[],file1='data.phy'):
    '''
    auxiliary function for writing the distance matrices to a file
    :param m: matrix
    :type m:an array
    :param names:languages
    :type names:list
    :param file:a file
    :type file:file
    '''
    if len(names) != len(m):
        names = xrange(len(m))
        mx = 10
    else:
        mx = max([len(x) for x in names])
    f = open(file1,'w')
    f.write(str(len(names))+'\n')
    for nm, row in zip(names,m):
        f.write(str(nm).ljust(mx))
        for cell in row:
            f.write(' '+str(cell))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    matrix_list = read_matrices()
    print matrix_list
    for m in matrix_list:
        t, mtx = transform_distance_matrices(m)
        print type(mtx)