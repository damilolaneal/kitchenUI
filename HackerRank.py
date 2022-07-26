# Author: Damilola Olawoyin-Yussuf

import heapq


def beautifulTriplets(d, arr):
    count = 0
    for i in arr:
        if ((i + d) in arr) and ((i + (2 * d)) in arr):
            count += 1
    return count


def matrix_spiral(inputMatrix):
    ret = []
    while len(inputMatrix) > 0:
        ret.extend(inputMatrix[0])
        inputMatrix.remove(inputMatrix[0])
        for i, data in enumerate(inputMatrix):
            if len(data) > 0:
                if i == len(inputMatrix) - 1:
                    last_row = inputMatrix[-1]
                    ret.extend(last_row[::-1])
                    inputMatrix.remove(data)
                else:
                    ret.append(data[-1])
                    inputMatrix[i].remove(data[-1])
            else:
                inputMatrix.remove(data)
        if len(inputMatrix) > 0:
            up = []
            for j, data_ in enumerate(inputMatrix):
                if len(data_) > 0:
                    up.append(data_[0])
                    inputMatrix[j].remove(data_[0])
                else:
                    inputMatrix.remove(data_)
            ret.extend(up[::-1])
    return ret


def reorganizeString(s):
    """
    :type s: str
    :rtype: str
    """

    final_string = ""
    my_map = {}
    for i in s:
        # keys = my_map.keys()
        if i not in my_map:
            my_map[i] = 1
        else:
            my_map[i] = my_map[i] + 1
    maxHeap = [[-val, key] for key, val in my_map.items()]
    heapq.heapify(maxHeap)

    prev = None
    while maxHeap or prev:

        if prev and not maxHeap:
            if prev[0] < -1:
                return ""

        currVal, currKey = heapq.heappop(maxHeap)
        final_string += currKey
        currVal += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None
        if currVal != 0:
            prev = [currVal, currKey]
    # my_map = {k: v for k, v in sorted(my_map.items(), key=lambda x: x[1], reverse=True)}
    return final_string


def minimumDistances(a):
    # Write your code here
    my_map = {}
    for i, data in enumerate(a):
        if data in my_map:
            # temp = my_map.get(data) + [i]
            # temp = temp + [i]
            my_map[data] = my_map.get(data) + [i]
        else:
            my_map[data] = [i]
    print(my_map)

    def minimum_diff(temp_list):
        diff = []
        for el in range(len(temp_list) - 1):
            for em in range(el + 1, len(temp_list)):
                diff.append(temp_list[em] - temp_list[el])
        return min(diff)

    all_min = []
    for k, v in my_map.items():
        if len(v) > 1:
            all_min.append(minimum_diff(v))

    if len(all_min) > 0:
        return min(all_min)
    else:
        return -1


def longestDiverseString(a, b, c):
    """
    Happy strings
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    ret = ""
    maxHeap = []
    for cnt, key in [[-a, "a"], [-b, "b"], [-c, "c"]]:
        if cnt != 0:
            heapq.heappush(maxHeap, [cnt, key])

    while maxHeap:

        val, item = heapq.heappop(maxHeap)

        if len(ret) > 1 and ret[-1] == ret[-2] == item:
            if not maxHeap:
                break
            val1, item1 = heapq.heappop(maxHeap)
            ret += item1
            val1 += 1
            if val1 != 0:
                heapq.heappush(maxHeap, [val1, item1])
        else:
            ret += item
            val += 1

        if val != 0:
            heapq.heappush(maxHeap, [val, item])

    return ret


def numSteps(s):
    """
    Number of Steps to Reduce a Number in Binary Representation to One
    :type s: str
    :rtype: int
    """
    div = 1000000
    num = 0
    for i, data in enumerate(s[::-1]):
        num += int(data) * (2 ** i)

    if num <= 1:
        return 0
    count = 0
    while div > 1:
        if num % 2 == 0:
            div = num / 2
            count += 1
            num = div
        else:
            num += 1
            count += 1

    return count


def containsDuplicate(nums):
    """
        :type nums: List[int]
        :rtype: bool
        """
    myMap = {}
    for i in nums:
        if i not in myMap:
            myMap[i] = 1
        else:
            return True
    # myMapList = list(myMap)
    # heapq.heapify(myMapList)
    # print(myMapList)
    # for k, v in myMap.items():
    #     if v > 1:
    #         return True
    return False


def isAnagram(s, t):
    """
        :type s: str
        :type t: str
        :rtype: bool
    """
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    return False


def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    loc = {}
    ret = []
    for i, data in enumerate(nums):
        num = target - data
        if num in loc:
            ret.append(i)
            ret.append(loc.get(num))
        else:
            loc[data] = i
    return ret


def groupAnagrams(strs):
    """
        :type strs: List[str]
        :rtype: List[List[str]]
    """
    myMap = {}
    for i in strs:
        count = [0] * 26
        for c in i:
            count[ord(c) - ord("a")] += 1
        k = tuple(count)
        if k in myMap:
            curr = myMap.get(k, [])
            curr.append(i)
            myMap[k] = curr
        else:
            myMap[k] = [i]
        # k = (sorted(i))
        # k = "".join(k)
        # if k in myMap:
        #     curr = myMap.get(k, [])
        #     curr.append(i)
        #     myMap[k] = curr
        # else:
        #     myMap[k] = [i]

    # res = []
    # for k, v in myMap.items():
    #     res.append(v)

    return list(myMap.values())


def topKFrequent(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
    """
    myMap = {}
    for i in nums:
        if i in myMap:
            myMap[i] = myMap.get(i, 0) + 1
        else:
            myMap[i] = 1

    myHeap = []
    for key, v in myMap.items():
        myHeap.append([-v, key])

    heapq.heapify(myHeap)

    ret = []
    for j in range(k):
        c_key, c_value = heapq.heappop(myHeap)
        ret.append(c_value)

    return ret


def productExceptSelf(nums):
    """
        :type nums: List[int]
        :rtype: List[int]
        """
    ret = []
    prefix = 1
    for i in range(len(nums)):
        if i == 0:
            prefix = 1
        else:
            prefix *= nums[i - 1]
        ret.append(prefix)

    assert (len(nums) == len(ret))
    postfix = 1
    for i in range(len(nums) - 2, -1, -1):
        postfix *= nums[i + 1]
        ret[i] = ret[i] * postfix
    return ret


def isValidSudoku1(board):
    """
        :type board: List[List[str]]
        :rtype: bool
    """
    # get 3 x 3 cell collect number of each digits
    col1 = {}
    col2 = {}
    col3 = {}
    col4 = {}
    col5 = {}
    col6 = {}
    col7 = {}
    col8 = {}
    col9 = {}
    for i in range(0, 9, 3):
        line1 = {}
        line2 = {}
        line3 = {}
        sq1 = {}
        sq2 = {}
        sq3 = {}
        for idx, (j, k, m) in enumerate(zip(board[i], board[i + 1], board[i + 2])):
            if j != ".":
                curr = line1.get(j, 0) + 1
                if curr > 1:
                    return False
                line1[j] = curr

                if idx > 5:
                    curr = sq3.get(j, 0) + 1
                    if curr > 1:
                        return False
                    sq3[j] = curr
                elif idx > 2:
                    curr = sq2.get(j, 0) + 1
                    if curr > 1:
                        return False
                    sq2[j] = curr
                else:
                    curr = sq1.get(j, 0) + 1
                    if curr > 1:
                        return False
                    sq1[j] = curr

                if idx == 0:
                    curr = col1.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col1[j] = curr
                if idx == 1:
                    curr = col2.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col2[j] = curr
                if idx == 2:
                    curr = col3.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col3[j] = curr
                if idx == 3:
                    curr = col4.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col4[j] = curr
                if idx == 4:
                    curr = col5.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col5[j] = curr
                if idx == 5:
                    curr = col6.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col6[j] = curr
                if idx == 6:
                    curr = col7.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col7[j] = curr
                if idx == 7:
                    curr = col8.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col8[j] = curr
                if idx == 8:
                    curr = col9.get(j, 0) + 1
                    if curr > 1:
                        return False
                    col9[j] = curr

            if k != ".":
                curr = line2.get(k, 0) + 1
                if curr > 1:
                    return False
                line2[k] = curr

                if idx > 5:
                    curr = sq3.get(k, 0) + 1
                    if curr > 1:
                        return False
                    sq3[k] = curr
                elif idx > 2:
                    curr = sq2.get(k, 0) + 1
                    if curr > 1:
                        return False
                    sq2[k] = curr
                else:
                    curr = sq1.get(k, 0) + 1
                    if curr > 1:
                        return False
                    sq1[k] = curr

                if idx == 0:
                    curr = col1.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col1[k] = curr
                if idx == 1:
                    curr = col2.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col2[k] = curr
                if idx == 2:
                    curr = col3.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col3[k] = curr
                if idx == 3:
                    curr = col4.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col4[k] = curr
                if idx == 4:
                    curr = col5.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col5[k] = curr
                if idx == 5:
                    curr = col6.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col6[k] = curr
                if idx == 6:
                    curr = col7.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col7[k] = curr
                if idx == 7:
                    curr = col8.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col8[k] = curr
                if idx == 8:
                    curr = col9.get(k, 0) + 1
                    if curr > 1:
                        return False
                    col9[k] = curr

            if m != ".":
                curr = line3.get(m, 0) + 1
                if curr > 1:
                    return False
                line3[m] = curr

                if idx > 5:
                    curr = sq3.get(m, 0) + 1
                    if curr > 1:
                        return False
                    sq3[m] = curr
                elif idx > 2:
                    curr = sq2.get(m, 0) + 1
                    if curr > 1:
                        return False
                    sq2[m] = curr
                else:
                    curr = sq1.get(m, 0) + 1
                    if curr > 1:
                        return False
                    sq1[m] = curr

                if idx == 0:
                    curr = col1.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col1[m] = curr
                if idx == 1:
                    curr = col2.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col2[m] = curr
                if idx == 2:
                    curr = col3.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col3[m] = curr
                if idx == 3:
                    curr = col4.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col4[m] = curr
                if idx == 4:
                    curr = col5.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col5[m] = curr
                if idx == 5:
                    curr = col6.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col6[m] = curr
                if idx == 6:
                    curr = col7.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col7[m] = curr
                if idx == 7:
                    curr = col8.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col8[m] = curr
                if idx == 8:
                    curr = col9.get(m, 0) + 1
                    if curr > 1:
                        return False
                    col9[m] = curr
    return True


"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""


def encode(strs):
    # write your code here
    ret = "#$".join(strs)
    return ret + "#$"


"""
@param: str: A string
@return: decodes a single string to a list of strings
"""


def decode(str):
    # write your code here
    ret = []
    curr = str[0]
    for i in range(1, len(str)):
        # if i < len(str) and str[i] == "#" and str[i + 1] == "$":
        if str[i - 1] == "#" and str[i] == "$":
            ret.append(curr[:-1])
            curr = ""
        else:
            curr += str[i]

    return ret


def isValidSudoku(board):
    """
        :type board: List[List[str]]
        :rtype: bool
    """
    # horizontal
    for i in board:
        hor = {}
        for j in i:
            if j != ".":
                curr = hor.get(j, 0) + 1
                if curr > 1:
                    return False
                else:
                    hor[j] = curr
    # vertical
    for i in range(len(board)):
        ver = {}
        for j in range(len(board)):
            if board[j][i] != ".":
                curr = ver.get(board[j][i], 0) + 1
                if curr > 1:
                    return False
                else:
                    ver[board[j][i]] = curr
    # Box of 3
    for i in range(0, len(board), 3):
        box = {}
        y = board[i:i + 3]
        # print(y)
        for j in range(len(board)):
            if j % 3 == 0:
                box = {}
            curr1, curr2, curr3 = 0, 0, 0
            if y[0][j] != ".":
                curr1 = box.get(y[0][j], 0) + 1
            if y[1][j] != ".":
                curr2 = box.get(y[1][j], 0) + 1
            if y[2][j] != ".":
                curr3 = box.get(y[2][j], 0) + 1

            if curr1 > 1 or curr2 > 1 or curr3 > 1:
                return False
            else:
                if y[0][j] != ".":
                    box[y[0][j]] = curr1
                if y[1][j] != ".":
                    box[y[1][j]] = curr2
                if y[2][j] != ".":
                    box[y[2][j]] = curr3
            # print(box)
    return True


def alphaNum(c):
    return (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <= ord(c) <= ord("9")) or (ord("a") <= ord(c) <= ord("z"))


def isPalindrome(s):
    """
        :type s: str
        :rtype: bool
    """
    # str_ = ""
    # if len(s) < 2:
    #     return True
    # for i in s:
    #     if i.isalnum():
    #         str_ += i.lower()
    # return str_ == str_[::-1]
    l_ = 0
    r = len(s) - 1
    while l_ < r:
        while l_ < r and not alphaNum(s[l_]):
            l_ += 1
        while r > l_ and not alphaNum(s[r]):
            r -= 1

        if s[l_].lower() != s[r].lower():
            return False
        else:
            l_ += 1
            r -= 1
            continue

    return True


def threeSum(nums):
    """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    nums = sorted(nums)
    ret = []
    for i, data in enumerate(nums):
        if i > 0 and data == nums[i - 1]:
            continue
        print(data)
        l_ = i + 1
        r = len(nums) - 1
        while l_ < r:
            rec = data + nums[l_] + nums[r]
            if rec < 0:
                l_ += 1
            elif rec > 0:
                r -= 1
            else:
                ret.append([data, nums[l_], nums[r]])
                l_ += 1
                while nums[l_] == nums[l_ - 1] and l_ < r:
                    l_ += 1
    return ret


def maxArea(height):
    """
        :type height: List[int]
        :rtype: int
        """
    max_ = 0
    le, r = 0, len(height) - 1
    while le < r:
        length = min(height[le], height[r])
        width = r - le
        area = length * width
        if height[le] < height[r]:
            le += 1
        else:
            r -= 1
        max_ = max(max_, area)

    return max_


def substrCount(n, s):
    count = 0

    for i in range(n):
        l_ = r = i
        prev = ""
        temp_count = 0
        while l_ >= 0 and r < n and s[l_] == s[r]:
            if temp_count > 1 and s[l_] != prev:
                break
            temp_count += 1
            count += 1
            prev = s[l_]
            l_ -= 1
            r += 1

        l_ = i
        r = i + 1
        prev = s[l_]
        while l_ >= 0 and r < n and s[l_] == s[r]:
            if s[l_] != prev:
                break
            prev = s[l_]
            count += 1
            l_ -= 1
            r += 1
    return count


# def commonChild(s1, s2):
#     # Write your code here
#     count = 0
#     l1, r1 = 0, len(s1) - 1
#     l2, r2 = 0, len(s2) - 1
#     while l1 < r1 and l2 < r2:
#         if s1[l1] == s2[l2]:

def floodFill(image, sr, sc, color):
    """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
    """
    visited = set()
    myStack = [[sr, sc]]
    maxRow, maxCol = len(image), len(image[0])
    imVal = image[sr][sc]
    while len(myStack) > 0:
        sr_, sc_ = myStack.pop(0)

        image[sr_][sc_] = color
        visited.add((sr_, sc_))

        t, b = sr_ - 1,  sr_ + 1
        l_, r = sc_ - 1, sc_ + 1
        if 0 <= t < maxRow and image[t][sc_] == imVal and ((t, sc_) not in visited):
            myStack.append([t, sc_])
            visited.add((t, sc_))
        if b < maxRow and image[b][sc_] == imVal and ((b, sc_) not in visited):
            myStack.append([b, sc_])
            visited.add((b, sc_))
        if 0 <= l_ < maxCol and image[sr_][l_] == imVal and ((sr_, l_) not in visited):
            myStack.append([sr_, l_])
            visited.add((sr_, l_))
        if r < maxCol and image[sr_][r] == imVal and ((sr_, r) not in visited):
            myStack.append([sr_, r])
            visited.add((sr_, r))
    return image
