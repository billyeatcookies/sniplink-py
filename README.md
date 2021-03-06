<h1 align="center">
    SnipLink Py
</h1>

<h1 align="center">
    <a href="https://github.com/billyeatcookies/sniplink-py/pulls">
        <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/billyeatcookies/sniplink-py?style=for-the-badge">
    </a>
    <a href="https://github.com/billyeatcookies/sniplink-py/issues">
        <img alt="GitHub issues" src="https://img.shields.io/github/issues/billyeatcookies/sniplink-py?style=for-the-badge&logo=github">
    </a>
</h1>

<p align="center">
An API wrapper for SnipLink written in Python.</br>
Official SnipLink API docs found <a href="https://beta.sniplink.net/api/docs/index.html">here</a>.
</p>
<p align="center">
All aspects of the v1 endpoint are currently implemented.
</p>

---

## Installation

Install the package using pip as follows
```bash
pip install sniplink
```
and now you are ready to go!

---

## Usage

For example, 
- Information on a shortlink can be retrieved as such:

```py
# first of all, importing the library, in order to
# access functions provided by the library
import sniplink

# sniplink-py is powered by a backend client
# here we creates a new instance of client
client = sniplink.Client()

# get_link takes one parameter,
# public_id, that is the id of shortened link you want to fetch
client.get_link("123")
```

- creation of a shortlink can be done as follows:
```python
# first of all, importing the library, in order to
# access functions provided by the library
import sniplink

# sniplink-py is powered by a backend client
# here we creates a new instance of client
client = sniplink.Client

# create_link takes two parameters, 
# expires_in value, that is a unix timestamp
# url value, that is the url you want to shorten
client.create_link(1627168204, "https://example.com")
```

Have a look at the [samples](https://github.com/billyeatcookies/sniplink-py/tree/master/samples) provided for further usage instructions.

You can find a list of endpoints over on SnipLink's [API docs](https://beta.sniplink.net/api/docs/index.html). Each of these endpoints has an equivalent wrapper method in the library. 

## Requirements

- [requests](https://pypi.org/project/requests/)

```cmd
> pip install requests
```

## License

This project is available under a [MIT](./LICENSE.md) license.
