from diaries.DiarySample import DiarySample
from diaries.IchikawaDiaryNew import IchikawaDiaryNew

diaries = [DiarySample(), IchikawaDiaryNew(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()