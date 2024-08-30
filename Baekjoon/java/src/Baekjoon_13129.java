// source : https://www.acmicpc.net/problem/13129

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Baekjoon_13129 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        // input
        int[] inputs = Arrays.stream(bufferedReader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        bufferedReader.close();

        int A = inputs[0];
        int B = inputs[1];
        int N = inputs[2];

        ArrayList<String> heights = new ArrayList<String>();
        int base = A + B;

        for (int i = N - 1; i > -1; i--) {
            heights.add(String.valueOf(base + (A * i) + ((N - 1 - i) * (A + B))));
        }

        bufferedWriter.write(String.join(" ", heights));
        bufferedWriter.flush();
        bufferedWriter.close();
    }
}
