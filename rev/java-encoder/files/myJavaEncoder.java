import java.util.Base64;
import java.nio.charset.StandardCharsets;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger; 
import java.security.MessageDigest; 
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;  


class MyJavaEncoder {

    public static void main(String[] args) {
    	String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{~-:}";

    	Scanner input = new Scanner(System.in);
    	System.out.println("Type in your flag guess: ");
    	String userFlagGuess = input.nextLine();
    	String[] flagParts = userFlagGuess.split("_");

        if (flagParts.length==3){
        	Boolean split1 = part1(flagParts[Integer.parseInt("A74", 16)%14]);
        	Boolean split2 = part2(flagParts[(alphabet.length()+1)%4]);
        	Boolean split3 = part3(flagParts[67352854%19], alphabet,userFlagGuess.length()%50);
        	
        	if (split1 && split2 && split3){
        		System.out.println("Correct flag! :)");
        		return;
        	}
        }
        System.out.println("That's not it, try again");
    }
    
    
     public static boolean part1(String s) {
     	if (s.length()!=12){return false;}
     	if (!s.substring(0,8).equals("d0ne~:cl")){return false;}
        try { 
            MessageDigest md = MessageDigest.getInstance("MD5"); 
            byte[] digest = md.digest(s.getBytes()); 
            BigInteger no = new BigInteger(1, digest); 
            String hash = no.toString(16); 
            while (hash.length() < 32) { 
                hash = "0" + hash; 
            } 
            return hash.equals("7716715cf6f91f8b4b51c55aa3312169"); 
        }  
        catch (NoSuchAlgorithmException e) { 
            throw new RuntimeException(e); 
        } 
    } 
    public static boolean part2(String s) {
    	try {
            return Base64.getEncoder().encodeToString(s.getBytes(StandardCharsets.UTF_8.toString())).equals("S0lEMjB7SDB0fmRhbW4=");        
        } catch(UnsupportedEncodingException ex) {
            throw new RuntimeException(ex);
        }
    }
    public static boolean part3(String s, String alphabet, int rot) {
        String o = "";
        for (char c: s.toCharArray()) {
            int pos = alphabet.indexOf(c);
            o += alphabet.charAt((pos+rot)%alphabet.length());
        }
        return o.equals("-JbZ-LZSZ8138JJ-381"); 
    }
}
