## Section 9: Database migrations with Alembic and Flask-Migrate

#### Table of Contents
- What are Git repositories and commits?
- Initialize a Git repository for our project
- Writing Markdown for documents and commits
- Remote repositories and how to use them
- Git branches and merging
- Merge conflicts and how to resolve them


### What are Git repositories and commits?
- Working area: Files in your project, before Git knows anything about them
- Staging area: Files to include in the next commit
- Committed: Files that Git is tracking because they are part of a past commit
- Remote: Commits that have been uploaded to a cloud repository (called a remote)

A Git commit is a snapshot of tracked files from a repository.

```
git add myfile.py
git commit
git push
```

`git checkout -- myfile.py` erases any changes to the file, so it looks as it did on the last commit that included this file.

`git reset HEAD myfile.py` keeps the file changes in your working area.

`git reset COMMIT_ID` tells git to get rid of a commit and deletes it.

`git revert COMMIT_ID` creates a new commit with the opposite changes of another commit.

If you revert a commit, you can revert the revert later. It's safer to revert than to reset.
Also, if you share your repository with others (via a remote), then resetting can cause problems.


### Initialize a Git repository for our project
```
git init
git status
git add .
git checkout -- app.py
git status
git restore app.py
git add app.py
git status
git reset HEAD app.py
git commit -am 'added new line in imports'
```

### Writing Markdown for documents and commits

### Remote repositories and how to use them
```
git status
git remote add origin https://github.com/<your_github_repository>
git push --set-upstream origin main
```

### Git branches and merging
#### What are branches?
A name for a commit
- New repositories usually start with a branch called "main" or "master"
- This name is created when you make your first commit, and is attached to it
- When you have a branch active and you make a new commit, the name moves to it

C1 <-- C2 <-- C3 (HEAD, main*)

HEAD is similar to a branch. It is the currently active commit.

C1 <-- C2 (HEAD) <-- C3 (main*)

"Checking out" a commit changes your working area to match what it was at that commit.
So any changes added by C3 are eliminated. You can later `git checkout main` to got back
to the main branch.

#### How to create new branches
- When you create a new branch, the name is assigned to the current commit
- Assume we've ran `git checkout main` first, otherwise `new_branch` would be C2

C1 <-- C2 <-- C3 (HEAD, new_branch*, main)

#### Merging branches
Let's say you've been working in `new_branch`. Someone else made commits in "main". What do you do?
```
C1 <-- C2 <-- C3 <-- C5 <-- C6 (main)
         \
          \-- C4 <-- C7 <-- C8 (HEAD, new_branch*)
```

```
git checkout main
git merge new_branch
```

What if both people changed the same lines in the same file? Then you get a **merge conflict**.

### Merge conflicts and how to resolve them
Keep theirs
Keep ours



