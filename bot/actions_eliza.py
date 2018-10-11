# -*- coding: utf-8 -*-

import random, re
from bot import chatbot, Answer

reflections = {
    "i": "you",
    "am": "are",
    "i'm": "you are",
    "im": "you are",
    "was": "were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

def reflect(token):
    t = token.lower()
    if t in reflections:
        return reflections[t]
    return token

def substitute(text, factsheet, apply_reflection):
    t = text
    if factsheet is not None and len(factsheet) > 0:
        for i in factsheet.get_facts():
            v = i.get_value()
            if apply_reflection:
                v = v.replace('!', ' ').replace('?', ' ').strip()
                v = ' '.join([reflect(j) for j in v.split(' ')])
            t = t.replace('{%s}' % i.get_label(), v)
    return t

def make_answer(templates, subfacts, context):
    random.shuffle(templates)
    for i in templates:
        try:
            t = i
            t = substitute(t, subfacts, True)
            t = substitute(t, context, False)
            if re.search(r"{[a-zA-Z0-9_\-]+}", t) is None:
                return Answer(message=t)
        except:
            pass

    return None

@chatbot.action('eliza_base')
def eliza_base(w, subfacts, conclusions, context):
    return(make_answer([
        "Please tell me more.",
        "Let's change focus a bit... Tell me about your family.",
        "Can you elaborate on that?",
        "Why do you say that {X}?",
        "I see.",
        "Very interesting.",
        "{X}...",
        "{X}?",
        "I see. And what does that tell you?",
        "How does that make you feel?",
        "How do you feel when you say that?",
        "I'm not sure I understand you fully.",
        "Please go on.",
        "That is interesting. Please continue.",
        "Tell me more about that.",
        "Does talking about this bother you?",
    ], subfacts, context))

@chatbot.action('eliza_base_question')
def eliza_base_question(w, subfacts, conclusions, context):
    return(make_answer([
        "Why do you ask?",
        "Why do you ask that?",
        "How would an answer to that help you?",
        "What do you think?",
        "How do you suppose?",
        "Perhaps you can answer your own question.",
        "Perhaps the answer lies within yourself?",
        "What is it you're really asking?",
        "Please consider whether you can answer your own question.",
        "Why don't you tell me?",
        "Does that question interest you?",
        "What is it you really want to know?",
        "Are such questions much on your mind?",
        "What answer would please you most?",
        "What comes to mind when you ask that?",
        "Have you asked such questions before?",
        "Have you asked anyone else?",
    ], subfacts, context))

@chatbot.action('eliza_i_need')
def eliza_i_need(w, subfacts, conclusions, context):
    return(make_answer([
        "Why do you need {X}?",
        "Would it really help you to get {X}?",
        "Are you sure you need {X}?",
    ], subfacts, context))

@chatbot.action('eliza_why_dont_you')
def eliza_why_dont_you(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you really think I don't {X}?",
        "Perhaps eventually I will {X}.",
        "Do you really want me to {X}?",
        "Do you believe I don't {X}?",
        "Perhaps I will {X} in good time.",
        "Should you {X} yourself?",
        "You want me to {X}?",
    ], subfacts, context))

@chatbot.action('eliza_why_cant_i')
def eliza_why_cant_i(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you think you should be able to {X}?",
        "If you could {X}, what would you do?",
        "I don't know - why can't you {X}?",
        "Have you really tried?",
        "Do you want to be able to {X}?",
        "Do you believe this will help you to {X}?",
        "Have you any idea why you can't {X}?",
    ], subfacts, context))

@chatbot.action('eliza_i_cant')
def eliza_i_cant(w, subfacts, conclusions, context):
    return(make_answer([
        "How do you know you can't {X}?",
        "Perhaps you could {X} if you tried.",
        "What would it take for you to {X}?",
        "How do you know that you can't {X}?",
        "Have you tried?",
        "Perhaps you could {X} now.",
        "Do you really want to be able to {X}?",
        "What if you could {X}?",
    ], subfacts, context))


@chatbot.action('eliza_i_am')
def eliza_i_am(w, subfacts, conclusions, context):
    return(make_answer([
        "Did you come to me because you are {X}?",
        "How long have you been {X}?",
        "How do you feel about being {X}?",
        "How does being {X} make you feel?",
        "Do you enjoy being {X}?",
        "Why do you tell me you're {X}?",
        "Why do you think you're {X}?",
        "Is it because you are {X} that you came to me?",
        "Do you believe it is normal to be {X}?",
        "Do you know anyone else who is {X}?",
    ], subfacts, context))

@chatbot.action('eliza_are_you')
def eliza_are_you(w, subfacts, conclusions, context):
    return(make_answer([
        "Why does it matter whether I am {X}?",
        "Would you prefer it if I were not {X}?",
        "Perhaps you believe I am {X}.",
        "I may be {X} - what do you think?",
        "Are you interested in whether I am {X} or not?",
        "Would you prefer if I weren't {X}?",
        "Perhaps I am {X} in your fantasies.",
        "Do you sometimes think I am {X}?",
        "Would it matter to you?",
        "What if I were {X}?",
    ], subfacts, context))

@chatbot.action('eliza_because')
def eliza_because(w, subfacts, conclusions, context):
    return(make_answer([
        "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason apply to anything else?",
        "If {X}, what else must be true?",
        "Don't any other reasons come to mind?",
        "Does that reason seem to explain anything else?",
        "What other reasons might there be?",
    ], subfacts, context))

@chatbot.action('eliza_sorry')
def eliza_sorry(w, subfacts, conclusions, context):
    return(make_answer([
        "There are many times when no apology is needed.",
        "What feelings do you have when you apologize?",
        "Please don't apologize.",
        "Apologies are not necessary.",
        "It did not bother me. Please continue.",
    ], subfacts, context))


@chatbot.action('eliza_hello')
def eliza_hello(w, subfacts, conclusions, context):
    return(make_answer([
        "Hello... I'm glad you could drop by today.",
        "Hi there... how are you today?",
        "Hello, how are you feeling today?",
        "How do you do. Please state your problem.",
        "Hi. What seems to be your problem?",
    ], subfacts, context))

@chatbot.action('eliza_i_think')
def eliza_i_think(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you doubt {X}?",
        "Do you really think so?",
        "But you're not sure {X}?",
    ], subfacts, context))

@chatbot.action('eliza_friend')
def eliza_friend(w, subfacts, conclusions, context):
    return(make_answer([
        "Tell me more about your friends.",
        "When you think of a friend, what comes to mind?",
        "Why don't you tell me about a childhood friend?",
    ], subfacts, context))

@chatbot.action('eliza_yes')
def eliza_yes(w, subfacts, conclusions, context):
    return(make_answer([
        "You seem quite sure.",
        "OK, but can you elaborate a bit?",
        "Please go on.",
        "Please tell me more about this.",
        "Why don't you tell me a little more about this.",
        "I see.",
        "I understand.",
    ], subfacts, context))

@chatbot.action('eliza_computer')
def eliza_computer(w, subfacts, conclusions, context):
    return(make_answer([
        "Are you really talking about me?",
        "Does it seem strange to talk to a computer?",
        "How do computers make you feel?",
        "Do you feel threatened by computers?",
        "Do computers worry you?",
        "Why do you mention computers?",
        "What do you think machines have to do with your problem?",
        "Don't you think computers can help people?",
        "What about machines worries you?",
        "What do you think about machines?",
    ], subfacts, context))

@chatbot.action('eliza_is_it')
def eliza_is_it(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you think it is {X}?",
        "Perhaps it's {X} - what do you think?",
        "If it were {X}, what would you do?",
        "It could well be that {X}.",
    ], subfacts, context))

@chatbot.action('eliza_it_is')
def eliza_it_is(w, subfacts, conclusions, context):
    return(make_answer([
        "You seem very certain.",
        "If I told you that it probably isn't {X}, what would you feel?",
    ], subfacts, context))

@chatbot.action('eliza_can_you')
def eliza_can_you(w, subfacts, conclusions, context):
    return(make_answer([
        "What makes you think I can't {X}?",
        "If I could {X}, then what?",
        "Why do you ask if I can {X}?",
        "You believe I can {X} don't you?",
        "You want me to be able to {X}.",
        "Perhaps you would like to be able to {X} yourself.",
    ], subfacts, context))

@chatbot.action('eliza_can_i')
def eliza_can_i(w, subfacts, conclusions, context):
    return(make_answer([
        "Perhaps you don't want to {X}.",
        "Do you want to be able to {X}?",
        "If you could {X}, would you?",
        "Whether or not you can {X} depends on you more than on me.",
    ], subfacts, context))

@chatbot.action('eliza_you_are')
def eliza_you_are(w, subfacts, conclusions, context):
    return(make_answer([
        "Why do you think I am {X}?",
        "Does it please you to think that I'm {X}?",
        "Perhaps you would like me to be {X}.",
        "Perhaps you're really talking about yourself?",
        "Why do you say I am {X}?",
        "Why do you think I am {X}?",
        "Are we talking about you, or me?",
        "What makes you think I am {X}?",
        "Does it please you to believe I am {X}?",
        "Do you sometimes wish you were {X}?",
        "Perhaps you would like to be {X}.",
    ], subfacts, context))

@chatbot.action('eliza_i_dont')
def eliza_i_dont(w, subfacts, conclusions, context):
    return(make_answer([
        "Don't you really {X}?",
        "Why don't you {X}?",
        "Do you want to {X}?",
        "Do you wish to be able to {X}?",
        "Does that trouble you?",
    ], subfacts, context))

@chatbot.action('eliza_i_feel')
def eliza_i_feel(w, subfacts, conclusions, context):
    return(make_answer([
        "Good, tell me more about these feelings.",
        "Do you often feel {X}?",
        "When do you usually feel {X}?",
        "When you feel {X}, what do you do?",
        "Tell me more about such feelings.",
        "Do you enjoy feeling {X}?",
        "Of what does feeling {X} remind you?",
    ], subfacts, context))

@chatbot.action('eliza_i_have')
def eliza_i_have(w, subfacts, conclusions, context):
    return(make_answer([
        "Why do you tell me that you've {X}?",
        "Have you really {X}?",
        "Now that you have {X}, what will you do next?",
    ], subfacts, context))

@chatbot.action('eliza_i_would')
def eliza_i_would(w, subfacts, conclusions, context):
    return(make_answer([
        "Could you explain why you would {X}?",
        "Why would you {X}?",
        "Who else knows that you would {X}?",
    ], subfacts, context))

@chatbot.action('eliza_is_there')
def eliza_is_there(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you think there is {X}?",
        "It's likely that there is {X}.",
        "Would you like there to be {X}?",
    ], subfacts, context))

@chatbot.action('eliza_my')
def eliza_my(w, subfacts, conclusions, context):
    return(make_answer([
        "I see, your {X}.",
        "Why do you say that your {X}?",
        "When your {X}, how do you feel?",
    ], subfacts, context))

@chatbot.action('eliza_you')
def eliza_you(w, subfacts, conclusions, context):
    return(make_answer([
        "We should be discussing you, not me.",
        "Why do you say that about me?",
        "Why do you care whether I {X}?",
    ], subfacts, context))

@chatbot.action('eliza_why')
def eliza_why(w, subfacts, conclusions, context):
    return(make_answer([
        "Why don't you tell me the reason why {X}?",
        "Why do you think {X}?",
    ], subfacts, context))

@chatbot.action('eliza_i_want')
def eliza_i_want(w, subfacts, conclusions, context):
    return(make_answer([
        "What would it mean to you if you got {X}?",
        "Why do you want {X}?",
        "What would you do if you got {X}?",
        "If you got {X}, then what would you do?",
    ], subfacts, context))

@chatbot.action('eliza_mother')
def eliza_mother(w, subfacts, conclusions, context):
    return(make_answer([
        "Tell me more about your mother.",
        "What was your relationship with your mother like?",
        "How do you feel about your mother?",
        "How does this relate to your feelings today?",
        "Good family relations are important.",
    ], subfacts, context))

@chatbot.action('eliza_father')
def eliza_father(w, subfacts, conclusions, context):
    return(make_answer([
        "Tell me more about your father.",
        "How did your father make you feel?",
        "How do you feel about your father?",
        "Does your relationship with your father relate to your feelings today?",
        "Do you have trouble showing affection with your family?",
    ], subfacts, context))

@chatbot.action('eliza_child')
def eliza_child(w, subfacts, conclusions, context):
    return(make_answer([
        "Did you have close friends as a child?",
        "What is your favorite childhood memory?",
        "Do you remember any dreams or nightmares from childhood?",
        "Did the other children sometimes tease you?",
        "How do you think your childhood experiences relate to your feelings today?",
    ], subfacts, context))

@chatbot.action('eliza_i_remember')
def eliza_i_remember(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you often think of {X}?",
        "Does thinking of {X} bring anything else to mind?",
        "Why do you remember {X} just now?",
        "What in the present situation reminds you of {X}?",
        "What is the connection between me and {X}?",
        "What else does {X} remind you of?",
    ], subfacts, context))

@chatbot.action('eliza_do_you_remember')
def eliza_do_you_remember(w, subfacts, conclusions, context):
    return(make_answer([
        "Did you think I would forget {X}?",
        "Why do you think I should recall {X} now?",
        "What about {X}?",
        "You mentioned {X}?",
        "How could I forget {X}?",
        "What about {X} should I remember?",
    ], subfacts, context))

@chatbot.action('eliza_i_forget')
def eliza_i_forget(w, subfacts, conclusions, context):
    return(make_answer([
        "Can you think of why you might forget {X}?",
        "Why can't you remember {X}?",
        "How often do you think of {X}?",
        "Does it bother you to forget that?",
        "Could it be a mental block?",
        "Are you generally forgetful?",
        "Do you think you are suppressing {X}?",
    ], subfacts, context))

@chatbot.action('eliza_did_you_forget')
def eliza_did_you_forget(w, subfacts, conclusions, context):
    return(make_answer([
        "Why do you ask?",
        "Are you sure you told me?",
        "Would it bother you if I forgot {X}?",
        "Why should I recall {X} just now?",
        "Tell me more about {X}.",
    ], subfacts, context))

@chatbot.action('eliza_if')
def eliza_if(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you think it's likely that {X}?",
        "Do you wish that {X}?",
        "What do you know about {X}?",
        "Really, if {X}?",
        "What would you do if {X}?",
        "But what are the chances that {X}?",
        "What does this speculation lead to?",
    ], subfacts, context))

@chatbot.action('eliza_perhaps')
def eliza_perhaps(w, subfacts, conclusions, context):
    return(make_answer([
        "You don't seem quite certain.",
        "Why the uncertain tone?",
        "Can't you be more positive?",
        "You aren't sure?",
        "Don't you know?",
        "How likely, would you estimate?",
    ], subfacts, context))

@chatbot.action('eliza_am_i')
def eliza_am_i(w, subfacts, conclusions, context):
    return(make_answer([
        "Do you believe you are {X}?",
        "Would you want to be {X}?",
        "Do you wish I would tell you you are {X}?",
        "What would it mean if you were {X}?",
    ], subfacts, context))
