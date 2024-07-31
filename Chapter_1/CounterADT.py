"""
1.1 A click counter is a small hand-held device that contains a push button and
a count display. To increment the counter, the button is pushed and the new
count shows in the display. Clicker counters also contain a button that can be
pressed to reset the counter to zero. Design and implement the Counter ADT
that functions as a hand-held clicker.
"""

class Counter:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

    def __str__(self):
        return str(self.count)
    

if __name__ == '__main__':
    counter = Counter()
    print("Initial Counter: ", counter)  # Output: 0
    counter.click()
    print("After first click: ", counter)  # Output: 1
    counter.click()
    print("After second click: ", counter)  # Output: 2
    print("Getting total count: ", counter.get_count())  #Output: 2
    counter.reset()
    print("After reset: ", counter)  # Output: 0
    print("Getting count after reset: ", counter.get_count())  # Output: 0