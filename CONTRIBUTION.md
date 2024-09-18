
# Contributing to Python MySQL API

Thank you for your interest in contributing to our MySQL API for Python! We believe in creating a learning space for everyone and are excited for you to join us in making this small project impactful during this semester. Let's grow and learn together!

## Getting Started

### Prerequisites
- Python 3.10 or later is required.
- We use `unittest` for testing.
- The main dependency is `mysql-connector-python`, so ensure you have it installed:
  ```bash
  pip install mysql-connector-python
  ```

### Setting Up the Development Environment
1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/Boaz-Maroko/pythonmysqlapi.git
   ```
2. Navigate into the project directory:
   ```bash
   cd pythonmysqlapi
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests to ensure everything is set up properly:
   ```bash
   python -m unittest discover
   ```

### Code Guidelines

- The functionality should be expressed primarily using **classes**. Functions are allowed, but only when necessary and appropriate.
- Ensure all code follows [PEP 8](https://pep8.org/) style guidelines. Use a linter to check before submitting.
- Each new feature or change should be accompanied by a corresponding test within the `unittest` framework.

### Branching and Commit Messages

#### Branch structure:
- **Feature branch**: Development starts in the features branch, where new ideas are first implemented.
- **Development branch**: Once a feature or idea is stable and functional in the feature branch, it is moved to the development branch, where it is refined and ironed out.
- **Main branch**: The main branch is reserved for production-ready code only.

- **Branch naming**: Use descriptive names for your branches:
   ```markdown
   feature/add-new-endpoint
   fix/correct-sql-bug
   ```
- **Commit messages**: Use the following format:
   ```markdown
   [type]: [subject]
   
   Example:
   feat: add user authentication
   fix: correct SQL query on User model
   ```

### Submitting a Pull Request

1. Fork and clone the repository.
2. Create a new branch for your feature or bug fix.
3. Run the tests:
   ```bash
   python -m unittest
   ```
4. Open a pull request and describe your changes.

Thank you for contributing!



# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others’ private information, such as a physical or email address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies to all community spaces, including public repositories, issues, and pull requests, as well as private communication directly related to the project.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project team at [INSERT EMAIL]. All complaints will be reviewed and investigated promptly and fairly.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions.
