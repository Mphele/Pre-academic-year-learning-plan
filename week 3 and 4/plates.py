def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    bad_char =". !():;_-,"
    error_counter =0
    if len(s) < 2 or not (s[0].isalpha() and s[1].isalpha()):
        error_counter +=1
    if len(s)<2 or len(s)>6 :
        error_counter +=1

    for char in s:
        if char in bad_char:
            error_counter +=1
            break

    for char in s:
        if char.isdigit():
            if char =="0":
                error_counter +=1
            break

    num_detect = 0
    for char in s:
        if char.isdigit():
            num_detect = 1
        if char.isalpha() and num_detect ==1:
            error_counter +=1
            break

    if error_counter >0:
        return False
    else:
        return True



main()
