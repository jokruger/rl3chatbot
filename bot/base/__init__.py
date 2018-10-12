# -*- coding: utf-8 -*-

import random
from bot.answer import Answer

class BaseActions():
    def __init__(self):
        pass

    def goodbye(self, w, subfacts, conclusions, context):
        t = random.choice([
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ])
        return Answer(message=t, stop=True)
