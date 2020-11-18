# funky-dog-1

## Description:

For this challenge we were given a zip file with a git repository, along with the description:

---

We found a git repository that may contain some sensitive information, can you find it?

---

In the repository we find a README describing that this a repo for learning git and OpenFaaS.
Looking through the master branch on the current commit we do not find any sensitive information.

Since this is a git repo we can use the version control to our advantage.
(Read more about version control and git here: [Git documentation](https://git-scm.com/doc))

```bash
❯ git log

commit 103937765ba4791c9564afc2551fab1b698bebc4 (HEAD -> master)
Author: Billy Port <billy@glass.org>
Date:   Mon Nov 9 20:18:30 2020 +0100

    Add README :)

commit b147b7ede4d81dc33f337304344b4a702a77c914
Author: Billy Port <billy@glass.org>
Date:   Mon Nov 9 20:17:01 2020 +0100

    Add .gitignore and move functions to new folder

commit bd585ae89da6c5479545c9709953a1d1f149f891
Author: Billy Port <billy@glass.org>
Date:   Mon Nov 9 20:14:59 2020 +0100

    Add some new cool functions!

commit be352942da952996c556e3b156f971b234d771c6
Author: Billy Port <billy@glass.org>
Date:   Mon Nov 9 20:10:52 2020 +0100

    Add hello world function! :D
```

The commit with a .gitignore could be worth checking out. Billy could have added a .gitignore to keep himself from pushing sensitive files, but could have forgotten to delete them from previous commits.

```bash
❯ git checkout bd585ae89da6c5479545c9709953a1d1f149f891
Note: switching to 'bd585ae89da6c5479545c9709953a1d1f149f891'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at bd585ae Add some new cool functions!
❯ ls -a
.  ..  build  echo  .git  .gitignore  hello-openfaas  my_functions  .note  stack.yml  Tester
```

That .note file was not there earlier. We can find the flag inside:

```bash
❯ cat .note
If I choose a hard username with my special password, should'nt it be twice as hard hacking me?

Ahhhhhhmmmmmmmmmmm I am always forgetting my new username!

REMEMBER TO DELETE THIS LATER: KID20{w1th_5_l0ng_sp3c14l_u5s3rn4m3_n0b0dy_c5n_h4ck_m3}
```
