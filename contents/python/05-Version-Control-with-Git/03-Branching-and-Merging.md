# Lesson 3: Branching and Merging

Branching is one of Git's most powerful features. A **branch** is like an independent line of development. It allows you to work on a new feature or experiment with an idea without affecting the main, stable version of your project.

### The `main` Branch

By default, your repository has one branch named `main` (or sometimes `master`). This is typically considered the official, stable version of your project.

### Why Branch?

Imagine you want to add a new feature, like a "dark mode" for a website.
- You create a new branch called `dark-mode`.
- You do all your work on this branch. The `main` branch is untouched and remains stable.
- If you make a mistake, you can just delete the `dark-mode` branch without any harm to the main project.
- Once you're happy with the new feature, you **merge** the `dark-mode` branch back into the `main` branch.

This workflow is essential for collaboration. Each developer can work on their own feature in a separate branch, and then the team can merge those features into the main project when they are ready.

---

### The Workflow

#### 1. `git branch` - List Branches

This command lists all the branches in your repository. The current branch will be marked with an asterisk (`*`).

```bash
# List all branches
git branch
```

#### 2. `git branch <branch-name>` - Create a Branch

This command creates a new branch.

```bash
# Create a new branch called 'new-feature'
git branch new-feature
```

#### 3. `git checkout <branch-name>` - Switch Branches

This command switches your working directory to the specified branch.

```bash
# Switch to the 'new-feature' branch
git checkout new-feature

# You can also create and switch to a new branch in one command
git checkout -b another-new-feature
```

Now, any commits you make will be on this new branch.

#### 4. `git merge <branch-name>` - Merge Branches

Once you've finished your work on a feature branch, you'll want to merge it back into your `main` branch.

First, switch back to the branch you want to merge into (usually `main`).

```bash
# Switch back to the main branch
git checkout main
```

Then, use `git merge` to bring the changes from the feature branch into `main`.

```bash
# Merge the 'new-feature' branch into the current branch (main)
git merge new-feature
```

Git will try to automatically combine the changes. If there are conflicting changes (e.g., you and another person edited the same line of a file), Git will pause and ask you to resolve the **merge conflict**.

---

In the next lesson, we'll look at how to use Git to collaborate with others using remote repositories on websites like GitHub.
