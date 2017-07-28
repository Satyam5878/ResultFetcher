"""
File for Retrieving Images
"""
import urllib.request
import os

from main import attr_object,createAttribute
if attr_object == "":
    createAttribute("http://dolphintechnologies.in/manit/accessview.php",
                         "http://manit.ecampuserp.com/assets/img/students")
    from main import attr_object,createAttribute
    print("Created URLs.")
    
#RESULT_URL = "http://dolphintechnologies.in/manit/accessview.php"
print("img "+ attr_object)
BASE_URL = attr_object.split(" ")[1]
#BASE_URL ="http://manit.ecampuserp.com/assets/img/students" 

#BASE_URL ="http://manit.ecampuserp.com/assets/img/students" 
def getImageOfIndividual(ACTUAL_CWD,IMAGE,SchNo):
    try:
        img_obj = urllib.request.urlopen(BASE_URL+"/"+str(SchNo)+".jpg",timeout=5)
        #print(ACTUAL_CWD+"/"+IMAGE+"/"+str(SchNo)+".jpg")
        file_obj = open(ACTUAL_CWD+"/"+IMAGE+"/"+str(SchNo)+".jpg",'wb')
        file_obj.write(img_obj.read())
        file_obj.close()
    except urllib.error.URLError:
        print("Error-: URLError Occured!")
        return False
    except urllib.error.HTTPError:
        print("Error-: HTTPError Occured!")
        return False
    except IOError:
        print("Error-: Input Output Error occured!")
        return False
    except :
        print("Error-: Some Error occured!")
        return False
    #print("Here")
    return True

def getImageInRange(ACTUAL_CWD,IMAGE,SchNoFrom,SchNoTo,increment = 1):
    #print("SOME :" ,ACTUAL_CWD+"1")
    try:
        os.makedirs(ACTUAL_CWD+"/"+IMAGE)
        print("Path :" +ACTUAL_CWD,"/"+IMAGE +" :: Creating inner Directory.")
        #os.makedirs(ACTUAL_CWD,"/"+IMAGE+"/"+SchNoFrom+"-"+SchNoTo)
        #print("Path : "+ACTUAL_CWD,"/"+IMAGE+"/"+SchNoFrom+"-"+SchNoTo+" Creating inner Directory.")
    except:
        #print("Path : "+ACTUAL_CWD,"/"+IMAGE+"/"+SchNoFrom+"-"+SchNoTo+" Inner Directory Already Exist.")
        print("Path :" +ACTUAL_CWD,"/"+IMAGE +" ::  Inner Directory Already Exist.")
    if int(SchNoFrom)<=int(SchNoTo):
        pass
    else:
        SchNoFrom,SchNoTo = SchNoTo,SchNoFrom
    
    unretrievedItem = []
    """
    while count:
        for item in range(int(SchNoFrom),int(SchNoTo)+1,int(increment)):
            print("Retriveing :",SchNoFrom,end=", ")
            truthness = getImageOfIndividual(ACTUAL_CWD,IMAGE,item)
            print("Retrieved : ",SchNoTo)
            if not truthness:
                unretrievedItem.append(item)
        if len(unretrievedItem) is 0:
            print("range Done!")
            return True
        count-= 1
    """
    for item in range(int(SchNoFrom),int(SchNoTo)+1,int(increment)):
            print("Retriveing :",item,end=", ")
            truthness = getImageOfIndividual(ACTUAL_CWD,IMAGE,item)
            if not truthness:
                unretrievedItem.append(item)
            else:
                print("Retrieved : ",item)
                
    count = 3
    if not len(unretrievedItem) is 0:
        while count:
            new_unretrievedItem = []
            for item in unretrievedItem:
                print("Retrieving :",item,end=", ")
                truthness = getImageOfIndividual(ACTUAL_CWD,IMAGE,item)
                
                if not truthness:
                    new_unretrievedItem.append(item)
                else:
                    print("Retrieved : ",item)
            count -= 1
            unretrievedItem = new_unretrievedItem
        print("Some Items are Not Retrieved!")
        return True
    else:
        print("Range Done!")
        return True   

if __name__=='__main__':
    getImageOfIndividual(os.getcwd(),"",'141112216')








