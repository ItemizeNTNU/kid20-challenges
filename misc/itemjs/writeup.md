Here, the point of the challange was to use flaws in javascript in order to bypass all assert messages. This could be done by the following string:
```json
{"b":100, "c":"Infinity", "d":0, "e":-0, "f":"0x0", "g": "Infinity", "j": "Object", "l": "keys", "m":"flagObj", "h": "-1", "i": "-12"}
```

This is why:

* `a`: We don't need an a actually.
* `b`: Must just be a number
* `c`: `"Infinity"` is casted as `Infinity` when a number. Therefor `Infinity + Infinity = "Infinity"` with double equal.
* `d`, `e`: `0` and `-0` are both the same, however, if you divide by them, the result is either `Infinity` or `-Infinity`
* `f`, `g`: `"0x0"` and an integer larger than what accepted by javascript (2^32) will be casted to `Infinity`, same with `"Infinity"`
* `h`, `i`: Using lexical values as strings, the strings will have some interesting properties
* `j`, `l`, `m`: Here, we wated to have `flagObj[Object.keys(flagObj)]`, therefor `j = "Object", k = "keys", m = "flagObj"`
