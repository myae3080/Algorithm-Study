import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Baek_15552 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int count = Integer.parseInt(bufferedReader.readLine());

        for (int i = 0; i < count; i++) {
            int tempSum = 0;

            for (String str : bufferedReader.readLine().split(" ")) {
                tempSum += Integer.parseInt(str);
            }

            bufferedWriter.write(tempSum + "\n");
        }

        bufferedReader.close();

        bufferedWriter.flush();
        bufferedWriter.close();
    }
}
