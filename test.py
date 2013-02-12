from crf_confusion_matrix_class import crf_confusion_matrix_class

def main():

	correct_label_pool = ["I-NP","B-NP","B-ADJP","I-ADJP"]
	filename = "final"
	
	test = crf_confusion_matrix_class(correct_label_pool, filename)
	test.confusion_matrix_print_func()

if __name__ == "__main__":
    main()