from datetime import timedelta, datetime
def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    
    # Replace this with your code!
    temp = time.split();
    date_object = datetime.strptime(start_date, '%Y/%m/%d')
    if ((temp[1] == 'days' or temp[1] == 'day')):
        end_date = date_object+timedelta(days = int(temp[0]));
    if ((temp[1] == 'weeks' or temp[1] == 'week')):
        end_date = date_object+timedelta(weeks=int(temp[0]))
        
    end_date = end_date.strftime("%Y/%m/%d");
    return end_date;

print(which_date('2016/02/10','35 days'));
print(which_date('2016/12/21', '3 weeks'));
print(which_date('2015/01/17', '1 week'));
    
