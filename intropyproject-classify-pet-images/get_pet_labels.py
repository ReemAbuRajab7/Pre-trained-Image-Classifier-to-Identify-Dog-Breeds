#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Reem Abu Rajab
# DATE CREATED: Nov 13 2024                                  
# REVISED DATE: 
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
    # Create a list of files in the directory
    in_files = listdir(image_dir)
    
    # Create an empty dictionary to store results
    results_dic = dict()
   
    # Iterate through each file to extract the pet label
    for idx in range(0, len(in_files), 1):
       
       # Skip files that start with . (like .DS_Store)
       if in_files[idx][0] != ".":
           
           # Extract the pet label from the filename
           pet_label = in_files[idx].split('_')[0].lower().strip()
           
           # Add the pet label to the dictionary if the file isn't a duplicate
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", in_files[idx])
 
    # Return the results dictionary
    return results_dic

