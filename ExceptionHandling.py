a = 5
#b = 0
b = 2

try:
    print("Resource Opened")
    print(a/b)
    k = int(input("Enter a number : "))
    print(k)
#except Exception:
    #print("Hey, you cannot divide by Zero")
#except Exception as e:  #Common exception
#    print("Hey, you cannot divide by Zero,",e)
except ZeroDivisionError:   #We can specify the exception as well
    print("Hey, you cannot divide by Zero")

except ValueError:
    print("Invalid Input")

except Exception:   #In case we do not know the exception to specify.
    print("Something Went Wrong")

finally:    #Prints the statement even though above one failed or passed
    print("Resource Closed")

