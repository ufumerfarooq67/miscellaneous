import Regular_Expressions as re



def showAllURLs(data,label):
    matchesList = re.regex_WebURLS(data)
    
    for i,eachMatch in enumerate(matchesList):
        print(label+"# ",i+1,": ",eachMatch[0])
        
        
def showAllIPAddresses(data,label):
    matchesList = re.regex_IPAddresses(data)
    
    for i,eachMatch in enumerate(matchesList):
        if i ==100:
            break
        print(label+" # ",i+1,": ",eachMatch[0])
      
    
def showAllPakistanMobileNumbers(data,label):
    matchesList = re.regex_PakistanNumbers(data)
    
    for i,eachMatch in enumerate(matchesList):
        print(label+" # ",i+1,": ",eachMatch[0])
        
        
def showAllEmailAddresses(data,label):
    matchesList = re.regex_Emails(data)
    print(len(matchesList))
    for i,eachMatch in enumerate(matchesList):
        print(label+" # ",i+1,": ",eachMatch[0])
        
        
def showAllHashtags(data,label):
    matchesList = re.regex_Hashtags(data)
    for i,eachMatch in enumerate(matchesList):
        print(label+" # ",i+1,": ",eachMatch[0])    
        
        
def showAllWindowsPaths(data,label):
    matchesList = re.regex_WindowsFilePaths(data)
    for i,eachMatch in enumerate(matchesList):
        print(label+" # ",i+1,": ",eachMatch[0])    
        


    
    
if __name__ == "__main__":
    data = None
    with open("htmlData.txt","r+") as html:
        data = str(html.readlines())
 
    
    #showAllURLs(data,"URLs")
    showAllIPAddresses(data,"IP")
    #showAllPakistanMobileNumbers(data,"Mobile #")
    #showAllEmailAddresses(data,"Email Address")
    #showAllHashtags(data,"Hashtag")
    #showAllWindowsPaths(data,"Path")
    