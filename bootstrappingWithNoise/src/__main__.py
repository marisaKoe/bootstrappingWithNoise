'''
Created on 07.03.2017

@author: marisakoe

Main function to control the input files.
The file name needs to be written, so it can be read by glob.

'''
import glob, timeit, os
from add_noise_matrices import std_cellwise




if __name__ == '__main__':
    ##ielex data
    #data = "IELex"
    #f = "input/"+data+"/distanceMatricesIELexPMI/*.phy"
    #std_cellwise(f,data)
    
    ##data NLex
    #start = timeit.default_timer()
    #pos = ["binaryFeatures", "phoneticFeatures","CogLev","CogLevGeo", "CogNormHamming", "CogNormHammingGeo", "CogNw", "CogNwGeo", "pmi", "pmiGeo", "pmiMultidata", "pmiMultidataGeo", "sigmoid", "sigmoidGeo", "sigmoidMultidata", "sigmoidMultidataGeo"]
    ##only the files which might be best for the dissertation, always use synonyms!!!!
    #note: CogLev rausgenommen, da berechnung unterbrochen wurde, nachher wieder miteinbeziehen
    pos = ["CogLevGeo", "CogNw", "CogNwGeo", "pmiMultidata", "pmiMultidataGeo", "sigmoidMultidata", "sigmoidMultidataGeo","phoneticFeatures"]
    #pos = ["languageTree"]
    #pos = ["test"]
    data = "nelex"
    for p in pos:
	start = timeit.default_timer()
	print "Begin!", p
        f = "input/"+data+"/"+p+"/phylip/*.phy"
        dataFolder = data+"/"+p
        if not os.path.exists("output/"+dataFolder):
            os.makedirs("output/"+dataFolder)
        std_cellwise(f, dataFolder)
        print p,"DONE!"
    
    	stop = timeit.default_timer()
   	print stop-start
