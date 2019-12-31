######################################################################
# Created By: Prashanth
# Purpose: Check if the AD group is present in the Domain
# Date: 31/12/2019
# Example of how to use the script:
# python adComparison.py <pathToADFromExcelFile> <pathToADFromDomain>
#######################################################################

import argparse
import csv 

def printLineBreaks(heading):
	print
	print
	print "************************************************************************"
	print heading
	print

def writeToFile(filePath, listToBeWritten):
	with open(filePath, "w") as output:
		writer = csv.writer(output, lineterminator='\n')
		for eachVal in listToBeWritten:
			writer.writerow([eachVal])
	print "Write Completed"
	print

parser = argparse.ArgumentParser()
parser.add_argument("adFromExcel", help="Path to File which conatins AD groups from excel")
parser.add_argument("adInDomain", help="Path to File which contains AD groups created in the domain")
args = parser.parse_args()
adFromExcelFile = args.adFromExcel
adInDomain = args.adInDomain
printLineBreaks("Input Files")
print adFromExcelFile
print adInDomain


printLineBreaks("AD groups from Excel File: ")
f = open(adFromExcelFile)
adFromExcelList = []
for eachLine in f:
	adFromExcelList.append(eachLine.strip())

f.close()
print adFromExcelList

printLineBreaks("AD groups Generated from the Domain Input File: ")
f = open(adInDomain)
adInDomainList = []
for eachLine in f:
	adInDomainList.append(eachLine.strip())
f.close 

print adInDomainList

printLineBreaks("AD groups from excel File which are presnt in Domain File:")
exceptionList = []
allGoodList = []
for eachAD in adFromExcelList:
	if eachAD in adInDomainList:
		allGoodList.append(eachAD)
	else:
		exceptionList.append(eachAD)

print allGoodList
printLineBreaks("EXCEPTION LIST: AD groups from excel file not present in Domain File")
print exceptionList 
printLineBreaks(" ")

print "writing all good ADs to file ......."

allGoodAdPath = "./allGoodADs/"  + str(adInDomain.split("/")[-1]) + "_allGood"
print allGoodAdPath
writeToFile(allGoodAdPath, allGoodList)


print "writing all Exceptions to file ......."

exceptionsAdPath = "./exceptionADs/"  + str(adInDomain.split("/")[-1]) + "_exception"
print exceptionsAdPath
writeToFile(exceptionsAdPath, exceptionList)

