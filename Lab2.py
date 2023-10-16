#Задание №1

#def list_recorder(ref_list):
   #new_list = []
    #for i in range(len(ref_list) // 2):
       #new_list.append([ref_list[i * 2], ref_list[i * 2 + 1]]):
            #return new_list
        
#Зажание №2

#def del_rep(num):
    #seen = set()
    #reesult = []
    #for item in num:
        #if item not in seen:
            #seen.add(item)
            #result.append(item)
            
            #return sorted(result)
        #if __name__ == "__main__":
            #num = [1, 2, 3, 4, 5, 6, 2, 1, 5, 3]
            #print(del_rep(num))
            
#Задание №3

#def lim_max(nums, limit):
    #if len(nums) == 0:
        #return -1
    #max_value = nums[0]
    #for num in nums:
        #if num > max_value and num < limit:
            #max_value = num
            #return max_value
    
#Задание №4

def temp_cat(temp):
    if temp < -20:
        return 0
    elif temp <= 0:
        return 1
    elif temp <= +15:
        return 2
    elif temp <= +25:
        return 3
    else:
        return 4
    
     
#Задание №5