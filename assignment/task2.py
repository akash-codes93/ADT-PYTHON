def solution(AA, AB, BB):
    mem = {}

    def dfs(aa, ab, bb, prev_state):

        if (aa, ab, bb, prev_state) in mem:
            return mem[(aa, ab, bb, prev_state)]

        string1 = ""
        string21 = ""
        string22 = ""
        string31 = ""
        string32 = ""

        if prev_state == 'AA':
            if bb > 0:
                string1 = 'BB' + dfs(aa, ab, bb - 1, 'BB')

        if prev_state == 'BB':
            if aa > 0:
                string21 = 'AA' + dfs(aa - 1, ab, bb, 'AA')

            if ab > 0:
                string22 = 'AB' + dfs(aa, ab - 1, bb, 'AB')

        if prev_state == 'AB':
            if aa > 0:
                string31 = 'AA' + dfs(aa - 1, ab, bb, 'AA')
            if ab > 0:
                string32 = 'AB' + dfs(aa, ab - 1, bb, 'AB')

        max_str = sorted([string1, string21, string22, string31, string32], key=lambda x: len(x))[-1]
        mem[(aa, ab, bb, prev_state)] = max_str
        return max_str

    s1 = ""
    s2 = ""
    s3 = ""

    if AA > 0:
        s1 = 'AA' + dfs(AA - 1, AB, BB, 'AA')
    if AB > 0:
        s2 = 'AB' + dfs(AA, AB - 1, BB, 'AB')
    if BB > 0:
        s3 = 'BB' + dfs(AA, AB, BB - 1, 'BB')

    return sorted([s1, s2, s3], key=lambda x: len(x))[-1]


print(solution(100, 100, 100))




