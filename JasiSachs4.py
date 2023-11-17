import csv, re, os


def main():
	os.chdir(os.path.dirname(__file__))

	r_mode_input = open('input.txt', 'r')

	w_mode_csv = open('output.csv', 'w', newline='')
	csv_writer = csv.writer(w_mode_csv, delimiter=',')

	w_mode_txt = open('output.txt', 'w', newline='')

	csv_writer.writerow(['Email', 'Day', 'Date', 'Month', 'Year', 'Time'])

	email_dict = {}
	email_count = 0
	email_str = 'Email'
	w_mode_txt.write(f'{email_str:<40} - Count\n')

	for line in r_mode_input:
		if re.match('^From .*', line):
			line_list = line.split()
			line_list_sorted = [line_list[1], line_list[2], line_list[4], line_list[3], line_list[6], line_list[5].lstrip('0')]
			csv_writer.writerow(line_list_sorted)

		if re.match('^From: ', line):
			email_address = re.findall('^From: (.*)', line)[0]
			email_dict[email_address] = email_dict.get(email_address, 0) + 1
			email_count += 1

	for key in email_dict:
		w_mode_txt.write(f'{key:<40} - {email_dict[key]}\n')

	w_mode_txt.write('-'*49+'\n')
	w_mode_txt.write(f'{"Total emails":<40} - {email_count}\n')

	r_mode_input.close()
	w_mode_csv.close()
	w_mode_txt.close()


if __name__ == "__main__":
	main()