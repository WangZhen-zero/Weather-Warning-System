from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, current_user
from werkzeug.utils import secure_filename
import pymysql
import os
import argparse
import sys
import importlib

from models import User
from models import db
from insert_data import insert_data 

importlib.reload(sys)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:0728@localhost/weather_system'
app.secret_key = '0728'
mysql_pwd = "0728"
db_name = "weather_system"
# 初始化数据库
db.init_app(app)

# 全局变量
username = ""
userRole = ""
notFinishedNum = 0
# 上传文件要储存的目录
UPLOAD_FOLDER = '/static/images/'
# 允许上传的文件扩展名的集合
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 连接数据库，默认数据库用户名root，密码空
def get_db_connection():
    return pymysql.connect(host="localhost", user="root", password=mysql_pwd, database=db_name, charset='utf8')


# 数据库工具函数
def execute_query(query, params=None):
    """执行查询并返回结果"""
    try:
        db = pymysql.connect(host="localhost", user="root", password=mysql_pwd, database=db_name, charset="utf8")
        with db.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as e:
        print(f"Database Error: {e}")
        return []
    finally:
        db.close()


# 首页
@app.route('/')
@app.route('/index')

# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 注册
@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    global username
    global userRole
    msg = ""
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        userRole = request.form.get('userRole')
        print(userRole)
        print(username)
        # 连接数据库，默认数据库用户名root，密码空
        db = get_db_connection()

        if userRole == 'Passenger':
            cursor = db.cursor()
            try:
                cursor.execute("use weather_system")
            except:
                print("Error: unable to use database!")
            sql1 = "SELECT * from User where username = '{}' ".format(username)
            cursor.execute(sql1)
            db.commit()
            res1 = cursor.fetchall()
            num = 0
            for row in res1:
                num = num + 1
            # 如果已经存在该旅客
            if num == 1:
                print("失败！该用户已注册！")
                msg = "fail1"
            else:
                sql2 = "insert into User (Username, Password, Role, Phone) values (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql2, (username, password, userRole, phone))
                    db.commit()
                    print("注册成功")
                    msg = "done1"
                except ValueError as e:
                    print("--->", e)
                    print("注册出错，失败")
                    msg = "fail1"
            return render_template('register.html', messages=msg, username=username, userRole=userRole)

        elif userRole == 'AirlineStaff':
            cursor = db.cursor()
            try:
                cursor.execute("use weather_system")
            except:
                print("Error: unable to use database!")
            sql1 = "SELECT * from User where Username = '{}'".format(username)
            cursor.execute(sql1)
            db.commit()
            res1 = cursor.fetchall()
            num = 0
            for row in res1:
                num = num + 1
            # 如果已存在该用户
            if num == 1:
                print("用户已注册！请直接登录。")
                msg = "fail2"
            else:
                sql2 = "insert into User (Username, Password, Role, Phone) values (%s, %s, %s, %s)"
                try:
                    cursor.execute(sql2, (username, password, userRole, phone))
                    db.commit()
                    print("注册成功")
                    msg = "done2"
                except ValueError as e:
                    print("--->", e)
                    print("注册出错，失败")
                    msg = "fail2"
            return render_template('register.html', messages=msg, username=username, userRole=userRole)


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    global username
    global userRole
    msg = ""
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        userRole = request.form.get('userRole')
        print(userRole)
        print(username)
        # 连接数据库
        db =  get_db_connection()

        if userRole == 'Admin':
            cursor = db.cursor()
            try:
                cursor.execute("use weather_system")
            except:
                print("Error: unable to use database!")
            sql = "SELECT * from User where Username = '{}' and Password='{}'".format(username, password)
            cursor.execute(sql)
            db.commit()
            res = cursor.fetchall()
            num = 0
            for row in res:
                num = num + 1
            # 如果存在该管理员且密码正确
            if num == 1:
                print("登录成功！欢迎管理员！")
                msg = "done1"
            else:
                print("您没有管理员权限或登录信息出错。")
                msg = "fail1"
            return render_template('login.html', messages=msg, username=username, userRole=userRole)

        elif userRole == 'Passenger':
            cursor = db.cursor()
            try:
                cursor.execute("use weather_system")
            except:
                print("Error: unable to use database!")
            sql = "SELECT * from User where Username = '{}' and Password='{}'".format(username, password)
            cursor.execute(sql)
            db.commit()
            res = cursor.fetchall()
            num = 0
            for row in res:
                num = num + 1
            # 如果存在该旅客且密码正确
            if num == 1:
                print("登录成功！欢迎旅客！")
                msg = "done2"
            else:
                print("您没有旅客权限或登录信息出错。")
                msg = "fail2"
            return render_template('login.html', messages=msg, username=username, userRole=userRole)

        elif userRole == 'AirlineStaff':
            cursor = db.cursor()
            try:
                cursor.execute("use weather_system")
            except:
                print("Error: unable to use database!")
            sql = "SELECT * from User where Username = '{}' and Password='{}'".format(username, password)
            cursor.execute(sql)
            db.commit()
            res = cursor.fetchall()
            num = 0
            for row in res:
                num = num + 1
            # 如果存在该机场人员且密码正确
            if num == 1:
                print("登录成功！欢迎机场人员！")
                msg = "done3"
            else:
                print("您没有机场人员权限或登录信息出错。")
                msg = "fail3"
            return render_template('login.html', messages=msg, username=username, userRole=userRole)


# 旅客主页面
@app.route('/passenger_dashboard', methods=['GET'])
def passenger_dashboard():
    alerts = []
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM alert_info ORDER BY Severity")
        alerts = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()
    return render_template('passenger_dashboard.html', alerts=alerts)

# 显示航班信息
@app.route('/passenger/flights', methods=['GET'])
def passenger_flights():
    flights = []
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM flight_info ORDER BY ScheduledTime")
        flights = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()
    return render_template('passenger_flights.html', flights=flights)

# 显示机场信息
@app.route('/passenger/airports', methods=['GET'])
def passenger_airports():
    airports = []
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM airport_info")
        airports = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()
    return render_template('passenger_airports.html', airports=airports)

# 显示气象信息
@app.route('/passenger/weather', methods=['GET'])
def passenger_weather():
    weather = []
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM weather_info ORDER BY Timestamp DESC")
        weather = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()
    return render_template('passenger_weather.html', weather=weather)

@app.route('/passenger/search', methods=['GET', 'POST'])
def passenger_search():
    """旅客查询页面"""
    results = []
    table = None     # 初始化查询结果和表名
    if request.method == 'POST':
        table = request.form.get('table')
        keyword = request.form.get('keyword')
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query_map = {
                "flights": "SELECT * FROM flight_info WHERE FlightNumber LIKE %s",
                "airports": "SELECT * FROM airport_info WHERE AirportName LIKE %s",
                "weather": "SELECT * FROM weather_info WHERE WindDirection LIKE %s",
                "alerts": "SELECT * FROM alert_info WHERE AlertType LIKE %s",
            }
            if table in query_map:
                cursor.execute(query_map[table], (f"%{keyword}%",))
                results = cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            db.close()
    
    return render_template('passenger_search_results.html', results=results, table=table)



# 机场人员主页面
@app.route('/airport_staff_dashboard', methods=['GET'])
def airport_staff_dashboard():
    """显示机场人员主页面，包含所有表数据的展示"""
    try:
        db = get_db_connection()
        cursor = db.cursor()

        # 查询所有数据表
        cursor.execute("SELECT * FROM alert_info")
        alerts = cursor.fetchall()

        cursor.execute("SELECT * FROM flight_info")
        flights = cursor.fetchall()

        cursor.execute("SELECT * FROM airport_info")
        airports = cursor.fetchall()

        cursor.execute("SELECT * FROM weather_info")
        weather = cursor.fetchall()

    except Exception as e:
        print(f"Error: {e}")
        alerts, flights, airports, weather = [], [], [], []
    finally:
        cursor.close()
        db.close()

    return render_template(
        "airport_staff_dashboard.html",
        alerts=alerts, flights=flights, airports=airports, weather=weather
    )

# 添加航班信息
@app.route('/airport_staff/add_flight', methods=['POST'])
def airport_staff_add_flight():
    """添加航班信息"""
    flight_number = request.form.get("flight_number")
    departure = request.form.get("departure")
    arrival = request.form.get("arrival")
    scheduled_time = request.form.get("scheduled_time")
    status = request.form.get("status")

    try:
        db = pymysql.connect(host="localhost", user="root", password=mysql_pwd, database=db_name, charset="utf8")
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO flight_info (FlightNumber, Departure, Arrival, ScheduledTime, Status) VALUES (%s, %s, %s, %s, %s)",
            (flight_number, departure, arrival, scheduled_time, status)
        )

        db.commit()
        flash("航班添加成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("添加航班失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for('airport_staff_dashboard'))

# 删除航班信息
@app.route('/airport_staff/delete_flight', methods=['POST'])
def airport_staff_delete_flight():
    """删除航班信息"""
    flight_id = request.form.get("flight_id")
    if not flight_id:
        flash("缺少航班ID", "error")
        return redirect(url_for("airport_staff_dashboard"))

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM flight_info WHERE FlightID = %s", (flight_id,))

        db.commit()
        flash("航班删除成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("删除航班失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("airport_staff_dashboard"))

# 修改航班信息
@app.route('/airport_staff/update_flight', methods=['POST'])
def airport_staff_update_flight():
    """修改航班信息"""

    flight_id = request.form.get("flight_id")
    flight_number = request.form.get("flight_number")
    departure = request.form.get("departure")
    arrival = request.form.get("arrival")
    scheduled_time = request.form.get("scheduled_time")
    status = request.form.get("status")

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE flight_info SET FlightNumber=%s, Departure=%s, Arrival=%s, ScheduledTime=%s, Status=%s WHERE FlightID=%s",
            (flight_number, departure, arrival, scheduled_time, status, flight_id)
        )
        db.commit()
        flash("航班信息更新成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("更新航班信息失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("airport_staff_dashboard"))

# 添加机场信息
@app.route('/airport_staff/add_airport', methods=['POST'])
def airport_staff_add_airport():
    """添加机场信息"""

    airport_name = request.form.get("airport_name")
    location_code = request.form.get("location_code")
    location = request.form.get("location")

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO airport_info (AirportName, LocationCode, Location) VALUES (%s, %s, %s)",
            (airport_name, location_code, location)
        )

        db.commit()
        flash("机场信息添加成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("添加机场信息失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("airport_staff_dashboard"))

# 删除机场信息
@app.route('/airport_staff/delete_airport', methods=['POST'])
def airport_staff_delete_airport():
    """删除机场信息"""
    airport_id = request.form.get("airport_id")

    if not airport_id:
        flash("缺少机场ID", "error")
        return redirect(url_for("airport_staff_dashboard"))

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM airport_info WHERE AirportID = %s", (airport_id,))

        db.commit()
        flash("机场删除成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("删除机场失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("airport_staff_dashboard"))

# 修改机场信息
@app.route('/airport_staff/update_airport', methods=['POST'])
def airport_staff_update_airport():

    """修改机场信息"""
    airport_id = request.form.get("airport_id")
    airport_name = request.form.get("airport_name")
    location_code = request.form.get("location_code")
    location = request.form.get("location")

    if not (airport_id and airport_name and location_code and location):
        flash("所有字段均为必填", "error")
        return redirect(url_for("airport_staff_dashboard"))

    try:
        db = get_db_connection()
        cursor = db.cursor()

        # 更新机场信息
        cursor.execute(
            "UPDATE airport_info SET AirportName=%s, LocationCode=%s, Location=%s WHERE AirportID=%s",
            (airport_name, location_code, location, airport_id)
        )

        db.commit()
        flash("机场信息更新成功", "success")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        flash("更新机场信息失败", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("airport_staff_dashboard"))



# 管理员主页面
@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
    """管理员主页面"""
    return render_template('admin_dashboard.html')


# 系统日志页面
@app.route('/system_log', methods=['GET'])
def system_log():
    """查看系统日志"""
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM system_logs")
    logs = cursor.fetchall()
    return render_template('system_log.html', logs=logs)


# 气象信息管理页面
@app.route('/admin_weather', methods=['GET', 'POST'])
def admin_weather():

    """查看和添加气象信息"""
    if request.method == 'POST':  # 添加气象信息
        data = (
            request.form.get('location'),
            request.form.get('temperature'),
            request.form.get('wind_speed'),
            request.form.get('wind_direction'),
            request.form.get('humidity'),
        )

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO weather_info (LocationID, Temperature, WindSpeed, WindDirection, Humidity, TimeStamp) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP)",
            data,
        )

        db.commit()
        flash("气象信息添加成功", "success")

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM weather_info")
    weather_data = cursor.fetchall()  # 使用 fetchall() 获取查询结果
    return render_template('admin_weather.html', weather_data=weather_data)


# 修改气象信息
@app.route('/admin_update_weather', methods=['GET', 'POST'])
def admin_update_weather():

    weather_id = request.args.get('weather_id')

    """修改气象信息"""
    if request.method == 'POST':
        data = (
            request.form.get('location'),
            request.form.get('temperature'),
            request.form.get('wind_speed'),
            request.form.get('wind_direction'),
            request.form.get('humidity'),
        )

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE weather_info SET Location=%s, Temperature=%s, WindSpeed=%s, WindDirection=%s, Humidity=%s WHERE WeatherID=%s",
            (*data, weather_id),
        )

        db.commit()
        flash("气象信息更新成功", "success")
    except Exception as e:
        flash(f"更新气象信息失败: {e}", "error")
    finally:
        cursor.close()
        db.close()
        return redirect(url_for('admin_weather'))

    # 预填充数据
    db = get_db_connection()
    cursor = db.cursor()

    weather_data = cursor.execute("SELECT * FROM weather_info WHERE WeatherID = %s", (weather_id,))
    return render_template('admin_update_weather.html', weather=weather_data[0])


# 删除气象信息
@app.route('/delete_weather', methods=['POST'])
def delete_weather():

    weather_id = request.args.get('weather_id')

    """删除气象信息"""
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM weather_info WHERE WeatherID = %s", (weather_id,))

        db.commit()
        flash("气象信息删除成功", "success")
    except Exception as e:
        flash(f"删除气象信息失败: {e}", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for('admin_weather'))


# 预警信息管理页面
@app.route('/admin_warning', methods=['GET', 'POST'])
def admin_warning():

    """查看和添加预警信息"""

    # 处理添加预警信息
    if request.method == 'POST': 
        # 获取表单数据
        alert_type = request.form.get('alert_type')
        severity = request.form.get('severity')
        location = request.form.get('location')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        details = request.form.get('details')

        data = (alert_type, severity, location, start_time, end_time, details)

        # 数据库连接
        db = get_db_connection()
        cursor = db.cursor()

        # 插入新的预警信息
        cursor.execute(
            "INSERT INTO alert_info (AlertType, Severity, LocationID, StartTime, EndTime, Details) VALUES (%s, %s, %s, %s, %s, %s)",
            data,
        )

        db.commit()
        flash("预警信息添加成功", "success")
        db.close()


    # 获取所有预警信息
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alert_info ORDER BY AlertID DESC")
    alerts = cursor.fetchall()  # 获取所有查询结果
    db.close()

    return render_template('admin_warning.html', alerts=alerts)

# 修改预警信息
@app.route('/admin_update_warning/<int:alert_id>', methods=['GET', 'POST'])
def admin_update_warning():

    alert_id = request.args.get('alert_id')

    """修改预警信息"""
    if request.method == 'POST':
        data = (
            request.form.get('alert_type'),
            request.form.get('severity'),
            request.form.get('details'),

            request.form.get('alert_id'),
            request.form.get('details'),
        )

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE alert_info SET AlertType=%s, Severity=%s, Details=%s WHERE AlertID=%s",
            (*data, alert_id),
        )

        db.commit()
        flash("预警信息更新成功", "success")
        return redirect(url_for('admin_warning'))

    # 预填充数据
    db = get_db_connection()
    cursor = db.cursor()

    alert_data = cursor.execute("SELECT * FROM alert_info WHERE AlertID = %s", (alert_id,))
    return render_template('admin_warning.html', alert=alert_data[0])


# 删除预警信息
@app.route('/delete_warning', methods=['POST'])
def delete_warning():
    """删除预警信息"""

    alert_id = request.form.get('alert_id')

    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM alert_info WHERE AlertID = %s", (alert_id,))

        db.commit()
        flash("预警信息删除成功", "success")
    except Exception as e:
        flash(f"删除预警信息失败: {e}", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for('admin_warning'))


# 机场信息管理页面
@app.route('/admin_airport', methods=['GET', 'POST'])
def admin_airport():
    if request.method == 'POST':  # 添加机场信息
        data = (
            request.form.get('airport_name'),
            request.form.get('location_code'),
            request.form.get('location'),
        )

        db = get_db_connection()
        cursor = db.cursor()    

        cursor.execute(
            "INSERT INTO airport_info (AirportName, LocationCode, Location) VALUES (%s, %s, %s)",
            data,
        )

        db.commit()
        flash("机场信息添加成功", "success")

    # 显示所有机场信息
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM airport_info")
    airports = cursor.fetchall()  # 使用 fetchall() 获取查询结果
    return render_template('admin_airport.html', airports=airports)


# 修改机场信息
@app.route('/admin_update_airport', methods=['GET', 'POST'])
def admin_update_airport():
    """修改机场信息"""
    airport_id = request.form.get('airport_id')
    if request.method == 'POST':
        data = (
            request.form.get('airport_name'),
            request.form.get('location_code'),
            request.form.get('location'),
        )

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE airport_info SET AirportName=%s, LocationCode=%s, Location=%s WHERE AirportID=%s",
            (*data, airport_id),
        )

        db.commit()
        flash("机场信息更新成功", "success")
        return redirect(url_for('admin_airport'))

    # 预填充数据
    db = get_db_connection()
    cursor = db.cursor()
    airport_data = cursor.execute("SELECT * FROM airport_info WHERE AirportID = %s", (airport_id,))
    return render_template('admin_airport.html', airport=airport_data[0])


# 删除机场信息
@app.route('/delete_airport', methods=['POST'])
def delete_airport():
    """删除机场信息"""

    airport_id = request.form.get('airport_id')

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM airport_info WHERE AirportID = %s", (airport_id,) )
        
        db.commit()
        flash("机场信息删除成功", "success")
    except Exception as e:
        flash(f"删除机场信息失败: {e}", "error")
    finally:
        cursor.close()
        db.close()

    return redirect(url_for('admin_airport'))


# 航班信息管理页面
@app.route('/admin_flight', methods=['GET', 'POST'])
def admin_flight():
    """查看和添加航班信息"""
    if request.method == 'POST':  # 添加航班信息
        data = (
            request.form.get('flight_number'),
            request.form.get('departure'),
            request.form.get('arrival'),
            request.form.get('scheduled_time'),
            request.form.get('status'),
        )

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO flight_info (FlightNumber, Departure, Arrival, ScheduledTime, Status) VALUES (%s, %s, %s, %s, %s)",
            data,
        )
        db.commit()
        cursor.close()
        db.close()

        flash("航班信息添加成功", "success")

    # 查看航班信息
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM flight_info")
    flights = cursor.fetchall() 


    return render_template('admin_flight.html', flights=flights)

# 修改航班信息
@app.route('/admin_update_flight', methods=['GET', 'POST'])
def admin_update_flight():
    flight_id = request.form.get('flight_id')

    """修改航班信息"""
    if request.method == 'POST':
        data = (
            request.form.get('flight_number'),
            request.form.get('departure'),
            request.form.get('arrival'),
            request.form.get('scheduled_time'),
            request.form.get('status'),
        )

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE flight_info SET FlightNumber=%s, Departure=%s, Arrival=%s, ScheduledTime=%s, Status=%s WHERE FlightID=%s",
            (*data, flight_id),
        )

        db.commit()
        flash("航班信息更新成功", "success")
        return redirect(url_for('admin_flight'))

    # 预填充数据
    db = get_db_connection()
    cursor = db.cursor()
    flight_data = cursor.execute("SELECT * FROM flight_info WHERE FlightID = %s", (flight_id,))
    return render_template('admin_update_flight.html', flight=flight_data[0])


# 删除航班信息
@app.route('/delete_flight', methods=['POST'])
def delete_flight():

    flight_id = request.form.get('flight_id')
    """删除航班信息"""
    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM flight_info WHERE FlightID = %s", (flight_id,))

        db.commit()
        flash("航班信息删除成功", "success")
    except Exception as e:
        flash(f"删除航班信息失败: {e}", "error")

    finally:
        cursor.close()
        db.close()

    return redirect(url_for('admin_flight'))


# 用户信息管理页面
@app.route('/admin_user', methods=['GET'])
def admin_user():
    """查看用户信息"""
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall() 

    return render_template('admin_user.html', users=users)


# 删除用户
@app.route('/delete_user', methods=['POST'])
def delete_user():

    user_id = request.form.get('user_id')

    """删除用户"""

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM user WHERE UserID = %s", (user_id,))

    db.commit()
    flash("用户删除成功", "success")
    cursor.close()
    db.close()

    return redirect(url_for('admin_user'))



def parse_args():
    """parse the command line args

    Returns:
        args: a namespace object including args
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--mysql_pwd',
        help='the mysql root password',
        default="0728"
    )
    parser.add_argument(
        '--db_name',
        help='which database to use',
        default="weather_system"
    )

    args = parser.parse_args()
    return args


if __name__ == '__main__':

    # with app.app_context():
    #     db.create_all()  # 创建数据库表
    #     insert_data()  # 插入数据

    args = parse_args()
    mysql_pwd = args.mysql_pwd
    db_name = args.db_name
    app.run(host='localhost', port='4090')
