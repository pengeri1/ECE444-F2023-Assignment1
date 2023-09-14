class utils:
  def reversed(num):
    return (str(num))[::-1]

  def formatter(num):
    return bin(int(num))[2:], oct(int(num))[2:]