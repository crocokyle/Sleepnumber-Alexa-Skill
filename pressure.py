from sleepyq import Sleepyq
from pprint import pprint
import time

sn = 100

client = Sleepyq('<EMAIL>', '<PASSWORD>')
client.login()
client.set_sleepnumber("-9223372019870281837", "L", sn)
time.sleep(10)
client.set_sleepnumber("-9223372019870281837", "R", sn)
