class Solution {
  int romanToInt(String s) {

    Map<String, int> roman = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    };

    int ans = 0;

    for (int i = 0; i < s.length; i++) {

      int current = roman[s[i]]!;

      // Last character
      if (i == s.length - 1) {
        ans += current;
      }

      // Current < Next -> Subtract
      else if (current < roman[s[i + 1]]!) {
        ans -= current;
      }

      // Otherwise Add
      else {
        ans += current;
      }
    }

    return ans;
  }
}