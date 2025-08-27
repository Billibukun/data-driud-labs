# Lesson 2: Git Basics - The Core Workflow

Let's learn the fundamental commands you'll use every time you work with Git. These commands allow you to track changes to your project.

**Note:** These commands are run in your computer's **terminal** or **command line**, not in a Python notebook.

### The Three Areas

Git has three main areas where your files can live:
1.  **Working Directory:** The folder on your computer where your project files are.
2.  **Staging Area (or Index):** A "waiting room" where you place the specific changes you want to save.
3.  **Repository (.git directory):** The "time machine" itself. This is where Git permanently stores the history of your project as snapshots called **commits**.

---

### The Workflow

Here is the most common workflow you'll use:

#### 1. `git init` - Initialize a Repository

This is the very first command you run in a new project. It creates the hidden `.git` directory, turning your project folder into a Git repository. You only need to run this **once** per project.

```bash
# Navigate to your project folder in the terminal
cd my-project

# Initialize the repository
git init
```

#### 2. `git status` - Check the Status

This is your most-used Git command. It tells you the current state of your repository:
- Which files are new (untracked)?
- Which files have been modified?
- Which files are in the staging area, ready to be saved?

```bash
# See the status of your project
git status
```

#### 3. `git add` - Stage Your Changes

When you've made changes to a file (or created a new one) and you're ready to save it, you first add it to the staging area.

```bash
# Stage a single file
git add filename.py

# Stage all changes in the current directory
git add .
```

Staging is useful because it allows you to be selective. You can choose to save only some of your changes in one commit, making your project history clean and organized.

#### 4. `git commit` - Save Your Changes

A **commit** is a permanent snapshot of your staged changes. Each commit has a unique ID and a descriptive message explaining what you changed.

Writing good commit messages is a very important skill. A standard format is a short subject line (e.g., "Add user login feature"), followed by a blank line and a more detailed description if needed.

```bash
# Create a commit with a message
git commit -m "Add a new function to calculate area"
```

#### 5. `git log` - View the History

This command shows you the history of all the commits in your project, starting with the most recent.

```bash
# See the commit history
git log
```

---

### Summary

The basic workflow is:
1.  Make changes to your files.
2.  Use `git add` to stage the changes you want to save.
3.  Use `git commit` to permanently save the staged changes to your repository's history.
4.  Repeat!

In the next lesson, we'll learn about **branching**, which allows you to work on different features or experiments in isolation.
