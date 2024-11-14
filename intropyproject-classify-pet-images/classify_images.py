#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Reem Abu Rajab
# DATE CREATED: Nov 13 2024                                
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
import os
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images and compares classifier labels to pet labels.
    Adds classifier labels and comparison results to the results_dic.
    """
    for key in results_dic:
        # Use the classifier function to get the model label
        model_label = classifier(images_dir + key, model)

        # Process the model_label (convert to lowercase and strip whitespace)
        model_label = model_label.lower().strip()

        # Define the truth (pet image label)
        truth = results_dic[key][0]

        # Check if the pet label matches the classifier label
        if truth in model_label:
            results_dic[key].extend([model_label, 1])  # Add classifier label and match (1)
        else:
            results_dic[key].extend([model_label, 0])  # Add classifier label and no match (0)
None