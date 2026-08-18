# LOOPS - Game Script for Review

## ACT 3: TESTING AND APPLYING KNOWLEDGE
**Files Covered:** quiz.rpy (quizzes), maze_challenges.rpy (challenges), scene6_enablePhase.rpy (victory)

---

### SCENE 3.1: Quiz Time - Testing Knowledge
**Location:** Maze Interior  
**Characters:** Harry, Kendall  
**Source File:** Story/Quizzes/quiz.rpy

*(After all four errors have been learned in Act 2, continuing directly from Scene 2.4, "All Errors Complete")*

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

**[QUIZ QUESTION DISPLAYED: What is the output of this code?]**
- It runs normally and stops after 5 iterations.
- It will run forever. *(CORRECT)*
- It won't run at all.

**HARRY (if correct):**  
Good job! The condition never changes, so the loop runs forever.

**KENDALL:**  
That makes sense! So we need to be careful about our loop conditions.

**HARRY:**  
That's the idea. Now you know how to spot infinite loops.

**KENDALL:**  
I can't wait to learn more!

**HARRY (if incorrect):**  
Not quite. Think about whether the loop condition is ever updated.
*(If 2+ attempts) Let me explain this concept again. [Returns to infinite_loop_error]*
*(Option to try again or re-read about Infinite Loops)*

---

#### QUIZ 2: LOGIC ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: logic_error_quiz)

**HARRY:**  
Here's a tricky one about logic errors. What do you think will happen?

**[QUIZ QUESTION DISPLAYED: What happens when you run this code?]**
- It never prints anything. *(CORRECT)*
- It prints 'Found it!' 5 times.
- It prints 'Found it!' once.

**HARRY (if correct):**  
Excellent! The condition 'count > 5' is never true because the loop stops at count < 5. That's a logic error.

**KENDALL:**  
Oh! So the logic is wrong, even though the code runs without crashing.

**HARRY:**  
Exactly! Logic errors are tricky because the code runs, but it doesn't do what you want.

**KENDALL:**  
I'll definitely watch out for those!

**HARRY (if incorrect):**  
Not quite. Look carefully at the condition inside the if statement compared to the while loop condition.
*(If 2+ attempts) Let me explain logic errors again. [Returns to logic_error]*
*(Option to try again or re-read about Logic Errors)*

---

#### QUIZ 3: OFF-BY-ONE ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: off_by_one_quiz)

**HARRY:**  
Let's test your understanding of off-by-one errors!

**[QUIZ QUESTION DISPLAYED: How many times does this loop print 'Hello'?]**
- 6 times
- 5 times *(CORRECT)*
- 4 times

**HARRY (if correct):**  
Perfect! Count starts at 0, so the loop runs for 0, 1, 2, 3, and 4. That's 'Hello' five times before the condition fails.

**KENDALL:**  
I almost said 4. I assumed it started counting at 1.

**HARRY:**  
And that's the trap. Off-by-one errors come from the starting value just as often as from the condition.

**KENDALL:**  
Got it! I'll check both ends before I trust a loop.

**HARRY (if incorrect):**  
Not quite. Trace it carefully: count starts at 0, and the loop runs while count < 5. That's 0, 1, 2, 3, and 4.
*(If 2+ attempts) Let me explain off-by-one errors again. [Returns to off_by_one_error]*
*(Option to try again or re-read about Off-By-One Errors)*

---

#### QUIZ 4: PRE-TEST LOGIC ERROR
**Source File:** Story/Quizzes/quiz.rpy (label: pre_test_logic_quiz)

**HARRY:**  
One more! This is about pre-test logic errors.

**[QUIZ QUESTION DISPLAYED: What is the output of this code?]**
- It prints nothing *(CORRECT)*
- It runs forever
- It prints 10, 11, 12, 13, 14

**HARRY (if correct):**  
Correct! Since count starts at 10 and the condition is 'count < 5', the condition is false from the very beginning. The loop never runs!

**KENDALL:**  
So the pre-test checks the condition first, sees it's false, and skips the entire loop?

**HARRY:**  
Exactly! That's why they're called pre-test loops—they test the condition before running any code.

**KENDALL:**  
I need to make sure my starting values make sense with my loop conditions!

**HARRY (if incorrect):**  
Not quite. Remember, pre-test loops check the condition BEFORE running any code.
*(If 2+ attempts) Let me explain pre-test logic errors again. [Returns to pre_test_logic_error]*
*(Option to try again or re-read about Pre-Test Logic Errors)*

---

**HARRY:**  
You've completed all the quizzes! Let me show you your final score.

**[FINAL SCORE DISPLAYED]**
*(3 second pause)*

---

### SCENE 3.2: Enable Phase - Time to Navigate!
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
That's right! I'll help guide you, but you'll need to make the decisions yourself. Think of it like... I'm your code reviewer, but you're the programmer.

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
Nice work. Let's move forward.

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
Spot on. That's how you write safe loops.

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

**[CHALLENGE 3 QUESTION: Check exactly 5 paths (1 to 5)]**
- Option A: while path < 6 *(CORRECT - alternate)*
- Option B: while path < 5
- Option C: while path <= 5 *(CORRECT)*

**DESIGN NOTE:** Two of the three options are correct by design. `while path <= 5` and `while path < 6` both check paths 1 through 5, so both are accepted and each has its own dialogue branch. Only `while path < 5` is wrong, because it stops at path 4. This is deliberate: after three challenges of matching one right answer, the goal is to show that correct logic can be written more than one way.

**HARRY (if correct - option C, `while path <= 5`):**  
Perfect! Using <= 5 means we check paths 1, 2, 3, 4, and 5. That's exactly what we need!

**KENDALL:**  
I see! The <= includes 5, while < would stop before it.

**HARRY:**  
That's the difference. You've got off-by-one errors figured out!

**HARRY (if correct - option A, `while path < 6`):**  
Correct! Using < 6 also checks paths 1 through 5. Both this and <= 5 work!

**KENDALL:**  
So there can be multiple ways to write the same logic?

**HARRY:**  
Often, yes. As long as the logic is correct, there are usually multiple solutions.

**HARRY (if wrong answer - option B, `while path < 5`):**  
Not quite. That would only check paths 1, 2, 3, and 4. We'd miss path 5! Remember what we learned about off-by-one errors.
*(If 2+ attempts) We need to include 5 in our check. Think about < versus <=.*

---

### SCENE 3.3: Victory - Escape from the Maze
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

**END OF ACT 3**
**END OF GAME**



Edits made v1: 

1. Added the image of full of students in Scene
2. Cleared the confusion about Narrator. Narrator is only used in paper script, not on visual novel.
3. Fixed the position of Kendall in scene 2.2
4. Again in scene 2.2, used "on my ipad" instead of "using my ipad"
5. Added another infinite loop error code
6. In scene 2.3B, clarified the problem statemen
7. Use of printf is correct.