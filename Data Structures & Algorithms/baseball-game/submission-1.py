class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == "C" and res != [] :
                res.pop()
            elif op == "D" and res != [] :
                dub = 2 * res[-1]
                res.append(dub)
            elif op == "+" and len(res) > 1 :
                add = res[-1] + res[-2]
                res.append(add)
            else:
                res.append(int(op))
        return sum(res)

        