#Remove duplicate from
from importlib.metadata import unique_everseen

my_dict={"a":1,"b":2,"c":1,"d":3}
#output={"a":1,"b":2,"d":3}
unique_value=set()
result={}
for key,value in my_dict.items():
    if value not in unique_value:
        result[key]=value
        unique_value.add(value)
print(result)