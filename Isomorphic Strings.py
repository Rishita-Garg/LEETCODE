# 205. Isomorphic Strings

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map, t_map = {}, {}
    for c1, c2 in zip(s, t):
        if s_map.get(c1, c2) != c2 or t_map.get(c2, c1) != c1:
            return False
        s_map[c1] = c2
        t_map[c2] = c1
    return True

# Example
print(isIsomorphic("egg", "add"))  # True
