# generated by datamodel-codegen:
#   filename:  helper/time.json
#   timestamp: 2021-09-10T06:28:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Time(BaseModel):
    start_time: Optional[float] = Field(
        None, description='The time an event started', title='start time'
    )
    end_time: Optional[float] = Field(
        None, description='The time an event ended', title='end time'
    )