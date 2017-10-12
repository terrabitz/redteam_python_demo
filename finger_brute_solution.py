from finger import finger

##record = finger('tjtaubit', 'mtu.edu')
##print(record)

female_names_file = open('name_lists/female.txt')
male_names_file = open('name_lists/male.txt')


female_records = female_names_file.readlines()
male_records = male_names_file.readlines()

##print(female_records)

##for record in female_records:
##    name = record.split()[0]
##    print(name)

names = []
for record in female_records:
    name = record.split()[0]
    names.append(name)

for record in male_records:
    name = record.split()[0]
    names.append(name)

##print(names)

finger_db = []
for name in names:
    result = finger(name, 'mtu.edu')
    finger_db.extend(result)

##print(finger_db)
##print(len(finger_db))

emails = []
for record in finger_db:
    if 'email' in record.keys():
        emails.append(record['email'])

##print(emails)

email_file = open('emails.txt', 'w')
for email in emails:
    email_file.write(email + '\n')

email_file.close()

female_names_file.close()
male_names_file.close()
