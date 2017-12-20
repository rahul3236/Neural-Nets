import network
import mnist_loader
import cv2
import pickle
import numpy as np
##########################################################################

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

##########################################################################

def train_network():
	net = network.Network([784, 30, 10])
	net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
	return net

##########################################################################

def convert_image(pixels):
	index=0
	newpixel=test_data[0][0]
	for i in range(28):
		for j in range(28):
			newp=str(pixels[i][j])
			newp=newp+'.0'
			newp=float(newp)
			newpixel[index][0]=1.0-(newp/255.0)
			index=index+1
	return newpixel

##########################################################################


def  show_image(im):
	image1=training_data[im][0]
	for i in range(784):
		if image1[i][0]>0:
			image1[i][0]=0
		else:
			image1[i][0]=255
	temp=np.ndarray([28,28],'float32')
	index=0
	for i in range(28):
		for j in range(28):
			temp[i][j]=image1[index][0]
			index=index+1
	cv2.imwrite("new.jpg",temp)

######################################################################
def test_image(ch):
	c=1
	tem=output_image(ch,c)
	show_image(ch)
	return tem
######################################################################

def custom_image(file3):
	c=2
	file2=cv2.imread(file3,0)
	pixels=convert_image(file2)
	tem=output_image(pixels,c)
	return tem
######################################################################

def output_image(pix,z):
	if z==1:
		value=net.feedforward(training_data[ch][0])
	else:
		value=net.feedforward(pix)
	index=0
	loc=0
	max=value[0][0]
	for i in range(9):
		if value[i][0]>max:
			max=value[i][0]
			loc=index
		index=index+1
	return loc
	
#####################################################################	
try:
	f=open("neuralnet.obj","r")
	net=pickle.load(f)
except IOError:
	net=train_network()
	f=open("neuralnet.obj","w")
	pickle.dump(f,net)
print "Enter 1 to test an image from the dataset\n"
print "Enter 2 for a custom image provided by you\n"
choice=int(raw_input("Enter your choice\n")) 
if choice==1:
	ch=int(raw_input("Enter a random number\n"))
	output=test_image(ch)
else:
	file1=raw_input("Enter file name with full path\n")
	output=custom_image(file1)
print "Output is " , output 




	
