# -*- coding: utf-8 -*-

import wikipedia, warnings
from bot.core import Option, Answer

warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

class WikipediaActions():
    def __init__(self):
        wikipedia.set_lang('en')

    def wikipedia_summary(self, w, subfacts, conclusions, context):
        for i in subfacts.get_facts('query'):
            try:
                t = wikipedia.summary(i.get_value(), sentences=1)
                if t and len(t) < 100:
                    t = wikipedia.summary(i.get_value(), sentences=2)
                if t and len(t) >= 100:
                    return Answer(message=t)

            except wikipedia.exceptions.DisambiguationError as e:
                opts = []
                for j in e.options:
                    if j.lower().strip() != i.get_value().lower().strip():
                        opts.append(Option(title=j.strip(), body='What is %s?' % j.strip()))
                if len(opts) > 0:
                    return Answer(message='What exactly do you mean by "%s"?' % i.get_value().strip(), options=opts)

            except:
                pass

        return None
