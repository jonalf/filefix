#!/usr/bin/python
# File uploader
# Copyright Mike Zamansky, January 2004
#

import cgi
import stat
import os
import sys
import crypt
import nis
import string
import re
import time
import xmlrpclib
import curses.ascii

#import cgitb
#cgitb.enable()

tempdir = '/tmp/filefix/'

def process(f):
    upload = f['filename']
    data = upload.file.read()
    data = data.replace('\r\n', '\n')
    
    s = 'Content-type: unknown\nContent-Disposition: attachment; filename="' + upload.filename + '"\n'
    print s
    print data


form = cgi.FieldStorage()
if form.has_key("SUBMIT") and form["SUBMIT"].value == "SUBMIT":
    process(form)

else:
    html='''
        <html>
        <head><title>File Fix</title>
        <link rel="stylesheet"
              type="text/css"
              href="style.css" />
        </head>
        <body>
        <h1>Fix Windows Newline Problems</h1>
        <ol>
        <li>Click Choose File below and select your file.</li>
        <li>Click Submit</li>
        <li>Your browser will either automatically download the file or ask you where to save the file
             <ul>
               <li>SUPER IMPORTANT NOTE: DO NOT CHOSE TO OPEN THE FILE!</li>
               <li>If you open the file, windows will then add those pesky \rs back!</li>
             </ul></li>
        <li>You should then use the downloaded file to ftp back to your class webserver</li>
        </ol>
        <center>
        <FORM METHOD="POST"  ENCTYPE="multipart/form-data">
        <table>
           <tr><td>File:</td><td><input type="FILE" name="filename"></td></tr>
           </table>
        <input type="SUBMIT" NAME="SUBMIT" VALUE="SUBMIT">
        <input type="SUBMIT" NAME="SUBMIT" VALUE="CANCEL">
        </form>
        </center>
        </body>
        </html>'''
    print 'Content-type: text/html\n'
    print html
