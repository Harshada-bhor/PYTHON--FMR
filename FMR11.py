
#filter() Map() Reduce() using lambda function.
#Python Applicaion which contain list of numbers from user. filter function should filter out
# all such numbers which are prime. map function will multiply each number by 2.
# and Reduce will return Maximum number from that numbers.


from functools import reduce


def main():
    print("Enter number of elements you want to enter:")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data")
    for i in range(0,iSize,1):
        value = int(input())
        Data_Input.append(value)


    print("Data is :",Data_Input)

    Data_Filter = list(filter(lambda No:(No % i != 0),Data_Input))

    print("Data after filter is :",Data_Filter)

    Data_Map = list(map(lambda No :No*2,Data_Filter ))

    print("Data after map is :", Data_Map)

    Output = reduce(lambda A,B: max(A,B),Data_Map)

    print("Result after reduce is :",Output)

if __name__ == "__main__":
    main()