# Basic def

1.	Branch  
    Repo has diff braches, default is main
    Can make changes in a new branch, commit (save) the change.
    To finalize the change, send a pull request and if it’s approved, branch will be merged into main.



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
