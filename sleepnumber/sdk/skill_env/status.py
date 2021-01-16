from sleepyq import Sleepyq
from pprint import pprint
import time

client = Sleepyq('kyle@akhawaii.com', 'S$Mf8o@0{/Me')
client.login()
print("Sleeper 0\n-----------------------------------")
print(" ")
pprint(vars(client.sleepers()[0]))
print(" ")
print("Sleeper 1\n-----------------------------------")
print(" ")
pprint(vars(client.sleepers()[1]))
print(" ")
print("_____________________________________________")
print(" ")

print("Beds\n-----------------------------------")
pprint(vars(client.beds()[0]))

print(" ")
print("_____________________________________________")
print(" next is sleeper status ")

pprint(client.get_favsleepnumber("-9223372019870281837").left)
pprint(vars(client.beds_with_sleeper_status()[0].left))
pprint(vars(client.beds_with_sleeper_status()[0].right))

print(" ")
pprint(vars(client.get_light("-9223372019870281837", 3)))

#NotWorking
#print("Bed Family Status L\n-----------------------------------")
#pprint(vars(client.bed_family_status()[0].left))
#print("Bed Family Status R\n-----------------------------------")
#pprint(vars(client.bed_family_status()[0].right))
