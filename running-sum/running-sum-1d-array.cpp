class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
       vector <int> r;
        int n=nums.size();
        r.push_back(nums[0]);
        for(int i=1;i<n;i++)
            r.push_back(nums[i]+r[i-1]);
        return r;
    }
};
