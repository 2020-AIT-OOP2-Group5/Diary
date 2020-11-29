from diaries.DiarySample import DiarySample
from diaries.KatoDiaryNew import KatoDiary
from diaries.NonakaDiary import NonakaDiary
from diaries.TakahashiDiaryNew import TakahashiDiary

diaries = [DiarySample(), 
           KatoDiary(), 
           NonakaDiary(),
           TakahashiDiary(),
          ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()