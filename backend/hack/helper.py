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
  
  if len( accel_data ) != 3:
    return ( None, None, None )
  
  return ( float( accel_data[0] ), float( accel_data[1] ), float( accel_data[2] ) )