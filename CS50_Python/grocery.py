def main():
    d = {}
    while True:
        try:
            item = input("")
            if d[item] != item:
                # If item in dict. d, then add to its total frequency
                d[item] += 1
        except EOFError:
            l = sorted(d)
            for item in l:
                print(d[item], item.upper())
            break
        except KeyError:
            # If item is not in dict. d then stores this new item with int. 1
            d[item] = 1
main()
