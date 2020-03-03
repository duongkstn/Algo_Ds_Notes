from math import sqrt
class Query:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class All_Query:
    def __init__(self):
        self.queries = []

    def add(self, start, end):
        q = Query(start, end)
        self.queries.append(q)
    def queryResults(self, arr):
        size = len(arr)
        block = int(sqrt(size))
        self.queries = sorted(self.queries, key=lambda q: (int(q.start / block), q.end))
        currentstart = currentend = currentsum = 0

        for i in range(len(self.queries)):
            start, end = self.queries[i].start, self.queries[i].end
            while (currentstart < start):
                currentsum -= arr[currentstart]
                currentstart += 1
            
            while (currentstart > start):
                currentsum += arr[currentstart - 1]
                currentstart -= 1

            while (currentend < end):
                currentsum += arr[currentend]
                currentend += 1
            while (currentend > end):
                currentsum -= arr[currentend - 1]
                currentend -= 1
            print("Sum of [%s, %s] is %s" % (start, end, currentsum))


arr = []

def main():
    n = int(input("Enter the size of the array "))
    print("Enter the elements ")
    for i in range(n):
        arr.append(int(input()))
    
    no = int(input("Enter the numbers of query "))

    all_query = All_Query()
    for i in range(no):
        start = int(input("Enter the start of the query "))
        end = int(input("Enter the end of the query "))
        all_query.add(start, end)
    all_query.queryResults(arr)

if __name__ == '__main__':
    main()
    

