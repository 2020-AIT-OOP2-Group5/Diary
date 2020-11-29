from diaries.AbstractDiary import AbstractDiary


class IchikawaDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "今日は朝寒かった"

    def get_author(self):
        return "Ichikawa"
