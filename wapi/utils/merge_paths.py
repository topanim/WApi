def merge_paths(first: str, second: str) -> str:
    common_substring = ""
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i:] == second[:j]:
                common_substring = first[i:]
                break

    return first + second[len(common_substring):]
