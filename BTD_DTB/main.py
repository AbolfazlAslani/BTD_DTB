from BTD import binary_to_decimal
from DTB import decimal_to_binary
cmd = ">"
user_input = input(f"If you want to convert binary to decimal please type in BTD \nand if you want to convert decimal to binary please type in DTB {cmd} ")
while user_input != "BTD" and user_input != "DTB":
    print("don't forget to type in with uppercase and don't type anything else please try again options = <BTD> and <DTB>")
    user_input = input(f"{cmd} ")
if user_input == "BTD" :
    btd_input = input(f"Allright you want to convert binary to decimal\nplease type in your binary digits {cmd} ")
    print(binary_to_decimal(btd_input))
elif user_input =="DTB" :
    dtb_input = input(f"Allright you want to convert decimal to binary\nplease type in your decimal digits {cmd} ")
    print("Your Answer is : ", decimal_to_binary(int(dtb_input)))