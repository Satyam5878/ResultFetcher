import urllib
import bs4
import os
#import main

from main import attr_object,createAttribute
if attr_object == "":
    createAttribute("http://dolphintechnologies.in/manit/accessview.php",
                         "http://manit.ecampuserp.com/assets/img/students")
    from main import attr_object,createAttribute
    print("Created URLs.")
    
#RESULT_URL = "http://dolphintechnologies.in/manit/accessview.php"
print("info "+attr_object)
RESULT_URL = attr_object.split(" ")[0]

#RESULT_URL = "http://dolphintechnologies.in/manit/accessview.php"
resultPage = ""
soup  = bs4.BeautifulSoup("")
name = "Not Available"
sgpa = "--"
cgpa = "--"
branch = "--"

branch_option = {"ARCHITECTURE":"AR","CIVIL ENGINEERING":"CE",
          "COMPUTER SCIENCE & ENGINEERING":"CSE",
          "ELECTRICAL ENGINEERING":"EE",
          "ELECTRONICS & COMMUNICATION ENGINEERING":"EC",
          "MECHANICAL ENGINEERING":"ME",
          "CHEMICAL ENGINEERING":"CHE",
          "MATERIAL SCIENCE AND METALLURGICAL ENGINEERING":"MSE"
          }
#architecture and planning is not found todo
def fetchResult(schNo,sem):
    print("1")
    data = {"scholar":schNo,"semester":sem}
    data_encoded = urllib.parse.urlencode(data)
    data_bytes = data_encoded.encode("utf-8")
    global resultPage
    try:
        resultPage = urllib.request.urlopen(RESULT_URL,data_bytes).read()
        #print(resultPage)
        global soup
        soup = bs4.BeautifulSoup(resultPage)
        print("123")
        print(" len "+str(len(resultPage))) 
    except urllib.error.URLError:
        print("Error-: URLError occured!")
        return False
    except urllib.error.HTTPError:
        print("Error-: HTTPError!")
        return False
    except IOError:
        print("Error-: IOError")
        return False
    print("2")
    return True
        
"""
def fetchName():
    return True
"""
def fetchName():
    tables = soup.find_all("table")
    for table in tables:
        t_rows = table.find_all("tr")
        for t_row in t_rows:
            td_string = t_row.find_all("td",text="Name:")
            if len(td_string) is 1:
                td_parent = td_string[0].find_parent("td")
                td_next_sibling = td_parent.find_next_sibling()
                string = td_next_sibling.string
                string = string.replace("\\r","").replace("\\n","").strip()
                global name
                name = string
                return True        
    print("Error-: Name not Found!")  
    return False
"""
def fetchSGPA():
    return True
"""
def fetchSGPA():
    strong  = soup.find_all("strong",text="SGPA: ")
    print(strong)
    if len(strong) is not 1:
        print("Error-: More than one SGPA")
    else:
        stong_parent_parent_content = strong[0].find_parent().find_parent().contents[2]
        string = stong_parent_parent_content.replace("\\r","").replace("\\n","").strip()
        global sgpa
        sgpa = string
        return True
        #print(len(span))
        #print(strong)
    return False
"""
def fetchCGPA():
    return True
"""
def fetchCGPA():
    strong = soup.find_all("strong",text="CGPA: ")
    if len(strong) is not 1:
        print("Error-: More then one CGPA!")
    else:
        stong_parent_parent_content = strong[0].find_parent().find_parent().contents[2]
        string = stong_parent_parent_content.replace("\\r","").replace("\\n","").strip()
        global cgpa
        cgpa = string
        return True
        #print(len(span))
        #print(strong)
    return False
"""
def fetchBranch():
    return True
"""
def fetchBranch():
    tables = soup.find_all("table")
    for table in tables:
        t_rows = table.find_all("tr")
        for t_row in t_rows:
            td_string = t_row.find_all("td",text="Branch:")
            if len(td_string) is 1:
                td_parent = td_string[0].find_parent("td")
                td_next_sibling = td_parent.find_next_sibling()
                string = td_next_sibling.string
                string = string.replace("\\r","").replace("\\n","").strip()
                global branch
                branch = string
                return True
    print("Error-: Branch Not Found!")
    return False
def option12_string_return(schNo,sem,option):
#initializing string for scholar no
    info_string = "| "+schNo.center(12)+"|"
    truthness = fetchResult(schNo,sem)                                      #fetching result
    soup.prettify().decode("utf-8")
    if truthness:
        truthness = fetchName()                                             #fetching name
        if truthness:
            info_string += name.center(51)+"|"
        else:
            info_string += "Not Retrieved".center(51)+"|"
        #if truthness:
        truthness = fetchBranch()                                           #fetching branch
        if truthness:
            print(branch)
            branch_name = "--"
            try:
                branch_name = branch_option[branch] #to change 1 to branch
            except:
                print("Error-: Branch Name Not Found!")
            info_string += branch_name.center(8)+"|"
        else:
            info_string += "NA".center(8)+"|"
        if option.find('1') is not -1:                                      #presence of option 1
           truthness = fetchSGPA()                                          #fetch SGPA
           if truthness:
               info_string += sgpa.center(6)+"|"
           else:       
               info_string += "--".center(6)+"|"
        else:
            info_string += "--".center(6)+"|"
        if option.find('2') is not -1:                                      #presence of option 2
            truthness = fetchCGPA()                                      #fetch CGPA
            if truthness:
                info_string += cgpa.center(6)+"|"
            else:
                info_string += "--".center(6)+"|"
        else:
            info_string += "--".center(6)+"|"
        #else:
            #print("Error-: While Fetching Name!")
    else:
        print("Error-: while Fetching Result!")
        return (info_string,False)
    return (info_string,True)

                                                            

    truthness = truthness and fetchName()
    truthne
    


def option12(ACTUAL_CWD,PATH_RESULT,schNo,sem,option):
    s1 = " ________________________________________________________________________________________\n| Scholar No. |"+24*" "+"NAME"+23*" "+"| Branch | SGPA | CGPA |\n"
    s2= "|_____________|"+51*"_"+"|________|______|______|\n"
    info_string,truthness = option12_string_return(schNo,sem,option)
    info_string = s1+s2+info_string+"\n"+s2
    print("Some Thing")
    if truthness:
        try:
            """
            with open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNo+"-"+sem+"sem.txt",'w') as file_obj:
                file_obj.write(info_string)
            """   
            file_obj = open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+schNo+"-"+"Sem-"+str(sem)+".txt",'w')
            file_obj.write(info_string)
            file_obj.close()
        except IOError:
            print("Error-: Input Output Error")
    else:
        print("Error-: Result of scholar No. :"+schNo+" Not Fetched!")
        return False
    return True

def option34(ACTUAL_CWD,PATH_RESULT,schNoFrom,schNoTo,inc,sem,option):
    s0 = " ________________________________________________________________________________________\n"
    s1 = "RESULT".center(90,"_")+"\n"
    s2 = "| Scholar No. |"+24*" "+"NAME"+23*" "+"| Branch | SGPA | CGPA |\n"
    s3= "|_____________|"+51*"_"+"|________|______|______|"
    
    header_string = s0+s1+s0 + s0+s2+s3
    combined_string = header_string
    print("cpmbined _sreing Says :\n"+combined_string)
    #create folder
    
    try:
        os.makedirs(ACTUAL_CWD+"/"+PATH_RESULT)
        print("Path : "+ACTUAL_CWD+"/"+PATH_RESULT+" :: Creating directory for range.")
    except:
        print("Path : "+ACTUAL_CWD+"/"+PATH_RESULT+" :: directory for range Already exist.")
    
    #os.makedirs(ACTUAL_CWD+"/"+PATH_RESULT)
    #print("Path : "+ACTUAL_CWD+"/"+PATH_RESULT+" :: Creating directory for range.")
    #creating combined file
    #file_obj = open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+"combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt",'w')
    #file_obj.write(combined_string)
    
    try:
        file_obj = open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+"combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt",'w')
        print(ACTUAL_CWD+"/"+PATH_RESULT+"/"+"combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt")
        #file_obj.write(combined_string)
    except:
        print("Error-:x Input Output Error!")
        return False
    
    #adjusting schNos.
    if int(schNoFrom)<int(schNoTo):
        pass
    else:
        schNoFrom,schNoTo = schNoTo,schNoFrom
    #replacing 3 by 1 and 4 by 2
    print("option says : "+ option)
    if option.find("3") is not -1:
        option = option.replace('3','1')
    else:
        print("Gadbad")
    if option.find("4") is not -1:
        option = option.replace('4','2')
    else:
        print("Gadbad")
    print("option says 2: "+ option)

    unretrievedItem = []
    for item in range(int(schNoFrom),int(schNoTo)+1,int(inc)):
        print("Retrieving : ",item,end=" ")
        info_string,truthness = option12_string_return(str(item),sem,option)
        if truthness:
            print(info_string)
            combined_string = combined_string+"\n"+info_string
            print("Retrieved X:",item)
            print(ACTUAL_CWD+"/"+PATH_RESULT+"/"+str(item)+"-Sem-"+str(sem)+".txt")
            
            try:
                print(ACTUAL_CWD+"/"+PATH_RESULT+"/"+str(item)+"-Sem-"+str(sem)+".txt")
                file_obj_individual = open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+str(item)+"-Sem-"+str(sem)+".txt",'w')
                file_obj_individual.write(s0+s2+s3+info_string+"\n"+s3)
                file_obj_individual.close()
            except:
                unretrievedItem.append(item)
                print("Error-:x Input Ouptput Error! for scholar No. : ",item)
        else:
            print("Error-: Some Error Occured!")
            unretrievedItem.append(item)

    count = 3
    if not len(unretrievedItem) is 0:
        while count:
            new_unretrievedItem = []
            for item in unretrievedItem:
                 print("Retrieving : ",item,end=" ")
                 info_string,truthness = option12_string_return(str(item),sem,option)
                 if truthness:
                     combined_string = combined_string+info_string
                     print("Retrieved :",item)
                     try:
                         file_obj_individual = open(ACTUAl_CWD+"/"+PATH_RESULT+"/"+str(item)+"-Sem-"+str(sem)+".txt",'w')
                         file_obj_individual.write(s0+s2+s3+info_string+s3)
                         file_obj_individual.close()
                     except:
                         new_unretrievedItem.append(item)
                         print("Error-: Input Ouptput Error! for scholar No. : ",item)
                 else:
                     print("Error-: Some Error Occured!")
                     new_unretrievedItem.append(item)
            count -= 1
            unretrievedItem = new_unretrievedItem
        print("Some result are not fetched.")
        return True
            
    else:
        print("Range Done!")
    file_obj.write(combined_string+"\n"+s3)
    file_obj.close()
    return True
        

























    
