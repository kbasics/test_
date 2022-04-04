
C:\Users\krist>cd Desktop
The system cannot find the path specified.

C:\Users\krist>cd desktop
The system cannot find the path specified.

C:\Users\krist>cd
C:\Users\krist

C:\Users\krist>mkdir test_repo

C:\Users\krist>cd test_repo

C:\Users\krist\test_repo>git init
Initialized empty Git repository in C:/Users/krist/test_repo/.git/

C:\Users\krist\test_repo>git commit
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)

C:\Users\krist\test_repo>cd ..

C:\Users\krist>git commit
warning: could not open directory 'Application Data/': Permission denied
warning: could not open directory 'Cookies/': Permission denied
warning: could not open directory 'Local Settings/': Permission denied
warning: could not open directory 'My Documents/': Permission denied
warning: could not open directory 'NetHood/': Permission denied
warning: could not open directory 'PrintHood/': Permission denied
warning: could not open directory 'Recent/': Permission denied
warning: could not open directory 'SendTo/': Permission denied
warning: could not open directory 'Start Menu/': Permission denied
warning: could not open directory 'Templates/': Permission denied
warning: could not open directory 'Application Data/': Permission denied
warning: could not open directory 'Cookies/': Permission denied
warning: could not open directory 'Local Settings/': Permission denied
warning: could not open directory 'My Documents/': Permission denied
warning: could not open directory 'NetHood/': Permission denied
warning: could not open directory 'PrintHood/': Permission denied
warning: could not open directory 'Recent/': Permission denied
warning: could not open directory 'SendTo/': Permission denied
warning: could not open directory 'Start Menu/': Permission denied
warning: could not open directory 'Templates/': Permission denied
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .VirtualBox/
        .bash_history
        .config/
        .dotnet/
        .eclipse/
        .gitconfig
        .lesshst
        .nuget/
        .p2/
        .packettracer
        .tooling/
        .vscode/
        3D Objects/
        AppData/
        BullseyeCoverageError.txt
        Cisco Packet Tracer 8.0/
        Contacts/
        Documents/
        Downloads/
        Favorites/
        Links/
        MicrosoftEdgeBackups/
        Music/
        NTUSER.DAT
        NTUSER.DAT{927fc02d-0d6f-11eb-9db1-ace0c0edb5e2}.TM.blf
        NTUSER.DAT{927fc02d-0d6f-11eb-9db1-ace0c0edb5e2}.TMContainer00000000000000000001.regtrans-ms
        NTUSER.DAT{927fc02d-0d6f-11eb-9db1-ace0c0edb5e2}.TMContainer00000000000000000002.regtrans-ms
        OneDrive/
        Saved Games/
        Searches/
        Tracing/
        Videos/
        VirtualBox VMs/
        eclipse-workspace/
        eclipse/
        gitv/
        ntuser.dat.LOG1
        ntuser.dat.LOG2
        ntuser.ini
        test_repo/

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\krist>cd test_repo

C:\Users\krist\test_repo>git add readme.md

C:\Users\krist\test_repo>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


C:\Users\krist\test_repo>git commit -m "added readme.md"
[master (root-commit) afc38e5] added readme.md
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 readme.md

C:\Users\krist\test_repo>git status
On branch master
nothing to commit, working tree clean

C:\Users\krist\test_repo>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\krist\test_repo>git add .

C:\Users\krist\test_repo>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   readme.md


C:\Users\krist\test_repo>git commit -m "made changes"
[master e059bb6] made changes
 1 file changed, 3 insertions(+)

C:\Users\krist\test_repo>git checkout -b
error: switch `b' requires a value

C:\Users\krist\test_repo>git checkout -b new
Switched to a new branch 'new'

C:\Users\krist\test_repo>git add .

C:\Users\krist\test_repo>git commit -m "first commit"
[new 599803d] first commit
 1 file changed, 3 insertions(+), 1 deletion(-)

C:\Users\krist\test_repo>git checkout master
Switched to branch 'master'

C:\Users\krist\test_repo>git add .

C:\Users\krist\test_repo>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test.py


C:\Users\krist\test_repo>git commit -m "added test.py"
[master 247435e] added test.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.py

C:\Users\krist\test_repo>git checkout new
Switched to branch 'new'

C:\Users\krist\test_repo>git merge master
Merge made by the 'ort' strategy.
 test.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.py

C:\Users\krist\test_repo>git checkout master
Switched to branch 'master'
M       test.py

C:\Users\krist\test_repo>git remote add origin https://github.com/kbasics/test_.git

C:\Users\krist\test_repo>git checkout master
Already on 'master'
M       test.py

C:\Users\krist\test_repo>git push -u origin master
info: please complete authentication in your browser...
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 677 bytes | 135.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/kbasics/test_.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.

C:\Users\krist\test_repo>git config --global user.name "Kristina BS"

C:\Users\krist\test_repo>git config --global user.email "kristina.basic.sisko@aspira.hr"

C:\Users\krist\test_repo>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\krist\test_repo>git branch branch2

C:\Users\krist\test_repo>git branch checkout

C:\Users\krist\test_repo>echo "" > test.txt;

C:\Users\krist\test_repo>git add .

C:\Users\krist\test_repo>git commit -m "tekst komit"
[master 89d19ad] tekst komit
 2 files changed, 2 insertions(+)
 create mode 100644 test.txt

C:\Users\krist\test_repo>git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 339 bytes | 113.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/kbasics/test_.git
   247435e..89d19ad  master -> master

C:\Users\krist\test_repo>git push -u origin branch2
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'branch2' on GitHub by visiting:
remote:      https://github.com/kbasics/test_/pull/new/branch2
remote:
To https://github.com/kbasics/test_.git
 * [new branch]      branch2 -> branch2
branch 'branch2' set up to track 'origin/branch2'.

C:\Users\krist\test_repo>git checkout master
Already on 'master'
Your branch is up to date with 'origin/master'.

C:\Users\krist\test_repo>git merge branch2
Already up to date.

C:\Users\krist\test_repo>git merge grana2
merge: grana2 - not something we can merge

C:\Users\krist\test_repo>git branch -d branch2
Deleted branch branch2 (was 247435e).

C:\Users\krist\test_repo>git pull
Already up to date.

C:\Users\krist\test_repo>