def decFuncToAddString(targetFunc):
    def wrapper():
        print("Passed: " + targetFunc() + ", and decorated it!")
    return wrapper

@decFuncToAddString
def sampleFunc():
    return 'string'

def main():
    print('Peassing something to decorator:')
    sampleFunc()

main()