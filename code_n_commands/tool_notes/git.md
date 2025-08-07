# Basic def

1.	Branch  
    Repo has diff braches, default is main
    Can make changes in a new branch, commit (save) the change.
    To finalize the change, send a pull request and if it’s approved, branch will be merged into main.
1. (local and remote) Repo
   A remote repository is hosted on a remote (this could be on the internet or an off-site server; it could even be the same machine in a different path) and is ***shared among multiple team members***. A local repository is hosted on a local machine for an ***individual user***.
2.  Diff between git add and git commit: git add is to place the code into the staging area (not overwriting the previous), while commit is to save as permanent snapshot (overwriting the previous)  
3.  Diff between git commit and git push: commit is only done in local repo, but push is to push it on the remote repo
4.  Diff between push and pull: In essence, 'Git Pull' fetches the latest update from the remote repository and adds it to the local repository. 'Git Push' is used to upload the changes made to your local repository into a remote repository
5.  Pull request is to notify other team members to do a pull to update their repo


# How to download branch to local linux, make change and save (CSCI3150 asg as eg)
```bash
(goto the link of ACCEPTING the assignment and click accept)
git clone https://~  # my own repo
(make changes)
git status  
git add --all
git commit -m cmt 
git push  # update all the remote branches that have updated in local tracking branches

(then on github, go to pull request to check the feedback)
(DON’T MERGE PULL REQUEST!)
```

# PAT (Personal Access Tokens)
usually needed when trying to connect to github using in a non web-based manner. Will be a prompt for username and password. Username just the username, password use the PAT token (when using command line, when tell you to input password, always the PAT not the real password).


# config
1. to set your account's default identity:
    ```
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ```
    1. Omit --global to set the identity only in this repository.


1. to remember the password for a time period
    If always being prompted, probably because using a HTTPS protocal

    1. `[NOT RECOMMENDED]` 
    ```
    git config --global credential.helper store # permanent, store the password in file  ~/.git-credentials
    git config --global credential.helper 'cache --timeout=3600'    # for an hour
    ```

    It is stored in the file, then other users (eg root might be able to access your github password)

    2. update to ssh and not use https, set ssh keys, etc

    3. just use the text replacement on local machine to remember the passwords


# Convert existing non-empty directory to Git repository

[link](https://stackoverflow.com/questions/3311774/how-to-convert-existing-non-empty-directory-into-a-git-working-directory-and-pus), answer by Hitesh Sahu