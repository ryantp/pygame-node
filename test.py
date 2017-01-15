#PYTHON3.5.1 (Anaconda3, 64-BIT);

from backend import dbsave as d 
import loadmng as l 

a = d.SaveMaster(l.rootdir()) 
a._read_all() 
