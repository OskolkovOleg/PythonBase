# Принцип единой ответственности

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    ########### Это нарушение SRP
    # def save(self, filename):...

    # def load():...

    # def low_from_web():...
    ##############################

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug')
print(f"Journal entries:\n{j}")

file = r'C:\test\journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())