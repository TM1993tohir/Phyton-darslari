# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:35:49 2023

@author: t.mamasoliyev
"""

#Ro'yxat ichida lug'at
#Muallif:Tohirbek Mamasoliyev
#car0={"model":"Lacetti", 
#      "rangi":"oq",
#      "narx":15000, 
#      "pozitsiya":"yevro",
#      "yil":2020,
#      "uzatmasi":"avtomat",
#      "yoli":20000      
#      }
#car1={"model":"nexia 3", 
#      "rangi":"oq",
#      "narx":12000, 
#      "pozitsiya":"yevro",
#      "yil":2021,
#      "uzatmasi":"avtomat",
#      "yoli":10000      
#      }
#car2={"model":"damas", 
#      "rangi":"ko'k",
#      "narx":8000, 
#      "pozitsiya":"yevro",
#      "yil":2020,
#      "uzatmasi":"mexanika",
#      "yoli":20000      
#      }
#cars=[car0, car1, car2]

#for car in cars:
#    print(f"{car['model'].title()}",
 #         f"{car['rangi']} rang",
 #         f"{car['yil']}-yil",
 #         f"{car['narx']} $"
 #         )

#Yangi bo'sh ro'yhat yaratish va unga lug'at joylashtirish 
    
malibus=[]
for n in range(10):
    new_car={'model':"malibu",
             'rangi': None,
             'yoli': 0,
             'uzatmasi': "avto",
             "narx":None,
             "yil":2022,
             "pozitsiyas":"yevro"
            }   
    malibus.append(new_car)    
#print(malibus)

for malibu in malibus[:3]:
    malibu["rangi"]='qizil'
#print(malibus)
for malibu in malibus[3:6]:
    malibu["rangi"]='qora'
        
for malibu in malibus[6:]:
    malibu["rangi"]='oq'
    malibu['uzatmasi']="mexanika"
#print(malibus)

for malibu in malibus:
    if malibu["uzatmasi"]=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000 
print(malibus)   
    