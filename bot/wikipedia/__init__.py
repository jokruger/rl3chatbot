# -*- coding: utf-8 -*-

import wikipedia, warnings
from bot.answer import Answer

warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

class WikipediaActions():
    def __init__(self):
        wikipedia.set_lang('en')

    def wikipedia_summary(self, w, subfacts, conclusions, context):
        for i in subfacts.get_facts('query'):
            try:
                t = wikipedia.summary(i.get_value(), sentences=1)
                if t and len(t) > 50:
                    return Answer(message=t)
            except:
                pass
        return None
