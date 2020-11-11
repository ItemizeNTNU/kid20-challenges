author: bashgobrr
flag: KID20{4ll_my_c0d3_i5_fr0m_s74ck0v3rfl0w}

--

We found the ip address Billy is using for his openfaas functions from the git repo.
It seems he made a new function called secret-vault:

[http://129.241.209.104:8080/function/secret-vault](http://129.241.209.104:8080/function/secret-vault)

Can you retrive his secret from the vault?

_Note: Only /function/\* is within scope_
