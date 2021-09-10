# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player_name]")
define bro = Character("Brodie")
define z = Character("Zach")


# The game starts here.

label start:

    #The player name system is just a placeholder.
    $ player_name = ""
    $ player_name = renpy.input("Placeholder")

    "..."
    "...Well, {i}that was embarrassing.{/i}"
    "I exit my last period for the day as fast as I can."

    scene bg classroom
    with dissolve

    "In my last class, we were supposed to sort into groups to discuss the reading and compare notes."
    "Ms. Morrison told the whole class to bunch up, and everyone stood."
    "The sound of screeching chairs and eager footsteps surrounded me, friend groups quickly assembling."
    "And as you might have guessed, I was still frozen in my seat, at my now solitary table."
    "I suddenly felt as though I was shackled to my desk."
    "I didn’t wanna look around, I’d look like a 5 year old lost at the mall."
    "But I did, both hopeful and apprehensive to meet a classmate’s eyes, thinking maybe they’d make a socially merciful decision to include me."
    "But, in typical fashion, the teacher had to practically hold my hand as she informed another group I’d be joining them for today."
    "Well, I say ‘informed.’ In reality, she asked them politely, but in the moment it felt like she was on her knees, begging them."
    "The table was basically an image of juvenile popularity. Some of the girls with the most social clout in the grade."
    "And me."
    "I could have sworn one of them muttered {i}\“fuck..!\”{/i} quietly when I sat down, but my mind tends to play tricks on me."
    "Though, I knew for a fact they did {i}not{/i} really care about the reading."
    "I knew this because I asked them what they thought about the last chapter, and they looked at me and said \“We don’t really care.\”"
    "They were mainly occupied with talking amongst themselves."
    "So, whatever. I don’t mind just doing nothing for the last 15 minutes of class, really."
    "As they laughed with each other, I kind of zoned out and just stared at the marble desktop."
    "Then, with about 5 minutes til the bell, I heard one girl say something interesting."
    "\“Are you going on the 7th? To see the band?\”"
    "{i}Someone in this school has a band?{/i}"
    "\"It depends on what time.\""
    "\"I don't remember. It says it on the poster. I'll show you after class.\""
    "{i}What band?!{/i}"
    "\“I guess it doesn’t matter if we miss a few songs anyway. I’m really not going for the band, just to smoke in the bathroom.\”"
    "\“Yeah. It might be cool though. I’ve always wanted to learn an instrument.\""
    "{i}Wait, this is perfect!{/i} I thought."
    "{i}This is my “in” for the conversation. I can bring up my music, and we can strike up a chat. I could chat with the popular kids! And not about the reading!{/i}"
    "The old me would have just kept my mouth shut, but I made a decision when I moved here: new town, new me."
    "No more awkwardness or social anxiety. Now hurry up and speak before the subject changes!"
    p "\"Um, you know, I play a few instruments.\""
    "..."
    "Silence."
    "They glared."
    p "\"Learning an instrument is really fun! And fulfilling. I'd recommend it.\""
    "More glaring. And some subtle scoffing."
    "After exchanging some glances, one of the girls finally piped up with a laugh, \"Okay, cool.\""
    "\"Yeah, it can be hard at first but it’s worth it!\”"
    "{i}Why am I still talking?!{/i}"
    "\“Are you any good?\” one of the girls asked."
    "The real answer is 'not really.'"
    "But I need to be confident if I’m ever gonna shed my loner ways."
    #rewrite the next line
    "The key to avoiding social awkwardness is to not let anything feel awkward!"
    "\“Well, yes, I’d say I’m pretty okay!\” I force a smile."
    "Yet more scoffing."
    "\"Haha, yeah, I bet!\""
    "This clearly sarcastic remark stings like hell."
    "They all chortle maliciously. My ears burn."
    "And that's why I've decided to never try to make friends again."
    "I have a demeanor that no one can really take seriously. Especially with my music."
    "My parents don’t even take my music seriously. No one does."
    "I’m sunken in my seat, trying to will myself out of existence, when the bell rings."
    "I dart out of the room as quickly as I can, trying to escape the smothering embarrassment in the atmosphere."

    scene bg hallway 1
    with fade
    play sound "audio/classEnd.mp3"

    "And here we are! Speedwalking through the crowded hallway with my head down."
    "I can’t believe I’ve been going to the new school for an entire month now. It’s already the end of September!"
    "In the summer, I told myself I’d have a friend group by now."
    "Yet, every time I’ve tried to make friends, it goes something like that."
    "Except for Brodie, my gym partner."
    "He’s just a nice dude. The kind that doesn’t even give you a warning, and you’re already in a conversation with him."
    "I think he’s kind of friends with everyone."
    "But speak of the devil, there he is."
    show brodie 1 with dissolve
    bro "Hey [player_name]! What are you doing in the west wing? Shouldn’t you be heading home?"
    "Oh jeez. In my rush to get away from that classroom, I got completely lost."
    p "Whoops. Good point. I guess I went the wrong way."
    p "This school seems huge when you’re new, to be fair…"
    bro "Nah, I get that. I couldn’t navigate this place til about sophomore year!"
    "Yep, Brodie always finds a way to relate."
    bro "I might as well walk with you if we’re both heading out, yeah?"
    p "Fine with me."

    #change bg
    
    "We walk downstairs and approach the big exit doors, small-talking the whole time."
    "When suddenly, I notice a poster hastily scotch taped to the corridor wall."
    p "Hey, what’s that for?"
    "I approach it and read."

    #show the poster

    p "So that must be the band everyone’s talking about?"
    bro "Yep! Those guys are legit. I’m friends with them."
    p "Well, of course you are, Brodie."
    bro "So, are you going?"
    p "Oh, jeez. As much as I’d love to see this band, I don’t think the whole \“crowded high school party\” thing is my scene."
    p "I can barely stand the hallways."
    bro "Well, I won't force you. Suit yourself."
    "But, wait...{i}what is that one paragraph on the bottom about?{/i}"
    "{i}An audition? Play a real concert?{/i}"
    "{i}I'm not actually thinking about this...{/i}"
    bro "Hey, wait, you play music too, right? I think they’re looking for another player!"
    bro "You should totally audition!"
    p "W-what? No..."
    bro "Come on! What are you afraid of?"
    p "I mean, there’s no way they’d want {i}me.{/i}"
    p "Besides, a million people are probably gonna audition."
    p "And playing in front of people like that? I don’t know…It just doesn’t sound like me."
    bro "Aww, okay."
    bro "Well, do what makes you comfortable I guess."
    bro "But I think you should try to step out of your comfort zone a little!"
    "Hah."
    "Because we all know how well that went last time."
    bro "Besides, they're really cool dudes."
    bro "Anyway, I'm about to miss my bus. Lemme know what you decide on!"
    bro "See ya!"
    p "Adios, Brodie."
    hide brodie 1 with easeoutright
    "He jogs out the door, but I stay here, staring at the poster."
    "{i}Step out of my comfort zone...{/i}"
    "{i}Get my music taken seriously...{/i}"
    "{i}...Make new friends..?{/i}"
    "...I don't know what to do."
    "..."
    "..."
    "But it couldn't hurt to at least learn the song, right?"


    return
