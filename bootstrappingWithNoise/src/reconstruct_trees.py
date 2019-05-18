'''
Created on 05.12.2016

@author: marisa

this module reconstructs NJ trees for all 1000 matrices create and saves them in one file to get them into Dendroscope for making a majority-rule consensus tree
'''

from rpy2.robjects.packages import importr

#import the basis of R
base = importr("base")
utils = importr("utils")
stats = importr("stats")
#imports ape, required for phangorn
ape = importr("ape")
#imports phangorn
phangorn = importr("phangorn")


def reconstruct_treesR(matrix, concept, treeFolder):
    '''
    reconstructs NJ trees with ape.
    Saves all trees in one file to fit into dendroscope
    :param matrix:the matrix file
    :param concept:the concept
    '''
    folder = treeFolder+concept+"+allTrees.nwk"
    t = utils.read_table(matrix,header=False, skip=1, row_names=1)
    mx = base.as_matrix(t)
    dm = stats.as_dist(mx)
    #tree = ape.nj(dm)
    tree1 = ape.fastme_bal(dm, nni=True, spr=True, tbr=False)
    ape.write_tree(tree1, folder,append=True)
    #return tree


        
    





if __name__ == '__main__':
    pass
