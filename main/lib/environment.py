
class ENVIRONMENT:
    def __init__(self, filename):
        self.filename = filename
        self.env_vars = dict()
        with open(filename) as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                key, value = line.strip().split('=', 1)
                self.env_vars[key] = value

    def read(self, key):
        return self.env_vars[key]
