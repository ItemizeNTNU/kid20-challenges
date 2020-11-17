# guessy-as-fork:
## Description:
For this challenge we were only given an URL to a web-app, along with the description:

---

You can go buser your way all you want, but you'll never find my secret! Even if you try 10,000 times to guess your way in, you'll never find it!

_I swear, totally not guessy chall..._

[http://129.241.209.70:57284](http://129.241.209.70:57284)

---

When trying to access the website, we only get a 200 HTTP OK response with the text 
```
Hi there, nothing special at this place. Maybe try somewhere else?
```

From the description, it hints about trying several times, finding a secret, and even `go buster`. A quick search shows that `gobuster` is a popular tool for doing bruteforce lookup of URLs. It works by giving it a base URL, e.g. `http://129.241.209.70:57284/` and then providing a wordlist for paths to append, and it will work it's way through. It does also say something that it is really hard to try, and that we can try 10,000 times without finding it. We can then try maybe using a wordlist with over 10,000 entries and see if we find anything?

Here I'm using [dirsearch](https://github.com/maurosoria/dirsearch) which is similar to [gobuster](https://tools.kali.org/web-applications/gobuster), just my personal preference, as it has some nice defaults.

We see that I specify the URL with the `-u` flag, and just the default wordlist along with the default extensions provide a wordlist with over 10,000 entries. You could also have tried a wordlist from [SecLists web-content discovery](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content).

We do ho

```
$ dirsearch -u "http://129.241.209.70:57284/"

  _|. _ _  _  _  _ _|_    v0.4.0
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm, js | HTTP method: GET | Threads: 20 | Wordlist size: 10023

Target: http://129.241.209.70:57284/

[13:02:43] Starting: 
[13:03:00] 302 -   34B  - /login/cpanel.js  ->  /waf/error/speeding                                                                     
[13:03:00] 302 -   34B  - /login/cpanel/  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login/super  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login/index  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login/cpanel.html  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login/login  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.php  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.js  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.html  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login/oauth/  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login1  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin/  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.jsp  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.aspx  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.asp  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admin.htm  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login1/  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_db/  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_admi  ->  /waf/error/speeding
[13:03:00] 302 -   34B  - /login_ou.php  ->  /waf/error/speeding
...
```
We do however see that quite quickly, we get _alot_ of 302 redirects, all pointing to `/waf/error/speeding`. Trying to access the URL we get presented with the image:

![/waf/error/speeding](speeding.jpg)

The URL also says error speeding, indicating that some sort of filter kicked in when we sent too many requests to the web server, triggering the WAF, or [Web Application Firewall](https://en.wikipedia.org/wiki/Web_application_firewall).

If we wait too long, we also see that the image disapears and we get a `404 Not Found` message.

From this we can see that if we send 10,000 requests a WAF kicks in and redirects all our next requests over to `/waf/error/speeding`, and that after a little while, it clears up again, 1 minute later to be exact. It seems that if you send more than 10,000 requests per 60 seconds, then you get blocked.

This should be quite trivial to trigger, as a decent connection should be able to send 10,000 to the web server over a couple of seconds (tested with a server having 160 ms ping from the US to the web server at NTNU Trondheim).

So we can just keep triggering the WAF and see if we find anything more.

We can try accessing `/waf/error` and get presented with:
```
Unknown error, use one of the following: speeding
```
Remember to access these URLs _while your bruteforce tool is running, as the WAF only triggers when we send more than 10,000 requests per 60 seconds_.

Going another step up to `/waf/` we get:
```
Unknown action, use one of the following: error, statistics
```

We see there is another endpoint, `/waf/statistics`, so lets try that one:
```
Unknown statistic, use one of the following: access
```
Then we try `/waf/statistics/access` and get a huge list of entries on the form:
```json
{
  "*": 404,
  "/": 404,
  "/!": 404,
  "/!.gitignore": 404,
  "/!.htaccess": 404,
  "/!.htpasswd": 404,
  "/!_archives": 404,
  "/!_images": 404,
  "/!backup": 404,
  ...
```
It seems these are URLs that have been accessed on the web server and the response code from the server, in this case 404. It seems all of them are 404, which makes sence since people have been running wordlists that just give 404 responses from the server. We can try to search for a 200 response in the list, e.g. from the command line:

```
$ cat access.json | jq . | grep ": 200,"
  "/e73470324687126d04a9386831482ff7/flag.txt": 200,
```

Here we find a path `/e73470324687126d04a9386831482ff7/flag.txt` which returns 200 OK. Let us try this on the while the bruteforce tool is not running, so that we don't just get redirected to `/waf/errors/speeding`:

`/e73470324687126d04a9386831482ff7/flag.txt`:
```
KID20{tOlD_Y0u_n0t_6U3zzy}
```
