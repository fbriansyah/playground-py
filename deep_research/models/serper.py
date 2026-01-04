from pydantic import BaseModel

class SerperSearchParameters(BaseModel):
    q: str = Field(description="Search query")
    type: str = Field(description="Search type")
    engine: str = Field(description="Search engine")

class SerperSearchItem(BaseModel):
    title: str = Field(description="Search result title")
    link: str = Field(description="Search result link")
    snippet: str = Field(description="Search result snippet")
    position: int = Field(description="Search result position")

class SerperSearchResult(BaseModel):
    organic: list[SerperSearchItem] = Field(description="Search results")
    searchParameters: SerperSearchParameters = Field(description="Search parameters")
    credits: int = Field(description="Search credits")
