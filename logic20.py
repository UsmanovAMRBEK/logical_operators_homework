def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    n1=n%10
    n=n//10

    n2=n%10
    n=n//10

    n3=n%10
    n=n//10

    n4=n%10
    n=n//10

    n5=n%10
    n=n//10
    one=0;zero=0
    if n1==1:
        one+=1
    if n2==1:
        one+=1
    if n3==1:
        one+=1
    if n4==1:
        one+=1
    if n5==1:
        one+=1
    zero=5-one
    return one>zero
print(main(1100))