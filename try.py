for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, "--> Division by zero is not allowed!")
    except NameError:
        print("Name Error")
    except:
        print(e, "Error!")

