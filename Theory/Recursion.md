### What is Recursion?
It is a phenomenon when a function calls itself indefinitely until a specified condition is fulfilled.


### What is Stack Overflow in recursion?
Whenever recursion calls are executed, they are simultaneously stored in a recursion stack where they wait for the completion of the recursive 
function. A recursive function can only be completed if a base condition is fulfilled and the control returns to the parent function.

But, when there is no base condition given for a particular recursive function, it gets called indefinitely which results in a **Stack Overflow** 
i.e., execeeding the memory limit of the recursion stack and hence the program terminated giving a Segmentation Fault error.

The illustration above also represents the case of a **Stack Overflow** as there is no terminating condition for recursion to stop, hence it will 
also result in a memory limit exceeded error.


### Base Condition 
It is the condition that is written in a recursive function in order for it to get completed and not to run infinitely. After encountering the base 
condition, the function terminates and returns back to its parent function simultaneously.

To get a better understanding of how the base condition is an integral part of recursive functions.


```python
count=0
def func(){
    if count==3 return
    print(count)
    count++
    func()
}
print(func)
```

### Recursive Tree
A recursive tree is basically a representative form of recursion depends on the flow of the function calling and returned as a series of events 
happening consecutively.