from random import choice

def random_heading_color(function):
    def wrapper(*args, **kwargs):
        # print(args)
        # print(kwargs["guess"])
        # print(function(*args, **kwargs))
        
        color_list = ["purple", "yellow", "orange", "green", "pink", "brown"]
        random_color = choice(color_list)
        
        return f'<h1 style="color:{random_color};">' + function(*args, **kwargs)
    return wrapper