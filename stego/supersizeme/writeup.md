# supersizeme
## Description
In this challenge you are given a PNG file and a description saying it is a half done look. Running the tool pngcheck will give us a CRC error in the IHDR chunk. A quick internet search tells us that the IHDR chunk of a PNG file contains information about the dimensions of the image. As the challenge description references the image as a half look, we can try to double the height of the image by changing the IHDR chunk in a hex editor. Doing so will reveal the rest of the image, and the flag will be at the bottom of the image.

```
KID20{of_er_ikke_smart}
```