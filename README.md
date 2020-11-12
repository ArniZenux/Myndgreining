"Einfald myndgreining" 

0) Pre-installation
		
	Athuga hvort skjákort sé á GPU eða ekki.
	https://www.howtogeek.com/414201/how-to-check-what-graphics-card-gpu-is-in-your-pc/

	Þarf að setja CUDA og cuDNN í Windows eða Linux (Ubuntu / ArchLinux) áðan en hefst að nota Deep Learning stuff. Nauðsynlegt að athuga hvort skjákort sé GPU eða ekki. 
	https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781

1) Installation 
	
	Python 3
	Keras
	TensorFlow 
	Numpy 

	CPU
    python-m pip install -r requirements.txt 

	GPU
	python -m pip install -r requirements_gpu.txt


	https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781

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