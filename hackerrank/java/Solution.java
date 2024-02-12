import java.io.*;
import java.util.*;

public class Solution {

    static void loop(int a, int b, int n) {
        int[] result = new int[n];
        int res = a;
        result[0] = res;
        for (int i = 1; i < n; i++) {
            res += Math.pow(2, i) * b;
            result[i] = res;
        }
        System.out.println(Arrays.toString(result.toArray()));
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int q = scanner.nextInt();
        for (int i = 0; i < q; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int n = scanner.nextInt();
            loop(a, b, n);
        }
    }
}
