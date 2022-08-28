data_festa1 = int(input())
data_festa2 = int(input())
data_festa3 = int(input())

soma_festa = 3

if data_festa1 == data_festa2:
    soma_festa -= 1
if data_festa1 == data_festa3:
    soma_festa -= 1
if data_festa2 == data_festa3:
    soma_festa -= 1
if data_festa1 == data_festa2 and data_festa1 == data_festa3:
    soma_festa = 1


print(soma_festa)
