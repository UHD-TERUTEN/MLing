
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 19:04:38 2021

@author: gggg8
"""
"""def is_json_key_present(json, key):
    try:
    
    except: KeyError:
        return False
    return True
"""
import json
import csv

Main_list = []

ProgramName = []
errorCode = []
functionName = []
returnValue = []

creationTime = []
fileName = []
fileSize = []
isHidden = []
lastWriteTime = []


companyName = []
fileDescription = []
fileVersion = []
internalName = []
legalCopyright = []
originalFilename = []
productName = []
productVersion = []
"""
Exefile = []
OriginName = []
FileVer = []
ProductVer = []
Company = []
"""
input_file = []
line_tmp=[]

scv=open('F:\MLWS\hirebat5.csv','wt',encoding="utf-8-sig", newline='')
with open('F:\MLWS\log4.txt','rt', encoding="utf-8") as f:
    while True:
        line=f.readline()
        if not line: break
        if line_tmp==line: continue
        if line.find("ProgramName") >0:
            print("PITT")
            pass
        else:
            print("SHITT")
            continue
        #print(line)
        print(type(line))
        line_tmp=line
        json_data=json.loads(line)
        
        #print(json.dumps(json_data,indent="\t"))
        test=json_data
        jsonStr=json.dumps(test, ensure_ascii=False)
        

        #print(jsonStr)
        #print(type(jsonStr))

        dict=json.loads(jsonStr)

        #print(dict['moduleInfo'])
        
        NewStr=json.dumps(dict['ProgramName'],ensure_ascii=False)
        
        input_file.append(dict['ProgramName'])


        NewStr=json.dumps(dict['fileAccessInfo'],ensure_ascii=False)
           
        dict=json.loads(NewStr)
        
        input_file.append(dict['errorCode'])
        
        input_file.append(dict['functionName'])
        
        input_file.append(dict['returnValue'])
        
        #print("fileAccessInfo collected")
        
        
        dict=json.loads(jsonStr)
        
        NewStr=json.dumps(dict['fileInfo'], ensure_ascii=False)
        dict=json.loads(NewStr)
        
        input_file.append(dict['creationTime'])
        
        input_file.append(dict['fileName'])
        
        input_file.append(dict['fileSize'])
        
        input_file.append(dict['isHidden'])
        
        input_file.append(dict['lastWriteTime'])
        print(dict['lastWriteTime'])
        print(input_file)
       # print("fileInfo collected")
        
        
        #NewStr=json.dumps(dict['moduleInfo'])
        dict=json.loads(jsonStr)
        try:
            print("HELLO")
            NewStr=json.dumps(dict['moduleInfo'],ensure_ascii=False)
            
            dict=json.loads(NewStr)
            #Company from TERUTEN-attribute
            input_file.append(dict['companyName'])
            
            input_file.append(dict['fileDescription'])
            #FileVer from TERUTEN-attribute
            input_file.append(dict['fileVersion'])
            
            #OriginName from TERUTEN-attribute
            input_file.append(dict['internalName'])
            
            input_file.append(dict['legalCopyright'])
            #ExeFile from TERUTEN-attribute
            input_file.append(dict['originalFilename'])
            
            input_file.append(dict['productName'])
            #ProductVer from TERUTEN-attribute
            input_file.append(dict['productVersion'])
            
            if input_file[0] not in ProgramName:
                ProgramName.append(input_file[0])
            if str(input_file[1]) not in errorCode:
                errorCode.append(str(input_file[1]))
            if input_file[2] not in functionName:
                functionName.append(input_file[2])
            if str(input_file[3]) not in returnValue:
                returnValue.append(str(input_file[3]))
            if input_file[4] not in creationTime:
                creationTime.append(input_file[4])
            if input_file[5] not in fileName:
                fileName.append(input_file[5])
            if str(input_file[6]) not in fileSize:
                fileSize.append(str(input_file[6]))
            if str(input_file[7]) not in isHidden:
                isHidden.append(str(input_file[7]))
            if input_file[8] not in lastWriteTime:
                lastWriteTime.append(input_file[8])
            if input_file[9] not in companyName:
                companyName.append(input_file[9])
            if input_file[10] not in fileDescription:
                fileDescription.append(input_file[10])
            if input_file[11] not in fileVersion:
                fileVersion.append(input_file[11])
            if input_file[12] not in internalName:
                internalName.append(input_file[12])
            if input_file[13] not in legalCopyright:
                legalCopyright.append(input_file[13])
            if input_file[14] not in originalFilename:
                originalFilename.append(input_file[14])
            if input_file[15] not in productName:
                productName.append(input_file[15])
            if input_file[16] not in productVersion:
                productVersion.append(input_file[16])
            wr=csv.writer(scv)
            print("\n\n\n add to hirebat 1616\n\n")
            #print(input_file)
            wr.writerow(input_file)
            input_file=[]
            
            pass
        except KeyError:
            if input_file[0] not in ProgramName:
                ProgramName.append(input_file[0])
            if str(input_file[1]) not in errorCode:
                errorCode.append(str(input_file[1]))
            if input_file[2] not in functionName:
                functionName.append(input_file[2])
            if str(input_file[3]) not in returnValue:
                returnValue.append(str(input_file[3]))
            if input_file[4] not in creationTime:
                creationTime.append(input_file[4])
            if input_file[5] not in fileName:
                fileName.append(input_file[5])
            if str(input_file[6]) not in fileSize:
                fileSize.append(str(input_file[6]))
            if str(input_file[7]) not in isHidden:
                isHidden.append(str(input_file[7]))
            if input_file[8] not in lastWriteTime:
                lastWriteTime.append(input_file[8])
            wr=csv.writer(scv)
            print("\n\n\n add to hirebat 0808\n\n")
            wr.writerow(input_file)
            input_file=[]
            
            #print("\n\nfuck\n\n\n")
            pass
        
        #print(input_file)
        
        
        
       
        
for data in ProgramName:
    Main_list.append(data)
    
for data in errorCode:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in functionName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in returnValue:
    if data not in Main_list:
        Main_list.append(str(data))
        
        
        
for data in creationTime:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in fileName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in fileSize:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in isHidden:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in lastWriteTime:
    if data not in Main_list:
        Main_list.append(str(data))
        
        
        
for data in companyName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in fileDescription:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in fileVersion:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in internalName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in legalCopyright:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in originalFilename:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in productName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in productVersion:
    if data not in Main_list:
        Main_list.append(str(data))
        
        

scv.close()
marine=open('F:\MLWS\index4train.csv','wt',newline='')
w=csv.writer(marine)  
firebat=open('F:\MLWS\hirebat5.csv','rt',encoding='utf-8')
redir=csv.reader((line.replace('\0',' ') for line in firebat))
for line in redir:
    try:
        print("in")
        print(line[0])
        print("\nis line")
        print(errorCode.index(line[1]))
        templist=[ProgramName.index(line[0]),
                  len(ProgramName)+errorCode.index(line[1]), 
                  len(ProgramName)+len(errorCode)+functionName.index(line[2]), 
                  len(ProgramName)+len(errorCode)+len(functionName)+returnValue.index(line[3]),
                  len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+creationTime.index(line[4]),
                  len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(creationTime)+fileName.index(line[5]),
                  len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(creationTime)+len(fileName)+fileSize.index(line[6]),
                  len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(creationTime)+len(fileName)+len(fileSize)+isHidden.index(line[7]),
                  len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(creationTime)+len(fileName)+len(fileSize)+len(isHidden)+lastWriteTime.index(line[8])]
        print(templist)
    except ValueError:
        print("exception")
        continue
    if "Microsoft Office" in line[0]: 
        b=1
        print("OK")
    else : 
        b=0
        print("denied")
    templist.append(b)
    w.writerow(templist)    
      


f.close()  
firebat.close()
marine.close()
#print(json.dumps(json_data))

#print(json.dumps(json_data,indent="\t"))
#{"moduleInfo":{"companyName":"Microsoft Corporation","fileDescription":"Microsoft® C Runtime Library","fileVersion":"14.24.28127.4 built by: vcwrkspc","internalName":"vcruntime140.dll","legalCopyright":"© Microsoft Corporation. All rights reserved.","originalFilename":"vcruntime140.dll","productName":"Microsoft® Visual Studio®","productVersion":"14.24.28127.4"}}


