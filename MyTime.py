from datetime import datetime, timedelta

class MyTime:
    def __init__(self, *args):
        if len(args) == 0:
            now = datetime.now()
            self.time = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
            print("zero arguments:", self.time)

        elif len(args) == 1:
            time_args = args[0]

            if isinstance(time_args, str):
                list_hms_str = time_args.split(":")
                self.time = timedelta(hours=int(list_hms_str[0]), minutes=int(list_hms_str[1]), seconds=int(list_hms_str[2]))
                print("string:", self.time)

            elif isinstance(time_args, MyTime):
                self.time = time_args.time
                print("object:", self.time)

        elif len(args) == 3:
            self.time = timedelta(hours=args[0], minutes=args[1], seconds=args[2])
            print("numbers:", self.time)

    def __eq__(self, second_time):
        return True if self.time == second_time.time else False
    
    def __ne__(self, second_time):
        return True if self.time != second_time.time else False
    
    def __lt__(self, second_time):
        return True if self.time < second_time.time else False
    
    def __le__(self, second_time):
        return True if self.time <= second_time.time else False
    
    def __gt__(self, second_time):
        return True if self.time > second_time.time else False
    
    def __ge__(self, second_time):
        return True if self.time >= second_time.time else False

    def __add__(self, other):
        if isinstance(other, MyTime):
            result_time = self.time + other.time
            return MyTime(self._format_result(result_time))
        elif isinstance(other, timedelta):
            result_time = self.time + other
            return MyTime(self._format_result(result_time))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, MyTime):
            result_time = self.time - other.time
            return MyTime(self._format_result(result_time))
        elif isinstance(other, timedelta):
            result_time = self.time - other
            return MyTime(self._format_result(result_time))
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, int):
            result_time = timedelta(seconds=self.time.total_seconds() * factor)
            return MyTime(self._format_result(result_time))
        return NotImplemented

    def _format_result(self, result_time):
        total_seconds = int(result_time.total_seconds()) % (24 * 3600)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def __str__(self):
        return self._format_result(self.time)

        
my_time0 = MyTime()
my_time1 = MyTime("10:12:12")
my_time2 = MyTime(my_time0)
my_time3 = MyTime(23, 59, 59)

print(my_time0 == my_time1)
print(my_time1 != my_time3)
print(my_time3 > my_time0)
print(my_time0 >= my_time2)
print(my_time2 < my_time2)
print(my_time1 <= my_time2)
print("Adding:", my_time1 + my_time2)
print("subdivision:", my_time1 - my_time2)
print("mult with 2:", my_time1 * 2)