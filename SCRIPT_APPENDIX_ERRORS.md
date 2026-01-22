# LOOPS - Error Explanations (Appendix)

## APPENDIX A: ERROR EXPLANATIONS (NON-CHRONOLOGICAL)

**NOTE TO PROFESSOR:** These error explanations are NOT part of the chronological narrative flow. During Scene 2.3 of Act 2, the player can choose to learn about these errors in ANY order they prefer. Each error has its own complete explanation scene with code examples.

**Player Choice Menu Appears After Scene 2.2 (Inside the Maze)**

---

## ERROR 1: INFINITE LOOP ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/infinite_loop_error.rpy

---

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

## ERROR 2: LOGIC ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/logic_error.rpy

---

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

## ERROR 3: OFF-BY-ONE ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/off_by_one_error.rpy

---

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

## ERROR 4: PRE-TEST LOGIC ERROR
**Location:** Maze Interior  
**Characters:** Harry, Kendall, Narrator  
**Source File:** Story/Errors/pre_test_logic_error.rpy

---

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

**[Returns to error selection menu]**

---

**END OF ERROR EXPLANATIONS**

**NOTE:** After the player has gone through all 4 error explanations, the game automatically proceeds to Scene 2.4 (Quiz Time).
