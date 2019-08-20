class MaxStack:
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.trackMax = []

    def push(self, val):
        # Fill this in.
        self.stack.append(val)
        temp_max = val if len(self.trackMax) == 0 else self.trackMax[-1]
        if val < temp_max:
            self.trackMax.append(temp_max)
        else:
            self.trackMax.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return
        # Fill this in.
        self.stack.pop()
        self.trackMax.pop()

    def max(self):
        # Fill this in.
        return self.trackMax[-1] if len(self.trackMax) != 0 else None
