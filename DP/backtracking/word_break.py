"""
Given a valid sentence without any spaces between the words and a dictionary of valid 
English words, find all possible ways to break the sentence in individual dictionary words.

{ i, like, sam, sung, samsung, mobile, ice, 
  and, cream, icecream, man, go, mango}

Input: "ilikesamsungmobile"
Output: i like sam sung mobile
        i like samsung mobile
"""


#######solved own##################

class Solution:

    def word_break(self, string, p, dictionary, output):

        if p == len(string):
            print(" ".join(output))
            return

        for i in range(p, len(string)):
            word = string[p: i + 1]

            if word in dictionary:
                output.append(word)
                self.word_break(string, i + 1, dictionary, output)

                output.pop()

    def driver(self, string, dictionary):
        self.word_break(string, 0, dictionary, [])


main_dict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice",
             "and", "cream", "icecream", "man", "go", "mango"}

Solution().driver("ilikeicecreamandmango", main_dict)
