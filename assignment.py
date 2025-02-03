def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"
name,age=input("enter name and age separated by comma").split(",")   
print(format_string(name,age))    
    

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number>10:
        return f"Greater"
    elif number<10:
        return f"lesser"
    else:
        return f"Equal"
number=input("Enter a number") 
print(conditional_check(int(number)))   

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("Enter value of n"))  
print(loop_sum(n))      


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total_sum=sum(numbers)
    max_val=max(numbers)
    min_val=min(numbers)
    return (total_sum,max_val,min_val)
numbers=[1,2,3,4,8]
print(list_operations(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    high_scorers=[]
    for names,scores in students_dict.items():
        if scores>80:
            high_scorers.append(names)
    return high_scorers
students_dict={'Birendra':95,"Hari":60,'Sita':86,'Rita':90,"Deepa":50

               }
print(dict_operations(students_dict))

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1)& set(list2)
list1=[2,3,4,6,8]
list2=[2,3,4,9,6]
print(set_operations(list1,list2))

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {'Addition':a+b,
            "Subtraction":a-b,
            'Multiplication':a*b,
            'Division':a/b

           }
a=10
b=5
print(arithmetic_ops(a,b))

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "AND": x and y,  
        "OR": x or y,  
        "NOT x": not x,  
        "NOT y": not y,
        "XOR": x ^ y  
    }

x = True
y = False
print(logical_ops(x, y))

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "AND": a and b,  
        "OR": a or b,  
        "NOT a": not a,  
        "NOT b": not b,
        "XOR": a ^ b  
    }

a = 5
b = 7
print(bitwise_ops(a, b))