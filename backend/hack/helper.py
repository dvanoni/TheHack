import datetime

class UserState:
  SITTING = 0
  WALKING = 1
  RUNNING = 2

class DayState:
  MORNING   = 0
  AFTERNOON = 1
  EVENING   = 2

def analyze_accel( ax, ay, az ):
  '''
    Returns whether the, probable, user state based on accelerometer data
    
    Averages the accelerometer x, y, and z values and determines whether the
    user is sitting, walking and running depending on thresholds set.
  '''
  
  if ax is None or ay is None or az is None:
    return UserState.SITTING
    
  avg_accel = ( ax + ay + az ) / 3
  
  user_state = UserState.SITTING
  if avg_accel > 10 and avg_accel < 20:
    user_state = UserState.WALKING
  elif avg_accel >= 20:
    user_state = UserState.RUNNING
    
  return user_state

def parse_accel( accel_data ):
  '''
    Returns accelerometer x,y,z values that have been passed into the API from
    the phone.
    
    Input:
      accel_data - string
    
    Output:
      ( ax, ay, az ) - float tuple
      
      Returns ( None, None, None ) if it cannot parse the accelerometer data
  '''
  if accel_data is None:
    return ( None, None, None )

  accel_data = accel_data.split( ',' )  
  # Check to see if we have correct data
  if len( accel_data ) != 3:
    return ( None, None, None )
  
  try:
    return ( float( accel_data[0] ), float( accel_data[1] ), float( accel_data[2] ) )
  except ValueError:
    # For some reason we cannot convert these floats, return None
    return ( None, None, None )
    
def analyze_timestamp(timestamp):
  """timestamp as seconds from 1970"""

  # Convert timestamp into a python datetime object
  try:
    timestamp = datetime.datetime.fromtimestamp(float(timestamp))
  except Exception:
    # use the server time if we can't parse the sucker
    timestamp = datetime.datetime.now()

  hour = timestamp.time().hour
  if hour < 12:
    return DayState.MORNING
  elif hour < 17:
    return DayState.AFTERNOON
  else:
    return DayState.EVENING
