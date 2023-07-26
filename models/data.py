from pydantic import BaseModel
from typing import Optional, Literal


class GenerationAndCommitRequest(BaseModel):
    prompt: str
    num_samples: int
    repo: str
    split: Optional[list[int]] = [80, 10, 10]
    task: Literal['text_classification', 'seq2seq']
    num_labels: Optional[int] = 2