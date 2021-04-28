def init():
        while True:
                print('Do you want to read or write on a file?')
                mode = input().lower()
                if mode in ['read', 'r', 'write', 'w']:
                        return mode
                else:
                        print('Enter either "read" or "r" or "write" or "w".')
def get_info(num):
        info = []
        for i in range(num):
                print("**********************************")
                ID = int(input("Enter ID: "))
                name = input("Enter Name: ")
                salary = input("Enter Salary: ")
                info.append([ID,name,salary])
                write_file(info)
                info.clear()
        return info

def write_file(info):
        file = open("Document.txt","a")
        file.write("ID: {} ".format(info[0][0]))
        file.write("Name: {} ".format(info[0][1]))
        file.write("Salary: {} ".format(info[0][2]))
        file.write("\n")
        file.close()

def read_file():
        readFile =  open("Document.txt","r")
        data = readFile.readlines();
        print("Here is the data entries:")
        for i in data:
                print(i)

def main():
        if mode in ['write','w']:
                num = int(input("How many entries you want: "))
                get_info(num)
        if mode in ['read','r']:
                read_file()

mode = init()
main()