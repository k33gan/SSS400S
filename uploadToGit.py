#!/usr/bin/env python
from git import Repo

try:
    repo_dir = ''
    repo = Repo(repo_dir)
    file_list = [
        'status.log',
        'generateLog_sendSMS.py'
    ]
    commit_message = 'Latest Status'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()

except KeyboardInterrupt:
    print "\nKeyboard interrupt detected."

except:
    print "Unforseen error occured!"

finally:
    print "Log Updated..."
