# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:47:02 2023

@author: t.mamasoliyev
"""
#Lug'at ichida lug'at va ro'yhat 
#Muallif: Mamasoliyev Tohirjon
#dasturchilar={
#    "ali" :['c++', 'php', 'js'],
#    "vali":['css','phyton'],
#    'durdona':['jango', 'c#'],
#    }
#for ism, tillar in dasturchilar.items():
#    print(f'\n{ism.title()} quydagi tillarni biladi')
#    for til in tillar:
#        print(til.upper())
#
#    print(f'\n{ism.title()} quydagi tillarni biladi')
#    for til in tillar:
#        print(f'{til.upper()}',  end=' ')

#Ichma-ich lug'at
#Muallif Tohirjon Mamasoliyev

hamkasblar={ 
    'jaloldin':{'familiya':'Choriyev',
                'lavozimi':'Sektor boshligi',
                'tyil':1996,
                'viloyat':'Qashqadaryo',
                'tillar':['php','paskal','html']
                          },
    'zafar':{ 'familiya':'Turabov',
                'lavozimi':'yetakchi mutaxassis',
                'tyil':1996,
                'viloyat':'Jizzax',
                'tillar':['sql','css']
        },
    'shukrullo': { 'familiya':'Juraqulov',
                'lavozimi':'Mutaxassis',
                'tyil':1998,
                'viloyat':'Buxoro',
                'tillar':['phyton', 'c++']                
        }
    
    }
for ism, info in hamkasblar.items():
    print(f"\n {ism.title()} {info['familiya'].title()},"
          f"{info['tyil']} - yilda tugilgan,"
          f"Lavozimi: {info['lavozimi']} \n"
          f"Qyidagi dasturlash tillarini biladi:")
          
    for til in info['tillar']:
        print(til.upper())
    