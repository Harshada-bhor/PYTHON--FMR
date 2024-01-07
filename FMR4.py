
# filter() , Map() function
#Python Applicaion which contain list of numbers from user. filter function should
# filter out all such numbers which are even. map function will calculate increment by 2.
# step 3


def CheckEven(No):
    return (No % 2 == 0)

def Doubles(No):
    return No*2

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


if __name__ == "__main__":
    main()
