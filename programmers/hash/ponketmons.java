package programmers.hash;

import java.util.*;

class ponketmons {
    public static int solution(int[] nums) {
        HashSet<Integer> p = new HashSet<>();
        for (int num : nums) {
            p.add(num);
        }
        return Math.min(nums.length/2, p.size());
    }

    public static void main(String[] args) {
        int[] nums = {3, 1, 2, 3};
        int answer = solution(nums);
        System.out.println(answer);
    }
}
