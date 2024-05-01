class Solution:
    def minimumKeypresses(self, s: str) -> int:
        hash_map=Counter(s)
        freq_array=[[key,hash_map[key]] for key in hash_map.keys()]
        freq_array = sorted(freq_array,key=lambda x:x[1], reverse=True)
        total_press=0
        single_press=1
        for index,char in enumerate(freq_array):
            total_press+=char[1]*single_press
            if (index+1)%9==0:
                single_press+=1
        return total_press
    
            
        
            
        