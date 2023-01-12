import copy             # importuję potrzebne biblioteki
import random

def quicksort(I:list):  # funkcja odpowiedzialna za algorytm quicksort
    if isinstance(I, str):  #sprawdzam, czy funkcja nie dostała danych tekstowych
        return None

    I2 = copy.deepcopy(I)   #tworzę kopię danych wejściowych, by algorytm nie wariował w trakcie sortowania
    start = 0               #ustawiam parametry startowe, które sę indeksami pierwszego i ostatniego elementu
    stop = len(I2)-1
    
    def quicksort_inplace(input_array, start, stop):    # właściwa funkcja sortowania szybkiego
        i = start
        j = stop
        pivot = input_array[random.randint(start, stop)]    #liczę pivot w sposób losowy
        while i < j:    # pętla sortująca
            while input_array[i] < pivot:
                i = i + 1
            while input_array[j] > pivot:
                j = j - 1
            if i <= j:
                input_array[j], input_array[i] = input_array[i], input_array[j] #zamiana elementów miejscami
                i = i + 1
                j = j - 1
        if start < j:
            quicksort_inplace(input_array, start, j)
        if i < stop:
            quicksort_inplace(input_array, i, stop)
        return input_array #jeśli wszystko zostanie posortowane, zwracam wartość
            
    return quicksort_inplace(I2, start, stop)

def quicksort_descending(I:list):   #funkcja odpowiedzialna za odwrócenie posortowanej listy, by uzyskać sortowanie malejące
    sorted = quicksort(I)
    sorted.reverse()
    return sorted