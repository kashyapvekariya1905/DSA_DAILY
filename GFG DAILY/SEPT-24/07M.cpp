// User function Template for C++

class Solution {
  public:
    long long findNth(long long n) {
        // code here.
        if(n<9)return n;
        return findNth(n/9)*10+n%9;
    }
};