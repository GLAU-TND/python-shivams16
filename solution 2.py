try:
    n=int(input())
    b=int(input())
    a=input()
    c=n+b
    l=a+b
    n.append(3)
except ValueError:
    raise ValueError("value error occured")
except TypeError:
    raise TypeError("type Error occured")
except:
    raise AttributeError("Attribute error occured")