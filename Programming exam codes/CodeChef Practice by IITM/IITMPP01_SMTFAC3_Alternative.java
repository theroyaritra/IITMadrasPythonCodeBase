//https://www.codechef.com/IITMPP01/problems/SNTFAC3
import java.util.*;

class IITMPP01_SMTFAC3_Alternative
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t!= 0) {
            int sum = 0;
            int m = sc.nextInt();
            int n = sc.nextInt();
            int k = sc.nextInt();
            int arr[] = new int[m];
            for (int i = 0; i < m; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);
            for (int i = 0; i < k; i++){
                arr[i] = n - arr[i];
            } 
            for (int i = 0; i < m; i++) {
                sum += arr[i];
            }
            System.out.println(sum);
            t--;
        }
        sc.close();
	}
}
