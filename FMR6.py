#filter() Map() Reduce()
#Python Applicaion which contain list of numbers from user. filter function should filter out
# all such numbers which are even. map function will calculate increment by 2. and Reduce
#will return Addition of that numbers.
# Helper function in the form of lambda function
# step 5


CheckEven = lambda No:(No % 2 == 0)

Doubles = lambda No:No*2

Sum = lambda A,B :A+B

def filterx(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No)== True):
            Result.append(No)
    return Result

def mapx(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result

def reducex(Helper_Function,Data):
    Ans = 0
    for No in Data:
        Ans = Helper_Function(Ans,No)

    return Ans


def main():
    print("Enter number of elements you want to enter :")
    isize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    Data_Filter = filterx(CheckEven, Data_Input)
    print("Data after filter is :",Data_Filter)

    Data_Map = mapx(Doubles,Data_Filter)
    print("Data after map is :", Data_Map)

    Output = reducex(Sum,Data_Map)
    print("Result after reduce is :", Output)


if __name__ == "__main__":
    main()
