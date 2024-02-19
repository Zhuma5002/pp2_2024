#iterators
myTulple=("banana","apple","grusha")
myIt=iter(myTulple)

print(next(myIt))
print(next(myIt))
print(next(myIt))
#All these objects have a iter() method which is used to get an iterator

myStr="banana"
myIt=iter(myStr)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
#Strings are also iterable objects, containing a sequence of characters

#looping though a iterator:
mytuple=("banana", "apple", "mango")
for x in mytuple:
    print(x)

mystr="apple"
for x in mystr:
    print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
