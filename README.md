# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

  **Glitchy Guesser** is a number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls both the number range and how many guesses the player gets. Each wrong guess deducts points from your score, and guessing correctly awards bonus points based on how quickly you solved it.

- [x] Detail which bugs you found.

  1. **Secret number kept resetting** — every time Submit was clicked, Streamlit re-ran the script and generated a new secret number, making it impossible to win.
  2. **Attempts counter not initialized** — `st.session_state.attempts` was never set to `0` on game start, causing a `KeyError` crash.
  3. **Attempts incremented on invalid input** — the counter went up even when a non-number was entered, wasting the player's guesses.
  4. **New Game didn't fully reset** — clicking New Game only re-rolled the secret; it didn't reset `history`, `score`, or `status`, leaving the game in a broken state.
  5. **Secret range was hardcoded to 100** — the New Game button always generated a number between 1–100 regardless of difficulty, ignoring the `low`/`high` range variables.
  6. **Difficulty ranges were inverted** — Easy had the smallest range (1–10) and Hard had the largest (1–100), which was backwards.
  7. **`parse_guess()` return was unreachable** — the `return` statement was placed outside the `try` block, so a valid guess would fall through and return `None` instead of the parsed integer.
  8. **Info banner showed stale attempt count** — the banner rendered before the submit logic ran, so it always showed the count from the previous guess.

- [x] Explain what fixes you applied.

  1. Wrapped `secret` in `st.session_state` with an `if "secret" not in st.session_state` guard so it only generates once per game session.
  2. Added `st.session_state.attempts = 0` initialization alongside the other session state defaults.
  3. Moved `st.session_state.attempts += 1` inside the `if ok:` branch so only valid guesses count.
  4. Updated the New Game button handler to also reset `history`, `score`, and `status` back to their starting values.
  5. Changed the New Game secret generation from `random.randint(0, 100)` to `random.randint(low, high)` to respect the selected difficulty.
  6. Corrected difficulty ranges in `get_range_for_difficulty()`: Easy → 1–100, Normal → 1–50, Hard → 1–20.
  7. Moved the `return True, value, None` statement inside the `try` block in `parse_guess()` so valid integers are actually returned.
  8. Moved the info banner to an `st.empty()` placeholder rendered before the submit logic, then written to after processing so it reflects the updated attempt count immediately.

## 📸 Demo

![Screenshot of fixed winning game](Screenshot%202026-03-15%20at%2010.42.08%20PM.png)
<!-- (Screenshot 2026-03-15 at 10.42.08 PM.png) -->

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
