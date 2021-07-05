'''
Created on 05.12.2016

@author: marisa

this module provides three methods to add noise to a distance matrix

1. one-half of the standard deviation, which varies uniformly 0 <= r <= c (r=noise, c=one-half standard deviation), added differently to each cell

2. one-half of the standard deviation, which varies uniformly 0 <= r <= c (r=noise, c=one-half standard deviation), added to the whole matrix


'''

import os

from numpy import *
from random import uniform
from itertools import combinations
from collections import defaultdict


from helper_methods import *
from reconstruct_trees import *
from createConsensusPaup import reconstruct_consensus

############main method##############################################

def std_cellwise(f,dataFolder):
    '''
    This methods calculates the standard deviation (c) of the matrix and adds noise to each cell of the matrix.
    Noise (r) varies uniformly between 0 <= r <= c.
    '''
    ##get all the matrices in the input folder
    list_matrices = read_matrices(f)
    
    ##create all the folders needeed for the analysis
    folder = "output/"+dataFolder+"/matrices"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    treeFolder = "output/"+dataFolder+"/trees/"
    if not os.path.exists(treeFolder):
        os.makedirs(treeFolder)
        
    contreeFolder = "output/"+dataFolder+"/consensus/"
    if not os.path.exists(contreeFolder):
        os.makedirs(contreeFolder)
    
    ##go through the list of matrices, extract the concept, create a folder, transform the matrix in nparray, calculate standard deviation over original distances, add noise to the matrix
    for matrix in list_matrices:
        concept = matrix.split("/")[-1].split(".")[0]
        
        ##take of spaces and brackets PAUP cannot read
        if " " in concept:
            concept = concept.replace(" ","")
        elif "[" in concept:
            concept = concept.replace("[","")
            concept = concept.replace("]","")

        taxa, mtx = transform_distance_matrices(matrix)
        half_std = std(mtx)/2
        #edit_matrices_cellwise(taxa, mtx, half_std, folder, concept)
        edit_matrices_noise(taxa, mtx, half_std, folder, concept, treeFolder, contreeFolder)

        
        
#################helper methods#################################


def edit_matrices_noise(taxa, mtx, half_std, folder, concept, treeFolder, contreeFolder):
    '''
    Add noise only to the original matrix.
    Adds random noise to the original value in the matrix. Values are not added up.
    :param taxa: language names
    :param mtx: distance matrix
    :param half_std: half of the standard deviation
    :param folder:name of the folder
    :param concept:name of the concept
    '''
    ##create a list with numbers from 0 to the length of the taxa
    newList = range(0, len(taxa))
    number_matrices = range(0,1000)
    ##create default dict
    dict_noiseMtx = defaultdict()
    for i in number_matrices:
        #fill new matrix with 0
        S = asarray(0.0*ones([len(mtx),len(mtx)]))
        ##get the combinations from the matrix
        for x in combinations(newList, r=2):
            ##get the two values
            n1, n2 = x 
            ##get the random noise, which should be added
            noise_random = uniform(0.0, half_std)
            #add noise to the value in the matrix
            S[n1,n2] = mtx[n1,n2]+noise_random
            S[n2,n1] = mtx[n2,n1]+noise_random
        ##save the noisy matrix in the dictionary
        dict_noiseMtx[i] = S

    
    for num_mtx, mtx in dict_noiseMtx.items():
        ##create the file for the matrix
        matrix_file = folder+"/noiseMatrix"+str(num_mtx)+".phy"
        #write the matrix to the file
        phylip_output(mtx, taxa, matrix_file)
        ##reconstruct the tree for the noisy matrix
        reconstruct_treesR(matrix_file,concept,treeFolder)
    
    ##remove the files for the next concept
#     for filename in os.listdir(folder):
#         os.remove(os.path.join(folder,filename))
         
    ##reconstruct the consensus tree for all trees in the noisy bootstrap
    reconstruct_consensus(treeFolder, concept, contreeFolder)


# def edit_matrices_cellwise(taxa,mtx, half_std, folder, concept):
#     '''
#     edits the matrix by adding noise to each cell. The noise is always adding up. The original matrix is excluded.
#     Always added to the values before.
#     Doing this 1000 times
#     '''
#     ##create a list with numbers from 0 to the length of the taxa
#     newList = range(0, len(taxa))
#     
#     number_matrices = range(0,10)
#     #print number_matrices
#     #list_of_trees = []
#     for i in number_matrices:
#         print i
#         ##make the possible combinations, draw the noise randomly, edit the matrix, save the matrix in a folder
#         for x in combinations(newList, r=2):
#             n1, n2 = x
#             noise_random = uniform(0.0,half_std)
#             mtx[n1,n2] = mtx[n1,n2]+noise_random
#             mtx[n2,n1] = mtx[n2,n1]+noise_random
#         matrix_file = folder+"/noiseMatrix"+str(i)+".phy"
#         phylip_output(mtx, taxa, matrix_file)
#         tree = reconstruct_treesR(matrix_file,concept)
#         #list_of_trees.append(tree)
    
    


if __name__ == '__main__':
    std_cellwise()
