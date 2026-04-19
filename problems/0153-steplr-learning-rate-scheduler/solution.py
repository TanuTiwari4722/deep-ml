class StepLRScheduler:
    def __init__(self, initial_lr, step_size, gamma):
        # Initialize initial_lr, step_size, and gamma
        self.initial_lr = initial_lr
        self.step_size = step_size
        self.gamma = gamma

    def get_lr(self, epoch):
        # Calculate and return the learning rate for the given epoch
        decay_steps = epoch//self.step_size
        lr = self.initial_lr * (self.gamma ** decay_steps)
        return round(lr,4)