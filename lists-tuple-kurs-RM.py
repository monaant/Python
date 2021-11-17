marketing = ["loyality program", "client promotion", "market research"]
marketing.append("public relation")
print(marketing[2])
marketing[1] = "investor relations"
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ["internal communication"]
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailMarketing1 = tuple(emailMarketing)
print(emailMarketing1)
print(emailMarketing)