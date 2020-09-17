def twoSum(list_num, target):
        idx_lst = []
        for idx in range(len(list_num)):
            num1 = list_num[idx]
            for idx2 in range(len(list_num)):
                num2 = list_num[idx2]
                if idx == idx2:
                    continue
                else:
                    sum = num1 + num2
                    if sum == target:
                        idx_lst.append(idx)
                        idx_lst.append(idx2)
                        return idx_lst  


# test

a = [2,7,11,15]
a2 = [15,7,2,11]
b = 9

print(twoSum(a2,b))