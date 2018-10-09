# -*- coding: utf-8 -*-

import random
from bot import chatbot, Answer

@chatbot.action('goodbye')
def default(w, subfacts, conclusions, context):
    t = random.choice(["Thank you for talking with me.", "Good-bye.", "Thank you, that will be $150. Have a good day!"])
    return Answer(message=t, stop=True)
