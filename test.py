from crf_confusion_matrix_class import crf_confusion_matrix_class

def main():

	correct_label_pool = ["I-NP","B-NP","B-ADJP","I-ADJP"]
	crf_test_result_filename = "crf_test_result"
	
	test = crf_confusion_matrix_class(correct_label_pool, crf_test_result_filename)
	
	# confusion_matrix_print_func
	test.confusion_matrix_print_func()

	# crf_result_correct_and_wrong_file_mapping
	#test.crf_result_correct_and_wrong_file_mapping()

if __name__ == "__main__":
    main()