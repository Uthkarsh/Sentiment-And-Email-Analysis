# arg1 = percenetage split
# arg2 = either modifiedFeatureFile or labeledBow2.feat
# arg3 = spam.nb or sentiment.nb
 # sh naiveBayes.sh 0.25 modifiedFeatureFile spam.nb
 # sh naiveBayes.sh 0.25 modifiedFeatureFile sentiment.nb

 # The fourth argument indicates if the test data must have labels. 


 echo "preprocesing..";
 python3 preProcess.py labeledBow.feat enron.vocab enron1 enron2 enron4 enron5 0;
 echo "splitting data";
 python3 datasplit.py $2 $1 0;
 echo "training the learner..";
 modelfile=`echo $3.model `
 python3 nblearn.py genTraining.txt $modelfile
 echo "Classifying the data";

 python3 nbclassify.py $modelfile generatedTest.txt > $3.out;
 echo "Calculating the results";
 python3 calculations.py $3.out labelsOnly.txt;