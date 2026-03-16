# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  1. I guessed the correct answer the first time I ran the game, and it correctly congratulates me for getting it right. However, when I clicked "New Game", the attempts counter and the history didn't reset.
  2. Inconsistent attempts counter variables across panels (Debug Panel, Difficulty Side Panel, and the Info banner).
  3. The ranges for each difficulty didn't seem right. The "Easy" should have a smaller range to guess from and the range should increase as the difficulty gets harder.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. The hints are backwards. If the number I guessed was greater than the secret number, the hint would incorrectly suggest to guess higher, for example.

  2. Starting a new game should reset the history or the attempt counter to an empty list or 0, respectively. Instead, it seems the state of the last game persists and I am unable to play the game since I ran out of attempts.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude to help me quickly identify where the main logic for the buggy functionality lie.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I prompted Claude to identify the initialization and assignments of st.session_state. Claude returned a table that mapped each occurrence of st.session_state with a line number and explanation of the code. I was able to quickly locate how variables like "Attempts" and "History" were being initialized when the game starts. Additionally, I was able to quickly get familiar with the way these variables were accessed, which made it easier to make changes to these variables when a user starts a new game, for example.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - In order to fix the history bug, Claude suggested to place st.rerun() at the end of the code. When I ran the game and tested it out, I noticed the history was getting updated accordingly but the hints were no longer visible. This led to the discovery that rerunning the game after a user hits submit doesn't update the history in the best way. It skips the code that comes after writing to the debug panel (that displays the hint) in order for the user to see their updated history. Instead, I used a container to keep the panel at its original position with default starter values and updated the default variables when a user submits a guess. This approach allows for the rest of the code to run (displaying the hint based on the user's guess) and updates the user's guess history, improving the responsiveness and user experience of the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had the game running in an adjacent window and refreshed the browser every time I wanted to verify the correctness of any recent changes I made.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
For example, when I changed the ranges of guessing values based on difficulty, I manually refreshed the page to make sure that the text on the page corresponded to the changes I made in the code.
- Did AI help you design or understand any tests? How?
Yes, AI helped me write the tests we ran to verify the correctness of the history bugs I fixed.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  Every time a user interacted with the app (clicking Submit, for example), Streamlit re-ran the entire script from top to bottom. Because the secret number was generated with `random.randint()` at the top level with no guard, it got a brand new value on every rerun.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit is like a whiteboard that gets fully erased and redrawn every time someone clicks a button. By default, nothing is remembered between redraws. `st.session_state` functions like a sticky note that you can attach to the whiteboard — it saves values beyond the erase-and-redraw cycle, so important values like the secret number or attempt count stay put.

- What change did you make that finally gave the game a stable secret number?
  I wrapped the secret number generation in an `if "secret" not in st.session_state:` check. This means the number is only generated once — the very first time the app loads — and every subsequent rerun reads the already-stored value instead of creating a new one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I would like to have a system of live testing where I can quickly verify whether changes I make are functional or not. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would like to make more frequent uploads to GitHub / version control hubs in case I want to revert any AI changes.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It fortified my understanding of the importance of revising AI generated code before insertion. There were many occasions where I had to make small tweaks in AI generated code for it to fully function within the existing project code.
