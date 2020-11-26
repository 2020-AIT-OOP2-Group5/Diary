from diaries.DiarySample import DiarySample
from diaries.NonakaDiary import NonakaDiary

diaries = [DiarySample(), NonakaDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()