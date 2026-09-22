#include <vector>

using namespace std;

struct Node {
    int total_prod = 1;
    vector<int> remain;
    Node(int k) {
        remain.assign(k, 0);
    }
};

class SegmentTree {
private:
    int n;
    int k;
    vector<Node> tree;

    void merge(Node& parent, const Node& left, const Node& right) {
        parent.total_prod = (left.total_prod * right.total_prod) % k;
        
        // Inherit all valid prefixes from the left child
        for (int i = 0; i < k; ++i) {
            parent.remain[i] = left.remain[i];
        }
        
        // Append prefixes extending into the right child, shifting their remainders
        for (int i = 0; i < k; ++i) {
            if (right.remain[i] > 0) {
                int target_rem = (left.total_prod * i) % k;
                parent.remain[target_rem] += right.remain[i];
            }
        }
    }

    void build(const vector<int>& nums, int node, int start, int end) {
        if (start == end) {
            int val = nums[start] % k;
            tree[node].total_prod = val;
            tree[node].remain[val] = 1;
            return;
        }
        int mid = start + (end - start) / 2;
        build(nums, 2 * node, start, mid);
        build(nums, 2 * node + 1, mid + 1, end);
        merge(tree[node], tree[2 * node], tree[2 * node + 1]);
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            fill(tree[node].remain.begin(), tree[node].remain.end(), 0);
            int rem = val % k;
            tree[node].total_prod = rem;
            tree[node].remain[rem] = 1;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        merge(tree[node], tree[2 * node], tree[2 * node + 1]);
    }

    Node query(int node, int start, int end, int l, int r) {
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = start + (end - start) / 2;
        if (r <= mid) {
            return query(2 * node, start, mid, l, r);
        }
        if (l > mid) {
            return query(2 * node + 1, mid + 1, end, l, r);
        }
        Node left_res = query(2 * node, start, mid, l, r);
        Node right_res = query(2 * node + 1, mid + 1, end, l, r);
        Node parent_res(k);
        merge(parent_res, left_res, right_res);
        return parent_res;
    }

public:
    SegmentTree(const vector<int>& nums, int modulo_k) {
        n = nums.size();
        k = modulo_k;
        tree.assign(4 * n, Node(k));
        build(nums, 1, 0, n - 1);
    }

    void update_value(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }

    int query_x(int start_idx, int target_x) {
        Node res = query(1, 0, n - 1, start_idx, n - 1);
        return res.remain[target_x];
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        SegmentTree st(nums, k);
        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            int index = q[0];
            int value = q[1];
            int start = q[2];
            int x = q[3];

            // 1. Persistently update the array
            st.update_value(index, value);
            
            // 2. Fetch the number of prefixes matching the target remainder x
            ans.push_back(st.query_x(start, x));
        }
        return ans;
    }
};
