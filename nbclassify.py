import sys;
import math;

modelfile = open(sys.argv[1],"r",encoding = "latin1");
testInput = open(sys.argv[2],"r", encoding = "latin1");

nlines = int(modelfile.readline());
uniqueWords = int(modelfile.readline());

nPositiveDict = int(modelfile.readline());
nNegativeDict = int(modelfile.readline());

plabel1 = float(modelfile.readline());
plabel2 = float(modelfile.readline());

logpl1 = math.log(plabel1);
logpl2 = math.log(plabel2);

finalPosProb = 0.0;
finalNegProb = 0.0;

nPosWords = int(modelfile.readline());
nNegWords = int(modelfile.readline());

probDict = dict();

POS = int(modelfile.readline()); # if POS = 0, then it is HAM or SPAM, else it is POSITIVE or NEGATIVE

for i in range(9,9+uniqueWords):
	temp = modelfile.readline().split(" ");
	probDict[int(temp[0])] = [float(temp[1]),float(temp[2])] ;

for line in testInput:
	tempDict = dict();
	words = line.split();
	for word in words:
		if int(word.split(":")[0]) in probDict.keys():
			key = int(word.split(":")[0]);
			value = int(word.split(":")[1]);
			tempDict[key]=value;
			#print("word skipped"+word);


	sigmaLogPPos = 0.0;
	sigmaLogPNeg = 0.0;
	for key,value in tempDict.items():
		sigmaLogPPos+=math.log(float(probDict[key][0]))*float(value);
		sigmaLogPNeg+=math.log(float(probDict[key][1]))*float(value);
	finalPosProb = logpl1+sigmaLogPPos;
	finalNegProb = logpl2+sigmaLogPNeg;

	if finalPosProb>=finalNegProb:
		if POS == 1:
			print("POSITIVE");
		else:
			print("HAM");
	else:
		if POS == 1:
			print("NEGATIVE");
		else:
			print("SPAM");

	#print(finalPosProb,finalNegProb);




#print(probDict);

