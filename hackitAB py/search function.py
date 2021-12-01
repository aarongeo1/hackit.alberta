import csv

returnDict = {}

def search(courselist,term):
    word = term
    cname = []
    word1 = word.lower().split()
        
    for i in courselist:
        k = i[3].lower().split()
        l=len(word1[0])
        for p in k:
            if p[0:l] == word1[0] and i[0]+" "+i[1] not in cname: 
                cname.append(i[0]+" "+i[1])
    cnamefinal = []
    def check(courselist,cname,cnamefinal,word):
        
        for i in courselist:
            k = i[3].lower().split() 
            l=len(word)
            for p in k:
                if p[0:l] == word and i[0]+" "+i[1] in cname and i[0]+" "+i[1] not in cnamefinal : 
                    cnamefinal.append(i[0]+" "+i[1])
                

    if len(word1) > 1:
        cnamefinal = []
        for i in range(1,len(word1)):
            check(courselist,cname,cnamefinal,word1[i])
            cname = cnamefinal
            cnamefinal = []
        return cname
    else:
        return cname

def dict_convert(courselist,list1):
    list2 = []
    for i in list1:
        for j in courselist:
            if i == j[0]+" "+j[1]:
                list2.append(j)
    return list2
    
    
def MAIN(returnDict,word):      
    for uni in (['University of Alberta',"ualberta.csv"],['University of Calgary',"ucalgary.csv"],['SAIT',"sait.csv"]) :
            courselist = []
            with open(uni[1],encoding = "utf8") as f:
                reader = csv.reader(f,delimiter=",")
                for i in reader:
                    courselist.append(i)
            list1 = search(courselist,word)
            returnDict[uni[0]] = dict_convert(courselist,list1)
    print(returnDict)
    return returnDict

term = input("Enter the word : ")
MAIN(returnDict,term)
    
    


        
