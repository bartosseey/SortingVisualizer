from tkinter import *
from tkinter import ttk
from ttkbootstrap import *
import time
import random



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
                                     padding=5, width=15,
                                     command=self.bubble)
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

        self.shuffleArray = ttk.Button(self.root, text='Shuffle', style='info.TButton',
                                       padding=5, width=15,
                                       command=self.shuffle)
        self.shuffleArray.grid(column=3, row=3, padx=5, pady=30) 

        ttk.Label(self.root, text='Speed & Array Size:').grid(row=3,column=1, padx=10)
        self.arraySize=ttk.Scale(self.root,from_=5,to=100,
                                 length=300,style='success.Horizontal.TScale',value=10,
                                 command=lambda x:self.slide_function())
        self.arraySize.grid(row=4,column=0,columnspan=3, padx=5)




        self.canvas=Canvas(self.root, width=900, height=400, bg='yellow')
        self.canvas.grid(row=6, padx=5, pady=10, columnspan=6)


    def bubble(self):
        pass

    def insertion(self):
        pass

    def selection(self):
        pass

    def merge(self):
        pass

    def quick(self):
        pass

    def radix(self):
        pass

    def heap(self):
        pass

    def counting(self):
        pass

    def bucket(self):
        pass

    def shell(self):
        pass

    def shuffle(self):
        pass

if __name__=="__main__":
    window = Style(theme='cyborg').master
    app = Gui(window)

    window.mainloop()