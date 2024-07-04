def programToLaunch(fileExtn):
    if fileExtn == ".gif":
        print("image/gif")
    elif fileExtn == ".jpeg":
        print("image/jpeg")
    elif fileExtn == ".jpg":
        print("image/jpeg")
    elif fileExtn == ".png":
        print("image/png")
    elif fileExtn == ".pdf":
        print("application/pdf")
    elif fileExtn == ".txt":
        print("text/plain")
    elif fileExtn == ".zip":
        print("application/zip")
    elif fileExtn == ".bin":
        print("application/octet-stream")
    else:
        print("application/octet-stream")

# !!! match only works in python3.10 and above !!! 
# def programToLaunch(fileExtn):
#     match fileExtn:
#         case ".gif":
#             print("image/gif")
#         case ".jpeg":
#             print("image/jpeg")
#         case ".jpg":
#             print("image/jpeg")
#         case ".png":
#             print("image/png")
#         case ".pdf":
#             print("application/pdf")
#         case ".txt":
#             print("text/plain")
#         case ".zip":
#             print("application/zip")
#         case _:
#             print("Well, well, well... how did you get in this place first")

def main():
    fileExtn = ""
    fileName = input("Enter File Name with extension: ").strip()

    # while True:
    #     fileName = input("Enter File Name with extension: ").strip()
    #     if "." not in fileName or fileName[(fileName.rfind('.')):].casefold() not in [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip",".bin"]:
    #         continue
    #     else:
    #         break

    fileExtn = fileName[(fileName.rfind('.')):].casefold()
    #print("fileType - ", fileExtn)
    programToLaunch(fileExtn)

main()