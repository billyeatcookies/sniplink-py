# first of all, importing the library, in order to
# access functions provided by the library
import sniplink

# sniplink-py is powered by a backend client
# here we creates a new instance of client
client = sniplink.Client()

# create_link takes two parameters,
# expires_in value, that is a unix timestamp
# url value, that is the url you want to shorten
created_link = client.create_link(1627168204, "https://example.com")

# get_link takes one parameter,
# public_id, that is the id of shortened link you want to fetch
client.get_link(created_link.id)
