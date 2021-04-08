temperature_breach_types = {'PASSIVE_COOLING': {'coolingType': 'PASSIVE_COOLING' },'HI_ACTIVE_COOLING': {'coolingType': 'HI_ACTIVE_COOLING' },'MED_ACTIVE_COOLING': {'coolingType': 'MED_ACTIVE_COOLING' }}

temperature_breach_limits = {'PASSIVE_COOLING': {'low': 0, 'high':35 },'HI_ACTIVE_COOLING': {'low': 0, 'high':45 },'MED_ACTIVE_COOLING': {'low': 0, 'high':40 }}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = temperature_breach_limits[coolingType]['low']
  upperLimit = temperature_breach_limits[coolingType]['high']
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
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  return (alertType[alertTarget](breachType))

