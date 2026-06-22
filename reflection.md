# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like a decently created game. It had decent visuals and had a text field for entering guesses and a button for submitting guesses. It had a response field after every guess

- List at least two concrete bugs you noticed at the start
The "New Game" button doesn't work
The guess response field doesn't work as intended
The final score was a negative number

  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input        | Expected Behavior   | Actual Behavior                 | Console Output / Error                                |
|--------------|---------------------|---------------------------------|----------------------------------------------------|
| Guess of 25  | Go higher           | Go lower                        | No error text. Actual answer was 51                |
| Guess of 500 | Go lower            | Go higher                       | No error text. Actual answer was 100               |
| Guess of "3d"| That is not a number| Bypass the limit on tries       | The number of tries remaining was a negative number|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I'm currently using Claude for this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Re-ran the app and tested it with the same input that raised the bug/error

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
