from config import config as myconfig
import sysconfig
from services.general_services import print_env_var
from services.db_service import lees_db as mydbservice


for row in mydbservice():
	print(row)
