#filter() Map() Reduce() using lambda function.
#Python Applicaion which contain list of numbers from user. filter function should filter out
# all such numbers which are even. map function will calculate increment by 2. and Rrduce
#will return Addition of that numbers.
# step 7


from functools import reduce


def main():
    print("Enter number of elements you want to enter:")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data")
    for iCnt in range(0,iSize,1):
        value = int(input())
        Data_Input.append(value)


    print("Data is :",Data_Input)

    Data_Filter = list(filter(lambda No:(No % 2 == 0),Data_Input))

    print("Data after filter is :",Data_Filter)

    Data_Map = list(map(lambda No :No*2,Data_Filter ))

    print("Data after map is :", Data_Map)

    Output = reduce(lambda A,B: A+B,Data_Map)

    print("Result after reduce is :",Output)

if __name__ == "__main__":
    main()