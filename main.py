from diaries.DiarySample import DiarySample
from diaries.KatoDiaryNew import KatoDiary

diaries = [DiarySample(), KatoDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()