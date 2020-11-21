# grocery-shopping-2
## Description
In this challenge we are given a black and white image with static noise. In the top of the image we can see a suspicious black line. At first this line could look like morse code, however, decoding it will only return garbage. If you instead look at the beginning and end of the black line, and think back to grocery-shopping-1, you can see that they match with the control lines in a code 128 barcode (assuming you know how they look like). Removing the noise and stretching the black line to be taller the barcode will present itself. Reading the barcode with a barcode reader will reveal the flag.

```
KID20{Base128}
```