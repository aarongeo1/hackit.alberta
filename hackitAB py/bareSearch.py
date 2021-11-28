import pandas as pd
sait_data = pd.read_csv("sait.csv")
ua_data = pd.read_csv("ualberta.csv")
uc_data = pd.read_csv("ucalgary.csv")
uc_data.dropna(subset = ["Course Desc"], inplace=True)
ua_data.dropna(subset = ["Course Desc"], inplace=True)
sait_data.dropna(subset = ["Course Desc"], inplace=True)

def searchCourse(dframe,term):
    print(type(dframe))
    x = dframe["Course Desc"].str.contains(term)
    print(type(dframe))
    print(type(x))
    return dframe[dframe['Course Desc'].str.contains(term)]

def multisearch(term):
    returnDict = {}
    returnDict['University of Alberta'] = searchCourse(ua_data,term).values.tolist()
    returnDict['University of Calgary'] = searchCourse(uc_data,term).values.tolist()
    returnDict['SAIT'] = searchCourse(sait_data,term).values.tolist()
    return returnDict
