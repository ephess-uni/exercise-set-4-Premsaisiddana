from datetime import datetime

def logstamp_to_datetime(datestr):
    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
    