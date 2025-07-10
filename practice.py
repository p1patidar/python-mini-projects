#get prime numbers between 1 and 1000
def get_prime_numbers(limit):
    return [x for x in range(2,limit) if all(x%i!=0 for i in range(2,int(x**0.5)+1))]

# print(get_prime_numbers(100))

def get_prime_numbers(limit):
    """Returns a list of prime numbers up to the specified limit."""
    primes = []
    for num in range(2, limit ):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
# print(get_prime_numbers(100))
def enumaration():
    lst = ['apple', 'banana', 'cherry']
    for i in range(len(lst)):
        print(i,lst[i])
    for index, value in enumerate(lst):
        print(index,value)

# print(enumaration)

# zip(): Combine multiple lists together


def zip_file():
    names = ['pawan', 'rahul', 'deepak']
    scores = [85, 90, 78]
    combined_lst=[]
    for name, score in zip(names, scores):
        print(name, score)
        combined_lst.append(name).append(score)
        # combined_lst.append(score)


    return combined_lst

# print(zip_file())

# 🔁 3. map(): Apply a function to every item in a list

def map_f():
    nums = [1, 2, 3, 4]
    # squred_num=[num**2 for num in range(len(nums))]
    # squred_num=list(map(lambda x:x**2 ,nums))
    squred_num=list(map(lambda x:x**2 ,nums))
    print(squred_num)



# map_f()

def filters():
    nums = [10, 15, 20, 25]
    even_nums=list(filter(lambda x:x%2==0,nums))
    print(even_nums)

# filters()

# ⚡ 5. lambda: Anonymous (nameless) one-liner functions
def oneliner_lambda():
    square=lambda x:x**2
    print(square(2))
# oneliner_lambda()

# Combine with map / filter 

def lambda_map():
    nums = [2, 4, 6]
    doubled=list(map(lambda x:x*2,nums))
    print(doubled)

# lambda_map()

# 💡 Challenge 1: Inverting a Dictionary
def invert_dict():
    employee_dept = {
    'Pawan': 'Sales',
    'Ravi': 'Marketing',
    'Sneha': 'HR'
        }
    # inverted={}
    # for key, value in employee_dept.items():
    #     inverted[value]=key
    inverted={v:k for k,v in employee_dept.items()}

    
    print(inverted)

# invert_dict()

# Bonus challenge

def invert_smarts():
    dict={
    'Pawan': 'Sales',
    'Ankit': 'Sales',
    'Sneha': 'HR'
    }
    invert_smart={}
    for k,v in dict.items():
        if v not in invert_smart:
            invert_smart[v]=[k]
        else:
            invert_smart[v].append(k)
    print(invert_smart)

# invert_smarts()

# 💡 Challenge 2: Creating Quick Lookups
def conv_to_dict_for_quick_lookup():
    stocks = [
        ('RELIANCE', 2850),
        ('TCS', 3750),
        ('INFY', 1600),
        ('HDFCBANK', 1720)
    ]
    stock_dict={i:v for i,v in stocks}

        
    print(stock_dict['TCS'])

# conv_to_dict_for_quick_lookup()


# 💡 Challenge 3: Transforming Key-Value Pairs

def convert_it_to_10():
    marks = {
        'Pawan': 88,
        'Ravi': 77,
        'Sneha': 95
    }
    marks_updated={k:v/10 for k,v in marks.items()}
    print(marks_updated)

# convert_it_to_10()

# combo challenge

def combo_challenge():
    students = ['Pawan', 'Ravi', 'Sneha', 'Amit']
    math_scores = [88, 77, 95, 65]
    science_scores = [92, 81, 89, 70]
    # updatd_dict={}
    # # for v in students:
    # i=0
    # for x,y in zip(math_scores,science_scores):
    #     updatd_dict[students[i]]={"Math":x,'Science':y}
    #     i=i+1
    updated_dict={st:{"Math":m,"Science":s} for st,m,s in zip(students,math_scores,science_scores)}


    print(updated_dict)

# combo_challenge()
