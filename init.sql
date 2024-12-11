-- 创建数据库
CREATE DATABASE weather_system;

-- 创建气象信息表
CREATE TABLE weather_info (
    WeatherID INT PRIMARY KEY,
    LocationID INT NOT NULL,
    Timestamp DATETIME NOT NULL,
    Temperature FLOAT NOT NULL,
    WindSpeed FLOAT NOT NULL,
    WindDirection VARCHAR(10) NOT NULL,
    Humidity FLOAT NOT NULL,
    Visibility FLOAT,
    Pressure FLOAT
);

-- 创建预警信息表
CREATE TABLE alert_info (
    AlertID INT PRIMARY KEY,
    AlertType VARCHAR(50) NOT NULL,
    Severity ENUM('Low', 'Medium', 'High') NOT NULL,
    LocationID INT NOT NULL,
    StartTime DATETIME NOT NULL,
    EndTime DATETIME,
    Details TEXT
);

-- 创建航班信息表
CREATE TABLE flight_info (
    FlightID INT PRIMARY KEY,
    FlightNumber VARCHAR(20) UNIQUE NOT NULL,
    Departure INT NOT NULL,
    Arrival INT NOT NULL,
    ScheduledTime DATETIME NOT NULL,
    Status ENUM('On Time', 'Delayed', 'Cancelled') NOT NULL DEFAULT 'On Time'
);

-- 创建机场信息表
CREATE TABLE airport_info (
    AirportID INT PRIMARY KEY,
    AirportName VARCHAR(100) NOT NULL,
    LocationCode VARCHAR(10) UNIQUE NOT NULL,
    Location VARCHAR(100)
);

-- 创建用户查询记录表
CREATE TABLE user_query_record (
    QueryID INT PRIMARY KEY,
    UserID INT NOT NULL,
    QueryTime DATETIME NOT NULL,
    FlightID INT NOT NULL,
    QueryResult TEXT
);

-- 创建用户表
CREATE TABLE user (
    UserID INT PRIMARY KEY,
    Username VARCHAR(25) UNIQUE NOT NULL,
    Password VARCHAR(16) NOT NULL,
    Role ENUM('Admin', 'Passenger', 'AirlineStaff') NOT NULL,
    Phone VARCHAR(11)
);

-- 创建系统日志表
CREATE TABLE system_logs (
    LogID INT PRIMARY KEY,
    OperateTime DATETIME NOT NULL,
    UserID INT NOT NULL,
    Ttype VARCHAR(255) NOT NULL,
    Details TEXT,
    FOREIGN KEY (UserID) REFERENCES user(UserID)
);

-- 创建航班与机场关联表
CREATE TABLE flight_airport (
    FlightID INT NOT NULL,
    AirportID INT NOT NULL,
    PRIMARY KEY (FlightID, AirportID),
    FOREIGN KEY (FlightID) REFERENCES flight_info(FlightID),
    FOREIGN KEY (AirportID) REFERENCES airport_info(AirportID)
);

-- 创建预警与机场关联表
CREATE TABLE alert_airport (
    AlertID INT NOT NULL,
    AirportID INT NOT NULL,
    PRIMARY KEY (AlertID, AirportID),
    FOREIGN KEY (AlertID) REFERENCES alert_info(AlertID),
    FOREIGN KEY (AirportID) REFERENCES airport_info(AirportID)
);
-- 创建气象与机场关联表
CREATE TABLE weather_airport (
    WeatherID INT NOT NULL,
    AirportID INT NOT NULL,
    PRIMARY KEY (WeatherID, AirportID),
    FOREIGN KEY (WeatherID) REFERENCES weather_info(WeatherID),
    FOREIGN KEY (AirportID) REFERENCES airport_info(AirportID)
);
-- 创建航班与预警关联表
CREATE TABLE flight_alert (
    FlightID INT NOT NULL,
    AlertID INT NOT NULL,
    PRIMARY KEY (FlightID, AlertID),
    FOREIGN KEY (FlightID) REFERENCES flight_info(FlightID),
    FOREIGN KEY (AlertID) REFERENCES alert_info(AlertID)
);
-- 创建航班与用户关联表
CREATE TABLE flight_user (
    FlightID INT NOT NULL,
    UserID INT NOT NULL,
    PRIMARY KEY (FlightID, UserID),
    FOREIGN KEY (FlightID) REFERENCES flight_info(FlightID),
    FOREIGN KEY (UserID) REFERENCES user(UserID)
);
-- 创建预警与用户关联表
CREATE TABLE alert_user (
    AlertID INT NOT NULL,
    UserID INT NOT NULL,
    PRIMARY KEY (AlertID, UserID),
    FOREIGN KEY (AlertID) REFERENCES alert_info(AlertID),
    FOREIGN KEY (UserID) REFERENCES user(UserID)
);

-- 插入初始数据
-- 插入气象信息
INSERT INTO weather_info (WeatherID, LocationID, Timestamp, Temperature, WindSpeed, WindDirection, Humidity, Visibility, Pressure)
VALUES
(1, 1, '2023-12-01 12:00:00', 15.5, 5.2, 'NE', 65.0, 10.0, 1012.5),
(2, 2, '2023-12-01 13:00:00', 20.3, 3.8, 'N', 55.0, 8.0, 1010.2);

-- 插入预警信息
INSERT INTO alert_info (AlertID, AlertType, Severity, LocationID, StartTime, EndTime, Details)
VALUES
(1, '雷暴', 'High', 1, '2023-12-02 10:00:00', '2023-12-02 18:00:00', '预计区域内将发生强雷暴，请注意避险'),
(2, '台风', 'Medium', 2, '2023-12-03 08:00:00', '2023-12-03 22:00:00', '中度台风预计影响航班，请注意调整行程');

-- 插入航班信息
INSERT INTO flight_info (FlightID, FlightNumber, Departure, Arrival, ScheduledTime, Status)
VALUES
(1, 'CA123', 1, 2, '2023-12-03 15:30:00', 'Delayed'),
(2, 'MU456', 2, 3, '2023-12-03 10:00:00', 'On Time');

-- 插入机场信息
INSERT INTO airport_info (AirportID, AirportName, LocationCode, Location)
VALUES
(1, '北京首都国际机场', 'PEK', '北京'),
(2, '上海浦东国际机场', 'PVG', '上海'),
(3, '广州白云国际机场', 'CAN', '广州');

-- 插入用户
INSERT INTO user (UserID, Username, Password, Role, Phone)
VALUES
(1, 'admin', 'admin123', 'Admin', '19157959839'),
(2, 'john', 'password123', 'Passenger', '15538275803');

-- 插入用户查询记录
INSERT INTO user_query_record (QueryID, UserID, QueryTime, FlightID, QueryResult)
VALUES
(1, 2, '2023-12-03 09:00:00', 1, '航班CA123已延误'),
(2, 2, '2023-12-03 12:30:00', 2, '航班MU456准时起飞');

-- 插入系统日志
INSERT INTO system_logs (LogID, OperateTime, UserID, Ttype, Details)
VALUES
(1, '2023-12-03 14:00:00', 1, '登录', '用户admin登录系统'),
(2, '2023-12-03 14:15:00', 2, '查询', '用户john_doe查询航班CA123信息');


-- 插入气象信息
INSERT INTO weather_info (WeatherID, LocationID, Timestamp, Temperature, WindSpeed, WindDirection, Humidity, Visibility, Pressure)
VALUES
(11, 11, '2024-01-01 09:00:00', 15.0, 4.0, 'NE', 55.0, 12.0, 1013.5),
(12, 12, '2024-01-02 10:00:00', 18.0, 7.5, 'W', 70.0, 15.0, 1010.0),
(13, 13, '2024-01-02 11:00:00', 10.0, 5.0, 'S', 80.0, 8.0, 1014.0),
(14, 14, '2024-01-02 12:00:00', 25.0, 4.0, 'SW', 65.0, 20.0, 1011.0),
(15, 15, '2024-01-03 08:00:00', 22.3, 6.0, 'SE', 70.0, 14.0, 1008.5),
(16, 16, '2024-01-03 09:00:00', 15.5, 4.0, 'N', 75.0, 10.0, 1010.0),
(17, 17, '2024-01-04 06:00:00', 5.0, 10.0, 'W', 85.0, 5.0, 1007.5),
(18, 18, '2024-01-05 10:00:00', 12.0, 3.5, 'NW', 65.0, 12.0, 1012.0),
(19, 19, '2024-01-06 14:00:00', 30.0, 2.0, 'E', 50.0, 20.0, 1005.0),
(20, 10, '2024-01-06 15:00:00', 20.0, 7.0, 'S', 68.0, 9.0, 1011.5),
(21, 11, '2024-01-07 09:00:00', 21.0, 6.0, 'E', 65.0, 11.0, 1009.8),
(22, 12, '2024-01-07 11:00:00', 19.5, 5.5, 'NE', 72.0, 14.0, 1012.3),
(23, 13, '2024-01-07 13:00:00', 23.0, 3.5, 'SE', 62.0, 10.0, 1010.0),
(24, 14, '2024-01-07 15:00:00', 28.0, 2.5, 'SW', 48.0, 18.0, 1008.0),
(25, 15, '2024-01-08 08:00:00', 9.0, 3.5, 'W', 70.0, 8.0, 1011.0),
(26, 16, '2024-01-08 10:00:00', 25.0, 5.0, 'NE', 58.0, 12.0, 1009.5),
(27, 17, '2024-01-08 12:00:00', 29.5, 4.5, 'E', 53.0, 15.0, 1006.0),
(28, 18, '2024-01-08 14:00:00', 16.5, 6.5, 'N', 68.0, 9.0, 1013.0),
(29, 19, '2024-01-08 16:00:00', 35.0, 1.0, 'NW', 40.0, 25.0, 1007.0);

-- 插入预警信息
INSERT INTO alert_info (AlertID, AlertType, Severity, LocationID, StartTime, EndTime, Details)
VALUES
(10, '暴雨', 'High', 10, '2024-01-01 00:00:00', '2024-01-01 12:00:00', '区域内预计暴雨，请注意安全'),
(11, '台风', 'Medium', 11, '2024-01-02 10:00:00', '2024-01-02 18:00:00', '台风影响，请调整出行计划'),
(12, '大雪', 'High', 12, '2024-01-03 08:00:00', '2024-01-03 20:00:00', '预计将出现大雪天气，航班可能延误'),
(13, '冰雹', 'High', 13, '2024-01-04 15:00:00', '2024-01-04 20:00:00', '出现冰雹可能，请避免户外活动'),
(14, '雷暴', 'High', 14, '2024-01-05 10:00:00', '2024-01-05 18:00:00', '强雷暴来临，请注意避险'),
(15, '高温', 'Medium', 15, '2024-01-06 08:00:00', '2024-01-06 20:00:00', '高温天气，注意防暑'),
(16, '寒潮', 'Low', 16, '2024-01-07 00:00:00', '2024-01-07 12:00:00', '寒潮来袭，请注意保暖'),
(17, '大雾', 'Low', 17, '2024-01-08 05:00:00', '2024-01-08 10:00:00', '大雾天气，能见度低，请谨慎驾驶'),
(18, '沙尘暴', 'High', 18, '2024-01-09 10:00:00', '2024-01-09 20:00:00', '区域内沙尘暴天气，尽量减少外出'),
(19, '暴雪', 'High', 19, '2024-01-10 00:00:00', '2024-01-10 12:00:00', '暴雪来袭，请减少外出'),
(20, '台风', 'High', 10, '2024-01-11 08:00:00', '2024-01-11 18:00:00', '台风影响，请调整出行计划'),
(21, '暴雨', 'High', 11, '2024-01-12 00:00:00', '2024-01-12 12:00:00', '区域内预计暴雨，请注意安全'),
(22, '大雪', 'High', 12, '2024-01-13 08:00:00', '2024-01-13 20:00:00', '预计将出现大雪天气，航班可能延误'),
(23, '冰雹', 'High', 13, '2024-01-14 15:00:00', '2024-01-14 20:00:00', '出现冰雹可能，请避免户外活动'),
(24, '雷暴', 'High', 14, '2024-01-15 10:00:00', '2024-01-15 18:00:00', '强雷暴来临，请注意避险'),
(25, '高温', 'Medium', 15, '2024-01-16 08:00:00', '2024-01-16 20:00:00', '高温天气，注意防暑'),
(26, '寒潮', 'Low', 16, '2024-01-17 00:00:00', '2024-01-17 12:00:00', '寒潮来袭，请注意保暖'),
(27, '大雾', 'Low', 17, '2024-01-18 05:00:00', '2024-01-18 10:00:00', '大雾天气，能见度低，请谨慎驾驶')
(28, '沙尘暴', 'High', 18, '2024-01-19 10:00:00', '2024-01-19 20:00:00', '区域内沙尘暴天气，尽量减少外出'),
(29, '暴雪', 'High', 19, '2024-01-20 00:00:00', '2024-01-20 12:00:00', '暴雪来袭，请减少外出');

-- 插入机场信息
INSERT INTO airport_info (AirportID, AirportName, LocationCode, Location)
VALUES
(10, '北京国际机场', 'PEK', '北京'),
(11, '上海虹桥机场', 'SHA', '上海'),
(12, '广州白云机场', 'CAN', '广州'),
(13, '深圳宝安机场', 'SZX', '深圳'),
(14, '成都天府机场', 'CTU', '成都'),
(15, '杭州萧山机场', 'HGH', '杭州'),
(16, '长沙黄花机场', 'CSX', '长沙'),
(17, '武汉天河机场', 'WUH', '武汉'),
(18, '西安咸阳机场', 'XIY', '西安'),
(19, '重庆江北机场', 'CKG', '重庆'),
(20, '昆明长水机场', 'KMG', '昆明'),
(21, '海口美兰机场', 'HAK', '海口'),
(22, '澳门国际机场', 'MFM', '澳门'),
(23, '香港国际机场', 'HKG', '香港'),
(24, '台北桃园国际机场', 'TPE', '台北'),
(25, '东京羽田机场', 'HND', '东京'),
(26, '首尔仁川国际机场', 'ICN', '首尔'),
(27, '悉尼金斯福德机场', 'SYD', '悉尼'),
(28, '洛杉矶国际机场', 'LAX', '洛杉矶');

-- 插入航班信息
INSERT INTO flight_info (FlightID, FlightNumber, Departure, Arrival, ScheduledTime, Status)
VALUES
(10, 'CA101', 10, 11, '2024-01-02 10:00:00', 'On Time'),
(11, 'MU202', 11, 12, '2024-01-02 12:00:00', 'Delayed'),
(12, 'CZ303', 12, 13, '2024-01-03 15:30:00', 'Cancelled'),
(13, 'HU404', 13, 14, '2024-01-04 09:00:00', 'On Time'),
(14, 'ZH505', 14, 15, '2024-01-05 08:15:00', 'Delayed'),
(15, 'CA606', 15, 16, '2024-01-06 11:30:00', 'On Time'),
(16, 'MU707', 16, 17, '2024-01-07 14:45:00', 'On Time'),
(17, 'CZ808', 17, 18, '2024-01-08 09:20:00', 'On Time'),
(18, 'HU909', 18, 19, '2024-01-09 10:35:00', 'On Time'),
(19, 'ZH1010', 19, 10, '2024-01-10 12:50:00', 'On Time'),
(20, 'CA1111', 10, 11, '2024-01-11 08:00:00', 'On Time'),
(21, 'MU1212', 11, 12, '2024-01-12 09:30:00', 'On Time'),
(22, 'CZ1313', 12, 13, '2024-01-13 10:00:00', 'On Time'),
(23, 'HU1414', 13, 14, '2024-01-14 11:30:00', 'On Time'),
(24, 'ZH1515', 14, 15, '2024-01-15 15:00:00', 'On Time'),
(25, 'CA1616', 15, 16, '2024-01-16 08:00:00', 'On Time'),
(26, 'MU1717', 16, 17, '2024-01-17 09:30:00', 'On Time'),
(27, 'CZ1818', 17, 18, '2024-01-18 10:00:00', 'On Time');



-- 插入用户信息
INSERT INTO user (UserID, Username, Password, Role, Phone)
VALUES
(10, 'admin10', 'adminpass10', 'Admin', '13800000010'),
(11, 'passenger11', 'pass1234', 'Passenger', '13800000011'),
(12, 'staff12', 'staffpass12', 'AirlineStaff', '13800000012'),
(13, 'guest13', 'guestpass13', 'Passenger', '13800000013'),
(14, 'user14', 'userpass14', 'Passenger', '13800000014'),
(15, 'admin15', 'adminpass15', 'Admin', '13800000015'),
(16, 'passenger16', 'pass1234', 'Passenger', '13800000016'),
(17, 'staff17', 'staffpass17', 'AirlineStaff', '13800000017'),
(18, 'guest18', 'guestpass18', 'Passenger', '13800000018'),
(19, 'user19', 'userpass19', 'Passenger', '13800000019'),
(20, 'admin20', 'adminpass20', 'Admin', '13800000020'),
(21, 'passenger21', 'pass1234', 'Passenger', '13800000021'),
(22, 'staff22', 'staffpass22', 'AirlineStaff', '13800000022'),
(23, 'guest23', 'guestpass23', 'Passenger', '13800000023'),
(24, 'user24', 'userpass24', 'Passenger', '13800000024'),
(25, 'admin25', 'adminpass25', 'Admin', '13800000025');

-- 插入用户查询记录
INSERT INTO user_query_record (QueryID, UserID, QueryTime, FlightID, QueryResult)
VALUES
(10, 10, '2024-01-02 08:00:00', 10, '航班CA101准时起飞'),
(11, 11, '2024-01-02 09:30:00', 11, '航班MU202延误'),
(12, 12, '2024-01-03 10:00:00', 12, '航班CZ303已取消'),
(13, 13, '2024-01-04 11:30:00', 13, '航班HU404准时起飞'),
(14, 14, '2024-01-05 15:00:00', 14, '航班ZH505延误'),
(15, 10, '2024-01-06 08:00:00', 10, '航班CA101准时起飞'),
(16, 11, '2024-01-06 09:30:00', 11, '航班MU202延误'),
(17, 12, '2024-01-07 10:00:00', 12, '航班CZ303已取消'),
(18, 13, '2024-01-08 11:30:00', 13, '航班HU404准时起飞'),
(19, 14, '2024-01-09 15:00:00', 14, '航班ZH505延误'),
(20, 10, '2024-01-10 08:00:00', 10, '航班CA101准时起飞'),
(21, 11, '2024-01-10 09:30:00', 11, '航班MU202延误'),
(22, 12, '2024-01-11 10:00:00', 12, '航班CZ303已取消'),
(23, 13, '2024-01-12 11:30:00', 13, '航班HU404准时起飞');


-- 插入系统日志
INSERT INTO system_logs (LogID, OperateTime, UserID, Ttype, Details)
VALUES
(10, '2024-01-01 10:00:00', 10, '登录', '用户 admin10 登录系统'),
(11, '2024-01-02 09:00:00', 11, '查询', '用户 passenger11 查询航班 CA101 信息'),
(12, '2024-01-03 11:00:00', 12, '查询', '用户 staff12 查询天气信息'),
(13, '2024-01-04 14:00:00', 13, '登录', '用户 guest13 登录系统'),
(14, '2024-01-05 08:00:00', 14, '查询', '用户 user14 查询航班 ZH505 信息'),
(15, '2024-01-06 12:00:00', 10, '登出', '用户 admin10 登出系统'),
(16, '2024-01-07 15:00:00', 11, '查询', '用户 passenger11 查询航班 MU202 信息'),
(17, '2024-01-08 09:00:00', 12, '查询', '用户 staff12 查询航班 CZ303 信息'),
(18, '2024-01-09 11:00:00', 13, '登录', '用户 guest13 登出系统'),
(19, '2024-01-10 14:00:00', 14, '查询', '用户 user14 查询航班 HU404 信息'),
(20, '2024-01-11 08:00:00', 10, '登录', '用户 admin10 登录系统'),
(21, '2024-01-12 09:00:00', 11, '查询', '用户 passenger11 查询航班 CA101 信息'),
(22, '2024-01-13 11:00:00', 12, '查询', '用户 staff12 查询天气信息');


--创建用户视图
-- 创建管理员视图
CREATE VIEW admin_flight_view AS
SELECT 
    f.FlightID,
    f.FlightNumber,
    dep.AirportName AS DepartureAirport,
    arr.AirportName AS ArrivalAirport,
    f.ScheduledTime,
    f.Status
FROM 
    flight_info f
JOIN 
    airport_info dep ON f.Departure = dep.AirportID
JOIN 
    airport_info arr ON f.Arrival = arr.AirportID;

-- 创建普通用户视图
CREATE VIEW user_flights_view AS
SELECT 
    f.FlightID,
    f.FlightNumber,
    dep.AirportName AS DepartureAirport,
    arr.AirportName AS ArrivalAirport,
    f.ScheduledTime,
    f.Status
FROM 
    flight_info f
JOIN 
    airport_info dep ON f.Departure = dep.AirportID
JOIN 
    airport_info arr ON f.Arrival = arr.AirportID
WHERE 
    f.Status IN ('On Time', 'Delayed');


--创建触发器
-- 记录用户登录日志触发器，当用户登录时，自动记录到登录日志表中
DELIMITER //
CREATE TABLE login_logs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    LoginTime DATETIME NOT NULL,
    FOREIGN KEY (UserID) REFERENCES user(UserID)
);
//
DELIMITER ;

-- 更新航班状态触发器，根据起飞时间更新航班状态
DELIMITER //
CREATE TRIGGER update_flight_status
BEFORE INSERT ON flight_info
FOR EACH ROW
BEGIN
    IF NEW.ScheduledTime < NOW() THEN
        SET NEW.Status = 'Delayed';
    ELSE
        SET NEW.Status = 'On Time';
    END IF;
END;
//
DELIMITER ;

--记录用户操作日志触发器，当用户表有新的登录或查询操作时，自动记录到系统日志表中
DELIMITER //
CREATE TRIGGER log_user_operation
AFTER INSERT ON user_query_record
FOR EACH ROW
BEGIN
    INSERT INTO system_logs (OperateTime, UserID, Ttype, Details)
    VALUES (NOW(), NEW.UserID, 'Query', CONCAT('User queried flight info for FlightID: ', NEW.FlightID));
END;
//
DELIMITER ;


-- 创建存储过程
-- 添加新航班
DELIMITER //
CREATE PROCEDURE AddFlight(
    IN p_FlightNumber VARCHAR(20),
    IN p_Departure INT,
    IN p_Arrival INT,
    IN p_ScheduledTime DATETIME
)
BEGIN
    DECLARE v_Status ENUM('On Time', 'Delayed', 'Cancelled');
    IF p_ScheduledTime < NOW() THEN
        SET v_Status = 'Delayed';
    ELSE
        SET v_Status = 'On Time';
    END IF;
    INSERT INTO flight_info (FlightNumber, Departure, Arrival, ScheduledTime, Status)
    VALUES (p_FlightNumber, p_Departure, p_Arrival, p_ScheduledTime, v_Status);
END;
//
DELIMITER ;

-- 获取特定机场的当前天气
DELIMITER //
CREATE PROCEDURE GetWeatherForAirport(
    IN p_AirportID INT
)
BEGIN
    SELECT w.*
    FROM weather_info w
    JOIN weather_airport wa ON w.WeatherID = wa.WeatherID
    WHERE wa.AirportID = p_AirportID
    ORDER BY w.Timestamp DESC
    LIMIT 1;
END;
//
DELIMITER ;

-- 备份数据库
DELIMITER //
CREATE PROCEDURE BackupDatabase()
BEGIN
    DECLARE backup_file VARCHAR(255);
    SET backup_file = CONCAT('D:\Projects\weather_system', 'backup_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%S'), '.sql');
    
    -- 使用mysqldump命令进行备份
    SET @cmd = CONCAT('mysqldump -u root -0728 weather_system > ', backup_file);
    PREPARE stmt FROM @cmd;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    
    INSERT INTO system_logs (OperateTime, UserID, Ttype, Details)
    VALUES (NOW(), 1, 'Backup', CONCAT('Database backup created at ', backup_file));
END;
//
DELIMITER ;
