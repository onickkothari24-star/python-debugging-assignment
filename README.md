# Question 3: Debugging Practice

This is a practice script created because no teacher-provided buggy script was available.

## Files

- `buggy_script.py` — intentionally contains three bugs.
- `test_buggy_script.py` — unit tests that help reveal the bugs.
- `README.md` — instructions.

## Open in Cursor

1. Extract the ZIP file.
2. Open Cursor.
3. Select **File → Open Folder**.
4. Choose the extracted `Question_3_Buggy_Script` folder.
5. Open `buggy_script.py` to inspect the code.
6. Open `test_buggy_script.py` to inspect the tests.

## Run the tests

Open Cursor's terminal (**Terminal → New Terminal**) and run:

```bash
python -m unittest -v
```

The tests are expected to fail before you fix the bugs. Your task is to identify and fix the three intentional bugs in `buggy_script.py` so the tests pass.

## Hint

- Check the average calculation, including a list with one number.
- Check how the largest value is initialized.
- Check the condition used to count even numbers.

Try to solve it yourself first. You can ask Cursor Chat for one hint at a time rather than asking it to rewrite the entire script.
