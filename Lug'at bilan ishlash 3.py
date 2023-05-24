# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:13:17 2023

@author: t.mamasoliyev
"""

#akt={'ismi':'Shukurullo', 'tug_yili':1998, 'lavozimi':'mutaxassis'}
#print(akt.items())
#for kalit, qiymat in akt.items():
#    print(f'Kalit:{kalit}')
#   print(f'Qiymat:{qiymat}')
#for k,q in akt.items():
  #  print(f'{k.title()} {q}')
  
  
  
#dictionary={'print':'chop etish', 'for':'takrorlash', 'if':'shart', 'else':'aks holda',\
#          'string':'matnli tip', 'float':'haqiqiy sonli tip',\
#           'int':'butun sonli tip', 'boolen':'mantiqiy tip', \
#           'elif':'ketma-ket shart tekshirish',\
#         'upper':'barchasini katta harflarda yozish'}
#for k, q in sorted(dictionary.items()):
#    print(f'{k.title()} - {q}')

davlatlar={"aqsh":"vashington", "uzbekistan":"tashkent", "japan":"tokiyo", "tadjikistan":"dushanbe","russia":"maskva", \
           "australiya":"canberra", "angliya":"london", \
            "iroq":"bogdod","qozog\'iston":"astana"}  
#print('Dunyo davlatlari:')
#for k,q in davlatlar.items():
#    print (f'{k.upper()}')
    
#print('\nDunyo davlatlari poytaxtlari')
#for k,q in davlatlar.items():
#    print(q.title())
    
#foydalanuvchi=input('Qaysi davlat poytaxtini bilishni hohlisiz?>>>')
#foydalanuchi1=foydalanuvchi.lower()
#for davlat, q in davlatlar.items():
#    if davlat == foydalanuchi1:
#      print(f'{davlat.upper()} ning poytaxti {q.title()} shahri')       
#    else:
#        print("Kichirasiz bizda bu davlat haqida ma'lumot yo'q. Noqulaylik uchu uzur so'raymiz!")
        
country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
 
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()} ning poytaxti {capital.title()} shahri")       
    
        
    
    


