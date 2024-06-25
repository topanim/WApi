import asyncio
from dataclasses import dataclass
from typing import List

from colorama import Fore

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
    def sync_fetch(self) -> List[Post]: pass

    @GET("/posts", List[Post])
    async def async_fetch(self) -> List[Post]: pass


async def main():
    postService = PostService()

    print(
        Fore.GREEN + "create_post's response:",
        Fore.WHITE, create_post(postService)
    )

    print(
        Fore.YELLOW + "sync_request's response:",
        Fore.WHITE, sync_request(postService)
    )

    print(
        Fore.RED + "async_request's response:",
        Fore.WHITE, await async_request(postService)
    )


def create_post(postService: PostService):
    return postService.create(
        body=CreatePostRequest(
            userId=1,
            title="foo",
            body="bar"
        )
    )


def sync_request(postService: PostService):
    posts = postService.sync_fetch()
    return posts[0]


async def async_request(postService: PostService):
    posts = await postService.async_fetch()
    return posts[0]


asyncio.run(main())
