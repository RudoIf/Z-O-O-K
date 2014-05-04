#!python
# "Grab Red Packets"
# Owner sets a total red packets zoobars
# Every visitor will get random zoobars from the total value if owner has enough zoobars
# Similar to granter.py, it has been at least a miniute since the last time the visitor got a red packet
import sys, time, errno, os, random

global api
selfuser = api.call('get_self')
visitor = api.call('get_visitor')

me = api.call('get_user_info', username=selfuser)

rp_fn = 'red_packets_%s.dat' % selfuser
if not os.path.exists(rp_fn):
    with open(rp_fn, 'w') as f:
        f.write("10") #updater set this value

if me['zoobars'] <= 0:
    print 'Sorry, this guy has no more zoobars for his red packet'
    sys.exit(0)

total = 0
with open(rp_fn) as f:
    total = int(f.read())
currp = min(total, me['zoobars'])

last_fn = 'last_freebie_%s_%s.dat' % (selfuser, visitor)
last_xfer = 0
try:
  with open(last_fn) as f:
    last_xfer = float(f.read())
except IOError, e:
  if e.errno == errno.ENOENT:
    pass

now = time.time()
if now - last_xfer < 60:
  print 'I gave you red packets %.1f seconds ago' % (now-last_xfer)
  sys.exit(0)

random.seed(now)
visitor_rp = random.randint(0, currp)
api.call('xfer', target=visitor, zoobars=visitor_rp)
print 'Happy New Year.  I gave you %d red_packet.' % (visitor_rp)

with open(last_fn, 'w') as f:
  f.write(str(now))

with open(rp_fn, 'w') as f:
  f.write(str(total-visitor_rp))

