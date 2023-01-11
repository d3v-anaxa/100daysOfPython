# 'finally' keyword is used incase there is a return value inside try/catch of any function ot execute a compulsory program statement
# NOTE : using 'finally' keyword the return value always returns in the end

def fun(index):
    try:
        li = [0b101, 0o341, 0b1110, 0xaa1]
        index %= len(li) # int(input("Enter index : ")) % len(li)
        return li[index]
    except Exception as e:
        print(f"Exception : {e}")
        return -1
    finally:
        print('''Code inside finally keyword is always executed''')

    print("printline outside try-catch-finally")

#print(fun(0))
print(fun("string_input"))
