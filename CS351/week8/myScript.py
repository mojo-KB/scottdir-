import sys
print "this is:", sys.argv[0]
print "and", sys.argv[1]

OpenComputeEngine("localhost","serial")
OpenDatabase(sys.argv[1])
AddPlot("Mesh","mesh")
AddPlot("Pseudocolor","patch")
DrawPlots()
#quit()

#visit -cli -assume-format tecplot -s myScript.py
#OpenDatabase("mytest.tec")
#visit -cli -assume-format tecplot -s myScript.py mytest.tec
