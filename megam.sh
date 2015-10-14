# Argument 1 : File name Input to be slpit (labeledFeatureBow*)
# Argument 2 : Split Ration
# Argument 3 : "SPAM" or "POSITIVE"

# Example : sh megam.sh labeledBow.feat .75 POSITIVE
#           sh megam.sh modfiedFeatureFile 1 POSITIVE sentiment_test.sh

if [ $1 = "help" ]
	then
	echo "USAGE: sh megam.sh <TRAINING FILE(PDF)> <SLPIT RATIO> <POSITIVE or SPAM> [file to be classified]"
	echo "The final argument is optional if the split ratio is 1, otherwise it takes generatedTest.txt from cwd"
	echo "sh megam.sh modfiedFeatureFile .75 POSITIVE
sh megam.sh modfiedFeatureFile 1 POSITIVE sentiment_test.sh";
	exit;
	
 fi
if [ $2 = 1 ]
	then
	echo "TRAINING 100% DATA"
	echo "Pre Processing"
	python3 processInputMegaM.py $1 1
	cp MEGAMInput.feat MEGAMPreProcessedFeat.feat
	echo "Learning.."	
	weights_b=""
	if [ $3 = "SPAM" ]
		then 
		weights_b="spam.megam.model";
	else
		weights_b="sentiment.megam.model";
	fi;
	./megam_i686.opt -fvals binary MEGAMInput.feat > $weights_b
	echo "Classifying.."
	# Assume a 4th argument for classification
	python3 processInputMegaM.py $4 2
	./megam_i686.opt -fvals -predict $weights_b binary MEGAMInput.feat > RESULTS.txt
	python3 processInputMegaM.py RESULTS.txt 0 $3
	exit;
fi;
echo "Processing Input.."
python3 processInputMegaM.py $1 1

echo "Splitting Data.."
python3 datasplit.py MEGAMInput.feat $2 1 MEGAM

echo "Learning from MEGAM.."
./megam_i686.opt -fvals binary genTraining.txt > weights_b

echo "Predicting from MEGAM.."
./megam_i686.opt -fvals -predict weights_b binary generatedTest.txt > RESULTS.txt

# Now Post Process this
echo "Processing the results .."
python3 processInputMegaM.py RESULTS.txt 0 $3
python3 processInputMegaM.py labelsOnly.txt 0 $3 8
name=`echo n` 
pos=`echo POSITIVE`
third=`echo $3`
echo "$third";

if [ "$third" = "$pos" ];
then 
name=`echo sentiment.megam.out`
else
name=`echo spam.megam.out`
fi

echo "Line Count:"
file=`echo labelsOnly1.txt`

#python3 ../processInputMegaM.py labelsOnly.txt 0 $3

diff $name $file | grep ">" | wc -l

python3 calculations.py $name labelsOnly1.txt > Statistics.txt;



# The output of this will be generatedTest.txt and genTraining.txt

