# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:13:09 2023

@author: t.mamasoliyev
"""
               #1-mashq
#Otam={'ism':'Xudobergan', 't_yil':1965, 'viloyat':"Farg'ona"}
#Onam={'ism':'Dilfuza', 't_yil':1970, 'viloyat':"Farg'ona"}
#Akam={'ism':'Zoirjon', 't_yil':1991, 'viloyat':"Farg'ona"}
#Ukam={'ism':'Iqboljon', 't_yil':1998, 'viloyat':"Farg'ona"}
#print(f"Otamning ismi {Otam['ism'].title()} {Otam['t_yil']}-yilda {Otam['viloyat']}da tug'ilgan")
#print(f"Onamning ismi {Onam['ism'].title()} {Onam['t_yil']}-yilda {Onam['viloyat']}da tug'ilgan")
#print(f"Akamning ismi {Akam['ism'].title()} {Akam['t_yil']}-yilda {Akam['viloyat']}da tug'ilgan")
#print(f"Ukamning ismi {Ukam['ism'].title()} {Ukam['t_yil']}-yilda {Ukam['viloyat']}da tug'ilgan")

               #2-mashq
                         
#taom={'Dadam':'Palov', 'Onam':'Manti', 'akam':'Pitsa', 'ukam':'Mastava'}
#print(f"Dadamning sevimli taomi {taom['Dadam']},\
     # Onamning sevimli taomi {taom['Onam']},\
    #  Akamning sevimli taomi {taom['akam']},\
     # Ukamning sevimli taomi {taom['ukam']}")

              #3-mashq

dictionary={'print':'chop etish', 'for':'takrorlash', 'if':'shart', 'else':'aks holda',\
           'string':'matnli tip', 'float':'haqiqiy sonli tip',\
           'int':'butun sonli tip', 'boolen':'mantiqiy tip', \
           'elif':'ketma-ket shart tekshirish',\
          'upper':'barchasini katta harflarda yozish'}
#print(f"Print bu yozilgan kodlar natijasini ekranga {dictionary['print']} uchun qo'llaniladi")
#print(f"for bu-dasturda keladigan {dictionary['for']} amallarini bajaradi")
#print(f"if bu-dasturda {dictionary['if']} bajarish kelganda qo'llaniladi")
#print(f"else bu- shart tekshirilganda shart bajarilmasa {dictionary['else']} holat uchun ishlatiladi")            

             #4-mashq
#lugat=dictionary[input('biron metod kiriting: ')]
kiritish = input("ma'lumot turini kiriting: ")
lugat=dictionary.get(kiritish ,"bunday metod bizning lug'atda yo'q")
print(lugat)

             