def getGCD(a, b):
  if(b > a):
    raise Exception("First argument has to be bigger than second")
  remainder = a%b
  if(remainder):
    return getGCD(b, remainder)
  else:
    return  b

class linear_combination:
  def __init__(self, weights: list[int], numbers: list[int]):
    self.numbers = numbers
    self.weights = weights
    self.lhs = 0
    for i in range(len(weights)):
      self.lhs += weights[i] * numbers[i]
  
  def calLHS(self):
    self.lhs = 0
    for i in range(len(self.weights)):
      self.lhs += self.weights[i] * self.numbers[i]

  def getNums(self, indices: list[int] = []):
    if(len(indices) == 0):
      return self.numbers
    outputArr = []
    for i in indices:
      if(i>=len(self.numbers) or i <0):
        raise Exception("Please check the indices, unusable index: {}".format(i))
      outputArr.append(self.numbers[i])
    return outputArr
  
  def getWeights(self, indices: list[int] = []):
    if(len(indices) == 0):
      return self.weights
    outputArr = []
    for i in indices:
      if(i>=len(self.weights) or i <0):
        raise Exception("Please check the indices, unusable index: {}".format(i))
      outputArr.append(self.weights[i])
    return outputArr

  def getLHS(self):
    return self.lhs
  
  def addTerms(self, weight: int, number: int):
    self.weights.append(weight)
    self.numbers.append(number)
    self.calLHS()
  
  def replaceNum(self, num: int, newWeights: list[int], newNums: list[int]):
    oldLen = len(self.numbers)-1
    for i in range(oldLen,-1,-1):
      if(self.numbers[i] == num):
        for j in range(len(newWeights)):
          if(newNums[j] != 0):
            self.addTerms(self.weights[i] * newWeights[j], newNums[j])
        del self.numbers[i]
        del self.weights[i]
    self.calLHS()
    self.shortenLikeTerms()
  
  def removeTerm(self, i: int):
    del self.numbers[i]
    del self.weights[i]
    self.calLHS()

  def __str__(self):
    outputText = ""
    for i in range(len(self.weights)-1):
      if(self.weights[i] == 1):
        outputText += f"{self.numbers[i]} + "
      else:
        outputText += f"({self.weights[i]} * {self.numbers[i]}) + "
    if(self.weights[-1] == 1):
      outputText += f"{self.numbers[-1]}"
    else:
      outputText += f"({self.weights[-1]} * {self.numbers[-1]})"
    return f"{self.lhs} = " + outputText

  def shortenLikeTerms(self):
    newWeights = []
    newNums = []
    for k in range(len(self.numbers)):
      selectI = -1
      for i in range(len(newNums)):
        if(newNums[i] == self.numbers[k]):
          selectI = i
      if(selectI == -1):
        selectI = len(newNums)
        newNums.append(self.numbers[k])
        newWeights.append(0)
      newWeights[selectI] += self.weights[k]
    self.numbers = newNums
    self.weights = newWeights 
    
def get_GCD_Steps(a: int, b: int, outputArr: list[linear_combination]):
  if(b > a):
    raise Exception("First argument has to be bigger than second")
  
  remainder = a%b
  lc = linear_combination([a//b,1],[b,remainder])
  outputArr.append(lc)
  if(remainder):
    return get_GCD_Steps(b, remainder, outputArr)
  return outputArr

def transportFirstTermToOtherSide(lc: linear_combination):
  lhs = lc.getLHS()
  firstW = lc.getWeights()[0]
  firstN = lc.getNums()[0]
  del lc
  return linear_combination([1, firstW*-1], [lhs, firstN])

def gcdAsLinearCombination(a, b):
  if(b > a):
    raise Exception("First argument has to be bigger than second")
  allLC = get_GCD_Steps(a, b, [])
  for i in range(len(allLC)-2,-1,-1):
    allLC[i] = transportFirstTermToOtherSide(allLC[i])

  curLC = allLC[-2]

  for i in range(len(allLC)-3,-1,-1):
    curLC.replaceNum(allLC[i].getLHS(), allLC[i].getWeights(), allLC[i].getNums())

  return  curLC

print(getGCD(66528, 52920))
print(gcdAsLinearCombination(32321, 26513))
print(gcdAsLinearCombination(66528, 52920))
