alpha = 1
beta = 3

CHOSUNGS = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONGSUNGS = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONGSUNGS = [u'',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']

NUM_CHOSUNGS = 19
NUM_JOONGSUNGS = 21
NUM_JONGSUNGS = 28

FIRST_HANGUL_UNICODE = 0xAC00 #'가'
LAST_HANGUL_UNICODE = 0xD7A3 #'힣'

def decompose(hangul_letter):
    """This function returns letters by decomposing the specified Hangul letter."""
    dec = ord(hangul_letter)
    if ord('ㄱ') <= dec and dec <= ord('ㅎ'):
        return (hangul_letter, '', '')

    if ord('ㅏ') <= dec and dec <= ord('ㅣ'):
        return ('', hangul_letter, '')

    code = ord(hangul_letter) - FIRST_HANGUL_UNICODE
    jongsung_index = int(code % NUM_JONGSUNGS)
    code /= NUM_JONGSUNGS
    joongsung_index = int(code % NUM_JOONGSUNGS)
    code /= NUM_JOONGSUNGS
    chosung_index = int(code)

    return (CHOSUNGS[chosung_index], JOONGSUNGS[joongsung_index], JONGSUNGS[jongsung_index])


def SEO(c1, c2):
    p_list1 = decompose(c1)
    p_list2 = decompose(c2)

    diff_count = 0
    for i in range(3):
        if p_list1[i] != p_list2[i]:
            diff_count = diff_count + 1

    if diff_count == 3:
        return beta

    else:
        return alpha * diff_count

def get_SED(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    dp = [[0]*(len2+1) for i in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            dp[i][j] = -1

    def SED(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0:
            return j * beta

        if j == 0:
            return i * beta

        v1 = SED(i, j-1) + beta
        v2 = SED(i-1, j) + beta
        v3 = SED(i-1, j-1) + SEO(s1[i-1], s2[j-1])
        m = min(v1, v2, v3)
        dp[i][j] = m

        return m

    return SED(len1, len2)
