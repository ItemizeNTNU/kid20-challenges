import java.io.*;  
import java.util.*;
import java.nio.file.*;

class FlagManipulatorSolver {

    public static void main(String[] args) {
        String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{_}";
        String flag = "";
        BufferedReader br;
        try{
            File f=new File("output.txt"); 
            FileReader fr=new FileReader(f);
            br=new BufferedReader(fr); // Read from output.txt
            int c = 0;  
            char prevChar='0';         
            int counter = 0;
            while((c = br.read()) != -1){ // Iterate over every bit in output.txt
                if ((char) c == prevChar){
                    counter++;
                }else {
                    flag+=(char)counter;
                    counter=1;
                }
                prevChar=(char)c;
            }
            flag+=(char)counter;
        } catch (IOException e){return;}

        String mid = flag.substring(6,flag.length()-1); 
        String useThis = "C0uld_Th15_b3_1T7gsl9"; // Retrived from the libstring.so native library
        mid = revertD(mid, useThis, alphabet); 
        mid = revertA(mid, alphabet);

        int num=0;
        try { // Get the binary number from bits.txt
            File myObj = new File("bits.txt"); 
            Scanner r = new Scanner(myObj);
            num = Integer.parseInt(r.nextLine(), 2)%255;
            r.close();
        } catch (FileNotFoundException e) {return;}
        //Get the final value for a from Manipulator.java
        int start = (int)Math.pow(mid.length(),3)/4 - (int)(Math.pow(mid.length(),3)/4)%num;
        for (int a = start;a>=0;a-=num){//go backwards from the end 
            if(mid.codePointAt(0)%2==0){
                mid = mid.substring(0,1)+revertB(mid.substring(1));
            }
            mid = revertA(mid.substring(0,a%mid.length()), alphabet) + mid.substring(a%mid.length());
        }
        // Print out the flag 
        System.out.println(flag.substring(0,6)+mid+flag.substring(flag.length()-1));
    }
    public static String revertA(String s, String alphabet) {
        String oldString = "";
        for(int i=0;i<s.length();i++){
            oldString += alphabet.charAt((alphabet.indexOf(s.charAt(i))-i+alphabet.length())%alphabet.length());
        }
        return revertHelp(oldString);
    }   
    public static String revertB(String s){
        return new StringBuilder(s).reverse().toString(); 
    }
    
    public static String revertD(String a, String b, String alphabet) {
        String o = "";
        char[] ca = a.toCharArray();
        char[] cb = b.toCharArray();
        for (int i=0;i<ca.length;i++) {
            int posa = alphabet.indexOf(ca[i]);
            int posb = alphabet.indexOf(cb[i]);
            o += alphabet.charAt((posa-posb+alphabet.length())%alphabet.length());
        }
        return o; 
    }  
    public static String revertHelp(String s){
        int middle = s.length()/2;
        if (s.length()%2==1){
            middle++;
        }
        String end = s.substring(0,middle);
        String start = s.substring(middle,s.length());
        if(middle==0||middle==1||(s.length()%2==1 && middle==2)){
            return revertB(start)+revertB(end);
        } else {
            return revertB(revertHelp(start))+revertB(revertHelp(end));
        }
            
    }
}

