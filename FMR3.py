
# filter() function
# # Python Applicaion which contain list of numbers from user. filter function should filter out
# # all such numbers which are even.
# step 2

def CheckEven(No):  #Helper function
    return (No % 2 == 0)


def filterx(Helper_Function,Data):
    Result = []
    for no in Data:
        if(Helper_Function(no)== True):
            Result.append(no)
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


if __name__ == "__main__":
    main()
