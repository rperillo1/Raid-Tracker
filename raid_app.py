import sys
sys.path.insert(0, '/Projects/raid_project/API/src/Repositories')
from raid_repository import RaidRepository

sys.path.insert(0, '/Projects/raid_project/API/src/Models')
from raid import Raid

x = RaidRepository


'''
r = Raid(name = "Derakor the Vindicator", is_active = True, priority = 3, chat_link_url = "www.chickenbreh.com")

x.CreateRaid(r)
print(r.id)
'''


x.GetAllRaids()
