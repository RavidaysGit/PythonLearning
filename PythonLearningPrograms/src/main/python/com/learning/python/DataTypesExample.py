#Data Types 
'''
1.    None        : (like null in java) 'if you not assigned any value to the variable,iterater will considered as None'
2.    Numeric     :
                    i.     int (like 2,3,4,..values)
                    ii.    float (like ,2.3,45.5,45.0...values)
                    iii.    complex (like a+bj (6+9j))
                    iv.    bool (boolean) (like True->1 , False->0)
            Number system
                    i. Binary number :  convert number to binBinaryary using bin() method
                    ii. Octal number  : convert number to Octal using oct() method
                    iii. HexaDecimal number  : convert number to Octal using oct() method
under Sequence
    3.    Array (import array)
    4.    List
    5.    Tuple
    6.    Set
    7.    String
    8.    Range

9.    Dictionary
'''
#Examples
#1. None

name = "employee Name"
age= None #The None keyword is used to define a null value, or no value at all.
print(name,age)

#2.Numeric
int_var = 20
float_var = 100.23
comp_var = 10+20j
bool_var = (1==1)
bi_var = bin(10)
oct_vat = oct(12)
hex_var = hex(10)

print(f'Age : {int_var}, salary : {float_var} , complexValue : {comp_var} , booleanValue : {bool_var}')
print(f'{bi_var},  {oct_vat},  {hex_var}')

# Convert String to int, string to float values
str_to_int = "35"
print(int(str_to_int)) # string to int
print(float(str_to_int)) # string to float


# arrays
import array as arr 
arr1 = arr.array('i',[1,2,3,4,3])
print("type : ",type(arr1))
arr1.append(20),print("append: ",arr1) #append the value at the end of the array
print("count :",arr1.count(3)) # no.of time the value is available in the array
#print(arr1.buffer_info())
arr1.extend([12,13]),print("extend: ",arr1) # extend:  array('i', [1, 2, 3, 4, 3, 20, 12, 13]) , if you want to add more than one value then we can use extend method
#arr1.frombytes(buffer)
arr1.fromlist([50,60,70]),print("fromlist : ",arr1) #array('i', [1, 2, 3, 4, 3, 20, 50, 60, 70])
arr1.insert(1, 100),print("insert : ",arr1) #array('i', [1, 100, 2, 3, 4, 3, 20, 50, 60, 70])
print(arr1[3])
print(arr1.index(3)) # 3
print(arr1.itemsize) # 4
print(arr1.pop(1)) # 100
arr1.remove(3),print(arr1) # array('i', [1, 2, 4, 3, 20, 50, 60, 70])
arr1.reverse(),print(arr1) # array('i', [70, 60, 50, 20, 3, 4, 2, 1])
print(len(arr1)) # 8 , size of the array

#list
print("=========List===============")

l = [12,"ravi",12.23,968678666]
print(type(l)) # <class 'list'>
print(l) # [12, 'ravi', 12.23, 968678666]
print(l[3])
l.extend(["ravi",32,232.43]),print(l) # output : [12, 'ravi', 12.23, 968678666, 'ravi', 32, 232.43]
l.append(5000),print(l) # output : [12, 'ravi', 12.23, 968678666, 'ravi', 32, 232.43, 5000]
l.insert(0,"test23"),print(l) # output : ['test23', 12, 'ravi', 12.23, 968678666, 'ravi', 32, 232.43, 5000]
print("index :",l.index(12.23,3,6))

#Set
print("===========Set==========")
se = {"ravi",23,34.34,"ravi",23,}
print(se)
print()
se.add("kumars"),print(se)
se.remove(23),print(se)

#tuple
print("========tuple=========")

t = (23,23,23,45,45,"ravi",23.343)
print(t)
print(t[5])
print("count :",t.count(23))
print("index :",t.index(23,1,4))

#range
print("=======Range===========")

r = range(12,23)
l = list(range(1,10,4))
print(l)

#Dictionary
print("==========Dictionary============")

d1 = dict() 
print(d1) #output : {}
d2 = {"name":"ravi","age":23,"sal":23.34,"phone":98989989898} 
print(d2) # output : {'name': 'ravi', 'age': 23, 'sal': 23.34, 'phone': 98989989898}
print("d2[] :",d2["name"]) # ravi , will return the error, if dont have the given key
print("get :",d2.get("name")) # ravi, get will return 'None', if dont have the given key
print("get :",d2.get("names","no key available")) # output no key available
print("keys :",type(d2.keys())) #dict_keys(['name', 'age', 'sal', 'phone'])
print("values :",type(d2.values())) #dict_values(['ravi', 23, 23.34, 98989989898])
print("items :",d2.items()) # dict_items([('name', 'ravi'), ('age', 23), ('sal', 23.34), ('phone', 98989989898)])


keys = ["ravi","kumar"]
values=["java","python"]
dic =dict(zip(keys,values)) # creating the dictionary using 2list(key , value)
print(dic)  #{'ravi': 'java', 'kumar': 'python'}

dic['ram'] ='bigdata'  # adding the key value to the existing dictionary
print(dic)     #{'ravi': 'java', 'kumar': 'python', 'ram': 'bigdata'}

del dic['ram'] # remove the key value from the existing dictionary
print(dic)     # {'ravi': 'java', 'kumar': 'python'}

dic1 = {"quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        }
        }
    }
print(dic1) #{'quiz': {'sport': {'q1': {'question': 'Which one is correct team name in NBA?', 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'], 'answer': 'Huston Rocket'}}}}

print(dic1['quiz']['sport']['q1']['options'][0]) # New York Bulls , it alloes json format of the data
