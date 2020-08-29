#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = """
stephguirand,
Help from demo, lessons and activities,
youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about
assignment in study group"""

from morse_dict import MORSE_2_ASCII
# import MORSE_2_ASCII from morse_dict


""" This function returns a Morse code string. It will transcode the binary
sequence into Morse code representation, taking into account the variable
coding speed of the key operator(transmission rate)
`time_unit` is the reciprocal of the transmission rate. """


def decode_bits(bits):
    bits = bits.strip('0')
    time_unit = min([len(bit)
                     for bit in bits.split('1') + bits.split('0') if bit])
    return bits.replace(
        '111' * time_unit, '-').replace(
            '1' * time_unit, '.').replace(
                '0000000' * time_unit, '   ').replace(
                    '000' * time_unit, ' ').replace(
                        '0' * time_unit, '')


""" This function accepts a string parameter, which consists
of '.' and '-' and ' ' characters arranged to form a morse code message.
Also will use the included MORSE_2_ASCII, mapping between Morse letters and
alphabetic characters to return an ASCII string which
represents the decoded input message."""


def decode_morse(morse):
    words = morse.split('   ')
    decode_code = ''
    for word in words:
        letters = word.split()
        for letter in letters:
            decode_code += MORSE_2_ASCII[letter]
        decode_code += ' '
    return decode_code.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
