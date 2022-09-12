"""
SRP: Single Responsibility Principle / SOC: Separation of Concers

Class should have a single primary responsibility and should not take on other responsibilities.
"""


# Journal class responsible for storing journal entries and adding/removing of such entries.
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # Methods below break the single responsibility of a journal class
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


# PersistanceManager class responsible for saving/loading journals
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
journal_file = r'c:\temp\journal.txt'
p.save_to_file(j, journal_file)

# verify!
with open(journal_file) as fh:
    print(fh.read())
