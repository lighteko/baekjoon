import java.util.*;
import java.io.*;
public class P1655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder()); // max-heap
        PriorityQueue<Integer> big = new PriorityQueue<>(); // min-heap
        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(br.readLine());
            if (small.isEmpty() || small.peek() >= value) {
                small.offer(value);
            } else {
                big.offer(value);
            }
            if (small.size() > big.size() + 1) {
                big.offer(small.poll());
            } else if (small.size() < big.size()) {
                small.offer(big.poll());
            }
            assert small.peek() != null;
            System.out.println(small.peek());
        }
    }
}
