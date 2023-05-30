# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:11:32 2023

@author: t.mamasoliyev
"""
#Amaliyot:Nesting
#Muallif:Tohirjon Mamasoliyev 
alloma0 = { 'ism':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy',
        'tyil':810,
        'tjoy':'Buxoro',
        'unvoni':' Muhaddislar imomi, hadis ilmining sultoni',
        'vafoti':870,
        'asar':['Al-jomeʼ as-sahih', 'At-tarix al-kabir', 'At-tarix al-avsat']
        }
alloma1={ 'ism':'Abul Abbos Ahmad ibn Muhammad ibn Kasir al-Fargʻoniy',
          'tyil':797,
          'tjoy':'Fargona',
          'unvoni':'oʻzbek qomusiy olimi',
          'vafoti':865,
          'asar':['Kitob al-harakot as-samoviya va javomi ilm an-nujum', ]
    }
alloma2={'ism':'Alisher Navoiy',
          'tyil':1441,
          'tjoy':'Hirot',
          'unvoni':'gazal mulkining sultoni',
          'vafoti':1501,
          'asar':['Majolisun-nafois', 'Mahbubul-qulub', 'Lisonut-tayr']
     }



olimlar=[alloma0, alloma1, alloma2]

# for shax in olimlar:
#     print(shax['ism'])
#     asr =  shax['asar']
#     for asa in asr:
#         print(asr)


for olim in olimlar:
        print(f"{olim['ism'].title()}",
                f"{olim['tyil']}-yilda",
                f"{olim['tjoy']}da tug\'ilgan,",
                f"{olim['unvoni']} buyuk alloma ",
                f"{olim['vafoti']}-yilda vafot etgan")
  

# for shaxs in olimlar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)\
    

    







































    
    