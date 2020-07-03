import datetime
import time
from datetime import datetime, timedelta

import pytz


def date_sub(date_in, interval):
    """
    sub date with interval day
    :param date_in: str format %Y-%m-%d %H:%M:%S
    :param interval:
    :return:
    """
    return datetime.strptime(date_in, '%Y-%m-%d %H:%M:%S') - timedelta(days=interval)


def date_add(date_in, interval):
    """
    sub date with interval day
    :param date_in: str format %Y-%m-%d %H:%M:%S
    :param interval: int
    :return:
    """
    return datetime.strptime(date_in, '%Y-%m-%d %H:%M:%S') + timedelta(days=interval)


def date_sub_from_now(time_zone, interval):
    """
    add date with interval day from now
    :param time_zone: str
    :param interval: int
    :return:
    """
    return datetime.now(pytz.timezone(time_zone)) - timedelta(days=interval)


def date_add_from_now(time_zone, interval):
    """
    add date with interval day from now
    :param time_zone:
    :param interval:
    :return:
    """
    return datetime.now(pytz.timezone(time_zone)) + timedelta(days=interval)


def format_timestamp_to_str_time():
    """
    convert timestamp to time str: %Y-%m-%d %H:%M:%S
    :return: str
    """
    ts = time.time()
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def compare_2date(d1, d2):
    """
    compare 2 date
    :param d1: str
    :param d2: str
    :return: boolean
    """
    d1 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    return True if d1 <= d2 else False


def sub_2date(d1, d2):
    """
    sub 2 date
    :param d1: str
    :param d2: str
    :return: elapsed_time (datetime object), you can elapsed_time.total_seconds() to convert total seconds
    """
    d1 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    elapsed_time = d1 -d2
    return elapsed_time