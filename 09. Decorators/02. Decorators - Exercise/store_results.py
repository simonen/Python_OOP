class store_results:
    _logfile = 'out.log'
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = f"Function {self.func.__name__} was called. Result: {self.func(*args)}"
        with open(self._logfile, 'a') as open_file:
            open_file.write(log_string + '\n')
        return self.func(*args)


@store_results
def add(a, b):
    return a + b