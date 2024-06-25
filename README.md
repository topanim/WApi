
# WApi: Library to simplify api development

[![PyPI version](https://badge.fury.io/py/whaox-wapi.svg)](https://badge.fury.io/py/whaox-wapi)

## Libraries used:
* [jsons](https://github.com/ramonhagenaars/jsons)
* [requests](https://github.com/psf/requests)
* [aiohttp](https://github.com/aio-libs/aiohttp)

## Features

* Routes
* Serialization
* Asynchrony
* Request Params
	* Smart substitution

## Installation

 You can install the latest version with the command:
 
```commandline
pip install whaox-wapi
```

## • Routes

> You can create paths as you like, splitting your api-client into modules

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
requests.get("https://example.com/wapi/path")
```

## • Serialization

> The library deserializes the received data according to the type that you specify in the `_T` parameter of the decorator. 
> 
> NOTE: The specified type must be json serializable - these are the base types and classes marked with the `@dataclass` annotation

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

## • Asynchrony

> You can make the query asynchronous simply by adding an `async` keyword.

```python
@Route("https://example.com")
class WApi:

  @GET("/person")
  async def person(self): pass

```
```python
person = await api.person(params={"id": 1})
```

## • Request Params

> You can flexibly add parameters to request passing relevant attributes.

```python
@dataclass
class GetPersonRequest:
  id: int
  
@dataclass
class CreatePersonRequest:
  name: str


@Route("https://example.com")
class WApi:

  @POST("/person")
  def create_person(self, body: CreatePersonRequest | dict): pass
	
  @Route("/person") 
  @GET("/")
  def person(self, params: GetPersonRequest | dict): pass

```
```python
api.person(params={"id": 1})
api.create_person(body={"name": "john"})
# or
api.person(params=GetPersonRequest(1))
api.create_person(body=CreatePersonRequest("john"))
```


### • • Smart substitution

> The library understands what variables you used during formatting and will not substitute them into the path parameters.

```python
@dataclass
class GetPersonRequest:
    id: int
    preview: bool

@Route("https://example.com")
class WApi:

  @Route("/person")
  @GET("/{id}")
  def person(self, params: GetPersonRequest): pass
```

```python
person = api.person(params=GetPersonRequest(1, true))
# eq
person = requests.get("https://example.com/person/1?preview=true")
```

