def check(string_para,numbers,upper,lower,spaces,sp_char):
    for i in range(0,len(string_para)):
        if string_para[i].isnumeric()==True:
            numbers+=1
        if string_para[i].isupper()==True:
            upper+=1
        if string_para[i].islower()==True:
            lower+=1
        if string_para[i]==" ":
            spaces+=1
        sp_char=(len(string_para)-(numbers+upper+lower+spaces))
    print("For the given string \n No. of Numbers: ",numbers,"\n No. of Upper Characters: ",upper,"\n No. of Lower Characters: ",lower,"\n No. of Spaces: ",spaces,"\n No. of Special Characters: ",sp_char)

string_para=input("Enter your String: ")
numbers=upper=lower=spaces=sp_char=0
check(string_para,numbers,upper,lower,spaces,sp_char)