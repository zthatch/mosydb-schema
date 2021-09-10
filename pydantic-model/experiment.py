# generated by datamodel-codegen:
#   filename:  experiment.json
#   timestamp: 2021-09-10T06:28:00+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from .helper import time


class AccessControl(Enum):
    group = 'group'
    public = 'public'


class Meta(BaseModel):
    contributors: Optional[List] = Field(
        None,
        description='the ID of the contributors who designed the experiment',
        title='user@id',
    )
    date: Optional[float] = Field(
        None, description='the datetime when this protocol was created', title='date'
    )
    editions: Optional[str] = Field(
        None,
        description='the edition of the experiment - a commit id (GitHub-like)',
        title='_key',
    )


class ProtocolMeta(BaseModel):
    system: Optional[str] = Field(
        None,
        description='the target compound that is made, LiCl, Organic-compound name',
        title='system',
    )
    category: Optional[str] = Field(
        None,
        description='the category of the synthesis, e.g,: solid-state, sol-gel, solvent, etc.',
        title='system category',
    )
    motivation: Optional[str] = Field(
        None, description='main motivation for the experiment', title='main motivation'
    )
    version: Optional[str] = Field(
        None,
        description='Preferably a number, but can be also a version name',
        title='version',
    )
    description: Optional[str] = Field(
        None, description='a description about the experiment', title='description'
    )
    free_text: Optional[str] = Field(
        None,
        description='a free text description about the experiment',
        title='free text',
    )


class Executed(BaseModel):
    executed: Optional[bool] = Field(
        None, description='mark if an experiment was ever executed', title='executed'
    )
    time: Optional[time.Time] = Field(
        None, description='the time an experiment was executed'
    )
    notes: Optional[str] = Field(
        None, description='a note about the experiment - free', title='notes'
    )
    events: Optional[List] = Field(None, description="event id's", title='event@ids')
    outputs: Optional[List] = Field(None, description="output id's", title='_key')


class Experiment(BaseModel):
    _id: Optional[str] = Field(
        None,
        alias='@id',
        description='unique ID for an experiment',
        title='experiment @id',
    )
    access_control: Optional[AccessControl] = Field(
        None, description='who can access the experiment information', title='_key'
    )
    meta: Optional[Meta] = Field(
        None, description='metadata of an experiment', title='_key'
    )
    protocol_meta: Optional[ProtocolMeta] = Field(None, title='protocol')
    executed: Optional[Executed] = Field(
        None, description='the executed protocols', title='executed'
    )