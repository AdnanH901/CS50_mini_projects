def main():
    file = input("File name: ").strip()
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf") or file.endswith(".PDF"):
        print("application/pdf")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()
