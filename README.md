"Einfald myndgreining á LeNet

1) Installtion 

	Python 3
	Keras
	TensorFlow 
	Numpy 

2) Driver 

	-cudnn
	-cuda

3) Data of Images 
	Icelandic Flag

	train = 100
	test = 20
	total = 120 (20% for test /80% for train) 

4) Train.py 
	Þjálfa myndum í deep learning og býr módel til.

	python3 train.py --model fani.model --dataset data

5) Test.py 
	Keyra á OpenCV með mynd og láta að þekkja íslenska fána.

	python3 test.py --model fani.model --image data/IcelandicFlag/image01.jpg 