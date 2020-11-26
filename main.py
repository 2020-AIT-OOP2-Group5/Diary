from diaries.DiarySample import DiarySample
from diaries.KatoDiaryNew import KatoDiary
from diaries.NonakaDiary import NonakaDiary

diaries = [DiarySample(), 
           KatoDiary(), 
           NonakaDiary(),
          ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()