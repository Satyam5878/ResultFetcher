import os
import sys
import pickle


attr_object = ""
def createAttribute(RESULT_URL,BASE_URL):
    pickle.dump(RESULT_URL+" "+BASE_URL,open(os.getcwd()+"/URL.p","wb"))
    global attr_object
    attr_object = pickle.load(open(os.getcwd()+"/URL.p","rb"))
    
    print("Created URL.p")
def definingAttribute():
    if os.path.exists(os.getcwd()+"/URL.p"):
        print("Yes")
        global attr_object
        attr_object = pickle.load(open(os.getcwd()+"/URL.p","rb"))
        print(attr_object)
    else:
        print("No")
        RESULT_URL = "http://dolphintechnologies.in/manit/accessview.php"
        BASE_URL ="http://manit.ecampuserp.com/assets/img/students"
        createAttribute(RESULT_URL,BASE_URL)

definingAttribute()

import ImageFetcher
import InfoCollector
import Sorter





    





PROJECT_NAME =  "ManitResultFetcher"
EMPTY_PATH = os.path.expanduser("~")+"/Desktop/"
PATH_ENTERED =""
PATH_SGPA = "SGPA"
PATH_SGPA_CGPA = "SGPA_CGPA"
PATH_CGPA = "CGPA"
PATH_RESULT = "Result"
PATH_IMAGE = "Image"
ACTUAL_CWD = "p"
def welcomeDisplay():
    print("/*\n *\n * Welcome to MANIT RESULT FETCHER!\n *\n */")
option = ["SGPA of Individual.  ","CGPA of Individual.  ",
          "SGPA in Range.       ","CGPA in Range.       ",
          "Result of Individual.","Result In Range.     ",
          "Sort Result on SGPA. ","Sort Result on CGPA. ",
          "Image of Individual. ","Image in Range.     ",
          "                    ", "Quit                ",]
def directoryInput():
    tmp = input("Enter Working Directory. : ")
    if tmp == "":
        print("Path Empty.")
        tmp = EMPTY_PATH
        print(EMPTY_PATH)
        #os.makedirs(tmp)
    global ACTUAL_CWD
    ACTUAL_CWD = tmp+"/"+PROJECT_NAME
    print(ACTUAL_CWD+"1")
    #for making root dir for project
    try:
        os.makedirs(ACTUAL_CWD)
        print("Path : "+ACTUAL_CWD+" :: Created Working Directory.")
    except:
        print("Path : "+ACTUAL_CWD+" :: Already Exist.\n")

    #creating sgpa directory
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_SGPA)
        print("Path : "+ACTUAL_CWD+"/"+PATH_SGPA+" :: Creating SGPA Directory.")
    except:
        print("Path : "+ACTUAL_CWD+"/"+PATH_SGPA+" ::  SGPA Directory Already Exists.")
    #creating sgpa_cgpa directory
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_SGPA_CGPA)
        print("Path :"+ACTUAL_CWD+"/"+PATH_SGPA_CGPA+" :: Creating SGPA_CGPA Directory.")
    except:
        print("Path  : "+ACTUAL_CWD+"/"+PATH_SGPA_CGPA+" :: Directory SGPA_CGPA Already Exists.")
    #creating cgpa directory
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_CGPA)
        print("Path : "+ACTUAL_CWD+"/"+PATH_CGPA+" :: Creating CGPA Directory.")
    except:
        print("Path : "+ACTUAL_CWD+"/"+PATH_CGPA+" ::  CGPA Directory Already Exists.")
    #creating result directory
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_RESULT)
        print("Path : "+ACTUAL_CWD+"/"+PATH_RESULT+" :: Creating RESULT Direcory.")
    except:
        print("Path : "+ACTUAL_CWD+"/"+PATH_RESULT+" :: RESULT Direcory Already Exists.")
    #creating image folder
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_IMAGE)
        print("Path : "+ACTUAL_CWD+"/"+PATH_IMAGE+" :: Creating IMAGE Directory.")
    except:
        print("Path : "+ACTUAL_CWD+"/"+PATH_IMAGE+":: IMAGE Directory Already Exists.")
        
        
    """
    if os.path.exists(tmp):
        print("Path : "+tmp+" :: Already Exist.\n        Created Working Directory Inside it.")
    else:
        try:
            os.makedir(tmp)
            print("Path : "+tmp+"Created Working Directory")
        except:
            pass
    """
            
        
def optionDisplay():
    print("\n\nSelect Something:--\n\n")
    for i in range(1,28):
        print("*",end="")
    print()
    count = 1
    for item in option:
        print("* "+ str(count)+" "+item +" *" )
        count += 1
    for i in range(1,28):
        print("*",end="")
    print()
def noteDisplay():
    print("Note :- \n Option 1 and 2 can be Combined. as 1 2 or 2 1\n Option 3 and 4 can Be Combined.as 3 4 or 4 3\n"
          " Option 7 work with 1. as 3 7 or 7 3\n Option 8 work with option 4. as 4 8 or 8 4")

def optionCaller():
    optionDisplay()
    noteDisplay()
def valid(schNo):
    if not schNo.isdigit():
        print("Error-: Scholar No. must be digit.")
        return False
    if not (len(schNo)is 9):
        print("Error-: Length of Scholar No. must be 9.")
        return False
    return True    
if __name__ == '__main__':
    print(1)
    #definingAttribute()
    welcomeDisplay()
    directoryInput()
    while 1:
        optionCaller()
        while 1:
            selectedOption = input("\nEnter option : ")
            
            if (selectedOption.lower() in ('q','qu','qui','quit')) or (selectedOption == '12'):
                print("Hope to see You Again. Have a Nice Day!!")
                sys.exit()
            if selectedOption.lower() in ("fuck","fuck you","fucking "):
                s =  ""
                for i in range(200000):
                    #"""
                    x = 4
                    print("fun**ing You!" ,x*" " ,end=" ")
                    x = 1
                    print("fun**ing You!" ,x*" " ,end=" ")
                    #"""
                    """
                    s = s+"fun**ing You!" +3*" "
                    """
                print(s)
                os.system("cls")
            if selectedOption.lower() in ('i','image','img','9','image of individual'):
                schNo = input("Enter Scholar No. : ").strip()
                """
                if not schNo.isdigit():
                    print("Scholar No. must be digit.")
                elif not (len(schNo) is 9):
                    print("Length of Scholar No. must be 9.")
                else:
                    #print("there")
                    #print(ACTUAL_CWD)
                    truthness = ImageFetcher.getImageOfIndividual(ACTUAL_CWD,PATH_IMAGE,schNo)
                    if truthness:
                        print("Fetched the Image of Scholar No. : ",schNo)
                        option = input("Want to open Image (y/n): ")
                        if option.lower() in ('y','yes','yaa','yo','ok','yooman'):
                            os.startfile(ACTUAL_CWD+"/"+PATH_IMAGE+"/"+schNo+".jpg")
                            print("File Opened")
                        else:
                            print("Not opened")
                    else:
                        print("Some Error has Occured!")
                """
                if valid(schNo):
                    print("Fetching Started...")
                    truthness = ImageFetcher.getImageOfIndividual(ACTUAL_CWD,PATH_IMAGE,schNo)
                    if truthness:
                        print("Fetching Done. Fetched the Image of Scholar No. : ",schNo)
                        option = input("Want to open Image (y/n): ").strip()
                        if option.lower() in ('y','yes','yaa','yo','yoo','ok','yooman'):
                            os.startfile(ACTUAL_CWD+"/"+PATH_IMAGE+"/"+schNo+".jpg")
                            print("File Opened")
                        else:
                            print("Opening Failed!")
                    else:
                        print("Error-: Some Error has Occured!")
            if selectedOption.lower() in ('10','ir','imager','imgr','image in range'):
                schNoFrom = input("Enter Starting Scholar No. : ").strip()
                if valid(schNoFrom):
                    schNoTo = input("Enter End Scholar No. : ").strip()
                    if valid(schNoTo):
                        inc = input("Enter Steps to Increment. : ").strip()
                        if (inc.isdigit() and 0<int(inc)<100000) or inc == "":
                            if inc =="":
                                inc = 1
                            print("Fetching Started...")
                            truthness = ImageFetcher.getImageInRange(ACTUAL_CWD,PATH_IMAGE+"/"+schNoFrom+"-"+schNoTo,schNoFrom,schNoTo,inc)
                            if truthness:
                                print("Fetching is Done!")
                                option =  input("Want to open Containing Folder.(y/n) : ")
                                if option.lower() in ('y','yes','yaa','yo','ok','yooman'):
                                    os.startfile(ACTUAL_CWD+"/"+PATH_IMAGE+"/"+schNoFrom+"-"+schNoTo)
                                else:
                                    print("Opening Failed!")
                            else:
                                print("Fetching Failed!")
                                print("Error-: Some Error has Occured!")
                        else:
                            print("Error-: Increment is not proper!")
                    else:
                        print("Error-: Last Scholar No. is not Valid!")
                else:
                    print("Error-: Starting Scholar No. is not Valid!")
            #print("Looking")
            if selectedOption.lower() in ('1','2','1 2','2 1',
                                          'sgpa','cgpa','sgpa cgpa','cgpa sgpa','sc',
                                          'cs','sgpa of individual',' cgpa of individual',
                                          'sgpa of individual cgpa of individual'):
                listOption = {'1':'1','2':'2','1 2':'12','2 1':'21','sgpa':'1','cgpa':'2',
                              'sgpa cgpa':'12','cgpa sgpa':'21','sc':'12','cs':'21',
                              'sgpa of individual':'1',' cgpa of individual':'2',
                              'sgpa of individual cgpa of individual':'12',
                              'cgpa of individual sgpa of individual':'21'}
                semOption = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                             'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8}
                
                schNo = input("\nEnter Scholar No. : ").strip()
                if valid(schNo):
                    sem = input("\nEnter Semester : ").strip()
                    if sem in ('1','2','3','4','5','6','7','8','i','ii','iii','iv','v','vi','vii','viii'):
                        print("Fetching Started...")
                        #input("Look")
                        truthness = InfoCollector.option12(ACTUAL_CWD,PATH_SGPA_CGPA,
                                             schNo,semOption[sem],listOption[selectedOption.lower()])
                        if truthness:
                            print("Fetching is Done!")
                            selection = input("Want to open Result.(y/n) : ")
                            if selection in ('y','yes','yaa','yo','ok','yooman'):
                                #print("AMan")
                                print(ACTUAL_CWD+"/"+PATH_SGPA_CGPA+"/"+schNo+"-"+"Sem-"+str(sem)+".txt")
                                os.startfile(ACTUAL_CWD+"/"+PATH_SGPA_CGPA+"/"+schNo+"-Sem-"+str(semOption[sem])+".txt")
                            #input("Ruukja")
                        else:
                            print("Fetching Failed!")
                            print("Error-: Some Error has Occured!")
                    else:
                        print("Error-: Invalid Semester!")
                else:
                    print("Error-: Scholar No. Not Valid!")
            if selectedOption.lower() in ('3','4','3 4','4 3','sc r','cs r'
                                          'sgpa r','cgpa r','sgpa cgpa r','cgpa sgpa r',
                                          'sgpa in range','cgpa in range',
                                          'sgpa in range cgpa in range',
                                          'cgpa in range sgpa in range'):
                listOption = {'3':'3','4':'4','3 4':'34','4 3':'43','sgpa r':'3','cgpa r':'4',
                              'sgpa cgpa r':'34','cgpa sgpa r':'43','sc r':'34','cs r':'43',
                              'sgpa in range':'3',' cgpa in range':'4',
                              'sgpa in range cgpa in range':'34',
                              'cgpa in range sgpa in range':'43'}
                semOption = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                             'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8}
                schNoFrom = input("\nEnter starting Scholar No. : ").strip()
                if valid(schNoFrom):
                    schNoTo = input("Enter end Scholar No. : ").strip()
                    if valid(schNoTo):
                        sem = input("Enter Semenster : ").strip()
                        if sem in ('1','2','3','4','5','6','7','8','i','ii','iii','iv','v','vi','vii','viii'):
                            inc = input("Enter Increment : ").strip()
                            if ((inc.isdigit() and 0<int(inc)<10000)) or inc == "":
                                if inc == "":
                                    inc = 1
                                print("Fetching Started...")
                                truthness = InfoCollector.option34(ACTUAL_CWD,PATH_RESULT+"/"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])
                                                                   ,schNoFrom,schNoTo,inc,sem,listOption[selectedOption.lower()])
                                if truthness:
                                    print("Fecthing Done!")
                                    s="1) Open combined result file. \n2) Open Individual file Folder.\n3) Both 1 and 2\n4)Do Nothing.\n"
                                    option = input(s+"Enter Option : ").strip()
                                    print(option)
                                    if option.lower() == '1':
                                        print("Opening combined result file...")
                                        os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])+"/combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt")
                                        print("File Opened.")
                                    elif option.lower() == '2':
                                        print("Opening Individual file Folder...")
                                        os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem]))
                                        print("Folder Opened.")
                                    elif option.lower() == '3':
                                        os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])+"/combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt")
                                        os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem]))
                                        print("Opened both.")
                                    elif option.lower() == "4":
                                        pass
                                    else:
                                        print("Incorrect Input!")
                                else:
                                    print("Error-: Some Error Occured!")
                            else:
                                print("Error-: Increment Not Proper!")
                        else:
                            print("Error-: Semester is Not Valid!")
                    else:
                        print("Error-: End Scholar No. Not Valid!")
                else:
                    print("Error-: Starting Scholar No. Not Valid!")
            if selectedOption.lower() in ('5','result','result of individual'):
                #to change this listOption
                listOption = {'3':'3','4':'4','3 4':'34','4 3':'43','sgpa r':'3','cgpa r':'4',
                              'sgpa cgpa r':'34','cgpa sgpa r':'43','sc r':'34','cs r':'43',
                              'sgpa in range':'3',' cgpa in range':'4',
                              'sgpa in range cgpa in range':'34',
                              'cgpa in range sgpa in range':'43'}
                semOption = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                             'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8}
                
                schNo = input("\nEnter Scholar No. : ").strip()
                if valid(schNo):
                    sem = input("\nEnter Semester : ").strip()
                    if sem in ('1','2','3','4','5','6','7','8',
                               'i','ii','iii','iv','v','vi','vii','viii'):
                        print("Fetching Started...")
                        truthness = ResultCollector.option6(ACTUAL_CWD,PATH_RESULT,schNo,semOption[sem],listOption[selectedOption.lower()])
                        if truthness:
                            print("Fetching Done.")
                            option  = input("Want to Open File.(y/n) : ").strip()
                            if option.lower() in ('y','yes','yaa','yo','ok','yooman'):
                                os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNo+"-Sem-"+semOption[sem]+".txt",semOption[sem])
                                print("File Opened.")
                            else:
                                print("Not Open.")
                        else:
                            print("Error-: Some Error Occured!")
                    else:
                        print("Error-: Invalid Semester!")
                else:
                    print("Error-: Scholar No. valid!")

            if selectedOption.lower() in ('7','8','sort result on sgpa','sort sgpa','sort result on sgpa','sort cgpa'):
                listOption = {'7':0,'8':1,'sort result on sgpa':0,'sort sgpa':0,'sort result on sgpa':1,'sort cgpa':1}
                semOption = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                             'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8}
                schNoFrom = input("\nEnter Starting Scholar No. : ").strip()
                if valid(schNoFrom):
                    schNoTo = input("Enter End scholar No. : ").strip()
                    if valid(schNoTo):
                        sem = input("Enter Semester : ").strip()
                        if sem in ('1','2','3','4','5','6','7','8',
                                   'i','ii','iii','iv','v','vi','vii','viii'):
                            inc = input("Enter Increment : ").strip()
                            if (inc.isdigit() and 0<int(inc)<=10000) or inc =="":
                                if inc =="":
                                    inc =1 
                                print("Fetching Started...")
                                truthness = InfoCollector.option34(ACTUAL_CWD,PATH_RESULT+"/Sorted-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])
                                                                   ,schNoFrom,schNoTo,inc,sem,'34')
                                if truthness:
                                    print("Fecthing Done.")
                                    print("Sorting Started...")
                                    truthness = Sorter.sortResult(ACTUAL_CWD,PATH_RESULT+"/Sorted-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])
                                                                  ,schNoFrom,schNoTo,sem,listOption[selectedOption.lower()])
                                    
                                    
                                    if truthness:
                                        print("Sorting Done.")
                                        option = input("\nWant to open Sorted file(y/n) : ").strip()
                                        if option.lower() in ('y','yes','yaa','yo','ok','yooman'):
                                            print("Opening...")
                                            os.startfile(ACTUAL_CWD+"/"+PATH_RESULT+"/Sorted-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(semOption[sem])
                                                         +"/sorted-"+"combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt")
                                            print("Opened.")
                                        else:
                                            print("Done Sorting.")
                                    else:
                                        print("Sorting Failed")
                                        print("Error-: Some Error Occured While Sorting!")
                                else:
                                    print("Error-: Some Error Occured!")
                            else:
                                print("Error-: Increment Not Proper!")
                        else:
                            print("Error-: Invalid Semester!")
                    else:
                        print("Error-: End Schilar No. Not Valid!")
                else:
                    print("Error-: Starting Scholar No. Not Valid!")
            if selectedOption.lower() in ('update imageurl'):
                imageURL = input("Enter updated URL : ").strip()
                CONFIRM = input("Are you Sure to UPDATE Image Retrieval URL.(y/n) : ").strip()
                if CONFIRM.lower() == 'y':
                    createAttribute(attr_object.split(" ")[0],imageURL)
                    print("Successfully Updated Image Retrieval URL.")
                    print("Hope you have Updated it correctly else come here again.")
                else:
                    print("Try Again.")
            if selectedOption.lower() in ('update ResultURL'):
                resultURL = input("Enter updated URL : ").strip()
                CONFIRM = input("Are you Sure to UPDATE Result Retrieval URL.(y/n) : ").strip()
                if CONFIRM.lower() == 'y':
                    createAttribute(resultURL,attr_object.spilt(" ")[1])
                    print("Successfully Updated Result Retrieval URL.")
                    print("Hope you have Updated it correctly, else come here again.")
                else:
                    print("Try Again.")
            
                
    #optionD isplay()
    #noteDisplay()














