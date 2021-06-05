import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baek_13305 {
    public static void main(String[] args) throws IOException {
        int cityCount;
        long minPrice = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        cityCount = Integer.parseInt(br.readLine());
        long[] distanceArray = new long[cityCount - 1];
        long[] priceArray = new long[cityCount];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < cityCount - 1; i++) {
            distanceArray[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < cityCount; i++) {
            priceArray[i] = Integer.parseInt(st.nextToken());
        }

        minPrice = distanceArray[0] * priceArray[0];

        // 이중 for문으로 최소값을 다 체크해서 더하는 방식은 시간 초과 발생.
        int currentOil = 0;
        int currentCity = 1;

        while (currentCity < cityCount -1) {
            if (priceArray[currentOil] > priceArray[currentCity]) {
                currentOil = currentCity;
            }

            minPrice += distanceArray[currentCity] * priceArray[currentOil];
            currentCity++;
        }

        System.out.println(minPrice);
    }
}
