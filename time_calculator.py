
def add_time(start, duration, day = None):

  day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  num_days = 0
  new_meridian = ""
  calculated_hours = 0

  #using split to get information from start 
  time, meridian = start.split()
  hour, minutes = time.split(":")
  hour = int(hour)
  minutes = int(minutes)

  #converting into a 24 hour format
  if meridian == "PM":
      hour += 12

  #getting information from duration 
  dur_hour, dur_minutes = duration.split(":")
  dur_hour = int(dur_hour)
  dur_minutes = int(dur_minutes)

  total_minutes = minutes + dur_minutes
  if total_minutes >= 60:  
      hour += total_minutes // 60
      total_minutes = total_minutes % 60
 
  total_hours = hour + dur_hour
  calculated_hours = total_hours % 24
  if calculated_hours == 0:
      calculated_hours = 12

    
  if total_hours >= 24:
      num_days += total_hours // 24
      total_hours = total_hours % 24
  if total_hours == 0 or total_hours <= 11:
      new_meridian = "AM"
  else:
      new_meridian = "PM"
  if total_hours == 0:
      total_hours = 12

  if total_hours % 24 > 12:
      calculated_hours = total_hours % 12           

     #Handling for minutes to be in :00 format
  if total_minutes < 10:
      total_minutes = '0' + str(total_minutes)
  else: 
      total_minutes = str(total_minutes)
  
  calculated_time = str(calculated_hours) + ":" + total_minutes + " " + new_meridian

  if day == None:
      day = ""
  else:
      for x in range(7):
          if day.lower() == day_of_week[x].lower():
              day = ", " + day_of_week[(x + num_days) % 7]

  if num_days == 0:
      num_days = ""
  elif num_days == 1:
      num_days = " (next day)"
  else:
      num_days = " ("+ str(num_days) + " days later)"




  new_time = calculated_time + day + num_days 

  return new_time