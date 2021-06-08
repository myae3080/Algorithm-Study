// math, arithmetic

import java.util.Arrays;
import java.util.Scanner;

public class Baekjoon_4153 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            int a = input.nextInt();
            int b = input.nextInt();
            int c = input.nextInt();

            int[] lengthArray = {a, b, c};

            // ASC
            Arrays.sort(lengthArray);

            // escape
            // frequency를 사용해 보려 했는데 느리고 복잡함.
            if (a == 0 && b == 0 && c == 0) {
                break;
            }

            if (Math.pow(lengthArray[0], 2) + Math.pow(lengthArray[1], 2) == Math.pow(lengthArray[2], 2)) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
