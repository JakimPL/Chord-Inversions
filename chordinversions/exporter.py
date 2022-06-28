import abjad
from abjad.parsers.parser import LilyPondParser
from music21.chord import Chord
from music21.lily.translate import LilypondConverter
from music21.note import Note
from music21.note import Rest
from music21.stream import Stream
from music21.tempo import MetronomeMark

TEMPO = 120
SEQUENTIAL = False


def add_rest(stream: Stream):
    rest = Rest()
    rest.duration.type = 'half'
    stream.append(rest)


def create_sequence(iterable: list[int], stream: Stream):
    for note in iterable:
        note = Note(note)
        note.duration.type = 'quarter'
        stream.append(note)


def create_chord(iterable: list[int], stream: Stream):
    chord = Chord(iterable)
    chord.duration.type = 'whole'
    stream.append(chord)


def create_stream(iterable: list[int], tempo: int = TEMPO, sequential: bool = SEQUENTIAL):
    stream = Stream()
    tempo = MetronomeMark(number=tempo)
    stream.append(tempo)
    if sequential:
        create_sequence(iterable, stream)
    else:
        create_chord(iterable, stream)

    return stream


def to_abjad(iterable: list[int], tempo: int = TEMPO, sequential: bool = SEQUENTIAL) -> abjad.Score:
    stream = create_stream(iterable, tempo, sequential)
    ly_converter = LilypondConverter()
    ly_stream = ly_converter.lySequentialMusicFromStream(stream)

    parser = LilyPondParser('nederlands')
    staff = parser(str(ly_stream))

    abjad_tempo = abjad.MetronomeMark((1, 4), tempo)
    abjad.attach(abjad_tempo, staff[0])
    score = abjad.Score([staff])
    return score
