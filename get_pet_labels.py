#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ashraful Islam
# DATE CREATED:  6/17/23                                
# REVISED DATE: 6/24/23
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # get the list of files in the image directory
    in_files = listdir(image_dir)
    
    #create an empty results_dic dictionary
    results_dic = dict()
    
    #process the list of files and add images file names to the dictionary
    for filename in in_files:
        # if the file name starts with a dot (hidden files) then skip
        if filename[0] == ".":
            continue
        
        #empty string for storing pet label
        pet_label = ""
        #make everything lower case and split with underscore
        file_name_split = filename.lower().split('_')
        
        #add the split portion to pet_label if its alphabetic and not numbers
        for name_split in file_name_split:
            if name_split.isalpha():
                pet_label += name_split + " "
                
        #remove the trailing white space
        pet_label = pet_label.strip()
        
        # not sure why we need to check for duplicate but since its suggested in hints...
        # If filename doesn't already exist in dictionary add it and it's
        # pet label - otherwise print an error message because indicates 
        # duplicate files (filenames)
        if filename not in results_dic:
            #add it to dictionary
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Duplicate files exist in directory:", filename)
        
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
