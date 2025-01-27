label logic_error:
    # Explanation for Logic Error
    scene bg_maze_interior with dissolve

    # Harry starts the explanation
    show harry at left
    harry "Logic errors are trickier. They don’t break your code outright, but they make it behave in ways you didn’t intend."

    # Kendall asks for clarification
    hide harry
    show kendall at right
    kendall "So, the loop works, but it’s doing the wrong thing?"

    # Harry elaborates
    hide kendall
    show harry at left
    harry "Exactly. Let’s say you want to check numbers greater than 5, but you accidentally write it to check numbers greater than 6."
    harry "It doesn’t crash, but it skips the range you wanted to include."

    # Show the first code snippet as background
    scene bg_logic_error_code1 with dissolve
    "Harry points to the screen where the incorrect code is displayed."

    # Kendall reacts
    show kendall at right
    kendall "That’s tricky. It looks fine at first, but the result is wrong. How would I catch something like this?"

    # Harry explains testing
    hide kendall
    show harry at left
    harry "That’s the problem with logic errors—they don’t cause crashes. You’d need to test your code carefully and compare the output to what you expect."

    # Show the fixed code as background
    scene bg_logic_error_code2 with dissolve
    "Harry shows the corrected version of the code."

    # Harry explains the fix
    harry "Here’s the fixed version. Now the loop checks for numbers greater than 5 as intended, so you get the correct result."

    # Kendall reflects
    hide harry
    show kendall at right
    kendall "So, the key is testing the code and double-checking the logic carefully, right?"

    # Harry confirms
    hide kendall
    show harry at left
    harry "Exactly. With careful testing and attention to detail, you can catch logic errors before they cause trouble."

    return
