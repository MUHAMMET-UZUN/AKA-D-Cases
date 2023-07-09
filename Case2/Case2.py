import time


print("Write your name as fast as possible.")
print("\n3")
time.sleep(1)
print("\n2")
time.sleep(1)
print("\n1")
time.sleep(1)
print("\nSTART!\n")

start_time = time.time()
inp = input()
end_time = time.time()

if end_time - start_time < 1:
    print("WOW, you are so fast!")
    print("\nYour time is {} seconds".format(end_time - start_time))

elif end_time - start_time < 2:
    print("Really fast!")
    print("\nYour time is {} seconds".format(end_time - start_time))

elif end_time - start_time < 3:
    print("So Good!")
    print("\nYour time is {} seconds".format(end_time - start_time))

else:
    print("You are slow!")
    print("\nYour time is {} seconds".format(end_time - start_time))
