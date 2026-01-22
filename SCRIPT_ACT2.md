# LOOPS - Game Script for Review

## ACT 2: LEARNING ABOUT LOOPS AND ERRORS
**Files Covered:** scene4_mazeEntrance.rpy, scene5_insideTheMaze.rpy, infinite_loop_error.rpy, logic_error.rpy, off_by_one_error.rpy, pre_test_logic_error.rpy

**NOTE:** During Scene 2.3, the player can choose to learn about errors in ANY order. All four error explanations are documented here in sequence for completeness.

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

--- - Introduction
**Location:** Maze Interior (continuing from previous scene)  
**Characters:** Harry, Kendall  
**Source File:** Story/Maze/scene5_insideTheMaze.rpy  

**NOTE:** The player can choose to learn about these errors in ANY order. All four error explanations are documented below in sequence.

**[ERROR SELECTION MENU - Player chooses which error to learn about first]**

---

### SCENE 2.3A: INFINITE LOOP ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/infinite_loop_error.rpy

**HARRY:**  
An infinite loop happens when the condition for the loop never becomes false. In simple terms, it just keeps going forever.

**KENDALL:**  
Forever? That sounds... bad. What would cause that to happen?

**HARRY:**  
Let's say you write a loop but forget to update the condition inside it.

*(Scene transition to code example screen - bg_infinite_loop_code1)*

**NARRATOR:**  
Harry points to the screen where the incorrect code is displayed.

**HARRY:**  
This kind of loop has no condition to stop, so it keeps running endlessly.

**KENDALL:**  
So, the loop keeps asking the same question, but there's no way to change the answer?

**HARRY:**  
Exactly. Think of it like someone repeatedly asking, 'Is it raining?' when they're inside and can't check. To fix it, you need to make sure the loop's condition changes. For example, by updating a variable or checking a new value inside the loop.

*(Scene transition to corrected code screen - bg_infinite_loop_code2)*

**NARRATOR:**  
Harry shows the corrected version of the code.

**HARRY:**  
Here, we update the variable `count` in each iteration, so the condition eventually becomes false, and the loop stops.

**KENDALL:**  
Got it! So, as long as we update the condition properly, the loop will end when it's supposed to.

*(Scene transition back to maze interior)*

**[Returns to error selection menu]**

---

### SCENE 2.3B: LOGIC ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/logic_error.rpy

**HARRY:**  
Logic errors are trickier. They don't break your code outright, but they make it behave in ways you didn't intend.

**KENDALL:**  
So, the loop works, but it's doing the wrong thing?

**HARRY:**  
Exactly. Let's say you want to check numbers greater than 5, but you accidentally write it to check numbers greater than 6. It doesn't crash, but it skips the range you wanted to include.

*(Scene transition to code example screen - bg_logic_error_code1)*

**NARRATOR:**  
Harry points to the screen where the incorrect code is displayed.

**KENDALL:**  
That's tricky. It looks fine at first, but the result is wrong. How would I catch something like this?

**HARRY:**  
That's the problem with logic errors—they don't cause crashes. You'd need to test your code carefully and compare the output to what you expect.

*(Scene transition to corrected code screen - bg_logic_error_code2)*

**NARRATOR:**  
Harry shows the corrected version of the code.

**HARRY:**  
Here's the fixed version. Now the loop checks for numbers greater than 5 as intended, so you get the correct result.

**KENDALL:**  
So, the key is testing the code and double-checking the logic carefully, right?

**HARRY:**  
Exactly. With careful testing and attention to detail, you can catch logic errors before they cause trouble.

*(Scene transition back to maze interior)*

**[Returns to error selection menu]**

---

### SCENE 2.3C: OFF-BY-ONE ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/off_by_one_error.rpy

**HARRY:**  
An off-by-one error happens when the loop iterates one time too many or one time too few. It's one of the most common errors in coding.

**KENDALL:**  
So, the loop works, but it doesn't cover all the cases? Like it skips something or stops too early?

**HARRY:**  
Exactly. Let me show you an example where we want to count up to 5, but the loop stops too early.

*(Scene transition to code example screen - bg_off_by_one_code1)*

**NARRATOR:**  
Harry points to the screen where the incorrect code is displayed.

**HARRY:**  
In this code, the condition says 'count < 5', so the loop stops before reaching 5. The 'if' statement inside the loop checks if the number is 5, but it never prints 'True' because 5 isn't included.

**KENDALL:**  
Oh, I see! The loop condition makes it stop before 5, so it misses the chance to print 'True'.

**HARRY:**  
Exactly! Now let me show you how to fix it by updating the loop condition.

*(Scene transition to corrected code screen - bg_off_by_one_code2)*

**NARRATOR:**  
Harry shows the corrected version of the code.

**HARRY:**  
Here's the corrected version. By changing the condition to 'count <= 5', the loop includes 5. Now it prints 'True' when the count reaches 5.

**KENDALL:**  
So, I just need to carefully check the loop conditions to make sure it does what I expect. Got it.

**HARRY:**  
Exactly! Paying attention to loop conditions will help you avoid off-by-one errors and other tricky mistakes.

*(Scene transition back to maze interior)*

**[Returns to error selection menu]**

---

### SCENE 2.3D: PRE-TEST LOGIC ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/pre_test_logic_error.rpy

**HARRY:**  
A pre-test logic error happens when the condition of the loop is false from the very beginning. This means the loop doesn't run at all.

**KENDALL:**  
So, even if the code is written correctly, the loop doesn't run because of the starting condition?

**HARRY:**  
Exactly. Let me show you an example where we set up a loop, but the starting condition makes it skip everything.

*(Scene transition to code example screen - bg_pre_test_logic_error_code1)*

**NARRATOR:**  
Harry points to the screen where the incorrect code is displayed.

**HARRY:**  
In this code, the loop's condition is 'count < 1', but the starting value is 5. Since the condition is false from the start, the loop doesn't run.

**KENDALL:**  
Oh, I see! The loop doesn't even get a chance to start because the condition fails right away.

**HARRY:**  
Exactly! Now let me show you how to fix it by adjusting the starting value and condition.

*(Scene transition to corrected code screen - bg_pre_test_logic_error_code2)*

**NARRATOR:**  
Harry shows the corrected version of the code.

**HARRY:**  
Here's the corrected version. By setting the starting value to 1 and the condition to 'count <= 5', the loop runs as expected and prints the numbers from 1 to 5.

**KENDALL:**  
So, I need to make sure the starting value and condition are aligned to allow the loop to run properly. Got it.

**HARRY:**  
Exactly! Setting the right initial value and condition is key to avoiding pre-test logic errors.

*(Scene transition back to maze interior)*

**[Returns to error selection menu until all 4 errors are completed]**

---

**END OF ACT 2**

*(After completing all four error explanations, the game continues to Act 3 with quizzes)*

