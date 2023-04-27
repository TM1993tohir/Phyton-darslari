# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:58:41 2023

@author: t.mamasoliyev
"""
#1-mashq for yordamida kaliq va qiymatlarni tartiblab chiqarish

#dictionary={'print':'chop etish', 'for':'takrorlash', 'if':'shart', 'else':'aks holda',\
    #       'string':'matnli tip', 'float':'haqiqiy sonli tip',\
   #        'int':'butun sonli tip', 'boolen':'mantiqiy tip', \
  #         'elif':'ketma-ket shart tekshirish',\
 #         'upper':'barchasini katta harflarda yozish'}

#print(dictionary.keys())
#for k, q in sorted(dictionary.items()):
 #  print(k, "-", q)
    
 #2-mashq Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
  # keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
  
  
davlatlar={"AQSH":"Vashington", "Uzbekistan":"Tashkent", "Japan":"Tokiyo", "Tadjikistan":"Dushanbe","Russia":"Maskva"} 
print("Dunyo davlatlari")
for  davlat in sorted(davlatlar.keys()):
    print(davlat)
print("\nDunyo davlatlarining poytaxtlari")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)
    
country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:")
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")