import random
import string


def get_random_serial():
	serial = "000000000000000000"
	digits = string.digits

	while (serial == "000000000000000000"):
		serial = ""
		for i in range(18):
			serial += random.choice(digits)

	return serial


def generate_valid_checksum(serial):
	num1= 0;
	num2 = 0;
	num3 = 0;
	num4 = -5;
	serial_len = len(serial);
	ret_num = 0;

	while ((num4 < serial_len)):
		num3 = 1
		i = 1
		while (i <= 6): # ref index: 1
			num3 *= 10
			i += 1

		num2 = 0
		num5 = serial_len
		if ((num4 + 7) < num5): # ref index: 1
			num5 = (num4 + 7)

		i = num4
		while (i <= (num5 - 1)): # ref index: 2
			if (i >= 0): # ref index: 1
				num2 += (int(serial[i:i+1]) * num3)

			num3 /= 10
			i += 1

		num1+= num2
		num1%= 37
		num4 += 7

	ret_num = (num1* 100)



	num1= 0;
	num4 = 0;
	while (num4 < serial_len): # ref index: 7
		num3 = 1
		i = 1
		while (i <= 4): # ref index: 1
			num3 *= 10
			i += 1

		num2 = 0
		num5 = serial_len
		if((num4 + 5) < num5): # ref index: 1
			num5 = (num4 + 5)
		

		i = num4
		while(i <= (num5 - 1)): # ref index: 2
			if(i >= 0): # ref index: 1
				num2 += (int(serial[i:i+1]) * num3)

			num3 /= 10
			i += 1
			
		num1+= num2
		num1%= 47
		num4 += 5

	return str(int(ret_num + num1)).rjust(4, "0")


def main():
	serial = get_random_serial()		
	checksum = generate_valid_checksum(serial)

	print("""  ________              _                          _       __
 /_  __/ /_  ___  _____(_)___ ___  ________  _____(_)___ _/ /
  / / / __ \/ _ \/ ___/ / __ `__ \/ ___/ _ \/ ___/ / __ `/ / 
 / / / / / /  __(__  ) / / / / / (__  )  __/ /  / / /_/ / /  
/_/ /_/ /_/\___/____/_/_/ /_/ /_/____/\___/_/  /_/\__,_/_/   
                                                             
		""")
	print("By Xenomit\n\nSerial: %s-%s-%s-%s"%(serial[:4], serial[4:11], serial[11:], checksum))



if __name__ == "__main__":
	main()
