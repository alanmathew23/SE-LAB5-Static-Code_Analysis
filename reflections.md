# Reflections

## Which issues were the easiest to fix, and which were the hardest? Why?

The easiest fixes were style issues like adding docstrings, renaming functions to snake_case, converting to f-strings, and removing the unused import. These were basically copy-paste and formatting changes that took just a few minutes.

The hardest issue was the mutable default argument (`logs=[]`). I didn't initially understand why it was problematic until I learned that Python creates the default list once, so all function calls share the same object. The fix required changing to `logs=None` and initializing inside the function. Removing `eval()` was also tricky since I had to understand what it did and determine it wasn't actually needed.

## Did the static analysis tools report any false positives? If so, describe one example.

No real false positives. All the warnings were legitimate - bare except was dangerous, eval() was a security risk, and the mutable default would cause bugs. The global statement warning might be debatable since sometimes globals are necessary, but avoiding them is still better design practice.

## How would you integrate static analysis tools into your actual software development workflow?

For local development, I'd set up pre-commit hooks to run Pylint and Flake8 before commits, catching issues immediately. I'd also configure my IDE to show real-time linting warnings while coding.

For CI/CD, I'd use GitHub Actions to automatically run all three tools on pull requests. Critical issues from Bandit or major Pylint errors would block merging until fixed, ensuring bad code never reaches main. I'd also generate reports and store them as artifacts to track code quality trends over time.

## What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Security and robustness improved dramatically. Removing `eval()` eliminated a major vulnerability, and fixing bare except prevents silent error swallowing that would make debugging impossible.

Readability got way better with f-strings, docstrings, and snake_case naming. Anyone can now understand what each function does without reading the implementation.

The `with` statements ensure files close properly even during errors, preventing resource leaks. Fixing the mutable default prevents bugs where logs from different calls would incorrectly share the same list. Overall, the code went from sketchy to production-ready.