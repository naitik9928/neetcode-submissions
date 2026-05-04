class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for num in nums:
            if num in store:
                store[num]+=1
            else:
                store[num]=1
        result=sorted(store.items(),key=lambda x:x[1],reverse=True)[:k]
        return [item[0] for item in result]