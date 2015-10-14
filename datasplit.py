import sys;
import random;

################## DATA SPLITTING #############################

# python3 datasplit.py modifiedFeatureFile .75 1 SVM
 # python3 datasplit.py MEGAMInput.feat .75 1 MEGAM
 # python3 datasplit.py MEGAMInput.feat .75 0

checkDict = dict();

generatedTraining = open("genTraining.txt","w");
generatedTest = open("generatedTest.txt","w");
actualLabels = open("labelsOnly.txt","w");
percentage = sys.argv[2];

testWithLabel = int(sys.argv[3]);  # Indicating whether the test data must have lebels in them as requrired by MEGAM and SVM. 

if testWithLabel == 1 and len(sys.argv) == 4:
	print("If the test data must have labels, please mention if it is for MEGAM or SVM (4th Argument)");
	sys.exit();
elif testWithLabel == 1:
	typeOfLabel = sys.argv[4];


dataFile = open(sys.argv[1],"r");

lineCount = 0;

for line in dataFile:
	lineCount+=1;


end = int(lineCount*float(percentage));
count = 0;
while count != end:
	index = random.randrange(0,lineCount);
	if index in checkDict.keys():
		continue;
	checkDict[index]=1;
	count+=1;
	#print(index);

# Now, for all the indexes that can be found in the hashmap.keys(), you push it to the training set, else to the
#  testing set.

count = 0;

dataFile.seek(0);

for line in dataFile:
	if count in checkDict.keys():
		generatedTraining.write(line);
	else:
		words = line.split();
		#print(count);
		actualLabels.write(words[0]+"\n");
		if testWithLabel == 1: 
			# It means that it must have labels. 
			if typeOfLabel == "MEGAM":
				if words[0] == "POSITIVE" or words[0] == "SPAM" or words[0] == "1":
					generatedTest.write("1 ");
				else:
					generatedTest.write("0 ");

			elif typeOfLabel == "SVM":
				if words[0] == "POSITIVE" or words[0] == "SPAM" or words[0] == "+1":
					generatedTest.write("+1 ");
				else:
					generatedTest.write("-1 ");
			else:
				print("Invalid label name type given = "+ typeOfLabel);
				sys.exit();

		for i in range(1, len(words)):
			generatedTest.write(words[i]);
			if i != len(words)-1:
				generatedTest.write(" ");
		generatedTest.write("\n");
	count+=1;


#print(str(lineCount));
