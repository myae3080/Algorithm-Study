import java.io.*;
import java.util.Arrays;

public class Baek_30033 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        // input
        int N = Integer.parseInt(bufferedReader.readLine());
        int[] listA = Arrays.stream(bufferedReader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] listB = Arrays.stream(bufferedReader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        bufferedReader.close();

        int result = 0;
        for (int i = 0; i < N; i++) {
            if (listA[i] <= listB[i]) {
                result++;
            }
        }

        bufferedWriter.write(result + "");

        bufferedWriter.flush();
        bufferedWriter.close();
    }
}
