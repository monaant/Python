channels = {"Google":1480, "Email":300, "Natural Traffic":440, "Tv Spot":700 }

print(channels["Email"])

chanelsUpdate = {"Natural Traffic":520, "News":600}

channels.update(chanelsUpdate)

print(channels)

print(channels.keys())

print(channels.pop("Email"))