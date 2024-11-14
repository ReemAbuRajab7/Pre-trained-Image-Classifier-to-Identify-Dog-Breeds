#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Reem Abu Rajab
# DATE CREATED: Nov 13 2024                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments.
    """
    # Creates parser
    parser = argparse.ArgumentParser()

    # Creates 3 command line arguments args.dir, args.arch, args.dogfile
    parser.add_argument('--dir', type=str, default='/home/reem/Downloads/AIPND-revision-master/intropyproject-classify-pet-images/pet_images/', 
                        help='path to folder of images')
    # Added help and type for the CNN architecture and dog names file
    parser.add_argument('--arch', type=str, default='vgg', 
                        choices=['vgg', 'alexnet', 'resnet'], 
                        help='CNN model architecture to use for classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Text file with the names of dog breeds')

    # Parse the arguments and return them
    return parser.parse_args()

