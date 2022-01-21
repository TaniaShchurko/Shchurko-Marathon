import inspect

def logger(func):
    def wrapper(*args, **kwargs):
        f=func(*args, **kwargs)
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        result=""
        if 'args' in func_args.keys():
            for i in func_args['args']:
                result+=str(i)+", "
            func_args.pop('args')
        if 'kwargs' in func_args.keys():
            for i in func_args['kwargs']:
                result+=str(func_args['kwargs'][i])+", "
            func_args.pop('kwargs')
        if len(func_args)>0:
            for i in func_args.keys():
                result += str(func_args[i]) + ", "
        if f == None:
            print(f"Executing of function {func.__qualname__} with arguments {result[:-2]}...")
        else:
            print(f"Executing of function {func.__qualname__} with arguments {result[:-2]}...")
            return f
    return wrapper

@logger
def sum(a,b):
    return a+b


@logger
def print_arg(arg):
    print(arg)

@logger
def concat(*args,**kwargs):
    sum=""
    for i in args:
        sum += str(i)
    for i in kwargs.values():
        sum += str(i)
    return sum