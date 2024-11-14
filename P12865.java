import java.util.*;

public class P12865 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int k = scan.nextInt();

        int[] dp = new int[k + 1];
        for (int i = 0; i < n; i++) {
            int w = scan.nextInt();
            int v = scan.nextInt();
            for (int j = k; j >= w; j--) {
                dp[j] = Math.max(dp[j], dp[j - w] + v);
            }
        }
        System.out.println(dp[k]);
    }
}
