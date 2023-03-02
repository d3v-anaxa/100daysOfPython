import os
path = "./"
string = str(input("Enter extension name [txt, png, jpg] : ")).lower()
raw_file_list = os.listdir(path)
directory_file_list = list(filter(lambda x : x.split(".")[-1] == string, raw_file_list))

def rename(string):
    file_count = 0
    for index in range(len(directory_file_list)):
        if(directory_file_list[index].split(".")[-1] == string):
            try:
                print(f"Renamed \"{directory_file_list[index]}\" to \"{index+1}.{string}\" successfully!")
                os.rename(directory_file_list[index], f"{index+1}.{string}")
                file_count+=1
            except Exception:
                print("Rename unsuccessfull")
    else:
        print(f"0 file found with {string} extension" if file_count == 0
              else f"{file_count} files renamed successfully!")


rename(string)
