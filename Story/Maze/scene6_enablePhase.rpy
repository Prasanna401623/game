label enable_phase:
    # Show the maze interior background
    scene bg_maze_interior with fade

    # Add ambient maze sounds
    play sound "maze_interior_ambience.ogg" fadein 2.0

    # Introduction to Enable Phase
    show harry at left
    harry "Now that you've learned about all the loop errors, it's time to apply your knowledge!"
    harry "I'll give you some code challenges. You'll need to complete them on your own."
    
    hide harry
    show kendall at right
    kendall "On my own? No hints this time?"
    
    hide kendall
    show harry at left
    harry "You've got this, Kendall! Everything you need to know, you've already learned."
    hide harry
    
    # Reset attempts for challenges
    $ attempts = 0
    
    # Run the 3 code challenges
    call maze_challenge_1
    call maze_challenge_2
    call maze_challenge_3
    
    # All challenges completed - Move to victory
    jump maze_victory


label maze_victory:
    # Show completion and escape sequence
    scene bg_maze_interior with fade
    show harry at left
    harry "Amazing work, Kendall! You've completed all the challenges!"
    
    hide harry
    show kendall at right
    kendall "I did it! I can't believe I actually solved them all!"
    
    hide kendall
    show harry at left
    harry "You understood loops perfectly. Now let's get out of this maze!"
    hide harry
    
    # Maze escape sequence
    scene bg_maze_interior with dissolve
    "The maze walls begin to shift and glow. A clear path forward appears, illuminated by bright blue light."
    
    scene bg_maze with dissolve
    "Harry and Kendall rush through the glowing pathway, their footsteps echoing through the corridors."
    
    # Victory scene
    scene bg_maze with fade
    show kendall at right
    kendall "We made it! We escaped the maze!"
    
    hide kendall
    show harry at left
    harry "You did more than escape, Kendall. You mastered pre-test loops!"
    
    hide harry
    show kendall at right
    kendall "Thanks to your teaching! I feel like I can tackle any loop now."
    
    hide kendall
    show harry at left
    harry "That's the spirit! Remember: always check your conditions, watch for infinite loops, and pay attention to your boundaries."
    
    hide harry
    show kendall at right
    kendall "Got it! I'm ready for the next challenge!"
    
    # Show final score one more time
    hide kendall
    scene bg_maze_interior with fade
    show screen final_score_display
    with dissolve
    pause 4.0
    hide screen final_score_display
    with dissolve
    
    # Final message
    scene bg_maze with fade
    show harry at left with dissolve
    show kendall at right with dissolve
    
    "Congratulations! You've completed 'Escape the Virtual Maze'!"
    "You've learned about pre-test loops, common errors, and how to fix them."
    "Keep practicing, and you'll become a loop master in no time!"
    
    hide harry
    hide kendall
    
    # Game complete
    return
    
    # Game complete
    return