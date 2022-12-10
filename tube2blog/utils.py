def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def find_type(key,value,iter):
    filter_func = lambda x: x.get(key) == value
    return next(filter(filter_func(), iter), None)