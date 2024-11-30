import java.io.*;
import java.util.*;

class Node {
    int x, y;
    Node prev;
    public Node(int x, int y, Node prev) {
        this.x = x;
        this.y = y;
        this.prev = prev;
    }
    public static List<Node> BFS(int[][] graph, Node RBPos, boolean[][] visited) {
        Queue<Node> queue = new LinkedList<>();
        List<Node> paths = new ArrayList<>();
        queue.offer(RBPos);
        visited[RBPos.x][RBPos.y] = true;
        while (!queue.isEmpty()) {
            Node cursor = queue.poll();
            if (graph[cursor.x][cursor.y] == 0) {
                Node subCursor = cursor;
                while(subCursor != null) {
                    paths.add(0,subCursor);
                    subCursor = subCursor.prev;
                }
                break;
            }
            if (Node.check(cursor.x - 1, cursor.y, graph) && !visited[cursor.x - 1][cursor.y]) {
                queue.offer(new Node(cursor.x - 1, cursor.y, cursor));
                visited[cursor.x - 1][cursor.y] = true;
            }
            if (Node.check(cursor.x + 1, cursor.y, graph) && !visited[cursor.x + 1][cursor.y]) {
                queue.offer(new Node(cursor.x + 1, cursor.y, cursor));
                visited[cursor.x + 1][cursor.y] = true;
            }
            if (Node.check(cursor.x, cursor.y - 1, graph) && !visited[cursor.x][cursor.y - 1]) {
                queue.offer(new Node(cursor.x, cursor.y - 1, cursor));
                visited[cursor.x][cursor.y - 1] = true;
            }
            if (Node.check(cursor.x, cursor.y + 1, graph) && !visited[cursor.x][cursor.y + 1]) {
                queue.offer(new Node(cursor.x, cursor.y + 1, cursor));
                visited[cursor.x][cursor.y + 1] = true;
            }
        }
        return paths;
    }

    public static boolean check(int x, int y, int[][] graph) {
        int n = graph.length;
        int m = graph[0].length;
        if (x >= n || x < 0 || y >= m || y < 0) return false;
        return graph[x][y] == 1 || graph[x][y] == 0;
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
                    red = new Node(i, j, null);
                } else if (value.charAt(j) == 'B') {
                    arr[i][j] = 1;
                    blue = new Node(i, j, null);
                } else {
                    arr[i][j] = 0;
                }
            }
        }
        // STEP 2: Search valid paths for red ball using BFS
        List<Node> paths = Node.BFS(arr, red, visited);

        // STEP 3: Simulate blue ball by the path of red ball
        // STEP 3-1: Remove redundant paths.
        for (int i = 1; i + 1 < paths.size(); i++) {
            Node cursor = paths.get(i - 1);
            if (cursor.x == paths.get(i).x && cursor.x == paths.get(i + 1).x || cursor.y == paths.get(i).y && cursor.y == paths.get(i + 1).y) {
                paths.remove(i);
                i--;
            }
        }

        // STEP 3-2: Simulate both red and blue balls.
        int tilts = 0;
        for (int i = 1, len = paths.size(); i < len; i++) {
            int dx = paths.get(i).x - red.x;
            int dy = paths.get(i).y - red.y;
            if (dx != 0) {
                red.x += dx;
                if (dx > 0) {
                    while (Node.check(blue.x, blue.y, arr)) {
                        blue.x++;
                        if (blue.x == red.x && blue.y == red.y) break;
                    }
                    blue.x--;
                    Node cursor = new Node(blue.x, blue.y, null);
                    for (int x = 0; x < m && Node.check(cursor.x, cursor.y, arr); x++) {
                        cursor.x += 1;
                        if (arr[cursor.x][cursor.y] == 0) break;
                    }
                    if (arr[cursor.x][cursor.y] == 0) {
                        tilts = -1;
                        break;
                    }
                } else {
                    while (Node.check(blue.x, blue.y, arr)) {
                        blue.x--;
                        if (blue.x == red.x && blue.y == red.y) break;
                    }
                    blue.x++;
                    Node cursor = new Node(blue.x, blue.y, null);
                    for (int x = 0; x < m && Node.check(cursor.x, cursor.y, arr); x++) {
                        cursor.x -= 1;
                        if (arr[cursor.x][cursor.y] == 0) break;
                    }
                    if (arr[cursor.x][cursor.y] == 0) {
                        tilts = -1;
                        break;
                    }
                }
                tilts++;
            } else if (dy != 0) {
                red.y += dy;
                if (dy > 0) {
                    while (Node.check(blue.x, blue.y, arr)) {
                        blue.y++;
                        if (blue.x == red.x && blue.y == red.y) break;
                    }
                    blue.y--;
                    Node cursor = new Node(blue.x, blue.y, null);
                    for (int x = 0; x < m && Node.check(cursor.x, cursor.y, arr); x++) {
                        cursor.y += 1;
                        if (arr[cursor.x][cursor.y] == 0) break;
                    }
                    if (arr[cursor.x][cursor.y] == 0) {
                        tilts = -1;
                        break;
                    }
                } else {
                    while (Node.check(blue.x, blue.y, arr)) {
                        blue.y--;
                        if (blue.x == red.x && blue.y == red.y) break;
                    }
                    blue.y++;
                    Node cursor = new Node(blue.x, blue.y, null);
                    for (int x = 0; x < m && Node.check(cursor.x, cursor.y, arr); x++) {
                        cursor.y -= 1;
                        if (arr[cursor.x][cursor.y] == 0) break;
                    }
                    if (arr[cursor.x][cursor.y] == 0) {
                        tilts = -1;
                        break;
                    }
                }
                tilts++;
            }
        }
        if (tilts > 10) System.out.println(-1);
        else System.out.println(tilts);
    }
}
