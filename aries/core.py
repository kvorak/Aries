'''
Created on Jul 27, 2015

@author: jhamilton
'''

import os
import quarks

class Aries(object):
    """ Defines the root object
    """

    class ReadOnlyMember(Exception):
        pass

    @property
    def journal_path(self):
        return self._journal_path

    @journal_path.setter
    def journal_path(self, journal_path):
        """ Set the `journal_path` member

        @params: journal_path; as a string or os.path object

        TODO: Add error checking like exists(), can_read, can_write, etc.
        """

        self._journal_path = journal_path

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        raise Aries.ReadOnlyMember("Use Aries.load_resources")

    def __init__(self, journal_path="~/Documents/"):
        """ Initializes the Aries object """

        self.journal_path = os.path.abspath(journal_path)
        self.load_resources()

    def load_resources(self, journal_path=None):
        """ Loads resources at the specified path

        Defaults to self.journal_path
        """

        if not journal_path:
            journal_path = self.journal_path

        # Load the directory and walk it.
        self._resources = quarks.functions.map_path(journal_path)

    def get_uri(self, uri):
        return quarks.functions.rget(self._resources, uri.split('/'))

