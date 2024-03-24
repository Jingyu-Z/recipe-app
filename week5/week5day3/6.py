# public static string GetDayOfWeek(int day)
# {
#     return Enum.GetName(typeof(DayOfWeek), day);
# }

def get_day_of_week(day):
    
    days_of_week = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday", "Sunday"]

    return days_of_week [day - 1]

