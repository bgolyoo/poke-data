from subprocess import call
import glob
import os

host = raw_input('Enter host name: ')
db = raw_input('Enter db name: ')
username = raw_input('Enter user name: ')
password = raw_input('Enter password: ')

files = glob.glob("./converted_resources/**.json")

for f in files:
    collection = os.path.basename(f).split('.')[0]
    print
    print "--------- start: " + collection + " ---------"
    command = [
        "./mongoimport",
        "-h", host,
        "-d", db,
        "-c", collection,
        "-u", username,
        "-p", password,
        "--file", f,
        "--jsonArray"
    ]
    call(command)
    print "--------- end: " + collection + " ---------"
    print
