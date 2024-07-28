import sys
import time

def spinning_cursor(): #use this in conjuction to the below function
    while True:
        for cursor in '|/-\\':
            yield cursor
def usethisforspinningcursor(x):
    spinner = spinning_cursor()
    for i in range(x): #this is the timer
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def spinning_cursor_new(timeuser):
    for i in range(timeuser):
        for cursor in '\\|/-':
            time.sleep(0.1)
            print(f"\r{cursor}", end= '', flush=True)

def progress_bar():
  for i in range(101):
    time.sleep(0.1)
    print(f"\r{i:02d}: {'#'*(i//2)}", end="", flush=True)
    # print(f"\r{i:02d}: [{'#'*(i//2)}{'='*(50-(i//2))}>]", end="", flush=True) #fancier pbar

def spinning_cursor_boolean(boo):
    print('LOADING                         ')
    while boo:
        if not boo:
            break
        for cursor in '\\|/-':
            time.sleep(0.1)
            print(f"\b{cursor}", end= '', flush=True)
