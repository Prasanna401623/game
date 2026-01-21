label hallway_scene:
    # Show the hallway background
    scene hallway_background with fade

    # Add ambient hallway sounds
    play sound "hallway_ambience.ogg" fadein 2.0

    # Narration
    "The hallway is quiet, with only a few students lingering near their lockers. Harry spots Kendall walking ahead and hurries to catch up."

    # Conversation begins
    show harry at left
    harry "Hey, Kendall! Wait up!"
    
    hide harry
    show kendall at right
    kendall "Oh, hey Harry. How’s it going?"

    hide kendall
    show harry at left
    harry "Not bad. Just another day at the coding grind. How about you?"
    
    hide harry
    show kendall at right
    kendall "Same here. Though, I'm hoping today won't be too crazy. I need a break from these puzzles."
    
    hide kendall
    show harry at left
    harry "Don’t count on it. This is Professor Carter we’re talking about. He probably dreams of ways to make our lives harder."

    hide harry
    show kendall at right
    kendall "You’re probably right. What do you think he’s got planned for today?"

    hide kendall
    show harry at left
    harry "Whatever it is, I’m ready. Bring it on!"

    hide harry
    show kendall at right
    kendall "I wish I had your confidence. Loops are already tricky enough without Carter throwing in some wild twist."

    hide kendall
    show harry at left
    harry "Loops aren’t so bad. They’re just repetitive logic. Once you crack the pattern, it’s easy."

    hide harry
    show kendall at right
    kendall "That’s easy for you to say, Mr. ‘Coding Comes Naturally to Me.’"

    hide kendall
    show harry at left
    harry "It's not magic, Kendall. It's just practice. Besides, Carter's challenges are always fun."

    hide harry
    show kendall at right
    kendall "Fun, huh? Tell that to my sleep schedule. Recursion last week nearly broke me."

    hide kendall
    show harry at left
    harry "You made it through, though. That’s what counts."

    hide harry
    show kendall at right
    kendall "Barely. Let’s just hope today’s challenge doesn’t involve anything crazy. I’d like one normal day for a change."

    # Transition to classroom
    hide kendall
    "They reach the classroom door. Students are chatting inside."

    show kendall at right
    kendall "Here we go. Let’s see what Carter has up his sleeve today."

    hide kendall
    show harry at left
    harry "I bet it’s going to be something fun."

    hide harry
    return
