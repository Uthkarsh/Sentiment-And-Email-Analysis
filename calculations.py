# RESULTS.txt, labels.txt

import sys;

results = open(sys.argv[1],"r");
labels = open(sys.argv[2],"r");

nCorrectClassifiedL1 = 0;
nCorrectClassifiedL2 = 0;

nActualL1 = 0;
nActualL2 = 0;

nClassifiedL1 = 0;
nClassifiedL2 = 0;

lineCount = 0;

for line in results:
	lineCount+=1;

results.seek(0);

diffCount = 0;

for i in range(0, lineCount):
	labeli = labels.readline();
	resulti = results.readline();
	if labeli == "POSITIVE\n" or labeli == "SPAM\n":
		nActualL1+=1;
		if(resulti.split("\n") == labeli.split("\n")):
			nCorrectClassifiedL1+=1;
	else:
		nActualL2+=1;
		if(resulti.split("\n") == labeli.split("\n")):
			nCorrectClassifiedL2+=1;

	if resulti == "POSITIVE\n" or resulti == "SPAM\n":
		nClassifiedL1+=1;
	else:
		nClassifiedL2+=1;

if nClassifiedL1 == 0:
	print("Denominator 0, hence Precision Assigned to zero");
	precLabel1=0;
else:
	precLabel1 = float(nCorrectClassifiedL1/nClassifiedL1);
if nClassifiedL2 == 0:
	print("Denominator 0, hence Precision Assigned to zero");
	precLabel2=0;
else:
	precLabel2 = float(nCorrectClassifiedL2/nClassifiedL2);


recallLabel1 = float(nCorrectClassifiedL1/nActualL1);
recallLabel2 = float(nCorrectClassifiedL2/nActualL2);

print("Precision for Label1 = "+str(precLabel1));
print("Precision for Label2 = "+str(precLabel2));

print("Recall for Label1 = "+str(recallLabel1));
print("Recall for Label2 = "+str(recallLabel2));
fL1=0;
fL2=0;

if (precLabel1+recallLabel1) == 0:
	fL1 =0;
	print("Denominator 0, hence F score Assigned to zero");
else:
	fL1 = (2*precLabel1*recallLabel1)/(precLabel1+recallLabel1);
if (precLabel2+recallLabel2) == 0:
	fL1 =0;
	print("Denominator 0, hence F score Assigned to zero");
else:
	fL2 = (2*precLabel2*recallLabel2)/(precLabel2+recallLabel2);


print("F score for Label1 = "+str(fL1));
print("F score for Label2 = "+str(fL2));

