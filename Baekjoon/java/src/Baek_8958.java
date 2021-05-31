import java.util.Scanner;

// 제출 시, class명을 Main으로 바꾸고 제출해야 함.
public class Baek_8958 {
    public static void main(String[] args) {
        String tempString;
        int tempScore;
        int resultScore;

        Scanner input = new Scanner(System.in);

        String oxList[] = new String[input.nextInt()];

        for (int i = 0; i < oxList.length; i++) {
            oxList[i] = input.next();
        }

        for (String str : oxList) {
            tempScore = 1;
            resultScore = 0;

            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == 'O') {
                    if (i != 0 && str.charAt(i-1) == 'O') {
                        tempScore += 1;
                    }

                    resultScore += tempScore;
                } else {
                    tempScore = 1;
                }
            }

            System.out.println(resultScore);
        }
    }
}
