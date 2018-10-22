################################################################################
# PART #1 #worked with Hannah and Marissa 
################################################################################
import string 
import csv
import os 
from os import listdir 
import json 


def countWordsUnstructured(filename):
    #wordcount = {}
    #file = open(filename)
    #for word in file.read().split():
        #if word not in wordcount: 
            #wordcount[word] = 1 
        #else: 
            #wordcount[word] += 1
    #print (word,wordcount)
    #file.close();
    
    #initialize a word count dictionare
    wordCounts = {}
    #step 1 - open the file & read it 
    
    datafile = open(filename).read()
    #step 3 - split out into words 
    data = datafile.split()
    #step 4 - count it 
    for word in data:
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word in wordCounts:
            wordCounts[word] = wordCounts[word] + 1
        else:
            wordCounts[word] = 1
    #step 5 - return word count dictionary 
    return wordCounts
    
    
    
    
        
    #return the word count dictionary 
        #return wordCounts 
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
# Test your part 1 code below.
bush1989 = countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
print (bush1989)

################################################################################
# PART 2 #worked with Hannah and Marissa 
################################################################################
#import CSV 

#with open('taret_file.csv' , 'w') as csv_file:
    #writer = csv.writer(csv_file)
    #writer.writerow(('column 1, column 2, column 3'))
    #for key, value in dictionary.items():
        #writer.writerow([key, value[0],value[1]])
    
def generateSimpleCSV(targetfile,wordCounts):
    #def generateSimpleCSV(targetfile, wordCounts): 
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
    #open the file 
    with open (targetfile, 'w') as csv_file:
    
    #print the headers 
        writer = csv.writer(csv_file)
        writer.writerow(['Word', 'Count'])
        
        for key,value in wordCounts.items():
            writer.writerow([key, value])
    
    #iterate through the word counts 
    
        #add to our CSV file 
        
    #close the file 
    csv_file.close()
    
    
    
    #return pointer to the file 
    
    return csv_file
    
    
# Test your part 2 code below
generateSimpleCSV('pleasepleasework', countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')) 
################################################################################
# PART 3 #worked with Hannah and Marissa 
################################################################################
#def countWordsMany(directory): 
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
    
    
#open the directory pull a list of all file names 
def countWordsMany(directory):
        
        #open the directory and pulling list of name files 
        directory_list = listdir(directory)
        
        
        wordCountDict = {}
        
        #looping through the list of files, for each file you call the word counts function 
        for file in directory_list:
            eachWordCount = countWordsUnstructured(directory + "/" + file )
            
            
            wordCountDict[file] = eachWordCount
            
            
        return wordCountDict 
    
    


    
    
    
# Test your part 3 code below

big_dictionary = countWordsMany('./state-of-the-union-corpus-1989-2017')
    
print(big_dictionary)

################################################################################
# PART 4 #worked with Hannah and Marissa 
################################################################################
#def generateDirectoryCSV(wordCounts, targetfile): 

def generateDirectoryCSV(wordCounts, targetfile):
    
    
    #open file as csv 
    
    with open(targetfile, 'w') as csv_file: 
        
        #create the csv 
        writer = csv.writer(csv_file)
        
        #make the header row 
        writer.writerow(['Filename','Word','Count'])
        
        #iterate the word counts and write them into csv  
        for key,value in wordCounts.items():
            writer.writerow([key, value])
            
   
    #close the csv 
    csv_file.close()
    
    #return the file 
    return csv_file

    
    
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below

generateDirectoryCSV(countWordsMany('state-of-the-union-corpus-1989-2017'), 'part4CSV')
    
################################################################################
# PART 5 # worked with hannah and marissa and Steven 
################################################################################
#def generateJSONFile(wordCounts, targetfile): 

    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
def generateJSONFile(wordCounts, targetfile):
    
    #opens the file 
    JSON_file = open(targetfile, "w")
    
    #trasnform the word count directory to json 
    JSON_file.write(str(wordCounts).replace("\'","\""))
    
    # close the file 
    JSON_file.close()
    
    #return file 
    return JSON_file 


    
  


    
    
    
# Test your part 5 code below
generateJSONFile(big_dictionary, "part5file")

################################################################################
# PART 6 #worked with Jacob, Hannah and Marissa 
################################################################################
def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
    #set the variables to use 
    largest_count_file = ""
    largest_count = 0 
    
  
    #open the csv file 
    with open(csvfile) as csv_file:
        file = csv.reader(csv_file)

   
    #make a for loop to find the filename with the largest count of a specified word  
        for line in file: 
        
        #finds which line has largest count 
        #if the 2nd value in the line is the word we are looking for an dlarger 
            if line[1] == word and int(line[2]) > int(largest_count): 
                largest_count = line[2]
                largest_count_files = line[0]
                
    #return the file 
    return largest_count_file 
            
    
    #close the file 
    csv_file.close()
        

    
def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
    #set the variable 
    largest_count_file = ""
    largest_count = 0 
#open the json file 
    with open(JSONfile) as json_file: 
        data = json.load(json_file)
        
        # make a loop for finding the file that has the highest count fot that word
        for file in data: 
            if data[file][word] > largest_count:
                largest_count = data[file][word]
                largest_count_file = file
                
    #return the file 
    return largest_count_file
    
    #close the file 
    json_file.close()
    
print(searchCSV("part4CSV", "and"))
print(searchJSON("part5file","and"))
    
    
            
            
            
#make a search for words  

    
    #search the file by filename to find the largest value 
    #max_count = max(jsonFile['Count'])


#return the highest values filename 

#close file 
    #jsonFile.close()
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value



###############################################################################
#PART 7 #worked with Hannah and Marissa and Jacob 
###############################################################################









#import sqlite3 


#set up a connection to the database 

#conn = sqlite3.connect('presidents_speech.db')
#c = conn.cursor()

#ask the connection to execute SQL statement 
#c.execute('''CREATE TABLE word_counts ( filename, word, count)''')
#c.execute('''CREATE TABLE presidentInformation (index, number, start, end, president_name, prior occupation, party, VP)''')

#the table could be joined on president name or year of presidency 

#  Table 1 wordCounts
    #text filename 
    #text word 
    # number(integer) count 
    
# Table 2 - pres information 
    #integer index  
    #integer number 
    # text start 
    # text end 
    # text president_name 
    # text prior occupation 
    # text party 
    # text VP 


#save (commit) the changes 
#conn.commit()

#close the connection 
#conn.close() 
