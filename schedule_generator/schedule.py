import logging
from datetime import datetime, timedelta
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s -- %(levelname)s -- %(message)s')


def schedule_gen(days: int = 5,
                 work_days: int = 2,
                 rest_days: int = 2,
                 start_date: datetime = datetime(datetime.now().year, datetime.now().month, datetime.now().day)) -> List[datetime]:
    """
    The schedule_gen function takes in three arguments:
        days (int): the number of days to generate a schedule for.
        work_days (int): the number of consecutive working days before taking a rest day.
        rest_days (int): the number of consecutive resting days after working.

    :param days: int: Set the number of days in the schedule
    :param work_days: int: Specify the number of days to work
    :param rest_days: int: Set the number of days to rest
    :param start_date: datetime: Set the start date of the schedule
    :return: A list of dates,
    :doc-author: Trelent
    """
    schedule = []
    try:

        if days > 0 and work_days > 0 and rest_days > 0:

            for day in range(days):
                delta = timedelta(days=day)
                schedule.append(start_date + delta)
            return schedule[:work_days] + schedule[work_days + rest_days:]
        else:
            raise TypeError(f"argument of type 'NoneType' is not iterable")

    except Exception as exp:
        logging.error(f"schedule_gen(days={days}, work_days={work_days}, rest_days={rest_days}, start_date={start_date}) --> {exp.__class__.__qualname__}: {exp}!")


if __name__ == '__main__':

    print(schedule_gen())
    a = schedule_gen(days=0,
                        work_days=2,
                        rest_days=1,
                        start_date=datetime(2020, 1, 30)
                        )

    print(a)
