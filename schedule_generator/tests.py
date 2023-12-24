from datetime import datetime, timedelta

from schedule import schedule_gen


def test_schedule():

    # successful test: All arguments valid
    assert schedule_gen(days=5,
                        work_days=2,
                        rest_days=1,
                        start_date=datetime(2020, 1, 30)
                        ) == [datetime(2020, 1, 30, 0, 0),
                              datetime(2020, 1, 31, 0, 0),
                              datetime(2020, 2, 2, 0, 0),
                              datetime(2020, 2, 3, 0, 0)]

    # successful test: Default arguments
    assert schedule_gen() == [datetime(datetime.now().year, datetime.now().month, datetime.now().day),
                              datetime(datetime.now().year, datetime.now().month, datetime.now().day) + timedelta(days=1),
                              datetime(datetime.now().year, datetime.now().month, datetime.now().day) + timedelta(days=4)]

    # failed test: The 'days' argument equal 0
    assert schedule_gen(days=0,
                        work_days=2,
                        rest_days=1,
                        start_date=datetime(2020, 1, 30)) is None

    # failed test: The 'work_days' argument equal 0
    assert schedule_gen(days=5,
                        work_days=0,
                        rest_days=1,
                        start_date=datetime(2020, 1, 30)) is None

    # failed test: The 'rest_days' argument equal 0
    assert schedule_gen(days=5,
                        work_days=2,
                        rest_days=0,
                        start_date=datetime(2020, 1, 30)) is None

    # failed test: The 'start_date' argument wrong type
    assert schedule_gen(days=5,
                        work_days=2,
                        rest_days=0,
                        start_date=2) is None


if __name__ == '__main__':
    test_schedule()
