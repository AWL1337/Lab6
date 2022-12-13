def calc(input_string):
    try:
        return eval(input_string)
    except:
        return "ERROR"

def main():
    inp = input()
    calc(inp)

if __name__ == "__main__":
    main()
