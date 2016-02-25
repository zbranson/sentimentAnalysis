#!/bin/sh

cd /N/u/atremukh/Karst/A3;
module load timbl/6.4.2;

#base case

timbl -f interest.newtrain.txt -t interest.newtest.txt 		> interest_output.txt; 		 	#0.634409
timbl -f difficulty.newtrain.txt -t difficulty.newtest.txt 	> difficulty_output.txt;  		#0.434783
timbl -f arm.newtrain.txt -t arm.newtest.txt 				> arm_output.txt;               #0.842105

#case 1 - k-NN with different distances & feature weighing schemes for varying k values

rm -rf *.out;

for counter in 1 3 5 7 9 11 13 15
do
	for distance in `cat dist.txt`
	do
		for weights in {0..4}
		do
				timbl -f "interest.newtrain.txt" -t "interest.newtest.txt" 	-k $counter -m $distance -w $weights > $counter"_"$distance"_"$weights"_interest_output.out"; 
				#tail -5  $counter"_interest_output.out" > $counter"_interest_output.txt";		 	
				timbl -f "difficulty.newtrain.txt" -t "difficulty.newtest.txt" 	-k $counter -m $distance  -w $weights  > $counter"_"$distance"_"$weights"_difficulty_output.out";  		
				#tail -5  $counter"_difficulty_output.out" > $counter"_difficulty_output.txt";
				timbl -f "arm.newtrain.txt" -t "arm.newtest.txt" 				-k $counter -m $distance   -w $weights > $counter"_"$distance"_"$weights"_arm_output.out";   
				#tail -5  $counter"_arm_output.out" > $counter"_arm_output.txt";

		done;
	done;
done;            

grep "overall accuracy:" *_output.out > overall_accuracies_3words.txt;

grep "interest" overall_accuracies_3words.txt > overall_accuracies_interest.txt;
grep "difficulty" overall_accuracies_3words.txt > overall_accuracies_difficulty.txt;
grep "arm" overall_accuracies_3words.txt > overall_accuracies_arm.txt;

#manual one in other

for algo in {0..4}
do
	for q_val in {1..15}
	do
		for weights in {0..4}
		do
			for w_n_f_d in `cat wt_nghbr_func_dist.txt`
			do
				for TO in `cat Treeorder.txt`
				do
					timbl -f "interest.newtrain.txt" -t "interest.newtest.txt" 		-a $algo  -w $weights	-d $w_n_f_d	--Treeorder=$TO	> $algo"_""_"$weights"_"$w_n_f_d"_"$TO"_interest_output.out";	
					timbl -f "difficulty.newtrain.txt" -t "difficulty.newtest.txt" 	-a $algo  -w $weights	-d $w_n_f_d	--Treeorder=$TO	> $algo"_""_"$weights"_"$w_n_f_d"_"$TO"_difficulty_output.out"; 
					timbl -f "arm.newtrain.txt" -t "arm.newtest.txt" 				-a $algo  -w $weights	-d $w_n_f_d	--Treeorder=$TO	> $algo"_""_"$weights"_"$w_n_f_d"_"$TO"_arm_output.out"; 
				done;
			done;
		done;
	done;	
done;	
	
	
	
	
	
	
	