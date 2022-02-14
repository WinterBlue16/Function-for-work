from genericpath import samefile
from urllib.parse import unquote

sample = 'videoplayback%253Fexpire%253D1532566750%2526mime%253Dvideo%25252Fmp4%2526key%253Dyt6%2526mt%253D1532544983%2526fvip%253D5%2526i'
print(unquote(unquote(sample)))
