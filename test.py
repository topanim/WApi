from dataclasses import dataclass
from typing import List

from wapi import Route, GET


@dataclass
class MetaResponse:
    message: str
    timestamp: str


@dataclass
class MemberDTO:
    id: int
    guild_id: int
    user_id: int
    name: str
    gender: str
    birthdate: str
    about: str
    lover: int
    exp: int
    lvl: int
    up_exp: int
    wallet: int


@dataclass
class FetchMembersRequest:
    meta: MetaResponse
    data: List[MemberDTO]


@Route("/{_id}/members")
class MembersService:

    @GET("/", FetchMembersRequest)
    def all(self, *, _id: int) -> FetchMembersRequest: pass


@Route("/guilds")
class GuildsService:
    members = MembersService()


@Route("http://127.0.0.1:8080")
class SawakoAPI:
    guilds = GuildsService()


sawako_api = SawakoAPI()

members = sawako_api.guilds.members.all(_id=1056553604246413313)
print(members)
