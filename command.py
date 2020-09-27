#!/usr/bin/python3

print("content-type: text/html\n")
print()
import cgi
import subprocess
form = cgi.FieldStorage()
cmd = form.getvalue("command")
#print(cmd)
status, output = subprocess.getstatusoutput(cmd)
print("<center>Output</center>")
#print(output,status)
if status==0:
	print("<center><h1>"+output+"</h1></center>")
else:
	print("<h1>Command failed Sorry for inconvenience</h1>")
output = 0