#include <vector>
#include <iostream>
#include <vector>
#include <__algorithm/pstl_sort.h>
class Solution {
public:
    long long minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        sort(horizontalCut.rbegin(), horizontalCut.rend());
        sort(verticalCut.rbegin(), verticalCut.rend());
        
        long long h = 0, v = 0; // Use long long to avoid overflow
        long long horizontalPieces = 1, verticalPieces = 1;
        long long totalCost = 0;
        
        while (h < horizontalCut.size() && v < verticalCut.size()) {
            if (horizontalCut[h] > verticalCut[v]) {
                totalCost += (long long)horizontalCut[h] * verticalPieces;
                horizontalPieces++;
                h++;
            } else {
                totalCost += (long long)verticalCut[v] * horizontalPieces;
                verticalPieces++;
                v++;
            }
        }
        
        while (h < horizontalCut.size()) {
            totalCost += (long long)horizontalCut[h] * verticalPieces;
            h++;
        }
        
        while (v < verticalCut.size()) {
            totalCost += (long long)verticalCut[v] * horizontalPieces;
            v++;
        }
        
        return totalCost;

    }
};
