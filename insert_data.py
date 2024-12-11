# insert_data.py

from models import db, WeatherInfo, AlertInfo, FlightInfo, AirportInfo, User, UserQueryRecord, SystemLog

from sqlalchemy import func

def insert_data():
    # 插入气象信息
    db.session.add_all([
        WeatherInfo(WeatherID=11, LocationID=11, Timestamp='2024-01-01 09:00:00', Temperature=15.0, WindSpeed=4.0, WindDirection='NE', Humidity=55.0, Visibility=12.0, Pressure=1013.5),
        WeatherInfo(WeatherID=12, LocationID=12, Timestamp='2024-01-02 10:00:00', Temperature=18.0, WindSpeed=7.5, WindDirection='W', Humidity=70.0, Visibility=15.0, Pressure=1010.0),
        WeatherInfo(WeatherID=13, LocationID=13, Timestamp='2024-01-02 11:00:00', Temperature=10.0, WindSpeed=5.0, WindDirection='S', Humidity=80.0, Visibility=8.0, Pressure=1014.0),
        WeatherInfo(WeatherID=14, LocationID=14, Timestamp='2024-01-02 12:00:00', Temperature=25.0, WindSpeed=4.0, WindDirection='SW', Humidity=65.0, Visibility=20.0, Pressure=1011.0),
        WeatherInfo(WeatherID=15, LocationID=15, Timestamp='2024-01-03 08:00:00', Temperature=22.3, WindSpeed=6.0, WindDirection='SE', Humidity=70.0, Visibility=14.0, Pressure=1008.5),
        WeatherInfo(WeatherID=16, LocationID=16, Timestamp='2024-01-03 09:00:00', Temperature=15.5, WindSpeed=4.0, WindDirection='N', Humidity=75.0, Visibility=10.0, Pressure=1010.0),
        WeatherInfo(WeatherID=17, LocationID=17, Timestamp='2024-01-04 06:00:00', Temperature=5.0, WindSpeed=10.0, WindDirection='W', Humidity=85.0, Visibility=5.0, Pressure=1007.5),
        WeatherInfo(WeatherID=18, LocationID=18, Timestamp='2024-01-05 10:00:00', Temperature=12.0, WindSpeed=3.5, WindDirection='NW', Humidity=65.0, Visibility=12.0, Pressure=1012.0),
        WeatherInfo(WeatherID=19, LocationID=19, Timestamp='2024-01-06 14:00:00', Temperature=30.0, WindSpeed=2.0, WindDirection='E', Humidity=50.0, Visibility=20.0, Pressure=1005.0),
        WeatherInfo(WeatherID=20, LocationID=10, Timestamp='2024-01-06 15:00:00', Temperature=20.0, WindSpeed=7.0, WindDirection='S', Humidity=68.0, Visibility=9.0, Pressure=1011.5),
        WeatherInfo(WeatherID=21, LocationID=11, Timestamp='2024-01-07 09:00:00', Temperature=21.0, WindSpeed=6.0, WindDirection='E', Humidity=65.0, Visibility=11.0, Pressure=1009.8),
        WeatherInfo(WeatherID=22, LocationID=12, Timestamp='2024-01-07 11:00:00', Temperature=19.5, WindSpeed=5.5, WindDirection='NE', Humidity=72.0, Visibility=14.0, Pressure=1012.3),
        WeatherInfo(WeatherID=23, LocationID=13, Timestamp='2024-01-07 13:00:00', Temperature=23.0, WindSpeed=3.5, WindDirection='SE', Humidity=62.0, Visibility=10.0, Pressure=1010.0),
        WeatherInfo(WeatherID=24, LocationID=14, Timestamp='2024-01-07 15:00:00', Temperature=28.0, WindSpeed=2.5, WindDirection='SW', Humidity=48.0, Visibility=18.0, Pressure=1008.0),
        WeatherInfo(WeatherID=25, LocationID=15, Timestamp='2024-01-08 08:00:00', Temperature=9.0, WindSpeed=3.5, WindDirection='W', Humidity=70.0, Visibility=8.0, Pressure=1011.0),
        WeatherInfo(WeatherID=26, LocationID=16, Timestamp='2024-01-08 10:00:00', Temperature=25.0, WindSpeed=5.0, WindDirection='NE', Humidity=58.0, Visibility=12.0, Pressure=1009.5),
        WeatherInfo(WeatherID=27, LocationID=17, Timestamp='2024-01-08 12:00:00', Temperature=29.5, WindSpeed=4.5, WindDirection='E', Humidity=53.0, Visibility=15.0, Pressure=1006.0),
        WeatherInfo(WeatherID=28, LocationID=18, Timestamp='2024-01-08 14:00:00', Temperature=16.5, WindSpeed=6.5, WindDirection='N', Humidity=68.0, Visibility=9.0, Pressure=1013.0),
        WeatherInfo(WeatherID=29, LocationID=19, Timestamp='2024-01-08 16:00:00', Temperature=35.0, WindSpeed=1.0, WindDirection='NW', Humidity=40.0, Visibility=25.0, Pressure=1007.0),
    ])

    # 插入预警信息
    db.session.add_all([
        AlertInfo(AlertID=10, AlertType='暴雨', Severity='High', LocationID=10, StartTime='2024-01-01 00:00:00', EndTime='2024-01-01 12:00:00', Details='区域内预计暴雨，请注意安全'),
        AlertInfo(AlertID=11, AlertType='台风', Severity='Medium', LocationID=11, StartTime='2024-01-02 10:00:00', EndTime='2024-01-02 18:00:00', Details='台风影响，请调整出行计划'),
        AlertInfo(AlertID=12, AlertType='大雪', Severity='High', LocationID=12, StartTime='2024-01-03 08:00:00', EndTime='2024-01-03 20:00:00', Details='预计将出现大雪天气，航班可能延误'),
        AlertInfo(AlertID=13, AlertType='冰雹', Severity='High', LocationID=13, StartTime='2024-01-04 15:00:00', EndTime='2024-01-04 20:00:00', Details='出现冰雹可能，请避免户外活动'),
        AlertInfo(AlertID=14, AlertType='雷暴', Severity='High', LocationID=14, StartTime='2024-01-05 10:00:00', EndTime='2024-01-05 18:00:00', Details='强雷暴来临，请注意避险'),
        AlertInfo(AlertID=15, AlertType='高温', Severity='Medium', LocationID=15, StartTime='2024-01-06 08:00:00', EndTime='2024-01-06 20:00:00', Details='高温天气，注意防暑'),
        AlertInfo(AlertID=16, AlertType='寒潮', Severity='Low', LocationID=16, StartTime='2024-01-07 00:00:00', EndTime='2024-01-07 12:00:00', Details='寒潮来袭，请注意保暖'),
        AlertInfo(AlertID=17, AlertType='大雾', Severity='Low', LocationID=17, StartTime='2024-01-08 05:00:00', EndTime='2024-01-08 10:00:00', Details='大雾天气，能见度低，请谨慎驾驶'),
        AlertInfo(AlertID=18, AlertType='沙尘暴', Severity='High', LocationID=18, StartTime='2024-01-09 10:00:00', EndTime='2024-01-09 20:00:00', Details='区域内沙尘暴天气，尽量减少外出'),
        AlertInfo(AlertID=19, AlertType='暴雪', Severity='High', LocationID=19, StartTime='2024-01-10 00:00:00', EndTime='2024-01-10 12:00:00', Details='暴雪来袭，请减少外出'),
    ])

    # 插入机场信息
    db.session.add_all([
        AirportInfo(AirportID=10, AirportName='北京国际机场', LocationCode='PEK', Location='北京'),
        AirportInfo(AirportID=11, AirportName='上海虹桥机场', LocationCode='SHA', Location='上海'),
        AirportInfo(AirportID=12, AirportName='广州白云机场', LocationCode='CAN', Location='广州'),
        AirportInfo(AirportID=13, AirportName='深圳宝安机场', LocationCode='SZX', Location='深圳'),
        AirportInfo(AirportID=14, AirportName='成都天府机场', LocationCode='CTU', Location='成都'),
        AirportInfo(AirportID=15, AirportName='杭州萧山机场', LocationCode='HGH', Location='杭州'),
        AirportInfo(AirportID=16, AirportName='长沙黄花机场', LocationCode='CSX', Location='长沙'),
        AirportInfo(AirportID=17, AirportName='武汉天河机场', LocationCode='WUH', Location='武汉'),
        AirportInfo(AirportID=18, AirportName='西安咸阳机场', LocationCode='XIY', Location='西安'),
        AirportInfo(AirportID=19, AirportName='重庆江北机场', LocationCode='CKG', Location='重庆'),
    ])

    # 插入航班信息
    db.session.add_all([
        FlightInfo(FlightID=10, FlightNumber='CA101', Departure=10, Arrival=11, ScheduledTime='2024-01-02 10:00:00', Status='On Time'),
        FlightInfo(FlightID=11, FlightNumber='MU202', Departure=11, Arrival=12, ScheduledTime='2024-01-02 12:00:00', Status='Delayed'),
        FlightInfo(FlightID=12, FlightNumber='CZ303', Departure=12, Arrival=13, ScheduledTime='2024-01-03 15:30:00', Status='Cancelled'),
        FlightInfo(FlightID=13, FlightNumber='HU404', Departure=13, Arrival=14, ScheduledTime='2024-01-04 09:00:00', Status='On Time'),
        FlightInfo(FlightID=14, FlightNumber='ZH505', Departure=14, Arrival=15, ScheduledTime='2024-01-05 08:15:00', Status='Delayed'),
    ])

    # 插入用户信息
    db.session.add_all([
        User(UserID=10, Username='admin10', Password='adminpass10', Role='Admin', Phone='13800000010'),
        User(UserID=11, Username='passenger11', Password='pass1234', Role='Passenger', Phone='13800000011'),
        User(UserID=12, Username='staff12', Password='staffpass12', Role='AirlineStaff', Phone='13800000012'),
        User(UserID=13, Username='guest13', Password='guestpass13', Role='Passenger', Phone='13800000013'),
        User(UserID=14, Username='user14', Password='userpass14', Role='Passenger', Phone='13800000014'),
    ])

    # 插入用户查询记录 
    db.session.add_all([
        UserQueryRecord(QueryID=10, UserID=10, QueryTime='2024-01-02 08:00:00', FlightID=10, QueryResult='航班CA101准时起飞'),
        UserQueryRecord(QueryID=11, UserID=11, QueryTime='2024-01-02 09:30:00', FlightID=11, QueryResult='航班MU202延误'),
        UserQueryRecord(QueryID=12, UserID=12, QueryTime='2024-01-03 10:00:00', FlightID=12, QueryResult='航班CZ303已取消'),
        UserQueryRecord(QueryID=13, UserID=13, QueryTime='2024-01-04 11:30:00', FlightID=13, QueryResult='航班HU404准时起飞'),
        UserQueryRecord(QueryID=14, UserID=14, QueryTime='2024-01-05 15:00:00', FlightID=14, QueryResult='航班ZH505延误'),
    ])

    # 插入系统日志
    db.session.add_all([
        SystemLog(LogID=10, OperateTime='2024-01-01 10:00:00', UserID=10, Ttype='登录', Details='用户 admin10 登录系统'),
        SystemLog(LogID=11, OperateTime='2024-01-02 09:00:00', UserID=11, Ttype='查询', Details='用户 passenger11 查询航班 CA101 信息'),
        SystemLog(LogID=12, OperateTime='2024-01-03 11:00:00', UserID=12, Ttype='查询', Details='用户 staff12 查询天气信息'),
    ])

    # 提交数据
    db.session.commit()
    print("数据已成功插入到每张表！")