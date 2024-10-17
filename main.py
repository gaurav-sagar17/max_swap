class Solution:
    def maximumSwap(self, num: int) -> int:
        def helper(arr,ptr) :
            m = arr[len(arr)-ptr-1]
            pos = 0  ## starting position 
            for i in range(len(arr)-ptr) :
                if(arr[i] > m) :
                    m = arr[i] 
                    pos = i 
            if(pos == len(arr)-ptr-1) :
                return -1 

            else :
                print(arr)
                temp = arr[len(arr)-ptr-1] 
                arr[len(arr)-ptr-1] = arr[pos] 
                arr[pos] = temp 
                print(arr)

            return 0 

        self.lst = [] 
        while(num > 0) :
            d = num%10 
            num = num//10 
            self.lst.append(d) 

        for i in range(len(self.lst)) :
            exit_status = helper(self.lst,i)
            if(exit_status == 0) :
                break 
        ans = 0
        for j in range(len(self.lst)) :
            ans = ans*10 + self.lst[len(self.lst)-j-1] 

        return ans 
