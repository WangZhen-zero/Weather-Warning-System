class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:0728@localhost/weather_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用对象修改跟踪
    SECRET_KEY = '0728'  # Flask session 的加密秘钥
