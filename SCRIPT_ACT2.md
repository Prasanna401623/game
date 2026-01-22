# LOOPS - Game Script for Review

## ACT 2: THE MAZE ADVENTURE
**Files Covered:** scene4_mazeEntrance.rpy, scene5_insideTheMaze.rpy, scene5_mazeNavigation.rpy (quiz setup), quiz.rpy (quizzes), maze_challenges.rpy (enable phase), scene6_enablePhase.rpy (victory)

---

### SCENE 2.1: Maze Entrance
**Location:** Entrance to the Virtual Maze  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Maze/scene4_mazeEntrance.rpy

**NARRATOR:**  
The entrance to the maze is strange. Metallic structures rise up between green vines and glowing flowers. A faint mist drifts along the ground. The hum of machinery mixes with rustling leaves. The whole place feels alive.

**KENDALL:**  
Wow… This maze is enormous! How are we supposed to figure out which path is the right one?

**HARRY:**  
We'll solve it with code. Professor Carter's challenge is all about using a loop.

**KENDALL:**  
A loop? How's that supposed to help us get out of here?

**HARRY:**  
Think of a loop as a way to repeat a set of actions. Specifically, a pre-test loop checks a condition first. If the condition is true, it keeps running. We'll use it to test each path in the maze until we find the exit.

---

### SCENE 2.2: Inside the Maze - Loop Explanation
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Maze/scene5_insideTheMaze.rpy

**NARRATOR:**  
The maze stretches out in all directions. The walls glow faintly, and the paths keep shifting. A faint blue mist hangs in the air.

**KENDALL:**  
Whoa. This is nothing like the entrance. It's like a whole other world in here.

**HARRY:**  
It's definitely more than just a puzzle. But I think I can show you how we can solve it systematically.

**KENDALL:**  
Systematically? How?

**HARRY:**  
Exactly. Wait a second. Let me show you from my iPad.

**NARRATOR:**  
Harry pulls out his iPad. The screen lights up, showing an overhead view of simple maze.

*(Scene transition to iPad display)*

**NARRATOR:**  
A simple maze with multiple paths is displayed on the screen.

**KENDALL:**  
That's what we're stuck in?

**HARRY:**  
No, this is an example of a simple maze. We can solve this maze easily in our mind. But I wanted to show you how we can use loop to solve it.

**KENDALL:**  
Okay, I'm listening.

*(Harry writes code on iPad)*

**NARRATOR:**  
Harry writes a code in his iPad. The code is an example of loop using while statement.

**NARRATOR:**  
Harry points to the screen. 'This loop checks each path. If it leads to the exit, it stops. If not, it moves to the next path.'

**KENDALL:**  
So, it's like the loop keeps asking, 'Am I at the exit?' and only stops when it gets a yes?

**HARRY:**  
Exactly. Initially it first path is checked. If it doesn't lead to the exit, it moves to the next path. Pre-test loops are perfect for situations like this where we don't know the solution upfront. We just keep testing until we find it.

*(Scene transition back to maze interior)*

**NARRATOR:**  
Harry switches off his iPad and puts it away.

**HARRY:**  
Now that you've seen how a loop works, there's something else you should know. Loops can run into problems. Let me give you some examples.

**KENDALL:**  
Problems? What kind of problems?

**HARRY:**  
For starters, you might encounter an infinite loop if the condition is never updated or if there's a mistake in your logic. But that's not the only type of issue. There are others, too.

---

### SCENE 2.3: Learning About Errors
**Location:** Maze Interior (continuing from previous scene)  
**Characters:** Harry, Kendall  
**Source File:** Story/Maze/scene5_insideTheMaze.rpy  
**NOTE:** This section is NON-CHRONOLOGICAL - player can choose any error to study first

**[ERROR SELECTION MENU - Player chooses which error to learn about]**
- Infinite Loop Error
- Logic Error
- Off-By-One Error
- Pre-Test Logic Error

*(The player will go through all four errors in any order they choose. See APPENDIX A for full error explanations - not part of chronological narrative)*

---

### SCENE 2.4: Quiz Time - Testing Knowledge
**Location:** Maze Interior  
**Characters:** Harry, Kendall  
**Source File:** Story/Quizzes/quiz.rpy

*(After all errors have been learned)*

**HARRY:**  
Great work learning about all those errors! Now let's see how well you understood them.

**KENDALL:**  
Quiz time? I think I'm ready!

**HARRY:**  
You'll answer 4 questions, one for each error type we covered. Let's begin!

---

#### QUIZ 1: INFINITE LOOP
**Source File:** Story/Quizzes/quiz.rpy (label: infinite_loop_quiz)

**HARRY:**  
What do you think? Choose the correct answer below.

**[QUIZ QUESTION DISPLAYED ON SCREEN]**
*(Player selects answer)*

**HARRY (if correct):**  
*(Feedback varies based on answer)*

**HARRY (if incorrect):**  
Not quite. Think about when the loop should keep running.
*(If two attempts) Remember what we learned about loop conditions.*

---

#### QUIZ 2: LOGIC ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: logic_error_quiz)

**[QUIZ QUESTION DISPLAYED ON SCREEN]**
*(Player selects answer)*

---

#### QUIZ 3: OFF-BY-ONE ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: off_by_one_quiz)

**[QUIZ QUESTION DISPLAYED ON SCREEN]**
*(Player selects answer)*

---

#### QUIZ 4: PRE-TEST LOGIC ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: pre_test_logic_quiz)

**[QUIZ QUESTION DISPLAYED ON SCREEN]**
*(Player selects answer)*

---

**HARRY:**  
You've completed all the quizzes! Let me show you your final score.

**[FINAL SCORE DISPLAYED]**
*(3 second pause)*

---

### SCENE 2.5: Enable Phase - Time to Navigate!
**Location:** Maze Interior  
**Characters:** Harry, Kendall  
**Source File:** Story/Maze/scene6_enablePhase.rpy

**KENDALL:**  
Okay, we've studied all the errors. But we're still stuck in this maze!

**HARRY:**  
You're right. The knowledge was important, but now we need to actually use it to get out of here.

**KENDALL:**  
So... we need to write the actual code to navigate through?

**HARRY:**  
Exactly! I'll help guide you, but you'll need to make the decisions yourself. Think of it like... I'm your code reviewer, but you're the programmer.

**KENDALL:**  
No pressure, right? Okay, I can do this. Let's start!

---

#### CHALLENGE 1: Navigate the Maze (Loop Condition)
**Source File:** Story/Quizzes/maze_challenges.rpy (label: maze_challenge_1)

**HARRY:**  
Alright, we're at our first junction. I've got the basic navigation code here. But I need you to tell me—what condition should keep us moving?

**[CHALLENGE 1 QUESTION: Choose the correct loop condition]**
- Option A: while True
- Option B: while at_exit
- Option C: while not at_exit *(CORRECT)*

**HARRY (if correct):**  
Perfect! The loop should continue while we're NOT at the exit. Great job!

**KENDALL:**  
That makes sense! We keep going until we reach the exit.

**HARRY:**  
Exactly! Let's move forward.

**HARRY (if incorrect):**  
Not quite. Think about when the loop should keep running.
*(If 2+ attempts) Remember what we learned about loop conditions.*

---

#### CHALLENGE 2: Prevent Infinite Loop (Add Safety Counter)
**Source File:** Story/Quizzes/maze_challenges.rpy (label: maze_challenge_2)

**KENDALL:**  
Great! That worked! But... what if the maze has a glitch or something? Couldn't we get stuck in an infinite loop?

**HARRY:**  
Good thinking! We should add a safety measure. What's the best way to write this loop condition?

**[CHALLENGE 2 QUESTION: What's the safest loop condition?]**
- Option A: while not at_exit and steps < 100 *(CORRECT)*
- Option B: while steps < 100
- Option C: while not at_exit

**HARRY (if correct):**  
Excellent! Adding a step counter prevents infinite loops while still checking for the exit.

**KENDALL:**  
So we check both conditions—not at exit AND haven't exceeded max steps!

**HARRY:**  
Exactly! That's how you write safe loops.

**HARRY (if partial answer - option C):**  
That works, but what if the maze has a bug? We might get stuck in an infinite loop! Think about what we learned about preventing infinite loops.
*(If 2+ attempts) Remember, we should add a safety counter to prevent infinite loops.*

**HARRY (if wrong answer):**  
That's not quite right. We still need to check if we've reached the exit!
*(If 2+ attempts) We need BOTH conditions: checking for the exit AND limiting the steps.*

---

#### CHALLENGE 3: Fix Off-By-One Error (Path Counting)
**Source File:** Story/Quizzes/maze_challenges.rpy (label: maze_challenge_3)

**HARRY:**  
We're getting close! I can see the exit, but there are 5 different paths ahead.

**KENDALL:**  
So we need to check all 5 paths, numbered 1 through 5?

**HARRY:**  
Exactly. Which loop condition will check all 5 without missing any?

**[CHALLENGE 3 QUESTION DISPLAYED ON SCREEN]**
*(Player selects answer)*

**HARRY (if correct):**  
*(Feedback)*

---

### SCENE 2.6: Victory - Escape from the Maze
**Location:** Maze Interior → Maze Entrance → Victory Scene  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Maze/scene6_enablePhase.rpy (label: maze_victory)

**HARRY:**  
Amazing work, Kendall! You've completed all the challenges!

**KENDALL:**  
I did it! I can't believe I actually solved them all!

**HARRY:**  
You understood loops perfectly. Now let's get out of this maze!

**NARRATOR:**  
The maze walls begin to shift and glow. A clear path forward appears, lit up in blue.

*(Scene transition)*

**NARRATOR:**  
Harry and Kendall rush through the glowing pathway, their footsteps echoing through the corridors.

*(Scene transition to victory background)*

**KENDALL:**  
We made it! We escaped the maze!

**HARRY:**  
You escaped the maze, Kendall. And you've got pre-test loops down now!

**KENDALL:**  
Thanks to your teaching! I feel like I can tackle any loop now.

**HARRY:**  
That's the spirit! Remember: always check your conditions, watch for infinite loops, and pay attention to your boundaries.

**KENDALL:**  
Got it! I'm ready for the next challenge!

**[FINAL SCORE DISPLAYED]**
*(4 second pause)*

**NARRATOR:**  
Congratulations! You've completed 'Escape the Virtual Maze'! You've learned about pre-test loops, common errors, and how to fix them. Keep practicing!

---

**END OF ACT 2**
**END OF GAME**

---

## APPENDIX A: ERROR EXPLANATIONS (NON-CHRONOLOGICAL)

**NOTE TO PROFESSOR:** These error explanations are not part of the chronological narrative. The player can choose to learn about these errors in any order during Scene 2.3. Each error has its own detailed explanation scene with examples.

### Error 1: Infinite Loop Error
**Source File:** Story/Errors/infinite_loop_error.rpy  
*(Full dialogue to be documented separately if needed)*

### Error 2: Logic Error
**Source File:** Story/Errors/logic_error.rpy  
*(Full dialogue to be documented separately if needed)*

### Error 3: Off-By-One Error
**Source File:** Story/Errors/off_by_one_error.rpy  
*(Full dialogue to be documented separately if needed)*

### Error 4: Pre-Test Logic Error
**Source File:** Story/Errors/pre_test_logic_error.rpy  
*(Full dialogue to be documented separately if needed)*

---

**NOTE:** Would you like me to create a separate document with the full error explanation dialogues from the Errors folder?
