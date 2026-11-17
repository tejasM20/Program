
import java.util.*;

public class HuffmanEncoding2 {
    // Tree node structure
    static class Node {
        char ch;
        int freq;
        Node left, right;

        // Leaf node constructor
        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }

        // Internal node constructor
        Node(int freq, Node left, Node right) {
            this.freq = freq;
            this.left = left;
            this.right = right;
        }
    }

    // Generate Huffman codes via recursive traversal
    static void generate(Node root, String code, Map<Character, String> map) {
        if (root == null)
            return;

        // If it's a leaf node, assign the accumulated binary string
        if (root.left == null && root.right == null) {
            map.put(root.ch, code);
            return;
        }

        // Traverse left (append '0') and right (append '1')
        generate(root.left, code + "0", map);
        generate(root.right, code + "1", map);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter string: ");
        String str = sc.nextLine();

        // Step 1: Find frequency of each character
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : str.toCharArray())
            freq.put(c, freq.getOrDefault(c, 0) + 1);

        // Step 2: Build a Min Priority Queue
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.freq - b.freq);

        // Add all unique characters as leaf nodes
        for (char c : freq.keySet())
            pq.add(new Node(c, freq.get(c)));

        // Step 3: Build the Huffman Tree (Greedy Approach)
        while (pq.size() > 1) {
            Node a = pq.poll(); // Extract min freq
            Node b = pq.poll(); // Extract 2nd min freq

            // Create a parent node summing the frequencies
            pq.add(new Node(a.freq + b.freq, a, b));
        }

        // The last remaining node is the root of the tree
        Node root = pq.poll();

        // Step 4: Generate and map the binary codes
        Map<Character, String> code = new HashMap<>();
        generate(root, "", code);

        // Display codes
        System.out.println("\nHuffman Codes:");
        for (char c : code.keySet())
            System.out.println(c + " : " + code.get(c));

        // Encode the original string
        String encoded = "";
        for (char c : str.toCharArray())
            encoded += code.get(c);

        System.out.println("\nOriginal String: " + str);
        System.out.println("Encoded String: " + encoded);
        System.out.println("\nTime Complexity: O(n log n)");
        System.out.println("Space Complexity: O(n)");
        sc.close();
    }
}