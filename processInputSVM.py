import sys;

file = open(sys.argv[1], "r" , encoding ="latin1");
output = open("SVMInput.feat", "w", encoding = "latin1");

# If it is 1, it means that it is preprocessing, else it is postprocessing. 
# For Pre-Processing, the input will be in Project Data format.
# For Post-Processing, the input will be in SVM format.

# If Preprocess is 0, then the third argument has to be either "SPAM" or "POSITIVE", indicating based on what the post-processing
#has to be done with.  

preProcess = int(sys.argv[2]); 
label = "";
start = 1;
if preProcess >= 1:
	if preProcess == 2:
		start = 0;
		print("Start set to 0");
	for line in file:
		if line.split()[0] == "POSITIVE" or line.split()[0] == "SPAM":
			label = "+1";
		else:
			label = "-1";
		output.write(label);
		words = line.split();
		tempDict = dict();
		keys=[];
		for i in range(start,len(words)):
			key = words[i].split(":")[0];
			freq = words[i].split(":")[1];
			keys.append(int(key));
			tempDict[int(key)] = int(freq);
		keys.sort();
		for key in keys:
			output.write(" "+str(key+1)+":"+str(tempDict[key]));
		output.write("\n");

else:
	# We are doing post processing here. 
	# The third command line argument has to be given at this point
	if len(sys.argv)!=4 and len(sys.argv)!=5:
		print("Please provide the third command line argument");
		sys.exit();

	label = sys.argv[3];
	name = "";
	if label == "POSITIVE":
		name = "sentiment.svm.output";
	elif label == "SPAM":
		name = "spam.svm.output";
	if len(sys.argv) == 5:
		name = "labelsOnly1.txt";
	output1 = open(name,"w",encoding = "latin1");
	label = sys.argv[3];
	for line in file:
		if float(line.split()[0].split("\n")[0]) > 0:
			if label == "SPAM":
				output1.write("SPAM\n");
			else:
				output1.write("POSITIVE\n");
		else:
			# If it comes here, then it means it is less than zero.
			if label == "SPAM":
				output1.write("HAM\n");
			else:
				output1.write("NEGATIVE\n");




