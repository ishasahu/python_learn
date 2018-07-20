# part 2-1
def count_word(s):
   return len(s.split(' '))
# part 2-2
def count_word_w_delimiter(s, d):
   return len(s.split(d))

# part 2-3
def word_length(s, d):
   return [d.join ([w.strip() for w in s.split(' ')])]

def is_prime(n):
   for i in range(2,n):
       if n%i == 0:
           return 'is not prime'
   return 'is prime'

# part 2-4
def get_prime(n):
   return [n for n in range(2, n+1) if is_prime(n) == 'is prime' ]

# part 2-5
def diviable_count(l, n):
   return [sum(1 for i in l if i%n == 0)]

# part 2-6
def end_with_letter(my_list, l):
   return[w for w in my_list if w.upper().endswith(l.upper())]

# part 2-7
def contain_string(my_list, s):
   l=[]
   for i, w in enumerate(my_list):
       if w.upper().strip().find(s.upper())>=0:
           l.append(i)
   return l
print(count_word('hello world how are you'))
print(count_word_w_delimiter('hope | you | have | a | great | weekend', '|'))
print(word_length('hello world how are you', '-'))
print(get_prime(50))
print(diviable_count([2,4,8,12,16,20,21], 4))
print(end_with_letter(['lol', 'Love', 'do', 'little'], 'e'))
print(contain_string(['This', 'Is', 'an', 'Example'], 'is'))