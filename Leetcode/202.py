# Happy number


class Solution:

    def isHappy(self, n):
        '''Determine whether a number is 'happy'.

        For a positive integer, replaces it with the sum of square
         of its digits until 1. If cannot become 1, it's not happy.

        Parameters
        ----------
        n : {[integer]}
                input number.
        '''
        def rep(n):
            sos = []
            for i in range(1, len(str(n)) + 1):
                d = n % 10**i
                sos += d**2
            return sos

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = rep(n)

        return n == 1

    def isHappy_2(self, n):
        '''Determine whether a number is 'happy'.

        The iteration forms an implicit list. 
        Track the loop with fast and slow pointers.

        Parameters
        ----------
        n : {[integer]}
                input number.
        '''
        def get_next(n):
            sos = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sos += digit ** 2
            reutrn sos

            slow = n
            fast = get_next(n)
            while fast != 1 and slow != fast:
                slow = get_next(slow)
                fast = get_next(get_next(fast))
            return fast == 1
