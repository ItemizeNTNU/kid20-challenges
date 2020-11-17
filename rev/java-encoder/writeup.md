# java-encoder:
## Description:
In this task we are given a java file which uses differnt type of encoding to check if the flag is correct. We can see that the flag is split into 3 parts where each part is sent into a verification function to see if that part is correct. *part1* converts the input string into its MD5 hash sum, *part2* encodes the input string with Base64 encoding and *part3* is a rotation cipher on the input string with a given rotation value. 
A possible solution can be seen in  [javaEncoderSolution.java](javaEncoderSolution.java).

To compile the code:
```
javac javaEncoderSolution.java
```
To run the code:
```
java javaEncoderSolution.java
```
And the output from:
```
KID20{H0t~damn_r3ver5e-engin33ring_d0ne~:clap:}
```