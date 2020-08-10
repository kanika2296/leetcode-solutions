class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int,int> m;
        for(int i=0;i<nums.size();i++)
        {
            int d=target-nums[i];
            if(m.count(d))
                return {i,m[d]};
            else
                m.insert(make_pair(nums[i],i));
        }
        return {0,0};
    }
};
