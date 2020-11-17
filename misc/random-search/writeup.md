# random-search
## Description:
For this challenge, you were presented with connecting to a service over netcat, and also got the source-code for the `app.py`. We can see that to get the flag we need to locate the index of a randomly chosen element from a list of randomly generated numbers. We can see that the list is always 500 elements big and we also get 9 tries to lookup any element by index in the list we want before we need to provide an answer. The key take-away from the way the list is generated is that it is *ascending*, meaning the list is sorted and all elements gets bigger further in the list.

We can then do a binary-search looking for the value provided. Doing this 10 times unlocks the flag.

A possible solution script has been provided in `solve.py`.