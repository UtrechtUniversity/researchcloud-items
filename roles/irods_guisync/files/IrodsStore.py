#!/usr/bin/python
# (c) 2021 Ton Smeele - Utrecht University
#
#  IrodsStore manages the interaction with an iRODS zone
#  
#
#  It assumes that the user has executed iinit or equivalent authentication
# 
import os
import json
import ssl
import irods
from irods.session import iRODSSession
from irods.exception import CollectionDoesNotExist

IRODS_ENV_PATH = '~/.irods/irods_environment.json'


class IrodsStore():

    def __init__(self):
        self.session = None
        try:
            irods_env_file = os.environ['IRODS_ENVIRONMENT_FILE']
        except KeyError:
            irods_env_file = os.path.expanduser(IRODS_ENV_PATH)
        try:
            with open(irods_env_file, 'rt') as f:
                json.load(f)
            self.irods_env_file = irods_env_file
        except IOError:
            self.irods_env_file = None
        self.connect()

    def __del__(self):
        if self.session is not None:
            self.disconnect()


    def connect(self):
        if self.irods_env_file is None:
            # this case is not yet supported, could ask for credentials
            raise IOError('Unable to open iRODS environment file')
        ssl_context = ssl.create_default_context(
                purpose=ssl.Purpose.SERVER_AUTH, 
                cafile=None, capath=None, cadata=None)
        ssl_settings = {'ssl_context': ssl_context}
        self.session = iRODSSession(
                irods_env_file=self.irods_env_file, **ssl_settings)

    def disconnect(self):
        if self.session is not None:
            self.session.cleanup
            self.session = None

    def get_hostname(self):
        if self.session is None:
            return ''
        return self.session.host


    def get_localzone_path(self):
        return '/' + self.session.zone
    

    # generator
    def subcollections(self, path):
        try:
            coll = self.session.collections.get(path)
        except:
            # collection does not exist or is inaccessible, just pretend no children
            raise StopIteration
        for subcoll in coll.subcollections:
            yield subcoll.path, subcoll.name
