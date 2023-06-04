class Party:
    def __init__(self):
        self.people = []

    def say_hello(self):
        print("Hello")


party = Party()

command = input()

while command != "End":
    party.people.append(command)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
