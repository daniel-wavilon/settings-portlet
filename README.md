Specification of JSON objects for Wavilon

## Set up git to use this repository

_Setup your ssh key_

Account Settings -> SSH Public Key -> Add public key

Title: anything you want
Key: the full content of your ~/.ssh/id_rsa.pub

_Make sure you can log in to github_

ssh -T git@github.com
Hi <user>! You've successfully authenticated, but GitHub does not provide shell access.

_Fork this repository_

This repo gives you only pull access. To make changes, you need to fork this repo and work with your private copy.

_Clone this repository locally_

git clone git@github.com:<your user>/settings-portlet.git

_Create a remote branch, and track it locally_

* git push origin origin:refs/heads/<branch_name>
* git checkout -b <branch_name> origin/<branch_name>

_Make changes, and push them when you are ready_

* Edit some files, until you are ready.
* Check the status of your repository: git status
* Stage the files that you want to commit: git add <files>
* Commit your changes locally: git commit -m "Your message"
* Check your log: git log
* Push your changes: git push

