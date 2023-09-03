target_value = 11
lst = [2,3,7,8,10]
answer = []

# Populating the table with default values
for i in range(len(lst)):
  temp_list = []
  for j in range(12):
    if j == 0:
      temp_list.append(True)
    else:
      temp_list.append(0)
  answer.append(temp_list)

# do one iteration for the first row so the subsequent rows can make use of this row to do
for sum in range(1,12):
  print(sum)
  if sum == lst[0]:
    answer[0][sum] = True
  else:
    answer[0][sum] = False

for i in range(1, len(lst)):
  for sum in range(1 , 12):
    if sum < lst[i]:
      answer[i][sum] = answer[i-1][sum] # follow the previous row result
    else:
      answer[i][sum] = answer[i-1][j] or answer[i-1][sum - lst[i]] # find a combo that will add up to sum




print("There is subset in the set {} that will give {}".format(lst , answer[len(lst)-1][11]))
    
    
    