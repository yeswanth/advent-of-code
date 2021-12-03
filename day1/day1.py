f = open('day1.input').read()

arr = [int(i) for i in f.split('\n')[:-1]]
increase = 0
for i,reading in enumerate(arr):
    if i > 0:
        curr = reading
        prev = arr[i-1]
        if curr > prev:
            increase = increase + 1 

print(increase)

prev = 0
increase = 0
for i, reading in enumerate(arr):
    if i+2 < len(arr):
        print(arr[i],arr[i+1],arr[i+2])
        sliding_window = arr[i] + arr[i+1] + arr[i+2]
        if sliding_window > prev and prev != 0:
            increase = increase + 1 
            print sliding_window, prev
            print "Increase"
        prev = sliding_window 
print(increase)
    

