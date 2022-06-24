# -*- encoding :: utf-8 -*-

import os


class BulkClone:
    """Class responsible for dealing with the actual clone stage."""
    @staticmethod
    def clone(url, dest):
        """Clone a given github url"""
        os.system(f"git clone {url} {dest}")
