#!/usr/bin/env python
# coding: utf-8

# In[1]:



import os
import pandas as pd
import json
import csv
path_dir = 'F:\LogGatherer\Logs'

file_list = os.listdir(path_dir)

print(file_list)

Main_list = []
pre_list = []

ProgramName = []

isWorkingTime = []

obj_creationTime = []
obj_fileName = []
obj_fileSize = []
obj_isHidden = []
obj_lastWriteTime = []

errorCode = []
functionName = []
returnValue = []

subj_creationTime = []
subj_fileName = []
subj_fileSize = []
subj_isHidden = []
subj_lastWriteTime = []

companyName = []
fileDescription = []
fileVersion = []
internalName = []
legalCopyright = []
originalFilename = []
productName = []
productVersion = []


# In[2]:


def get_data_from_json(line,file_name):
    try:
        input_file.append(file_name)

        json_line=json.loads(line)

        jsonStr=json.dumps(json_line, ensure_ascii=False)
        dict=json.loads(jsonStr)
        


        tmpStr=json.dumps(dict['environment'], ensure_ascii=False)
        dict=json.loads(tmpStr)
        NewStr=json.dumps(dict['timeInfo'],ensure_ascii=False)
        dict=json.loads(NewStr)

        input_file.append(dict['isWorkingTime'])
        
        jsonStr=json.dumps(json_line, ensure_ascii=False)
        dict=json.loads(jsonStr)

        tmpStr=json.dumps(dict['object'], ensure_ascii=False)
        dict=json.loads(tmpStr)
        NewStr=json.dumps(dict['fileInfo'],ensure_ascii=False)
        dict=json.loads(NewStr)

        input_file.append(dict['creationTime'])
        
        #####################
        '''
        cut_hwakjangja = (dict['fileName'])
        cut_hwakjangja.split()[-1]
        input("잉")
        '''
        #####################
        #cut_hwakjangja = (dict['fileName'])
        #cut_extension=cut_extension.split('\\')[-1]
        #print(cut_extension)
        cut_extension=(dict['fileName'])
        extension=cut_extension.split('.')[-1]
        
        input_file.append(extension)
        
        input_file.append(dict['fileSize'])

        input_file.append(dict['isHidden'])

        input_file.append(dict['lastWriteTime'])

        jsonStr=json.dumps(json_line, ensure_ascii=False)
        dict=json.loads(jsonStr)

        tmpStr=json.dumps(dict['operation'], ensure_ascii=False)
        dict=json.loads(tmpStr)
        NewStr=json.dumps(dict['fileAccessInfo'],ensure_ascii=False)
        dict=json.loads(NewStr)

        input_file.append(dict['errorCode'])

        input_file.append(dict['functionName'])

        input_file.append(dict['returnValue'])

        jsonStr=json.dumps(json_line, ensure_ascii=False)

        dict=json.loads(jsonStr)
        tmpStr=json.dumps(dict['subject'], ensure_ascii=False)
        dict=json.loads(tmpStr)
        NewStr=json.dumps(dict['fileInfo'], ensure_ascii=False)
        dict=json.loads(NewStr)

        input_file.append(dict['creationTime'])

        input_file.append(dict['fileName'])

        input_file.append(dict['fileSize'])

        input_file.append(dict['isHidden'])

        input_file.append(dict['lastWriteTime'])
        dict=json.loads(jsonStr)
        tmpStr=json.dumps(dict['subject'], ensure_ascii=False)
        dict=json.loads(tmpStr)
        write_to_csv(input_file, dict)
    except KeyError:
        print("KeyError")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        dict=json.loads(jsonStr)
        write_to_csv(input_file, dict)


# In[3]:


#file_list=file_list[0] 0번 파일 열기
def file_open(file_list,file_name):
    f=open('F:\LogGatherer\Logs\\'+file_list, 'r', encoding='utf-8')

    for line in f:
        #print(file_name + line, end='')
        tmp_line=line
        get_data_from_json(line, file_name)
    f.close()


# In[4]:


def read_file_name(file_list):
    for item in file_list :
        tmp=item[:-4]
        print(item[:-4])
        programName.append(tmp)
        file_open(item, tmp)


# In[5]:


def write_to_csv(input_file, dict):
    try:
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
        #add to array that has name of attribute same
        if input_file[0] not in ProgramName:
            ProgramName.append(input_file[0])
            print("1")
            print(ProgramName)
        
        if input_file[1] not in isWorkingTime:
            isWorkingTime.append(input_file[1])
        
        if input_file[2] not in obj_creationTime:
            obj_creationTime.append(input_file[2])
        if input_file[3] not in obj_fileName:
            obj_fileName.append(input_file[3])
        if str(input_file[4]) not in obj_fileSize:
            obj_fileSize.append(str(input_file[4]))
        if str(input_file[5]) not in obj_isHidden:
            obj_isHidden.append(str(input_file[5]))
        if input_file[6] not in obj_lastWriteTime:
            obj_lastWriteTime.append(input_file[6])    
            
        if str(input_file[7]) not in errorCode:
            errorCode.append(str(input_file[7]))
        if input_file[8] not in functionName:
            functionName.append(input_file[8])
        if str(input_file[9]) not in returnValue:
            returnValue.append(str(input_file[9]))
            
        if input_file[10] not in subj_creationTime:
            subj_creationTime.append(input_file[10])
        if input_file[11] not in subj_fileName:
            subj_fileName.append(input_file[11])
        if str(input_file[12]) not in subj_fileSize:
            subj_fileSize.append(str(input_file[12]))
        if str(input_file[13]) not in subj_isHidden:
            subj_isHidden.append(str(input_file[13]))
        if input_file[14] not in subj_lastWriteTime:
            subj_lastWriteTime.append(input_file[14]) 
        #moduleInfo
        if input_file[15] not in companyName:
            companyName.append(input_file[15])
        if input_file[16] not in fileDescription:
            fileDescription.append(input_file[16])
        if input_file[17] not in fileVersion:
            fileVersion.append(input_file[17])
        if input_file[18] not in internalName:
            internalName.append(input_file[18])
        if input_file[19] not in legalCopyright:
            legalCopyright.append(input_file[19])
        if input_file[20] not in originalFilename:
            originalFilename.append(input_file[20])
        if input_file[21] not in productName:
            productName.append(input_file[21])
        if input_file[22] not in productVersion:
            productVersion.append(input_file[22])
        b="YES"
        if '(ERROR)' in str(input_file[1]):
            b="NO"
            print("에러노")
        elif 'False' in str(input_file[1]):
            b="NO"
            print("불펄스")
        else:
            print("불트루")
            if 'WINWORD.EXE' in input_file[0]:
                print("월드")
                if 'DetouredWriteFile' in input_file[8]:
                    b="NO"
                    print("콘펄스")
        input_file.append(b)
        wr=csv.writer(scv)
        
        wr.writerow(input_file)
        input_file.clear()
        return ProgramName,isWorkingTime,obj_creationTime, obj_fileName, obj_fileSize, obj_isHidden, obj_lastWriteTime,errorCode, functionName, returnValue,subj_creationTime, subj_fileName, subj_fileSize, subj_isHidden, subj_lastWriteTime,companyName, fileDescription, fileVersion, internalName, legalCopyright, originalFilename, productName, productVersion
        pass
    except KeyError:
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        input_file.append("(ERROR)")
        if input_file[0] not in ProgramName:
            ProgramName.append(input_file[0])
            print("1")
        
        if input_file[1] not in isWorkingTime:
            isWorkingTime.append(input_file[1])
        
        if input_file[2] not in obj_creationTime:
            obj_creationTime.append(input_file[2])
        if input_file[3] not in obj_fileName:
            obj_fileName.append(input_file[3])
        if str(input_file[4]) not in obj_fileSize:
            obj_fileSize.append(str(input_file[4]))
        if str(input_file[5]) not in obj_isHidden:
            obj_isHidden.append(str(input_file[5]))
        if input_file[6] not in obj_lastWriteTime:
            obj_lastWriteTime.append(input_file[6])    
            
        if str(input_file[7]) not in errorCode:
            errorCode.append(str(input_file[7]))
        if input_file[8] not in functionName:
            functionName.append(input_file[8])
        if str(input_file[9]) not in returnValue:
            returnValue.append(str(input_file[9]))
            
        if input_file[10] not in subj_creationTime:
            subj_creationTime.append(input_file[10])
        if input_file[11] not in subj_fileName:
            subj_fileName.append(input_file[11])
        if str(input_file[12]) not in subj_fileSize:
            subj_fileSize.append(str(input_file[12]))
        if str(input_file[13]) not in subj_isHidden:
            subj_isHidden.append(str(input_file[13]))
        if input_file[14] not in subj_lastWriteTime:
            subj_lastWriteTime.append(input_file[14]) 
        #moduleInfo
        if input_file[15] not in companyName:
            companyName.append(input_file[15])
        if input_file[16] not in fileDescription:
            fileDescription.append(input_file[16])
        if input_file[17] not in fileVersion:
            fileVersion.append(input_file[17])
        if input_file[18] not in internalName:
            internalName.append(input_file[18])
        if input_file[19] not in legalCopyright:
            legalCopyright.append(input_file[19])
        if input_file[20] not in originalFilename:
            originalFilename.append(input_file[20])
        if input_file[21] not in productName:
            productName.append(input_file[21])
        if input_file[22] not in productVersion:
            productVersion.append(input_file[22])
        #if DENY b is NO PERMITYES
        b="YES"
        if '(ERROR)' in str(input_file[1]):
            b="NO"
            print("에러노")
        elif 'False' in str(input_file[1]):
            b="NO"
            print("불펄스")
        else:
            print("불트루")
            if 'WINWORD.EXE' in input_file[0]:
                print("월드")
                if 'DetouredWriteFile' in input_file[8]:
                    b="NO"
                    print("콘펄스")
        input_file.append(b)
        print("write")
        wr=csv.writer(scv)
        
        wr.writerow(input_file)
        input_file.clear()
        return ProgramName,isWorkingTime,obj_creationTime, obj_fileName, obj_fileSize, obj_isHidden, obj_lastWriteTime,errorCode, functionName, returnValue,subj_creationTime, subj_fileName, subj_fileSize, subj_isHidden, subj_lastWriteTime,companyName, fileDescription, fileVersion, internalName, legalCopyright, originalFilename, productName, productVersion


# In[6]:


print(file_list[0])
programName=[]
i=0

scv=open('F:\MLWS\ML0518.csv','wt',encoding="utf-8-sig", newline='')
wr=csv.writer(scv)

input_file=['ProgramName',
     'isWorkingTime',
     'obj_creationTime','obj_fileName','obj_fileSize','obj_isHidden','obj_lastWriteTime',
    'errorCode','functionName','returnValue',
    'subj_creationTime','subj_fileName','subj_fileSize','subj_isHidden','subj_lastWriteTime',
    'companyName','fileDescription','fileVersion','internalName','legalCopyright',
    'originalFilename','productName','productVersion','Permit?']
wr.writerow(input_file)
input_file.clear()
read_file_name(file_list)


# In[7]:


scv.close()


# In[8]:



for data in ProgramName:
    Main_list.append(data)

for data in isWorkingTime:
    Main_list.append(data)

for data in obj_creationTime:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_fileName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_fileSize:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_isHidden:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_lastWriteTime:
    if data not in Main_list:
        Main_list.append(str(data))
        
        
for data in errorCode:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in functionName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in returnValue:
    if data not in Main_list:
        Main_list.append(str(data))
            
for data in subj_creationTime:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_fileName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_fileSize:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_isHidden:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_lastWriteTime:
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


# In[9]:


#print(Main_list)


# In[10]:


#from tensorflow.keras.preprocessing.text import Tokenizer


# In[ ]:





# In[11]:


csv_file= open('F:\MLWS\ML0518Permission.csv', 'wt',encoding="utf-8-sig", newline='')
w=csv.writer(csv_file)
op_file=open('F:\MLWS\ML0518.csv', 'rt', encoding = 'utf-8-sig')
redir=csv.reader((line.replace('\0',' ')for line in op_file))

ing=['Permit?']
w.writerow(ing)

for line in redir:
    if line[0] is '\ufeffProgramName':
        continue
    if 'ProgramName' in line[0]:
        continue
    
   
    templist=[]
    b="YES"
    print(type(line))
    if '(ERROR)' in line[1]:
        b="NO"
        print("에러노")
    elif 'False' in line[1]:
        b="NO"
        print("불펄스")
    else:
        print("불트루")
        if 'WINWORD.EXE' in line[0]:
            print("월드")
            if 'DetouredWriteFile' in line[8]:
                b="NO"
                print("콘펄스")
    templist.append(b)
    print("write")
    w.writerow(templist)
    '''
    if 'ngen' in line[0]:
        b="NO"
    elif line[9] != '(EMPTY)':
        print("잉")
        b="YES"
    else:
        b="YES"
       
    if "Microsoft" in line[0]: 
        b=1
    elif "Acro" in line[0]: 
        b=1
    elif "Adobe" in line[0]:
        b=1
    elif "WORD" in line[0]:
        b=1
    elif "EXCEL" in line[0]:
        b=1
    else : 
        b=0
        print("denied")
    '''


# In[12]:


csv_file.close()
op_file.close()


# In[13]:


'''
   try :
       templist=[ProgramName.index(line[0]),
               len(ProgramName)+isWorkingTime.index(line[1]),
               len(ProgramName)+len(isWorkingTime)+obj_creationTime.index(line[2]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+ obj_fileName.index(line[3]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + obj_fileSize.index(line[4]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + obj_isHidden.index(line[5]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+obj_lastWriteTime.index(line[6]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ errorCode.index(line[7]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+functionName.index(line[8]), 
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+returnValue.index(line[9]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+subj_creationTime.index(line[10]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+subj_fileName.index(line[11]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+subj_fileSize.index(line[12]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+subj_isHidden.index(line[13]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+subj_lastWriteTime.index(line[14]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ companyName.index(line[15]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ fileDescription.index(line[16]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ fileVersion.index(line[17]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ internalName.index(line[18]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + legalCopyright.index(line[19]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ originalFilename.index(line[20]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ len(originalFilename)+ productName.index(line[21]),
               len(ProgramName)+len(isWorkingTime)+len(obj_creationTime)+len(obj_fileName)+ len(obj_fileName) + len(obj_fileSize) + len(obj_isHidden)+len(obj_lastWriteTime)+ len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ len(originalFilename)+ len(productName)+productVersion.index(line[22])]
       print("시발")
                 #len(ProgramName)+len(errorCode)+functionName.index(line[2]), 
                 #len(ProgramName)+len(errorCode)+len(functionName)+returnValue.index(line[3]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+subj_creationTime.index(line[9]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+subj_fileName.index(line[10]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+subj_fileSize.index(line[11]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+subj_isHidden.index(line[12]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+subj_lastWriteTime.index(line[13]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ companyName.index(line[14]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ fileDescription.index(line[15]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ fileVersion.index(line[16]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ internalName.index(line[17]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + legalCopyright.index(line[18]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ originalSubj_fileName.index(line[19]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ len(originalSubj_fileName)+ productName.index(line[20]),
                 #len(ProgramName)+len(errorCode)+len(functionName)+len(returnValue)+len(subj_creationTime)+len(subj_fileName)+len(subj_fileSize)+len(subj_isHidden)+len(subj_lastWriteTime)+ len(companyName)+ len(fileDescription)+ len(fileVersion)+ len(internalName) + len(legalCopyright)+ len(originalSubj_fileName)+ len(productName)+productVersion.index(line[21])]
       print(templist)
   except ValueError:
       
       print("exception")
       print(">>>>>>")
       print(line)
       print("<<<<<<")
       print(line[0])
       print("#########")
       continue
   '''


'''
if 'False' in line[1]:
   b="NO"
else:
   if 'word' in line[0]:
       if 'write' in line[8]:
           b="NO"
templist=b
templist.append(b)
print("write")
w.writerow(templist)
'''

   '''
   if 'ngen' in line[0]:
       b="NO"
   elif line[9] != '(EMPTY)':
       print("잉")
       b="YES"
   else:
       b="YES"
      
   if "Microsoft" in line[0]: 
       b=1
   elif "Acro" in line[0]: 
       b=1
   elif "Adobe" in line[0]:
       b=1
   elif "WORD" in line[0]:
       b=1
   elif "EXCEL" in line[0]:
       b=1
   else : 
       b=0
       print("denied")
   '''











# In[ ]:





# In[ ]:





# In[ ]:




