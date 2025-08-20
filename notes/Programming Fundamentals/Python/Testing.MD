# Testing

Created: 26 March 2025 18:44
Class: 3
Is Completed: Yes

## Testing Individual Units of Code

Test-Driven Development (TDD): Write tests before writing the actual code. Code is then written to meet these tests and refined when necessary.

## Python's Assert Statement

- Checks if a given condition is true and raises an error if false. It verifies that variables or preconditions are satisfied.

- Assert statements can include an error message as a second argument.
- Limitations: Can only check simple conditions and stops execution when an assertion fails.
- Python's Unittest
- Offers more features and flexibility than assert statements. Provides a test runner that can execute all tests in one package and report outcomes.

- **Testing your code is essential to ensure its reliability and functionality**. Writing tests helps you catch bugs early, verify that changes don't introduce new issues, and maintain confidence in your code as it evolves.
- **Good tests strike a balance between thoroughness and efficiency**. While comprehensive testing can improve reliability, overly exhaustive tests may slow down development. Focus on testing critical paths and edge cases to achieve effective coverage.
- **Documentation serves as a guide** for others and your future self. Writing clear and detailed documentation explains the purpose, functionality, and usage of your code, making it easier to reuse, maintain, extend, or debug.
- **While documentation is crucial, avoid over-commenting your code**. Overly detailed comments can clutter your codebase, making it harder to read and maintain. Aim for comments that clarify intent or explain non-obvious logic while letting clear code speak for itself.
- **A comment should provide insight into the *why* behind a piece of code**, clarifying the intent, purpose, or reasoning when it is not immediately obvious. It should not simply restate the *what*, as this duplicates the code itself and adds unnecessary clutter. For example, instead of commenting `# Adds 1 to x` for `x += 1`, explain the broader purpose if needed, such as `# Increment counter to track processed items`.
- **Well-documented code increases collaboration** by allowing others to understand your intentions, even if they are unfamiliar with your project. It also reduces the learning curve for onboarding new team members or revisiting your own work after time has passed.
- **Incorporating testing and documentation from the beginning of a project** can streamline development. These practices help prevent frustration later by making your code more robust and accessible from the outset.

What is Code Testing?

Test-Driven Development (TDD) is a simple approach: write tests first, then write code that passes those tests. This helps make sure your code works correctly.

Basic Testing in Python:

1. Assert Statements:

- These are simple checks that make sure something is true
- If the check fails, Python tells you there's an error
- They're basic but helpful for quick tests

1. Unittest:

- This is Python's more powerful testing tool
- It can run many tests at once and tell you what worked and what didn't
- **Testing is important**. It helps you find mistakes early and makes sure your code keeps working when you make changes.
- **Focus on what matters**. Test the most important parts of your code and any tricky situations that might cause problems.
- **Good documentation helps everyone**. Writing clear instructions about how your code works makes it easier for others to use and fix.
- **Keep comments simple**. Don't write too many comments in your code. Only add them when something needs extra explanation.
- **Comments should explain why, not what**. Instead of stating the obvious, explain the reason behind your code. For example, don't write `# Adds 1 to x` - instead, write `# Count how many items we've processed`.
- **Clear documentation helps teamwork**. When your code is well-explained, others can understand and work with it more easily.
- **Start testing and documenting early**. Building these good habits from the beginning makes everything easier later on.
