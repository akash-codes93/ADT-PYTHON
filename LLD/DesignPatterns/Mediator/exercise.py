class Participant:
    def __init__(self, name, mediator):
        self.name= name
        self.value = 0
        self.mediator = mediator
        mediator.add_participants(self)

    def say(self, value):
        # todo
        self.mediator.broadcast(self, value)

    def receive(self, sender, value):
        print("Message received")
        self.value += value

    def __str__(self):
        return f'{self.name} - {self.value}'


class Mediator:

    def __init__(self):
        self.participants = []

    def add_participants(self, participant):
        self.participants.append(participant)
        participant.mediator = self

    def broadcast(self, sender, value):

        for participant in self.participants:
            if participant != sender:
                participant.receive(sender, value)

    def __str__(self):
        for _, participant in enumerate(self.participants):
            print(participant)
        return ''


if __name__ == '__main__':
    mediator = Mediator()
    p1 = Participant("John", mediator)
    p2 = Participant("Jane", mediator)

    p1.say(1)
    p2.say(3)
    print(mediator)
