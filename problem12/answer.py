def init():
  limit = 1000000
  nums = []
  for i in range(limit):
    if i is not 0:
      nums.append(i)
      count = 0
      number = sum(nums)
      if number > 64689625 and number % 500 == 0:
        for n in range(number + 1):
          if i != 0 and n != 0:
            # print(f'{number} % {n} = {number%n}')
            if number % n == 0:
              count = count + 1
        if count > 0:
          print(f'{number}: {count}')
        if count > 500:
          break