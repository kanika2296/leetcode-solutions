class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=nums.size(),j,i;
        if(n==0)
            return 0;
        j=0;
        for(i=1;i<n;i++)
        {
            if(nums[j]!=nums[i])
                nums[++j]=nums[i];
        }
        nums.resize(++j);
        return j;
    }
};
