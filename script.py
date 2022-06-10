from tkinter import *
from tkinter import ttk
from ttkbootstrap import *
import time
import random
import threading



class Gui:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting alghortims") 
        self.root.geometry("1000x800")
        self.root.resizable(False, False)
        Label(self.root, text='Sorting Algorithms', font=("17")).grid(
               row=0, columnspan=6)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.bubbleSort = ttk.Button(self.root, text='Bubble Sort', style='info.TButton',
                                     padding=5, width=15, command=self.bubble)
                                     #command=threading.Thread(target=self.bubble).start)
        self.bubbleSort.grid(column=0, row=1, padx=5, pady=5)

        self.insertionSort = ttk.Button(self.root, text='Insertion Sort', style='info.TButton',
                                        padding=5, width=15,
                                        command=self.insertion)
        self.insertionSort.grid(column=1, row=1, padx=5, pady=5)

        self.selectionSort = ttk.Button(self.root, text='Selection Sort', style='info.TButton',
                                        padding=5, width=15,
                                        command=self.selection)
        self.selectionSort.grid(column=2, row=1, padx=5, pady=5)

        self.mergeSort = ttk.Button(self.root, text='Merge Sort', style='info.TButton',
                                    padding=5, width=15,
                                    command=self.merge)
        self.mergeSort.grid(column=0, row=2, padx=5, pady=5)   

        self.quickSort = ttk.Button(self.root, text='Quick Sort', style='info.TButton',
                                    padding=5, width=15,
                                    command=self.quick)
        self.quickSort.grid(column=1, row=2, padx=5, pady=5)       

        self.radixSort = ttk.Button(self.root, text='Radix Sort', style='info.TButton',
                                    padding=5, width=15,
                                    command=self.radix)
        self.radixSort.grid(column=2, row=2, padx=5, pady=5)      
 
        self.heapSort = ttk.Button(self.root, text='Heap Sort', style='info.TButton',
                                   padding=5, width=15,
                                   command=self.heap)
        self.heapSort.grid(column=3, row=1, padx=5, pady=5) 

        self.countingSort = ttk.Button(self.root, text='Counting Sort', style='info.TButton',
                                       padding=5, width=15,
                                       command=self.counting)
        self.countingSort.grid(column=3, row=2, padx=5, pady=5) 

        self.bucketSort = ttk.Button(self.root, text='Bucket Sort', style='info.TButton',
                                     padding=5, width=15,
                                     command=self.bucket)
        self.bucketSort.grid(column=4, row=1, padx=5, pady=5) 

        self.shellSort = ttk.Button(self.root, text='Shell Sort', style='info.TButton',
                                    padding=5, width=15,
                                    command=self.shell)
        self.shellSort.grid(column=4, row=2, padx=5, pady=5) 

        self.createArray = ttk.Button(self.root, text='Create/Shuffle', style='info.TButton',
                                       padding=5, width=15,
                                       command=self.create)
        self.createArray.grid(column=3, row=3, padx=5, pady=30) 

        ttk.Label(self.root, text='Array Size:').grid(row=3,column=1, padx=10)
        self.slide=ttk.Scale(self.root,from_=15,to=100,
                                 length=300,style='success.Horizontal.TScale',value=15,
                                 command=lambda x:self.slideFunc())
        self.slide.grid(row=4,column=0,columnspan=3, padx=5)

        ttk.Label(self.root, text='Speed:').grid(row=5,column=1, padx=10)
        self.slideSpeed=ttk.Scale(self.root,from_=300,to=1,
                                 length=300,style='success.Horizontal.TScale',value=300,
                                 command=lambda x:self.slideSpeedFunc())
        self.slideSpeed.grid(row=6,column=0,columnspan=3, padx=5)




        self.canvas=Canvas(self.root, width=900, height=400, bg='yellow')
        self.canvas.grid(column=0 ,row=7, padx=5, pady=10, columnspan=6)

        
    def bubble(self):
        speed = int(self.slideSpeedFunc())
        for i in range(len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 

                    self.displayArr(arr, ["blue" if x == j else "red" if x==j+1 else "#EFCB68" for x in range(len(arr))])
                    self.canvas.after(speed)

        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])

    def insertion(self):
        speed = int(self.slideSpeedFunc())
        for i in range(1, len(arr)):
            key = arr[i]

            j = i-1
            while j>= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1

                self.displayArr(arr, ["blue" if x == j else "red" if x==j+1 else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)
            arr[j+1] = key

        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])

    def selection(self):
        speed = int(self.slideSpeedFunc())
        for i in range(len(arr)-1):
     
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    self.displayArr(arr, ["blue" if x == j else "red" if x==j+1 else "#47E5BC" if x<i  else "#EFCB68" for x in range(len(arr))])
                    self.canvas.after(speed)

        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])

    def merge(self):
        speed = int(self.slideSpeedFunc())
        def mergeArray(arr, begin, mid, end):
            p = begin
            q = mid + 1
            tempArray = []

            for i in range(begin, end+1):
                if p > mid:
                    tempArray.append(arr[q])
                    q+=1
                elif q > end:
                    tempArray.append(arr[p])
                    p+=1
                elif arr[p] < arr[q]:
                    tempArray.append(arr[p])
                    p+=1
                else:
                    tempArray.append(arr[q])
                    q+=1

            for p in range(len(tempArray)):
                arr[begin] = tempArray[p]
                begin += 1

        def mergeSort(arr, begin, end):
            if begin < end:
                mid = int((begin + end) / 2)
                mergeSort(arr, begin, mid)
                mergeSort(arr, mid+1, end)

                mergeArray(arr, begin, mid, end)

                self.displayArr(arr, ["red" if x >= begin and x < mid else "purple" if x == mid 
                                else "green" if x > mid and x <=end else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)

        mergeSort(arr, 0, len(arr)-1)
        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])

        

    def quick(self):
        speed = int(self.slideSpeedFunc())
        def partition(l, r, arr):
            pivot, ptr = arr[r], l
            for i in range(l, r):
                if arr[i] <= pivot:
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
                    self.displayArr(arr, ["green" if x == i else "purple" if x==ptr else "#EFCB68" for x in range(len(arr))])
                    self.canvas.after(speed)
            arr[ptr], arr[r] = arr[r], arr[ptr]

            return ptr
        def quickSort(l, r, arr):
            if len(arr) == 1:  
                return arr
            if l < r:
                pi = partition(l, r, arr)
                quickSort(l, pi-1, arr) 
                quickSort(pi+1, r, arr)  
                self.displayArr(arr, ["blue" if x == l else "red" if x==r else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)
            return(arr)
        l = 0
        r = len(arr)-1
        quickSort(l, r, arr)
        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])
 
            
    def radix(self):
        speed = int(self.slideSpeedFunc())
        def countingSort(exp1):
            n = len(arr)
        
            output = [0] * (n)
        
            count = [0] * (10)
        
            for i in range(0, n):
                index = arr[i] // exp1
                count[index % 10] += 1
        

            for i in range(1, 10):
                count[i] += count[i - 1]
        
            i = n - 1
            while i >= 0:
                index = arr[i] // exp1
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            i = 0
            for i in range(0, len(arr)):
                arr[i] = output[i]
                self.displayArr(arr, ["blue" if x == i else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)
        
        def radixSort():
            max1 = max(arr)
            exp = 1
            while max1 / exp > 1:
                countingSort(exp)
                exp *= 10
        radixSort()
        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])


    def heap(self):
        speed = int(self.slideSpeedFunc())
        def heapify(arr, n, i):

            largest = i 
            l = 2 * i + 1   
            r = 2 * i + 2     

            if l < n and arr[largest] < arr[l]:
                largest = l
        
            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                self.displayArr(arr, ["green" if x == i else "purple" if x==largest else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)
                heapify(arr, n, largest)
        
        
        
        def heapSort(arr):
            n = len(arr)
        
            for i in range(n//2 - 1, -1, -1):
                heapify(arr, n, i)
        
            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i] 
                self.displayArr(arr, ["blue" if x == i else "#EFCB68" for x in range(len(arr))])
                self.canvas.after(speed)
                heapify(arr, i, 0)
        heapSort(arr)
        self.displayArr(arr, ["#47E5BC" for x in range(len(arr))])

    def counting(self):
        pass

    def bucket(self):
        pass

    def shell(self):
        pass

    def slideFunc(self):
        slideValue = self.slide.get()
        return slideValue
    
    def slideSpeedFunc(self):
        slideSpeedValue = self.slideSpeed.get()
        return slideSpeedValue

    def create(self):
        global arr
        arr = []

        array_size = int(self.slideFunc())
        print(array_size)
        range_begin = 10
        range_end = 200

        
        for i in range(0, array_size):  
            random_integer = random.randint(range_begin, range_end) #starting from a higher value and not 0 because the vertical bars wont be visible
            arr.append(random_integer)

        self.displayArr(arr, ["#EFCB68" for x in range(len(arr))])

    def displayArr(self, arr, colorArray):
        self.canvas.delete("all")
        canvasWidth = 900
        canvasHeight = 400
        widthColumn = canvasWidth / (len(arr) + 1)
        distanceBetween = 2
        tempArr = [i / max(arr) for i in arr]

        for i in range(len(tempArr)):
            x1 = i * widthColumn + distanceBetween
            y1 = canvasHeight - tempArr[i] * 350
            x2 = (i + 1) * widthColumn 
            y2 = canvasHeight
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

        self.root.update_idletasks()


if __name__=="__main__":
    window = Style(theme='cyborg').master
    app = Gui(window)

    window.mainloop()