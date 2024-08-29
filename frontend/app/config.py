class Config:
    MYSQL_HOST = 'localhost'  # Puede ser 'localhost' si accedes desde la máquina anfitriona
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'myflaskapp'
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:32000/{MYSQL_DB}'

