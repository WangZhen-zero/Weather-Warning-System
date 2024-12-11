from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

# 气象信息表
class WeatherInfo(db.Model):
    __tablename__ = 'weather_info'
    WeatherID = db.Column(db.Integer, primary_key=True)  # 气象编号
    LocationID = db.Column(db.Integer, nullable=False)  # 地点编号
    Timestamp = db.Column(db.DateTime, nullable=False)  # 数据时间戳
    Temperature = db.Column(db.Float, nullable=False)  # 温度
    WindSpeed = db.Column(db.Float, nullable=False)  # 风速
    WindDirection = db.Column(db.String(10), nullable=False)  # 风向
    Humidity = db.Column(db.Float, nullable=False)  # 湿度
    Visibility = db.Column(db.Float, nullable=True)  # 能见度
    Pressure = db.Column(db.Float, nullable=True)  # 气压

# 预警信息表
class AlertInfo(db.Model):
    __tablename__ = 'alert_info'
    AlertID = db.Column(db.Integer, primary_key=True)  # 预警编号
    AlertType = db.Column(db.String(50), nullable=False)  # 预警类型
    Severity = db.Column(db.Enum('Low', 'Medium', 'High'), nullable=False)  # 预警等级
    LocationID = db.Column(db.Integer, nullable=False)  # 地点编号
    StartTime = db.Column(db.DateTime, nullable=False)  # 开始时间
    EndTime = db.Column(db.DateTime, nullable=True)  # 结束时间
    Details = db.Column(db.Text, nullable=True)  # 详细信息

# 航班信息表
class FlightInfo(db.Model):
    __tablename__ = 'flight_info'
    FlightID = db.Column(db.Integer, primary_key=True)  # 航班编号
    FlightNumber = db.Column(db.String(20), unique=True, nullable=False)  # 航班号
    Departure = db.Column(db.Integer, nullable=False)  # 起飞机场编号
    Arrival = db.Column(db.Integer, nullable=False)  # 降落机场编号
    ScheduledTime = db.Column(db.DateTime, nullable=False)  # 计划起飞时间
    Status = db.Column(db.Enum('On Time', 'Delayed', 'Cancelled'), nullable=False, default='On Time')  # 航班状态

# 机场信息表
class AirportInfo(db.Model):
    __tablename__ = 'airport_info'
    AirportID = db.Column(db.Integer, primary_key=True)  # 机场编号
    AirportName = db.Column(db.String(100), nullable=False)  # 机场名称
    LocationCode = db.Column(db.String(10), unique=True, nullable=False)  # 机场代码
    Location = db.Column(db.String(100), nullable=True)  # 位置

# 用户查询记录表
class UserQueryRecord(db.Model):
    __tablename__ = 'user_query_record'
    QueryID = db.Column(db.Integer, primary_key=True)  # 查询编号
    UserID = db.Column(db.Integer, nullable=False)  # 旅客编号
    QueryTime = db.Column(db.DateTime, nullable=False)  # 查询时间
    FlightID = db.Column(db.Integer, nullable=False)  # 查询航班编号
    QueryResult = db.Column(db.Text, nullable=True)  # 查询结果

# 用户表
class User(db.Model):
    __tablename__ = 'user'
    UserID = db.Column(db.Integer, primary_key=True)  # 用户编号
    Username = db.Column(db.String(25), unique=True, nullable=False)  # 用户名
    Password = db.Column(db.String(16), nullable=False)  # 密码
    Role = db.Column(db.Enum('Admin', 'Passenger', 'AirlineStaff'), nullable=False)  # 用户角色
    Phone = db.Column(db.String(11), nullable=True)  # 联系信息

# 系统日志表
class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    LogID = db.Column(db.Integer, primary_key=True)  # 日志编号
    OperateTime = db.Column(db.DateTime, nullable=False)  # 操作时间
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)  # 用户编号
    Ttype = db.Column(db.String(255), nullable=False)  # 操作类型
    Details = db.Column(db.Text, nullable=True)  # 操作详情

    user = db.relationship('User', backref=db.backref('logs', lazy=True))  # 关联用户表

# 初始数据插入函数
def insert_initial_data():
    # 检查是否已有数据，如果有则不插入
    if not WeatherInfo.query.first():
        # 插入气象信息
        db.session.add_all([
            WeatherInfo(WeatherID=1,LocationID=1, Timestamp='2023-12-01 12:00:00', Temperature=15.5, WindSpeed=5.2, WindDirection='NE', Humidity=65.0, Visibility=10.0, Pressure=1012.5),
            WeatherInfo(WeatherID=2,LocationID=2, Timestamp='2023-12-01 13:00:00', Temperature=20.3, WindSpeed=3.8, WindDirection='N', Humidity=55.0, Visibility=8.0, Pressure=1010.2)
        ])

        # 插入预警信息
        db.session.add_all([
            AlertInfo(AlertID=1,AlertType='雷暴', Severity='High', LocationID=1, StartTime='2023-12-02 10:00:00', EndTime='2023-12-02 18:00:00', Details='预计区域内将发生强雷暴，请注意避险'),
            AlertInfo(AlertID=2,AlertType='台风', Severity='Medium', LocationID=2, StartTime='2023-12-03 08:00:00', EndTime='2023-12-03 22:00:00', Details='中度台风预计影响航班，请注意调整行程')
        ])

        # 插入航班信息
        db.session.add_all([
            FlightInfo(FlightID=1,FlightNumber='CA123', Departure=1, Arrival=2, ScheduledTime='2023-12-03 15:30:00', Status='Delayed'),
            FlightInfo(FlightID=2,FlightNumber='MU456', Departure=2, Arrival=3, ScheduledTime='2023-12-03 10:00:00', Status='On Time')
        ])

        # 插入机场信息
        db.session.add_all([
            AirportInfo(AirportID=1,AirportName='北京首都国际机场', LocationCode='PEK', Location='北京'),
            AirportInfo(AirportID=2,AirportName='上海浦东国际机场', LocationCode='PVG', Location='上海'),
            AirportInfo(AirportID=3,AirportName='广州白云国际机场', LocationCode='CAN', Location='广州')
        ])

        # 插入用户
        db.session.add_all([
            User(UserID=1,Username='admin', Password='admin123', Role='Admin', Phone='19157959839'),
            User(UserID=2,Username='john', Password='password123', Role='Passenger', Phone='15538275803')
        ])

        # 插入用户查询记录
        db.session.add_all([
            UserQueryRecord(QueryID=1,UserID=2, QueryTime='2023-12-03 09:00:00', FlightID=1, QueryResult='航班CA123已延误'),
            UserQueryRecord(QueryID=2, UserID=2, QueryTime='2023-12-03 12:30:00', FlightID=2, QueryResult='航班MU456准时起飞')
        ])

        # 插入系统日志
        db.session.add_all([
            SystemLog(LogID=1,OperateTime='2023-12-03 14:00:00', UserID=1, Ttype='登录', Details='用户admin登录系统'),
            SystemLog(LogID=2,OperateTime='2023-12-03 14:15:00', UserID=2, Ttype='查询', Details='用户john_doe查询航班CA123信息')
        ])

        db.session.commit()
        print("初始数据已成功插入！")
    else:
        print("数据库中已有数据，无需插入初始数据！")


