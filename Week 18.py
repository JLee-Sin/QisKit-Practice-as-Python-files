import numpy as np
import matplotlib.pyplot as plt

list_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
search_choice = 13
number_queries = 0
for choice in list_choices:
    number_queries += 1
    if choice == search_choice:
        print("13 has been found. It was found at position", number_queries)
        break

list_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
number_queries = 0
search_choice = 13
N = len(list_choices)
lower = 0
upper = N - 1
for choice in list_choices:
    mid = int((lower + upper) / 2)
    number_queries += 1
    if list_choices[mid] > search_choice:
        upper = mid
    elif list_choices[mid] < search_choice:
        lower = mid
    else:
        print(str(search_choice) + " was found at position " + str(mid))
        break


N = np.arange(1,100) # Creating different dataset sizes
plt.semilogy(N,N)
plt.semilogy(N,np.log(N))
#plt.semilogy(N,np.pi/4*np.sqrt(N))
plt.xlabel("size of dataset")
plt.ylabel("big O complexity")
plt.legend(["linear", "binary"])