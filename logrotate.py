#!/usr/bin/env python
import os

try:
	filename = "/home/pi/SSS400S/status.log"
	filename1 = "/var/log/status.log"
	
	statinfo = os.stat(filename)
	if statinfo.st_size > 1000000:
		os.mv(filename,filename1)
		target = open(filename, 'w')
		target.close()
	else:
		pass

except KeyboardInterrupt:
	print "\nKeyboard interrupt detected."
	target.close()

except:
        print "Unforseen error occured during logrotate!"
        target.close()

finally:
	target.close()
	print "Closing Program..."
