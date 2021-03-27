def randomize(self):
        sequence = string.ascii_letters + string.digits
        random_list = random.choices(sequence, k=10)
        random_string = "".join(random_list)
        return random_string