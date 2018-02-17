#import module
from simplebash import sbash
#create class object
sb = sbash()
#call function to build command through user input
#returns command in tuple
cmd = sb.usrcmd()
#cmd[0] will always be the command
#cmd[2] will always be the arguments, no matter how may there are
results = sb.runbash(cmd[0],cmd[1])

#results stored in string.  Printed below.
print results
