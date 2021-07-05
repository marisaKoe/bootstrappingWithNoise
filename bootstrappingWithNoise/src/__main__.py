'''
Created on 07.03.2017

@author: marisakoe

Main function to control the input files.
The file name needs to be written, so it can be read by glob.

'''
import glob, timeit, os
from add_noise_matrices import std_cellwise




if __name__ == '__main__':
    
    ##data NLex
    pos = ["CogLevGeo", "CogNw", "CogNwGeo", "pmiMultidata", "pmiMultidataGeo", "sigmoidMultidata", "sigmoidMultidataGeo"]
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
