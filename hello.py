#!/usr/bin/python3
import cmd
"""
    Simple Command Hello worlld
"""


class HelloWorld(cmd.Cmd):
    """
        HelloWorld Class
    """

    def do_greet(self, line):
        print ("Hello")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
