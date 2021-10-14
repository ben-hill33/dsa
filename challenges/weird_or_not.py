def weird_not_weird(n):
    nums = []
# If n is odd, print Weird
    if n % 3 == 0:
        print("Weird")
# If n is even and in the inclusive range of 2 to 5, print Not Weird
    if n % 2 == 0 and n <= 5:
        print("Not Weird")
# If n is even and in the inclusive range of 6 to 20, print Weird
    if n % 2 == 0 and n in range(nums[6:20]):
        print(nums)
        print("Weird") 
# If n is even and greater than 20, print Not Weird

if __name__ == "__main__":
    num = int()
    weird = weird_not_weird(num=6)
    print(weird)
