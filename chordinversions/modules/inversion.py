from typing import NamedTuple

from chordinversions.modules.auxiliary import get_note_name


class ChordInversion(NamedTuple):
    chord_type: str
    base_chord: tuple[int, ...]
    inversion_index: int
    base_note: int = 0

    def _note_name(self) -> str:
        if self.base_note:
            return get_note_name(self.base_note)
        else:
            return ''

    def _inversion_description(self) -> str:
        if self.inversion_index:
            return 'inversion no. {index}'.format(index=self.inversion_index)
        else:
            return 'root position'

    def __str__(self):
        return '{base_note}{chord_type}, {inversion_index}: {chord}'.format(
            chord=self.chord,
            base_note=self._note_name(),
            chord_type=self.chord_type,
            inversion_index=self._inversion_description()
        )

    @property
    def chord(self) -> list[int]:
        return [note + self.base_note for note in self.base_chord]
