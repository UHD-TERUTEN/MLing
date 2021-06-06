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

obj_companyName=[]
obj_fileDescription=[]
obj_fileVersion=[]
obj_internalName=[]
obj_legalCopyright=[]
obj_originalFilename=[]
obj_productName=[]
obj_productVersion=[]

errorCode = []
functionName = []
returnValue = []

subj_creationTime = []
subj_fileName = []
subj_fileSize = []
subj_isHidden = []
subj_lastWriteTime = []

subj_companyName = []
subj_fileDescription = []
subj_fileVersion = []
subj_internalName = []
subj_legalCopyright = []
subj_originalFilename = []
subj_productName = []
subj_productVersion = []


# In[2]:


def get_data_from_json(line,file_name):
    try:
        input_file.append(file_name)

        json_line=json.loads(line)

        jsonStr=json.dumps(json_line, ensure_ascii=False)
        dict=json.loads(jsonStr)
        try:
            tmpStr=json.dumps(dict['environment'], ensure_ascii=False)
            dict=json.loads(tmpStr)
            NewStr=json.dumps(dict['timeInfo'],ensure_ascii=False)
            dict=json.loads(NewStr)
    
            input_file.append(dict['isWorkingTime'])
        except KeyError:
            input_file.append("(env_ERROR)")
            
        jsonStr=json.dumps(json_line, ensure_ascii=False)
        dict=json.loads(jsonStr)
        try:
            tmpStr=json.dumps(dict['object'], ensure_ascii=False)
            dict=json.loads(tmpStr)
            NewStr=json.dumps(dict['fileInfo'],ensure_ascii=False)
            dict=json.loads(NewStr)
    
            input_file.append(dict['creationTime'])
            
            cut_extension=(dict['fileName'])
            extension=cut_extension.split('.')[-1]
            print(cut_extension)
            input_file.append(extension)
            
            input_file.append(dict['fileSize'])
    
            input_file.append(dict['isHidden'])
    
            input_file.append(dict['lastWriteTime'])
        except KeyError:
            input_file.append("(obj_ERROR)")
            input_file.append("(obj_ERROR)")
            input_file.append("(obj_ERROR)")
            input_file.append("(obj_ERROR)")
            input_file.append("(obj_ERROR)")
            
        try:
            TryStr=json.dumps(dict['moduleInfo'],ensure_ascii=False)
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
            
        except KeyError:
            print("Object group has no module_info")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            input_file.append("(obj_module_ERROR)")
            
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
        
        cut_extension=(dict['fileName'])
        extension_filename=cut_extension.split('.')[-1]

        input_file.append(extension_filename)

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
        dict=json.loads(jsonStr)
        write_to_csv(input_file, dict)





#file_list=file_list[0] 0번 파일 열기
def file_open(file_list,file_name):
    f=open('F:\LogGatherer\Logs\\'+file_list, 'r', encoding='utf-8')

    for line in f:
        #print(file_name + line, end='')
        tmp_line=line
        get_data_from_json(line, file_name)
    f.close()



def read_file_name(file_list):
    for item in file_list :
        tmp=item[:-4]
        print(item[:-4])
        programName.append(tmp)
        file_open(item, tmp)




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
        
        if input_file[7] not in obj_companyName:
            obj_companyName.append(input_file[7])
        if input_file[8] not in obj_fileDescription:
            obj_fileDescription.append(input_file[8])
        if input_file[9] not in obj_fileVersion:
            obj_fileVersion.append(input_file[9])
        if input_file[10] not in obj_internalName:
            obj_internalName.append(input_file[10])
        if input_file[11] not in obj_legalCopyright:
            obj_legalCopyright.append(input_file[11])
        if input_file[12] not in obj_originalFilename:
            obj_originalFilename.append(input_file[12])
        if input_file[13] not in obj_productName:
            obj_productName.append(input_file[13])
        if input_file[14] not in obj_productVersion:
            obj_productVersion.append(input_file[14])
            
        if str(input_file[15]) not in errorCode:
            errorCode.append(str(input_file[15]))
        if input_file[16] not in functionName:
            functionName.append(input_file[16])
        if str(input_file[17]) not in returnValue:
            returnValue.append(str(input_file[17]))
            
        if input_file[18] not in subj_creationTime:
            subj_creationTime.append(input_file[18])
        if input_file[19] not in subj_fileName:
            subj_fileName.append(input_file[19])
        if str(input_file[20]) not in subj_fileSize:
            subj_fileSize.append(str(input_file[20]))
        if str(input_file[21]) not in subj_isHidden:
            subj_isHidden.append(str(input_file[21]))
        if input_file[22] not in subj_lastWriteTime:
            subj_lastWriteTime.append(input_file[22]) 
        #moduleInfo
        if input_file[23] not in subj_companyName:
            subj_companyName.append(input_file[23])
        if input_file[24] not in subj_fileDescription:
            subj_fileDescription.append(input_file[24])
        if input_file[25] not in subj_fileVersion:
            subj_fileVersion.append(input_file[25])
        if input_file[26] not in subj_internalName:
            subj_internalName.append(input_file[26])
        if input_file[27] not in subj_legalCopyright:
            subj_legalCopyright.append(input_file[27])
        if input_file[28] not in subj_originalFilename:
            subj_originalFilename.append(input_file[28])
        if input_file[29] not in subj_productName:
            subj_productName.append(input_file[29])
        if input_file[30] not in subj_productVersion:
            subj_productVersion.append(input_file[30])
        b="YES"
        if '(ERROR)' in str(input_file[1]):
            b="NO"
            print("에러노")
        elif 'False' in str(input_file[1]):
            b="NO"
            print("불펄스")
        else:
            print("불 트루")
            if 'pptx' in input_file[3]:
                print("PPTX")
                b="NO"
            elif 'pdf' in input_file[3]:
                print("pdf")
                b="NO"
            elif 'NOTEPAD' in input_file[0]:
                print("메모장")
                b="NO"
        input_file.append(b)
        wr=csv.writer(scv)
        
        wr.writerow(input_file)
        input_file.clear()
        return ProgramName,isWorkingTime,obj_creationTime, obj_fileName, obj_fileSize, obj_isHidden, obj_lastWriteTime,    obj_fileDescription, obj_fileVersion, obj_internalName, obj_legalCopyright, obj_originalFilename, obj_productName, obj_productVersion,    errorCode, functionName, returnValue,    subj_creationTime, subj_fileName, subj_fileSize, subj_isHidden, subj_lastWriteTime,subj_companyName, subj_fileDescription, subj_fileVersion, subj_internalName, subj_legalCopyright, subj_originalFilename, subj_productName, subj_productVersion
        pass
    except KeyError:
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
        input_file.append("(subj_module_ERROR)")
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
            
        if input_file[7] not in obj_companyName:
            obj_companyName.append(input_file[7])
        if input_file[8] not in obj_fileDescription:
            obj_fileDescription.append(input_file[8])
        if input_file[9] not in obj_fileVersion:
            obj_fileVersion.append(input_file[9])
        if input_file[10] not in obj_internalName:
            obj_internalName.append(input_file[10])
        if input_file[11] not in obj_legalCopyright:
            obj_legalCopyright.append(input_file[11])
        if input_file[12] not in obj_originalFilename:
            obj_originalFilename.append(input_file[12])
        if input_file[13] not in obj_productName:
            obj_productName.append(input_file[13])
        if input_file[14] not in obj_productVersion:
            obj_productVersion.append(input_file[14])

        if str(input_file[15]) not in errorCode:
            errorCode.append(str(input_file[15]))
        if input_file[16] not in functionName:
            functionName.append(input_file[16])
        if str(input_file[17]) not in returnValue:
            returnValue.append(str(input_file[17]))
            
        if input_file[18] not in subj_creationTime:
            subj_creationTime.append(input_file[18])
        if input_file[19] not in subj_fileName:
            subj_fileName.append(input_file[19])
        if str(input_file[20]) not in subj_fileSize:
            subj_fileSize.append(str(input_file[20]))
        if str(input_file[21]) not in subj_isHidden:
            subj_isHidden.append(str(input_file[21]))
        if input_file[22] not in subj_lastWriteTime:
            subj_lastWriteTime.append(input_file[22]) 
        #moduleInfo
        if input_file[23] not in subj_companyName:
            subj_companyName.append(input_file[23])
        if input_file[24] not in subj_fileDescription:
            subj_fileDescription.append(input_file[24])
        if input_file[25] not in subj_fileVersion:
            subj_fileVersion.append(input_file[25])
        if input_file[26] not in subj_internalName:
            subj_internalName.append(input_file[26])
        if input_file[27] not in subj_legalCopyright:
            subj_legalCopyright.append(input_file[27])
        if input_file[28] not in subj_originalFilename:
            subj_originalFilename.append(input_file[28])
        if input_file[29] not in subj_productName:
            subj_productName.append(input_file[29])
        if input_file[30] not in subj_productVersion:
            subj_productVersion.append(input_file[30])
        #if DENY b is NO PERMITYES Make your rule to permit or deny 
        b="YES"
        if '(ERROR)' in str(input_file[1]):
            b="NO"
            print("에러노")
        elif 'False' in str(input_file[1]):
            b="NO"
            print("불펄스")
        else:
            print("불 트루")
            if 'pptx' in input_file[3]:
                print("PPTXdddd")
                b="NO"
            elif 'pdf' in input_file[3]:
                print("pdfdddd")
                b="NO"
            elif 'NOTEPAD' in input_file[0]:
                print("메모장")
                b="NO"
        input_file.append(b)
        print("write")
        wr=csv.writer(scv)
        
        wr.writerow(input_file)
        input_file.clear()
        return ProgramName,isWorkingTime, obj_creationTime, obj_fileName, obj_fileSize, obj_isHidden, obj_lastWriteTime,obj_fileDescription, obj_fileVersion, obj_internalName, obj_legalCopyright, obj_originalFilename, obj_productName, obj_productVersion,errorCode, functionName, returnValue,    subj_creationTime, subj_fileName, subj_fileSize, subj_isHidden, subj_lastWriteTime,subj_companyName, subj_fileDescription, subj_fileVersion, subj_internalName, subj_legalCopyright, subj_originalFilename, subj_productName, subj_productVersion



print(file_list[0])
programName=[]
i=0

scv=open('F:\MLWS\\UHD\ML0607.csv','wt',encoding="utf-8-sig", newline='')
wr=csv.writer(scv)

input_file=['ProgramName',
     'environment_isWorkingTime',
     'object_creationTime','object_fileName','object_fileSize','object_isHidden','object_lastWriteTime',
    'object_companyName','object_fileDescription', 'object_fileVersion', 'object_internalName', 'object_legalCopyright', 'object_originalFilename', 'object_productName', 'object_productVersion',
    'operation_errorCode','operation_functionName','operation_returnValue',
    'subject_creationTime','subject_fileName','subject_fileSize','subject_isHidden','subject_lastWriteTime',
    'subject_companyName','subject_fileDescription','subject_fileVersion','subject_internalName','subject_legalCopyright',
    'subject_originalFilename','subject_productName','subject_productVersion','Permit?']
wr.writerow(input_file)
input_file.clear()
read_file_name(file_list)



scv.close()



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


for data in obj_companyName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_fileDescription:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_fileVersion:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_internalName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_legalCopyright:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_originalFilename:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_productName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in obj_productVersion:
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
        
        
        
for data in subj_companyName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_fileDescription:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_fileVersion:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_internalName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_legalCopyright:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_originalFilename:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_productName:
    if data not in Main_list:
        Main_list.append(str(data))
        
for data in subj_productVersion:
    if data not in Main_list:
        Main_list.append(str(data))




csv_file= open('F:\MLWS\ML0607Permission.csv', 'wt',encoding="utf-8-sig", newline='')
w=csv.writer(csv_file)
op_file=open('F:\MLWS\\UHD\ML0607.csv', 'rt', encoding = 'utf-8-sig')
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
        print("불 트루")
        if 'pptx' in line[3]:
            print("PPTXaa")
            b="NO"
        elif 'pdf' in line[3]:
            print("pdfaa")
            b="NO"
        elif 'NOTEPAD' in line[0]:
            print("메모장")
            b="NO"
 
    templist.append(b)
    print("write")
    w.writerow(templist)


csv_file.close()
op_file.close()



'''
2021 산학 연계 프로젝트 발표 TERUTEN _ UHD 
'''










# In[ ]:





# In[ ]:





# In[ ]:




