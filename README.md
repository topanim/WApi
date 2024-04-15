# WApi: Web-Library for Python

[![PyPI version](https://badge.fury.io/py/whaox-wapi.svg)](https://badge.fury.io/py/whaox-wapi)

## Libraries used:
* [jsons](https://github.com/ramonhagenaars/jsons)
* [requests]() 


## Installation

 You can install the latest version with the command:
 
```commandline
pip install whaox-wapi
```

## • Routes 

> You can create paths as you like, splitting your client into modules

```python

@Route("https://example.com")
class WApi:
    service = Service()

@Route("/wapi")
class Service:

  @Route("/path")
  @GET("/")
  def get(self): pass	

  @POST("/path")
  def post(self): pass
```

```python 
wapi = WApi()
wapi.service.get()
# eq
requests.get("https://example.com/wapi/path/")
```

## • Serialization 

> The library deserializes the received data according to the type that you specify in the \_T parameter of the decorator. 
> 
> NOTE: The specified type must be json serializable - these are the base types and classes marked with the @dataclass annotation

```python

@dataclass
class Person:
	name: str

@Route("https://example.com")
class WApi:

  @GET("/person", _T=Person)
  def person(self) -> Person: pass

  @GET("/people", _T=List[Person])
  def people(self) -> List[Person]: pass

```

```python
api = WApi()
person = api.person()

print(person.name)
>>> "John"
```

## • Params

> You can flexibly add parameters to the path using {}. The library uses formatting from the standard library.

```python
@Route("https://example.com")
class WApi:

  @GET("/path?name={name}")
  def route(self, name: str): pass
```


### • • Auto-complete

> If you want the parameters to be set automatically, you can switch the auto flag to True.
> 
> NOTE: if auto=True, you must pass named parameters so that they are added to the path.

```python

@Route("https://example.com")
class WApi:

  @GET("/path", auto=True) # eq /path?name={name}
  def route(self, name: str): pass
```

### • • Unpacking

> In order not to pass a lot of parameters, you can pass one by calling it body, it will automatically decompose into parameters, to do this, set the unpack flag to True.
> 
> NOTE: Nested non-standard type parameters are not decomposed.

```python

@dataclass
class Person:
  name: str
  age: int  


@Route("https://example.com")
class WApi:

  @GET("/path", auto=True, unpack=True) # eq /path?name={name}&age={age}
  def route(self, body: Person): pass
```
