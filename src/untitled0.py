# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 08:46:16 2016

@author: vmuriart
"""

import re

path = r'.\sql2003.grako'

with open(path) as f:
    b = f.read()

regex = re.compile(r'((.*) =\s+(\w+)\s*;\n)')
found = regex.findall(b)
# print found
names = []
news = []


for def_, name, new in found:
    if name == 'start':
        continue
    names.append(name), news.append(new)

for def_, name, new in found:
    if name == 'start':
        continue
    if name in news:
        continue
    b=re.sub('\n' + def_+'\n', '\n', b)
    b=re.sub(' ' + name + ' ', ' ' + new + ' ', b)
    b=re.sub(' ' + name + '\n', ' ' + new + '\n', b)    
    b=re.sub('\[' + name + '\]', '[' + new + ']', b)        
    b=re.sub(' ' + name + '\]', ' ' + new + ']', b)        
    b=re.sub('\[' + name + ' ', '[' + new + ' ', b)        
    b=re.sub('{' + name + '}', '{' + new + '}', b)        
    b=re.sub('{' + name + ' ', '{' + new + ' ', b)        
    b=re.sub(' ' + name + '}', ' ' + new + '}', b)        
    b=re.sub('\(' + name + '\)', '(' + new + ')', b)        
    b=re.sub(' ' + name + '\)', ' ' + new + ')', b)        
    b=re.sub('\(' + name + ' ', '(' + new + ' ', b)        
    

with open(path, 'w') as f:
    f.write(b)



"""

import re

path = r'.\sql92.grako'

with open(path) as f:
    b = f.read()

regex = re.compile(r'(.*) =\n')
found = regex.findall(b)

res = {}
for def_ in found:
    regex = re.compile(r'\b' + def_ + r'\b')
    res[def_] = len(regex.findall(b))




regex = re.compile(r'((.*) =\s+(.*?)\s*;\n)')
# regex = re.compile(r'((.*) =\s+(.*?\s+.*?)\s*;\n)')
# regex = re.compile(r'((.*) =\s+(.*?\s+.*?\s+.*?)\s*;\n)')

found = regex.findall(b)
#print found
names = []
news = []


for def_, name, new in found:
    if name == 'start':
        continue
    if name in ['start', 'regular_identifier', 'temporary_table_declaration',
'large_object_length_token',  'with_list',   'day_time_interval',  'dereference_operator'  ,       
                'delimited_identifier', 'multiple_group_specification', 'in_value_list'
    ]:
        continue
    
    if 'statement' in name:
        continue
    
    if 'list' in name:
        continue    
    
    if 'clause' in name:
        continue

    if 'literal' in name:
        continue


    if 'type' in name:
        continue
    
    
    if 'join' in name:
        continue    
    
    names.append(name), news.append(new)  

#print names        

#with open(path, 'w') as f:
#    f.write(b)


to_do = []

for key, value in res.items():
    if key == 'start':
        continue
    
    if value > 2 or key not in names:
        continue
    to_do.append(key)


for def_, name, new in found:
    if name in ['start', 'regular_identifier', 
    
'window_definition'    ,'window_function',
    
    'temporary_table_declaration', 'time_zone_interval','repeat_factor',
'large_object_length_token', 'with_list', 'time_value',    'day_time_interval',  'dereference_operator'  ,       
                'delimited_identifier', 'multiple_group_specification', 'in_value_list'
    ]:
        continue
    
    if 'statement' in name:
        continue
    
    if 'clause' in name:
        continue

    if 'literal' in name:
        continue

    if 'regular' in name:
        continue


 
    if 'type' in name:
        continue
    
    if 'list' in name:
        continue
    
    if 'join' in name:
        continue
    
    if 'unquoted' in name:
        continue
    
    def temp():
        for x in news:
            if name in x:
                return True
            
    #if temp():
    #    continue
    

    
    if name not in to_do:
        continue
    print name
    # print def_
    b=b.replace('\n' + def_+'\n', '\n')
    b=b.replace(' ' + name + ' ', ' ' + new + ' ')
    b=b.replace(' ' + name + '\n', ' ' + new + '\n')    
    b=b.replace('[' + name + ']', '[' + new + ']')        
    b=b.replace(' ' + name + ']', ' ' + new + ']')        
    b=b.replace('[' + name + ' ', '[' + new + ' ')        
    b=b.replace('{' + name + '}', '{' + new + '}')        
    b=b.replace('{' + name + ' ', '{' + new + ' ')        
    b=b.replace(' ' + name + '}', ' ' + new + '}')        
    b=b.replace('(' + name + ')', '(' + new + ')')        
    b=b.replace(' ' + name + ')', ' ' + new + ')')        
    b=b.replace('(' + name + ' ', '(' + new + ' ')        


with open(path, 'w') as f:
    f.write(b)
"""