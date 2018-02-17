#Simplipyed Bash Helper
import subprocess as subproc
import re
import inspect

class sbash(object):
    """Simplipyed Bash Module."""
    def __init__(self,command=None,command_argument=None,command_pipe=None):
        cmd,cmd_arg,cmd_pipe=command,command_argument,command_pipe
        self.replace_chars = ("""\n""",',','None')
        self.command_dict = {'list_files':'ls','new_file':'touch','working_dir':'pwd'}
        self.error_dict = {'user_error':'Invalid User input','bash_error':'problem running command'}

    def usrcmd(self):
        commands,error = self.command_dict.values(),self.error_dict['user_error']
        print "Here are available commands" + str(commands)
        user_in = raw_input('Please enter a command').lower().split()
        if(len(user_in)==1):command,arguments=user_in[0],None
        elif(len(user_in)>1):command,arguments=user_in[0],user_in[1:]
        else:command,arguments = None,None
        if(command in commands):
            if(not arguments):print "Warning, arguments set to none"
            return (command,arguments)

    def runbash(self,cmd,cmd_arg=None,cmd_pipe=None):
        error = self.error_dict['bash_error']
        if(not cmd_arg):
            try:
                proc = subproc.Popen(cmd,stdout=subproc.PIPE)
                result = proc.communicate()
            except: return error
        else:
            try:
                proc = subproc.Popen([cmd,cmd_arg[0]],stdout=subproc.PIPE)
                result = proc.communicate()
            except: return error
        for r in result:
            if(r!=None):
                result = re.sub(',',"",r)
                return result


if __name__ == "__main__":
    print 'running as main'
    test = sbash()
