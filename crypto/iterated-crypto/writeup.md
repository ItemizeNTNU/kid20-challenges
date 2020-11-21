# iterated-crypto
## Description

In this challenge, you see that an emperor encrypted something. There is also a weird phrasing of the year 2020, as two thousand and 20. This could perhaps indicate the usage of the Caesar cipher with a shift of `20`. 

With this decrypted, you get
```
An old french dude encoded this.. are you KIDding?
Nqg iwx odhb ohd br ztdi bko Vlxbhxlr64?
C0tHWrE7lrE0H2D2P25pG3MJkKAeA2Xpev9hgQ9YA3uegF9QgGp9Fq==
```

An old french dude could be regarded as rather cryptic, but if you have had a cryptography course you would be familiar with the Vigenère cipher. The cipher require a key, which can be spotted hiding in the decrypted sencence: "...are you KIDding?". `KID` is the key, and you get the following text:

```
Did you ever get to play the Nintendo64?
S0lEMjB7bjB0X2V2M25fY3JZcHQwX2Nhbl9zdG9QX3kwdV9IdWh9Cg==
```

Nintendo 64 huh? For those familiar with Base64, would immediately recognize the two trailing equal signs. This is often found with something encoded with Base64. 

Converting from Base64 gives you the flag: `KID20{n0t_ev3n_crYpt0_can_stoP_y0u_Huh}`