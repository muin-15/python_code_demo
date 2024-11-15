import array as arr
def bubble_sort(a):
  for i in range(len(a)):
    for j in range(0,len(a)-i-1):
      if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
  return a
a=('i',[4,7,2,8,1,3])
result=bubble_sort(a)
print(result)
