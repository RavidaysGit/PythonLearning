# String methods

str = "python learning examples examples"
dic = {'name':'ravi'}

print("len : ",len(str)) # output : 33 , length of the string.
print("format ","The sum of 1 + 2 is {0}".format(1+2))  # output : The sum of 1 + 2 is 3

print(str.capitalize()) # output : Python learning examples examples, This method will make the first character in to upper case.
print("istitle :" ,"Ravikumar".istitle()) # output :True, This methid will check the first character is upper case or not.
print("count :", str.count("examples"[1:4])) # output : 2 (xam) ,This method will count the no.of time the substring available in the main string.
print("endswith : ",str.endswith("examplespractice"[0:8])) #output : True , because str string ending with the 'examples'.
print("startswith :",str.startswith("python"))  #output : True , This method will check whether the main string start with the sub string or not.
print("expandtabs : ","ravi\tkumar\tnarahari".expandtabs(1)) #output : ravi kumar narahari , this method it will replace the '\t' to give no.of spaces(here 1)
print("find ", str.find("examplespractice"[0:8])) # output :16 , This method will find the sub string and return the first sub starting index ,if the sub string not found it will return -1.
print("rfind : ", str.rfind("examples"[1:4]))# output : 26 , This method return last matching sub string index.if the sub string not found it will return -1.
print("index : ",str.index("examplespractice"[0:8])) #output :16 , This method will find the sub string and return the first sub starting index',if the sub string not found then method will return 'substring not found' exception.
print("rindex : ",str.rindex("examples"[1:4])) # output : 26 , This method return last matching sub string index.if the sub string not found then method will return 'substring not found' exception.
print("isalnum : ",str.isalnum()) #False , return True if the str is alpha numeric string , other False
print("isalpha : ",str.isalpha()) #False , return True if the str is alpha string , other False, not even space or any other special characters
print("isalpha : ","pythonlearningexamplesexamples".isalpha()) #True , return True if the str is alpha string , other False
print("isascii : ",str.isascii()) # True ,Return True if all characters in the string are ASCII, False otherwise.
print("isascii : ","python learning éxamples examples".isascii()) #False , because string have non ascii caharacer 'é'
print("isidentifier :" , "True".isidentifier())  # output :True
print("islower :" ,"ravi kumar".islower())  # output :True
print("isdecimal : " ,"23.23".isdecimal())  # output :True
print("isdigit :","123".isdigit())  # output :True
print("isnumeric :" , "1234".isnumeric())  # output :True
print("isspace :"," ".isspace())  # output :True
print("isupper","RAVI".isupper()) # output :True
print("lower : ","RAVI".lower()) #output : ravi
print(":".join(["test1","est2", "test3"])) #output : test1:est2:test3
print("isprintable : ",str.isprintable()) # output : True
print("lstrip :","  ravi  ".lstrip()) # output :ravi  
print("rstrip :","  ravi  ".rstrip()) # output :  ravi
print("strip :","  ravi  ".strip())   #output:ravi
print("partition :",str.partition(" ")) # Split the string at the first occurrence (left most string) of sep
print("partition :",str.rpartition(" "))# Split the string at the last occurrence (right most string) of sep
print("replace : ",str.replace("examples", "programs",2)) # outout : python learning programs programs
print("rsplit :", str.rsplit(" ")) # outout : ['python', 'learning', 'examples', 'examples']
print("split :",str.split(" "))# outout :  ['python', 'learning', 'examples', 'examples']

strr = """hi this is ravi kumar
hi this is tes2
hi this is test3
"""
print("splitlines : ",strr.splitlines()) # output : ['hi this is ravi kumar', 'hi this is tes2', 'hi this is test3']
strr = """hi this is ravi kum\nar
hi this is t\res2
hi this is test3
"""
print("splitlines : ",strr.splitlines(keepends=True)) # output : ['hi this is ravi kumar', 'hi this is tes2', 'hi this is test3']
print("zfill : ",str.zfill(40)) # output :  0000000python learning examples examples , zero in the benining of the string ,because Pad a numeric string with zeros on the left, to fill a field of the given width.
print("rjust :",str.rjust(40)) #output :       python learning examples examples, This method Pad space in the left side of the main string.
print("ljust : ",str.ljust(40)) #output :python learning examples examples       , This method Pad space in the right side of the main string.
print("center :" ,str.center(40, '0')) #outout : 000python learning examples examples0000

str_sp_ch="python,lea≥rnin®g,éx€amples,eáx@a≤mpl¼∇eâs"

dic1={'é':'e','≤':'','≥':'','∇':'','á':'','â':'','®':'','¼':'','€':'','@':''}
#thebeow 2 methods are comibnation to remove some special characters from the files/line of string
ms1 = str_sp_ch.maketrans(dic1) # To create table we need use this method
print(str_sp_ch.translate(ms1)) # output : python,learning,examples,examples ,To replace the character from main string using the table which created by maketrace() methos



# need to understand more on the below methods
#============================================
#print("encode :",str.encode(encoding="utf-8", errors="strict")) #output : b'python learning examples examples',
#print(str.casefold())
#print("{0} staying in benglore".format_map(dic.get()))

