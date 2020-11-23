# fermeture-éclair
## Description
In this challenge we are given an image file and asked to find a zip file. If we open the image in a text or hex editor we can search for the magic bytes of a zip file, and can see that the zip file is places directly after the image file. Simply copying the last part of the file after the zip magic bytes and saving it as a zip will give us the requested zip file.
Alternatively the task can be solved using a forensic tool, such as binwalk.
```
$ binwalk fermeture-éclair.jpg -e
```

When we have the zip file, getting the flag is as simple as unzipping the file and reading the image.

```
KID20{Zip-a-dee-doo-dah_zip-a-dee-ay}
```