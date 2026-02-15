# Melodic and rhythmic patterns for retro-jam

MELODIC_PATTERNS = [
    [0, 2, 4, 5, 7, 5, 4, 2],  # Ascend and descend
    [0, 4, 7, 4, 0, 4, 7, 12], # Arpeggio
    [0, 2, 0, 5, 4, 2, 0, 7],  # Motif with repetition
    [0, 3, 5, 7, 5, 3, 0, 12], # Minor flavor
    [0, 5, 7, 5, 0, 7, 5, 0],  # Fifth jumps
    [0, 2, 4, 7, 4, 2, 0, 12], # Up and leap
    [0, 7, 5, 4, 2, 0, 2, 4],  # Down then up
    [0, 0, 7, 7, 5, 5, 4, 4],  # Double notes
    [0, 2, 4, 2, 0, 5, 7, 5],  # Zig-zag
    [0, 3, 7, 10, 7, 3, 0, 12], # Dorian/minor
    [0, 4, 5, 7, 9, 7, 5, 4],  # Major walk
    [0, 2, 5, 9, 7, 5, 2, 0],  # Wide leaps
    [0, 7, 12, 7, 0, 5, 9, 5], # Octave jumps
    [0, 3, 5, 8, 10, 8, 5, 3], # Minor leaps
    [0, 2, 4, 5, 7, 9, 11, 12], # Full scale
    [0, 5, 9, 7, 4, 2, 0, 12], # Modal
    [0, 2, 4, 7, 9, 7, 4, 2],  # Up, leap, down
    [0, 4, 7, 11, 7, 4, 0, 12], # Major 7th
    [0, 3, 6, 10, 6, 3, 0, 12], # Diminished
    [0, 5, 8, 10, 8, 5, 0, 12], # Minor 6th
]

RHYTHM_PATTERNS = [
    # Flowing, legato with rare longer rests
    [360, 0, 480, 0, 240, 0, 360, 0, 480, 0, 360, 0, 720, 120, 240, 0],
    # Syncopated, with some ties and offbeats
    [180, 0, 360, 0, 180, 0, 540, 60, 240, 0, 360, 0, 180, 0, 480, 120],
    # Waltz-like, with longer notes and rests
    [360, 0, 240, 0, 480, 120, 360, 0, 720, 0, 240, 0, 480, 120, 360, 0],
    # Ballad: long notes, rare long rests
    [720, 0, 480, 0, 360, 0, 720, 120, 480, 0, 360, 0, 720, 120, 480, 0],
    # Groove: short bursts, then space
    [120, 0, 120, 0, 240, 0, 120, 0, 360, 60, 120, 0, 480, 120, 240, 0],
    # Swing: triplet feel, but smoother
    [240, 0, 360, 0, 240, 0, 360, 60, 240, 0, 360, 0, 240, 0, 480, 120],
    # March: even, but with some longer notes
    [240, 0, 240, 0, 480, 60, 240, 0, 240, 0, 480, 60, 240, 0, 360, 0],
    # Funky: syncopation and space
    [180, 0, 360, 0, 120, 0, 360, 60, 180, 0, 360, 0, 120, 0, 480, 120],
    # Lyrical: long, flowing lines
    [480, 0, 720, 120, 360, 0, 480, 0, 720, 120, 360, 0, 480, 0, 720, 120],
    # Chiptune: short, punchy notes and rests
    [120, 0, 120, 0, 120, 0, 120, 0, 120, 0, 120, 0, 120, 0, 120, 0],
    # Latin: syncopated, offbeat rests
    [180, 0, 120, 0, 240, 0, 180, 0, 360, 60, 120, 0, 240, 0, 360, 60],
    # Blues: shuffle feel
    [240, 0, 360, 0, 180, 0, 360, 60, 240, 0, 360, 0, 180, 0, 480, 120],
    # Techno: driving, repetitive
    [240, 0, 240, 0, 240, 0, 240, 0, 240, 0, 240, 0, 240, 0, 240, 0],
    # Reggae: offbeat emphasis
    [120, 0, 240, 0, 120, 0, 240, 0, 120, 0, 240, 0, 120, 0, 240, 0],
    # Jazz: complex, varied
    [180, 0, 360, 0, 120, 0, 540, 60, 240, 0, 360, 0, 180, 0, 480, 120],
    # Experimental: irregular
    [90, 0, 360, 0, 120, 0, 480, 60, 180, 0, 360, 0, 90, 0, 720, 120],
    # Anthemic: long, powerful notes
    [720, 0, 480, 0, 720, 0, 480, 0, 720, 0, 480, 0, 720, 0, 480, 120],
    # Minimal: sparse, lots of space
    [360, 0, 0, 360, 480, 0, 0, 480, 360, 0, 0, 360, 480, 0, 0, 480],
    # Pop: catchy, regular
    [240, 0, 240, 0, 360, 0, 240, 0, 240, 0, 360, 0, 240, 0, 360, 0],
    # Classical: flowing, dynamic
    [360, 0, 480, 0, 240, 0, 360, 0, 480, 0, 360, 0, 720, 0, 240, 0],
    # Rock: driving, energetic
    [180, 0, 360, 0, 240, 0, 360, 0, 480, 0, 360, 0, 720, 0, 240, 0],
]
