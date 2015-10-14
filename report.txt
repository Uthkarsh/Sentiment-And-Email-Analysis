Calculations :
----------------------------------------------------------------------------------------------
Naive Baye's :
------------
Sentiment Analysis :
------------------

case 1 :

Learning % : 75
Test % : 25

	POSITIVE Label : 
						Precision : 0.8736948467497474
						Recall :	0.8167506297229219
						F Score :	0.8442636289666395

	NEGATIVE Label :    Precision :	0.8226150563852483
						Recall :	0.8780091086532206
						F Score :	0.8494099134539731


Case 2 :

Learning % : 25
Test % : 75

	POSITIVE Label	:
						Precision:  0.8653038046564452
						Recall	:	0.8093265349479498
						F Score :	0.8363796037104122

	NEGATIVE Label	:
						Precision:	0.8195072900955254
						Recall	:	0.8729648671808055
						F Score	:	0.8453918365230019

Email Analysis : 
--------------

case 1 :

Learning % : 75
Test % : 25

	SPAM Label : 
						Precision :	0.9891618497109826
						Recall :	0.9771591720199857
						F Score :	0.9831238779174147

	HAM Label :   		Precision :	0.9770032339202299
						Recall :	0.9890869407057111
						F Score :	0.9830079537237888


Case 2 :

Learning % : 25
Test % : 75

	SPAM Label	:
						Precision:	0.9861499210302515
						Recall	:	0.9781875150638708
						F Score :	0.9821525803133886

	HAM Label	:
						Precision:	0.9785086677748753
						Recall	:	0.9863554757630162
						F Score	:	0.9824164034094296


SVM : 
-----

Sentiment Analysis :
------------------

case 1 :

Learning % : 75
Test % : 25

Precision for POSITIVE = 0.8623507228158391
Precision for NEGATIVE = 0.886245110821382
Recall for POSITIVE = 0.8871645651471064
Recall for NEGATIVE = 0.8612606905289832
F score for POSITIVE = 0.8745816733067729
F score for NEGATIVE = 0.873574297188755


Case 2 :

Learning % : 25
Test % : 75

	NEGATIVE Label	:
						Precision:  0.8653038046564452
						Recall	:	0.8093265349479498
						F Score :	0.8363796037104122

	POSITIVE Label	:
						Precision:	0.8195072900955254
						Recall	:	0.8729648671808055
						F Score	:	0.8453918365230019

Email Analysis : 
--------------
Learning % : 75
Test % : 25

case 1 :

Precision for HAM = 0.9929078014184397
Precision for SPAM = 0.9303020245602389
Recall for HAM = 0.9230769230769231
Recall for SPAM = 0.9936192839418646
F score for HAM = 0.9567198177676539
F score for SPAM = 0.9609187521426122

Case 2 :

Learning % : 25
Test % : 75

Precision for HAM = 0.9891055817081372
Precision for SPAM = 0.9005207203297896
Recall for HAM = 0.889130697618184
Recall for SPAM = 0.9903364352183249
F score for HAM = 0.9364574048134471
F score for SPAM = 0.9432954545454546

MEGAM : 
-----
Sentiment Analysis :
------------------

case 1 :

Learning % : 75
Test % : 25

Precision for HAM = 0.875919411576591
Precision for SPAM = 0.8658341338456612
Recall for HAM = 0.8673210892970235
Recall for SPAM = 0.8745148771021992
F score for HAM = 0.8715990453460621
F score for SPAM = 0.8701528559935638


Learning % : 25
Test % : 75

Case 2 :

Precision for HAM = 0.8618760757314974
Precision for SPAM = 0.8524434101967421
Recall for HAM = 0.8517061762517274
Recall for SPAM = 0.8625709087017018
F score for HAM = 0.8567609474415869
F score for SPAM = 0.8574772570090972


Email Analysis : 
--------------
Learning % : 75
Test % : 25

Precision for HAM = 0.9724284199363733
Precision for SPAM = 0.9845701689933872
Recall for HAM = 0.9849624060150376
Recall for SPAM = 0.971718636693256
F score for HAM = 0.9786552828175026
F score for SPAM = 0.9781021897810219


Case 2 :

Learning % : 25
Test % : 75

Precision for HAM = 0.9635750029093448
Precision for SPAM = 0.9859801488833747
Recall for HAM = 0.986536399380436
Recall for SPAM = 0.9621065375302663
F score for HAM = 0.9749205227834687
F score for SPAM = 0.9738970588235294


-----------------------------------------------------------------------------------------------

Comments :


Answers to Questions
-----------------------------------------------------------------------------------------------

1 & 2) For 75 training and 25 testing
   Sentiment Analysis : 

   If we do the performance comparision based on F Scores, then, 

   			Sentiment Analysis				|		SPAM Detection
-----------------------------------------------------------------------
  			POSITIVE 	|	NEGATIVE 		|		SPAM  |	HAM 
-----------------------------------------------------------------------
   75:25	MEGAM and SVM perform equally well		Naive Bayes

   25:75	MEGAM 									Naive Bayes
-----------------------------------------------------------------------


-As can be seen above, for both the splits, MEGAM does well with respect to POSITIVE/NEGATIVE (both labels). 

-SVM seems to perform equally well for the POSITIVE/NEGATIVE with 75:25 split, and just below MEGAM for 25:75 split. 

- For SPAM Detection, for both kind of splits, Naive Bayes seems to be performing the best among the three algorithms. 

- Although MEGAM seems to be performing well for 25:75 split (SPAM detection), it is found to be unstable. When run for 3-4 times consecutively, there seems to be drastic changes in values for certain runs. I think this is mainly due to the small training set compared to the testing set (75%) given to the toolkit. 

- Naive Bayes seems to working surprisingly well for all the splits and cases -- sentiment and SPAM -- even though it treats each word independently. 


------------------------------------------------------------------------------------------------

Commands to be run :
--------------------

1) Method How Pre-Processing for Naive Bayes is done :
---------------------------------------------------


python3 preProcess.py labeledBow.feat enron.vocab enron1 enron2 enron4 enron5 0

Description : -This script does the preprocessing of the files to be converted to the data format. 
			  Arguments : 
			  -The sentiment features file with the IMDB ratings which has to be converted to POSITIVE/NEGATIVE.
			  - The enron vocabulary files.
			  -The four enron directories that have to be preprocessed (Variable number of arguments depending upon the number of directories to be preprocssed).
			  -0 or 1, depending upon if the directories for SPAM/HAM are labeled or not. If it is 1, then the preprocessing is for the unlabelled test directory. 


For the test data, you can run it as :

python3 preProcess.py labeledBow.feat enron.vocab spam_or_ham_test 1

Description : -Here, the spam_or_ham_test is the directory that contains all the test emails to be 				  processed. 
			  - The last argument is 1, indicating that this is supposed to be unlabeled data. 
			  - Other arguments are same as described previously. 
Output files : 
-------------
The labeled sentiment feature file is named as : modifiedFeatureFile
The labeled enron* is named as : labeledBow2.feat (When the last argument is sent as 0)

When the last argument is sent as 1 (for the unlabeled data -- spam_or_ham_test directory), then the output file will be named as test_mails.feat


This is just a matter of choice, could have made them command line arguments. 


2) Data Splitting Script into different percentages and algorithms
------------------------------------------------
Ex :

python3 datasplit.py modifiedFeatureFile .75 1 SVM
python3 datasplit.py MEGAMInput.feat .75 1 MEGAM
python3 datasplit.py labeledBow.feat.feat .75 0

Description : 
------------
- First argument is the labeled feature file that has to be split into training and test data.
- The second argument is the ration in which the split has to happen. Ex: .75 indicates, 75% 		  Trainging and 25% Test data. 
- Argument 3 indicates whether the generated test file should hae sudo-labels (as required for SVM and MEGAM) or not. If it is 1, it indicates yes.
- IF the previous argument is 1, then this has to be specified as either SVM or MEGAM, based on which the sudo labels would be +1/0 as required by SVM and MEGAM respectively. 

Generated file names : genTraining.txt, generatedTest.txt, labelsOnly.txt -- Which is the correct labels for the generatedTest.txt. This will be used by the calculations script. 


3) Calculations of Precisions, Recalls and F-Scores :
--------------------------------------------------

Ex :

python3 calculations.py sentiment.nb.out labelsOnly.txt

Description :
------------
- The first argument will be the output file with only the labels (Classified)
- The second file is the labelsOnly.txt file got from the datasplit.py script. 


OPTIONAL Shell script for the process :
-------------------------------------

There is a shell script to automate the entire process -- from preprocessing the enron* directories and the sentiment file to the calculation of statistics. 

Ex : sh naiveBayes.sh 0.25 modifiedFeatureFile sentiment.nb

Description : 

- The first argument is the split of the data
- The second argument is the file to be split
- Third is the name of the model and output files (That has to be named)

Assumptions : Everything is expected to be in the current working directory (The python and the shell scripts).

----------------------------------------------------------------------------------------------------

SVM :
----

Pre and Post processing for the purpose of converting project data format to SVM format and vice versa :

Ex :

python3 processInputSVM.py labeledBow2.feat 1

Description : The first argument is the labeled file that has to be preprocessed to the SVM data format, and the second argument indicates whether it is pre or post processing. If it is 1, it means pre - processing, Postprocessing, if it is 0. 

If the second argument is 0 (Post Processing) , then the input file has to be in the SVM data format. 

Ex :

./svm_learn genTraining.txt modelfile
./svm_classify generatedTest.txt modelfile RESULTS.txt




There is an OPTIONAL shell script to automate the process :
----------------------------------------------------------

sh svm.sh modifiedFeatureFile .75 POSITIVE

- Argument 1 : The file to be split
- Argument 2 : The split 
- Argument 3 : POSITIVE/SPAM Either of these two depending on the type of features file. 

For the splits, the calculated scripts are stored (redirected by the shell script) to a file called statistics.txt

 -- sh svm.sh help 

Will give you the exact usage of the command. 

**ASSUMPTION : All the python scripts, SVM binaries and the shell scripts/files are expected to be in the same directory. 

Ex : sh svm.sh labeledBow.feat .75 POSITIVE
	 sh svm.sh modifiedFeatureFile 1 SPAM testing_mails.feat
     sh svm.sh modifiedFeatureFile 1 POSITIVE sentiment_test.feat

     // If the split is 1, then it means that is the test data, so you will send the test file as the last argument.

MEGAM :
----

Pre and Post processing for the purpose of converting project data format to MEGAM format and vice versa :

Ex :

python3 processInputMegaM.py labeledBow2.feat 1

Description : The first argument is the labeled file that has to be preprocessed to the MEGAM data format, and the second argument indicates whether it is pre or post processing. If it is 1, it means pre - processing, Postprocessing, if it is 0. 

If the second argument is 0 (Post Processing) , then the input file has to be in the MEGAM data format.

Steps used for running MEGAM :

Ex :

 ./megam_i686.opt -fvals binary genTraining.txt > weights_b

echo "Predicting from MEGAM.."
./megam_i686.opt -fvals -predict weights_b binary generatedTest.txt > RESULTS.txt

There is an OPTIONAL shell script to automate the process :
----------------------------------------------------------

sh megam.sh modifiedFeatureFile .75 POSITIVE

- Argument 1 : The file to be split
- Argument 2 : The split 
- Argument 3 : POSITIVE/SPAM Either of these two depending on the type of features file. 

For the splits, the calculated scripts are stored (redirected by the shell script) to a file called statistics.txt

 -- sh megam.sh help 

Will give you the exact usage of the command. 

**ASSUMPTION : All the python scripts, MEGAM binary and the shell scripts/files are expected to be in the same directory. 

Ex : 

sh megam.sh labeledBow.feat .75 POSITIVE
sh megam.sh modfiedFeatureFile 1 POSITIVE sentiment_test



--------------------------------------------------------------------------------------------------

ASSUMPTION :
----------

All the scripts assume that the required files for each script are in the same directory. 
-----------------------------------------------------------------------------------------







