#!/usr/bin/env python
import os

try:
	filename = "/home/pi/SSS400S/status.log"
	filename1 = "/var/log/status.log"
	
	statinfo = os.stat(filename)
	print statinfo.st_size
	if statinfo.st_size > 1000:
		os.rename(filename,filename1)
		target = open(filename, 'w')
		target.close()
		os.system("sudo python /home/pi/SSS400S/uploadToGit.py")
	else:
		pass

except KeyboardInterrupt:
	print "\nKeyboard interrupt detected."
	
except:
        print "Unforseen error occured during logrotate!"
        
finally:
	print "Closing Program..."
