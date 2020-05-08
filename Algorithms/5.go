// Dynamic Programming

func longestPalindrome(s string) string {
	n := len(s)

	if n <= 1 {
		return s
	}

	dp := make([][]bool, n)

	start := 0
	maxlen := 1

	for r := 0; r < n; r++ {
		dp[r] = make([]bool, n)
		dp[r][r] = true
		for l := 0; l < r; l++ {
			if s[l] == s[r] && (r - l <= 2 || dp[l+1][r-1]) {
				dp[l][r] = true
			} else {
				dp[l][r] = false
			}

			if dp[l][r] {
				cur := r-l+1
				if cur > maxlen {
					maxlen = cur
					start = 1
				}
			}
		}
	}
	return s[start:start+maxlen]
}