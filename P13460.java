import java.io.*;
import java.util.*;

class Node {
    int x, y;
    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public static void BFS(int[][] board, Node red, Node blue) {
        class State {
            final Node red, blue;
            public State(Node red, Node blue) {
                this.red = red;
                this.blue = blue;
            }
        }
        Queue<State> queue = new LinkedList<>();
        Set<State> visited = new HashSet<>();
        State start = new State(red, blue);
        queue.offer(start);
        visited.add(start);

    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}
public class P13460 {
    public static void main(String[] args) throws IOException {

        // STEP 1: Initialize Input data
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[nm.length - 1]);
        int[][] arr = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n * m; i++) {
            visited[i / m][i % n] = false;
        }
        Node red = new Node(0,0, null);
        Node blue = new Node(0,0,null);
        for (int i = 0; i < n; i++) {
            String value = br.readLine();
            for (int j = 0; j < m; j++) {
                if (value.charAt(j) == '#') {
                    arr[i][j] = -1;
                } else if (value.charAt(j) == '.') {
                    arr[i][j] = 1;
                } else if (value.charAt(j) == 'R') {
                    arr[i][j] = 1;
                    red = new Node(i, j);
                } else if (value.charAt(j) == 'B') {
                    arr[i][j] = 1;
                    blue = new Node(i, j);
                } else {
                    arr[i][j] = 0;
                }
            }
        }
        // STEP 2: Search the minimum number of tilts using BFS
        Node.BFS(arr, red, blue);
    }
}
