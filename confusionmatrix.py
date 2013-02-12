#
# CRF++ crf_test result confusion matrix
# author: bryanyuan2
# date: 20130212
#

#
# 	confusion_matrix_print_func
#


from __future__ import division
import sys

__author__ = "bryanyuan2"
__email__ = "bryanyuan2@gmail.com"

correct_label_pool = ["I-NP","B-NP","B-ADJP","I-ADJP"]

def confusion_matrix_print_func(correct_label_pool,full_confusion_matrix_const, full_confusion_matrix, precision_label_pool, recall_label_pool, accuracy_of_all_data):
	
	#	ary[actual class][predicted class]
	#
	#   table				[predicted class]
	#
	#	[actual class]

	#print full_confusion_matrix

	total_data = 0
	correct_data = 0

	print "====\nConfusion Matrix\n===="
	print del_synbol_const + del_synbol_const,
	for i in range (0,len(correct_label_pool)):
		print correct_label_pool[i] + del_synbol_const,
	print " [predicted class]"

	#correct_label_pool[i/len(correct_label_pool)]
	for i in range (0,len(full_confusion_matrix)):
		if (i%len(correct_label_pool)==0):
			print correct_label_pool[int(i/len(correct_label_pool))] + str(del_synbol_const) + str(del_synbol_const),

		# precision_label_pool
		precision_label_pool[int(i%len(correct_label_pool))] = precision_label_pool[i%len(correct_label_pool)] + full_confusion_matrix[i]
		# recall_label_pool
		recall_label_pool[int(i/len(correct_label_pool))] = recall_label_pool[int(i/len(correct_label_pool))] + full_confusion_matrix[i]
		# total_correct_data
		total_data = total_data + full_confusion_matrix[i]

		print str(full_confusion_matrix[i]) + del_synbol_const,
		if ((i+1)%len(correct_label_pool)==0):
			print ""
	print "[actual class]"
	
	print "\n====\n(Precision, Recall, F1 score)\n===="
	for i in range(0,len(precision_label_pool)):
		#print precision_label_pool[i] 
		curr_id = i*(len(correct_label_pool)+1)
		correct_data = correct_data + full_confusion_matrix[curr_id]
		precision_label_pool[i] =  full_confusion_matrix[curr_id] / precision_label_pool[i]
		recall_label_pool[i] =  full_confusion_matrix[curr_id] / recall_label_pool[i]
		
		print correct_label_pool[i] + " = (" + str(precision_label_pool[i]) + ", " + str(recall_label_pool[i]) + ", " + str(2*precision_label_pool[i]*recall_label_pool[i]/(precision_label_pool[i]+recall_label_pool[i])) + ")"
		
	print "Accuracy = " + str(correct_data/total_data)

#
#
#

precision_label_pool = []
recall_label_pool = []
accuracy_of_all_data = 0
del_synbol_const = "\t"

#
#
#
full_confusion_matrix_const = []
full_confusion_matrix = []

# initialize confusion_matrix
for i in range(0,len(correct_label_pool)*len(correct_label_pool)):
	full_confusion_matrix.append(0)
	
#print full_confusion_matrix

# initialize full_confusion_matrix_const
for i in range(0,len(correct_label_pool)):
	precision_label_pool.append(0)
	recall_label_pool.append(0)
	for j in range(0,len(correct_label_pool)):
		full_confusion_matrix_const.append(correct_label_pool[i] + "_" + correct_label_pool[j])

#print precision_label_pool
#print recall_label_pool

for line in sys.stdin:
	if not line:
		break
	else:
		if (line.replace("\n","")!=""):
			data = line.replace("\n","").split("\t")
			curr_correct_answer = data[len(data)-2]
			curr_guess_label = data[len(data)-1]

			for j in range(0,len(full_confusion_matrix_const)):
				if (full_confusion_matrix_const[j] == curr_correct_answer + "_" + curr_guess_label):
					full_confusion_matrix[j] = full_confusion_matrix[j] + 1


confusion_matrix_print_func(correct_label_pool,full_confusion_matrix_const, full_confusion_matrix, precision_label_pool, recall_label_pool, accuracy_of_all_data)