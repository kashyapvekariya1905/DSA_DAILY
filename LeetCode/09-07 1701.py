from typing import List
def averageWaitingTime(customers: List[List[int]]) -> float:
    total = 0
    free = 0
    for arr,pre in customers:
        st = max(free,arr)
        fin = st+pre
        wai = fin-arr
        total+=wai
        free = fin
    avgw = total/len(customers)
    return avgw

customers = [[1,2],[2,5],[4,3]]
print(averageWaitingTime(customers))
customers = [[5,2],[5,4],[10,3],[20,1]]
print(averageWaitingTime(customers))

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prepare, n=0, len(customers)
        return sum((prepare:=max(t[0],prepare)+t[1])-t[0] for t in customers)/n
      

100% beats
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        const int n=customers.size();
        double prepare=0, sum=0;
        for(auto& t: customers){
            prepare=((t[0]>prepare)?t[0]:prepare)+t[1];
            sum+=prepare-t[0];
        }
        return sum/n;
    }
};

auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();
