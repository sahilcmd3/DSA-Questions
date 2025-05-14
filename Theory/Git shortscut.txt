Absolutely! Here are some essential Git commands that will boost your workflow:

### Basic Git Commands
- `git init` → Initializes a new Git repository.
- `git clone <repo-url>` → Clones a remote repository to your local machine.
- `git status` → Shows the current state of your working directory.
- `git add <file>` → Stages a specific file for commit.
- `git add .` → Stages all changes in the working directory.
- `git commit -m "message"` → Commits staged changes with a message.
- `git push origin <branch>` → Pushes changes to the remote repository.

### Branch Management
- `git branch` → Lists all branches.
- `git branch <new-branch>` → Creates a new branch.
- `git checkout <branch>` → Switches to a different branch.
- `git merge <branch>` → Merges another branch into the current branch.
- `git rebase <branch>` → Reapplies commits from one branch onto another.

### Undo & Reset
- `git reset --hard <commit>` → Resets to a specific commit, discarding changes.
- `git reset --soft <commit>` → Resets to a commit but keeps changes staged.
- `git revert <commit>` → Creates a new commit that undoes a previous commit.
- `git stash` → Temporarily saves uncommitted changes.
- `git stash pop` → Restores stashed changes.

### Collaboration & Remote Repositories
- `git remote -v` → Lists remote repositories.
- `git fetch origin` → Fetches changes from the remote repository.
- `git pull origin <branch>` → Pulls changes from the remote branch.
- `git push -u origin <branch>` → Sets upstream tracking for a branch.

### Advanced Commands
- `git log` → Shows commit history.
- `git diff` → Displays differences between commits.
- `git cherry-pick <commit>` → Applies a specific commit from another branch.
- `git bisect` → Helps find a bug by binary searching through commits.

You can find a detailed cheat sheet [here](https://www.freecodecamp.org/news/git-cheat-sheet/).