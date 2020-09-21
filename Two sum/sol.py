def twoSum(nums, target):
        know_val = {}
        final_lst = []
        for (idx, num) in enumerate(nums):
            rest = target - num
            if rest in know_val:
                if idx < know_val[rest]:
                    final_lst.append(idx)
                    final_lst.append(know_val[rest])
                else:
                    final_lst.append(know_val[rest])
                    final_lst.append(idx)
                return final_lst               
            else:
                know_val[num] = idx
        