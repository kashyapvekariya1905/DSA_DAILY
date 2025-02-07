class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # balls = [0] * (limit + 1)
        # colors = {}
        # result = []
        # for ball, color in queries:
        #     if balls[ball] != color:
        #         if balls[ball] in colors:
        #             colors[balls[ball]] -= 1
        #         if color in colors:
        #             colors[color] += 1
        #         else:
        #             colors[color] = 1
        #         balls[ball] = color

        #     distinct_colors = sum(1 for count in colors.values() if count > 0)
        #     result.append(distinct_colors)

        # return result

        b_colors = {}
        col_count = {}
        dis_colors = set()
        res = []

        for x, y in queries:
            if x in b_colors:
                old_color = b_colors[x]
                col_count[old_color] -= 1
                if col_count[old_color] == 0:
                    dis_colors.remove(old_color)

            b_colors[x] = y
            if y in col_count:
                col_count[y] += 1
            else:
                col_count[y] = 1
            dis_colors.add(y)
            
            res.append(len(dis_colors))
        
        return res
