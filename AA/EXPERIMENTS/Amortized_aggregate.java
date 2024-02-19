import java.util.*;

public class Amortized_aggregate {
    static int maxSize = 3, top = 0, pop_cost = 0, push_cost = 0, multipop_cost = 0;

    public static boolean isFull (){
        return top == maxSize-1;
    }

    public static void multipop (int k, int maxSize, Stack<Integer> st){
        for(int i = 0; i < k; i++) {
            if (!st.empty()) {
                int popped = st.pop();
                pop_cost++;
                System.out.println("Popped element "+popped+" stack = "+st);
            } else {
                break;
            }
        }
    }

    public static void main(String args[]) {
        Stack<Integer> stack = new Stack<>();

        int[] arr = {5,7,9,2,6,1,8,3};
        for(int i = 0; i < arr.length; i++) {
            if (arr[i] <= maxSize) {
                int k = arr[i];
                multipop(k,maxSize,stack);
                multipop_cost++;
            }
            stack.push(arr[i]);
            push_cost++;
            System.out.println("Pushed element "+i+" stack = "+stack);
            top++;
        }
        System.out.println("Cost of all operation = "+(push_cost+pop_cost));
        System.out.println("Cost of multipop operation = "+multipop_cost);
        System.out.println("Time complexity = O("+(push_cost+pop_cost-multipop_cost)/arr.length+")");
    }
}