
import re


def regex_PakistanNumbers(string):
    numbers = []
    regular_expression = r'[0 | +92]-?\d{2,3}-?\d{3}-?\d{4}'
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        numbers.append(match)

    return numbers

#print(regex_PakistanNumbers("03332774967"))


# umer@gmail.com
def regex_Emails(string):
    emails = []
    regular_expression = r'[a-zA-z0-9_.]+@[a-zA-Z0-9_]+(\.[a-zA-Z0-9]{2,3}){1,}'
    
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        emails.append(match)

    return emails

#print(regex_Emails("umer.farooq@technogenics.edu.pk"))
    

# question means (s) exist or not.
# http://www.example.com/index.html
def regex_WebURLS(string):
    urls = []
    regular_expression = r'(http(s)?\:\/\/)?www\.[a-zA-z0-9]+\.[a-zA-Z0-9]{2,}(\/?[a-zA-Z0-9=\-]+){1,}(\.[a-zA-Z0-9]{2,})?'
    #regular_expression = r'http(s)'
    
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        urls.append(match)

    return urls


#print(regex_WebURLS(data))


# 0.0.0.0
# 255.255.255.255
# [0-5][0-9]
def regex_IPAddresses(string):
    ip_addresses = []
    #regular_expression = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    regular_expression = r'(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])'
    
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        ip_addresses.append(match)

    return ip_addresses

print(regex_IPAddresses("10.0.0.0"))

def regex_Hashtags(string):
    hashtags = []
    regular_expression = r'#[a-zA-Z0-9]+'
    
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        hashtags.append(match)
        
    
    return hashtags

#print(regex_Hashtags("#iuoiulkn"))

data = r"""
www.google.com
www.youtube.com/alibaba
www..google.com/asdsa
This is the only way to code this problem.
https://www.example.com/ds/sd=90-k.aps

A:\Documents\Newsletters\assignment.doc

B:\Documents\Newsletters\Summer2018.pdf
C:Projects\apilibrary\apilibrary.sln
..\Publications\TravelBrochure.pdf
2018\January.xlsx
\Program Files\Custom Utilities\StringFinder.exe
D:\Games\Ultimate Man\play.exe

"""

# C:\Documents\Newsletters\Summer2018.pdf

def regex_WindowsFilePaths(string):
    paths = []
    regular_expression = r'[A-Z]:(\\?\\?[a-zA-Z0-9\s]+)+(\.[a-zA-Z0-9]{2,})?'
    
    pattern = re.compile(regular_expression)
    matches = pattern.finditer(string)
    
    for match in matches:
        paths.append(match)
     
    #print(paths)
    return paths


#regex_WindowsFilePaths(data)
    
    

    
    
    
    
    
    
    
    
    






        