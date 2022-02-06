def is_the_month_valid(mm):

    if mm >= 1 or mm <= 12:
        return True
    else:
        return False


def is_the_day_valid(dd, mm, yyyy):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    days_feb = [2]

    for mm in days_31:
        if 1 <= dd <= 31:
            return True
        else:
            return False

    for mm in days_30:
        if 1 <= dd <= 30:
            return True
        else:
            return False
    for mm in days_feb:
        if mm == days_feb:
            if 1 <= dd <= 28:
                return True
            else:
                return False
    for mm in days_feb:
        if yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
            if mm == days_feb:
                if 1 <= dd <= 29:
                    return True
                else:
                    return False



def is_the_year_valid(yyyy):
    if 0 <= yyyy <= 3000:
        return True
    else:
        return False


def main():
    date = input("Enter the date in dd/mm/yyyy format: ")
    dd, mm, yyyy = date.split('/')
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    mm_validity = is_the_month_valid(int(mm))
    dd_validity = is_the_day_valid(int(dd), int(mm), yyyy)
    yyyy_validity = is_the_year_valid(yyyy)
    if dd_validity and mm_validity and yyyy_validity == True:
        print("The date is valid.")
    else:
        print("The date is invalid.")
main()