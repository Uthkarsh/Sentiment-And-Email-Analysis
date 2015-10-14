# Use seperate dictionaries for positive and negative labels.

# TODO: Count the number of unique words in the file -- For smoothing purposes. 
import sys;
import math;
import itertools;

positiveDict = dict(); # For positive/ham labels
negativeDict = dict(); # For negative/spam labels 
consolidated = dict(); # For the purpose of consolidated count of unique labels. 

# These reprsent the number of positive and negative sentences
nPos = 0;
nNeg = 0;   

# These represent the TOTAL number of words in postive and negative context. 

nPosWords = 0;
nNegWords = 0;

testList = [];

POS = 0;

input = open (sys.argv[1], "r+");
output = open (sys.argv[2], "w"); # Output model file

Count = 0;
uniqueWords = 0;   # Stores the Vocabulary length. 
for line in input:
	Count+=1;
	listLine = line.split();
	if line.split()[0] == "POSITIVE" or line.split()[0] == "NEGATIVE":
		POS = 1;

	if line.split()[0] == "POSITIVE" or line.split()[0] == "HAM":
		type = 1;
		nPos+=1;
	else:
		type = 0;
		nNeg+=1;

	for i in range(1, len(listLine)):
		identifier = int(listLine[i].split(":")[0]);
		frequency = int(listLine[i].split(":")[1]);
		if type==1:

			if identifier in positiveDict.keys():
				positiveDict[identifier] = int(positiveDict[identifier])+frequency; 
				nPosWords+=frequency;
			else:
				positiveDict[identifier] = frequency; 
				nPosWords+=frequency;
		else:

			if identifier in negativeDict.keys():
				negativeDict[identifier] = int(negativeDict[identifier])+frequency;
				nNegWords+=frequency;
			else:
				negativeDict[identifier] = frequency; 
				nNegWords+=frequency;

		if identifier not in consolidated.keys():
			consolidated[identifier] = 1;
			uniqueWords+=1;
			testList.append(identifier);
			#print(str(identifier)+"\n");

			'''if Count==5:
		sys.exit();'''



output.write(str(Count)+"\n");
output.write(str(uniqueWords)+"\n");
output.write(str(len(positiveDict.keys()))+"\n");
output.write(str(len(negativeDict.keys()))+"\n");
#print(str(nPos),str(nNeg));
#print(str(nPosWords,str(nNegWords)));
output.write(str(nPos/Count)+"\n");
output.write(str(nNeg/Count)+"\n");
output.write(str(nPosWords)+"\n"+str(nNegWords)+"\n");
output.write(str(POS)+"\n");

for keys in negativeDict.keys():
	if keys not in positiveDict.keys():
		positiveDict[int(keys)]=0;
		#print("added a new one");

for key,value in positiveDict.items():
	output.write(str(key)+" ");
	#output.write(str(value)+" ");
	output.write(str((value+1)/(nPosWords+uniqueWords))+" ");
	if key in negativeDict:
		#output.write(str(negativeDict[key])+" ");
		output.write(str((negativeDict[key]+1)/(nNegWords+uniqueWords))+"\n");
	else:
		output.write(str(1/(nNegWords+uniqueWords))+"\n");


testList.sort();

'''for elem in testList:
	print(elem);'''
'''for keys,values in positiveDict.items():
	print('+',keys,':',values);'''

'''with open(sys.argv[1]) as f:
    print sum(1 for _ in f)'''


