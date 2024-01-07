
#Application which  gives a list of numbers from user.
# step1


def main():
    print("Enter number of elements you want to enter?:")
    isize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)


if __name__ == "__main__":
    main()
