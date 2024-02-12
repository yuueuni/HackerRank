import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            try{
                long n = scanner.nextLong();
                System.out.println(n + " can be fitted in:");

                if (-128<=n && n <= 127) System.out.println("* byte");
                if (-32768<=n && n <= 32767) System.out.println("* short");
                if (-2147483648<=n && n <= 2147483647) System.out.println("* int");
                System.out.println("* long");

            } catch(Exception e) {
                System.out.println(scanner.next() + " can't be fitted anywhere.");
            }
        }
    }
}