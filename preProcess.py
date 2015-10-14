
import sys;
from os import walk,getcwd;
numArgs = len(sys.argv);

featureFile = sys.argv[1];
vocabFileName = sys.argv[2];


vmap = dict();

f = open(featureFile, "r", encoding = "latin1");
f2 = open ("modifiedFeatureFile", "w");
outputName = "";

if sys.argv[len(sys.argv)-1] == "1":
	outputName = "test_mails.feat"
	print("Naming the output file as test_mails.feat as this is the unlabeled data");
else:
	outputName = "labeledBow2.feat"; 
output = open(outputName,"w", encoding="latin1");
vocab = open(vocabFileName,"r", encoding = "latin1");

for line in f:
	listLine = line.split(" ");
	review=" ";
	rating=line.split()[0];
	if int(rating)>=7:
		review = "POSITIVE";
	elif int(rating)<=4:
		review = "NEGATIVE";

	for i in range(0,len(listLine)):
		if i==0:
			f2.write(review+" ");
		else:
			tempSpilt = listLine[i].split(":");
			f2.write(str(int(tempSpilt[0]))+":"+tempSpilt[1]);
			if i!=len(listLine)-1:
				f2.write(" ");

# Store all the vocab in a dictionary
count = 0;
for token in vocab:
	#print(token);
	vmap[str(token.split("\n")[0])] = count;
	count+=1;

#print("Vocab count = "+str(len(vmap.keys())));

#for word in vmap.keys():
	#print(word);

print("HERE:"+str(numArgs));
label = "";
space = "";
test = 0;
valid = 0;
for i in range(3,numArgs-1):
	curdir = parentdir = sys.argv[i];
	print("FOR:",curdir);
	for (dirpath, dirnames, filenames) in walk(curdir):
		if dirpath.split("/")[len(dirpath.split("/"))-1]=="ham":
			label="HAM";
			space = " ";
			valid = 1;
		elif dirpath.split("/")[len(dirpath.split("/"))-1]=="spam":
			label = "SPAM";
			space = " ";
			valid = 1;
		else:

			valid = 1;
			test = int(sys.argv[numArgs-1]);
		if valid ==1:	
			filenames.sort();
			for file in filenames:
				if file != ".DS_Store" and file != "Summary.txt" and file!="._.DS_Store":
					if test == 1:
						space = "";
					else:
						space = " "; 
					fileToOpen = getcwd()+"/"+dirpath+"/"+file;
					#print(getcwd()+dirpath+"/"+file);
					output.write(label); # Becaue each file corresponds to one line of output. 
					handler = open(fileToOpen, "r", encoding = "latin1");
					#print(fileToOpen);
					tempdict = dict();
					for line in handler:
						words = line.split();
						for word in words:
							#print(word);
							if word in vmap.keys():
								if int(vmap[word]) in tempdict.keys():
									tempdict[int(vmap[word])] += 1; #Means that it has already occured in this sentence
								else:
										#print("added");
									tempdict[int(vmap[word])] = 1;	# Means that it is the first time we are seeing this word. 
					for key,value in tempdict.items():
						output.write(space+str(key)+":"+str(value));
						if space != " ":
							space = " ";
					output.write("\n");
					valid = 0;

f2.close();





			
		#if(os.getcwd() == "ham")
		


	#f2.write("\n");   # Where is the extra '/n' coming from?
