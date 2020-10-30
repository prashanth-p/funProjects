##################################################################################
# Author: Prashanth Pradee
# Date: Friday, 30-Oct-2020
# Description: Generate report from Kafka Topic - offset - Partitions
##################################################################################

import glob
import json
import csv


FILE_PATH="D:\\Users\\PPradee2\\Videos\\projects\\kafka_last_record_report\\ETH\\"
FILE_NAME_PATH= FILE_PATH + "*.out"
OUTPUT_FILE_PATH="D:\\Users\\PPradee2\\Videos\\projects\\kafka_last_record_report\\output.csv"
outputData=[]
for fileName in glob.glob(FILE_NAME_PATH):
    details={}
    fileNameToPrint=fileName.split(FILE_PATH)[1]
    print(fileNameToPrint)
    details["fileName"]=fileNameToPrint
    with open(fileName, 'r') as f:
        data = f.readlines()
        for i in data:
            if "=" in i:
               line=i.split(" = ")
               kafka_details=line[1].split("\n")[0]
               details["kafka_details"]=kafka_details
            else:
                line=i.replace("\n","")
                line=line.split("\t")
                table_name=line[0]
                details["table_name"]=table_name 
                jsonData=json.loads(line[1])
                print(jsonData)
                for key,value in jsonData.items():
                    if (value is None):
                        details[key]=""
                    else:
                        for k,v in value.items():
                            #print(key,k,v)
                            key=key.strip()
                            v = v.strip()
                            if (
                                (key == "INFA_BIGINT_SEQUENCE")
                                or (key == "INFA_SEQUENCE")
                                or (key == "DTL__CAPXACTION")
                                or (key == "DTL__CAPXRESTART1")
                                or (key == "DTL__CAPXRESTART2")
                                or (key == "DTL__CAPXROWID")
                                or (key == "DTL__CAPXTIMESTAMP")
                                or (key == "DTL__CAPXUSER")
                                or (key == "DTL__CAPXUSER")
                                or (key == "INFA_OP_TYPE")
                                or (key == "INFA_TABLE_NAME")
                                or (key == "INFA_TIME_CREATED")
                            ):
                                if str.isspace(str(v)):
                                    details[key]=""
                                else:
                                    details[key]=v
        outputData.append(details)
            
keys=outputData[0].keys()
with open(OUTPUT_FILE_PATH, 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(outputData)
