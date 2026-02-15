import argparse
from music import generate_music

def main():
    parser = argparse.ArgumentParser(
        description="Retro Jam: Generate retro video game music from the CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate retro game music")
    generate_parser.add_argument("-tempo", "--tempo", type=int, default=120, help="Tempo in BPM")
    generate_parser.add_argument("-key", "--key", type=str, choices=["A", "Am", "A#", "A#m", "B", "Bm", "C", "Cm", "C#", "C#m", "D", "Dm", "D#", "D#m", "E",
                                                                     "Em", "F", "Fm", "F#", "F#m", "G", "Gm", "G#", "G#m"], default="C", help="Musical key (e.g., C, Am, D#, etc.)")
    generate_parser.add_argument("-style", "--style", type=str, choices=["8bit", "16bit"], default="8bit", help="Musical style (8bit or 16bit)")
    generate_parser.add_argument("-filename", "--filename", type=str, default="output", help="Output file name")
    generate_parser.add_argument("-octave", "--octave", type=int, choices=[1, 2, 3, 4, 5, 6], default=4, help="Octave for melody (1=lowest, 6=highest)")
    generate_parser.add_argument("-repeat", "--repeat", type=int, default=3, help="Number of times to repeat the main section (default: 3)")

    # Waveform command
    wave_parser = subparsers.add_parser("wave", help="Generate a simple retro waveform as a WAV file")
    wave_parser.add_argument("-type", "--type", type=str, choices=["square", "triangle", "sawtooth", "sine"], default="square", help="Waveform type for audio export")
    wave_parser.add_argument("-filename", "--filename", type=str, default="output", help="Output file name")
    wave_parser.add_argument("-length", "--length", type=float, default=10.0, help="Song length in seconds (default: 10)")

    args = parser.parse_args()

    if args.command == "generate":
        generate_music(
            tempo=args.tempo,
            key=args.key,
            style=args.style,
            filename=args.filename,
            octave=args.octave,
            repeat=args.repeat
        )

    if args.command == "wave":
        # Audio export prototype
        from music import generate_simple_wave
        wav_out = args.filename if args.filename.endswith('.wav') else args.filename + '.wav'
        generate_simple_wave(wav_out, duration=args.length, freq=420.0, wave_type=args.type)

if __name__ == "__main__":
    main()
