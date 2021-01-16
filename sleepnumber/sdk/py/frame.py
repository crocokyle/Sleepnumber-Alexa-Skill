from sleepyq import Sleepyq
from pprint import pprint
import time

client = Sleepyq('kyle@akhawaii.com', 'S$Mf8o@0{/Me')
client.login()

position = 3

# Presets
# 1 = Favorite
# 2 = Read
# 3 = Watch TV
# 4 = Flat
# 5 = Zero-G
# 6 = Snore Mode

client.preset("-9223372019870281837", position, "R", slowSpeed=False)

