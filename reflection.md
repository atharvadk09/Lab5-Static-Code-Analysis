
## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were formatting problems, naming conventions, and the mutable default argument. These required small changes, such as adding proper spacing, correcting indentation, and following Python's snake_case naming convention.

The hardest issues were security-related problems, such as hardcoded credentials, weak PIN hashing, and insecure temporary-file creation. These required more careful changes because I needed to improve security while ensuring that the wallet program continued to work correctly.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

I did not identify any definite false positives in the reports. Pylint reported code-quality issues, while Flake8 identified formatting problems. Bandit initially helped me examine potential security risks, and after fixing the issues, the final scan reported no issues identified.

This experience taught me to examine each warning and understand its cause before deciding how to fix it.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would use Pylint, Bandit, and Flake8 regularly while developing Python applications. I would run Pylint to evaluate code quality, Bandit to check for potential security vulnerabilities, and Flake8 to identify style and formatting problems.

I would run these tools before committing code to Git and integrate them into a CI/CD pipeline. This would help detect problems early, maintain coding standards, and reduce the chance of introducing avoidable errors into the application.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code became more readable and consistent after fixing naming and formatting issues. Replacing the mutable default argument helped prevent unexpected sharing of list data between function calls. Improving PIN hashing and temporary-file creation also strengthened the security of the demonstration.

The final Pylint score improved from 5.69/10 to 10.00/10. Bandit reported no issues identified, and Flake8 produced no output, indicating that it found no remaining style violations. The program also continued to produce the expected final balance of Rs. 1900.0, total credited amount of Rs. 2500, and cashback of Rs. 8.40. These results demonstrated that the code quality improved while the wallet demonstration continued to work as expected.