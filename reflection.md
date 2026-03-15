# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The first time I ran the game it loaded in Streamlit and looked mostly normal, but when I started playing it became clear that several things were not working correctly. The higher/lower hints were wrong, because sometimes the game told me to go higher even though my guess was already too high. The difficulty settings were also strange because the Normal difficulty had a bigger range than Hard, which made it feel harder than it should be. I also noticed that starting a new game did not fully reset the game state. The secret number seemed to reset incorrectly and the range did not always match the selected difficulty.

---

## 2. How did you use AI as a teammate?

For this project I used GitHub Copilot and ChatGPT to help review and understand the code. One helpful suggestion from AI was moving the game logic functions out of `app.py` and into `logic_utils.py`. This made the code easier to read and separated the UI from the core logic. I verified that this change worked by running the game again and also running `pytest` to make sure the tests still passed.

One misleading suggestion from the original AI-generated code was converting the secret number into a string during certain turns. This caused incorrect comparisons between the guess and the secret number. I realized this was a problem after reading through the code carefully and removed the string conversion so the secret number always stays an integer.

---

## 3. Debugging and testing your fixes

To decide whether a bug was fixed, I tested the game manually and also used automated tests. After making changes, I ran the game with Streamlit and played several rounds to see if the hints and scoring worked correctly. I also ran `pytest` to make sure the logic functions behaved as expected.

One test I ran checked that when a guess is higher than the secret number, the game correctly returns the "Too High" result and tells the player to go lower. This confirmed that the hint logic was working properly after I fixed it. AI also helped suggest some example test cases, which helped me understand how to verify the functions more clearly.

---

## 4. What did you learn about Streamlit and state?

The secret number originally kept changing because Streamlit reruns the entire script every time the user interacts with the page. Without storing the value in session state, the game would generate a new secret number each time the page refreshed. That made it impossible to play the game correctly.

Streamlit session state allows the app to remember variables between reruns. By saving the secret number inside `st.session_state.secret`, the game keeps the same number between guesses. The key change that fixed the issue was making sure the secret number was only created once and stored in session state instead of being recreated during each interaction.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing small tests while debugging. Using `pytest` helped confirm that the functions worked correctly and made it easier to verify fixes. I also found it useful to isolate logic into separate files instead of mixing everything in one large script.

Next time I work with AI on a coding task, I will be more careful about reviewing the generated code instead of assuming it is correct. This project showed me that AI-generated code can look reasonable but still contain logic errors. Overall, it changed the way I think about AI code generation because it showed me that developers still need to carefully review and test everything.

