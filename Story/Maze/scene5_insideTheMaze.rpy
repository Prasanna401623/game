label inside_maze:
    # Show the maze interior background
    scene bg_maze_interior with fade

    # Add ambient maze sounds
    play sound "maze_interior_ambience.ogg" fadein 2.0

    # Narration: Describe the interior
    "The maze stretches out in all directions. The walls glow faintly, and the paths keep shifting."
    "A faint blue mist hangs in the air."

    # Kendall expresses awe
    show kendall at right
    kendall "Whoa. This is nothing like the entrance. It's like a whole other world in here."

    # Switch to Harry
    hide kendall
    show harry at left
    harry "It's definitely more than just a puzzle. But I think I can show you how we can solve it systematically."

    # Harry takes out his iPad
    hide harry
    show kendall at right
    kendall "Systematically? How?"

    hide kendall
    show harry at left
    harry "Exactly. Wait a second. Let me show you from my iPad."

    # Harry takes out his iPad
    hide harry
    scene bg_ipad_black with dissolve
    "Harry pulls out his iPad. The screen lights up, showing an overhead view of simple maze."

    # Display the maze image
    scene bg_maze_example_ipad with fade
    "A simple maze with multiple paths is displayed on the screen. "

    # Switch back to Kendall's voice
    show kendall at left
    kendall "That's what we're stuck in?"

    # Switch to Harry
    hide kendall
    show harry at left
    harry "No, this is an example of a simple maze."  
    harry "We can solve this maze easily in our mind. But I wanted to show you how we can use loop to solve it."

    hide harry
    show kendall at right
    kendall "Okay, I'm listening."

    hide kendall

    # Show the highlighted path animation (description)
    scene maze_iPad_solveSimpleMaze with dissolve
    "Harry writes a code in his iPad. The code is an example of loop using while statement."

    # Narration: Code explanation
    "Harry points to the screen. 'This loop checks each path. If it leads to the exit, it stops. If not, it moves to the next path.'"

    # Show Kendall's reaction
    hide harry
    show kendall at right
    kendall "So, it's like the loop keeps asking, 'Am I at the exit?' and only stops when it gets a yes?"

    # Switch to Harry
    hide kendall
    show harry at left
    harry "Exactly. Initially it first path is checked. If it doesn't lead to the exit, it moves to the next path."
    
    harry "Pre-test loops are perfect for situations like this where we don't know the solution upfront. We just keep testing until we find it."

    # Transition back to the maze
    hide harry
    scene bg_maze_interior with dissolve
    "Harry switches off his iPad and puts it away."

        # Harry starts the conversation about errors
    show harry at left
    harry "Now that you've seen how a loop works, there's something else you should know."
    harry "Loops can run into problems. Let me give you some examples."

    # Kendall shows curiosity
    hide harry
    show kendall at right
    kendall "Problems? What kind of problems?"

    # Harry explains briefly
    hide kendall
    show harry at left
    harry "For starters, you might encounter an infinite loop if the condition is never updated or if there's a mistake in your logic."
    harry "But that's not the only type of issue. There are others, too."

label choose_error:
    while error_options:
        # Ask the player to choose an error
        $ choice = renpy.display_menu([(error, error) for error in error_options])

        # Remove the selected error from the list
        $ remove_error(choice)

        # Jump to the corresponding error explanation
        if choice == "Infinite Loop":
            jump infinite_loop_error
        elif choice == "Logic Error":
            jump logic_error
        elif choice == "Off-By-One Error":
            jump off_by_one_error
        elif choice == "Pre-Test Logic Error":
            jump pre_test_logic_error

    jump all_errors_done  # Once all errors are covered, continue the game

label all_errors_done:
    show harry at left
    harry "These are just a couple of examples. Errors can be tricky, but you'll get better at spotting them with practice."
    harry "Before we tackle the maze, let's make sure you really understand these concepts."
    hide harry
    
    # Call all quizzes in sequence
    call all_quizzes
    
    # After quizzes, move to enable phase
    jump enable_phase  # Jump to the next scene instead of returning
