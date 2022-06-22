import json
import os
import pathlib

import pydub
from music21.chord import Chord
from music21.note import Note
from music21.note import Rest
from music21.stream import Stream

from chordinversions.converter import to_audio
from chordinversions.inversion import ChordInversion

SOUNDFONT_PATH = os.path.join(os.getcwd(), 'soundfont', 'st_concert.sf2')
AUDIO_FORMAT = 'wav'
CONVERT_TO_MP3 = True


class Exporter:
    def __init__(self, sequential: bool = False):
        self._sequential: bool = sequential

    @staticmethod
    def _add_rest(stream: Stream):
        rest = Rest()
        rest.duration.type = 'half'
        stream.append(rest)

    @staticmethod
    def _create_sequence(chord_inversion: ChordInversion, stream: Stream):
        for note in chord_inversion.chord:
            note = Note(note)
            note.duration.type = 'quarter'
            stream.append(note)

    @staticmethod
    def _create_chord(chord_inversion: ChordInversion, stream: Stream):
        chord = Chord(chord_inversion.chord)
        chord.duration.type = 'whole'
        stream.append(chord)

    def _create_stream(self, chord_inversion: ChordInversion):
        stream = Stream()
        if self._sequential:
            self._create_sequence(chord_inversion, stream)
        else:
            self._create_chord(chord_inversion, stream)

        return stream

    def _export_midi(self, chord_inversion: ChordInversion, chord_midi_path: str):
        stream = self._create_stream(chord_inversion)
        stream.write('midi', chord_midi_path)

    @staticmethod
    def _export_chord_inversion(chord_inversion: ChordInversion, chord_info_path: str):
        with open(chord_info_path, 'w') as file:
            json.dump(chord_inversion._asdict(), file)

    @staticmethod
    def _export_audio(chord_midi_path: str, chord_audio_path: str):
        to_audio(SOUNDFONT_PATH, chord_midi_path, chord_audio_path, out_type=AUDIO_FORMAT)
        if CONVERT_TO_MP3:
            chord_mp3_path = pathlib.Path(chord_audio_path).with_suffix('.mp3')
            sound = pydub.AudioSegment.from_wav(chord_audio_path)
            sound.export(chord_mp3_path, format='mp3')

    def export(self, chord_inversion: ChordInversion, path: str):
        chord_info_path = os.path.join(path, 'chord.json')
        chord_midi_path = os.path.join(path, 'chord.mid')
        chord_audio_path = os.path.join(path, 'chord.wav')

        self._export_chord_inversion(chord_inversion, chord_info_path)
        self._export_midi(chord_inversion, chord_midi_path)
        self._export_audio(chord_midi_path, chord_audio_path)
