class ThreeDigitConverter:
  regex = '[0-9]{3}'

  # we must provide the following function
  def to_python(self, value):
    return int(value)

  def to_url(self, value):
    return '%03d' % value