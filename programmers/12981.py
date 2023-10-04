def solution(n, words):
    last = ''
    s = set()
    for i,word in enumerate(words):
        if last != '' and (last != word[0] or (word in s)):
            # wrong
            return [i%n+1, i//n+1]
        
        s.add(word)
        last = word[len(word)-1]

    return [0,0]
ql = [
    [3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]],
    [5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]],
    [2,["hello", "one", "even", "never", "now", "world", "draw"]]
]

for q in ql:
    print(solution(*q))