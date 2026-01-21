label classroom_scene:
    # Show the classroom background
    scene classroom_background with fade

    # Add ambient classroom sounds
    play sound "classroom_ambience.ogg" fadein 2.0

    # Narration
    "The classroom is bright and full of students. Laptops are open, and everyone's talking about what's coming next."

    # Show Professor Carter at the center
    show professor_carter at center
    professor_carter "Alright, class, settle down. Today, we're diving into something exciting. A challenge that will test your coding skills."

    # Show Harry and Kendall (speaking alternately)
    hide professor_carter
    show harry at left
    harry "I knew it! Another one of Carter's challenges. I can't wait!"

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

    # Narration with suspense
    "The room goes quiet. The maze appears on the projector screen—twisting paths lit up in neon colors."

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
    "Students start getting ready for the challenge."
    return
