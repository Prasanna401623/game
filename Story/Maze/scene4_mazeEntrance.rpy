label maze_entrance:
  # Show the maze background
  scene bg_maze with fade

  # Add ambient maze sounds
  play sound "maze_ambience.ogg" fadein 2.0

  # Narration: Describe the setting
  "The entrance to the maze is strange. Metallic structures rise up between green vines and glowing flowers." 
  
  "A faint mist drifts along the ground." 
  
  "The hum of machinery mixes with rustling leaves. The whole place feels alive."

  # Show Kendall on screen
  show kendall at right

  # Kendall's dialogue
  kendall "Wow… This maze is enormous! How are we supposed to figure out which path is the right one?"

  # Switch to Harry
  hide kendall
  show harry at left

  harry "We'll solve it with code. Professor Carter's challenge is all about using a loop."

  # Switch back to Kendall
  hide harry
  show kendall at right

  kendall "A loop? How’s that supposed to help us get out of here?"

  # Switch to Harry
  hide kendall
  show harry at left

  # Harry explaining loops
  harry "Think of a loop as a way to repeat a set of actions. Specifically, a pre-test loop checks a condition first. If the condition is true, it keeps running."
  harry "We’ll use it to test each path in the maze until we find the exit."

  return