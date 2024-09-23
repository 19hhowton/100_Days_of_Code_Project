
# @make_bold "<b></b>"
# @make_emphasis "<em></em>"
# @make_underlined "<u></u>"

def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        result = function()
        return f"<em>{result}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        result = function()
        return f"<u>{result}</u>"
    return wrapper

