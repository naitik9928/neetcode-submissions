class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store={}
        for word in strs:
            key="".join(sorted(word))
            if key in store:
                store[key].append(word)
            else:
                store[key]=[word]
        return list(store.values())