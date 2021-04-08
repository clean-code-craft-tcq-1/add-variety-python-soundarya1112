temperature_breach_limits = { 'PASSIVE_COOLING' : {'lowerLimit': 0,'upperLimit':35}, 'HI_ACTIVE_COOLING' : {'lowerLimit': 0,'upperLimit':45},'MED_ACTIVE_COOLING' : {'lowerLimit': 0,'upperLimit':40} }

temperature_breach_msgs = {'TOO_LOW' : 'too low', 'TOO_HIGH' : 'too high', 'NORMAL' : 'normal'}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = temperature_breach_limits[coolingType]['lowerLimit']
  upperLimit = temperature_breach_limits[coolingType]['upperLimit']
  return infer_breach(temperatureInC, lowerLimit, upperLimit)

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return f'{header}, {breachType}'
  
def send_to_console(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return f'{header}, {breachType}'


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
    
alertType = {"TO_CONTROLLER": send_to_controller, "TO_EMAIL" : send_to_email, "TO_CONSOLE" : send_to_console}
    
def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar,temperatureInC)
  return (alertType[alertTarget](breachType))

