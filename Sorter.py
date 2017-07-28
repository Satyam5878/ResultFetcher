import os

def sortResult(ACTUAL_CWD,PATH_RESULT,schNoFrom,schNoTo,sem,option):
    s0 = " ________________________________________________________________________________________\n"
    s1 = "RESULT".center(90,"_")+"\n"
    s2 = "| Scholar No. |"+24*" "+"NAME"+23*" "+"| Branch | SGPA | CGPA |\n"
    s3= "|_____________|"+51*"_"+"|________|______|______|"
    header_string = s0+s1+s0 + s0+s2+s3
    combined_string = header_string +"\n"
    data_store = []
    
    try:
        file_obj = open(ACTUAL_CWD+"/"+PATH_RESULT+"/"+"combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt",'r')
        
        file_obj_sort = open(ACTUAL_CWD+"/"+PATH_RESULT+"/sorted-combined-"+schNoFrom+"-"+schNoTo+"-Sem-"+str(sem)+".txt",'w')
        for item in range(6):
            file_obj.readline()
        while 1:
            line = file_obj.readline()
            if line == "":
                break
            tupleItem = line.split('|')
            tupleItem = tupleItem[1:len(tupleItem)-1]
            tupleItem_strip = []
            if len(tupleItem) is not 0:
                for item in tupleItem:
                    tupleItem_strip.append(item.strip())
                #tupleItem = tupleItem[1:len(tupelItem)-1]
                data_store.append(tupleItem_strip)
        if option is 0:
            data_store = sorted(data_store,key=lambda li:li[3],reverse=True)
            #pass #sort on sgpa
        if option is 1:
            data_store = sorted(data_store,key=lambda li:li[4],reverse=True)
            #pass#sort on cgpa
        for line in data_store:
            sch = "|"+line[0].center(13)+"|"
            name = line[1].center(51)+"|"
            branch = line[2].center(8)+"|"
            sgpa = line[3].center(6)+"|"
            cgpa = line[4].center(6)+"|\n"
            combined_string += sch+name+branch+sgpa+cgpa
        combined_string += s3
        file_obj_sort.write(combined_string)
        file_obj.close()
        file_obj_sort.close()
        return True
    except Exception as e:
        print(e)
        print("Error-: Input Output Error!")   
    return False

if __name__=='__main__':
    file = open("C:\\Users\\Aman\\Desktop\\ManitResultFetcher\\Result\\Sorted-141112216-141112225-Sem-4\\combined-141112216-141112225-Sem-4.txt",'r')
    #help(file)C:\Users\Aman\Desktop\ManitResultFetcher\Result\Sorted-141112216-141112225-Sem-4
    #print(file.readlines(7))
    data_store = []
    for i in range(6):
        (file.readline())
        #pass
    while 1:
        s = file.readline()
        if s =="":
            break
        l = file.readline().split('|')
        l = (l[1:len(l)-1])
        #print("here is "+str(l))
        l_strip = []
        if len(l) is not 0:
            for i in l:
                l_strip.append(i.strip())
                    #print(l_strip)
                #print(l_strip)
            data_store.append(l_strip)
        else:
            print("List l is zero")
    #print(data_store)
    for item in data_store:
        print(item)
    sorted(data_store,key=lambda li:li[3],reverse=True)
    for item in data_store:
        print(item)
    print("Done")
