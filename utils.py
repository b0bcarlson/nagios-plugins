import subprocess

def cmd(parts):
	output = subprocess.Popen(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	std_out, std_err = output.communicate()
	std_out = std_out.decode()
	std_err = std_err.decode()
	code = output.returncode
	return (std_out.split("\n"), std_err.split("\n"), code)
rcodes = ["OK", "WARN", "CRITICAL", "UNKNOWN"]
