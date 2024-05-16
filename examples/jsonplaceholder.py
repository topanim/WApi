from dataclasses import dataclass
from typing import List

from wapi import Route, GET, POST


@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str


@dataclass
class CreatePostRequest:
    userId: int
    title: str
    body: str


@Route("https://jsonplaceholder.typicode.com")
class PostService:

    @POST("/posts", Post)
    def create(self, body: CreatePostRequest) -> Post: pass

    @GET("/posts", List[Post])
    def fetch(self) -> List[Post]: pass


print(PostService().fetch()[0])
