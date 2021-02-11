import csv
def readDataFromCSVFile(filename):
    f = open(filename, newline='', encoding="utf-8")
    h = f.readline().strip().split(",")
    result = []
    for line in f.readlines():
        data = line.strip().split(",")
        result.append(makeDictionary(h, data))
    f.close()
    return result

def makeDictionary(key, vals):
   result ={}
   for i in range(len(key)):
       result[key[i]] = vals[i]
   return result

def dictionaryToListOfValues(k, dictionary):
    result = []
    for key in k:
        result.append(dictionary[key])
    return result

import csv
def writeDataToCSVFile(file,data,keysoflist,boolean):
    with open(file, 'w') as f:
     if boolean:
       f.write(",".join(keysoflist)+"\n")
       for i in data:
         result=[]
         for key in keysoflist:
           result.append(i[key])
           f.write(",".join(result)+"\n")
     




   