# question 2 task 1

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0


    def add_participant(self):
        self.participant_count +=1

    def get_count(self):
        return self.participant_count