class Exchange():
  def __init__(self, from_exc, to_exc, time, price):
    self.from_exc = from_exc
    self.to_exc = to_exc
    self.time = time
    self.price = price 
  
  def getFrom(self):
    return self.from_exc

  def getTo(self):
    return self.to_exc

  def getTime(self):
    return self.time

  def getPrice(self):
    return self.price
  
