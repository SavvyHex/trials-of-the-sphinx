def make_fair(ini_ans:float) -> str:
    ans = str(ini_ans)
    if(len(ans)>5):
        ans = ans[:5]
    return float(ans)