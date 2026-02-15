import mido
import numpy as np
import soundfile as sf
import random

# Define several melodic and rhythmic patterns for variety
MELODIC_PATTERNS = [
    [0, 2, 4, 5, 7, 5, 4, 2],  # Ascend and descend
    [0, 4, 7, 4, 0, 4, 7, 12], # Arpeggio
    [0, 2, 0, 5, 4, 2, 0, 7],  # Motif with repetition
    [0, 3, 5, 7, 5, 3, 0, 12], # Minor flavor
]
RHYTHM_PATTERNS = [
    [240, 240, 240, 240, 240, 240, 240, 240],
    [120, 360, 120, 360, 120, 360, 120, 360],
    [180, 180, 360, 180, 180, 360, 180, 180],
]

SECTION_ORDER = ['intro', 'main', 'main', 'main', 'outro']

SECTION_LENGTHS = {
    'intro': 4,
    'main': 8,
    'outro': 4
}

def generate_scale(key: str, is_minor: bool = False, octave: int = 4):
    key_map = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    base = key_map.get(key.replace('m','').replace('#',''), 0) + 12 * octave
    intervals = [0, 2, 3, 5, 7, 8, 10, 12] if is_minor else [0, 2, 4, 5, 7, 9, 11, 12]
    return [base + i for i in intervals]

def select_pattern(scale):
    melodic = random.choice(MELODIC_PATTERNS)
    rhythm = random.choice(RHYTHM_PATTERNS)
    notes = [scale[n % len(scale)] + (12 if n >= len(scale) else 0) for n in melodic]
    return list(zip(notes, rhythm))

def generate_song_structure(key: str, octave: int):
    is_minor = 'm' in key
    scale = generate_scale(key, is_minor, octave)
    song = []
    for section in SECTION_ORDER:
        for _ in range(SECTION_LENGTHS[section] // len(MELODIC_PATTERNS[0])):
            song.extend(select_pattern(scale))
    return song

def generate_music(tempo: int, key: str, style: str, filename: str, octave: int = 4):
    print(f"[PATTERN] Generating {style} music: tempo={tempo}, key={key}, octave={octave}, filename={filename}")
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    tempo_bpm = max(tempo, 30)
    microseconds_per_beat = mido.bpm2tempo(tempo_bpm)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))
    program = 80 if style == '8bit' else 81
    track.append(mido.Message('program_change', program=program, time=0))
    song = generate_song_structure(key, octave)
    for note, duration in song:
        track.append(mido.Message('note_on', note=note, velocity=100, time=0))
        track.append(mido.Message('note_off', note=note, velocity=100, time=duration))
    mid.save(filename if filename.endswith('.mid') else filename + '.mid')
    print(f"[MIDI] Pattern-based MIDI file written to {filename if filename.endswith('.mid') else filename + '.mid'}")

def generate_simple_wave(filename: str, duration: float = 2.0, freq: float = 440.0, samplerate: int = 44100, wave_type: str = "square"):
    """
    Generate and export a simple retro waveform (square, triangle, sawtooth, sine) as a WAV file.
    Args:
        filename (str): Output file name
        duration (float): Duration in seconds
        freq (float): Frequency in Hz
        samplerate (int): Sample rate
        wave_type (str): 'square', 'triangle', 'sawtooth', 'sine'
    """
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    if wave_type == "square":
        data = 0.5 * np.sign(np.sin(2 * np.pi * freq * t))
    elif wave_type == "triangle":
        data = 2 * np.abs(2 * (t * freq - np.floor(0.5 + t * freq))) - 1
    elif wave_type == "sawtooth":
        data = 2 * (t * freq - np.floor(0.5 + t * freq))
    else:
        data = np.sin(2 * np.pi * freq * t)
    sf.write(filename, data, samplerate)
    print(f"[AUDIO] Prototype {wave_type} wave written to {filename}")
