# password-protected
## Description
In this task we are once again given an image. The task description tells us that we both need to use a secret tool and a password to retrieve the flag. Looking at the image, we can see that an unhidden password can be seen in the login form of the current tab. Furthermore we can see a hint in the other open browser tab. Performing an internet search of the title of the other tab will yield many responses about a tool called steghide.
Using steghide on the image with the password from the login form will yield a text file with the password.

```
KID20{59628a1868c20385dcbffb47ae344109}
```