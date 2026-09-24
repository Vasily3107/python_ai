
# parse emails.txt into python list
emails = []

with open('ai/emails.txt', 'r') as f:
    lines = f.readlines()

lines = [i for i in lines if i != '\n']
lines = [lines[i : i + 3] for i in range(0, len(lines), 3)]
for email in lines:
    new_email = {}
    for i in email:
        k, v = i.split(': ', 1)
        new_email[k] = v[:-1]
    emails.append(new_email)


# filtering
with open('ai/spam_words.txt', 'r') as f:
    spam_words = eval(f.read())

spam_words = [i.lower() for i in spam_words]

spam_senders = []
spam_emails = []
good_emails = []

for i in emails:
    if any(word in i['text'].lower() for word in spam_words):
        spam_emails.append(i)
        spam_senders.append(i['from'])
    else:
        good_emails.append(i)


with open('ai/not_spam.txt', 'w') as f: # writing not spam
    for i in good_emails:
        for k, v in i.items():
            f.write(f'{k}: {v}\n')
        f.write('\n')

with open('ai/spam.txt', 'w') as f: # writing spam
    for i in spam_emails:
        for k, v in i.items():
            f.write(f'{k}: {v}\n')
        f.write('\n')

with open('ai/spam_senders.txt', 'w') as f: # writing spam senders
    f.write(spam_senders.__repr__())