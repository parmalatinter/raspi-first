# -*- coding: utf-8 -*-
from . import helpers

class He:
    def get_hmm(self):
        """Get a thought."""
        return 'hmmm...'


    def hmm(self):
        """Contemplation..."""
        if helpers.get_answer():
            print(self.get_hmm())
