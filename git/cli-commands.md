# Clone and checkout:

- clone and checkout a specific brancg: git clone -b <branch> <remote_repo>
- Cleans the working tree by recursively removing files that are not under version control, starting from the current directory. -> git clean -dfx
  
# Branch: 
  
- Rename branch -> git branch -m new_name
- Move to a new branch with current changes (uncommitted) -> git checkout -b new_name
- List all local branch (* marke the current) -> git branch 
- List all remote branch (* marke the current) -> git branch -r
* Note: git store remote and local branch in separate folders
- Switch and checkout a remote branch -> git switch "branch name (without /origin/"
- Download remote content -> git fetch
  
  # Fix:
  
- Delete the most recent commit (change 1 withe the number of commits to delete), keeping the work you've done: git reset --soft HEAD~1
- Delete the most recent commit, destroying the work you've done: git reset --hard HEAD~1
- - Delete the most recent local commit  git reset HEAD~

