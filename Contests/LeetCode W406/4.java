import java.util.*;

class Solution {
    public long minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        Arrays.sort(horizontalCut);
        reverseArray(horizontalCut);
        Arrays.sort(verticalCut);
        reverseArray(verticalCut);

        long a = 0, b = 0; 
        long hp = 1, vp = 1;
        long rst = 0;

        while (a < horizontalCut.length && b < verticalCut.length) {
            if (horizontalCut[(int)a] > verticalCut[(int)b]) {
                rst += (long)horizontalCut[(int)a] * vp;
                hp++;
                a++;
            } else {
                rst += (long)verticalCut[(int)b] * hp;
                vp++;
                b++;
            }
        }

        while (a < horizontalCut.length) {
            rst += (long)horizontalCut[(int)a] * vp;
            a++;
        }

        while (b < verticalCut.length) {
            rst += (long)verticalCut[(int)b] * hp;
            b++;
        }

        return rst;
    }
    private void reverseArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}
