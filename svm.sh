# Argument 1 : File name Input to be slpit (labeledFeatureBow*)
# Argument 2 : Split Ration
# Argument 3 : "SPAM" or "POSITIVE"
# Argument 4 : Either testing_mails.feat or sentiment_test.feat or something else

# Example : sh svm.sh labeledBow.feat .75 POSITIVE
		  # sh svm.sh modifiedFeatureFile 1 SPAM testing_mails.feat
		   # sh svm.sh modifiedFeatureFile 1 POSITIVE sentiment_test.feat

if [ $1 = "help" ]
	then
	echo "USAGE: sh svm.sh <TRAINING FILE (PDF)> <SLPIT RATIO> <POSITIVE or SPAM> [file to be classified]"
	echo "The final argument is optional if the split ratio is 1, otherwise it takes generatedTest.txt from cwd"
	echo "Example:"
	echo "sh svm.sh modifiedFeatureFile .75 POSITIVE
sh svm.sh modifiedFeatureFile 1 SPAM testing_mails.feat
sh svm.sh modifiedFeatureFile 1 POSITIVE sentiment_test.feat"
	exit;
	
 fi

if [ $2 = 1 ]
	then
	echo "TRAINING 100% DATA"
	echo "Pre Processing"
	python3 processInputSVM.py $1 1
	echo "Learning.."	
	modelfile=""
	if [ $3 = "SPAM" ]
		then 
		modelfile="spam.svm.model";
	else
		modelfile="sentiment.svm.model";
	fi;
	./svm_learn SVMInput.feat $modelfile
	echo "Classifying.."
	python3 processInputSVM.py $4 2
	cp SVMInput.feat SVMInput
	# Assume there is a 4th argument and use it for the classification file
	./svm_classify SVMInput.feat $modelfile RESULTS.txt
	python3 processInputSVM.py RESULTS.txt 0 $3
	exit;
fi;

echo "Processing Input.."
python3 processInputSVM.py $1 1

echo "Splitting Data.."
python3 datasplit.py SVMInput.feat $2 1 SVM

echo "Learning from MEGAM.."
./svm_learn genTraining.txt modelfile

echo "Predicting from MEGAM.."
./svm_classify generatedTest.txt modelfile RESULTS.txt

# Now Post Process this
echo "Processing the results .."
python3 processInputSVM.py RESULTS.txt 0 $3
python3 processInputSVM.py labelsOnly.txt 0 $3 8
name=`echo n` 
pos=`echo POSITIVE`
third=`echo $3`
echo "$third";

if [ "$third" = "$pos" ];
then 
name=`echo sentiment.svm.output`
else
name=`echo spam.svm.output`
fi

echo "Line Count:"
file=`echo labelsOnly1.txt`

#python3 ../processInputMegaM.py labelsOnly.txt 0 $3

diff $name $file | grep ">" | wc -l

python3 calculations.py $name labelsOnly1.txt > Statistics.txt;



# The output of this will be generatedTest.txt and genTraining.txt

