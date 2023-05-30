# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:14:18 2023

@author: t.mamasoliyev
"""

#Amaliyot NESTING
#Muallif:Mamasoliyev
#Sevimli kino serial
# sevimli={ 'ali':['Terminator', 'Transformer', 'Forsaj'],
#          'vali':['7 ta kal', 'choli qushi', 'ramayana'],
#          'shokir':['uddalab bo\'lmas topshiriq', 'john uik', 'sen yetim emassan']
#          }
# for ism, kino in sevimli.items():
#     print(f"{ism.title()} shu kinolarni yoqtiradi")
#     for kin in kino:
#         print(kin)
        
#Davlatlar haqida ma'lumot chiqarish


davlatlar={ 'uzbekistan':{'maydon':'448,978 km kv',
                          'aholisi':'33 mln',
                          'tili':'uzbek',
                          'pulbirligi':'som'
                          },
           'qozogiston': {'maydon':'2 million 724,9 ming km²',
                          'aholisi':'19.17 mln',
                          'tili':'qozoq',
                          'pulbirligi':'tenge'
               },
           'rossiya':{'maydon':'17 mln 98 ming 246 km kv',
                      'aholisi':'147 mln',
                      'tili':'rus',
                      'pulbirligi':'rubl'
                
                }
          }
# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.title()}ning yer maydoni \n"
#           f"{info['maydon']} ga teng \n"
#           f"Rasmiy tili {info['tili']} tili \n"
#           f"{info['aholisi']} odam istiqomad qiladi \n"
#           f"Pulbirligi {info['pulbirligi']}"
#           )
          
yangi=input("Qaysi davlat haqida ma'lumot olmoqchisiz?>>>")
yangi=yangi.lower()   
for davlat, info in davlatlar.items():
    if davlat == yangi:
        print(f"{davlat.title()} haqida ma'lumot \n"
              f"{info['maydon']} ga teng \n"
              f"Rasmiy tili {info['tili']} tili \n"
              f"{info['aholisi']} odam istiqomad qiladi \n"
              f"Pulbirligi {info['pulbirligi']}"
              )
    else:
        print("Bizda bu davlat haqida ma'lumot yo'q") 
        break
       