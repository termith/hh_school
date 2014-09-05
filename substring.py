def search(substring):
    last_number = 0
    sequence = ""
    while True:
        if sequence.find(substring) == -1:
            sequence += str(last_number+1)
            last_number += 1
        else:
            return sequence.find(substring)+1

if __name__ == '__main__':
    print(search("6789"))
    print(search("101"))

