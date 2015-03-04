__author__ = 'Roderick Lagunas'

from interface.command import CommandInterface
from common import command


class Create(CommandInterface):

    name = None
    odir = '.'

    def __init__(self):
        pass

    def main(self, args):

        try:
            self.name = args['name']
        except KeyError:
            print "ERROR: --name is required."
            exit()

        import re
        if not re.match('^[A-Z]{1}', self.name):
            print 'ERROR: --name=' + self.name + '. Use UpperCamelCase Names'
            exit()

        try:
            self.odir = args['dir']
        except KeyError:
            pass

        h = open('templates/Scene.h').read()
        cpp = open('templates/Scene.cpp').read()
        h = h.replace('%UNAME%',self.name.upper()).replace('%NAME%',self.name)
        cpp = cpp.replace('%NAME%',self.name)

        base_name = self.odir + '/' + self.name
        try:
            hf = open( base_name + 'Scene.h', 'w+')
            hf.write(h)
            hf.close()
            cppf = open(base_name + 'Scene.cpp', 'w+')
            cppf.write(cpp)
            cppf.close()
        except IOError, e:
            print "ERROR: " + unicode(e)



    @staticmethod
    def description():

        return "Create Cocos2d-x Scene"

    @staticmethod
    def usage():

        return command.Core.Color.green + 'scene:create --name=name [--dir=output_dir]'

    @staticmethod
    def arguments():
        return command.Core.Color.green + '--name ' + \
               command.Core.Color.gray  + ': name of scene files (.h and .cpp)' + \
               command.Core.Color.green + '\n\t--dir  ' + \
               command.Core.Color.gray  + ': output directory, if undefined current directory'

    @staticmethod
    def help():
        return "--name in UpperCamelCase" + \
               "\n\t--dir is an absolute path with end slash"





