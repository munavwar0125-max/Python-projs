import json
eapcet='''
{
"clgs" :
[
    {"name":"Vit" ,"location" :"amaravati","time":"7-10"  },
    {"name" :"Vvit","location":null, "time":"8-3"},
    {"name" :"KITS" ,"location":"vinjanampadu" ,"time":"9-6"}
]    
}
'''
data=json.loads(eapcet)
print(data)
for clg in data['clgs']:
    print(clg['name'])
    del clg['location']
info=json.dumps(data,indent=2)    
print(info)