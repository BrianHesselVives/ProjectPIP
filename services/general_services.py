import config.config as myconfig

def print_env_var():
	print(myconfig.db_path)

if __name__ == "__main__":
	print_env_var()