import java.util.*;

class Solution {
    int timer = 0;
    int LOGN = 17;
    int[] tin, tout, currentChars;
    int[][] up;
    int[] tree, lazy;

    // Fixed signature: Renamed from palindromicPathQueries to palindromePath
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        tin = new int[n];
        tout = new int[n];
        up = new int[n][LOGN];
        currentChars = new int[n];
        for (int i = 0; i < n; i++) {
            currentChars[i] = s.charAt(i) - 'a';
        }

        int[] initialMasks = new int[n];
        dfs(0, 0, 0, adj, initialMasks);

        int[] posMask = new int[n + 1];
        for (int i = 0; i < n; i++) {
            posMask[tin[i]] = initialMasks[i];
        }

        tree = new int[4 * (n + 1)];
        lazy = new int[4 * (n + 1)];
        build(1, 1, n, posMask);

        List<Boolean> ans = new ArrayList<>();
        for (String q : queries) {
            String[] parts = q.split(" ");
            if (parts[0].equals("update")) {
                int u = Integer.parseInt(parts[1]);
                int newC = parts[2].charAt(0) - 'a';
                int oldC = currentChars[u];
                if (oldC != newC) {
                    int changeMask = (1 << oldC) ^ (1 << newC);
                    updateRange(1, 1, n, tin[u], tout[u], changeMask);
                    currentChars[u] = newC;
                }
            } else {
                int u = Integer.parseInt(parts[1]);
                int v = Integer.parseInt(parts[2]);
                int lca = getLca(u, v);
                int maskU = queryPoint(1, 1, n, tin[u]);
                int maskV = queryPoint(1, 1, n, tin[v]);
                int pathMask = maskU ^ maskV ^ (1 << currentChars[lca]);
                ans.add((pathMask & (pathMask - 1)) == 0);
            }
        }
        return ans;
    }

    private void dfs(int u, int p, int currentMask, List<List<Integer>> adj, int[] initialMasks) {
        tin[u] = ++timer;
        up[u][0] = p;
        for (int i = 1; i < LOGN; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        int newMask = currentMask ^ (1 << currentChars[u]);
        initialMasks[u] = newMask;
        for (int v : adj.get(u)) {
            if (v != p) {
                dfs(v, u, newMask, adj, initialMasks);
            }
        }
        tout[u] = timer;
    }

    private boolean isAncestor(int u, int v) {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    }

    private int getLca(int u, int v) {
        if (isAncestor(u, v)) return u;
        if (isAncestor(v, u)) return v;
        for (int i = LOGN - 1; i >= 0; i--) {
            if (!isAncestor(up[u][i], v)) {
                u = up[u][i];
            }
        }
        return up[u][0];
    }

    private void build(int node, int start, int end, int[] posMask) {
        if (start == end) {
            tree[node] = posMask[start];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid, posMask);
        build(2 * node + 1, mid + 1, end, posMask);
    }

    private void push(int node) {
        if (lazy[node] != 0) {
            tree[2 * node] ^= lazy[node];
            lazy[2 * node] ^= lazy[node];
            tree[2 * node + 1] ^= lazy[node];
            lazy[2 * node + 1] ^= lazy[node];
            lazy[node] = 0;
        }
    }

    private void updateRange(int node, int start, int end, int l, int r, int val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            tree[node] ^= val;
            lazy[node] ^= val;
            return;
        }
        push(node);
        int mid = (start + end) / 2;
        updateRange(2 * node, start, mid, l, r, val);
        updateRange(2 * node + 1, mid + 1, end, l, r, val);
    }

    private int queryPoint(int node, int start, int end, int idx) {
        if (start == end) return tree[node];
        push(node);
        int mid = (start + end) / 2;
        if (idx <= mid) return queryPoint(2 * node, start, mid, idx);
        else return queryPoint(2 * node + 1, mid + 1, end, idx);
    }
}
