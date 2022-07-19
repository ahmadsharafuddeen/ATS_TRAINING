class Time:

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59
        
    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second})')
    
    def __str__(self):
        """Print Time in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))
    
    # hour property's getter method
    @property
    def hour(self):
        """Return the hour."""
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        self._hour = hour
        
    @property
    def minute(self):
        """Return the minute."""
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        """"Set the minute."""
        if not (0 <= minute < 59):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        self._minute = minute
        
    @property 
    def second(self):
        """Return the minute."""
        return self._second
    
    @second.setter
    def second(self, second):
        """"Set the second."""
        if not (0 <= second < 59):
            raise ValueError(f'second ({second}) must be 0-59')
        self._second = second
        
    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second
        

time = Time(12, 34, 57)

time.set_time(0, 6, 4)
print(repr(time))

print(f"{4:0>2}")

time._hour = 14
print(str(time))

