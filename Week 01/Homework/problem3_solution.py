import heapq

"""
Interviewbit
Magician and Chocolates
link: https://www.interviewbit.com/problems/magician-and-chocolates/

Problem Dsecription:
	Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i,
	eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.
	Find the maximum number of chocolates that kid can eat in A units of time.
	NOTE: 
		floor() function returns the largest integer less than or equal to a given number.
		Return your answer modulo 10^9+7

Problem Constraints:
	1 <= A <= 10^5
	1 <= |B| <= 10^5
	1 <= Bi <= INT_MAX

Example Input:
	Input 1:
	A = 3
	B = [6, 5]
	Input 2:
	A = 5
	b = [2, 4, 6, 8, 10]

Example Output:
	Output 1:
	14
	Output 2:
	33
"""

# @param a : integer
# @param b : list of integers
# @return an integer
def nchoc(A, B):
	pq = [-b for b in B]
	heapq.heapify(pq)
	sol = 0
	mod = 10 ** 9 + 7
	for _ in range(A):
		el = -heapq.heappop(pq)
		sol += el
		sol %= mod
		heapq.heappush(pq, -(el // 2))
	return sol
	
if __name__ == "__main__":
	print(nchoc(10, [2147483647, 2000000014, 2147483647]))
			