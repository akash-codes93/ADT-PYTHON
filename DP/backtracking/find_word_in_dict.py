"""
i/p: catsanddog
dict: ["cat", "cats", "dog", "and", "sand"]
o/p: cats and dog
     cat sand dog
"""
from typing import List


class Solution:

    # def divide_string(self, string: str, divisions: int) -> List[str]:
    #
    #     if divisions == 1:
    #         return [string]
    #
    #     if divisions >= len(string):
    #         return [s for s in string]
    #
    #     result = ["" for _ in range(0, divisions)]

    def get_valid_sentences2(self, string, dictionary, output):
        """better approach"""
        if not string:
            print(output)
            return

        for i in range(len(string)):
            _str = string[:i+1]
            res_str = string[i+1:]

            if _str in dictionary:
                output.append(_str)
                self.get_valid_sentences2(res_str, dictionary, output)
                output.pop()

    def get_valid_sentences(self, string: str, dictionary: List[str]) -> List[List[str]]:
        output = []
        result = ""
        for i in range(0, len(string)):
            result += string[i]

            if result in dictionary:
                sub_output = [result]
                op = self.get_valid_sentences(string[i + 1:], dictionary)

                for _ in op:
                    for __ in _:
                        sub_output.append(__)

                output.append(sub_output)

        return output

    def words_spelled_periodic(self, string: str, dictionary: List[str]) -> List[str]:

        output = self.get_valid_sentences(string, dictionary)
        result = []
        for out in output:
            out = list(map(lambda x: x.title(), out))
            s = "".join(out)
            if len(s) == len(string):
                result.append(s)

        return result


# print(Solution().get_valid_sentences("catsanddog", ["cat", "cats", "dog", "and", "sand"]))
# print(Solution().get_valid_sentences2("catsanddog", ["cat", "cats", "dog", "and", "sand"], []))
print(Solution().get_valid_sentences2("cacaneni", ["ca", "ni", "ne", "caca"], []))
# print(Solution().words_spelled_periodic("cacaneni", ["ca", "ni", "ne", "caca"]))
