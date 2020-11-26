from diaries.AbstractDiary import AbstractDiary


class TakahashiDiarySample(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "腰が痛かった"

    def get_author(self):
        return "Takahashi"
