"""
GCA Practice
"""

"""
Mutate the array
----------------
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1]
"""
a = [4, 0, 1, -2, 3]
n = 5


# passing
def mutateTheArray(n, a):
    if len(a) < 2:
        return a
    result = []
    for i in range(len(a)):
        # if i = 0 then i - 1 does not exist so [i-1] becomes 0 and we can
        # just leave it off
        if i == 0:
            result.append(a[i] + a[i + 1])
        # if i is pointing to the last element then [i + 1] does not exist so
        # it becomes 0 and we can just leave that off
        elif i == len(a) - 1:
            result.append((a[i - 1] + a[i]))
        # for all other cases just do the normal equation
        else:
            result.append(a[i - 1] + a[i] + a[i + 1])

    return result


# print(mutateTheArray(n, a))

"""
Alternating sort
You are given an array of integers a. A new array b is generated by rearranging the elements of a in the following way:

b[0] is equal to a[0];
b[1] is equal to the last element of a;
b[2] is equal to a[1];
b[3] is equal to the second-last element of a;
b[4] is equal to a[2];
b[5] is equal to the third-last element of a;
and so on.
Here is how this process works:



Your task is to determine whether the new array b is sorted in strictly ascending order or not.

Example

For a = [1, 3, 5, 6, 4, 2], the output should be alternatingSort(a) = true.

The new array b will look like [1, 2, 3, 4, 5, 6], which is in strictly ascending order, so the answer is true.

For a = [1, 4, 5, 6, 3], the output should be alternatingSort(a) = false.

The new array b will look like [1, 3, 4, 6, 5], which is not in strictly ascending order, so the answer is false.
"""
a = [1, 3, 5, 6, 4, 2]
# a = [1, 4, 5, 6, 3]
# a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
a = [-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87]
a = [-99, -29, -7, 17, 28, 71, 98, 86, 42, 22, 0, -29, -86]

# passing
from collections import deque


def alternatingSort(a):
    a = deque(a)
    if len(a) < 2:
        return True
    if a == []:
        return False
    # array to hold result
    b = []
    # sorted a without duplicates to check against result array to see if
    # result is sorted or not
    match = sorted(set(a))
    # while a still has numbers to sort into result array
    while len(a) > 0:
        # if there is an even number of items left
        if len(b) % 2 == 0:
            # remove first element and add to result
            b.append(a.popleft())
        # else if there is an odd number of items left
        else:
            # remove last element and add it to the result
            b.append(a.pop())
    # if result == the original array sorted then return True else return False
    if b == match:
        return True
    return False


# print(alternatingSort(a))

"""
Tiny pairs
----------
You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
countTinyPairs(a, b, k) = 2.

We're considering the following pairs during iteration:

(1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
(2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
(3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be
countTinyPairs(a, b, k) = 4.

We're considering the following pairs during iteration:

(16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;
(1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;
(4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.
(2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;
(14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.
There are 4 tiny pairs during the iteration, so the answer is 4.
"""

a = [16, 1, 4, 2, 14]
b = [7, 11, 2, 0, 15]
k = 743


# passing
def countTinyPairs(a, b, k):
    # variable to hold the number of tiny pairs we've encountered
    pairs = 0
    # index of the last number in the array
    b_index = len(b) - 1
    # iterate the array
    for i in range(len(a)):
        # if the integer value of the string concatenation of the number at
        # the first index and the number at the last index is less than K
        # we found a tiny pair and can increment the pairs value + 1
        if int(str(a[i]) + str(b[b_index])) < k:
            pairs += 1
        # decrement the last index to check the next to last number
        b_index -= 1
    # return the number of pairs found
    return pairs


# print(countTinyPairs(a, b, k))

"""
Merging Strings
---------------
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".



You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Example

For s1 = "dce" and s2 = "cccbd", the output should be
mergeStrings(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.



For s1 = "super" and s2 = "tower", the output should be
mergeStrings(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length ≤ 104.

[input] string s2

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length ≤ 104.

[output] string

The string that results by merging s1 and s2 using your special merge function.
"""

s1 = "super"
s2 = "tower"

s1 = "dce"
s2 = "cccbd"

s1 = "kkihj"
s2 = "jbsmfoftph"
expected = "jbsmfoftphkkihj"

s1 = "ougtaleegvrabhugzyx"
s2 = "wvieaqgaegbxg"
output = "owvieaqugaegbxggtaleegvrabhugzyx"
expected = "owvieaqugtaleegvrabhugzyxgaegbxg"


# fully passing
def mergeStrings(s1, s2):
    # variable to hold the result
    result = ''
    # variable to hold the current index of the longer of the two strings
    s2_index = 0
    # variable to hold the current index of the shorter of the two strings
    s1_index = 0
    # variables for the s2 string and the s1 string
    # s2 = ''
    # s1 = ''
    # logic to find the s2 and s1 strings from the given strings
    # if len(s1) > len(s2):
    #     s2 = s1
    #     s1 = s2
    # else:
    #     s2 = s2
    #     s1 = s1
    # hash maps for each string to hold the number of occurrences of each
    # letter
    s1_map = {}
    s2_map = {}
    # logic creating the hash maps
    for letter in s1:
        if letter not in s1_map:
            s1_map[letter] = 0
        s1_map[letter] += 1

    for letter in s2:
        if letter not in s2_map:
            s2_map[letter] = 0
        s2_map[letter] += 1
    print('s1 map:', s1_map)
    print('s2 map:', s2_map)
    # while the s1 string current index is less than the s1 string length
    # and the s2 string index is shorter than the s2 string length
    # (keeps us from index out of bounds error)
    while s1_index < len(s1) and s2_index < len(s2):
        print('s1', s1)
        print('s2', s2)
        print('result:', result)
        print('compare', 's1', s1[s1_index], 's2', s2[s2_index])
        # my print statements for debugging
        # print('i', i)
        # print('s2_index', s2_index)
        # print(chr(max(ord(s1[i]), ord(s2[s2_index]))))
        # if the letter count for the s1 string letter at current s1
        # string index is less than the letter count for the s2 string
        # letter at current s2 string index
        if s1_map[s1[s1_index]] < s2_map[s2[s2_index]]:

            # print('s1 i', s1[i])
            # print('count', s1_map[s1[i]])
            # print('s2 i', s2[s2_index])
            # print('count', s2_map[s2[s2_index]])
            # add the letter from the s1 string at the current index to
            # the result
            result += s1[s1_index]
            # increment the s1 string current index
            s1_index += 1
        # if the letter count for the s1 string letter at the current
        # index is greater than the letter count for the s2 string letter
        # at current s2 string index
        elif s1_map[s1[s1_index]] > s2_map[s2[s2_index]]:
            # add the letter from the s2 string at the current index to the
            # result
            result += s2[s2_index]
            # increment the s2 string current index
            s2_index += 1
        # if both letter have the same number of occurrences in their
        # respective strings
        else:
            # TODO if both strings are equal take from s1 **********
            if ord(s1[s1_index]) == ord(s2[s2_index]):
                result += s1[s1_index]
                s1_index += 1
            else:
                # add the letter that comes first sequentially
                result += chr(min(ord(s1[s1_index]), ord(s2[s2_index])))
                # if the s2 string letter was added
                if ord(s1[s1_index]) > ord(s2[s2_index]):
                    # increment the s2 string current index
                    s2_index += 1
                # else if the s1 string letter was added
                else:
                    # increment the s1 string current index
                    s1_index += 1
    # if the s1 string index is at the end of the string
    # we have added all the letters in that string and can just add the rest
    # of the letters in the s2 string to the result in the order they are in
    if s1_index == len(s1):
        # add rest of the s2 string from the current index to the end of
        # the string
        result += s2[s2_index:]
    # if the s2 string index is at the end of the string
    # we have added all the letters in that string and can just add the rest
    # of the letters in the s1 string to the result in the order they are in
    if s2_index >= len(s2):
        # add rest of the s1 string from the current index to the end of
        # the string
        result += s1[s1_index:]
    # return the result
    return result


# print(mergeStrings(s1, s2))

"""
Concatenations Sum
------------------
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

Example

For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

a[0] ∘ a[0] = 1 ∘ 1 = 11,
a[0] ∘ a[1] = 1 ∘ 2 = 12,
a[0] ∘ a[2] = 1 ∘ 3 = 13,
a[1] ∘ a[0] = 2 ∘ 1 = 21,
a[1] ∘ a[1] = 2 ∘ 2 = 22,
a[1] ∘ a[2] = 2 ∘ 3 = 23,
a[2] ∘ a[0] = 3 ∘ 1 = 31,
a[2] ∘ a[1] = 3 ∘ 2 = 32,
a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.
"""

a = [8]

a = [1, 2, 3]

a = [0, 0]

# needs to be optimized to pass all tests currently 250/300
def concatenationsSum(a):
    # variable for the result of the integer addition of concatenated strings
    result = 0
    # variables for the current index and the index of the number being added
    curr_i = 0
    sum_i = 0
    # iterate the array
    while curr_i < len(a):
        # if the number being added is the last one
        if sum_i == len(a) - 1:
            # do the concatenation
            result += int(str(a[curr_i]) + str(a[sum_i]))
            # increment the current index
            curr_i += 1
            # reset the sum index to 0
            sum_i = 0
        # otherwise just do the concatenation and increase the index of
        # number being added
        else:
            result += int(str(a[curr_i]) + str(a[sum_i]))
            sum_i += 1

    # return the result
    return result


# def concatenationsSum(a):
#     # variable to hold the current concatenation
#     string_sum = ''
#     # result of the integer addition of concatenated strings
#     result = 0
#     # iterate the array
#     for current_num in a:
#         # concat it with each other num in the array
#         for concat_num in a:
#             # add the integer value of the string concatenation to the result
#             result += int(str(current_num) + str(concat_num))
#     # return the result
#     return result


print(concatenationsSum(a))

"""
HashMap
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be hashMap(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.



For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be hashMap(queryType, query) = 6.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 4}
3 query: answer is 4
4 query: {1: 4, 2: 3}
5 query: {2: 4, 3: 3}
6 query: {2: 3, 3: 2}
7 query: answer is 2
The sum of the results for all the get queries is equal to 4 + 2 = 6.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string queryType

Array of query types. It is guaranteed that each queryType[i] is either "addToKey", "addToValue", "get", or "insert".

Guaranteed constraints:
1 ≤ queryType.length ≤ 105.

[input] array.array.integer query

Array of queries, where each query is represented either by two numbers for insert query or by one number for other queries. It is guaranteed that during all queries all keys and values are in the range [-109, 109].

Guaranteed constraints:
query.length = queryType.length,
1 ≤ query[i].length ≤ 2.

[output] integer64

The sum of the results for all get queries.
"""

queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue",
             "get"]
query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]

queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]

queryType = ["addToKey",
             "addToValue",
             "insert",
             "addToValue",
             "addToKey",
             "get",
             "insert",
             "addToValue",
             "addToValue",
             "get",
             "insert",
             "addToKey",
             "get",
             "addToKey",
             "addToKey",
             "addToValue",
             "insert",
             "addToValue",
             "get",
             "addToKey",
             "addToKey",
             "insert",
             "addToValue",
             "addToKey",
             "addToValue",
             "insert",
             "get",
             "addToKey",
             "addToValue",
             "get",
             "get",
             "get",
             "addToValue",
             "addToValue",
             "get",
             "get",
             "insert",
             "insert",
             "addToKey",
             "insert",
             "addToValue",
             "addToValue",
             "addToKey",
             "addToValue",
             "addToValue",
             "get",
             "addToValue",
             "addToKey",
             "get",
             "addToValue",
             "insert",
             "get",
             "get",
             "get",
             "addToValue",
             "addToValue",
             "get",
             "addToKey",
             "get",
             "addToKey",
             "addToValue",
             "get",
             "get",
             "addToKey",
             "insert",
             "addToKey",
             "get",
             "addToKey",
             "addToValue",
             "addToKey",
             "insert",
             "addToKey",
             "addToValue",
             "addToKey",
             "addToValue",
             "addToValue",
             "get",
             "get",
             "addToKey",
             "insert",
             "get",
             "get",
             "addToKey",
             "insert",
             "addToKey",
             "addToValue",
             "addToKey",
             "insert",
             "addToValue",
             "get",
             "get",
             "insert",
             "get",
             "get",
             "addToValue",
             "get",
             "addToValue",
             "insert",
             "addToKey",
             "addToValue"]

query = [[32],
         [-4],
         [32, -42],
         [19],
         [-45],
         [-13],
         [29, -29],
         [-50],
         [40],
         [-13],
         [39, -11],
         [-47],
         [-60],
         [16],
         [-14],
         [45],
         [-34, 17],
         [-12],
         [-6],
         [2],
         [-33],
         [-33, -6],
         [40],
         [-14],
         [30],
         [-13, 11],
         [-61],
         [-1],
         [-40],
         [-62],
         [-52],
         [-52],
         [-18],
         [-2],
         [-104],
         [-104],
         [-27, -13],
         [28, -17],
         [-40],
         [39, -1],
         [-40],
         [25],
         [-39],
         [46],
         [27],
         [-51],
         [-33],
         [11],
         [-130],
         [37],
         [37, -20],
         [-95],
         [-95],
         [11],
         [37],
         [-2],
         [-40],
         [-47],
         [-167],
         [13],
         [-41],
         [-164],
         [-206],
         [1],
         [14, 19],
         [23],
         [-92],
         [39],
         [25],
         [-33],
         [-5, -34],
         [-45],
         [23],
         [2],
         [-13],
         [-12],
         [-163],
         [-142],
         [-4],
         [-34, -44],
         [-91],
         [-34],
         [34],
         [-49, -19],
         [9],
         [-24]]


# this is not currently passing all tests but most
def hashMap(queryType, query):
    # variable to hold the sum of each 'get' query type
    sum_of_gets = 0
    # variable to hold the hash table
    query_hash = {}
    # variable to hold a new hash table for use with the addToKey function
    addedHash = {}

    # helper function to insert a new key value pair into the hash table
    def insert(key, value):
        query_hash[key] = value

    # helper function to get a value with a given key
    def get(key):
        return query_hash[key]

    # helper function to increment all the keys by a given value
    def addToKey(value):
        # iterate all keys in the hash table
        for key in query_hash:
            print('inside', query_hash)
            print(addedHash)
            print(query_hash[key])
            # create a new key value pair in the addedHash table with the key
            # incremented by the given value
            addedHash[key + value] = query_hash[key]

    # helper function to increment all the values by a given value
    def addToValue(value):
        # iterate all the keys in the hash table
        for key in query_hash:
            # increment the current value by the given value
            query_hash[key] += value

    # iterate the queryType array
    for i in range(len(queryType)):
        print('query type', queryType[i])
        print('query', query[i])
        print('hash before', query_hash)
        # if the query type is insert
        if queryType[i] == 'insert':
            # call the insert helper function with the values from the query
            # array that corresponds to the query type
            insert(query[i][0], query[i][1])
        # if the query type is get
        elif queryType[i] == 'get':
            # increment the sum_of_gets with the value returned from calling
            # the helper get function with the values from the query array
            # that corresponds to the query type
            sum_of_gets += get(query[i][0])
        # if the query type is addToValeu
        elif queryType[i] == 'addToValue':
            # call the add to value helper function with the value from the
            # query array that corresponds to the query type
            addToValue(query[i][0])
        # else if the query type is addToKey
        else:
            # call the addToKey helper function with the value from the
            # query array that corresponds to the query type
            addToKey(query[i][0])
            # then set the original query_hash to equal the new addedHash
            # with the incremented keys
            if addedHash != {}:
                query_hash = addedHash.copy()
        print('hash after', query_hash)

    print(query_hash)
    # return the sum of all the get calls
    return sum_of_gets


# print(hashMap(queryType, query))

"""
Mean Groups 
-----------
You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

Example

For

a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
the output should be

meanGroups(a) = [[0, 4],
                 [1],
                 [2, 3]]
mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
mean(a[1]) = (4 + 4) / 2 = 4;
mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
mean(a[3]) = (2 + 3) / 2 = 2.5;
mean(a[4]) = (3 + 3 + 3) / 3 = 3.
There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:

Arrays with indices 0 and 4 form a group with mean 3;
Array with index 1 forms a group with mean 4;
Arrays with indices 2 and 3 form a group with mean 2.5.
Note that neither

meanGroups(a) = [[0, 4],
                 [2, 3],
                 [1]]
nor

meanGroups(a) = [[0, 4],
                 [1],
                 [3, 2]]
will be considered as a correct answer:

In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
In the second case, the array at index 2 is not sorted in ascending order.
For

a = [[-5, 2, 3],
     [0, 0],
     [0],
     [-100, 100]]
the output should be

meanGroups(a) = [[0, 1, 2, 3]]
The mean values of all of the arrays are 0, so all of them are in the same group.
"""
a = [[0, 4],
     [2, 3],
     [1]]
a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]


# passing all tests
def meanGroups(a):
    # create dict to hold mean and arrays w that mean
    means = {}
    # iterate outer array
    for i in range(len(a)):
        # get the mean for each inner array
        sum = 0
        for num in a[i]:
            sum += num
        mean = sum / len(a[i])
        # hold array and mean in dictionary
        if mean not in means:
            means[mean] = []
        means[mean].append(i)
    # return the set of each unique mean with first occurring inner array listed first
    result = []
    for mean in means:
        result.append(means[mean])
    return result

print(meanGroups(a))
