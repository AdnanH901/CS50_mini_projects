def main():
    name_list = []
    while True:
        try:
            name_input = input("Name: ")
            name_list.append(name_input)
        except EOFError:
            adieu_text = "Adieu, adieu, to"
            l = len(name_list)
            if l == 1:
                adieu_text += f" {name_list[0]}"
            elif l == 2:
                adieu_text += f" {name_list[0]} and {name_list[1]}"
            else:
                for i in range(l - 1):
                    adieu_text += f" {name_list[i]},"
                adieu_text += f" and {name_list[len(name_list)-1]}"
            print(adieu_text)
            break
main()
