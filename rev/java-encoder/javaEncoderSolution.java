import java.util.Base64;
import java.nio.charset.StandardCharsets;
import java.io.UnsupportedEncodingException;
import java.util.function.Function;
import java.util.Arrays;
import java.math.BigInteger; 
import java.security.MessageDigest; 
import java.security.NoSuchAlgorithmException; 
import java.util.List;
import java.lang.*;
import java.util.Scanner;  


class JavaEncoderSolution {

    public static void main(String[] args) {
        String[] flag = {"","",""};
    	String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{~-:}";

        int num1 = Integer.parseInt("A74", 16)%14;
        int num2 = (alphabet.length()+1)%4;
        int num3 = 67352854%19;
        
    	flag[num1] = part1(alphabet);
        flag[num2] = part2();
        String s = "-JbZ-LZSZ8138JJ-381";
        int rot = (flag[num1].length()+flag[num2].length()+s.length()+2)%50;
        flag[num3] = part3(s, alphabet, rot);
        
        System.out.println(String.join("_", flag));  // Print out the flag 
    }
    
     public static String part1(String alphabet) {// Bruteforce all possible MD5 hashes
        String start = "d0ne~:cl";
        for(char a: alphabet.toCharArray()){
            for(char b: alphabet.toCharArray()){
                for(char c: alphabet.toCharArray()){
                    for(char d: alphabet.toCharArray()){
                       try {

                            MessageDigest md = MessageDigest.getInstance("MD5"); 
                            byte[] digest = md.digest((start+a+b+c+d).getBytes()); 
                            BigInteger no = new BigInteger(1, digest); 
                            String hash = no.toString(16); 
                            while (hash.length() < 32) { 
                                hash = "0" + hash; 
                            } 
                            if(hash.equals("7716715cf6f91f8b4b51c55aa3312169")){
                                return start+a+b+c+d;
                            }
                        }  
                        catch (NoSuchAlgorithmException e1) { 
                            throw new RuntimeException(e1); 
                        } 
                    }
                }
            }
        }
        return "";
    } 
    public static String part2() {// Decode the Base64 encoded string
    	try {
            return new String(Base64.getDecoder().decode("S0lEMjB7SDB0fmRhbW4=".getBytes()));
        } catch(Exception ex) {
            throw new RuntimeException(ex);
        }
    }
    public static String part3(String s, String alphabet, int rot) { // Revert a rotation cipher with rotation rot
        String o = "";
        for (char c: s.toCharArray()) {
            int pos = alphabet.indexOf(c);
            o += alphabet.charAt((pos-rot+alphabet.length())%alphabet.length());
        }
        return o; 
    }
}
