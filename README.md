# Introduction 
This repo is part of project submission for Udacity nano degree program "AI Programming with Python".
The purpose of the project is to use pre-trained image classifier to identify if the image is a dog and what breed of dog it is.


# Usage
The program can be run using the command `python check_images.py` in the terminal.
The program takes three arguments: `check_images.py [-h] [--dir DIR] [--arch ARCH] [--dogfile DOGFILE]`
1. Folder path to the images to be classified (default: pet_images/)
2. Architecture to be used for the classifier (default: vgg, options: vgg, alexnet, resnet)
3. File path to the text file containing the list of dog names (default: dognames.txt)

# Project Instructions for running the code in your local machine
1. Clone the repository to your local machine
2. Create a virtual environment and activate it
3. Install the dependencies using the command `pip install -r requirements.txt`
4. Run the command `python check_images.py` to run the program
