# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:30:32 2021

@author: optim
"""

string1 = 'data'
string2 = 'science'
string3 = 'infinity'

len(string1)

string1.index('d')

string3[0]

string3[3:6]

string1.replace('a', 'o')
string1a = string1.replace('a', 'o')
print(string1a)

string4 = string1 + '-' + string2 + '-' + string3
print(string4)

string4.upper()
string4.lower()

string4.split('-')

string4.count('-')

my_string = "RED ALERT - Meltdown in sector 7G. Please contact: Homer"

alert_level = "RED"
error_type = "Meltdown"
sector = "7G"
contact_name = "Homer"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. Please contact: {contact_name}"

print(my_string)

