

address = """
John Smith,
876 St Margarets Court,
Lawrence,
MA 01841
USA
"""
import spacy
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re 
from code import GetZipInfo             #importing other module in this module
from demo import AddressParse

class ParseAddress:

    results = {}                #empty list to store final result

    def find_person_name(self, lines):      #function to find person name
        nlp = spacy.load('en_core_web_lg')  #loading the package from spacy
        doc = nlp(lines)                    
        for ent in doc.ents:                #iterating through address lines
            if ent.label_ == 'PERSON':      #finding the label of the entities if label is PERSON then 
                print(ent, ent.label_)      #print person name


    def parse(self, address):  #function to parse the address lines
        address_lines = [line for line in address.split('\n') if line]  #split the address acc to new line
        zipobj = GetDetailsFromZip(address) #creating the object of class GetDetailsFromZip
        city, state, zipcode = zipobj.get_details_from_zip()  #calling the method to get all details and store
        print("city:"+city +"\n", "state:"+state + "\n", "zipcode:"+zipcode)
        o.find_person_name(address)     #function call to find person name
        demobj = AddressParse(address)  #creating object of the class in another module
        demobj.parse_street()       #call the method using that object

class GetDetailsFromZip:

    def __init__(self, address):
        self._address = address

    @property
    def address(self):
        return self._address

    def get_zipcode(self):
        address_list = [line for line in self.address.split('\n') if line]  #splitting the address by new line
        for i in range(len(address_list)-1,-1,-1):
            line = address_list[i]
            words = line.split(' ')
            for word in words: #to find zipcode in address
                if len(word) == 5 and word.isnumeric(): #if word length is 5 and its numeric then return zipcode
                    return word
                elif len(word) == 4 and word.isnumeric(): #if length of zipcode is 4 
                    word = "0" + word  #add one zero in the starting
                    return(word)

    def get_details_from_zip(self):
        zipcode = self.get_zipcode()    #calling the method and storing the returned values in zipcode
        zipobj = GetZipInfo()           #creating the object of the class of the module code.py
        
        zip = zipobj.get_info_from_zip(zipcode)  #method call by passing zipcode as argument
        city = zip['city']  #getting the value of city
        state = zip['state'] #getting the avlue of state
        zipcode = zip['zip_code'] #getting the value of zipcode
        return (city, state, zipcode)

o = ParseAddress()  #creating the object of the class
o.parse(address)    

