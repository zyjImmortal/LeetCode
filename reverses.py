def reverse(x):
    """
    :type x: int
    :rtype:  int
    """
    tran_list = list(str(x))
    if tran_list[0] == '-':
        reverse_list = tran_list[1:]
        reverse_list.reverse()
        for i in reverse_list:
            if i == 0:
                reverse_list.remove(i)
            else:
                break
        x = '-' + ''.join(reverse_list)
        return int(x)
    tran_list.reverse()
    for i in tran_list:
        if i == 0:
            tran_list.pop(i)
        else:
            break
    x = ''.join(tran_list)
    return int(x)


class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        tran_list = list(str(x))
        if tran_list[0] == '-':
            reverse_list = tran_list[1:]
            reverse_list.reverse()
            for i in reverse_list:
                if i == 0:
                    reverse_list.pop(i)
                else:
                    break
            x = '-' + ''.join(reverse_list)
        else:
            tran_list.reverse()
            for i in tran_list:
                if i == 0:
                    tran_list.pop(i)
                else:
                    break
            x = ''.join(tran_list)
        x = int(x)
        if x > 2 ** 31 or x < -2 ** 31:
            return 0
        return x

    @staticmethod
    def reverse_v2(x):
        rev = 0
        while x != 0:
            pop = x % 10
            x = round(x / 10)
            rev = rev * 10 + pop
        return rev

if __name__ == '__main__':
    print(Solution.reverse_v2(55345))
