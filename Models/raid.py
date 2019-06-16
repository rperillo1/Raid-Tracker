class Raid:
    def __init__(self, name, is_active, priority, chat_link_url, id=0):
        self.id = id
        self.name = name
        self.is_active = is_active
        self.priority = priority
        self.chat_link_url = chat_link_url



'''
fake_raid = Raid(1, "Trakanon", True, 4, "www.yodawg.com")

print(fake_raid.name)


import sys
print(sys.path)
'''
