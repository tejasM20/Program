import java.util.Scanner;
import java.util.Arrays;

public class FractionalKnapsack3 {

    // Class to define each item
    static class Item {
        int weight, value;
        double ratio;

        Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
            // Calculate value per unit of weight
            ratio = (double) value / weight;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();
        Item[] items = new Item[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight and value: ");
            int weight = sc.nextInt();
            int value = sc.nextInt();
            items[i] = new Item(weight, value);
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        // Step 1: Sort items in decreasing order of their value/weight ratio
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));

        double maxValue = 0;

        // Step 2: Greedy method to fill the knapsack
        for (Item item : items) {
            // If the whole item can fit, take it completely
            if (capacity >= item.weight) {
                capacity -= item.weight;
                maxValue += item.value;
            }
            // If it can't fit completely, take the fraction that fills the remaining capacity
            else {
                maxValue += item.ratio * capacity;
                break; // The knapsack is now full
            }
        }

        System.out.println("\nMaximum value we can obtain = " + maxValue);
        sc.close();
    }
}