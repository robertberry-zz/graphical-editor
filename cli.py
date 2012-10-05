#!/usr/bin/env python
"""Classes & functions related to the command line interface.
"""

import re

from image import Image, BadCoordinateError
from utils import number_args

# Maximum height of an image
MAX_IMAGE_HEIGHT = 250

# Maximum width of an image
MAX_IMAGE_WIDTH = 250

class CLIError(Exception):
    """Base error class for CLI.
    """
    pass

class NewImageError(CLIError):
    """Error raised when user enters bad dimensions for new image.
    """
    def __init__(self, message):
        self.message = message

    def cli_message(self):
        """Message the error prints on the command line.
        """
        return self.message

class UnknownCommandError(CLIError):
    """Error thrown when user enters an unknown command.
    """
    def __init__(self, command):
        self.command = command
    
    def cli_message(self):
        """Message the error prints on the command line.
        """
        return "Unknown command: %s" % self.command

class BadNumberArgsError(CLIError):
    """Error thrown when user invokes command with a bad number of args.
    """
    def __init__(self, command, args_supplied, args_required):
        self.command = command
        self.args_supplied = args_supplied
        self.args_required = args_required

    def cli_message(self):
        """Message the error prints on the command line.
        """
        return "Command %s requires %d args, not %d" % (self.command, \
                                                            self.args_supplied, \
                                                            self.args_required)

class NoImageError(CLIError):
    """Error raised when user tries to use a command that operates on an image
    but no image is present.
    """
    def __init__(self, command):
        self.command = command
    
    def cli_message(self):
        """Message the error prints on the command line.
        """
        return "%s can only be invoked after creating an image." % self.command

class CLI(object):
    """Represents the command line interface.
    """
    def __init__(self):
        self._commands = dict()
        self._image = None
        self._running = False

    @property
    def image(self):
        if self._image is None:
            raise NoImageError()
        else:
            return self._image

    def new_image(self, m, n):
        if m < 1:
            raise NewImageError("Image must be minimum 1 pixel wide.")
        if n < 1:
            raise NewImageError("Image must be minimum 1 pixel high.")
        if m > MAX_IMAGE_WIDTH:
            raise NewImageError("Image must be maximum %d pixels wide." % \
                                    MAX_IMAGE_WIDTH)
        if n > MAX_IMAGE_HEIGHT:
            raise NewImageError("Image must be maximum %d pixels high." % \
                                    MAX_IMAGE_HEIGHT)        
        self._image = Image(m + 1, n + 1)

    def register_command(self, name, command):
        """Registers a command function with the given token name. Command
        should be a function that takes the client object as its first
        argument, with a given number of integer arguments thereafter.
        """
        self._commands[name] = command

    def process_command(self, name, args):
        """Given the name of a command and an argument list, attempts to
        process that command. Raises errors if the command does not exist, if
        a bad number of arguments is supplied, or if the context in which the
        command is called is invalid.
        """
        try:
            command = self._commands[name]
            command(self, *args)
        except KeyError:
            raise UnknownCommandError(name)
        except TypeError:
            raise BadNumberArgsError(name, len(args), number_args(command) - 1)

    def terminate(self):
        """Terminate the CLI process.
        """
        self._running = False
        self._image = None

    def main_loop(self):
        """Starts the CLI input loop.
        """
        self._running = True

        while self._running:
            cmd = raw_input(">>> ")

            args = re.split(r"\s", cmd)

            cmd = args[0]

            try:
                args = [int(arg) for arg in args[1:]]
            except TypeError:
                print "Args must all be integer values."

            try:
                self.process_command(cmd, args)
            except CLIError, e:
                print e.cli_message()
            except BadCoordinateError, e:
                print "%d, %d is outside image's dimensions." % (e.x, e.y)

