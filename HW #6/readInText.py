#!/usr/bin/python
import fileinput 
import string
import numpy

def readInText():


	file = open("data_string_1.txt", 'r') 
	text = file.readlines()


	print text
	
	file.close()

def main():

	readInText()
	print("finished")