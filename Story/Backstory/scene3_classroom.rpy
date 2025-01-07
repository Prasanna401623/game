label classroom_scene:
    # Show the classroom background
    scene classroom_background with fade

    # Add ambient classroom sounds
    play sound "classroom_ambience.ogg" fadein 2.0

    # Narration
    "The classroom is bright and buzzing with energy. Rows of glowing laptops light up eager faces as students chat about what the day holds."

    # Show Professor Carter at the center
    show professor_carter at center
    professor_carter "Alright, class, settle down. Today, we’re diving into something exciting. A challenge that will test your coding skills like never before."

    # Show Harry and Kendall (speaking alternately)
    hide professor_carter
    show harry at left
    harry "I knew it! Another one of Carter’s legendary challenges. I can’t wait!"

    hide harry
    show kendall at right
    kendall "I’m not so sure about this. Recursion last week was tough enough. What’s it going to be this time?"

    hide kendall
    show professor_carter at center
    professor_carter "Loops! Specifically, pre-test loops. And to make it more interesting, you’ll be solving a virtual maze."

    hide professor_carter
    show harry at left
    harry "A virtual maze? That sounds awesome!"

    hide harry
    show kendall at right
    kendall "Wait… how do loops fit into a maze?"

    hide kendall
    show professor_carter at center
    professor_carter "You’ll write code to navigate the maze, testing paths one by one until you find the exit. Think of it as debugging in real time."

    # Narration with suspense
    "The room falls silent as the glowing maze appears on the projector screen, its twisting paths shimmering with neon colors."

    # Harry speaks with excitement
    hide professor_carter
    show harry at left
    harry "This is going to be fun! I’ve always wanted to try something like this."

    hide harry
    show kendall at right
    kendall "Fun? Speak for yourself. I’m already nervous."

    # Professor Carter delivers final instructions
    hide kendall
    show professor_carter at center
    professor_carter "This challenge is about teamwork, logic, and precision. Make every loop count. Are you ready?"

    # Transition to the maze setup
    "The room buzzes with anticipation as students prepare for the challenge ahead."
    return
