
def http_error(status):
    match status:
        case 400:
            print("Invalid status")
        case 401:
            print("token expired")
        case 500:
            print("Internal error")
        case _:
            print("Unknown error")

http_error(600)

