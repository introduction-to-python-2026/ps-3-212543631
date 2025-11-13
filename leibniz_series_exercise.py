def approximate_pi(n_terms):
    list_of_numbers = []
    sum = 0
    for i in range(n_terms):
        list_of_numbers.append(i)
        list_of_numbers[i] = ((-1)**i)/(2*i+1)
        sum += list_of_numbers[i]
    return sum


        


