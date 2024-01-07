#filter() Map() Reduce() using lambda function.
#Python Applicaion which contain list of numbers from user. filter function should filter out
# all such numbers which are even. map function will calculate increment by 2. and Rrduce
#will return Addition of that numbers.
# step 6


from functools import reduce

CheckEven = lambda No:(No % 2 == 0)

Doubles = lambda No:No*2

Sum = lambda A,B :A+B



def main():
    print("Enter number of elements you want to enter :")
    isize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    Data_Filter = list(filter(CheckEven, Data_Input))
    print("Data after filter is :",Data_Filter)

    Data_Map = list(map(Doubles,Data_Filter))
    print("Data after map is :", Data_Map)

    Output = reduce(Sum,Data_Map)
    print("Result after reduce is :", Output)


if __name__ == "__main__":
    main()
