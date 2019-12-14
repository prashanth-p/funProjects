#!/usr/bin/env python
# coding: utf-8

# # Access Streamlining

# In[45]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import glob
import os
path="D:\\Users\\PPradee2\\Documents\\MyFolder\\access_streamling_folder_test\\results\\"
print(path)
import openpyxl


# In[70]:


for fileName in glob.glob('*.xlsx'):
    # print("******************************************")
    print(fileName)
    df = pd.read_excel(fileName, sheetname='Sheet 1')
    columns = [] 
    i = 0
    # print(df.columns)
    for col in df.columns:
        columns.append(col)
    print(columns)
    
    dataForProcessing = {}
       
    for folderName in df[columns[0]].unique():
        folderName = str.strip(folderName)
        securityNames = []
        userNames = []
        for j in df[df[columns[0]]==folderName].index:
            currentSecurityName = str.strip(df[columns[1]][j])
            currentUserName = str.strip(df[columns[2]][j])
            
            if(currentSecurityName not in securityNames):
                securityNames.append(currentSecurityName)
                
            if(currentUserName not in userNames):
                userNames.append(currentUserName)
                
            dataForProcessing[folderName] = [securityNames, userNames]
    # print(dataForProcessing)
  

    processedData = {}
    processedData[columns[0]] = []
    processedData[columns[1]] = []
    processedData[columns[2]] = []
    processedData['uniqueSecurityDomains'] = []
    processedData['allGood'] = []
    
    
    for eachFolder, eachFolderSecurityAndUser in dataForProcessing.items():
        eachFolderSecurity = eachFolderSecurityAndUser[0]
        eachFolderUser = eachFolderSecurityAndUser[1]
        
        print("Folder Name: ", eachFolder)
        print("Security Domains: ", eachFolderSecurity)
        print("User Names: ", eachFolderUser)
        
        uniqueSecurityDomains = []
            # Generating Excel Sheets
        newFileName1=fileName.split(".")
        newFileName = path + newFileName1[0]+"_uniqueDomains.xlsx"
        
        for eachSecurityDomain in eachFolderSecurity:
            if(eachSecurityDomain.endswith("ADM") or eachSecurityDomain.endswith("USR")):
                print(eachSecurityDomain)
                if((eachSecurityDomain in eachFolderUser) and (eachSecurityDomain not in uniqueSecurityDomains)):
                    uniqueSecurityDomains.append(eachSecurityDomain)
        
        processedData['allGood'].append('True')    
        for eachUser in eachFolderUser:
            if(eachUser.endswith("USR") or eachUser.endswith("ADM")):
                if(eachUser not in uniqueSecurityDomains):
                    newFileName = path + "TO_CHECK_" + newFileName1[0]+"_uniqueDomains.xlsx"
                    processedData['allGood'].pop()
                    processedData['allGood'].append('False')
                    
                    
        print(uniqueSecurityDomains) 
        processedData[columns[0]].append(eachFolder)
        processedData[columns[1]].append(eachFolderSecurity)
        processedData[columns[2]].append(eachFolderUser)
        processedData['uniqueSecurityDomains'].append(uniqueSecurityDomains)
        print("**********************")
        
    # print(processedData)
    
    processedDataFrame = pd.DataFrame(processedData)
    # print(processedDataFrame)
 
    processedDataFrame.to_excel(newFileName)


# In[ ]:




