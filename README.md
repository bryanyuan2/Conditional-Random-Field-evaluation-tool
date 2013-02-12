**Intro**

A python class for CRF++ Confusion Matrix and their Precision, Recall, F1 score

CRF++: Yet Another CRF toolkit (http://crfpp.googlecode.com/svn/trunk/doc/index.html)

**Example Result**


Confusion Matrix

		I-NP		B-NP	B-ADJP	I-ADJP	 [predicted class]
I-NP		5440	130		3		1	
B-NP		420		4563	2		0	
B-ADJP		30		47		48		2	
I-ADJP		36		7		13		6	
[actual class]


(Precision, Recall, F1 score)

I-NP = (0.917988525143, 0.975959813419, 0.946086956522)
B-NP = (0.961238677059, 0.915346038114, 0.937731196054)
B-ADJP = (0.727272727273, 0.377952755906, 0.497409326425)
I-ADJP = (0.666666666667, 0.0967741935484, 0.169014084507)
Accuracy = 0.935708969111