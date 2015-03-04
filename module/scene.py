__author__ = 'Roderick Lagunas'

from interface.command import CommandInterface
from common import command


class Create(CommandInterface):

    name = 'HelloWorld'
    odir = '.'

    def __init__(self):
        pass

    def main(self, args):
        if len(args):
            self.name = args['name']
            self.odir = args['dir']

        print 'Parametros de entrada: ' + self.name + ' ' + self.odir

    @staticmethod
    def description():

        return "Create Cocos2d-x Scene"

    @staticmethod
    def usage():

        return command.Core.Color.green + 'scene:create --name=name --dir=output_dir'

    @staticmethod
    def arguments():
        return command.Core.Color.green + '--name ' + \
               command.Core.Color.gray  + ': name of scene files (.h and .cpp)' + \
               command.Core.Color.green + '\n\t--dir  ' + \
               command.Core.Color.gray  + ': output directory'

    @staticmethod
    def help():
        return "--name in UpperCamelCase" + \
               "\n\t--dir is an absolute path with end slash"





