import dataclasses as dc
import typing as t


@dc.dataclass(frozen=True)
class Parameters:
    max_new_tokens: t.Optional[int] = 1024
    temperature: t.Optional[float] = 1.0
    top_p: t.Optional[float] = 1.0
    repetition_penalty: t.Optional[float] = 1.0
